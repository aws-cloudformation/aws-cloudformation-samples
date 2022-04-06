import logging
import resource
from typing import Any, MutableMapping, Optional

from cloudformation_cli_python_lib import (
    BaseHookHandlerRequest,
    HandlerErrorCode,
    Hook,
    HookInvocationPoint,
    OperationStatus,
    ProgressEvent,
    SessionProxy,
    exceptions,
)

from .models import HookHandlerRequest, TypeConfigurationModel

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "AWSSamples::APIGWEnforceAuthorizer::Hook"

hook = Hook(TYPE_NAME, TypeConfigurationModel)
test_entrypoint = hook.test_entrypoint

PUBLIC_METHODS = ["options"]

@hook.handler(HookInvocationPoint.CREATE_PRE_PROVISION)
def pre_create_handler(
        session: Optional[SessionProxy],
        request: HookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: TypeConfigurationModel
) -> ProgressEvent:
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.FAILED
    )
    target_name = request.hookContext.targetName
    target_model = request.hookContext.targetModel
    resource_properties = target_model.get("resourceProperties")

    if validate_auth(target_name, resource_properties):
        progress.status = OperationStatus.SUCCESS
    else:
        progress.status = OperationStatus.FAILED
        progress.message = "Not all paths and methods have authorizers specified."
    return progress


@hook.handler(HookInvocationPoint.UPDATE_PRE_PROVISION)
def pre_update_handler(
        session: Optional[SessionProxy],
        request: BaseHookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: TypeConfigurationModel
) -> ProgressEvent:
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.FAILED
    )
    target_name = request.hookContext.targetName
    target_model = request.hookContext.targetModel
    resource_properties = target_model.get("resourceProperties")

    if validate_auth(target_name, resource_properties):
        progress.status = OperationStatus.SUCCESS
    else:
        progress.status = OperationStatus.FAILED
        progress.message = "Not all paths and methods have authorizers specified."
    return progress


def validate_auth(target_name, resource_properties) -> bool:
    if target_name == "AWS::ApiGateway::RestApi" or target_name == "AWS::ApiGatewayV2::Api":
        return validate_open_api_auth(resource_properties)
    elif target_name == "AWS::ApiGateway::Method" or target_name == "AWS::ApiGatewayV2::Route":
        return validate_cfn_auth(resource_properties)
    else:
        raise ValueError("Unknown target: " + target_name)


def validate_open_api_auth(resource_properties) -> bool:
    body = resource_properties.get("Body", {})

    # If security is defined at top level
    # skip individual validation
    top_level_security = body.get("security", None)
    if top_level_security is None:
        return True

    paths = body.get("paths", {})
    for path, methods in paths.items():
        for method, method_definition in methods.items():
            # Check both security and x-amazon-apigateway-auth section
            security = method_definition.get("security", None)
            apigateway_auth = method.definition.get("x-amazon-apigateway-auth", None)

            # Assume [] or {} is a valid security definition
            if security is None and apigateway_auth is None:
                return False

    return True


def validate_cfn_auth(resource_properties):
    if resource_properties.get("HttpMethod", "").lower() in PUBLIC_METHODS:
        return True
    return bool(resource_properties.get("AuthorizerId", None))