import logging

from cloudformation_cli_python_lib import (
    HandlerErrorCode,
    Hook,
    HookInvocationPoint,
    OperationStatus,
    ProgressEvent
)

from .models import HookHandlerRequest, TypeConfigurationModel

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "AWSSamples::SecurityGroupOpenIngress::Hook"

hook = Hook(TYPE_NAME, TypeConfigurationModel)
test_entrypoint = hook.test_entrypoint

supported_types = ["AWS::EC2::SecurityGroup", "AWS::EC2::SecurityGroupIngress"]


def non_compliant(msg):
    LOG.debug(f"returning FAILED: {HandlerErrorCode.NonCompliant} {msg}")
    return ProgressEvent(
            status=OperationStatus.FAILED,
            errorCode=HandlerErrorCode.NonCompliant,
            message=msg
        )


def is_open(sg_list):
    for sg in sg_list:
        if sg.get('CidrIp') == '0.0.0.0/0' or sg.get('CidrIpv6') == '::/0':
            return True
    return False


@hook.handler(HookInvocationPoint.CREATE_PRE_PROVISION)
@hook.handler(HookInvocationPoint.UPDATE_PRE_PROVISION)
def pre_handler(_s, request: HookHandlerRequest, _c, type_configuration: TypeConfigurationModel) -> ProgressEvent:
    LOG.setLevel(logging.DEBUG)
    LOG.debug(f"request: {request.__dict__}")
    LOG.debug(f"type_configuration: {type_configuration.__dict__ if type_configuration else dict()}")

    cfn_model = request.hookContext.targetModel.get("resourceProperties", {})
    cfn_type = request.hookContext.targetName

    # If we get a type that we don't care about, we should return InvalidRequest
    if cfn_type not in supported_types:
        LOG.error("returning invalidRequest")
        return ProgressEvent(
            status=OperationStatus.FAILED,
            errorCode=HandlerErrorCode.InvalidRequest,
            message=f"This hook only supports {supported_types}"
        )

    if cfn_type == "AWS::EC2::SecurityGroup":
        security_groups = cfn_model.get("SecurityGroupIngress", [])
    else:
        security_groups = [cfn_model] if cfn_model else []

    # Fail if an open ingress rule is found
    if is_open(security_groups):
        return non_compliant("Security Group cannot contain rules allow all destinations (0.0.0.0/0 or ::/0)")

    # Operation is compliant, return success
    LOG.debug("returning SUCCESS")
    return ProgressEvent(status=OperationStatus.SUCCESS)
