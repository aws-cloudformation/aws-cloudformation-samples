"""Unit tests for ConcurrentInvoker."""

from multiprocessing import (
    Pipe,
    Process,
    set_start_method,
)
from unittest.mock import (
    MagicMock,
    patch,
)

import botocore.session  # type: ignore
from botocore.stub import Stubber  # type: ignore
from cloudformation_cli_python_lib import (  # type: ignore
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
)

from ..concurrent_invoker import (
    LAMBDA_FUNCTION_FIELD_NAME,
    LAMBDA_FUNCTION_PAYLOAD_FIELD_NAME,
    ConcurrentInvoker,
)
from .mocks_concurrent_invoker import (
    INVOCATION_RESPONSE_FAILED,
    LAMBDA_FUNCTIONS_INFO_REQUEST_MULTIPLE_FUNCTIONS,
    LAMBDA_FUNCTIONS_INFO_REQUEST_SINGLE_FUNCTION,
    LAMBDA_SERVICE_INVOCATION_RESPONSE_FUNCTION_ERROR,
    LAMBDA_SERVICE_INVOCATION_RESPONSE_FUNCTION_SUCCESS,
)


def test_given_one_lambda_function_invoke_intent_when_invoked_then_should_return_one_invocation_response():  # noqa: E501
    mock_lambda_client = MagicMock()

    mock_concurrent_invoker = ConcurrentInvoker(
        lambda_client=mock_lambda_client,
        lambda_functions_info=MagicMock(),
    )
    with patch.object(
        mock_concurrent_invoker,
        "_run_multiprocess_invoke",
        return_value=[MagicMock()],
    ):
        with patch.object(
            mock_concurrent_invoker,
            "_receive_producer_to_consumer_connection_data",
            return_value=INVOCATION_RESPONSE_FAILED,
        ):
            mock_concurrent_invoker.invoke()

            assert len(mock_concurrent_invoker.get_invoke_results_info()) == 1
            assert (
                mock_concurrent_invoker.get_invoke_results_info()[0]
                == INVOCATION_RESPONSE_FAILED
            )


def test_given_two_lambda_functions_invoke_intent_when_invoked_then_should_return_invocation_response_for_each():  # noqa: E501
    mock_lambda_client = MagicMock()

    mock_concurrent_invoker = ConcurrentInvoker(
        lambda_client=mock_lambda_client,
        lambda_functions_info=MagicMock(),
    )
    with patch.object(
        mock_concurrent_invoker,
        "_run_multiprocess_invoke",
        return_value=[
            MagicMock(),
            MagicMock(),
        ],
    ):
        with patch.object(
            mock_concurrent_invoker,
            "_receive_producer_to_consumer_connection_data",
            return_value=INVOCATION_RESPONSE_FAILED,
        ):
            mock_concurrent_invoker.invoke()

            assert len(mock_concurrent_invoker.get_invoke_results_info()) == 2
            assert (
                mock_concurrent_invoker.get_invoke_results_info()[0]
                == INVOCATION_RESPONSE_FAILED
            )
            assert (
                mock_concurrent_invoker.get_invoke_results_info()[1]
                == INVOCATION_RESPONSE_FAILED
            )


def test_given_lambda_functions_info_when_lambda_invoke_api_called_then_should_return_expected_response():  # noqa: E501
    lambda_client = botocore.session.get_session().create_client(
        service_name="lambda",
        region_name="us-east-1",
    )
    stubber = Stubber(lambda_client)

    expected_params = {
        "FunctionName": LAMBDA_FUNCTIONS_INFO_REQUEST_SINGLE_FUNCTION[
            LAMBDA_FUNCTION_FIELD_NAME
        ],
        "InvocationType": "RequestResponse",
        "Payload": LAMBDA_FUNCTIONS_INFO_REQUEST_SINGLE_FUNCTION[
            LAMBDA_FUNCTION_PAYLOAD_FIELD_NAME
        ],
    }
    stubber.add_response(
        method="invoke",
        service_response=LAMBDA_SERVICE_INVOCATION_RESPONSE_FUNCTION_SUCCESS,
        expected_params=expected_params,
    )
    stubber.add_response(
        method="invoke",
        service_response=LAMBDA_SERVICE_INVOCATION_RESPONSE_FUNCTION_SUCCESS,
        expected_params=expected_params,
    )
    stubber.activate()

    service_response = lambda_client.invoke(
        **expected_params,
    )

    mock_concurrent_invoker = ConcurrentInvoker(
        lambda_client=lambda_client,
        lambda_functions_info=LAMBDA_FUNCTIONS_INFO_REQUEST_SINGLE_FUNCTION,
    )

    _make_invoke_request_and_get_response_return_value = (
        mock_concurrent_invoker._make_invoke_request_and_get_response(
            lambda_function_info=LAMBDA_FUNCTIONS_INFO_REQUEST_SINGLE_FUNCTION,
        )
    )

    assert (
        service_response == LAMBDA_SERVICE_INVOCATION_RESPONSE_FUNCTION_SUCCESS
    )
    assert (
        _make_invoke_request_and_get_response_return_value
        == LAMBDA_SERVICE_INVOCATION_RESPONSE_FUNCTION_SUCCESS
    )


