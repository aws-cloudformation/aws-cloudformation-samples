# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass

from cloudformation_cli_python_lib.interface import BaseModel
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

import sys
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class AwsBackupBackupplan(BaseModel):
    BackupPlan: Optional["_BackupPlanResourceType"]
    BackupPlanTags: Optional[MutableMapping[str, str]]
    BackupPlanArn: Optional[str]
    BackupPlanId: Optional[str]
    VersionId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsBackupBackupplan"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsBackupBackupplan"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            BackupPlan=BackupPlanResourceType._deserialize(json_data.get("BackupPlan")),
            BackupPlanTags=json_data.get("BackupPlanTags"),
            BackupPlanArn=json_data.get("BackupPlanArn"),
            BackupPlanId=json_data.get("BackupPlanId"),
            VersionId=json_data.get("VersionId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsBackupBackupplan = AwsBackupBackupplan


@dataclass
class BackupPlanResourceType(BaseModel):
    BackupPlanName: Optional[str]
    AdvancedBackupSettings: Optional[Sequence["_AdvancedBackupSettingResourceType"]]
    BackupPlanRule: Optional[Sequence["_BackupRuleResourceType"]]

    @classmethod
    def _deserialize(
        cls: Type["_BackupPlanResourceType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupPlanResourceType"]:
        if not json_data:
            return None
        return cls(
            BackupPlanName=json_data.get("BackupPlanName"),
            AdvancedBackupSettings=deserialize_list(json_data.get("AdvancedBackupSettings"), AdvancedBackupSettingResourceType),
            BackupPlanRule=deserialize_list(json_data.get("BackupPlanRule"), BackupRuleResourceType),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupPlanResourceType = BackupPlanResourceType


@dataclass
class AdvancedBackupSettingResourceType(BaseModel):
    BackupOptions: Optional[MutableMapping[str, Any]]
    ResourceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedBackupSettingResourceType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedBackupSettingResourceType"]:
        if not json_data:
            return None
        return cls(
            BackupOptions=json_data.get("BackupOptions"),
            ResourceType=json_data.get("ResourceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedBackupSettingResourceType = AdvancedBackupSettingResourceType


@dataclass
class BackupRuleResourceType(BaseModel):
    RuleName: Optional[str]
    TargetBackupVault: Optional[str]
    StartWindowMinutes: Optional[float]
    CompletionWindowMinutes: Optional[float]
    ScheduleExpression: Optional[str]
    RecoveryPointTags: Optional[MutableMapping[str, str]]
    CopyActions: Optional[Sequence["_CopyActionResourceType"]]
    Lifecycle: Optional["_LifecycleResourceType"]
    EnableContinuousBackup: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_BackupRuleResourceType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupRuleResourceType"]:
        if not json_data:
            return None
        return cls(
            RuleName=json_data.get("RuleName"),
            TargetBackupVault=json_data.get("TargetBackupVault"),
            StartWindowMinutes=json_data.get("StartWindowMinutes"),
            CompletionWindowMinutes=json_data.get("CompletionWindowMinutes"),
            ScheduleExpression=json_data.get("ScheduleExpression"),
            RecoveryPointTags=json_data.get("RecoveryPointTags"),
            CopyActions=deserialize_list(json_data.get("CopyActions"), CopyActionResourceType),
            Lifecycle=LifecycleResourceType._deserialize(json_data.get("Lifecycle")),
            EnableContinuousBackup=json_data.get("EnableContinuousBackup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupRuleResourceType = BackupRuleResourceType


@dataclass
class CopyActionResourceType(BaseModel):
    Lifecycle: Optional["_LifecycleResourceType"]
    DestinationBackupVaultArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CopyActionResourceType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CopyActionResourceType"]:
        if not json_data:
            return None
        return cls(
            Lifecycle=LifecycleResourceType._deserialize(json_data.get("Lifecycle")),
            DestinationBackupVaultArn=json_data.get("DestinationBackupVaultArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CopyActionResourceType = CopyActionResourceType


@dataclass
class LifecycleResourceType(BaseModel):
    MoveToColdStorageAfterDays: Optional[float]
    DeleteAfterDays: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LifecycleResourceType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecycleResourceType"]:
        if not json_data:
            return None
        return cls(
            MoveToColdStorageAfterDays=json_data.get("MoveToColdStorageAfterDays"),
            DeleteAfterDays=json_data.get("DeleteAfterDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecycleResourceType = LifecycleResourceType


