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
class AwsWorkspacesWorkspace(BaseModel):
    Id: Optional[str]
    BundleId: Optional[str]
    DirectoryId: Optional[str]
    RootVolumeEncryptionEnabled: Optional[bool]
    Tags: Optional[Any]
    UserName: Optional[str]
    UserVolumeEncryptionEnabled: Optional[bool]
    VolumeEncryptionKey: Optional[str]
    WorkspaceProperties: Optional["_WorkspaceProperties"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsWorkspacesWorkspace"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsWorkspacesWorkspace"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            BundleId=json_data.get("BundleId"),
            DirectoryId=json_data.get("DirectoryId"),
            RootVolumeEncryptionEnabled=json_data.get("RootVolumeEncryptionEnabled"),
            Tags=json_data.get("Tags"),
            UserName=json_data.get("UserName"),
            UserVolumeEncryptionEnabled=json_data.get("UserVolumeEncryptionEnabled"),
            VolumeEncryptionKey=json_data.get("VolumeEncryptionKey"),
            WorkspaceProperties=WorkspaceProperties._deserialize(json_data.get("WorkspaceProperties")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsWorkspacesWorkspace = AwsWorkspacesWorkspace


@dataclass
class Tag(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


@dataclass
class WorkspaceProperties(BaseModel):
    ComputeTypeName: Optional[str]
    RootVolumeSizeGib: Optional[int]
    RunningMode: Optional[str]
    RunningModeAutoStopTimeoutInMinutes: Optional[int]
    UserVolumeSizeGib: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_WorkspaceProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkspaceProperties"]:
        if not json_data:
            return None
        return cls(
            ComputeTypeName=json_data.get("ComputeTypeName"),
            RootVolumeSizeGib=json_data.get("RootVolumeSizeGib"),
            RunningMode=json_data.get("RunningMode"),
            RunningModeAutoStopTimeoutInMinutes=json_data.get("RunningModeAutoStopTimeoutInMinutes"),
            UserVolumeSizeGib=json_data.get("UserVolumeSizeGib"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkspaceProperties = WorkspaceProperties


