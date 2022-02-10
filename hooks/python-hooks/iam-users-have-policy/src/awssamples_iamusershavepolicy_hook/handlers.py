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
LOG.setLevel(logging.INFO)
TYPE_NAME = "AWSSamples::IamUsersHavePolicy::Hook"

hook = Hook(TYPE_NAME, TypeConfigurationModel)
test_entrypoint = hook.test_entrypoint


@hook.handler(HookInvocationPoint.CREATE_PRE_PROVISION)
@hook.handler(HookInvocationPoint.UPDATE_PRE_PROVISION)
def pre_create_handler(
        _session: Optional[SessionProxy],
        request: HookHandlerRequest,
        _callback_context: MutableMapping[str, Any],
        _type_configuration: TypeConfigurationModel
) -> ProgressEvent:
    target_model = request.hookContext.targetModel
    
    resource_properties = target_model.get("resourceProperties")
    resource_name = request.hookContext.targetLogicalId
    target_name = request.hookContext.targetName
    
    LOG.info("{} handler triggered for resource {} of type {}".format(TYPE_NAME, resource_name, target_name))
    
    if "AWS::IAM::User" == target_name:
        progress = _checkIamUserHasPolicies(resource_properties)
            
    else:
        raise exceptions.InvalidRequest(f"Unknown target type: {target_name}")

    if progress.status != OperationStatus.SUCCESS:
        LOG.info("{} FAIL: Resource {} - {}".format(TYPE_NAME, resource_name, progress.message))
    else:
        LOG.info("{} SUCCESS: Resource {} - {}".format(TYPE_NAME, resource_name, progress.message))

    return progress


def _checkIamUserHasPolicies(iam_user: MutableMapping[str,Any]) -> ProgressEvent:
    error_code = None
    
    if iam_user:
        user_policies = iam_user.get("Policies")
        user_managed_policies = iam_user.get("ManagedPolicyArns")
        
        if not user_policies and not user_managed_policies:
            status = OperationStatus.FAILED
            error_code = HandlerErrorCode.NonCompliant
            message = "No Policies or Managed Policy ARNs assigned to resource"
        else:
            status = OperationStatus.SUCCESS
            message = "User resource has Policies and/or Managed Policy ARNs assigned"
    else:
        status = OperationStatus.FAILED
        error_code = HandlerErrorCode.InternalFailure
        message = "Resource properties for IAM User target model are empty"

    return ProgressEvent(
        status=status,
        message=message,
        errorCode=error_code
    )


def _checkIamUserHasNotHadPoliciesRemoved(new_user: MutableMapping[str,Any], previous_user: MutableMapping[str,Any]) -> ProgressEvent:
    message = ""
    error_code = None
    
    if new_user and previous_user:
        new_policies = new_user.get("Policies")
        new_managed = new_user.get("ManagedPolicyArns")
        
        prev_policies = previous_user.get("Policies")
        prev_managed = previous_user.get("ManagedPolicyArns")
        
        # if it previously had a policy (managed or inline), don't allow it to be removed completely
        if prev_policies or prev_managed:
            if not new_policies and not new_managed:
                status = OperationStatus.FAILED
                error_code = HandlerErrorCode.NonCompliant
                message = "Cannot remove all policies from user via update"
            else:
                # still has policies and/or managed policy ARNs assigned
                status = OperationStatus.SUCCESS
                message = "User still has inline/managed policies assigned"
        else:
            # previous resource had no policies or managed policy ARNs defined
            status = OperationStatus.SUCCESS
            message = "Existing resource had no inline/managed policies originally"
            
    else:
        status = OperationStatus.FAILED
        error_code = HandlerErrorCode.InternalFailure
        message = "Resource properties for IAM User target model are empty"
    
    return ProgressEvent(
        status=status,
        message=message,
        errorCode=error_code
    )
