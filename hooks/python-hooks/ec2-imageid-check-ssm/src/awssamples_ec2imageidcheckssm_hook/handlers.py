import logging
from typing import Any, MutableMapping, Optional

from cloudformation_cli_python_lib import (
    HandlerErrorCode,
    Hook,
    HookInvocationPoint,
    OperationStatus,
    ProgressEvent,
    SessionProxy,
)
from .models import HookHandlerRequest, TypeConfigurationModel

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "AWSSamples::Ec2ImageIdCheckSsm::Hook"

# Set the logging level
LOG.setLevel(logging.INFO)  # or LOG.setLevel(logging.DEBUG)

hook = Hook(TYPE_NAME, TypeConfigurationModel)
test_entrypoint = hook.test_entrypoint


def _validate_ec2_instance_imageid(progress, target_name, resource_properties, ssm_key, session):
    try:
        if resource_properties:
            LOG.debug(f"DEBUG Details of resource_properties: {resource_properties}")

            # Get the name of the EC2 instance based on tag
            instance_tags = resource_properties.get("Tags")
            instance_name = None
            if instance_tags is not None:
                instance_name_tag = next(filter(lambda x: x['Key'] == 'Name', instance_tags))
                instance_name = instance_name_tag.get("Value")

            if instance_name is None:
                instance_name = "NameTagNotSet"
                LOG.debug(f"DEBUG Could not find the Tag 'Name'. Setting the EC2 Instance name to {instance_name}")
            else:
                LOG.debug(f"DEBUG EC2 Instance has the following name tag {instance_name}")

            # Get the ImageID of the AMI for the EC2 instance based on tag
            instance_imageid = resource_properties.get("ImageId")
            LOG.debug(f"DEBUG EC2 Instance has the following ImageID {instance_imageid}")

            # Get the expected ImageID from SSM Parameter Store
            client = session.client('ssm')
            LOG.info(f"getting ssm parameter store value for {ssm_key}")
            expected_imageid_ssm = client.get_parameter(
                Name=ssm_key,
                WithDecryption=True
            )
            expected_imageid = expected_imageid_ssm.get("Parameter", {}).get("Value")

            LOG.debug(f"DEBUG Verifying EC2 Instance ImageId for target {target_name}, expecting target to have "
                      f"ImageId {expected_imageid}.")

            if expected_imageid == instance_imageid:
                progress.status = OperationStatus.SUCCESS
                progress.message = f"Successfully invoked HookHandler for target {target_name} with name: " \
                                   f"{instance_name}. ImageId {instance_imageid} matches the required AMI"
            else:
                progress.status = OperationStatus.FAILED
                progress.message = f"Failed to verify ImageId for EC2 instance {instance_name}. Expected ImageId to " \
                                   f"be {expected_imageid}, actual ImageId is {instance_imageid}."
                progress.errorCode = HandlerErrorCode.NonCompliant

        else:
            progress.status = OperationStatus.FAILED
            progress.message = f"Failed to verify ImageId for target {target_name}."
            progress.errorCode = HandlerErrorCode.InternalFailure

    except TypeError as e:
        progress.status = OperationStatus.FAILED
        progress.message = f"was not expecting type {e}."
        progress.errorCode = HandlerErrorCode.InternalFailure

    LOG.info(f"Results Message: {progress.message}")

    return progress


@hook.handler(HookInvocationPoint.CREATE_PRE_PROVISION)
def pre_create_handler(
        session: Optional[SessionProxy],
        request: HookHandlerRequest,
        _callback_context: MutableMapping[str, Any],
        type_configuration: TypeConfigurationModel
) -> ProgressEvent:
    target_name = request.hookContext.targetName
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS
    )

    # Make sure this hook is running against the expected resource type
    if "AWS::EC2::Instance" == target_name:
        LOG.info(f"Successfully invoked PreCreateHookHandler for target {target_name}")
        LOG.debug(f"DEBUG SSM Parameter Store Key location for compliant ImageID: {type_configuration.SsmKey}")
        return _validate_ec2_instance_imageid(
            progress,
            target_name,
            request.hookContext.targetModel.get("resourceProperties"),
            type_configuration.SsmKey,
            session
        )
    else:
        return ProgressEvent.failed(HandlerErrorCode.InternalFailure, f"Unknown target type: {target_name}")
