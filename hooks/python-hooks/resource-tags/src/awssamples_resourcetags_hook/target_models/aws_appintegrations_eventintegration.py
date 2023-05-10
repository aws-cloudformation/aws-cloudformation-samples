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
class AwsAppintegrationsEventintegration(BaseModel):
    Description: Optional[str]
    EventIntegrationArn: Optional[str]
    Name: Optional[str]
    EventBridgeBus: Optional[str]
    EventFilter: Optional["_EventFilter"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppintegrationsEventintegration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppintegrationsEventintegration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            EventIntegrationArn=json_data.get("EventIntegrationArn"),
            Name=json_data.get("Name"),
            EventBridgeBus=json_data.get("EventBridgeBus"),
            EventFilter=EventFilter._deserialize(json_data.get("EventFilter")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppintegrationsEventintegration = AwsAppintegrationsEventintegration


@dataclass
class EventFilter(BaseModel):
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EventFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventFilter"]:
        if not json_data:
            return None
        return cls(
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventFilter = EventFilter


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


