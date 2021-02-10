import {
    Action,
    BaseResource,
    exceptions,
    handlerEvent,
    HandlerErrorCode,
    OperationStatus,
    Optional,
    ProgressEvent,
    ResourceHandlerRequest,
    SessionProxy,
} from 'cfn-rpdk';
import { ResourceModel } from './models';
import AWS from 'aws-sdk'
import { v4 as uuidv4 } from 'uuid'
import { getTemplate } from './devinstance'
import { env } from 'process'

interface CallbackContext extends Record<string, any> { }

function getCfClient(session: Optional<SessionProxy>) {
    if (env.HY_OVERRIDE_CREDENTIALS === "yes") {
        console.log('use override credentials')
        AWS.config.accessKeyId = env.HY_ACCESS_KEY_ID
        AWS.config.secretAccessKey = env.HY_SECRET_ACCESS_KEY
        return new AWS.CloudFormation()
    }

    const plainSession = session as any
    if (plainSession.options.credentials.secretAccessKey) {
        var cf = session.client("CloudFormation") as AWS.CloudFormation
        console.log("use provided credentials")
    } else {
        var cf = new AWS.CloudFormation()
        console.log("use local credentials")
    }

    return cf
}

function createErrorProgressEvent(err: any, code?: HandlerErrorCode): ProgressEvent {
    code = code || HandlerErrorCode.GeneralServiceException
    const progress = ProgressEvent.failed(code, `${err.code}: ${err.message}`)
    console.log(progress)
    return progress
}

function cfFailed(stackStatus: string): boolean {
    return ["UPDATE_ROLLBACK_COMPLETE", "ROLLBACK_IN_PROGRESS", "ROLLBACK_COMPLETE", "CREATE_FAILED", "ROLLBACK_FAILED", "DELETE_FAILED", "UPDATE_ROLLBACK_FAILED", "IMPORT_ROLLBACK_FAILED"].includes(stackStatus)
}

function emptyContext(progress: ProgressEvent<ResourceModel>) {
    const ctx = {}
    progress.callbackContext = ctx
    return ctx
}

function setContext(progress: ProgressEvent<ResourceModel>, ctx: CallbackContext) {
    progress.callbackContext = ctx
    return ctx
}

async function getResourceModelFromStack(session: Optional<SessionProxy>, stackName: string): Promise<ResourceModel> {
    if (stackName === undefined || stackName === "") {
        const err = new Error("Empty UID does not exist") as any
        err.code = "ValidationError"
        throw err
    }
    const response: AWS.CloudFormation.DescribeStacksOutput = await getCfClient(session).describeStacks({ StackName: stackName }).promise()

    const outputs = response.Stacks[0].Outputs.reduce((map: any, item) => {
        map[item.OutputKey] = item.OutputValue
        return map
    }, {})

    const props = response.Stacks[0].Parameters.reduce((map: any, item) => {
        map[item.ParameterKey] = item.ParameterValue
        return map
    }, {})

    return new ResourceModel(
        {
            UID: stackName,
            InstanceType: props.instanceType,
            DiskSize: parseInt(props.diskSize) as number,
            Keypair: props.keypair,
            SSH: outputs.ssh
        }
    )
}

function getStackParametersFromModel(model: ResourceModel): AWS.CloudFormation.Parameters {
    return [
        { ParameterKey: "keypair", ParameterValue: model.Keypair },
        { ParameterKey: "instanceType", ParameterValue: model.InstanceType },
        { ParameterKey: "diskSize", ParameterValue: model.DiskSize.toString() }
    ]
}

function debugLog(action: Action, request: ResourceHandlerRequest<ResourceModel>, callbackContext: CallbackContext) {
    console.log(action + " -----------------")
    console.log("Request: " + JSON.stringify(request))
    console.log("Context: " + JSON.stringify(callbackContext))
}

class Resource extends BaseResource<ResourceModel> {

