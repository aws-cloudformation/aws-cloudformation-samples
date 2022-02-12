import logging
import os
import sys
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
#    HookContext,        # debug
)

from .models import HookHandlerRequest, TypeConfigurationModel
#from models import HookHandlerRequest, TypeConfigurationModel  # for local debugging

#import boto3       # debug

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "AWSSamples::Ec2SsmSmOnly::Hook"

hook = Hook(TYPE_NAME, TypeConfigurationModel)
test_entrypoint = hook.test_entrypoint

LOG.setLevel(logging.DEBUG)

# Overwrite the error message for exceptions.NotFound
class NotFound(exceptions.Unknown):
    def __init__(self, type_name: str, identifier: str):
        super().__init__(
            f"Resource of type '{type_name}'; identifier '{identifier}' was not found or is empty."
        )

def _validate_ec2_ssmsm_only_access(session, hookContext, resourceProperties, typeConfiguration):

    targetLogicalId = hookContext.targetLogicalId

    # Make sure the instance has properties defined
    if not resourceProperties:
        raise NotFound(targetLogicalId, f"Properties")
        
    # Check if the instance has a IAMInstanceProfile property defined
    iamInstanceProfileName = resourceProperties.get("IamInstanceProfile")

    # Make sure we have a non-empty instance profile name
    if not iamInstanceProfileName or (iamInstanceProfileName == ""):
        raise NotFound(targetLogicalId, f"IamInstanceProfile")

    LOG.debug(f"iam_instance_profile_name: {iamInstanceProfileName}")

    iam = session.client('iam')

    # Get the profile details
    getInstanceProfileResp = iam.get_instance_profile(InstanceProfileName=iamInstanceProfileName)

    # SSM Session Manager requires these actions to operate
    ssmSessionManagerPermissions = [
        "ssmmessages:CreateControlChannel",
        "ssmmessages:CreateDataChannel",
        "ssmmessages:OpenControlChannel",
        "ssmmessages:OpenDataChannel"
    ]

    if typeConfiguration.requireSessionManagerEncryption == True:
        ssmSessionManagerPermissions.append("kms:decrypt")
    
    actionErrors = []

    # Iterate over the roles (should only be one role)
    for role in getInstanceProfileResp['InstanceProfile']['Roles']:

        # Make sure we have a non-empty role name
        roleName = role["RoleName"]
        if not roleName or (roleName == ""):
            raise NotFound(targetLogicalId, f"{iamInstanceProfileName}.RoleName")

        LOG.debug(f"role_name: {roleName}")

        # Get the role definition
        getRoleResp = iam.get_role(RoleName=roleName)

        # Simulate the role using the required SSM SM actions to see if their present and allowed
        # 'simulate_principal_policy will 'flatten' out the permissions regardless of whether they
        # are the result of managed, inline or inherited policies.
        simulatePrincipalPolicyResp = iam.simulate_principal_policy(
            PolicyInputList=[],
            ActionNames=ssmSessionManagerPermissions,
            PolicySourceArn=getRoleResp['Role']['Arn']
        )

        # Iterate over the simulation results.
        for eval_result in simulatePrincipalPolicyResp['EvaluationResults']:
            LOG.debug(f"ssm_sm_permissions= {ssmSessionManagerPermissions}")

            # We role contained the action, either as an explicit 'Allow' or explicit 'Deny'
            # Remove from the search list
            ssmSessionManagerPermissions.remove(eval_result['EvalActionName'])

            # If the action is not explicitly allowed, record the action error. While not typical, its possible the required
            # set of actions could be spread out over multiple roles and/or managed policies
            if eval_result['EvalDecision'] != 'allowed':
                # Save the failed action and reason (explicitDeny | implicitdeny)
                actionErrors.append(f"{eval_result['EvalActionName']}: \'{eval_result['EvalDecision']}\'")
            
            # If we found all of required actions, stop looking
            LOG.debug(f"len(ssmSessionManagerPermissions): {len(ssmSessionManagerPermissions)}")
            if len(ssmSessionManagerPermissions) == 0:
                break

    # After iterating over the InstanceProfile roles, see if any SSM-SM required permissions unaccounted for
    if len(ssmSessionManagerPermissions) != 0:
        for action in ssmSessionManagerPermissions:
            LOG.debug(f"action={action}")
            actionErrors.append(f"{action}")

    LOG.debug(f"actionErrors={actionErrors}")

    if len(actionErrors) != 0:
        raise exceptions.NonCompliant(TYPE_NAME, f"{targetLogicalId}.IamInstanceProfile({iamInstanceProfileName}).Roles({roleName}) does not support minimum required Session Manager permissions: {', '.join(actionErrors)}")

    # Check if the instance has a SecurityGroupIds property (non-default VPC)
    sgPropName = "SecurityGroupIds"
    securityGroupIds = resourceProperties.get(sgPropName)
    if not securityGroupIds:

        # Check if the instance has a SecurityGroups property (EC2-Classic, default VPC)
        sgPropName = "SecurityGroups"
        securityGroupIds = resourceProperties.get(sgPropName)
        if not securityGroupIds:

            # Check if the instance has a NetworkInterfaces property. If so, iterate over the network interfaces
            # and grab all of the security group ids they reference. 
            sgPropName = "NetworkInterfaces"
            networkInterfaces = resourceProperties.get(sgPropName)
            if networkInterfaces:
                securityGroupIds = []
                for networkInterface in networkInterfaces:
                    securityGroupIds.append(networkInterface["GroupSet"])

    # Instance has security-group(s) defined
    if securityGroupIds:

        ec2 = session.client("ec2")

        # Using the EC2 instance ImageId, get the 'platform' property for the AMI. If its not found, implies 'not Windows'
        # otherwise check if explicitly Windows.
        describeImagesResp = ec2.describe_images(
            ImageIds=[
                resourceProperties.get("ImageId")
            ]
        )

        # Based on the AMI platform, select the security group ingress port to prevent:
        # Windows=3389 (RDP) otherwise 22 (SSH)
        for image in describeImagesResp["Images"]:
            ingressPort = "22/SSH"
            amiPlatform = image.get("platform")
            if amiPlatform and amiPlatform == "windows":
                ingressPort = "3389/RDP"
            break;

        # Retrieve the security group(s) filtering on ingress-rules that allow port 22 (SSH)
        describeSecurityGroupsResp = ec2.describe_security_groups(
            GroupIds=securityGroupIds,
            Filters=[
                {
                    "Name": "ip-permission.from-port",
                    "Values": [ingressPort.split("/")[0]]
                },
                {
                    "Name": "ip-permission.to-port",
                    "Values": [ingressPort.split("/")[0]]
                }
            ]
        )

        # Iterate over the returned list, failing on the first one found as there should not be any 
        # that allow port 22 (SSH) ingress.
        for securityGroup in describeSecurityGroupsResp["SecurityGroups"]:
            raise exceptions.NonCompliant(TYPE_NAME, f"{targetLogicalId}.{sgPropName} Security Group {securityGroup['GroupName']} contains an {ingressPort} ingress rule")

    return ProgressEvent(status = OperationStatus.SUCCESS, message = f"Success")

