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
class AwsGreengrassSubscriptiondefinition(BaseModel):
    LatestVersionArn: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    Name: Optional[str]
    InitialVersion: Optional["_SubscriptionDefinitionVersion"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGreengrassSubscriptiondefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGreengrassSubscriptiondefinition"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            LatestVersionArn=json_data.get("LatestVersionArn"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            InitialVersion=SubscriptionDefinitionVersion._deserialize(json_data.get("InitialVersion")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGreengrassSubscriptiondefinition = AwsGreengrassSubscriptiondefinition


@dataclass
class SubscriptionDefinitionVersion(BaseModel):
    Subscriptions: Optional[Sequence["_Subscription"]]

    @classmethod
    def _deserialize(
        cls: Type["_SubscriptionDefinitionVersion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubscriptionDefinitionVersion"]:
        if not json_data:
            return None
        return cls(
            Subscriptions=deserialize_list(json_data.get("Subscriptions"), Subscription),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubscriptionDefinitionVersion = SubscriptionDefinitionVersion


@dataclass
class Subscription(BaseModel):
    Target: Optional[str]
    Id: Optional[str]
    Source: Optional[str]
    Subject: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Subscription"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Subscription"]:
        if not json_data:
            return None
        return cls(
            Target=json_data.get("Target"),
            Id=json_data.get("Id"),
            Source=json_data.get("Source"),
            Subject=json_data.get("Subject"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Subscription = Subscription


