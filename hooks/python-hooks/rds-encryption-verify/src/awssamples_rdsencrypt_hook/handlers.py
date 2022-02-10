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
TYPE_NAME = "AWSSamples::RdsEncrypt::Hook"

# Set the logging level
LOG.setLevel(logging.INFO)

hook = Hook(TYPE_NAME, TypeConfigurationModel)
test_entrypoint = hook.test_entrypoint


def _validate_rds_encryption(progress, target_name, resource_properties, excludeDBInstanceClassList):
    try:
        if resource_properties:
            LOG.debug(f"Details of resource_properties: {resource_properties}")
            is_rds_encrypt = resource_properties.get("StorageEncrypted")
            rds_instance_class= resource_properties.get("DBInstanceClass")
            
            LOG.debug(f"rds_instance_class value: {rds_instance_class}")
            LOG.debug(f"excludeDBInstanceClassList value: {excludeDBInstanceClassList}")
            
            # Passthrough if the RDS instance is part of excludeDBInstanceClassList; verify encryption status for all other DB classes
            if (rds_instance_class in excludeDBInstanceClassList or (is_rds_encrypt and is_rds_encrypt.lower() == 'true')):
                LOG.debug(f"is_rds_encrypt value: {is_rds_encrypt}")
                progress.status = OperationStatus.SUCCESS
                progress.message = f"Successfully invoked HookHandler for target {target_name}. Resource encrypted as expected"
            else: 
                LOG.debug(f"Noncompliant resource due to StorageEncrypted empty or false")
                progress.status = OperationStatus.FAILED
                progress.message = f"Failed Hook due to missing or non-encrypted {target_name} resource."
                progress.errorCode = HandlerErrorCode.NonCompliant
            
    except TypeError as e:
        # catch all exception and mark Hook status as failure
        progress.status = OperationStatus.FAILED
        progress.message = f"was not expecting type {e}."
        progress.errorCode = HandlerErrorCode.InternalFailure

    LOG.info(f"Results Message: {progress.message}")

    return progress


@hook.handler(HookInvocationPoint.CREATE_PRE_PROVISION)
def pre_create_handler(
        session: Optional[SessionProxy],
        request: HookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: TypeConfigurationModel
) -> ProgressEvent:
    target_model = request.hookContext.targetModel
    target_name = request.hookContext.targetName
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS
    )
    # This hook only validates non-aurora DB instances. Aurora cluster define encryption at the DBCluster resource type
    if "AWS::RDS::DBInstance" == target_name:
        LOG.info(f"Triggered PreCreateHookHandler for target {target_name}")
        return _validate_rds_encryption(progress, target_name, target_model.get("resourceProperties"), type_configuration.excludeDBInstanceClassList) 
    else:
        raise exceptions.InvalidRequest(f"Unknown target type: {target_name}")


@hook.handler(HookInvocationPoint.UPDATE_PRE_PROVISION)
def pre_update_handler(
        session: Optional[SessionProxy],
        request: BaseHookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: TypeConfigurationModel
) -> ProgressEvent:
    target_model = request.hookContext.targetModel
    target_name = request.hookContext.targetName
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS
    )
    
    if "AWS::RDS::DBInstance" == target_name:
        LOG.info(f"Triggered PreUpdateHookHandler for target {target_name}")
        return _validate_rds_encryption(progress, target_name, target_model.get("resourceProperties"), type_configuration.excludeDBInstanceClassList) 
    else:
        raise exceptions.InvalidRequest(f"Unknown target type: {target_name}")


@hook.handler(HookInvocationPoint.DELETE_PRE_PROVISION)
def pre_delete_handler(
        session: Optional[SessionProxy],
        request: BaseHookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: TypeConfigurationModel
) -> ProgressEvent:
    return ProgressEvent(
        status=OperationStatus.SUCCESS
    )
