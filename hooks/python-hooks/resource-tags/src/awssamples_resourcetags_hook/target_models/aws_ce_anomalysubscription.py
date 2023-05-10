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
class AwsCeAnomalysubscription(BaseModel):
    SubscriptionArn: Optional[str]
    SubscriptionName: Optional[str]
    AccountId: Optional[str]
    MonitorArnList: Optional[Sequence[str]]
    Subscribers: Optional[Sequence["_Subscriber"]]
    Threshold: Optional[float]
    ThresholdExpression: Optional[str]
    Frequency: Optional[str]
    ResourceTags: Optional[Sequence["_ResourceTag"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCeAnomalysubscription"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCeAnomalysubscription"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            SubscriptionArn=json_data.get("SubscriptionArn"),
            SubscriptionName=json_data.get("SubscriptionName"),
            AccountId=json_data.get("AccountId"),
            MonitorArnList=json_data.get("MonitorArnList"),
            Subscribers=deserialize_list(json_data.get("Subscribers"), Subscriber),
            Threshold=json_data.get("Threshold"),
            ThresholdExpression=json_data.get("ThresholdExpression"),
            Frequency=json_data.get("Frequency"),
            ResourceTags=deserialize_list(json_data.get("ResourceTags"), ResourceTag),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCeAnomalysubscription = AwsCeAnomalysubscription


@dataclass
class Subscriber(BaseModel):
    Address: Optional[str]
    Status: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Subscriber"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Subscriber"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Subscriber = Subscriber


@dataclass
class ResourceTag(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceTag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceTag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceTag = ResourceTag


