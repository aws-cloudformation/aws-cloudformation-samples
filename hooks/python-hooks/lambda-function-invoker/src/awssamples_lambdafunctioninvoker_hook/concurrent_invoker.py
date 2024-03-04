"""AWS Lambda function concurrent invoker module."""


import json
from dataclasses import (
    dataclass,
    field,
)
from multiprocessing import (
    Pipe,
    Process,
)
from multiprocessing.connection import Connection
from typing import (
    Any,
    Dict,
    List,
)

from cloudformation_cli_python_lib import (  # type: ignore
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
)

from .progress_event_deserializer import ProgressEventDeserializer

# Define constants for lambda_function_info data structure field names.
LAMBDA_FUNCTION_FIELD_NAME = "lambda_function"
LAMBDA_FUNCTION_PAYLOAD_FIELD_NAME = "lambda_function_payload"

# Encoding to use when decoding the response payload of an invoked
# Lambda function.
LAMBDA_FUNCTION_RESPONSE_PAYLOAD_DECODE_ENCODING = "utf-8"


@dataclass
class ConcurrentInvoker:
    """Concurrently invokes user-provided AWS Lambda functions."""

    # SessionProxy-based client for AWS Lambda.
    lambda_client: Any = None

    # Data structure holding information for Lambda functions to invoke.
    # Example of an expected structure, with redacted values:
    # [{'lambda_function': 'HookTargetFunctionTest',
    #   'lambda_function_payload': '{"request": {"clientRequestToken": '
    #                       '"REDACTED", '
    #                       '"hookContext": {"awsAccountId": "REDACTED", '
    #                       '"stackId": '
    #                       '"REDACTED", '
    #                       '"hookTypeName": '
    #                       '"AWSSamples::LambdaFunctionInvoker::Hook", '
    #                       '"hookTypeVersion": "00000001", '
    #                       '"invocationPoint": "CREATE_PRE_PROVISION", '
    #                       '"targetName": "AWS::S3::Bucket", "targetType": '
    #                       '"RESOURCE", "targetLogicalId": '
    #                       '"REDACTED", '
    #                       '"targetModel": {"resourceProperties": {}}, '
    #                       '"changeSetId": null}}, "callbackContext": null}'},
    #  {'lambda_function': 'HookTargetFunctionTestBis',
    #   'lambda_function_payload': '{"request": {"clientRequestToken": '
    #                       '"REDACTED", '
    #                       '"hookContext": {"awsAccountId": "REDACTED", '
    #                       '"stackId": '
    #                       '"REDACTED", '
    #                       '"hookTypeName": '
    #                       '"AWSSamples::LambdaFunctionInvoker::Hook", '
    #                       '"hookTypeVersion": "00000001", '
    #                       '"invocationPoint": "CREATE_PRE_PROVISION", '
    #                       '"targetName": "AWS::S3::Bucket", "targetType": '
    #                       '"RESOURCE", "targetLogicalId": '
    #                       '"REDACTED", '
    #                       '"targetModel": {"resourceProperties": {}}, '
    #                       '"changeSetId": null}}, "callbackContext": null}'}]
    lambda_functions_info: List[Dict[str, Any]] = field(default_factory=list)

    # Hold information on Lambda functions' invoke results.
    _invoke_results_info: List[Dict[str, Any]] = field(default_factory=list)

    def invoke(
        self,
    ) -> None:
        """Invoke user-provided Lambda functions concurrently."""
        invoke_results_info: List[Dict[str, Any]] = []

        producer_to_consumer_connections = self._run_multiprocess_invoke()

        for (
            producer_to_consumer_connection
        ) in producer_to_consumer_connections:
            invoke_results_info.append(
                self._receive_producer_to_consumer_connection_data(
                    producer_to_consumer_connection=producer_to_consumer_connection  # noqa: E501
                )
            )

        self._invoke_results_info = invoke_results_info

    def get_invoke_results_info(
        self,
    ) -> List[Dict[str, Any]]:
        """Return information on Lambda functions' invoke results."""
        return self._invoke_results_info

    def _receive_producer_to_consumer_connection_data(
        self,
        producer_to_consumer_connection: Connection,
    ) -> Dict[str, Any]:
        """Receive invoke results info from producer_to_consumer connection."""
        return producer_to_consumer_connection.recv()

    def _run_multiprocess_invoke(
        self,
    ) -> List[Connection]:
        """Invoke processes, and return producer-to-consumer connections."""
        invoke_processes = []
        producer_to_consumer_connections = []

        for lambda_function_info in self.lambda_functions_info:
            consumer_connection, producer_connection = Pipe()
            producer_to_consumer_connections.append(consumer_connection)

            invoke_processes.append(
                self._spawn_process(
                    producer_connection=producer_connection,
                    lambda_function_info=lambda_function_info,
                )
            )

        for invoke_process in invoke_processes:
            invoke_process.start()

        for invoke_process in invoke_processes:
            invoke_process.join()

        return producer_to_consumer_connections

    def _spawn_process(
        self,
        producer_connection: Connection,
        lambda_function_info: Dict[str, Any],
    ) -> Process:
        """Spawn a new process, and invoke a given Lambda function."""
        process = Process(
            target=self._do_invoke,
            args=(
                producer_connection,
                lambda_function_info,
            ),
        )

        return process

    def _do_invoke(
        self,
        producer_connection: Connection,
        lambda_function_info: Dict[str, Any],
    ) -> None:
        """Invoke a given Lambda function synchronously, and return results."""
        try:
            invoke_response = self._make_invoke_request_and_get_response(
                lambda_function_info=lambda_function_info,
            )

            # Read, and deserialize the payload from the response.
            response_payload_streaming_body = invoke_response["Payload"]
            response_payload = response_payload_streaming_body.read().decode(
                LAMBDA_FUNCTION_RESPONSE_PAYLOAD_DECODE_ENCODING,
            )

            # If the response contains an error, create a new FAILED
            # ProgressEvent.
            if "FunctionError" in invoke_response:
                progress_event = ProgressEvent(
                    status=OperationStatus.FAILED,
                    errorCode=HandlerErrorCode.InternalFailure,
                    message=json.loads(response_payload)["errorMessage"],
                    callbackContext=None,
                    callbackDelaySeconds=0,
                )
            # Otherwise, deserialize the response payload into a
            # ProgressEvent.
            else:
                progress_event = ProgressEventDeserializer.deserialize(
                    response_payload,
                )

            invoke_result_info = {
                "lambda_function": lambda_function_info[
                    LAMBDA_FUNCTION_FIELD_NAME
                ],
                "progress_event": progress_event,
            }
            producer_connection.send(invoke_result_info)
            producer_connection.close()
        except Exception as exception:
            invoke_result_info = {
                "lambda_function": lambda_function_info[
                    LAMBDA_FUNCTION_FIELD_NAME
                ],
                "progress_event": ProgressEvent(
                    status=OperationStatus.FAILED,
                    errorCode=HandlerErrorCode.GeneralServiceException,
                    message=str(exception),
                    callbackContext=None,
                    callbackDelaySeconds=0,
                ),
            }
            producer_connection.send(invoke_result_info)
            producer_connection.close()

    def _make_invoke_request_and_get_response(
        self,
        lambda_function_info: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Invoke a Lambda function with a synchronous RequestResponse type."""
        return self.lambda_client.invoke(
            FunctionName=lambda_function_info[LAMBDA_FUNCTION_FIELD_NAME],
            InvocationType="RequestResponse",
            Payload=lambda_function_info[LAMBDA_FUNCTION_PAYLOAD_FIELD_NAME],
        )
