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
class AwsBillingconductorPricingrule(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    Description: Optional[str]
    Scope: Optional[str]
    Type: Optional[str]
    ModifierPercentage: Optional[float]
    Service: Optional[str]
    BillingEntity: Optional[str]
    Tiering: Optional["_Tiering"]
    UsageType: Optional[str]
    Operation: Optional[str]
    AssociatedPricingPlanCount: Optional[int]
    CreationTime: Optional[int]
    LastModifiedTime: Optional[int]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsBillingconductorPricingrule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsBillingconductorPricingrule"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            Scope=json_data.get("Scope"),
            Type=json_data.get("Type"),
            ModifierPercentage=json_data.get("ModifierPercentage"),
            Service=json_data.get("Service"),
            BillingEntity=json_data.get("BillingEntity"),
            Tiering=Tiering._deserialize(json_data.get("Tiering")),
            UsageType=json_data.get("UsageType"),
            Operation=json_data.get("Operation"),
            AssociatedPricingPlanCount=json_data.get("AssociatedPricingPlanCount"),
            CreationTime=json_data.get("CreationTime"),
            LastModifiedTime=json_data.get("LastModifiedTime"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsBillingconductorPricingrule = AwsBillingconductorPricingrule


@dataclass
class Tiering(BaseModel):
    FreeTier: Optional["_FreeTier"]

    @classmethod
    def _deserialize(
        cls: Type["_Tiering"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tiering"]:
        if not json_data:
            return None
        return cls(
            FreeTier=FreeTier._deserialize(json_data.get("FreeTier")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tiering = Tiering


@dataclass
class FreeTier(BaseModel):
    Activated: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_FreeTier"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeTier"]:
        if not json_data:
            return None
        return cls(
            Activated=json_data.get("Activated"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeTier = FreeTier


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