    /**
     * CloudFormation invokes this handler when the resource is initially created
     * during stack create operations.
     *
     * @param session Current AWS session passed through from caller
     * @param request The request object for the provisioning request passed to the implementor
     * @param callbackContext Custom context object to enable handlers to process re-invocation
     */
    @handlerEvent(Action.Create)
    public async create(
        session: Optional<SessionProxy>,
        request: ResourceHandlerRequest<ResourceModel>,
        callbackContext: CallbackContext,
    ): Promise<ProgressEvent> {
        const model = new ResourceModel(request.desiredResourceState);
        const progress: ProgressEvent<ResourceModel> = ProgressEvent.builder()
            .status(OperationStatus.InProgress)
            .resourceModel(model)
            .callbackContext(callbackContext)
            .build() as ProgressEvent<ResourceModel>;

        debugLog(Action.Create, request, callbackContext)

        const state = callbackContext.state

        if (state === "creating") {
            const uuid: string = model.UID
            const response = await getCfClient(session).describeStacks({ StackName: uuid }).promise()
            const stack = response.Stacks[0]
            if (stack.StackStatus === "CREATE_COMPLETE") {
                const outputs = stack.Outputs.reduce((map: any, item) => {
                    map[item.OutputKey] = item.OutputValue
                    return map
                }, {})
                model.SSH = outputs.ssh
                progress.status = OperationStatus.Success
                emptyContext(progress)
            } else if (cfFailed(stack.StackStatus)) {
                emptyContext(progress)
                return createErrorProgressEvent(new Error(stack.StackStatus + ": " + stack.StackStatusReason), HandlerErrorCode.InvalidRequest)
            }

        } else {

            try {
                if (model.SSH !== undefined || model.UID !== undefined) {
                    return createErrorProgressEvent(new Error("The SSH and UID properties are read-only."), HandlerErrorCode.InvalidRequest)
                }
                const uuid: string = "DevInstance-" + uuidv4()
                const parameters = getStackParametersFromModel(model)
                const template = JSON.stringify(getTemplate())
                await getCfClient(session).createStack({ StackName: uuid, Parameters: parameters, Capabilities: ["CAPABILITY_IAM"], TemplateBody: template }).promise()
                setContext(progress, {
                    state: "creating"
                })
                model.UID = uuid
            } catch (err) {
                emptyContext(progress)
                return createErrorProgressEvent(err, HandlerErrorCode.InvalidRequest)
            }

        }
        console.log(progress)
        return progress


    }

    /**
     * CloudFormation invokes this handler when the resource is updated
     * as part of a stack update operation.
     *
     * @param session Current AWS session passed through from caller
     * @param request The request object for the provisioning request passed to the implementor
     * @param callbackContext Custom context object to enable handlers to process re-invocation
     */
    @handlerEvent(Action.Update)
    public async update(
        session: Optional<SessionProxy>,
        request: ResourceHandlerRequest<ResourceModel>,
        callbackContext: CallbackContext,
    ): Promise<ProgressEvent> {
        const model: ResourceModel = request.desiredResourceState;
        const progress: ProgressEvent<ResourceModel> = ProgressEvent.builder()
            .status(OperationStatus.InProgress)
            .resourceModel(model)
            .callbackContext(callbackContext)
            .build() as ProgressEvent<ResourceModel>

        debugLog(Action.Update, request, callbackContext)

        const state = callbackContext.state

        if (state === "updating") {
            const response = await getCfClient(session).describeStacks({ StackName: model.UID }).promise()
            const stack = response.Stacks[0]
            if (stack.StackStatus === "UPDATE_COMPLETE") {
                progress.status = OperationStatus.Success
                emptyContext(progress)
            } else if (cfFailed(stack.StackStatus)) {
                emptyContext(progress)
                return createErrorProgressEvent(new Error(stack.StackStatus + ": " + stack.StackStatusReason))
            }

        } else {

            try {
                if (model.UID === undefined || model.UID === "") {
                    const err = new Error("Empty UID does not exist") as any
                    err.code = "ValidationError"
                    throw err
                }
                const parameters = getStackParametersFromModel(model)
                const template = JSON.stringify(getTemplate())
                await getCfClient(session).updateStack({ StackName: model.UID, Parameters: parameters, Capabilities: ["CAPABILITY_IAM"], TemplateBody: template }).promise()
                setContext(progress, {
                    state: "updating"
                })
            } catch (err) {
                emptyContext(progress)
                if (err.code === "ValidationError" && err.message.includes("does not exist")) {
                    return createErrorProgressEvent(err, HandlerErrorCode.NotFound)
                } else {
                    return createErrorProgressEvent(err)
                }
            }
        }
        console.log(progress)
        return progress


    }

