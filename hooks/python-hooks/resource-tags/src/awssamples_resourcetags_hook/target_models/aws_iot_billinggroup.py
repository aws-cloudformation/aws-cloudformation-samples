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
class AwsIotBillinggroup(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]
    BillingGroupName: Optional[str]
    Tags: Optional[Any]
    BillingGroupProperties: Optional["_BillingGroupProperties"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotBillinggroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotBillinggroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            BillingGroupName=json_data.get("BillingGroupName"),
            Tags=json_data.get("Tags"),
            BillingGroupProperties=BillingGroupProperties._deserialize(json_data.get("BillingGroupProperties")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotBillinggroup = AwsIotBillinggroup


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


@dataclass
class BillingGroupProperties(BaseModel):
    BillingGroupDescription: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BillingGroupProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BillingGroupProperties"]:
        if not json_data:
            return None
        return cls(
            BillingGroupDescription=json_data.get("BillingGroupDescription"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BillingGroupProperties = BillingGroupProperties


