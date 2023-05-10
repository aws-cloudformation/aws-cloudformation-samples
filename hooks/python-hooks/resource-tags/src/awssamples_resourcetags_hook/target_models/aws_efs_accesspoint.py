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
class AwsEfsAccesspoint(BaseModel):
    AccessPointId: Optional[str]
    Arn: Optional[str]
    ClientToken: Optional[str]
    AccessPointTags: Optional[AbstractSet["_AccessPointTag"]]
    FileSystemId: Optional[str]
    PosixUser: Optional["_PosixUser"]
    RootDirectory: Optional["_RootDirectory"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEfsAccesspoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEfsAccesspoint"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AccessPointId=json_data.get("AccessPointId"),
            Arn=json_data.get("Arn"),
            ClientToken=json_data.get("ClientToken"),
            AccessPointTags=set_or_none(json_data.get("AccessPointTags")),
            FileSystemId=json_data.get("FileSystemId"),
            PosixUser=PosixUser._deserialize(json_data.get("PosixUser")),
            RootDirectory=RootDirectory._deserialize(json_data.get("RootDirectory")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEfsAccesspoint = AwsEfsAccesspoint


@dataclass
class AccessPointTag(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessPointTag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessPointTag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessPointTag = AccessPointTag


@dataclass
class PosixUser(BaseModel):
    Uid: Optional[str]
    Gid: Optional[str]
    SecondaryGids: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PosixUser"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PosixUser"]:
        if not json_data:
            return None
        return cls(
            Uid=json_data.get("Uid"),
            Gid=json_data.get("Gid"),
            SecondaryGids=json_data.get("SecondaryGids"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PosixUser = PosixUser


@dataclass
class RootDirectory(BaseModel):
    Path: Optional[str]
    CreationInfo: Optional["_CreationInfo"]

    @classmethod
    def _deserialize(
        cls: Type["_RootDirectory"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RootDirectory"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            CreationInfo=CreationInfo._deserialize(json_data.get("CreationInfo")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RootDirectory = RootDirectory


@dataclass
class CreationInfo(BaseModel):
    OwnerUid: Optional[str]
    OwnerGid: Optional[str]
    Permissions: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CreationInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreationInfo"]:
        if not json_data:
            return None
        return cls(
            OwnerUid=json_data.get("OwnerUid"),
            OwnerGid=json_data.get("OwnerGid"),
            Permissions=json_data.get("Permissions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreationInfo = CreationInfo


