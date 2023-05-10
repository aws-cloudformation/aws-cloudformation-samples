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
class AwsCodeguruprofilerProfilinggroup(BaseModel):
    ProfilingGroupName: Optional[str]
    ComputePlatform: Optional[str]
    AgentPermissions: Optional["_AgentPermissions"]
    AnomalyDetectionNotificationConfiguration: Optional[Sequence["_Channel"]]
    Arn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCodeguruprofilerProfilinggroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCodeguruprofilerProfilinggroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ProfilingGroupName=json_data.get("ProfilingGroupName"),
            ComputePlatform=json_data.get("ComputePlatform"),
            AgentPermissions=AgentPermissions._deserialize(json_data.get("AgentPermissions")),
            AnomalyDetectionNotificationConfiguration=deserialize_list(json_data.get("AnomalyDetectionNotificationConfiguration"), Channel),
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCodeguruprofilerProfilinggroup = AwsCodeguruprofilerProfilinggroup


@dataclass
class AgentPermissions(BaseModel):
    Principals: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AgentPermissions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AgentPermissions"]:
        if not json_data:
            return None
        return cls(
            Principals=json_data.get("Principals"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AgentPermissions = AgentPermissions


@dataclass
class Channel(BaseModel):
    channelId: Optional[str]
    channelUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Channel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Channel"]:
        if not json_data:
            return None
        return cls(
            channelId=json_data.get("channelId"),
            channelUri=json_data.get("channelUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Channel = Channel


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


