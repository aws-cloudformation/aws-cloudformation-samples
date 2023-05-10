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
class AwsMediaconvertJobtemplate(BaseModel):
    Category: Optional[str]
    Description: Optional[str]
    AccelerationSettings: Optional["_AccelerationSettings"]
    Priority: Optional[int]
    StatusUpdateInterval: Optional[str]
    SettingsJson: Optional[MutableMapping[str, Any]]
    Id: Optional[str]
    Arn: Optional[str]
    Queue: Optional[str]
    HopDestinations: Optional[Sequence["_HopDestination"]]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMediaconvertJobtemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMediaconvertJobtemplate"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Category=json_data.get("Category"),
            Description=json_data.get("Description"),
            AccelerationSettings=AccelerationSettings._deserialize(json_data.get("AccelerationSettings")),
            Priority=json_data.get("Priority"),
            StatusUpdateInterval=json_data.get("StatusUpdateInterval"),
            SettingsJson=json_data.get("SettingsJson"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Queue=json_data.get("Queue"),
            HopDestinations=deserialize_list(json_data.get("HopDestinations"), HopDestination),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMediaconvertJobtemplate = AwsMediaconvertJobtemplate


@dataclass
class AccelerationSettings(BaseModel):
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccelerationSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccelerationSettings"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccelerationSettings = AccelerationSettings


@dataclass
class HopDestination(BaseModel):
    WaitMinutes: Optional[int]
    Queue: Optional[str]
    Priority: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_HopDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HopDestination"]:
        if not json_data:
            return None
        return cls(
            WaitMinutes=json_data.get("WaitMinutes"),
            Queue=json_data.get("Queue"),
            Priority=json_data.get("Priority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HopDestination = HopDestination


