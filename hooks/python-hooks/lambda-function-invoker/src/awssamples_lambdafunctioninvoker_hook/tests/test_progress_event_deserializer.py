"""Unit tests for ProgressEventDeserializer."""


import json

from cloudformation_cli_python_lib import (  # type: ignore
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
)

from ..progress_event_deserializer import ProgressEventDeserializer
from .mocks_progress_event_deserializer import (
    CALLBACK_CONTEXT_WITH_NOT_IN_PROGRESS,
    CALLBACK_DELAY_SECONDS_GREATER_THAN_ZERO_NOT_IN_PROGRESS,
    EMPTY_JSON_INPUT,
    EMPTY_STRING,
    FAILED_NON_COMPLIANT,
    FAILED_WITH_NO_ERROR_CODE,
    IN_PROGRESS,
    INVALID_CALLBACK_DELAY_SECONDS_LESS_THAN_ZERO,
    INVALID_CALLBACK_DELAY_SECONDS_NOT_INTEGER,
    INVALID_HANDLER_ERROR_CODE,
    INVALID_INPUT_STRUCTURE,
    INVALID_STATUS,
    SUCCESS,
    SUCCESS_WITH_ERROR_CODE,
)


def test_given_payload_as_non_compliant_when_deserialized_then_should_return_progress_event_as_failed():  # noqa: E501
    payload = FAILED_NON_COMPLIANT
    progress_event = ProgressEventDeserializer.deserialize(
        input_json=json.dumps(payload),
    )

    assert isinstance(progress_event, ProgressEvent)
    assert progress_event.status == OperationStatus.FAILED
    assert progress_event.errorCode == HandlerErrorCode.NonCompliant
    assert progress_event.message == "The resource is not compliant."
    assert progress_event.callbackContext is None
    assert progress_event.callbackDelaySeconds == 0


def test_given_payload_as_compliant_when_deserialized_then_should_return_progress_event_as_success():  # noqa: E501
    payload = SUCCESS
    progress_event = ProgressEventDeserializer.deserialize(
        input_json=json.dumps(payload),
    )

    assert isinstance(progress_event, ProgressEvent)
    assert progress_event.status == OperationStatus.SUCCESS
    assert progress_event.errorCode is None
    assert progress_event.message == "The resource is compliant."
    assert progress_event.callbackContext is None
    assert progress_event.callbackDelaySeconds == 0


def test_given_payload_as_in_progress_when_deserialized_then_should_return_progress_event_as_in_progress():  # noqa: E501
    payload = IN_PROGRESS
    progress_event = ProgressEventDeserializer.deserialize(
        input_json=json.dumps(payload),
    )

    assert isinstance(progress_event, ProgressEvent)
    assert progress_event.status == OperationStatus.IN_PROGRESS
    assert progress_event.errorCode is None
    assert progress_event.message == "The resource is being evaluated."
    assert progress_event.callbackContext == {"key": "value"}
    assert progress_event.callbackDelaySeconds == 3


def test_given_payload_as_empty_json_input_when_deserialized_then_should_return_progress_event_as_failed_with_internal_failure():  # noqa: E501
    payload = EMPTY_JSON_INPUT
    progress_event = ProgressEventDeserializer.deserialize(
        input_json=json.dumps(payload),
    )

    assert isinstance(progress_event, ProgressEvent)
    assert progress_event.status == OperationStatus.FAILED
    assert progress_event.errorCode == HandlerErrorCode.InternalFailure
    assert (
        progress_event.message
        == "No message or evaluation outcome returned by a Lambda function invoked by this hook."  # noqa: E501
    )
    assert progress_event.callbackContext is None
    assert progress_event.callbackDelaySeconds == 0


def test_given_payload_as_empty_string_input_when_deserialized_then_should_return_progress_event_as_failed_with_internal_failure():  # noqa: E501
    payload = EMPTY_STRING
    progress_event = ProgressEventDeserializer.deserialize(
        input_json=payload,
    )

    assert isinstance(progress_event, ProgressEvent)
    assert progress_event.status == OperationStatus.FAILED
    assert progress_event.errorCode == HandlerErrorCode.InternalFailure
    assert (
        progress_event.message
        == "Unable to deserialize the response returned by a Lambda function invoked by this hook."  # noqa: E501
    )
    assert progress_event.callbackContext is None
    assert progress_event.callbackDelaySeconds == 0


def test_given_payload_as_invalid_input_structure_when_deserialized_then_should_return_progress_event_as_failed_with_internal_failure():  # noqa: E501
    payload = INVALID_INPUT_STRUCTURE
    progress_event = ProgressEventDeserializer.deserialize(
        input_json=payload,
    )

    assert isinstance(progress_event, ProgressEvent)
    assert progress_event.status == OperationStatus.FAILED
    assert progress_event.errorCode == HandlerErrorCode.InternalFailure
    assert (
        progress_event.message
        == "A Lambda function invoked by this hook should return JSON data with a key-value structure."  # noqa: E501
    )
    assert progress_event.callbackContext is None
    assert progress_event.callbackDelaySeconds == 0


def test_given_payload_as_invalid_status_when_deserialized_then_should_return_progress_event_as_failed_with_internal_failure():  # noqa: E501
    payload = INVALID_STATUS
    progress_event = ProgressEventDeserializer.deserialize(
        input_json=json.dumps(payload),
    )

    assert isinstance(progress_event, ProgressEvent)
    assert progress_event.status == OperationStatus.FAILED
    assert progress_event.errorCode == HandlerErrorCode.InternalFailure
    assert (
        progress_event.message
        == "A Lambda function invoked by this hook returned an invalid evaluation status."  # noqa: E501
    )
    assert progress_event.callbackContext is None
    assert progress_event.callbackDelaySeconds == 0


