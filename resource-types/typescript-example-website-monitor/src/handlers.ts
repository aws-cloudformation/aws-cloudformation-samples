import {
    Action,
    BaseResource,
    exceptions,
    handlerEvent,
    HandlerErrorCode,
    integer,
    Integer,
    LoggerProxy,
    OperationStatus,
    Optional,
    ProgressEvent,
    ResourceHandlerRequest,
    SessionProxy
} from 'cfn-rpdk';
import fetch, { Response } from 'node-fetch';

import { ResourceModel } from './models';

interface CallbackContext extends Record<string, any> {}

enum ApiEndpoints {
    US = 'https://synthetics.newrelic.com/synthetics/api',
    EU = 'https://synthetics.eu.newrelic.com/synthetics/api',
}

type EndpointRegions = keyof typeof ApiEndpoints;

interface Monitor {
    readonly id?: string;
    readonly name?: string;
    readonly uri?: string;
    readonly type?: string;
    readonly frequency?: integer;
    readonly status?: string;
    readonly locations?: string[];
    readonly slaThreshold?: number;
}

/**
 * Resource to be used in AWS CloudFormation to create and manage
 * New Relic's synthetic monitors of type "ping" (SIMPLE).
 * See documentation {@link https://docs.newrelic.com/docs/apis/synthetics-rest-api/monitor-examples/manage-synthetics-monitors-rest-api}.
 */
