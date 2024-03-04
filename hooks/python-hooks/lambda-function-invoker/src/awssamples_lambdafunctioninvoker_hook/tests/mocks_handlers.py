"""Unit test mocks for handlers."""


import uuid
from typing import (
    Any,
    MutableMapping,
)

from cloudformation_cli_python_lib import (  # type: ignore
    HandlerErrorCode,
    HookContext,
    HookInvocationPoint,
    OperationStatus,
    ProgressEvent,
)

from .. import handlers
from ..models import (
    HookHandlerRequest,
    TypeConfigurationModel,
)

ACCOUNT_ID = "111122223333"
ARN_SUFFIX = uuid.uuid4()
CALLBACK_CONTEXT: MutableMapping[str, Any] = {}
HOOK_TYPE_VERSION = "00000001"
REGION = "us-east-1"
STACK_NAME = "lambda-invoker-test-stack"
TARGET = "AWS::S3::Bucket"
TARGET_LOGICAL_ID = "TestS3Bucket"
UNSUPPORTED_TARGET = "Unsupported::Test::Target"
UNSUPPORTED_TARGET_LOGICAL_ID = "TestUnsupportedTarget"

STACK_ID = f"arn:aws:cloudformation:{REGION}::stack/{STACK_NAME}/{ARN_SUFFIX}"

HOOK_HANDLER_REQUEST_UNSUPPORTED_TARGET = HookHandlerRequest(
    clientRequestToken=str(uuid.uuid4()),
    hookContext=HookContext(
        awsAccountId=ACCOUNT_ID,
        hookTypeName=handlers.TYPE_NAME,
        hookTypeVersion=HOOK_TYPE_VERSION,
        invocationPoint=HookInvocationPoint.CREATE_PRE_PROVISION,
        stackId=STACK_ID,
        targetLogicalId=UNSUPPORTED_TARGET_LOGICAL_ID,
        targetModel=None,
        targetName=UNSUPPORTED_TARGET,
        targetType=UNSUPPORTED_TARGET,
    ),
)

HOOK_HANDLER_REQUEST = HookHandlerRequest(
    clientRequestToken=str(uuid.uuid4()),
    hookContext=HookContext(
        awsAccountId=ACCOUNT_ID,
        hookTypeName=handlers.TYPE_NAME,
        hookTypeVersion=HOOK_TYPE_VERSION,
        invocationPoint=HookInvocationPoint.CREATE_PRE_PROVISION,
        stackId=STACK_ID,
        targetLogicalId=TARGET_LOGICAL_ID,
        targetModel=None,
        targetName=TARGET,
        targetType=TARGET,
    ),
)

TYPE_CONFIGURATION_NO_LAMBDA_FUNCTION = TypeConfigurationModel(
    LambdaFunctions=[],
)

TYPE_CONFIGURATION_1_LAMBDA_FUNCTION = TypeConfigurationModel(
    LambdaFunctions=[
        "MockLambdaFunctionName1",
    ]
)

TYPE_CONFIGURATION_2_LAMBDA_FUNCTIONS = TypeConfigurationModel(
    LambdaFunctions=[
        "MockLambdaFunctionName1",
        "MockLambdaFunctionName2",
    ]
)

TYPE_CONFIGURATION_4_LAMBDA_FUNCTIONS = TypeConfigurationModel(
    LambdaFunctions=[
        "MockLambdaFunctionName1",
        "MockLambdaFunctionName2",
        "MockLambdaFunctionName3",
        "MockLambdaFunctionName4",
    ]
)

RESPONSE_FAILED_NON_COMPLIANT_1_LAMBDA_FUNCTION = [
    {
        "lambda_function": "MockLambdaFunctionName1",
        "progress_event": ProgressEvent(
            status=OperationStatus.FAILED,
            errorCode=HandlerErrorCode.NonCompliant,
            message="The resource is not compliant.",
            result=None,
            callbackContext=None,
            callbackDelaySeconds=0,
        ),
    },
]

RESPONSE_FAILED_NON_COMPLIANT_2_LAMBDA_FUNCTIONS = [
    {
        "lambda_function": "MockLambdaFunctionName1",
        "progress_event": ProgressEvent(
            status=OperationStatus.FAILED,
            errorCode=HandlerErrorCode.NonCompliant,
            message="The resource is not compliant.",
            result=None,
            callbackContext=None,
            callbackDelaySeconds=0,
        ),
    },
    {
        "lambda_function": "MockLambdaFunctionName2",
        "progress_event": ProgressEvent(
            status=OperationStatus.FAILED,
            errorCode=HandlerErrorCode.NonCompliant,
            message="The resource is not compliant.",
            result=None,
            callbackContext=None,
            callbackDelaySeconds=0,
        ),
    },
]

