"""Unit test mocks for ResultsEvaluator."""


from cloudformation_cli_python_lib import (  # type: ignore
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
)

HAS_FAILED_NON_COMPLIANT = [
    {
        "lambda_function": "LambdaFunctionInvokerHookTest-1",
        "progress_event": ProgressEvent(
            status=OperationStatus.SUCCESS,
            errorCode=None,
            message="The resource is compliant.",
            callbackContext=None,
            callbackDelaySeconds=0,
        ),
    },
    {
        "lambda_function": "LambdaFunctionInvokerHookTest-2",
        "progress_event": ProgressEvent(
            status=OperationStatus.FAILED,
            errorCode=HandlerErrorCode.NonCompliant,
            message="The resource is not compliant.",
            callbackContext=None,
            callbackDelaySeconds=0,
        ),
    },
]

HAS_SUCCESS = [
    {
        "lambda_function": "LambdaFunctionInvokerHookTest-1",
        "progress_event": ProgressEvent(
            status=OperationStatus.SUCCESS,
            errorCode=None,
            message="The resource is compliant.",
            callbackContext=None,
            callbackDelaySeconds=0,
        ),
    },
    {
        "lambda_function": "LambdaFunctionInvokerHookTest-2",
        "progress_event": ProgressEvent(
            status=OperationStatus.SUCCESS,
            errorCode=None,
            message="The resource is compliant.",
            callbackContext=None,
            callbackDelaySeconds=0,
        ),
    },
]

HAS_IN_PROGRESS = [
    {
        "lambda_function": "LambdaFunctionInvokerHookTest-1",
        "progress_event": ProgressEvent(
            status=OperationStatus.SUCCESS,
            errorCode=None,
            message="The resource is compliant.",
            callbackContext=None,
            callbackDelaySeconds=0,
        ),
    },
    {
        "lambda_function": "LambdaFunctionInvokerHookTest-2",
        "progress_event": ProgressEvent(
            status=OperationStatus.IN_PROGRESS,
            errorCode=None,
            message="The resource is being evaluated.",
            callbackContext={"key": "value"},
            callbackDelaySeconds=1,
        ),
    },
]

HAS_MULTIPLE_IN_PROGRESS = [
    {
        "lambda_function": "LambdaFunctionInvokerHookTest-1",
        "progress_event": ProgressEvent(
            status=OperationStatus.IN_PROGRESS,
            errorCode=None,
            message="The resource is being evaluated.",
            callbackContext={"key": "value"},
            callbackDelaySeconds=1,
        ),
    },
    {
        "lambda_function": "LambdaFunctionInvokerHookTest-2",
        "progress_event": ProgressEvent(
            status=OperationStatus.IN_PROGRESS,
            errorCode=None,
            message="The resource is being evaluated.",
            callbackContext={"key": "value"},
            callbackDelaySeconds=3,
        ),
    },
]
