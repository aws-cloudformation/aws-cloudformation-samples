"""AWSSamples::LambdaFunctionInvoker::Hook main module."""


import traceback
from typing import (
    Any,
    Dict,
    List,
    MutableMapping,
    Optional,
    Sequence,
    Union,
)

from cloudformation_cli_python_lib import (  # type: ignore
    HandlerErrorCode,
    Hook,
    HookInvocationPoint,
    OperationStatus,
    ProgressEvent,
    SessionProxy,
)

from .client_builder import ClientBuilder
from .concurrent_invoker import ConcurrentInvoker
from .logger import LOG
from .models import (
    HookHandlerRequest,
    TypeConfigurationModel,
)
from .payload_utils import (
    MESSAGES_MAP_KEY,
    PayloadUtils,
)
from .results_evaluator import ResultsEvaluator

TYPE_NAME = "AWSSamples::LambdaFunctionInvoker::Hook"

hook = Hook(TYPE_NAME, TypeConfigurationModel)
test_entrypoint = hook.test_entrypoint


@hook.handler(HookInvocationPoint.CREATE_PRE_PROVISION)
@hook.handler(HookInvocationPoint.UPDATE_PRE_PROVISION)
@hook.handler(HookInvocationPoint.DELETE_PRE_PROVISION)
def pre_create_pre_update_pre_delete_common_handler(
    session: Optional[SessionProxy],
    request: HookHandlerRequest,
    callback_context: MutableMapping[str, Any],
    type_configuration: TypeConfigurationModel,
) -> ProgressEvent:
    """Define an entry point for this hook."""
    progress = ProgressEvent(status=OperationStatus.IN_PROGRESS)
    try:
        target_name = request.hookContext.targetName
        if target_name and not target_name.startswith("AWS"):
            message = f"Unsupported target: {target_name}"
            LOG.error(message)
            return ProgressEvent(
                status=OperationStatus.FAILED,
                errorCode=HandlerErrorCode.UnsupportedTarget,
                message=message,
            )

        # Create a client for AWS Lambda using SessionProxy.
        lambda_client = ClientBuilder.get_session_client(
            session=session,
            aws_service_name="lambda",
        )

        if type_configuration.LambdaFunctions:
            lambda_functions: Union[List[str], Sequence[str]] = []

            LOG.debug(f"Callback context: {callback_context}")

            # Determine if there are Lambda functions still in
            # progress.
            in_progress_lambda_functions = PayloadUtils.get_in_progress_lambda_functions(  # noqa: E501
                type_configuration_lambda_functions=type_configuration.LambdaFunctions,  # noqa: E501
                callback_context=callback_context,
            )
            # If there are in-progress Lambda functions, this is a
            # handler callback: only invoke those functions, and not
            # the ones that were completed successfully earlier.
            if in_progress_lambda_functions:
                lambda_functions = in_progress_lambda_functions
                LOG.info(f"Reinvoking Lambda functions: {lambda_functions}")
            # Otherwise, this is a first handler invocation, and call
            # all the user-defined functions in the type
            # configuration.
            else:
                lambda_functions = type_configuration.LambdaFunctions
                LOG.info(f"Invoking Lambda functions: {lambda_functions}")

            lambda_functions_info: List[Dict[str, Any]] = []
            for lambda_function in lambda_functions:
                lambda_function_info = PayloadUtils.build_invocation_payload(
                    lambda_function=lambda_function,
                    request=request,
                    callback_context=PayloadUtils.get_single_tenant_callback_context(  # noqa: E501
                        lambda_function=lambda_function,
                        callback_context=callback_context,
                    ),
                )
                lambda_functions_info.append(lambda_function_info)
            LOG.debug(f"lambda_functions_info: {lambda_functions_info}")

            lambda_function_invoker = ConcurrentInvoker(
                lambda_client=lambda_client,
                lambda_functions_info=lambda_functions_info,
            )
            lambda_function_invoker.invoke()

            invoke_results_info = (
                lambda_function_invoker.get_invoke_results_info()
            )
            LOG.debug(f"Invoke results info: {invoke_results_info}")

            results_evaluator = ResultsEvaluator(
                invoke_results_info=invoke_results_info,
            )
            results_evaluator.evaluate()

            # Fail immediately if the status is FAILED.
            if results_evaluator.has_failed_events():
                message = str(results_evaluator.get_failed_events_messages())
                LOG.error(message)
                return ProgressEvent.failed(
                    error_code=HandlerErrorCode.NonCompliant,
                    message=message,
                )

            # Get all the events.
            events = results_evaluator.get_events()
            LOG.debug(events)

            # If one (or more) Lambda function returns an IN_PROGRESS
            # event, collect and process relevant information to
            # reinvoke the current handler.
            if results_evaluator.has_in_progress_events():
                # Fetch events that are in progress, and consume them
                # in LOG.
                in_progress_events = results_evaluator.get_in_progress_events()
                LOG.debug(f"IN_PROGRESS events: {in_progress_events}")

                # Use all the events, and pass them to the
                # multi-tenant callback context builder that is used
                # to create a map of Lambda functions to reinvoke, and
                # to create a map of status messages returned by
                # Lambda functions.
                multi_tenant_callback_context = (
                    PayloadUtils.build_multi_tenant_callback_context(
                        events=events,
                        callback_context=callback_context,
                    )
                )
                LOG.debug(multi_tenant_callback_context)

                progress.status = OperationStatus.IN_PROGRESS

                # Set the callback context with information on Lambda
                # functions to be reinvoked.
                progress.callbackContext = multi_tenant_callback_context

                # Set callbackDelaySeconds to the highest value
                # present in all the ProgressEvent objects.
                highest_callback_delay_seconds = (
                    results_evaluator.get_highest_callback_delay_seconds()
                )
                progress.callbackDelaySeconds = highest_callback_delay_seconds
                LOG.info(
                    f"Callback delay set to {highest_callback_delay_seconds}"
                )

                progress.message = str(
                    (
                        PayloadUtils.get_events_messages_from_multi_tenant_callback_context(  # noqa: E501
                            callback_context=multi_tenant_callback_context,
                        )
                    )
                )
                LOG.info(progress.message)

                LOG.debug(progress)

                return progress
        else:
            message = "No Lambda function to invoke in the type configuration."
            LOG.error(message)
            return ProgressEvent.failed(
                error_code=HandlerErrorCode.InvalidTypeConfiguration,
                message=message,
            )

        # If the resource is compliant, return SUCCESS.
        events_messages = []
        # If this handler invocation is a callback, then update the
        # callback context with messages returned by Lambda functions
        # invoked during this hook handler invocation.
        if callback_context and MESSAGES_MAP_KEY in callback_context:
            multi_tenant_callback_context = (
                PayloadUtils.build_multi_tenant_callback_context(
                    events=events,
                    callback_context=callback_context,
                )
            )
            events_messages = PayloadUtils.get_events_messages_from_multi_tenant_callback_context(  # noqa: E501
                callback_context=multi_tenant_callback_context,
            )
        else:
            # Otherwise, collect messages for this handler invocation
            # only.
            events_messages = results_evaluator.get_events_messages()

        progress.status = OperationStatus.SUCCESS
        progress.message = str(events_messages)
        progress.errorCode = None
        progress.callbackContext = None
        progress.callbackDelaySeconds = 0

        LOG.debug(progress)
        LOG.info(progress.message)

        return progress
    except Exception as exception:
        LOG.debug(f"Error while invoking the hook handler: {str(exception)}.")
        LOG.debug(f"Error details: {traceback.format_exc()}")
        return ProgressEvent.failed(
            error_code=HandlerErrorCode.InternalFailure,
            message=str(exception),
        )
