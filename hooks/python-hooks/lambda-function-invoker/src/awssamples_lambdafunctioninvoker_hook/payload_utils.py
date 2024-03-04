"""Payload utils module."""


import json
from typing import (
    Any,
    Dict,
    List,
    MutableMapping,
    Sequence,
)

from cloudformation_cli_python_lib import OperationStatus  # type: ignore

from .models import HookHandlerRequest

# Name of the dictionary key in the callback context that will hold
# information of Lambda functions to be reinvoked.
CALLBACKS_MAP_KEY = "lambda_functions_callbacks"

# Name of the dictionary key in the callback context that will hold
# messages returned by invoked Lambda functions.
MESSAGES_MAP_KEY = "lambda_functions_messages"


class PayloadUtils:
    """Utility class for AWS Lambda function payloads, and callbacks."""

    @staticmethod
    def get_in_progress_lambda_functions(
        type_configuration_lambda_functions: Sequence[str],
        callback_context: MutableMapping[str, Any] = {},
    ) -> List[str]:
        """Return a list of Lambda functions that are still in progress."""
        if CALLBACKS_MAP_KEY in callback_context:
            in_progress_lambda_functions: List[str] = [
                lambda_function
                for lambda_function in type_configuration_lambda_functions
                if lambda_function in callback_context[CALLBACKS_MAP_KEY]
            ]
            return in_progress_lambda_functions
        else:
            return []

    @staticmethod
    def get_single_tenant_callback_context(
        lambda_function: str,
        callback_context: MutableMapping[str, Any] = {},
    ) -> MutableMapping[str, Any]:
        """Return a callback content that is specific for a Lambda function."""
        if (
            CALLBACKS_MAP_KEY in callback_context
            and lambda_function in callback_context[CALLBACKS_MAP_KEY]
        ):
            # Pick the callback context for the current Lambda
            # function, with the intent to send only this one to the
            # Lambda function instead of all the others too.
            lambda_function_callback_context = callback_context[
                CALLBACKS_MAP_KEY
            ][lambda_function]

            return lambda_function_callback_context
        else:
            return {}

    @staticmethod
    def build_multi_tenant_callback_context(
        events: List[Dict[str, Any]],
        callback_context: MutableMapping[str, Any],
    ) -> MutableMapping[str, Any]:
        """Build a callback context when Lambda functions to reinvoke exist."""
        multi_tenant_callback_context: MutableMapping[str, Any] = {
            CALLBACKS_MAP_KEY: {},
            MESSAGES_MAP_KEY: {},
        }
        if (
            callback_context
            and CALLBACKS_MAP_KEY in callback_context
            and MESSAGES_MAP_KEY in callback_context
        ):
            multi_tenant_callback_context = callback_context

        # Create a list of Dict types, whereas each holds the name of
        # the Lambda function to reinvoke as a key, and its relevant
        # callback context as a value.
        for event in events:
            lambda_function = event["lambda_function"]
            lambda_function_status = event["progress_event"].status

            # Get events that are in progress, and set the relevant
            # Lambda function name as the key, and its callback
            # context as the value.
            if lambda_function_status == OperationStatus.IN_PROGRESS:
                lambda_function_callback_context = event[
                    "progress_event"
                ].callbackContext
                multi_tenant_callback_context[CALLBACKS_MAP_KEY][
                    lambda_function
                ] = lambda_function_callback_context

            # Create a map of messages returned by invoked Lambda
            # functions.
            lambda_function_message = event["progress_event"].message
            multi_tenant_callback_context[MESSAGES_MAP_KEY][
                lambda_function
            ] = lambda_function_message

        return multi_tenant_callback_context

    @staticmethod
    def build_invocation_payload(
        lambda_function: str,
        request: HookHandlerRequest,
        callback_context: MutableMapping[str, Any] = {},
    ) -> Dict[str, Any]:
        """Build and return a payload for a given Lambda function to invoke."""
        lambda_function_info = {}
        lambda_function_info["lambda_function"] = lambda_function
        lambda_function_info["lambda_function_payload"] = json.dumps(
            {
                "request": request,
                "callbackContext": callback_context,
            },
            default=vars,
        )

        return lambda_function_info

    @staticmethod
    def get_events_messages_from_multi_tenant_callback_context(
        callback_context: MutableMapping[str, Any] = {},
    ) -> List[str]:
        if MESSAGES_MAP_KEY in callback_context:
            messages = callback_context[MESSAGES_MAP_KEY]
            return [messages[message] for message in messages.keys()]
        else:
            return []