def test_given_payload_as_invalid_handler_error_code_when_deserialized_then_should_return_progress_event_as_failed_with_internal_failure():  # noqa: E501
    payload = INVALID_HANDLER_ERROR_CODE
    progress_event = ProgressEventDeserializer.deserialize(
        input_json=json.dumps(payload),
    )

    assert isinstance(progress_event, ProgressEvent)
    assert progress_event.status == OperationStatus.FAILED
    assert progress_event.errorCode == HandlerErrorCode.InternalFailure
    assert (
        progress_event.message
        == "A Lambda function invoked by this hook returned an invalid handler error code."  # noqa: E501
    )
    assert progress_event.callbackContext is None
    assert progress_event.callbackDelaySeconds == 0


def test_given_payload_as_failed_status_with_no_error_code_when_deserialized_then_should_return_progress_event_as_failed_with_internal_failure():  # noqa: E501
    payload = FAILED_WITH_NO_ERROR_CODE
    progress_event = ProgressEventDeserializer.deserialize(
        input_json=json.dumps(payload),
    )

    assert isinstance(progress_event, ProgressEvent)
    assert progress_event.status == OperationStatus.FAILED
    assert progress_event.errorCode == HandlerErrorCode.InternalFailure
    assert (
        progress_event.message
        == "A Lambda function invoked by this hook returned a failed status, but without an errorCode."  # noqa: E501
    )
    assert progress_event.callbackContext is None
    assert progress_event.callbackDelaySeconds == 0


def test_given_payload_as_success_status_with_error_code_when_deserialized_then_should_return_progress_event_as_failed_with_internal_failure():  # noqa: E501
    payload = SUCCESS_WITH_ERROR_CODE
    progress_event = ProgressEventDeserializer.deserialize(
        input_json=json.dumps(payload),
    )

    assert isinstance(progress_event, ProgressEvent)
    assert progress_event.status == OperationStatus.FAILED
    assert progress_event.errorCode == HandlerErrorCode.InternalFailure
    assert (
        progress_event.message
        == "A Lambda function invoked by this hook returned a success status, but an errorCode is set; note that if the Lambda function doesn't set, in the response, the errorCode to either a null value or to an empty string value when no errors occurred, this hook sets an InternalFailure value for errorCode, which can be the one that is set here."  # noqa: E501
    )
    assert progress_event.callbackContext is None
    assert progress_event.callbackDelaySeconds == 0


def test_given_payload_as_callback_delay_seconds_not_integer_when_deserialized_then_should_return_progress_event_as_failed_with_internal_failure():  # noqa: E501
    payload = INVALID_CALLBACK_DELAY_SECONDS_NOT_INTEGER
    progress_event = ProgressEventDeserializer.deserialize(
        input_json=json.dumps(payload),
    )

    assert isinstance(progress_event, ProgressEvent)
    assert progress_event.status == OperationStatus.FAILED
    assert progress_event.errorCode == HandlerErrorCode.InternalFailure
    assert (
        progress_event.message
        == "A Lambda function invoked by this hook returned a callbackDelaySeconds value that is not an integer value."  # noqa: E501
    )
    assert progress_event.callbackContext is None
    assert progress_event.callbackDelaySeconds == 0


def test_given_payload_as_callback_delay_seconds_less_than_zero_when_deserialized_then_should_return_progress_event_as_failed_with_internal_failure():  # noqa: E501
    payload = INVALID_CALLBACK_DELAY_SECONDS_LESS_THAN_ZERO
    progress_event = ProgressEventDeserializer.deserialize(
        input_json=json.dumps(payload),
    )

    assert isinstance(progress_event, ProgressEvent)
    assert progress_event.status == OperationStatus.FAILED
    assert progress_event.errorCode == HandlerErrorCode.InternalFailure
    assert (
        progress_event.message
        == "A Lambda function invoked by this hook returned a callbackDelaySeconds value that is not an integer greater than or equal to zero."  # noqa: E501
    )
    assert progress_event.callbackContext is None
    assert progress_event.callbackDelaySeconds == 0


def test_given_payload_as_callback_delay_seconds_greater_than_zero_with_not_in_progress_status_when_deserialized_then_should_return_progress_event_as_failed_with_internal_failure():  # noqa: E501
    payload = CALLBACK_DELAY_SECONDS_GREATER_THAN_ZERO_NOT_IN_PROGRESS
    progress_event = ProgressEventDeserializer.deserialize(
        input_json=json.dumps(payload),
    )

    assert isinstance(progress_event, ProgressEvent)
    assert progress_event.status == OperationStatus.FAILED
    assert progress_event.errorCode == HandlerErrorCode.InternalFailure
    assert (
        progress_event.message
        == "A Lambda function invoked by this hook returned a callbackDelaySeconds value greater than zero for a not-in-progress operation status."  # noqa: E501
    )
    assert progress_event.callbackContext is None
    assert progress_event.callbackDelaySeconds == 0


def test_given_payload_as_callback_context_with_not_in_progress_status_when_deserialized_then_should_return_progress_event_as_failed_with_internal_failure():  # noqa: E501
    payload = CALLBACK_CONTEXT_WITH_NOT_IN_PROGRESS
    progress_event = ProgressEventDeserializer.deserialize(
        input_json=json.dumps(payload),
    )

    assert isinstance(progress_event, ProgressEvent)
    assert progress_event.status == OperationStatus.FAILED
    assert progress_event.errorCode == HandlerErrorCode.InternalFailure
    assert (
        progress_event.message
        == "A Lambda function invoked by this hook returned a non-empty callbackContext value for a not-in-progress operation status."  # noqa: E501
    )
    assert progress_event.callbackContext is None
    assert progress_event.callbackDelaySeconds == 0
