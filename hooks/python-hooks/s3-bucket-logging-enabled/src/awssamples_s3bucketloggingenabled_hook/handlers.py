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
TYPE_NAME = "AWSSamples::S3BucketLoggingEnabled::Hook"

hook = Hook(TYPE_NAME, TypeConfigurationModel)
test_entrypoint = hook.test_entrypoint

supported_types = ["AWS::S3::Bucket"]


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

    target_model = request.hookContext.targetModel
    # If we get a type that we don't care about, we should return InvalidRequest
    if request.hookContext.targetName not in supported_types:
        LOG.error("returning invalidRequest")
        return ProgressEvent(
            status=OperationStatus.FAILED,
            errorCode=HandlerErrorCode.InvalidRequest,
            message=f"This hook only supports {supported_types}"
        )

    bucket_name = target_model.get("resourceProperties", {}).get("BucketName")
    logging_configuration = target_model.get("resourceProperties", {}).get("LoggingConfiguration")
    # type configuration can be None sometimes. If it is, create a config with defaults.
    if not type_configuration:
        type_configuration = TypeConfigurationModel(DestinationBucketName="", LogFilePrefix="")

    expected_logging_bucket_name = type_configuration.DestinationBucketName
    expected_logging_prefix: str = type_configuration.LogFilePrefix if type_configuration.LogFilePrefix else ""
    actual_logging_bucket = logging_configuration.get("DestinationBucketName") if logging_configuration else None
    actual_logging_prefix = logging_configuration.get("LogFilePrefix") if logging_configuration else None

    # if bucket name replacement is in the required logging prefix, then we must enforce BucketName to be set
    # because dynamic properties have not been resolved by CloudFormation at the time of pre-hook execution
    if not bucket_name and "%BUCKET_NAME%" in expected_logging_prefix:
        return non_compliant(f"The BucketName property must be set, LoggingConfiguration enabled and LogFilePrefix "
                             f"must be configured to {expected_logging_prefix}")
    expected_logging_prefix = expected_logging_prefix.replace("%BUCKET_NAME%", bucket_name if bucket_name else "")

    # Fail if specific DestinationBucketName and LogFilePrefix values are required and the actual values do not match
    if expected_logging_prefix \
            and expected_logging_prefix != actual_logging_prefix \
            and expected_logging_bucket_name \
            and expected_logging_bucket_name != actual_logging_bucket:
        return non_compliant(f"LoggingConfiguration must be enabled, DestinationBucketName must be configured "
                             f"to {expected_logging_bucket_name} and LogFilePrefix must be configured "
                             f"to {expected_logging_prefix}")

    # Fail if a specific LogFilePrefix is required and the actual value does not match
    if expected_logging_prefix and expected_logging_prefix != actual_logging_prefix:
        return non_compliant(f"LoggingConfiguration must be enabled and LogFilePrefix must be configured "
                             f"to {expected_logging_prefix}")

    # Fail if a specific DestinationBucketName is required and the actual value does not match
    if expected_logging_bucket_name and expected_logging_bucket_name != actual_logging_bucket:
        return non_compliant(f"LoggingConfiguration must be enabled and DestinationBucketName must be configured "
                             f"to {expected_logging_bucket_name}")

    # Fail if logging is not enabled
    if logging_configuration is None:
        return non_compliant("LoggingConfiguration must be enabled")

    # Operation is compliant, return success
    LOG.debug("returning SUCCESS")
    return ProgressEvent(status=OperationStatus.SUCCESS)
