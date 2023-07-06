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
class AwsCustomerprofilesCalculatedattributedefinition(BaseModel):
    DomainName: Optional[str]
    CalculatedAttributeName: Optional[str]
    DisplayName: Optional[str]
    Description: Optional[str]
    AttributeDetails: Optional["_AttributeDetails"]
    Conditions: Optional["_Conditions"]
    Statistic: Optional[str]
    CreatedAt: Optional[str]
    LastUpdatedAt: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCustomerprofilesCalculatedattributedefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCustomerprofilesCalculatedattributedefinition"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DomainName=json_data.get("DomainName"),
            CalculatedAttributeName=json_data.get("CalculatedAttributeName"),
            DisplayName=json_data.get("DisplayName"),
            Description=json_data.get("Description"),
            AttributeDetails=AttributeDetails._deserialize(json_data.get("AttributeDetails")),
            Conditions=Conditions._deserialize(json_data.get("Conditions")),
            Statistic=json_data.get("Statistic"),
            CreatedAt=json_data.get("CreatedAt"),
            LastUpdatedAt=json_data.get("LastUpdatedAt"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCustomerprofilesCalculatedattributedefinition = AwsCustomerprofilesCalculatedattributedefinition


@dataclass
class AttributeDetails(BaseModel):
    Attributes: Optional[AbstractSet["_AttributeItem"]]
    Expression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttributeDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributeDetails"]:
        if not json_data:
            return None
        return cls(
            Attributes=set_or_none(json_data.get("Attributes")),
            Expression=json_data.get("Expression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributeDetails = AttributeDetails


@dataclass
class AttributeItem(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttributeItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributeItem"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributeItem = AttributeItem


@dataclass
class Conditions(BaseModel):
    Range: Optional["_Range"]
    ObjectCount: Optional[int]
    Threshold: Optional["_Threshold"]

    @classmethod
    def _deserialize(
        cls: Type["_Conditions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Conditions"]:
        if not json_data:
            return None
        return cls(
            Range=Range._deserialize(json_data.get("Range")),
            ObjectCount=json_data.get("ObjectCount"),
            Threshold=Threshold._deserialize(json_data.get("Threshold")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Conditions = Conditions


@dataclass
class Range(BaseModel):
    Value: Optional[int]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Range"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Range"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Range = Range


@dataclass
class Threshold(BaseModel):
    Value: Optional[str]
    Operator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Threshold"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Threshold"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Operator=json_data.get("Operator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Threshold = Threshold


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


