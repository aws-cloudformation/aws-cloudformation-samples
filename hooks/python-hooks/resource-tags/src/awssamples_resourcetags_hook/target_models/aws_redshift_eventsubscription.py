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
class AwsRedshiftEventsubscription(BaseModel):
    SubscriptionName: Optional[str]
    SnsTopicArn: Optional[str]
    SourceType: Optional[str]
    SourceIds: Optional[Sequence[str]]
    EventCategories: Optional[AbstractSet[str]]
    Severity: Optional[str]
    Enabled: Optional[bool]
    Tags: Optional[Any]
    CustomerAwsId: Optional[str]
    CustSubscriptionId: Optional[str]
    Status: Optional[str]
    SubscriptionCreationTime: Optional[str]
    SourceIdsList: Optional[Sequence[str]]
    EventCategoriesList: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRedshiftEventsubscription"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRedshiftEventsubscription"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            SubscriptionName=json_data.get("SubscriptionName"),
            SnsTopicArn=json_data.get("SnsTopicArn"),
            SourceType=json_data.get("SourceType"),
            SourceIds=json_data.get("SourceIds"),
            EventCategories=set_or_none(json_data.get("EventCategories")),
            Severity=json_data.get("Severity"),
            Enabled=json_data.get("Enabled"),
            Tags=json_data.get("Tags"),
            CustomerAwsId=json_data.get("CustomerAwsId"),
            CustSubscriptionId=json_data.get("CustSubscriptionId"),
            Status=json_data.get("Status"),
            SubscriptionCreationTime=json_data.get("SubscriptionCreationTime"),
            SourceIdsList=json_data.get("SourceIdsList"),
            EventCategoriesList=set_or_none(json_data.get("EventCategoriesList")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRedshiftEventsubscription = AwsRedshiftEventsubscription


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


