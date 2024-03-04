"""ProgressEvent deserializer module."""


import json
from json.decoder import JSONDecodeError
from typing import (
    Any,
    Dict,
    MutableMapping,
    Optional,
)

from cloudformation_cli_python_lib import (  # type: ignore
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
)

# The invoked Lambda functions are expected to return a valid status
# from one of the following ones.
ALLOWED_OPERATION_STATUSES = [
    OperationStatus.FAILED,
    OperationStatus.IN_PROGRESS,
    OperationStatus.SUCCESS,
]


class ProgressEventDeserializer:
    """Return a ProgressEvent object from an input JSON data structure."""

    # Map ProgressEvent field names.
    status = "status"
    error_code = "errorCode"
    message = "message"
    callback_context = "callbackContext"
    callback_delay_seconds = "callbackDelaySeconds"

    @staticmethod
    def deserialize(
        input_json: str,
    ) -> ProgressEvent:
        """Deserialize a JSON input data structure into a ProgressEvent."""
        try:
            input_json_deserialized = json.loads(input_json)
        except JSONDecodeError:
            return ProgressEvent(
                status=OperationStatus.FAILED,
                errorCode=HandlerErrorCode.InternalFailure,
                message="Unable to deserialize the response returned by a Lambda function invoked by this hook.",  # noqa: E501
                callbackContext=None,
                callbackDelaySeconds=0,
            )

        try:
            status = ProgressEventDeserializer._derive_value(
                input_data=input_json_deserialized,
                field_name=ProgressEventDeserializer.status,
                fallback_value=OperationStatus.FAILED,
            )
            errorCode = ProgressEventDeserializer._derive_value(
                input_data=input_json_deserialized,
                field_name=ProgressEventDeserializer.error_code,
                fallback_value=HandlerErrorCode.InternalFailure,
            )
            message = ProgressEventDeserializer._derive_value(
                input_data=input_json_deserialized,
                field_name=ProgressEventDeserializer.message,
                fallback_value="No message or evaluation outcome returned by a Lambda function invoked by this hook.",  # noqa: E501
            )
            callbackContext = ProgressEventDeserializer._derive_value(
                input_data=input_json_deserialized,
                field_name=ProgressEventDeserializer.callback_context,
                fallback_value=None,
            )
            callbackDelaySeconds = ProgressEventDeserializer._derive_value(
                input_data=input_json_deserialized,
                field_name=ProgressEventDeserializer.callback_delay_seconds,
                fallback_value=0,
            )

            progress_event = (
                ProgressEventDeserializer._validate_deserialized_fields(
                    status=status,
                    error_code=errorCode,
                    message=message,
                    callback_context=callbackContext,
                    callback_delay_seconds=callbackDelaySeconds,
                )
            )
            if progress_event:
                return progress_event

            return ProgressEvent(
                status=status,
                errorCode=errorCode,
                message=message,
                callbackContext=callbackContext,
                callbackDelaySeconds=callbackDelaySeconds,
            )
        except AttributeError:
            return ProgressEvent(
                status=OperationStatus.FAILED,
                errorCode=HandlerErrorCode.InternalFailure,
                message="A Lambda function invoked by this hook should return JSON data with a key-value structure.",  # noqa: E501
                callbackContext=None,
                callbackDelaySeconds=0,
            )

    @staticmethod
    def _derive_value(
        input_data: Dict[str, Any],
        field_name: str,
        fallback_value: Any = None,
    ) -> Any:
        """Return either a value from an input dict, or a fallback value."""
        return (
            input_data[field_name]
            if field_name in input_data.keys()
            else fallback_value
        )

    @staticmethod
    def _validate_deserialized_fields(
        status: OperationStatus,
        error_code: HandlerErrorCode,
        message: str,
        callback_context: MutableMapping[str, Any],
        callback_delay_seconds: int,
    ) -> Optional[ProgressEvent]:
        # Validate that the returned status is an allowed one.
        if status not in ALLOWED_OPERATION_STATUSES:
            return ProgressEvent(
                status=OperationStatus.FAILED,
                errorCode=HandlerErrorCode.InternalFailure,
                message="A Lambda function invoked by this hook returned an invalid evaluation status.",  # noqa: E501
                callbackContext=None,
                callbackDelaySeconds=0,
            )

        # Validate that if errorCode is set, it is set to an
        # allowed value.
        if error_code and not hasattr(HandlerErrorCode, error_code):
            return ProgressEvent(
                status=OperationStatus.FAILED,
                errorCode=HandlerErrorCode.InternalFailure,
                message="A Lambda function invoked by this hook returned an invalid handler error code.",  # noqa: E501
                callbackContext=None,
                callbackDelaySeconds=0,
            )

        # Validate that errorCode is set when a failed evaluation
        # is returned.
        if status == OperationStatus.FAILED and not error_code:
            return ProgressEvent(
                status=OperationStatus.FAILED,
                errorCode=HandlerErrorCode.InternalFailure,
                message="A Lambda function invoked by this hook returned a failed status, but without an errorCode.",  # noqa: E501
                callbackContext=None,
                callbackDelaySeconds=0,
            )

        # Validate that errorCode is not set when a successful
        # evaluation is returned.
        if status != OperationStatus.FAILED and error_code:
            return ProgressEvent(
                status=OperationStatus.FAILED,
                errorCode=HandlerErrorCode.InternalFailure,
                message="A Lambda function invoked by this hook returned a success status, but an errorCode is set; note that if the Lambda function doesn't set, in the response, the errorCode to either a null value or to an empty string value when no errors occurred, this hook sets an InternalFailure value for errorCode, which can be the one that is set here.",  # noqa: E501
                callbackContext=None,
                callbackDelaySeconds=0,
            )

        # Validate that callbackDelaySeconds is an integer.
        try:
            int(callback_delay_seconds) >= 0
        except ValueError:
            return ProgressEvent(
                status=OperationStatus.FAILED,
                errorCode=HandlerErrorCode.InternalFailure,
                message="A Lambda function invoked by this hook returned a callbackDelaySeconds value that is not an integer value.",  # noqa: E501
                callbackContext=None,
                callbackDelaySeconds=0,
            )

        # Validate that callbackDelaySeconds is an integer greater
        # than zero.
        if callback_delay_seconds < 0:
            return ProgressEvent(
                status=OperationStatus.FAILED,
                errorCode=HandlerErrorCode.InternalFailure,
                message="A Lambda function invoked by this hook returned a callbackDelaySeconds value that is not an integer greater than or equal to zero.",  # noqa: E501
                callbackContext=None,
                callbackDelaySeconds=0,
            )

        # Validate that callbackDelaySeconds is set to zero for
        # statuses that are not IN_PROGRESS.
        if (
            callback_delay_seconds > 0
            and status != OperationStatus.IN_PROGRESS
        ):
            return ProgressEvent(
                status=OperationStatus.FAILED,
                errorCode=HandlerErrorCode.InternalFailure,
                message="A Lambda function invoked by this hook returned a callbackDelaySeconds value greater than zero for a not-in-progress operation status.",  # noqa: E501
                callbackContext=None,
                callbackDelaySeconds=0,
            )

        # Validate that callbackContext is not set for statuses
        # that are not IN_PROGRESS.
        if callback_context and status != OperationStatus.IN_PROGRESS:
            return ProgressEvent(
                status=OperationStatus.FAILED,
                errorCode=HandlerErrorCode.InternalFailure,
                message="A Lambda function invoked by this hook returned a non-empty callbackContext value for a not-in-progress operation status.",  # noqa: E501
                callbackContext=None,
                callbackDelaySeconds=0,
            )

        return None
