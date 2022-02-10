import logging
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
TYPE_NAME = "AWSSamples::IAMPrincipalBoundary::Hook"

LOG.setLevel(logging.DEBUG)

hook = Hook(TYPE_NAME, TypeConfigurationModel)
test_entrypoint = hook.test_entrypoint

def _isPrincipalExcluded(principalName: str, excludedPrincipalSuffixes: str):
    suffixesToExclude = [suffix.strip() for suffix in excludedPrincipalSuffixes.split(',')]
    for suffix in suffixesToExclude:
        LOG.info(f'**Checking if principal name {principalName} starts with {suffix}')
        if suffix and principalName.startswith(suffix):
            return True
    return False

def _validate_iam_principal_boundary(targetTypeName: str, iamPrincipal: MutableMapping[str, Any], iamPrincipalBoundaryArn: str, excludedPrincipalSuffixes: str) -> ProgressEvent:
    status = None
    message = ""
    error_code = None

    status = OperationStatus.FAILED

    if iamPrincipal:
        permissionsBoundary = iamPrincipal.get("PermissionsBoundary")
        LOG.info(f"**Permission boundary found on template: {permissionsBoundary}")

        principalName = ""
        if targetTypeName == "AWS::IAM::Role":
            principalName = iamPrincipal.get("RoleName")
        else: 
            principalName = iamPrincipal.get("UserName")

        if not principalName:
            LOG.info('**Principal Name not specified on template.')
        else:
            LOG.info(f"**Principal name: {principalName}")

        # Check if permission boundary check is needed
        # Principal name may be null if not specified on the template, meaning it can't qualify for exclusion
        if principalName and _isPrincipalExcluded(principalName, excludedPrincipalSuffixes):
            status = OperationStatus.SUCCESS
            message = f"PermissionsBoundary is not required for principal named: {principalName}."
        else:
            LOG.info(f"**The principal name {principalName} is not excluded from the permissions boundary check.")
            if permissionsBoundary != iamPrincipalBoundaryArn:
                status = OperationStatus.FAILED
                message = f"PermissionsBoundary is incorrect for principal named: {principalName}. Expected {iamPrincipalBoundaryArn} found {permissionsBoundary}."
            else:
                status = OperationStatus.SUCCESS
                message = f"Required PermissionsBoundary {iamPrincipalBoundaryArn} is specified on template."
    else:
        message = "Resource properties for the IAM Principal target model are empty"

    LOG.info(f"Results Message: {message}")
    LOG.debug(f"DEBUG Results Message: {message}")

    if status == OperationStatus.FAILED:
        error_code = HandlerErrorCode.NonCompliant

    return ProgressEvent(
        status=status,
        message=message,
        errorCode=error_code
    )

@hook.handler(HookInvocationPoint.CREATE_PRE_PROVISION)
def pre_create_handler(
        session: Optional[SessionProxy],
        request: HookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: TypeConfigurationModel
) -> ProgressEvent:

    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS
    )

    target_name = request.hookContext.targetName

    try:

        LOG.debug("Hook context:")
        LOG.debug(request.hookContext)

        if "AWS::IAM::Role" == target_name or "AWS::IAM::User" == target_name:
            progress = _validate_iam_principal_boundary(target_name, 
                request.hookContext.targetModel.get("resourceProperties"), 
                type_configuration.iamPrincipalBoundaryArn, 
                type_configuration.excludedPrincipalSuffixes)
        else:
            raise exceptions.InvalidRequest(f"Unknown target type: {target_name}")

    except exceptions.InvalidRequest as e:
        progress.status = OperationStatus.FAILED
        progress.message = "Unknown target type: {target_name}"
    except BaseException as e:
        progress = ProgressEvent.failed(HandlerErrorCode.InternalFailure, f"Unexpected error {e}")

    return progress

@hook.handler(HookInvocationPoint.UPDATE_PRE_PROVISION)
def pre_update_handler(
        session: Optional[SessionProxy],
        request: BaseHookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: TypeConfigurationModel
) -> ProgressEvent:
    target_model = request.hookContext.targetModel
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS
    )
    
    target_name = request.hookContext.targetName

    try:

        LOG.debug("Hook context:")
        LOG.debug(request.hookContext)

        # Reading the Resource Hook's target new properties
        resource_properties = target_model.get("resourceProperties")

        # Only need to check if the new resource properties match the required TypeConfiguration.
        # This will block automatically if they are trying to remove a permission boundary.
        if "AWS::IAM::Role" == target_name or "AWS::IAM::User" == target_name:
            progress = _validate_iam_principal_boundary(target_name, 
                        resource_properties,
                        type_configuration.iamPrincipalBoundaryArn, 
                        type_configuration.excludedPrincipalSuffixes)
        else:
            raise exceptions.InvalidRequest(f"Unknown target type: {target_name}")

    except exceptions.InvalidRequest as e:
        progress.status = OperationStatus.FAILED
        progress.message = "Unknown target type: {target_name}"
    except BaseException as e:
        progress = ProgressEvent.failed(HandlerErrorCode.InternalFailure, f"Unexpected error {e}")

    return progress

@hook.handler(HookInvocationPoint.DELETE_PRE_PROVISION)
def pre_delete_handler(
        session: Optional[SessionProxy],
        request: BaseHookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: TypeConfigurationModel
) -> ProgressEvent:
    
    # If deleting a principal - no additional checks are needed.
    return ProgressEvent(
        status=OperationStatus.SUCCESS
    )
