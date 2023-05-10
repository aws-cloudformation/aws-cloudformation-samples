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
class AwsTransferUser(BaseModel):
    Policy: Optional[str]
    Role: Optional[str]
    HomeDirectory: Optional[str]
    HomeDirectoryType: Optional[str]
    ServerId: Optional[str]
    UserName: Optional[str]
    HomeDirectoryMappings: Optional[Sequence["_HomeDirectoryMapEntry"]]
    PosixProfile: Optional["_PosixProfile"]
    SshPublicKeys: Optional[Sequence[MutableMapping[str, Any]]]
    Id: Optional[str]
    Arn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsTransferUser"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsTransferUser"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Policy=json_data.get("Policy"),
            Role=json_data.get("Role"),
            HomeDirectory=json_data.get("HomeDirectory"),
            HomeDirectoryType=json_data.get("HomeDirectoryType"),
            ServerId=json_data.get("ServerId"),
            UserName=json_data.get("UserName"),
            HomeDirectoryMappings=deserialize_list(json_data.get("HomeDirectoryMappings"), HomeDirectoryMapEntry),
            PosixProfile=PosixProfile._deserialize(json_data.get("PosixProfile")),
            SshPublicKeys=json_data.get("SshPublicKeys"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsTransferUser = AwsTransferUser


@dataclass
class HomeDirectoryMapEntry(BaseModel):
    Entry: Optional[str]
    Target: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HomeDirectoryMapEntry"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HomeDirectoryMapEntry"]:
        if not json_data:
            return None
        return cls(
            Entry=json_data.get("Entry"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HomeDirectoryMapEntry = HomeDirectoryMapEntry


@dataclass
class PosixProfile(BaseModel):
    Uid: Optional[float]
    SecondaryGids: Optional[Sequence[float]]
    Gid: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PosixProfile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PosixProfile"]:
        if not json_data:
            return None
        return cls(
            Uid=json_data.get("Uid"),
            SecondaryGids=json_data.get("SecondaryGids"),
            Gid=json_data.get("Gid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PosixProfile = PosixProfile


@dataclass
class Tag(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


