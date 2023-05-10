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
class AwsEfsFilesystem(BaseModel):
    FileSystemId: Optional[str]
    Arn: Optional[str]
    Encrypted: Optional[bool]
    FileSystemTags: Optional[Sequence["_ElasticFileSystemTag"]]
    KmsKeyId: Optional[str]
    LifecyclePolicies: Optional[Sequence["_LifecyclePolicy"]]
    PerformanceMode: Optional[str]
    ProvisionedThroughputInMibps: Optional[float]
    ThroughputMode: Optional[str]
    FileSystemPolicy: Optional[MutableMapping[str, Any]]
    BypassPolicyLockoutSafetyCheck: Optional[bool]
    BackupPolicy: Optional["_BackupPolicy"]
    AvailabilityZoneName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEfsFilesystem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEfsFilesystem"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            FileSystemId=json_data.get("FileSystemId"),
            Arn=json_data.get("Arn"),
            Encrypted=json_data.get("Encrypted"),
            FileSystemTags=deserialize_list(json_data.get("FileSystemTags"), ElasticFileSystemTag),
            KmsKeyId=json_data.get("KmsKeyId"),
            LifecyclePolicies=deserialize_list(json_data.get("LifecyclePolicies"), LifecyclePolicy),
            PerformanceMode=json_data.get("PerformanceMode"),
            ProvisionedThroughputInMibps=json_data.get("ProvisionedThroughputInMibps"),
            ThroughputMode=json_data.get("ThroughputMode"),
            FileSystemPolicy=json_data.get("FileSystemPolicy"),
            BypassPolicyLockoutSafetyCheck=json_data.get("BypassPolicyLockoutSafetyCheck"),
            BackupPolicy=BackupPolicy._deserialize(json_data.get("BackupPolicy")),
            AvailabilityZoneName=json_data.get("AvailabilityZoneName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEfsFilesystem = AwsEfsFilesystem


@dataclass
class ElasticFileSystemTag(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticFileSystemTag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticFileSystemTag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticFileSystemTag = ElasticFileSystemTag


@dataclass
class LifecyclePolicy(BaseModel):
    TransitionToIA: Optional[str]
    TransitionToPrimaryStorageClass: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LifecyclePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecyclePolicy"]:
        if not json_data:
            return None
        return cls(
            TransitionToIA=json_data.get("TransitionToIA"),
            TransitionToPrimaryStorageClass=json_data.get("TransitionToPrimaryStorageClass"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecyclePolicy = LifecyclePolicy


@dataclass
class BackupPolicy(BaseModel):
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackupPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupPolicy"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupPolicy = BackupPolicy


