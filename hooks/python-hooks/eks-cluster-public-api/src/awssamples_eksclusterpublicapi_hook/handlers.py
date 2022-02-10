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
TYPE_NAME = "AWSSamples::EksClusterPublicApi::Hook"

hook = Hook(TYPE_NAME, TypeConfigurationModel)
test_entrypoint = hook.test_entrypoint

supported_types = ["AWS::EKS::Cluster"]


def non_compliant(msg):
    LOG.debug(f"returning FAILED: {HandlerErrorCode.NonCompliant} {msg}")
    return ProgressEvent(
            status=OperationStatus.FAILED,
            errorCode=HandlerErrorCode.NonCompliant,
            message=msg
        )


@hook.handler(HookInvocationPoint.CREATE_PRE_PROVISION)
@hook.handler(HookInvocationPoint.UPDATE_PRE_PROVISION)
def pre_handler(_s, request: HookHandlerRequest, _c, type_configuration: TypeConfigurationModel) -> ProgressEvent:
    LOG.setLevel(logging.DEBUG)
    LOG.debug(f"request: {request.__dict__}")
    LOG.debug(f"type_configuration: {type_configuration.__dict__ if type_configuration else dict()}")

    cfn_model = request.hookContext.targetModel.get("resourceProperties", {})

    # If we get a type that we don't care about, we should return InvalidRequest
    if request.hookContext.targetName not in supported_types:
        LOG.error("returning invalidRequest")
        return ProgressEvent(
            status=OperationStatus.FAILED,
            errorCode=HandlerErrorCode.InvalidRequest,
            message=f"This hook only supports {supported_types}"
        )

    # If EndpointPublicAccess is not defined is default's to True
    is_public = cfn_model.get("ResourcesVpcConfig", {}).get("EndpointPublicAccess", "true")

    # cloudformation casts bools to strings, so we've got to cast it back
    is_public = True if is_public.lower() == "true" else False

    # Fail if an open ingress rule is found
    if is_public:
        return non_compliant("EKS Clusters cannot have public endpoint enabled. To disable, set the "
                             "EndpointPublicAccess property of ResourcesVpcConfig to false")

    # Operation is compliant, return success
    LOG.debug("returning SUCCESS")
    return ProgressEvent(status=OperationStatus.SUCCESS)
