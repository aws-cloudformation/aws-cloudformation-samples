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
class AwsIotScheduledaudit(BaseModel):
    ScheduledAuditName: Optional[str]
    Frequency: Optional[str]
    DayOfMonth: Optional[str]
    DayOfWeek: Optional[str]
    TargetCheckNames: Optional[AbstractSet[str]]
    ScheduledAuditArn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotScheduledaudit"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotScheduledaudit"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ScheduledAuditName=json_data.get("ScheduledAuditName"),
            Frequency=json_data.get("Frequency"),
            DayOfMonth=json_data.get("DayOfMonth"),
            DayOfWeek=json_data.get("DayOfWeek"),
            TargetCheckNames=set_or_none(json_data.get("TargetCheckNames")),
            ScheduledAuditArn=json_data.get("ScheduledAuditArn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotScheduledaudit = AwsIotScheduledaudit


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


