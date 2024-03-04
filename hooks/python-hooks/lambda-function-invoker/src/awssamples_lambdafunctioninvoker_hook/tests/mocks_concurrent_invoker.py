"""Unit test mocks for ConcurrentInvoker."""


import json
from io import BytesIO

from botocore.response import StreamingBody  # type: ignore
from cloudformation_cli_python_lib import (  # type: ignore
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
)

from ..concurrent_invoker import (
    LAMBDA_FUNCTION_RESPONSE_PAYLOAD_DECODE_ENCODING,
)

INVOCATION_RESPONSE_FAILED = {
    "lambda_function": "LambdaFunctionInvokerHookTest-1",
    "progress_event": ProgressEvent(
        status=OperationStatus.FAILED,
        errorCode=HandlerErrorCode.NonCompliant,
        message="The resource is not compliant.",
        result=None,
        callbackContext=None,
        callbackDelaySeconds=0,
    ),
}

LAMBDA_FUNCTIONS_INFO_REQUEST_SINGLE_FUNCTION = {
    "lambda_function": "LambdaFunctionInvokerHookTest-1",
    "lambda_function_payload": '{"request": {"clientRequestToken": "REDACTED", "hookContext": {"awsAccountId": "REDACTED", "stackId": "REDACTED", "hookTypeName": "AWSSamples::LambdaFunctionInvoker::Hook", "hookTypeVersion": "00000001", "invocationPoint": "CREATE_PRE_PROVISION", "targetName": "AWS::S3::Bucket", "targetType": "RESOURCE", "targetLogicalId": "REDACTED", "targetModel": {"resourceProperties": {}}, "changeSetId": null}}, "callbackContext": {}}',  # noqa: E501
}

LAMBDA_FUNCTIONS_INFO_REQUEST_MULTIPLE_FUNCTIONS = [
    {
        "lambda_function": "LambdaFunctionInvokerHookTest-1",
        "lambda_function_payload": '{"request": {"clientRequestToken": "REDACTED", "hookContext": {"awsAccountId": "REDACTED", "stackId": "REDACTED", "hookTypeName": "AWSSamples::LambdaFunctionInvoker::Hook", "hookTypeVersion": "00000001", "invocationPoint": "CREATE_PRE_PROVISION", "targetName": "AWS::S3::Bucket", "targetType": "RESOURCE", "targetLogicalId": "REDACTED", "targetModel": {"resourceProperties": {}}, "changeSetId": null}}, "callbackContext": {}}',  # noqa: E501
    },
    {
        "lambda_function": "LambdaFunctionInvokerHookTest-2",
        "lambda_function_payload": '{"request": {"clientRequestToken": "REDACTED", "hookContext": {"awsAccountId": "REDACTED", "stackId": "REDACTED", "hookTypeName": "AWSSamples::LambdaFunctionInvoker::Hook", "hookTypeVersion": "00000001", "invocationPoint": "CREATE_PRE_PROVISION", "targetName": "AWS::S3::Bucket", "targetType": "RESOURCE", "targetLogicalId": "REDACTED", "targetModel": {"resourceProperties": {}}, "changeSetId": null}}, "callbackContext": {}}',  # noqa: E501
    },
    {
        "lambda_function": "LambdaFunctionInvokerHookTest-3",
        "lambda_function_payload": '{"request": {"clientRequestToken": "REDACTED", "hookContext": {"awsAccountId": "REDACTED", "stackId": "REDACTED", "hookTypeName": "AWSSamples::LambdaFunctionInvoker::Hook", "hookTypeVersion": "00000001", "invocationPoint": "CREATE_PRE_PROVISION", "targetName": "AWS::S3::Bucket", "targetType": "RESOURCE", "targetLogicalId": "REDACTED", "targetModel": {"resourceProperties": {}}, "changeSetId": null}}, "callbackContext": {}}',  # noqa: E501
    },
]

LAMBDA_SERVICE_INVOCATION_RESPONSE_SUCCESS_PAYLOAD = json.dumps(
    {
        "status": "SUCCESS",
        "errorCode": None,
        "message": "The resource is compliant.",
        "callbackContext": None,
        "callbackDelaySeconds": 0,
    }
).encode(LAMBDA_FUNCTION_RESPONSE_PAYLOAD_DECODE_ENCODING)

LAMBDA_SERVICE_INVOCATION_RESPONSE_FUNCTION_SUCCESS = {
    "ResponseMetadata": {
        "RequestId": "REDACTED",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "date": "Thu, 08 Feb 2024 20:37:59 GMT",
            "content-type": "application/json",
            "content-length": "133",
            "connection": "keep-alive",
            "x-amzn-requestid": "REDACTED",
            "x-amzn-remapped-content-length": "0",
            "x-amz-executed-version": "$LATEST",
            "x-amzn-trace-id": "REDACTED",
        },
        "RetryAttempts": 0,
    },
    "StatusCode": 200,
    "ExecutedVersion": "$LATEST",
    "Payload": StreamingBody(
        raw_stream=BytesIO(LAMBDA_SERVICE_INVOCATION_RESPONSE_SUCCESS_PAYLOAD),
        content_length=len(LAMBDA_SERVICE_INVOCATION_RESPONSE_SUCCESS_PAYLOAD),
    ),
}

LAMBDA_SERVICE_INVOCATION_RESPONSE_ERROR_PAYLOAD = json.dumps(
    {
        "errorMessage": "name 'testtest' is not defined",
        "errorType": "NameError",
        "requestId": "REDACTED",
        "stackTrace": [
            '  File "/var/task/index.py", line 85, in lambda_handler\n    return testtest\n'  # noqa: E501
        ],
    }
).encode(LAMBDA_FUNCTION_RESPONSE_PAYLOAD_DECODE_ENCODING)

LAMBDA_SERVICE_INVOCATION_RESPONSE_FUNCTION_ERROR = {
    "ResponseMetadata": {
        "RequestId": "REDACTED",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "date": "Thu, 15 Feb 2024 15:30:39 GMT",
            "content-type": "application/json",
            "content-length": "229",
            "connection": "keep-alive",
            "x-amzn-requestid": "REDACTED",
            "x-amz-function-error": "Unhandled",
            "x-amzn-remapped-content-length": "0",
            "x-amz-executed-version": "$LATEST",
            "x-amzn-trace-id": "REDACTED",
        },
        "RetryAttempts": 0,
    },
    "StatusCode": 200,
    "FunctionError": "Unhandled",
    "ExecutedVersion": "$LATEST",
    "Payload": StreamingBody(
        raw_stream=BytesIO(LAMBDA_SERVICE_INVOCATION_RESPONSE_ERROR_PAYLOAD),
        content_length=len(LAMBDA_SERVICE_INVOCATION_RESPONSE_ERROR_PAYLOAD),
    ),
}
