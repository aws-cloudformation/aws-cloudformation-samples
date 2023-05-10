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
class AwsDatasyncLocationfsxopenzfs(BaseModel):
    FsxFilesystemArn: Optional[str]
    SecurityGroupArns: Optional[Sequence[str]]
    Protocol: Optional["_Protocol"]
    Subdirectory: Optional[str]
    Tags: Optional[Any]
    LocationArn: Optional[str]
    LocationUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDatasyncLocationfsxopenzfs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDatasyncLocationfsxopenzfs"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            FsxFilesystemArn=json_data.get("FsxFilesystemArn"),
            SecurityGroupArns=json_data.get("SecurityGroupArns"),
            Protocol=Protocol._deserialize(json_data.get("Protocol")),
            Subdirectory=json_data.get("Subdirectory"),
            Tags=json_data.get("Tags"),
            LocationArn=json_data.get("LocationArn"),
            LocationUri=json_data.get("LocationUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDatasyncLocationfsxopenzfs = AwsDatasyncLocationfsxopenzfs


@dataclass
class Protocol(BaseModel):
    NFS: Optional["_NFS"]

    @classmethod
    def _deserialize(
        cls: Type["_Protocol"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Protocol"]:
        if not json_data:
            return None
        return cls(
            NFS=NFS._deserialize(json_data.get("NFS")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Protocol = Protocol


@dataclass
class NFS(BaseModel):
    MountOptions: Optional["_MountOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_NFS"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NFS"]:
        if not json_data:
            return None
        return cls(
            MountOptions=MountOptions._deserialize(json_data.get("MountOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NFS = NFS


@dataclass
class MountOptions(BaseModel):
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MountOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MountOptions"]:
        if not json_data:
            return None
        return cls(
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MountOptions = MountOptions


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


