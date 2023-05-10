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
class AwsSesContactlist(BaseModel):
    ContactListName: Optional[str]
    Description: Optional[str]
    Topics: Optional[Sequence["_Topic"]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSesContactlist"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSesContactlist"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ContactListName=json_data.get("ContactListName"),
            Description=json_data.get("Description"),
            Topics=deserialize_list(json_data.get("Topics"), Topic),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSesContactlist = AwsSesContactlist


@dataclass
class Topic(BaseModel):
    TopicName: Optional[str]
    DisplayName: Optional[str]
    Description: Optional[str]
    DefaultSubscriptionStatus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Topic"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Topic"]:
        if not json_data:
            return None
        return cls(
            TopicName=json_data.get("TopicName"),
            DisplayName=json_data.get("DisplayName"),
            Description=json_data.get("Description"),
            DefaultSubscriptionStatus=json_data.get("DefaultSubscriptionStatus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Topic = Topic


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


