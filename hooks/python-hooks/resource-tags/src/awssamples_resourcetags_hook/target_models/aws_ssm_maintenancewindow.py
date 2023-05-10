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
class AwsSsmMaintenancewindow(BaseModel):
    StartDate: Optional[str]
    Description: Optional[str]
    AllowUnassociatedTargets: Optional[bool]
    Cutoff: Optional[int]
    Schedule: Optional[str]
    Duration: Optional[int]
    ScheduleOffset: Optional[int]
    Id: Optional[str]
    EndDate: Optional[str]
    Tags: Optional[Any]
    Name: Optional[str]
    ScheduleTimezone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSsmMaintenancewindow"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSsmMaintenancewindow"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            StartDate=json_data.get("StartDate"),
            Description=json_data.get("Description"),
            AllowUnassociatedTargets=json_data.get("AllowUnassociatedTargets"),
            Cutoff=json_data.get("Cutoff"),
            Schedule=json_data.get("Schedule"),
            Duration=json_data.get("Duration"),
            ScheduleOffset=json_data.get("ScheduleOffset"),
            Id=json_data.get("Id"),
            EndDate=json_data.get("EndDate"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
            ScheduleTimezone=json_data.get("ScheduleTimezone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSsmMaintenancewindow = AwsSsmMaintenancewindow


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


