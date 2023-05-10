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
class AwsBillingconductorCustomlineitem(BaseModel):
    Name: Optional[str]
    Description: Optional[str]
    CustomLineItemChargeDetails: Optional["_CustomLineItemChargeDetails"]
    BillingGroupArn: Optional[str]
    BillingPeriodRange: Optional["_BillingPeriodRange"]
    Arn: Optional[str]
    CreationTime: Optional[int]
    LastModifiedTime: Optional[int]
    AssociationSize: Optional[int]
    ProductCode: Optional[str]
    CurrencyCode: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsBillingconductorCustomlineitem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsBillingconductorCustomlineitem"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            CustomLineItemChargeDetails=CustomLineItemChargeDetails._deserialize(json_data.get("CustomLineItemChargeDetails")),
            BillingGroupArn=json_data.get("BillingGroupArn"),
            BillingPeriodRange=BillingPeriodRange._deserialize(json_data.get("BillingPeriodRange")),
            Arn=json_data.get("Arn"),
            CreationTime=json_data.get("CreationTime"),
            LastModifiedTime=json_data.get("LastModifiedTime"),
            AssociationSize=json_data.get("AssociationSize"),
            ProductCode=json_data.get("ProductCode"),
            CurrencyCode=json_data.get("CurrencyCode"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsBillingconductorCustomlineitem = AwsBillingconductorCustomlineitem


@dataclass
class CustomLineItemChargeDetails(BaseModel):
    Flat: Optional["_CustomLineItemFlatChargeDetails"]
    Percentage: Optional["_CustomLineItemPercentageChargeDetails"]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomLineItemChargeDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomLineItemChargeDetails"]:
        if not json_data:
            return None
        return cls(
            Flat=CustomLineItemFlatChargeDetails._deserialize(json_data.get("Flat")),
            Percentage=CustomLineItemPercentageChargeDetails._deserialize(json_data.get("Percentage")),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomLineItemChargeDetails = CustomLineItemChargeDetails


@dataclass
class CustomLineItemFlatChargeDetails(BaseModel):
    ChargeValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CustomLineItemFlatChargeDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomLineItemFlatChargeDetails"]:
        if not json_data:
            return None
        return cls(
            ChargeValue=json_data.get("ChargeValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomLineItemFlatChargeDetails = CustomLineItemFlatChargeDetails


@dataclass
class CustomLineItemPercentageChargeDetails(BaseModel):
    ChildAssociatedResources: Optional[AbstractSet[str]]
    PercentageValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CustomLineItemPercentageChargeDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomLineItemPercentageChargeDetails"]:
        if not json_data:
            return None
        return cls(
            ChildAssociatedResources=set_or_none(json_data.get("ChildAssociatedResources")),
            PercentageValue=json_data.get("PercentageValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomLineItemPercentageChargeDetails = CustomLineItemPercentageChargeDetails


@dataclass
class BillingPeriodRange(BaseModel):
    InclusiveStartBillingPeriod: Optional[str]
    ExclusiveEndBillingPeriod: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BillingPeriodRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BillingPeriodRange"]:
        if not json_data:
            return None
        return cls(
            InclusiveStartBillingPeriod=json_data.get("InclusiveStartBillingPeriod"),
            ExclusiveEndBillingPeriod=json_data.get("ExclusiveEndBillingPeriod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BillingPeriodRange = BillingPeriodRange


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


