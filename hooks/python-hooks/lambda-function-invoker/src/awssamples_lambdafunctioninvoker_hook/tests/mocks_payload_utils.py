"""Unit test mocks for PayloadUtils."""


from typing import (
    Any,
    MutableMapping,
)

from cloudformation_cli_python_lib import (  # type: ignore
    BaseHookHandlerRequest,
    HookContext,
    HookInvocationPoint,
    OperationStatus,
    ProgressEvent,
)

TYPE_CONFIGURATION_LAMBDA_FUNCTIONS_FIRST_INVOCATION = [
    "LambdaFunctionInvokerHookTest-1"
]

CALLBACK_CONTEXT_FIRST_INVOCATION: MutableMapping[str, Any] = {}

TYPE_CONFIGURATION_LAMBDA_FUNCTIONS_NEXT_INVOCATION = [
    "LambdaFunctionInvokerHookTest-1"
]

CALLBACK_CONTEXT_NEXT_INVOCATION = {
    "lambda_functions_callbacks": {
        "LambdaFunctionInvokerHookTest-1": {"test": 1}
    },
    "lambda_functions_messages": {
        "LambdaFunctionInvokerHookTest-1": "In progress"
    },
}


SINGLE_TENANT_LAMBDA_FUNCTION_FIRST_INVOCATION = (
    "LambdaFunctionInvokerHookTest-1"
)

SINGLE_TENANT_CALLBACK_CONTEXT_FIRST_INVOCATION: MutableMapping[str, Any] = {}


SINGLE_TENANT_LAMBDA_FUNCTION_NEXT_INVOCATION = (
    "LambdaFunctionInvokerHookTest-1"
)

SINGLE_TENANT_CALLBACK_CONTEXT_NEXT_INVOCATION: MutableMapping[str, Any] = {
    "lambda_functions_callbacks": {
        "LambdaFunctionInvokerHookTest-1": {"test": 1}
    },
    "lambda_functions_messages": {
        "LambdaFunctionInvokerHookTest-1": "In progress"
    },
}

MULTI_TENANT_EVENTS_FIRST_INVOCATION = [
    {
        "lambda_function": "LambdaFunctionInvokerHookTest-1",
        "progress_event": ProgressEvent(
            status=OperationStatus.IN_PROGRESS,
            errorCode=None,
            message="In progress",
            result=None,
            callbackContext={"test": 1},
            callbackDelaySeconds=0,
        ),
    }
]

MULTI_TENANT_CALLBACK_CONTEXT_FIRST_INVOCATION: MutableMapping[str, Any] = {}

MULTI_TENANT_EVENTS_NEXT_INVOCATION = [
    {
        "lambda_function": "LambdaFunctionInvokerHookTest-1",
        "progress_event": ProgressEvent(
            status=OperationStatus.SUCCESS,
            errorCode=None,
            message="(After a reinvocation of the handler) The resource is compliant.",  # noqa: E501
            result=None,
            callbackContext=None,
            callbackDelaySeconds=0,
        ),
    }
]

MULTI_TENANT_CALLBACK_CONTEXT_NEXT_INVOCATION = {
    "lambda_functions_callbacks": {
        "LambdaFunctionInvokerHookTest-1": {"test": 1}
    },
    "lambda_functions_messages": {
        "LambdaFunctionInvokerHookTest-1": "In progress"
    },
}

BUILD_INVOCATION_PAYLOAD_LAMBDA_FUNCTION = "LambdaFunctionInvokerHookTest-1"

BUILD_INVOCATION_PAYLOAD_REQUEST = BaseHookHandlerRequest(
    clientRequestToken="REDACTED",
    hookContext=HookContext(
        awsAccountId="REDACTED",
        stackId="REDACTED",
        hookTypeName="AWSSamples::LambdaFunctionInvoker::Hook",
        hookTypeVersion="00000001",
        invocationPoint=HookInvocationPoint.CREATE_PRE_PROVISION,
        targetName="AWS::S3::Bucket",
        targetType="RESOURCE",
        targetLogicalId="REDACTED",
        targetModel={"resourceProperties": {}},
        changeSetId=None,
    ),
)

BUILD_INVOCATION_PAYLOAD_CALLBACK_CONTEXT = {"test": 1}
