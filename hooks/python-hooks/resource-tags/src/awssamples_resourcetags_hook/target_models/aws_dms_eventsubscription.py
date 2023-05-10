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
class AwsDmsEventsubscription(BaseModel):
    SourceType: Optional[str]
    EventCategories: Optional[Sequence[str]]
    Enabled: Optional[bool]
    SubscriptionName: Optional[str]
    SnsTopicArn: Optional[str]
    SourceIds: Optional[Sequence[str]]
    Id: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDmsEventsubscription"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDmsEventsubscription"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            SourceType=json_data.get("SourceType"),
            EventCategories=json_data.get("EventCategories"),
            Enabled=json_data.get("Enabled"),
            SubscriptionName=json_data.get("SubscriptionName"),
            SnsTopicArn=json_data.get("SnsTopicArn"),
            SourceIds=json_data.get("SourceIds"),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDmsEventsubscription = AwsDmsEventsubscription


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


