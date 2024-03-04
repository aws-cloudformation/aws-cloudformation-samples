"""Unit tests for handlers."""


from unittest.mock import (
    MagicMock,
    patch,
)

from cloudformation_cli_python_lib import (  # type: ignore
    HandlerErrorCode,
    OperationStatus,
)

from .. import handlers
from ..client_builder import ClientBuilder
from ..concurrent_invoker import ConcurrentInvoker
from .mocks_handlers import (
    CALLBACK_CONTEXT_2_LAMBDA_FUNCTIONS,
    HOOK_HANDLER_REQUEST,
    HOOK_HANDLER_REQUEST_UNSUPPORTED_TARGET,
    RESPONSE_FAILED_NON_COMPLIANT_1_LAMBDA_FUNCTION,
    RESPONSE_FAILED_NON_COMPLIANT_2_LAMBDA_FUNCTIONS,
    RESPONSE_IN_PROGRESS_1_LAMBDA_FUNCTION,
    RESPONSE_IN_PROGRESS_2_LAMBDA_FUNCTIONS,
    RESPONSE_LAMBDA_FUNCTIONS_WITH_1_OR_MORE_FAILED,
    RESPONSE_SUCCESS_1_LAMBDA_FUNCTION,
    RESPONSE_SUCCESS_2_LAMBDA_FUNCTIONS,
    TYPE_CONFIGURATION_1_LAMBDA_FUNCTION,
    TYPE_CONFIGURATION_2_LAMBDA_FUNCTIONS,
    TYPE_CONFIGURATION_4_LAMBDA_FUNCTIONS,
    TYPE_CONFIGURATION_NO_LAMBDA_FUNCTION,
)


@patch.object(
    ConcurrentInvoker,
    "get_invoke_results_info",
    side_effect=ValueError("Mock error."),
)
@patch.object(ConcurrentInvoker, "invoke", return_value=None)
@patch.object(ClientBuilder, "get_session_client", return_value=MagicMock())
def test_given_exception_thrown_when_handler_code_runs_then_should_return_progress_event_failed_internal_failure(  # noqa: E501
    mock_get_session_client,
    mock_invoke,
    mock_get_invoke_results_info,
):
    HOOK_HANDLER_REQUEST.hookContext.targetModel = {
        "resourceProperties": {
            "VersioningConfiguration": {"Status": "Suspended"},
        },
    }

    response = handlers.pre_create_pre_update_pre_delete_common_handler(
        session=MagicMock(),
        request=HOOK_HANDLER_REQUEST,
        callback_context={},
        type_configuration=TYPE_CONFIGURATION_1_LAMBDA_FUNCTION,
    )

    assert mock_get_session_client.called
    assert mock_invoke.called
    assert mock_get_invoke_results_info.called

    assert response.callbackContext is None
    assert response.callbackDelaySeconds == 0
    assert response.errorCode == HandlerErrorCode.InternalFailure
    assert response.message == "Mock error."
    assert response.status == OperationStatus.FAILED


def test_given_unsupported_target_when_hook_is_invoked_then_should_return_progress_event_failed_unsupported_target():  # noqa: E501
    HOOK_HANDLER_REQUEST.hookContext.targetModel = {
        "resourceProperties": {},
    }

    response = handlers.pre_create_pre_update_pre_delete_common_handler(
        session=MagicMock(),
        request=HOOK_HANDLER_REQUEST_UNSUPPORTED_TARGET,
        callback_context={},
        type_configuration=TYPE_CONFIGURATION_1_LAMBDA_FUNCTION,
    )

    assert response.callbackContext is None
    assert response.callbackDelaySeconds == 0
    assert response.errorCode == HandlerErrorCode.UnsupportedTarget
    assert response.message == "Unsupported target: Unsupported::Test::Target"
    assert response.status == OperationStatus.FAILED


