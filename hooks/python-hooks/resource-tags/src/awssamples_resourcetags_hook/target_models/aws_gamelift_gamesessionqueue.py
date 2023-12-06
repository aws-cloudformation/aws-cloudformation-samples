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
class AwsGameliftGamesessionqueue(BaseModel):
    Name: Optional[str]
    TimeoutInSeconds: Optional[int]
    Destinations: Optional[Sequence["_GameSessionQueueDestination"]]
    PlayerLatencyPolicies: Optional[Sequence["_PlayerLatencyPolicy"]]
    CustomEventData: Optional[str]
    NotificationTarget: Optional[str]
    FilterConfiguration: Optional["_FilterConfiguration"]
    PriorityConfiguration: Optional["_PriorityConfiguration"]
    Arn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGameliftGamesessionqueue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGameliftGamesessionqueue"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            TimeoutInSeconds=json_data.get("TimeoutInSeconds"),
            Destinations=deserialize_list(json_data.get("Destinations"), GameSessionQueueDestination),
            PlayerLatencyPolicies=deserialize_list(json_data.get("PlayerLatencyPolicies"), PlayerLatencyPolicy),
            CustomEventData=json_data.get("CustomEventData"),
            NotificationTarget=json_data.get("NotificationTarget"),
            FilterConfiguration=FilterConfiguration._deserialize(json_data.get("FilterConfiguration")),
            PriorityConfiguration=PriorityConfiguration._deserialize(json_data.get("PriorityConfiguration")),
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGameliftGamesessionqueue = AwsGameliftGamesessionqueue


@dataclass
class GameSessionQueueDestination(BaseModel):
    DestinationArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GameSessionQueueDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GameSessionQueueDestination"]:
        if not json_data:
            return None
        return cls(
            DestinationArn=json_data.get("DestinationArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GameSessionQueueDestination = GameSessionQueueDestination


@dataclass
class PlayerLatencyPolicy(BaseModel):
    MaximumIndividualPlayerLatencyMilliseconds: Optional[int]
    PolicyDurationSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_PlayerLatencyPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlayerLatencyPolicy"]:
        if not json_data:
            return None
        return cls(
            MaximumIndividualPlayerLatencyMilliseconds=json_data.get("MaximumIndividualPlayerLatencyMilliseconds"),
            PolicyDurationSeconds=json_data.get("PolicyDurationSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlayerLatencyPolicy = PlayerLatencyPolicy


@dataclass
class FilterConfiguration(BaseModel):
    AllowedLocations: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterConfiguration"]:
        if not json_data:
            return None
        return cls(
            AllowedLocations=json_data.get("AllowedLocations"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterConfiguration = FilterConfiguration


@dataclass
class PriorityConfiguration(BaseModel):
    LocationOrder: Optional[Sequence[str]]
    PriorityOrder: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PriorityConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PriorityConfiguration"]:
        if not json_data:
            return None
        return cls(
            LocationOrder=json_data.get("LocationOrder"),
            PriorityOrder=json_data.get("PriorityOrder"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PriorityConfiguration = PriorityConfiguration


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