class Resource extends BaseResource<ResourceModel> {
    static readonly DEFAULT_HEADERS = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    };
    static readonly DEFAULT_MONITOR_KIND = 'SIMPLE';
    static readonly DEFAULT_MONITOR_STATUS = 'MUTED';
    static readonly DEFAULT_MONITOR_LOCATIONS = [
        'AWS_EU_CENTRAL_1',
        'AWS_US_WEST_1'
    ];
    static readonly DEFAULT_MONITOR_SLA_THRESHOLD = 7.0;

    private async checkResponse(response: Response, logger: LoggerProxy, uid?: string): Promise<any> {
        if (response.status === 400) {
            throw new exceptions.AlreadyExists(this.typeName, uid);
        } else if (response.status === 401) {
            throw new exceptions.AccessDenied(response.statusText);
        } else if (response.status === 404) {
            throw new exceptions.NotFound(this.typeName, uid);
        } else if (response.status > 400) {
            throw new exceptions.InternalFailure(
                `error ${response.status} ${response.statusText}`,
                HandlerErrorCode.InternalFailure,
            );
        }
        const responseData = await response.text() || '{}';
        logger.log('HTTP response', responseData);
        return JSON.parse(responseData);
    }

    /**
     * CloudFormation invokes this handler when the resource is initially created
     * during stack create operations.
     *
     * @param session Current AWS session passed through from caller
     * @param request The request object for the provisioning request passed to the implementor
     * @param callbackContext Custom context object to allow the passing through of additional
     * state or metadata between subsequent retries
     * @param logger Logger to proxy requests to default publishers
     */
    @handlerEvent(Action.Create)
    public async create(
        session: Optional<SessionProxy>,
        request: ResourceHandlerRequest<ResourceModel>,
        callbackContext: CallbackContext,
        logger: LoggerProxy
    ): Promise<ProgressEvent> {
        logger.log('request', request);
        
        // It is important that we create a new instance of the model,
        // because the desired state is immutable.
        const model = new ResourceModel(request.desiredResourceState);
        const progress = ProgressEvent.progress<ProgressEvent<ResourceModel>>(model);

        // Id is a read only property, which means that
        // it cannot be set during creation or update operations.
        if (model.id) {
            throw new exceptions.InvalidRequest('Read only property [Id] cannot be provided by the user.');
        }

        try {
            // Set or fallback to default values
            model.frequency = model.frequency || Integer(5);
            model.endpointRegion = model.endpointRegion || 'US';
            model.kind = Resource.DEFAULT_MONITOR_KIND;
            model.status = Resource.DEFAULT_MONITOR_STATUS;
            model.locations = Resource.DEFAULT_MONITOR_LOCATIONS;
            model.slaThreshold = Resource.DEFAULT_MONITOR_SLA_THRESHOLD;

            // Create a new synthetics monitor
            // https://docs.newrelic.com/docs/apis/synthetics-rest-api/monitor-examples/manage-synthetics-monitors-rest-api#create-monitor
            const apiKey = model.apiKey;
            const apiEndpoint = ApiEndpoints[model.endpointRegion as EndpointRegions];
            const createResponse: Response = await fetch(`${apiEndpoint}/v3/monitors`, {
                method: 'POST',
                headers: { ...Resource.DEFAULT_HEADERS, 'Api-Key': apiKey },
                body: JSON.stringify({
                    name: model.name,
                    uri: model.uri,
                    type: model.kind,
                    frequency: model.frequency,
                    status: model.status,
                    locations: model.locations,
                    slaThreshold: model.slaThreshold
                } as Monitor)
            });
            await this.checkResponse(createResponse, logger, request.logicalResourceIdentifier);

            // Use address from location header to read newly created monitor
            // https://docs.newrelic.com/docs/apis/synthetics-rest-api/monitor-examples/manage-synthetics-monitors-rest-api#get-specific-monitor
            const locationUrl = createResponse.headers.get('location');
            if (!locationUrl) {
                throw new exceptions.NotFound(this.typeName, request.logicalResourceIdentifier);
            }
            const response: Response = await fetch(locationUrl, {
                method: 'GET',
                headers: { ...Resource.DEFAULT_HEADERS, 'Api-Key': apiKey }
            });
            const monitor: Monitor = await this.checkResponse(response, logger, request.logicalResourceIdentifier);
            model.id = monitor.id;
            // model.apiKey = null;

            // Setting Status to success will signal to CloudFormation that the operation is complete
            progress.status = OperationStatus.Success;
        } catch(err) {
            logger.log(err);
            if (err instanceof exceptions.BaseHandlerException) {
                throw err;
            }
            throw new exceptions.InternalFailure(err.message);
        }
        logger.log('progress', progress);
        return progress;
    }

    /**
     * CloudFormation invokes this handler when the resource is updated
     * as part of a stack update operation.
     *
     * @param session Current AWS session passed through from caller
     * @param request The request object for the provisioning request passed to the implementor
     * @param callbackContext Custom context object to allow the passing through of additional
     * state or metadata between subsequent retries
     * @param logger Logger to proxy requests to default publishers
     */
    @handlerEvent(Action.Update)
    public async update(
        session: Optional<SessionProxy>,
        request: ResourceHandlerRequest<ResourceModel>,
        callbackContext: CallbackContext,
        logger: LoggerProxy
    ): Promise<ProgressEvent> {
        logger.log('request', request);
        const model = new ResourceModel(request.desiredResourceState);
        const { id, name } = request.previousResourceState;

        if (!model.id) {
            throw new exceptions.NotFound(this.typeName, request.logicalResourceIdentifier);
        } else if (model.id !== id) {
            logger.log(this.typeName, `[NEW ${model.id}] [${request.logicalResourceIdentifier}] does not match identifier from saved resource [OLD ${id}].`);
            throw new exceptions.NotUpdatable('Read only property [Id] cannot be updated.');
        } else if (model.name !== name) {
            // The Name is a create only property, which means that it cannot be updated.
            logger.log(this.typeName, `[NEW ${model.name}] [${request.logicalResourceIdentifier}] does not match identifier from saved resource [OLD ${name}].`);
            throw new exceptions.NotUpdatable('Create only property [Name] cannot be updated.');
        }

        try {
            // Set or fallback to default values
            model.frequency = model.frequency || Integer(5);
            model.endpointRegion = model.endpointRegion || 'US';
            model.kind = Resource.DEFAULT_MONITOR_KIND;
            model.status = Resource.DEFAULT_MONITOR_STATUS;
            model.locations = Resource.DEFAULT_MONITOR_LOCATIONS;
            model.slaThreshold = Resource.DEFAULT_MONITOR_SLA_THRESHOLD;

            // Update the synthetics monitor by calling the endpoint with its ID.
            // https://docs.newrelic.com/docs/apis/synthetics-rest-api/monitor-examples/manage-synthetics-monitors-rest-api#update-monitor
            const apiKey = model.apiKey;
            const apiEndpoint = ApiEndpoints[model.endpointRegion as EndpointRegions];
            const response: Response = await fetch(`${apiEndpoint}/v3/monitors/${id}`, {
                method: 'PUT',
                headers: { ...Resource.DEFAULT_HEADERS, 'Api-Key': apiKey },
                body: JSON.stringify({
                    name,
                    uri: model.uri,
                    type: model.kind,
                    frequency: model.frequency,
                    status: model.status,
                    locations: model.locations,
                    slaThreshold: model.slaThreshold
                } as Monitor)
            });
            await this.checkResponse(response, logger, id);
            // model.apiKey = null;

            const progress = ProgressEvent.success<ProgressEvent<ResourceModel>>(model);
            logger.log('progress', progress);
            return progress;
        } catch(err) {
            logger.log(err);
            if (err instanceof exceptions.BaseHandlerException) {
                throw err;
            }
            return ProgressEvent.failed<ProgressEvent<ResourceModel>>(HandlerErrorCode.InternalFailure, err.message);
        }
    }

    /**
     * CloudFormation invokes this handler when the resource is deleted, either when
     * the resource is deleted from the stack as part of a stack update operation,
     * or the stack itself is deleted.
     *
     * @param session Current AWS session passed through from caller
     * @param request The request object for the provisioning request passed to the implementor
     * @param callbackContext Custom context object to allow the passing through of additional
     * state or metadata between subsequent retries
     * @param logger Logger to proxy requests to default publishers
     */
    @handlerEvent(Action.Delete)
    public async delete(
        session: Optional<SessionProxy>,
        request: ResourceHandlerRequest<ResourceModel>,
        callbackContext: CallbackContext,
        logger: LoggerProxy
    ): Promise<ProgressEvent> {
        logger.log('request', request);
        const model = new ResourceModel(request.desiredResourceState);

        // The Id property, being the primary identifier, cannot be left empty.
        if (!model.id) {
            throw new exceptions.NotFound(this.typeName, request.logicalResourceIdentifier);
        }

        // Remove the synthetics monitor by calling the delete endpoint with its ID.
        // https://docs.newrelic.com/docs/apis/synthetics-rest-api/monitor-examples/manage-synthetics-monitors-rest-api#delete-monitor
        model.endpointRegion = model.endpointRegion || 'US';
        const apiEndpoint = ApiEndpoints[model.endpointRegion as EndpointRegions];
        const response: Response = await fetch(`${apiEndpoint}/v3/monitors/${model.id}`, {
            method: 'DELETE',
            headers: { ...Resource.DEFAULT_HEADERS, 'Api-Key': model.apiKey }
        });
        await this.checkResponse(response, logger, model.id);

        const progress = ProgressEvent.success<ProgressEvent<ResourceModel>>();
        logger.log('progress', progress);
        return progress;
    }

    /**
     * CloudFormation invokes this handler as part of a stack update operation when
     * detailed information about the resource's current state is required.
     *
     * @param session Current AWS session passed through from caller
     * @param request The request object for the provisioning request passed to the implementor
     * @param callbackContext Custom context object to allow the passing through of additional
     * state or metadata between subsequent retries
     * @param logger Logger to proxy requests to default publishers
     */
    @handlerEvent(Action.Read)
    public async read(
        session: Optional<SessionProxy>,
        request: ResourceHandlerRequest<ResourceModel>,
        callbackContext: CallbackContext,
        logger: LoggerProxy
    ): Promise<ProgressEvent> {
        logger.log('request', request);
        const model = new ResourceModel(request.desiredResourceState);

        if (!model.id) {
            throw new exceptions.NotFound(this.typeName, request.logicalResourceIdentifier);
        }

        model.kind = Resource.DEFAULT_MONITOR_KIND;
        model.status = Resource.DEFAULT_MONITOR_STATUS;
        model.locations = Resource.DEFAULT_MONITOR_LOCATIONS;
        model.slaThreshold = Resource.DEFAULT_MONITOR_SLA_THRESHOLD;

        const progress = ProgressEvent.success<ProgressEvent<ResourceModel>>(model);
        logger.log('progress', progress);
        return progress;
    }
}

export const resource = new Resource(ResourceModel.TYPE_NAME, ResourceModel);

// Entrypoint for production usage after registered in CloudFormation
export const entrypoint = resource.entrypoint;

// Entrypoint used for local testing purpose
export const testEntrypoint = resource.testEntrypoint;
