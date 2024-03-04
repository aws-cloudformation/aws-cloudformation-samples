"""Unit test mocks for ProgressEventDeserializer."""


from typing import (
    Any,
    Dict,
)

from cloudformation_cli_python_lib import HandlerErrorCode  # type: ignore

# Add data intended to be serialized first (as sent by an invoked
# Lambda function), and then consumed by ProgressEventDeserializer for
# deserialization into ProgressEvent objects; unit tests should
# serialize mocks below (that is, by passing them to json.dumps()
# calls) before consuming them against methods/classes under test,
# except for EMPTY_STRING and INVALID_INPUT_STRUCTURE that should not
# be serialized when consumed by unit tests.


FAILED_NON_COMPLIANT = {
    "status": "FAILED",
    "errorCode": "NonCompliant",
    "message": "The resource is not compliant.",
    "callbackContext": None,
    "callbackDelaySeconds": 0,
}

SUCCESS = {
    "status": "SUCCESS",
    "errorCode": None,
    "message": "The resource is compliant.",
    "callbackContext": None,
    "callbackDelaySeconds": 0,
}

IN_PROGRESS = {
    "status": "IN_PROGRESS",
    "errorCode": None,
    "message": "The resource is being evaluated.",
    "callbackContext": {"key": "value"},
    "callbackDelaySeconds": 3,
}

EMPTY_JSON_INPUT: Dict[str, Any] = {}

# When consuming EMPTY_STRING from unit tests, don't serialize it; use
# it as it is.
EMPTY_STRING = ""

# When consuming INVALID_INPUT_STRUCTURE from unit tests, don't
# serialize it; use it as it is.
INVALID_INPUT_STRUCTURE = "[]"

INVALID_STATUS = {
    "status": "INCORRECT",
    "errorCode": None,
    "message": "The resource is compliant.",
    "callbackContext": None,
    "callbackDelaySeconds": 0,
}

INVALID_HANDLER_ERROR_CODE = {
    "status": "FAILED",
    "errorCode": "INCORRECT",
    "message": "The resource is compliant.",
    "callbackContext": None,
    "callbackDelaySeconds": 0,
}

FAILED_WITH_NO_ERROR_CODE = {
    "status": "FAILED",
    "errorCode": None,
    "message": "The resource is not compliant.",
    "callbackContext": None,
    "callbackDelaySeconds": 0,
}

SUCCESS_WITH_ERROR_CODE = {
    "status": "SUCCESS",
    "errorCode": HandlerErrorCode.GeneralServiceException,
    "message": "The resource is compliant.",
    "callbackContext": None,
    "callbackDelaySeconds": 0,
}

INVALID_CALLBACK_DELAY_SECONDS_NOT_INTEGER = {
    "status": "IN_PROGRESS",
    "errorCode": None,
    "message": "The resource is being evaluated.",
    "callbackContext": {"key": "value"},
    "callbackDelaySeconds": "INVALID",
}

INVALID_CALLBACK_DELAY_SECONDS_LESS_THAN_ZERO = {
    "status": "IN_PROGRESS",
    "errorCode": None,
    "message": "The resource is being evaluated.",
    "callbackContext": {"key": "value"},
    "callbackDelaySeconds": -3,
}

CALLBACK_DELAY_SECONDS_GREATER_THAN_ZERO_NOT_IN_PROGRESS = {
    "status": "SUCCESS",
    "errorCode": None,
    "message": "The resource is compliant.",
    "callbackContext": 0,
    "callbackDelaySeconds": 3,
}

CALLBACK_CONTEXT_WITH_NOT_IN_PROGRESS = {
    "status": "SUCCESS",
    "errorCode": None,
    "message": "The resource is compliant.",
    "callbackContext": {"key": "value"},
    "callbackDelaySeconds": 0,
}
