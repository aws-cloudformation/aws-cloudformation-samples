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
    TimeoutInSeconds: Optional[int]
    PlayerLatencyPolicies: Optional[Sequence["_PlayerLatencyPolicy"]]
    Destinations: Optional[Sequence["_Destination"]]
    NotificationTarget: Optional[str]
    FilterConfiguration: Optional["_FilterConfiguration"]
    Id: Optional[str]
    Arn: Optional[str]
    CustomEventData: Optional[str]
    Tags: Optional[Any]
    Name: Optional[str]
    PriorityConfiguration: Optional["_PriorityConfiguration"]

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
            TimeoutInSeconds=json_data.get("TimeoutInSeconds"),
            PlayerLatencyPolicies=deserialize_list(json_data.get("PlayerLatencyPolicies"), PlayerLatencyPolicy),
            Destinations=deserialize_list(json_data.get("Destinations"), Destination),
            NotificationTarget=json_data.get("NotificationTarget"),
            FilterConfiguration=FilterConfiguration._deserialize(json_data.get("FilterConfiguration")),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            CustomEventData=json_data.get("CustomEventData"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
            PriorityConfiguration=PriorityConfiguration._deserialize(json_data.get("PriorityConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGameliftGamesessionqueue = AwsGameliftGamesessionqueue


@dataclass
class PlayerLatencyPolicy(BaseModel):
    PolicyDurationSeconds: Optional[int]
    MaximumIndividualPlayerLatencyMilliseconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_PlayerLatencyPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlayerLatencyPolicy"]:
        if not json_data:
            return None
        return cls(
            PolicyDurationSeconds=json_data.get("PolicyDurationSeconds"),
            MaximumIndividualPlayerLatencyMilliseconds=json_data.get("MaximumIndividualPlayerLatencyMilliseconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlayerLatencyPolicy = PlayerLatencyPolicy


@dataclass
class Destination(BaseModel):
    DestinationArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Destination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Destination"]:
        if not json_data:
            return None
        return cls(
            DestinationArn=json_data.get("DestinationArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Destination = Destination


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


@dataclass
class PriorityConfiguration(BaseModel):
    PriorityOrder: Optional[Sequence[str]]
    LocationOrder: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PriorityConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PriorityConfiguration"]:
        if not json_data:
            return None
        return cls(
            PriorityOrder=json_data.get("PriorityOrder"),
            LocationOrder=json_data.get("LocationOrder"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PriorityConfiguration = PriorityConfiguration


