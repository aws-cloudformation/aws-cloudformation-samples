from importlib.abc import ResourceReader
import logging
import os
import sys
from typing import Any, MutableMapping, Optional

from cloudformation_cli_python_lib import (
    BaseHookHandlerRequest,
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

def _validate_ec2_ssmsm_only_access(session, hookContext, resourceProperties, typeConfiguration):

    try:
    
        targetFriendlyName = f"{hookContext.targetName}({hookContext.targetLogicalId})"

        # Make sure the instance has properties defined
        if not resourceProperties:
            raise exceptions.InvalidRequest(f"{targetFriendlyName}: Resource properties for target model are empty")
           
        # Check if the instance has a IAMInstanceProfile property defined
        iamInstanceProfileName = resourceProperties.get("IamInstanceProfile")

        # Make sure we have a non-empty instance profile name
        if not iamInstanceProfileName or (iamInstanceProfileName == ""):
            raise exceptions.InvalidRequest(f"{targetFriendlyName}: InstanceProfileName property missing or empty value")

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
                raise exceptions.InvalidRequest(f"{targetFriendlyName}: Referenced InstanceProfileName's Roles property missing or empty value")

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
            raise exceptions.InvalidRequest(f"{targetFriendlyName}: Referenced InstanceProfileName's Role does not support minimum required Session Manager permissions: {', '.join(actionErrors)}")

        # Check if the instance has a SecurityGroupIds property (non-default VPC)
        securityGroupIds = resourceProperties.get("SecurityGroupIds")
        if not securityGroupIds:

            # Check if the instance has a SecurityGroups property (EC2-Classic, default VPC)
            securityGroupIds = resourceProperties.get("SecurityGroups")
            if not securityGroupIds:

                # Check if the instance has a NetworkInterfaces property. If so, iterate over the network interfaces
                # and grab all of the security group ids they reference. 
                networkInterfaces = resourceProperties.get("NetworkInterfaces")
                if networkInterfaces:
                    securityGroupIds = []
                    for networInterface in networkInterfaces:
                        securityGroupIds.append(networInterface["GroupSet"])

        # Instance has security-group(s) defined
        if securityGroupIds:

            # Retrieve the security group(s) filtering on ingress-rules that allow port 22 (SSH)
            ec2 = session.client("ec2")
            describeSecurityGroupsResp = ec2.describe_security_groups(
                GroupIds=securityGroupIds,
                Filters=[
                    {
                        "Name": "ip-permission.from-port",
                        "Values": ["22"]
                    },
                    {
                        "Name": "ip-permission.to-port",
                        "Values": ["22"]
                    }
                ]
            )

            # Iterate over the returned list, failing on the first one found as there should not be any 
            # that allow port 22 (SSH) ingress.
            for securityGroup in describeSecurityGroupsResp["SecurityGroups"]:
                raise exceptions.InvalidRequest(f"{targetFriendlyName}: Security GroupName {securityGroup['GroupName']} contains an SSH ingress rule")

        return ProgressEvent(status = OperationStatus.SUCCESS, message = f"Success")

    except Exception as e:
        LOG.debug(f"Unexpected exception: {e}")
        raise

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

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        LOG.debug(f"Unexpected exception: {e}")
        LOG.debug(exc_type, fname, exc_tb.tb_lineno)

        raise

""" # Use-case0 Request
# InstanceProfileName property missing or empty value
#
request = BaseHookHandlerRequest(
    clientRequestToken='32be1c5f-113a-427d-9ec5-e511fa34068a',
    hookContext=HookContext(
        awsAccountId='094559051528',
        stackId='arn:aws:cloudformation:us-west-2:094559051528:stack/xx/7add7a20-2b17-11ec-b3fa-025543d413f7',
        hookTypeName='skellishAws::EC2::EnforceSsmHook',
        hookTypeVersion='00000045',
        invocationPoint=HookInvocationPoint.CREATE_PRE_PROVISION,
        targetName='AWS::EC2::Instance',
        targetType='AWS::EC2::Instance',
        targetLogicalId='EC2Instance',
        targetModel={
            'resourceProperties': {
                'ImageId': 'ami-0c2d06d50ce30b442',
                'InstanceType': 't3.medium'
            },
            'previousResourceProperties': None
        },
        changeSetId=None
    )
)

# Use-case0 Request
# MyInstanceRoleWithManagedPolicyRole: Success
#
request = BaseHookHandlerRequest(
    clientRequestToken='32be1c5f-113a-427d-9ec5-e511fa34068a',
    hookContext=HookContext(
        awsAccountId='094559051528',
        stackId='arn:aws:cloudformation:us-west-2:094559051528:stack/xx/7add7a20-2b17-11ec-b3fa-025543d413f7',
        hookTypeName='skellishAws::EC2::EnforceSsmHook',
        hookTypeVersion='00000045',
        invocationPoint=HookInvocationPoint.CREATE_PRE_PROVISION,
        targetName='AWS::EC2::Instance',
        targetType='AWS::EC2::Instance',
        targetLogicalId='EC2Instance',
        targetModel={
            'resourceProperties': {
                'ImageId': 'ami-0c2d06d50ce30b442',
                'InstanceType': 't3.medium',
                'IamInstanceProfile': 'MyInstanceRoleWithManagedPolicyRole'
            },
            'previousResourceProperties': None
        },
        changeSetId=None
    )
)

# Use-case0 Request
# MyInstanceRoleWithManualPolicyRole: Success
#
request = BaseHookHandlerRequest(
    clientRequestToken='32be1c5f-113a-427d-9ec5-e511fa34068a',
    hookContext=HookContext(
        awsAccountId='094559051528',
        stackId='arn:aws:cloudformation:us-west-2:094559051528:stack/xx/7add7a20-2b17-11ec-b3fa-025543d413f7',
        hookTypeName='skellishAws::EC2::EnforceSsmHook',
        hookTypeVersion='00000045',
        invocationPoint=HookInvocationPoint.CREATE_PRE_PROVISION,
        targetName='AWS::EC2::Instance',
        targetType='AWS::EC2::Instance',
        targetLogicalId='EC2Instance',
        targetModel={
            'resourceProperties': {
                'ImageId': 'ami-0c2d06d50ce30b442',
                'InstanceType': 't3.medium',
                'IamInstanceProfile': 'MyInstanceRoleWithManualPolicyRole'
            },
            'previousResourceProperties': None
        },
        changeSetId=None
    )
)

request = BaseHookHandlerRequest(
    clientRequestToken='b35d7f1f-305c-4954-a7d7-4bb6d108f9f0', 
    hookContext=HookContext(
        awsAccountId='094559051528', 
        stackId='arn:aws:cloudformation:us-west-2:094559051528:stack/t1/2a9390a0-4673-11ec-bbd9-02f9de4065db', 
        hookTypeName='AWSSamples::Ec2SsmSmOnly::Hook', 
        hookTypeVersion='00000018', 
        invocationPoint=HookInvocationPoint.CREATE_PRE_PROVISION, 
        targetName='AWS::EC2::Instance', 
        targetType='AWS::EC2::Instance', 
        targetLogicalId='EC2Instance', 
        targetModel={
            'resourceProperties': {
                'ImageId': 'ami-0c2d06d50ce30b442', 
                'IamInstanceProfile': 't1-MyInstanceProfile-M0OE1I8SBSLG', 
                'SubnetId': 'subnet-00f149d595bf820cc', 
                'InstanceType': 't3.medium', 
                'SecurityGroupIds': [
                    'sg-09ef7fb3532fad6cf',
                    'sg-05db4665c8e7c3823'
                ]
            }, 
            'previousResourceProperties': None
        }, 
        changeSetId=None
    )
)

type_configuration = TypeConfigurationModel(
    requireSessionManagerEncryption=False
)

session = boto3.session.Session()

try:
    hookResult = pre_create_handler(
        SessionProxy(session),
        request,
        None,
        type_configuration
    )
    print(hookResult)
except Exception as e:
    print(e)
    raise
 """