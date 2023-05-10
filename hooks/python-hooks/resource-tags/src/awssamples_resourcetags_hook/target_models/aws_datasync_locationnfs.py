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
class AwsDatasyncLocationnfs(BaseModel):
    MountOptions: Optional["_MountOptions"]
    OnPremConfig: Optional["_OnPremConfig"]
    ServerHostname: Optional[str]
    Subdirectory: Optional[str]
    Tags: Optional[Any]
    LocationArn: Optional[str]
    LocationUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDatasyncLocationnfs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDatasyncLocationnfs"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            MountOptions=MountOptions._deserialize(json_data.get("MountOptions")),
            OnPremConfig=OnPremConfig._deserialize(json_data.get("OnPremConfig")),
            ServerHostname=json_data.get("ServerHostname"),
            Subdirectory=json_data.get("Subdirectory"),
            Tags=json_data.get("Tags"),
            LocationArn=json_data.get("LocationArn"),
            LocationUri=json_data.get("LocationUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDatasyncLocationnfs = AwsDatasyncLocationnfs


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
class OnPremConfig(BaseModel):
    AgentArns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_OnPremConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnPremConfig"]:
        if not json_data:
            return None
        return cls(
            AgentArns=json_data.get("AgentArns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnPremConfig = OnPremConfig


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