@hook.handler(HookInvocationPoint.CREATE_PRE_PROVISION)
def pre_create_handler(
        session: Optional[SessionProxy],
        request: HookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: TypeConfigurationModel
) -> ProgressEvent:

    LOG.debug(f"session: {session}")
    LOG.debug(f"request: {request}")
    LOG.debug(f"type_configuration: {type_configuration}")

    try:

        targetName = request.hookContext.targetName

        if targetName == "AWS::EC2::Instance":
            return _validate_ec2_ssmsm_only_access(session, request.hookContext, request.hookContext.targetModel.get("resourceProperties"), type_configuration)

        elif targetName == "AWS::EC2::LaunchTemplate":
            return _validate_ec2_ssmsm_only_access(session, request.hookContext, request.hookContext.targetModel.get("resourceProperties")['LaunchTemplateData'], type_configuration)
        
        else:
            raise exceptions.InvalidRequest(
                f"Unexpected target type: {targetName}")

    except exceptions._HandlerError as e:
        raise
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        LOG.debug(f"Unexpected exception: {e}")
        LOG.debug(exc_type, fname, exc_tb.tb_lineno)
        raise

@hook.handler(HookInvocationPoint.UPDATE_PRE_PROVISION)
def pre_update_handler(
        session: Optional[SessionProxy],
        request: BaseHookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: TypeConfigurationModel
) -> ProgressEvent:

    try:
        # Resource updates are checked same as creation
        return pre_create_handler(session, request, callback_context, type_configuration)

    except exceptions._HandlerError as e:
        raise
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        LOG.debug(f"Unexpected exception: {e}")
        LOG.debug(exc_type, fname, exc_tb.tb_lineno)
        raise
