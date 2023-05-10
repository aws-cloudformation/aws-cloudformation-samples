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
class AwsSsmcontactsRotation(BaseModel):
    Name: Optional[str]
    ContactIds: Optional[Sequence[str]]
    StartTime: Optional[str]
    TimeZoneId: Optional[str]
    Recurrence: Optional["_RecurrenceSettings"]
    Tags: Optional[Any]
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSsmcontactsRotation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSsmcontactsRotation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            ContactIds=json_data.get("ContactIds"),
            StartTime=json_data.get("StartTime"),
            TimeZoneId=json_data.get("TimeZoneId"),
            Recurrence=RecurrenceSettings._deserialize(json_data.get("Recurrence")),
            Tags=json_data.get("Tags"),
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSsmcontactsRotation = AwsSsmcontactsRotation


@dataclass
class RecurrenceSettings(BaseModel):
    MonthlySettings: Optional[Sequence["_MonthlySetting"]]
    WeeklySettings: Optional[Sequence["_WeeklySetting"]]
    DailySettings: Optional[Sequence[str]]
    NumberOfOnCalls: Optional[int]
    RecurrenceMultiplier: Optional[int]
    ShiftCoverages: Optional[Sequence["_ShiftCoverage"]]

    @classmethod
    def _deserialize(
        cls: Type["_RecurrenceSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecurrenceSettings"]:
        if not json_data:
            return None
        return cls(
            MonthlySettings=deserialize_list(json_data.get("MonthlySettings"), MonthlySetting),
            WeeklySettings=deserialize_list(json_data.get("WeeklySettings"), WeeklySetting),
            DailySettings=json_data.get("DailySettings"),
            NumberOfOnCalls=json_data.get("NumberOfOnCalls"),
            RecurrenceMultiplier=json_data.get("RecurrenceMultiplier"),
            ShiftCoverages=deserialize_list(json_data.get("ShiftCoverages"), ShiftCoverage),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecurrenceSettings = RecurrenceSettings


@dataclass
class MonthlySetting(BaseModel):
    DayOfMonth: Optional[int]
    HandOffTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MonthlySetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonthlySetting"]:
        if not json_data:
            return None
        return cls(
            DayOfMonth=json_data.get("DayOfMonth"),
            HandOffTime=json_data.get("HandOffTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonthlySetting = MonthlySetting


@dataclass
class WeeklySetting(BaseModel):
    DayOfWeek: Optional[str]
    HandOffTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WeeklySetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WeeklySetting"]:
        if not json_data:
            return None
        return cls(
            DayOfWeek=json_data.get("DayOfWeek"),
            HandOffTime=json_data.get("HandOffTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WeeklySetting = WeeklySetting


@dataclass
class ShiftCoverage(BaseModel):
    DayOfWeek: Optional[str]
    CoverageTimes: Optional[Sequence["_CoverageTime"]]

    @classmethod
    def _deserialize(
        cls: Type["_ShiftCoverage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShiftCoverage"]:
        if not json_data:
            return None
        return cls(
            DayOfWeek=json_data.get("DayOfWeek"),
            CoverageTimes=deserialize_list(json_data.get("CoverageTimes"), CoverageTime),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShiftCoverage = ShiftCoverage


@dataclass
class CoverageTime(BaseModel):
    StartTime: Optional[str]
    EndTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CoverageTime"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CoverageTime"]:
        if not json_data:
            return None
        return cls(
            StartTime=json_data.get("StartTime"),
            EndTime=json_data.get("EndTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CoverageTime = CoverageTime


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


