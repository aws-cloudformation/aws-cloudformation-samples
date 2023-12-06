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
    AcceptanceRequired: Optional[bool]
    AcceptanceTimeoutSeconds: Optional[int]
    AdditionalPlayerCount: Optional[int]
    BackfillMode: Optional[str]
    Arn: Optional[str]
    CreationTime: Optional[str]
    CustomEventData: Optional[str]
    Description: Optional[str]
    FlexMatchMode: Optional[str]
    GameProperties: Optional[AbstractSet["_GameProperty"]]
    GameSessionData: Optional[str]
    GameSessionQueueArns: Optional[Sequence[str]]
    Name: Optional[str]
    NotificationTarget: Optional[str]
    RequestTimeoutSeconds: Optional[int]
    RuleSetArn: Optional[str]
    RuleSetName: Optional[str]
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
            AcceptanceRequired=json_data.get("AcceptanceRequired"),
            AcceptanceTimeoutSeconds=json_data.get("AcceptanceTimeoutSeconds"),
            AdditionalPlayerCount=json_data.get("AdditionalPlayerCount"),
            BackfillMode=json_data.get("BackfillMode"),
            Arn=json_data.get("Arn"),
            CreationTime=json_data.get("CreationTime"),
            CustomEventData=json_data.get("CustomEventData"),
            Description=json_data.get("Description"),
            FlexMatchMode=json_data.get("FlexMatchMode"),
            GameProperties=set_or_none(json_data.get("GameProperties")),
            GameSessionData=json_data.get("GameSessionData"),
            GameSessionQueueArns=json_data.get("GameSessionQueueArns"),
            Name=json_data.get("Name"),
            NotificationTarget=json_data.get("NotificationTarget"),
            RequestTimeoutSeconds=json_data.get("RequestTimeoutSeconds"),
            RuleSetArn=json_data.get("RuleSetArn"),
            RuleSetName=json_data.get("RuleSetName"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGameliftMatchmakingconfiguration = AwsGameliftMatchmakingconfiguration


@dataclass
class GameProperty(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GameProperty"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GameProperty"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GameProperty = GameProperty


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


