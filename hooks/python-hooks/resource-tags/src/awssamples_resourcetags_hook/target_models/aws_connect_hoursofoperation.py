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
class AwsConnectHoursofoperation(BaseModel):
    InstanceArn: Optional[str]
    Name: Optional[str]
    Description: Optional[str]
    TimeZone: Optional[str]
    Config: Optional[AbstractSet["_HoursOfOperationConfig"]]
    HoursOfOperationArn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConnectHoursofoperation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConnectHoursofoperation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            InstanceArn=json_data.get("InstanceArn"),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            TimeZone=json_data.get("TimeZone"),
            Config=set_or_none(json_data.get("Config")),
            HoursOfOperationArn=json_data.get("HoursOfOperationArn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConnectHoursofoperation = AwsConnectHoursofoperation


@dataclass
class HoursOfOperationConfig(BaseModel):
    Day: Optional[str]
    StartTime: Optional["_HoursOfOperationTimeSlice"]
    EndTime: Optional["_HoursOfOperationTimeSlice"]

    @classmethod
    def _deserialize(
        cls: Type["_HoursOfOperationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HoursOfOperationConfig"]:
        if not json_data:
            return None
        return cls(
            Day=json_data.get("Day"),
            StartTime=HoursOfOperationTimeSlice._deserialize(json_data.get("StartTime")),
            EndTime=HoursOfOperationTimeSlice._deserialize(json_data.get("EndTime")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HoursOfOperationConfig = HoursOfOperationConfig


@dataclass
class HoursOfOperationTimeSlice(BaseModel):
    Hours: Optional[int]
    Minutes: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_HoursOfOperationTimeSlice"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HoursOfOperationTimeSlice"]:
        if not json_data:
            return None
        return cls(
            Hours=json_data.get("Hours"),
            Minutes=json_data.get("Minutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HoursOfOperationTimeSlice = HoursOfOperationTimeSlice


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


