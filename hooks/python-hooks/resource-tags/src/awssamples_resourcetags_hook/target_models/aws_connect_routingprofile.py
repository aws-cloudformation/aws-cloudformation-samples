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
class AwsConnectRoutingprofile(BaseModel):
    InstanceArn: Optional[str]
    Name: Optional[str]
    Description: Optional[str]
    MediaConcurrencies: Optional[Sequence["_MediaConcurrency"]]
    DefaultOutboundQueueArn: Optional[str]
    RoutingProfileArn: Optional[str]
    QueueConfigs: Optional[Sequence["_RoutingProfileQueueConfig"]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConnectRoutingprofile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConnectRoutingprofile"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            InstanceArn=json_data.get("InstanceArn"),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            MediaConcurrencies=deserialize_list(json_data.get("MediaConcurrencies"), MediaConcurrency),
            DefaultOutboundQueueArn=json_data.get("DefaultOutboundQueueArn"),
            RoutingProfileArn=json_data.get("RoutingProfileArn"),
            QueueConfigs=deserialize_list(json_data.get("QueueConfigs"), RoutingProfileQueueConfig),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConnectRoutingprofile = AwsConnectRoutingprofile


@dataclass
class MediaConcurrency(BaseModel):
    Channel: Optional[str]
    Concurrency: Optional[int]
    CrossChannelBehavior: Optional["_CrossChannelBehavior"]

    @classmethod
    def _deserialize(
        cls: Type["_MediaConcurrency"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MediaConcurrency"]:
        if not json_data:
            return None
        return cls(
            Channel=json_data.get("Channel"),
            Concurrency=json_data.get("Concurrency"),
            CrossChannelBehavior=CrossChannelBehavior._deserialize(json_data.get("CrossChannelBehavior")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MediaConcurrency = MediaConcurrency


@dataclass
class CrossChannelBehavior(BaseModel):
    BehaviorType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CrossChannelBehavior"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CrossChannelBehavior"]:
        if not json_data:
            return None
        return cls(
            BehaviorType=json_data.get("BehaviorType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CrossChannelBehavior = CrossChannelBehavior


@dataclass
class RoutingProfileQueueConfig(BaseModel):
    Delay: Optional[int]
    Priority: Optional[int]
    QueueReference: Optional["_RoutingProfileQueueReference"]

    @classmethod
    def _deserialize(
        cls: Type["_RoutingProfileQueueConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutingProfileQueueConfig"]:
        if not json_data:
            return None
        return cls(
            Delay=json_data.get("Delay"),
            Priority=json_data.get("Priority"),
            QueueReference=RoutingProfileQueueReference._deserialize(json_data.get("QueueReference")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutingProfileQueueConfig = RoutingProfileQueueConfig


@dataclass
class RoutingProfileQueueReference(BaseModel):
    Channel: Optional[str]
    QueueArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RoutingProfileQueueReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutingProfileQueueReference"]:
        if not json_data:
            return None
        return cls(
            Channel=json_data.get("Channel"),
            QueueArn=json_data.get("QueueArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutingProfileQueueReference = RoutingProfileQueueReference


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


