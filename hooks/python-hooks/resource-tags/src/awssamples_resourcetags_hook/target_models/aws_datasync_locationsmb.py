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
class AwsDatasyncLocationsmb(BaseModel):
    AgentArns: Optional[Sequence[str]]
    Domain: Optional[str]
    MountOptions: Optional["_MountOptions"]
    Password: Optional[str]
    ServerHostname: Optional[str]
    Subdirectory: Optional[str]
    User: Optional[str]
    Tags: Optional[Any]
    LocationArn: Optional[str]
    LocationUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDatasyncLocationsmb"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDatasyncLocationsmb"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AgentArns=json_data.get("AgentArns"),
            Domain=json_data.get("Domain"),
            MountOptions=MountOptions._deserialize(json_data.get("MountOptions")),
            Password=json_data.get("Password"),
            ServerHostname=json_data.get("ServerHostname"),
            Subdirectory=json_data.get("Subdirectory"),
            User=json_data.get("User"),
            Tags=json_data.get("Tags"),
            LocationArn=json_data.get("LocationArn"),
            LocationUri=json_data.get("LocationUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDatasyncLocationsmb = AwsDatasyncLocationsmb


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