def test_given_producer_to_consumer_connection_when_sending_data_then_should_receive_a_list_with_responses():  # noqa: E501
    mock_lambda_client = None

    mock_concurrent_invoker = ConcurrentInvoker(
        lambda_client=mock_lambda_client,
        lambda_functions_info=[],
    )

    def _mock_producer_to_consumer_connection(connection):
        connection.send(
            [
                "mock_data_1",
                "mock_data_2",
            ]
        )
        connection.close()

    set_start_method("fork")

    mock_consumer_connection, mock_producer_connection = Pipe()
    mock_process = Process(
        target=_mock_producer_to_consumer_connection,
        args=(mock_producer_connection,),
    )

    mock_process.start()

    return_data = (
        mock_concurrent_invoker._receive_producer_to_consumer_connection_data(
            producer_to_consumer_connection=mock_consumer_connection,
        )
    )

    mock_process.join()

    assert len(return_data) == 2
    assert return_data[0] == "mock_data_1"
    assert return_data[1] == "mock_data_2"


def test_given_multiple_lambda_functions_when_invoked_then_number_of_processes_should_match_number_of_invocations():  # noqa: E501
    mock_lambda_client = None

    mock_concurrent_invoker = ConcurrentInvoker(
        lambda_client=mock_lambda_client,
        lambda_functions_info=LAMBDA_FUNCTIONS_INFO_REQUEST_MULTIPLE_FUNCTIONS,
    )

    with patch.object(
        mock_concurrent_invoker,
        "_spawn_process",
        return_value=MagicMock(),
    ):
        mock_multiprocess_invoke = (
            mock_concurrent_invoker._run_multiprocess_invoke()
        )
        assert len(mock_multiprocess_invoke) == 3


def test_given_process_when_spawned_then_should_return_process():
    mock_lambda_client = None

    mock_concurrent_invoker = ConcurrentInvoker(
        lambda_client=mock_lambda_client,
        lambda_functions_info=[],
    )

    mock_process = mock_concurrent_invoker._spawn_process(
        producer_connection=MagicMock(),
        lambda_function_info=MagicMock(),
    )

    assert isinstance(mock_process, Process)


def test_given_lambda_service_request_when_invoked_then_consumer_should_get_expected_response():  # noqa: E501
    mock_lambda_client = None

    mock_concurrent_invoker = ConcurrentInvoker(
        lambda_client=mock_lambda_client,
        lambda_functions_info=LAMBDA_FUNCTIONS_INFO_REQUEST_MULTIPLE_FUNCTIONS,
    )

    with patch.object(
        mock_concurrent_invoker,
        "_make_invoke_request_and_get_response",
        return_value=LAMBDA_SERVICE_INVOCATION_RESPONSE_FUNCTION_SUCCESS,
    ):
        mock_consumer_connection, mock_producer_connection = Pipe()
        mock_concurrent_invoker._do_invoke(
            producer_connection=mock_producer_connection,
            lambda_function_info=LAMBDA_FUNCTIONS_INFO_REQUEST_MULTIPLE_FUNCTIONS[  # noqa: E501
                0
            ],
        )

        assert mock_consumer_connection.recv() == {
            "lambda_function": "LambdaFunctionInvokerHookTest-1",
            "progress_event": ProgressEvent(
                status="SUCCESS",
                errorCode=None,
                message="The resource is compliant.",
                result=None,
                callbackContext=None,
                callbackDelaySeconds=0,
                resourceModel=None,
                resourceModels=None,
                nextToken=None,
            ),
        }


def test_given_lambda_service_request_when_invoked_then_consumer_should_get_error_if_present_in_response():  # noqa: E501
    mock_lambda_client = None

    mock_concurrent_invoker = ConcurrentInvoker(
        lambda_client=mock_lambda_client,
        lambda_functions_info=LAMBDA_FUNCTIONS_INFO_REQUEST_MULTIPLE_FUNCTIONS,
    )

    with patch.object(
        mock_concurrent_invoker,
        "_make_invoke_request_and_get_response",
        return_value=LAMBDA_SERVICE_INVOCATION_RESPONSE_FUNCTION_ERROR,
    ):
        mock_consumer_connection, mock_producer_connection = Pipe()
        mock_concurrent_invoker._do_invoke(
            producer_connection=mock_producer_connection,
            lambda_function_info=LAMBDA_FUNCTIONS_INFO_REQUEST_MULTIPLE_FUNCTIONS[  # noqa: E501
                0
            ],
        )

        assert mock_consumer_connection.recv() == {
            "lambda_function": "LambdaFunctionInvokerHookTest-1",
            "progress_event": ProgressEvent(
                status=OperationStatus.FAILED,
                errorCode=HandlerErrorCode.InternalFailure,
                message="name 'testtest' is not defined",
                result=None,
                callbackContext=None,
                callbackDelaySeconds=0,
                resourceModel=None,
                resourceModels=None,
                nextToken=None,
            ),
        }


def test_given_lambda_service_request_when_invoked_then_consumer_should_get_progress_event_failed_if_exception_thrown():  # noqa: E501
    mock_lambda_client = None

    mock_concurrent_invoker = ConcurrentInvoker(
        lambda_client=mock_lambda_client,
        lambda_functions_info=LAMBDA_FUNCTIONS_INFO_REQUEST_MULTIPLE_FUNCTIONS,
    )

    with patch.object(
        mock_concurrent_invoker,
        "_make_invoke_request_and_get_response",
        side_effect=ValueError("Mock error."),
    ):
        mock_consumer_connection, mock_producer_connection = Pipe()
        mock_concurrent_invoker._do_invoke(
            producer_connection=mock_producer_connection,
            lambda_function_info=LAMBDA_FUNCTIONS_INFO_REQUEST_MULTIPLE_FUNCTIONS[  # noqa: E501
                0
            ],
        )

        assert mock_consumer_connection.recv() == {
            "lambda_function": "LambdaFunctionInvokerHookTest-1",
            "progress_event": ProgressEvent(
                status=OperationStatus.FAILED,
                errorCode=HandlerErrorCode.GeneralServiceException,
                message="Mock error.",
                result=None,
                callbackContext=None,
                callbackDelaySeconds=0,
            ),
        }
