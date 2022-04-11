"""
Hook handler for enforcing API Gateway authorizers.
"""
import logging
from typing import Any, Dict, MutableMapping, Optional

from cloudformation_cli_python_lib import (
    BaseHookHandlerRequest,
    HandlerErrorCode,
    Hook,
    HookInvocationPoint,
    OperationStatus,
    ProgressEvent,
    SessionProxy,
)

from .models import TypeConfigurationModel

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "AWSSamples::APIGWEnforceAuthorizer::Hook"

hook = Hook(TYPE_NAME, TypeConfigurationModel)
test_entrypoint = hook.test_entrypoint

PUBLIC_METHODS = ["options"]


@hook.handler(HookInvocationPoint.CREATE_PRE_PROVISION)
@hook.handler(HookInvocationPoint.UPDATE_PRE_PROVISION)
def pre_create_update_handler(
    _session: Optional[SessionProxy],
    request: BaseHookHandlerRequest,
    _callback_context: MutableMapping[str, Any],
    _type_configuration: TypeConfigurationModel,
) -> ProgressEvent:
    """
    Hook entry point for create and update.
    """
    progress: ProgressEvent = ProgressEvent(status=OperationStatus.FAILED)
    target_name = request.hookContext.targetName
    target_model = request.hookContext.targetModel
    resource_properties = (
        target_model.get("resourceProperties") if target_model is not None else None
    )

    if validate_auth(target_name, resource_properties):
        progress.status = OperationStatus.SUCCESS
    else:
        progress.status = OperationStatus.FAILED
        progress.message = "Not all paths and methods have authorizers specified."
        progress.errorCode = HandlerErrorCode.NonCompliant
    return progress


def validate_auth(
    target_name: Optional[str], resource_properties: Optional[Dict]
) -> bool:
    """Validate whether API Gateway APIs or Methods/Routes have authorizers."""
    if target_name is None or resource_properties is None:
        return False

    if target_name in ["AWS::ApiGateway::RestApi", "AWS::ApiGatewayV2::Api"]:
        return validate_open_api_auth(resource_properties)
    if target_name in ["AWS::ApiGateway::Method", "AWS::ApiGatewayV2::Route"]:
        return validate_cfn_auth(resource_properties)
    raise ValueError("Unknown target: " + target_name)


def validate_open_api_auth(resource_properties: Dict) -> bool:
    """Validate OpenAPI definition specified in an API resource."""
    body = resource_properties.get("Body", {})

    # If security is defined at top level
    # skip individual validation
    top_level_security = body.get("security", None)
    if top_level_security is not None:
        return True

    paths = body.get("paths", {})
    for _, methods in paths.items():
        for method, method_definition in methods.items():
            # Skip over public methods such as OPTIONS
            if method.lower() in PUBLIC_METHODS:
                continue
            # Check both security and x-amazon-apigateway-auth section
            security = method_definition.get("security", None)
            apigateway_auth = method_definition.get("x-amazon-apigateway-auth", None)

            # Assume [] or {} is a valid security definition
            if security is None and apigateway_auth is None:
                return False

    return True


def validate_cfn_auth(resource_properties: Dict) -> bool:
    """Validate API Gateway Method and Route resources for authorizers."""
    if resource_properties.get("HttpMethod", "").lower() in PUBLIC_METHODS:
        return True
    return bool(resource_properties.get("AuthorizerId", None))