RESPONSE_SUCCESS_1_LAMBDA_FUNCTION = [
    {
        "lambda_function": "MockLambdaFunctionName1",
        "progress_event": ProgressEvent(
            status=OperationStatus.SUCCESS,
            errorCode=None,
            message="The resource is compliant.",
            result=None,
            callbackContext=None,
            callbackDelaySeconds=0,
        ),
    },
]

RESPONSE_SUCCESS_2_LAMBDA_FUNCTIONS = [
    {
        "lambda_function": "MockLambdaFunctionName1",
        "progress_event": ProgressEvent(
            status=OperationStatus.SUCCESS,
            errorCode=None,
            message="The resource is compliant.",
            result=None,
            callbackContext=None,
            callbackDelaySeconds=0,
        ),
    },
    {
        "lambda_function": "MockLambdaFunctionName2",
        "progress_event": ProgressEvent(
            status=OperationStatus.SUCCESS,
            errorCode=None,
            message="The resource is compliant.",
            result=None,
            callbackContext=None,
            callbackDelaySeconds=0,
        ),
    },
]

RESPONSE_IN_PROGRESS_1_LAMBDA_FUNCTION = [
    {
        "lambda_function": "MockLambdaFunctionName1",
        "progress_event": ProgressEvent(
            status=OperationStatus.IN_PROGRESS,
            errorCode=None,
            message="The resource is being evaluated.",
            result=None,
            callbackContext={"key1": "value1"},
            callbackDelaySeconds=0,
        ),
    },
]

RESPONSE_IN_PROGRESS_2_LAMBDA_FUNCTIONS = [
    {
        "lambda_function": "MockLambdaFunctionName1",
        "progress_event": ProgressEvent(
            status=OperationStatus.IN_PROGRESS,
            errorCode=None,
            message="The resource is being evaluated.",
            result=None,
            callbackContext={"key1": "value1"},
            callbackDelaySeconds=0,
        ),
    },
    {
        "lambda_function": "MockLambdaFunctionName2",
        "progress_event": ProgressEvent(
            status=OperationStatus.IN_PROGRESS,
            errorCode=None,
            message="The resource is being evaluated.",
            result=None,
            callbackContext={"key2": "value2"},
            callbackDelaySeconds=0,
        ),
    },
]

RESPONSE_LAMBDA_FUNCTIONS_WITH_1_OR_MORE_FAILED = [
    {
        "lambda_function": "MockLambdaFunctionName1",
        "progress_event": ProgressEvent(
            status=OperationStatus.IN_PROGRESS,
            errorCode=None,
            message="The resource is being evaluated.",
            result=None,
            callbackContext={"key1": "value1"},
            callbackDelaySeconds=0,
        ),
    },
    {
        "lambda_function": "MockLambdaFunctionName2",
        "progress_event": ProgressEvent(
            status=OperationStatus.FAILED,
            errorCode=HandlerErrorCode.NonCompliant,
            message="The resource is not compliant.",
            result=None,
            callbackContext=None,
            callbackDelaySeconds=0,
        ),
    },
    {
        "lambda_function": "MockLambdaFunctionName3",
        "progress_event": ProgressEvent(
            status=OperationStatus.SUCCESS,
            errorCode=None,
            message="The resource is compliant.",
            result=None,
            callbackContext=None,
            callbackDelaySeconds=0,
        ),
    },
    {
        "lambda_function": "MockLambdaFunctionName4",
        "progress_event": ProgressEvent(
            status=OperationStatus.FAILED,
            errorCode=HandlerErrorCode.NonCompliant,
            message="The resource is not compliant.",
            result=None,
            callbackContext=None,
            callbackDelaySeconds=0,
        ),
    },
]

CALLBACK_CONTEXT_2_LAMBDA_FUNCTIONS = {
    "lambda_functions_callbacks": {
        "MockLambdaFunctionName1": {"key1": "value1"},
        "MockLambdaFunctionName2": {"key2": "value2"},
    },
    "lambda_functions_messages": {
        "MockLambdaFunctionName1": "The resource is being evaluated.",
        "MockLambdaFunctionName2": "The resource is being evaluated.",
    },
}
