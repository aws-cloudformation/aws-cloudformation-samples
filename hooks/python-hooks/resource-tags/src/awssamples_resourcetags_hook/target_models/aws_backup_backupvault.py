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
class AwsBackupBackupvault(BaseModel):
    AccessPolicy: Optional[Any]
    BackupVaultName: Optional[str]
    BackupVaultTags: Optional[MutableMapping[str, str]]
    EncryptionKeyArn: Optional[str]
    Notifications: Optional["_NotificationObjectType"]
    LockConfiguration: Optional["_LockConfigurationType"]
    BackupVaultArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsBackupBackupvault"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsBackupBackupvault"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AccessPolicy=json_data.get("AccessPolicy"),
            BackupVaultName=json_data.get("BackupVaultName"),
            BackupVaultTags=json_data.get("BackupVaultTags"),
            EncryptionKeyArn=json_data.get("EncryptionKeyArn"),
            Notifications=NotificationObjectType._deserialize(json_data.get("Notifications")),
            LockConfiguration=LockConfigurationType._deserialize(json_data.get("LockConfiguration")),
            BackupVaultArn=json_data.get("BackupVaultArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsBackupBackupvault = AwsBackupBackupvault


@dataclass
class NotificationObjectType(BaseModel):
    BackupVaultEvents: Optional[Sequence[str]]
    SNSTopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationObjectType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationObjectType"]:
        if not json_data:
            return None
        return cls(
            BackupVaultEvents=json_data.get("BackupVaultEvents"),
            SNSTopicArn=json_data.get("SNSTopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationObjectType = NotificationObjectType


@dataclass
class LockConfigurationType(BaseModel):
    MinRetentionDays: Optional[int]
    MaxRetentionDays: Optional[int]
    ChangeableForDays: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_LockConfigurationType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LockConfigurationType"]:
        if not json_data:
            return None
        return cls(
            MinRetentionDays=json_data.get("MinRetentionDays"),
            MaxRetentionDays=json_data.get("MaxRetentionDays"),
            ChangeableForDays=json_data.get("ChangeableForDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LockConfigurationType = LockConfigurationType


