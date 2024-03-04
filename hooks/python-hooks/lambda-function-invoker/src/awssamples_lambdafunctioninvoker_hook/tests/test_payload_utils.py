"""Unit tests for PayloadUtils."""


from ..payload_utils import PayloadUtils
from .mocks_payload_utils import (
    BUILD_INVOCATION_PAYLOAD_CALLBACK_CONTEXT,
    BUILD_INVOCATION_PAYLOAD_LAMBDA_FUNCTION,
    BUILD_INVOCATION_PAYLOAD_REQUEST,
    CALLBACK_CONTEXT_FIRST_INVOCATION,
    CALLBACK_CONTEXT_NEXT_INVOCATION,
    MULTI_TENANT_CALLBACK_CONTEXT_FIRST_INVOCATION,
    MULTI_TENANT_CALLBACK_CONTEXT_NEXT_INVOCATION,
    MULTI_TENANT_EVENTS_FIRST_INVOCATION,
    MULTI_TENANT_EVENTS_NEXT_INVOCATION,
    SINGLE_TENANT_CALLBACK_CONTEXT_FIRST_INVOCATION,
    SINGLE_TENANT_CALLBACK_CONTEXT_NEXT_INVOCATION,
    SINGLE_TENANT_LAMBDA_FUNCTION_FIRST_INVOCATION,
    SINGLE_TENANT_LAMBDA_FUNCTION_NEXT_INVOCATION,
    TYPE_CONFIGURATION_LAMBDA_FUNCTIONS_FIRST_INVOCATION,
    TYPE_CONFIGURATION_LAMBDA_FUNCTIONS_NEXT_INVOCATION,
)


def test_given_hook_first_invocation_when_hook_invoked_then_should_have_no_in_progress_lambda_function():  # noqa: E501
    return_value = PayloadUtils.get_in_progress_lambda_functions(
        type_configuration_lambda_functions=TYPE_CONFIGURATION_LAMBDA_FUNCTIONS_FIRST_INVOCATION,  # noqa: E501
        callback_context=CALLBACK_CONTEXT_FIRST_INVOCATION,
    )

    assert len(return_value) == 0


def test_given_hook_next_invocation_when_hook_invoked_if_in_progress_lambda_functions_then_should_have_in_progress_lambda_functions():  # noqa: E501
    return_value = PayloadUtils.get_in_progress_lambda_functions(
        type_configuration_lambda_functions=TYPE_CONFIGURATION_LAMBDA_FUNCTIONS_NEXT_INVOCATION,  # noqa: E501
        callback_context=CALLBACK_CONTEXT_NEXT_INVOCATION,
    )

    assert len(return_value) == 1
    assert return_value == ["LambdaFunctionInvokerHookTest-1"]


def test_given_hook_first_invocation_and_single_tenant_callback_context_when_hook_invoked_then_should_have_no_in_progress_lambda_function():  # noqa: E501
    return_value = PayloadUtils.get_single_tenant_callback_context(
        lambda_function=SINGLE_TENANT_LAMBDA_FUNCTION_FIRST_INVOCATION,
        callback_context=SINGLE_TENANT_CALLBACK_CONTEXT_FIRST_INVOCATION,
    )

    assert return_value == {}


def test_given_hook_next_invocation_and_single_tenant_callback_context_when_hook_invoked_then_should_have_in_progress_lambda_function():  # noqa: E501
    return_value = PayloadUtils.get_single_tenant_callback_context(
        lambda_function=SINGLE_TENANT_LAMBDA_FUNCTION_NEXT_INVOCATION,
        callback_context=SINGLE_TENANT_CALLBACK_CONTEXT_NEXT_INVOCATION,
    )

    assert return_value == {"test": 1}


def test_given_multi_tenant_callback_context_first_invocation_when_hook_invoked_should_return_lambda_function_callbacks_and_messages():  # noqa: E501
    return_value = PayloadUtils.build_multi_tenant_callback_context(
        events=MULTI_TENANT_EVENTS_FIRST_INVOCATION,
        callback_context=MULTI_TENANT_CALLBACK_CONTEXT_FIRST_INVOCATION,
    )

    assert return_value == {
        "lambda_functions_callbacks": {
            "LambdaFunctionInvokerHookTest-1": {"test": 1}
        },
        "lambda_functions_messages": {
            "LambdaFunctionInvokerHookTest-1": "In progress"
        },
    }


def test_given_multi_tenant_callback_context_next_invocation_when_hook_invoked_should_return_lambda_function_callbacks_and_messages():  # noqa: E501
    return_value = PayloadUtils.build_multi_tenant_callback_context(
        events=MULTI_TENANT_EVENTS_NEXT_INVOCATION,
        callback_context=MULTI_TENANT_CALLBACK_CONTEXT_NEXT_INVOCATION,
    )

    assert return_value == {
        "lambda_functions_callbacks": {
            "LambdaFunctionInvokerHookTest-1": {"test": 1}
        },
        "lambda_functions_messages": {
            "LambdaFunctionInvokerHookTest-1": "(After a reinvocation of the handler) The resource is compliant."  # noqa: E501
        },
    }


def test_given_lambda_function_to_invoke_when_building_its_invocation_payload_should_return_expected_payload_structure():  # noqa: E501
    return_value = PayloadUtils.build_invocation_payload(
        lambda_function=BUILD_INVOCATION_PAYLOAD_LAMBDA_FUNCTION,
        request=BUILD_INVOCATION_PAYLOAD_REQUEST,
        callback_context=BUILD_INVOCATION_PAYLOAD_CALLBACK_CONTEXT,
    )

    assert return_value == {
        "lambda_function": "LambdaFunctionInvokerHookTest-1",
        "lambda_function_payload": '{"request": {"clientRequestToken": "REDACTED", "hookContext": {"awsAccountId": "REDACTED", "stackId": "REDACTED", "hookTypeName": "AWSSamples::LambdaFunctionInvoker::Hook", "hookTypeVersion": "00000001", "invocationPoint": "CREATE_PRE_PROVISION", "targetName": "AWS::S3::Bucket", "targetType": "RESOURCE", "targetLogicalId": "REDACTED", "targetModel": {"resourceProperties": {}}, "changeSetId": null}}, "callbackContext": {"test": 1}}',  # noqa: E501
    }


def test_given_non_empty_callback_context_when_getting_events_messages_then_should_return_non_empty_list():  # noqa: E501
    messages = (
        PayloadUtils.get_events_messages_from_multi_tenant_callback_context(
            MULTI_TENANT_CALLBACK_CONTEXT_NEXT_INVOCATION
        )
    )

    assert len(messages) == 1
    assert messages == [
        "(After a reinvocation of the handler) The resource is compliant."
    ]


def test_given_empty_callback_context_when_getting_events_messages_then_should_return_empty_list():  # noqa: E501
    messages = (
        PayloadUtils.get_events_messages_from_multi_tenant_callback_context({})
    )

    assert len(messages) == 0
