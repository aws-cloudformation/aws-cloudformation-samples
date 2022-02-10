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
TYPE_NAME = "AWSSamples::EksClusterLogging::Hook"

hook = Hook(TYPE_NAME, TypeConfigurationModel)
test_entrypoint = hook.test_entrypoint

supported_types = ["AWS::EKS::Cluster"]
required_log_types = {"audit", "authenticator"}


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

    # object structure is strangely complex, simplifying down to a set of strings
    defined_log_types = cfn_model.get('Logging', {}).get("ClusterLogging", {}).get("EnabledTypes", [])
    defined_log_types = {v['Type'] for v in defined_log_types}

    is_compliant = required_log_types.issubset(defined_log_types)

    # Fail if log types required are not in the log types set
    if not is_compliant:
        return non_compliant(f"EKS Clusters should have at least {required_log_types} set")

    # Operation is compliant, return success
    LOG.debug("returning SUCCESS")
    return ProgressEvent(status=OperationStatus.SUCCESS)