def test_given_no_lambda_function_configured_when_hook_is_invoked_then_should_return_progress_event_failed_invalid_type_configuration():  # noqa: E501
    HOOK_HANDLER_REQUEST.hookContext.targetModel = {
        "resourceProperties": {},
    }

    response = handlers.pre_create_pre_update_pre_delete_common_handler(
        session=MagicMock(),
        request=HOOK_HANDLER_REQUEST,
        callback_context={},
        type_configuration=TYPE_CONFIGURATION_NO_LAMBDA_FUNCTION,
    )

    assert response.callbackContext is None
    assert response.callbackDelaySeconds == 0
    assert response.errorCode == HandlerErrorCode.InvalidTypeConfiguration
    assert (
        response.message
        == "No Lambda function to invoke in the type configuration."
    )
    assert response.status == OperationStatus.FAILED


@patch.object(
    ConcurrentInvoker,
    "get_invoke_results_info",
    return_value=RESPONSE_FAILED_NON_COMPLIANT_1_LAMBDA_FUNCTION,
)
@patch.object(ConcurrentInvoker, "invoke", return_value=None)
@patch.object(ClientBuilder, "get_session_client", return_value=MagicMock())
def test_given_failed_non_compliant_invoke_result_when_evaluated_then_should_return_progress_event_failed_non_compliant(  # noqa: E501
    mock_get_session_client,
    mock_invoke,
    mock_get_invoke_results_info,
):
    HOOK_HANDLER_REQUEST.hookContext.targetModel = {
        "resourceProperties": {
            "VersioningConfiguration": {"Status": "Suspended"},
        },
    }

    response = handlers.pre_create_pre_update_pre_delete_common_handler(
        session=MagicMock(),
        request=HOOK_HANDLER_REQUEST,
        callback_context={},
        type_configuration=TYPE_CONFIGURATION_1_LAMBDA_FUNCTION,
    )

    assert mock_get_session_client.called
    assert mock_invoke.called
    assert mock_get_invoke_results_info.called

    assert response.callbackContext is None
    assert response.callbackDelaySeconds == 0
    assert response.errorCode == HandlerErrorCode.NonCompliant
    assert response.message == "['The resource is not compliant.']"
    assert response.status == OperationStatus.FAILED


@patch.object(
    ConcurrentInvoker,
    "get_invoke_results_info",
    return_value=RESPONSE_FAILED_NON_COMPLIANT_2_LAMBDA_FUNCTIONS,
)
@patch.object(ConcurrentInvoker, "invoke", return_value=None)
@patch.object(ClientBuilder, "get_session_client", return_value=MagicMock())
def test_given_failed_non_compliant_invoke_results_when_evaluated_then_should_return_progress_event_failed_non_compliant(  # noqa: E501
    mock_get_session_client,
    mock_invoke,
    mock_get_invoke_results_info,
):
    HOOK_HANDLER_REQUEST.hookContext.targetModel = {
        "resourceProperties": {
            "VersioningConfiguration": {"Status": "Suspended"},
        },
    }

    response = handlers.pre_create_pre_update_pre_delete_common_handler(
        session=MagicMock(),
        request=HOOK_HANDLER_REQUEST,
        callback_context={},
        type_configuration=TYPE_CONFIGURATION_2_LAMBDA_FUNCTIONS,
    )

    assert mock_get_session_client.called
    assert mock_invoke.called
    assert mock_get_invoke_results_info.called

    assert response.callbackContext is None
    assert response.callbackDelaySeconds == 0
    assert response.errorCode == HandlerErrorCode.NonCompliant
    assert (
        response.message
        == "['The resource is not compliant.', 'The resource is not compliant.']"  # noqa: E501
    )
    assert response.status == OperationStatus.FAILED


@patch.object(
    ConcurrentInvoker,
    "get_invoke_results_info",
    return_value=RESPONSE_SUCCESS_1_LAMBDA_FUNCTION,
)
@patch.object(ConcurrentInvoker, "invoke", return_value=None)
@patch.object(ClientBuilder, "get_session_client", return_value=MagicMock())
def test_given_success_invoke_result_when_evaluated_then_should_return_progress_event_success(  # noqa: E501
    mock_get_session_client,
    mock_invoke,
    mock_get_invoke_results_info,
):
    HOOK_HANDLER_REQUEST.hookContext.targetModel = {
        "resourceProperties": {
            "VersioningConfiguration": {"Status": "Enabled"},
        },
    }

    response = handlers.pre_create_pre_update_pre_delete_common_handler(
        session=MagicMock(),
        request=HOOK_HANDLER_REQUEST,
        callback_context={},
        type_configuration=TYPE_CONFIGURATION_1_LAMBDA_FUNCTION,
    )

    assert mock_get_session_client.called
    assert mock_invoke.called
    assert mock_get_invoke_results_info.called

    assert response.callbackContext is None
    assert response.callbackDelaySeconds == 0
    assert response.errorCode is None
    assert response.message == "['The resource is compliant.']"
    assert response.status == OperationStatus.SUCCESS


