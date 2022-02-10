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
TYPE_NAME = "AWSSamples::IamPolicyDoesNotGiveAdmin::Hook"

hook = Hook(TYPE_NAME, TypeConfigurationModel)
test_entrypoint = hook.test_entrypoint


@hook.handler(HookInvocationPoint.CREATE_PRE_PROVISION)
@hook.handler(HookInvocationPoint.UPDATE_PRE_PROVISION)
def pre_create_handler(
        session: Optional[SessionProxy],
        request: HookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: TypeConfigurationModel
) -> ProgressEvent:
    target_model = request.hookContext.targetModel
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS
    )
    
    resource_properties = target_model.get("resourceProperties")
    resource_name = request.hookContext.targetLogicalId
    target_name = request.hookContext.targetName
    
    LOG.info(f"{TYPE_NAME} CREATE_PRE_PROVISION handler triggered for resource {resource_name} of type {target_name}")
    
    adminPolicyFound = False
    
    if "AWS::IAM::Policy" == target_name:
        adminPolicyFound = _isAdminPolicy(resource_properties)
        
    elif "AWS::IAM::User" == target_name or "AWS::IAM::Role" == target_name or "AWS::IAM::Group" == target_name:
        
        if resource_properties:
            policies = resource_properties.get("Policies")
            if policies:
                for policy in policies:
                    # iterate through them all - if multiple violations, logs will report them all
                    adminPolicyFound = adminPolicyFound or _isAdminPolicy(policy)
                
            else:
                LOG.info("No policies defined in this resource")
        else:
            raise exceptions.InternalFailure(f"{target_name} model empty")

    else:
        raise exceptions.InvalidRequest(f"Unknown target type: {target_name}")
        
        
    if adminPolicyFound:
        progress.status = OperationStatus.FAILED
        progress.errorCode = HandlerErrorCode.NonCompliant
        progress.message = "One or more policies granting 'Allow action * on resource *' found"
    else:
        progress.status = OperationStatus.SUCCESS
        progress.message = "No policies granting 'Allow action * on resource *' found"

    if progress.status != OperationStatus.SUCCESS:
        LOG.info(f"{TYPE_NAME} FAIL: Resource {resource_name} - {progress.message}")
    else:
        LOG.info(f"{TYPE_NAME} SUCCESS: Resource {resource_name} - {progress.message}")

    return progress


def _isAdminPolicy(policy: MutableMapping[str,Any]) -> bool:
    
    isAdminPolicy = False
    if policy:
        policyDocument = policy.get("PolicyDocument")
        policyName = policy.get("PolicyName")
        
        if policyDocument and policyName:
            
            for statement in policyDocument.get("Statement"):
                effect = statement.get("Effect")
                if effect != "Allow":
                    # not an allow statement -can skip
                    break
                
                wildcardResourceIncluded = False
                wildcardActionIncluded = False

                # resource may be single or multiple
                resource = statement.get("Resource")
                if resource == "*":
                    wildcardResourceIncluded = True
                elif type(resource) is list:
                    for res in resource:
                        if res == "*":
                            wildcardResourceIncluded = True
                            break # found a wildcard resource
                
                action = statement.get("Action") 
                if action == "*":
                    wildcardActionIncluded = True
                elif type(action) is list:
                    for act in action:
                        if act == "*":
                            wildcardActionIncluded = True
                            break  # found a wildcard action
                
                # we only get here if Effect was also Allow.
                if wildcardActionIncluded and wildcardResourceIncluded:
                    isAdminPolicy = True

            if isAdminPolicy:
                LOG.info(f"Policy with PolicyName {policyName} includes a Statement which grants 'Allow action * on "
                         f"resource *'")
                return True
            else:
                return False
        else:
            raise exceptions.InternalFailure(f"Policy model missing required parameters")  
    else:
        raise exceptions.InternalFailure(f"Policy model empty")
