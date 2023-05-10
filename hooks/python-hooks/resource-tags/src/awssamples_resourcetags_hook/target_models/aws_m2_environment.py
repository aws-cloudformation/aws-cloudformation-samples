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
class AwsM2Environment(BaseModel):
    Description: Optional[str]
    EngineType: Optional[str]
    EngineVersion: Optional[str]
    EnvironmentArn: Optional[str]
    EnvironmentId: Optional[str]
    HighAvailabilityConfig: Optional["_HighAvailabilityConfig"]
    InstanceType: Optional[str]
    KmsKeyId: Optional[str]
    Name: Optional[str]
    PreferredMaintenanceWindow: Optional[str]
    PubliclyAccessible: Optional[bool]
    SecurityGroupIds: Optional[Sequence[str]]
    StorageConfigurations: Optional[Sequence["_StorageConfiguration"]]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsM2Environment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsM2Environment"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            EngineType=json_data.get("EngineType"),
            EngineVersion=json_data.get("EngineVersion"),
            EnvironmentArn=json_data.get("EnvironmentArn"),
            EnvironmentId=json_data.get("EnvironmentId"),
            HighAvailabilityConfig=HighAvailabilityConfig._deserialize(json_data.get("HighAvailabilityConfig")),
            InstanceType=json_data.get("InstanceType"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Name=json_data.get("Name"),
            PreferredMaintenanceWindow=json_data.get("PreferredMaintenanceWindow"),
            PubliclyAccessible=json_data.get("PubliclyAccessible"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            StorageConfigurations=deserialize_list(json_data.get("StorageConfigurations"), StorageConfiguration),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsM2Environment = AwsM2Environment


@dataclass
class HighAvailabilityConfig(BaseModel):
    DesiredCapacity: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_HighAvailabilityConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HighAvailabilityConfig"]:
        if not json_data:
            return None
        return cls(
            DesiredCapacity=json_data.get("DesiredCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HighAvailabilityConfig = HighAvailabilityConfig


@dataclass
class StorageConfiguration(BaseModel):
    Efs: Optional["_EfsStorageConfiguration"]
    Fsx: Optional["_FsxStorageConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_StorageConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageConfiguration"]:
        if not json_data:
            return None
        return cls(
            Efs=EfsStorageConfiguration._deserialize(json_data.get("Efs")),
            Fsx=FsxStorageConfiguration._deserialize(json_data.get("Fsx")),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageConfiguration = StorageConfiguration


@dataclass
class EfsStorageConfiguration(BaseModel):
    FileSystemId: Optional[str]
    MountPoint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EfsStorageConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EfsStorageConfiguration"]:
        if not json_data:
            return None
        return cls(
            FileSystemId=json_data.get("FileSystemId"),
            MountPoint=json_data.get("MountPoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EfsStorageConfiguration = EfsStorageConfiguration


@dataclass
class FsxStorageConfiguration(BaseModel):
    FileSystemId: Optional[str]
    MountPoint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FsxStorageConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FsxStorageConfiguration"]:
        if not json_data:
            return None
        return cls(
            FileSystemId=json_data.get("FileSystemId"),
            MountPoint=json_data.get("MountPoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FsxStorageConfiguration = FsxStorageConfiguration


