"""Unit tests for ResultsEvaluator."""


from cloudformation_cli_python_lib import (  # type: ignore
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
)
from pytest import raises

from ..results_evaluator import ResultsEvaluator
from .mocks_results_evaluator import (
    HAS_FAILED_NON_COMPLIANT,
    HAS_IN_PROGRESS,
    HAS_MULTIPLE_IN_PROGRESS,
    HAS_SUCCESS,
)


def test_given_failed_non_compliant_when_evaluated_then_should_have_failed_event():  # noqa: E501
    invoke_results_info = HAS_FAILED_NON_COMPLIANT
    results_evaluator = ResultsEvaluator(
        invoke_results_info=invoke_results_info,
    )
    results_evaluator.evaluate()

    assert results_evaluator.has_events()
    assert len(results_evaluator.get_events()) == 2
    assert results_evaluator.has_failed_events()
    assert len(results_evaluator.get_failed_events()) == 1
    assert results_evaluator.get_events_messages() == [
        "The resource is compliant.",
        "The resource is not compliant.",
    ]
    assert results_evaluator.get_first_failed_event() == {
        "lambda_function": "LambdaFunctionInvokerHookTest-2",
        "progress_event": ProgressEvent(
            status=OperationStatus.FAILED,
            errorCode=HandlerErrorCode.NonCompliant,
            message="The resource is not compliant.",
            result=None,
            callbackContext=None,
            callbackDelaySeconds=0,
            resourceModel=None,
            resourceModels=None,
            nextToken=None,
        ),
    }
    assert results_evaluator.get_failed_events_messages() == [
        "The resource is not compliant."
    ]


def test_given_success_when_evaluated_then_should_have_success_event():
    invoke_results_info = HAS_SUCCESS
    results_evaluator = ResultsEvaluator(
        invoke_results_info=invoke_results_info,
    )
    results_evaluator.evaluate()

    assert results_evaluator.has_events()
    assert len(results_evaluator.get_events()) == 2
    assert results_evaluator.has_success_events()
    assert len(results_evaluator.get_success_events()) == 2
    assert results_evaluator.get_events_messages() == [
        "The resource is compliant.",
        "The resource is compliant.",
    ]


def test_given_in_progress_when_evaluated_then_should_have_in_progress_event():
    invoke_results_info = HAS_IN_PROGRESS
    results_evaluator = ResultsEvaluator(
        invoke_results_info=invoke_results_info,
    )
    results_evaluator.evaluate()

    assert results_evaluator.has_events()
    assert len(results_evaluator.get_events()) == 2
    assert results_evaluator.has_in_progress_events()
    assert len(results_evaluator.get_in_progress_events()) == 1
    assert results_evaluator.get_events_messages() == [
        "The resource is compliant.",
        "The resource is being evaluated.",
    ]


def test_given_multiple_in_progress_when_evaluated_then_should_get_highest_callback_delay_seconds():  # noqa: E501
    invoke_results_info = HAS_MULTIPLE_IN_PROGRESS
    results_evaluator = ResultsEvaluator(
        invoke_results_info=invoke_results_info,
    )
    results_evaluator.evaluate()

    assert results_evaluator.get_highest_callback_delay_seconds() == 3


def test_given_no_failed_events_when_evaluated_then_should_raise_index_error():
    invoke_results_info = HAS_SUCCESS
    results_evaluator = ResultsEvaluator(
        invoke_results_info=invoke_results_info,
    )
    results_evaluator.evaluate()

    with raises(IndexError):
        results_evaluator.get_first_failed_event()