    /**
     * CloudFormation invokes this handler when the resource is deleted, either when
     * the resource is deleted from the stack as part of a stack update operation,
     * or the stack itself is deleted.
     *
     * @param session Current AWS session passed through from caller
     * @param request The request object for the provisioning request passed to the implementor
     * @param callbackContext Custom context object to enable handlers to process re-invocation
     */
    @handlerEvent(Action.Delete)
    public async delete(
        session: Optional<SessionProxy>,
        request: ResourceHandlerRequest<ResourceModel>,
        callbackContext: CallbackContext,
    ): Promise<ProgressEvent> {
        const model: ResourceModel = request.desiredResourceState;
        const progress: ProgressEvent<ResourceModel> = ProgressEvent.builder()
            .status(OperationStatus.InProgress)
            .callbackContext(callbackContext)
            .build() as ProgressEvent<ResourceModel>

        debugLog(Action.Delete, request, callbackContext)

        const state = callbackContext.state
        var uuid: string

        if (state === "deleting") {
            uuid = callbackContext.uid
            try {
                const response = await getCfClient(session).describeStacks({ StackName: uuid }).promise()
                const stack = response.Stacks[0]
                if (stack.StackStatus === "DELETE_COMPLETE") {
                    progress.status = OperationStatus.Success
                    emptyContext(progress)
                } else if (cfFailed(stack.StackStatus)) {
                    emptyContext(progress)
                    return createErrorProgressEvent(new Error(stack.StackStatus + ": " + stack.StackStatusReason))
                }
            } catch (err) {
                emptyContext(progress)
                if (err.code === "ValidationError" && err.message.includes("does not exist")) {
                    progress.status = OperationStatus.Success
                } else {
                    return createErrorProgressEvent(err)
                }
            }

        } else {
            uuid = model.UID
            try {
                const response = await getCfClient(session).describeStacks({ StackName: uuid }).promise()
                const stack = response.Stacks[0]
                if (stack.StackStatus === "DELETE_COMPLETE") {
                    emptyContext(progress)
                    return createErrorProgressEvent(new Error("Already deleted."), HandlerErrorCode.NotFound)
                }
                await getCfClient(session).deleteStack({ StackName: uuid }).promise()
                setContext(progress, {
                    state: "deleting",
                    uid: uuid
                })
            } catch (err) {
                emptyContext(progress)
                return createErrorProgressEvent(err, HandlerErrorCode.NotFound)
            }

        }
        if (progress.status === OperationStatus.InProgress) {
            const minimalModel = new ResourceModel()
            minimalModel.UID = uuid
            progress.resourceModel = minimalModel
        }

        console.log(progress)
        return progress

    }

    /**
     * CloudFormation invokes this handler as part of a stack update operation when
     * detailed information about the resource's current state is required.
     *
     * @param session Current AWS session passed through from caller
     * @param request The request object for the provisioning request passed to the implementor
     * @param callbackContext Custom context object to enable handlers to process re-invocation
     */
    @handlerEvent(Action.Read)
    public async read(
        session: Optional<SessionProxy>,
        request: ResourceHandlerRequest<ResourceModel>,
        callbackContext: CallbackContext,
    ): Promise<ProgressEvent> {

        debugLog(Action.Read, request, callbackContext)
        /*
                const test = new ResourceModel(
                    {
                        UID: "stackName",
                        InstanceType: "props",
                        DiskSize: 100,
                        Keypair: "dev",
                        SSH: "url"
                    }
                )
                console.log(test)
        */
        try {
            const model: ResourceModel = await getResourceModelFromStack(session, request.desiredResourceState.UID)
            const progress: ProgressEvent<ResourceModel> = ProgressEvent.builder()
                .status(OperationStatus.Success)
                .resourceModel(model)
                .callbackContext(callbackContext)
                .build() as ProgressEvent<ResourceModel>

            console.log(progress)
            return progress

        } catch (err) {
            if (err.code === "ValidationError" && err.message.includes("does not exist")) {
                return createErrorProgressEvent(err, HandlerErrorCode.NotFound)
            } else {
                return createErrorProgressEvent(err)
            }
        }


    }

    /**
     * CloudFormation invokes this handler when summary information about multiple
     * resources of this resource provider is required.
     *
     * @param session Current AWS session passed through from caller
     * @param request The request object for the provisioning request passed to the implementor
     * @param callbackContext Custom context object to enable handlers to process re-invocation
     */
    @handlerEvent(Action.List)
    public async list(
        session: Optional<SessionProxy>,
        request: ResourceHandlerRequest<ResourceModel>,
        callbackContext: CallbackContext,
    ): Promise<ProgressEvent> {

        debugLog(Action.List, request, callbackContext)

        const stacks = await getCfClient(session).listStacks({}).promise()

        const results = stacks.StackSummaries
            .filter((stack: AWS.CloudFormation.StackSummary) => {
                return stack.StackName.includes("DevInstance-") && !["DELETE_COMPLETE"].includes(stack.StackStatus)
            })
            .map(async (summary: AWS.CloudFormation.StackSummary) => {
                return await getResourceModelFromStack(session, summary.StackName)
            })

        const models: Array<ResourceModel> = await Promise.all(results)

        const progress: ProgressEvent<ResourceModel> = ProgressEvent.builder()
            .status(OperationStatus.Success)
            .resourceModels(models)
            .callbackContext(callbackContext)
            .build() as ProgressEvent<ResourceModel>

        console.log(progress)
        return progress;
    }
}


const resource = new Resource(ResourceModel.TYPE_NAME, ResourceModel);

export const entrypoint = resource.entrypoint;

export const testEntrypoint = resource.testEntrypoint;