@patch.object(
    ConcurrentInvoker,
    "get_invoke_results_info",
    return_value=RESPONSE_SUCCESS_2_LAMBDA_FUNCTIONS,
)
@patch.object(ConcurrentInvoker, "invoke", return_value=None)
@patch.object(ClientBuilder, "get_session_client", return_value=MagicMock())
def test_given_success_invoke_results_when_evaluated_then_should_return_progress_event_success(  # noqa: E501
    mock_get_session_client,
    mock_invoke,
    mock_get_invoke_results_info,
):
    HOOK_HANDLER_REQUEST.hookContext.targetModel = {
        "resourceProperties": {
            "VersioningConfiguration": {"Status": "Enabled"},
        },
    }

    response = handlers.pre_create_pre_update_pre_delete_common_handler(
        session=MagicMock(),
        request=HOOK_HANDLER_REQUEST,
        callback_context={},
        type_configuration=TYPE_CONFIGURATION_2_LAMBDA_FUNCTIONS,
    )

    assert mock_get_session_client.called
    assert mock_invoke.called
    assert mock_get_invoke_results_info.called

    assert response.callbackContext is None
    assert response.callbackDelaySeconds == 0
    assert response.errorCode is None
    assert (
        response.message
        == "['The resource is compliant.', 'The resource is compliant.']"
    )
    assert response.status == OperationStatus.SUCCESS


@patch.object(
    ConcurrentInvoker,
    "get_invoke_results_info",
    return_value=RESPONSE_IN_PROGRESS_1_LAMBDA_FUNCTION,
)
@patch.object(ConcurrentInvoker, "invoke", return_value=None)
@patch.object(ClientBuilder, "get_session_client", return_value=MagicMock())
def test_given_in_progress_invoke_result_when_evaluated_then_should_return_progress_event_in_progress(  # noqa: E501
    mock_get_session_client,
    mock_invoke,
    mock_get_invoke_results_info,
):
    HOOK_HANDLER_REQUEST.hookContext.targetModel = {
        "resourceProperties": {
            "VersioningConfiguration": {"Status": "Enabled"},
        },
    }

    response = handlers.pre_create_pre_update_pre_delete_common_handler(
        session=MagicMock(),
        request=HOOK_HANDLER_REQUEST,
        callback_context={},
        type_configuration=TYPE_CONFIGURATION_1_LAMBDA_FUNCTION,
    )

    assert mock_get_session_client.called
    assert mock_invoke.called
    assert mock_get_invoke_results_info.called

    assert response.callbackContext == {
        "lambda_functions_callbacks": {
            "MockLambdaFunctionName1": {"key1": "value1"},
        },
        "lambda_functions_messages": {
            "MockLambdaFunctionName1": "The resource is being evaluated.",
        },
    }
    assert response.callbackDelaySeconds == 0
    assert response.errorCode is None
    assert response.message == "['The resource is being evaluated.']"
    assert response.status == OperationStatus.IN_PROGRESS


