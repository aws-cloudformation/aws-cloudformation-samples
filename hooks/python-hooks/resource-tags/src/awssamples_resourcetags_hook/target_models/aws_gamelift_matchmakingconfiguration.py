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
class AwsGameliftMatchmakingconfiguration(BaseModel):
    GameProperties: Optional[Sequence["_GameProperty"]]
    GameSessionData: Optional[str]
    Description: Optional[str]
    AcceptanceTimeoutSeconds: Optional[int]
    NotificationTarget: Optional[str]
    CustomEventData: Optional[str]
    Name: Optional[str]
    AdditionalPlayerCount: Optional[int]
    BackfillMode: Optional[str]
    RequestTimeoutSeconds: Optional[int]
    AcceptanceRequired: Optional[bool]
    FlexMatchMode: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    RuleSetName: Optional[str]
    GameSessionQueueArns: Optional[Sequence[str]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGameliftMatchmakingconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGameliftMatchmakingconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            GameProperties=deserialize_list(json_data.get("GameProperties"), GameProperty),
            GameSessionData=json_data.get("GameSessionData"),
            Description=json_data.get("Description"),
            AcceptanceTimeoutSeconds=json_data.get("AcceptanceTimeoutSeconds"),
            NotificationTarget=json_data.get("NotificationTarget"),
            CustomEventData=json_data.get("CustomEventData"),
            Name=json_data.get("Name"),
            AdditionalPlayerCount=json_data.get("AdditionalPlayerCount"),
            BackfillMode=json_data.get("BackfillMode"),
            RequestTimeoutSeconds=json_data.get("RequestTimeoutSeconds"),
            AcceptanceRequired=json_data.get("AcceptanceRequired"),
            FlexMatchMode=json_data.get("FlexMatchMode"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            RuleSetName=json_data.get("RuleSetName"),
            GameSessionQueueArns=json_data.get("GameSessionQueueArns"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGameliftMatchmakingconfiguration = AwsGameliftMatchmakingconfiguration


@dataclass
class GameProperty(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GameProperty"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GameProperty"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GameProperty = GameProperty


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


