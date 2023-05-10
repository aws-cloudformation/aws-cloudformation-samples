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
class AwsXrayGroup(BaseModel):
    FilterExpression: Optional[str]
    GroupName: Optional[str]
    GroupARN: Optional[str]
    InsightsConfiguration: Optional["_InsightsConfiguration"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsXrayGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsXrayGroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            FilterExpression=json_data.get("FilterExpression"),
            GroupName=json_data.get("GroupName"),
            GroupARN=json_data.get("GroupARN"),
            InsightsConfiguration=InsightsConfiguration._deserialize(json_data.get("InsightsConfiguration")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsXrayGroup = AwsXrayGroup


@dataclass
class InsightsConfiguration(BaseModel):
    InsightsEnabled: Optional[bool]
    NotificationsEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_InsightsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InsightsConfiguration"]:
        if not json_data:
            return None
        return cls(
            InsightsEnabled=json_data.get("InsightsEnabled"),
            NotificationsEnabled=json_data.get("NotificationsEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InsightsConfiguration = InsightsConfiguration


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