@patch.object(
    ConcurrentInvoker,
    "get_invoke_results_info",
    return_value=RESPONSE_IN_PROGRESS_2_LAMBDA_FUNCTIONS,
)
@patch.object(ConcurrentInvoker, "invoke", return_value=None)
@patch.object(ClientBuilder, "get_session_client", return_value=MagicMock())
def test_given_in_progress_invoke_results_when_evaluated_then_should_return_progress_event_in_progress(  # noqa: E501
    mock_get_session_client,
    mock_invoke,
    mock_get_invoke_results_info,
):
    HOOK_HANDLER_REQUEST.hookContext.targetModel = {
        "resourceProperties": {
            "VersioningConfiguration": {"Status": "Enabled"},
        },
    }

    response = handlers.pre_create_pre_update_pre_delete_common_handler(
        session=MagicMock(),
        request=HOOK_HANDLER_REQUEST,
        callback_context={},
        type_configuration=TYPE_CONFIGURATION_1_LAMBDA_FUNCTION,
    )

    assert mock_get_session_client.called
    assert mock_invoke.called
    assert mock_get_invoke_results_info.called

    assert response.callbackContext == {
        "lambda_functions_callbacks": {
            "MockLambdaFunctionName1": {"key1": "value1"},
            "MockLambdaFunctionName2": {"key2": "value2"},
        },
        "lambda_functions_messages": {
            "MockLambdaFunctionName1": "The resource is being evaluated.",
            "MockLambdaFunctionName2": "The resource is being evaluated.",
        },
    }
    assert response.callbackDelaySeconds == 0
    assert response.errorCode is None
    assert (
        response.message
        == "['The resource is being evaluated.', 'The resource is being evaluated.']"  # noqa: E501
    )
    assert response.status == OperationStatus.IN_PROGRESS


@patch.object(
    ConcurrentInvoker,
    "get_invoke_results_info",
    return_value=RESPONSE_LAMBDA_FUNCTIONS_WITH_1_OR_MORE_FAILED,
)
@patch.object(ConcurrentInvoker, "invoke", return_value=None)
@patch.object(ClientBuilder, "get_session_client", return_value=MagicMock())
def test_given_one_or_more_failed_event_when_evaluated_then_should_return_failed_immediately(  # noqa: E501
    mock_get_session_client,
    mock_invoke,
    mock_get_invoke_results_info,
):
    HOOK_HANDLER_REQUEST.hookContext.targetModel = {
        "resourceProperties": {
            "VersioningConfiguration": {"Status": "Enabled"},
        },
    }

    response = handlers.pre_create_pre_update_pre_delete_common_handler(
        session=MagicMock(),
        request=HOOK_HANDLER_REQUEST,
        callback_context={},
        type_configuration=TYPE_CONFIGURATION_4_LAMBDA_FUNCTIONS,
    )

    assert mock_get_session_client.called
    assert mock_invoke.called
    assert mock_get_invoke_results_info.called

    assert response.callbackContext is None
    assert response.callbackDelaySeconds == 0
    assert response.errorCode == HandlerErrorCode.NonCompliant
    assert (
        response.message
        == "['The resource is not compliant.', 'The resource is not compliant.']"  # noqa: E501
    )
    assert response.status == OperationStatus.FAILED


@patch.object(
    ConcurrentInvoker,
    "get_invoke_results_info",
    return_value=RESPONSE_SUCCESS_2_LAMBDA_FUNCTIONS,
)
@patch.object(ConcurrentInvoker, "invoke", return_value=None)
@patch.object(ClientBuilder, "get_session_client", return_value=MagicMock())
def test_given_callback_handler_invocation_when_hook_runs_then_should_consume_multi_tenant_callback_context(  # noqa: E501
    mock_get_session_client,
    mock_invoke,
    mock_get_invoke_results_info,
):
    HOOK_HANDLER_REQUEST.hookContext.targetModel = {
        "resourceProperties": {
            "VersioningConfiguration": {"Status": "Enabled"},
        },
    }

    response = handlers.pre_create_pre_update_pre_delete_common_handler(
        session=MagicMock(),
        request=HOOK_HANDLER_REQUEST,
        callback_context=CALLBACK_CONTEXT_2_LAMBDA_FUNCTIONS,
        type_configuration=TYPE_CONFIGURATION_2_LAMBDA_FUNCTIONS,
    )

    assert mock_get_session_client.called
    assert mock_invoke.called
    assert mock_get_invoke_results_info.called

    assert response.callbackContext is None
    assert response.callbackDelaySeconds == 0
    assert response.errorCode is None
    assert (
        response.message
        == "['The resource is compliant.', 'The resource is compliant.']"
    )
    assert response.status == OperationStatus.SUCCESS
