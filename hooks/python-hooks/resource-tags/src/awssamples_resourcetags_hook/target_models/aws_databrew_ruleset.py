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
class AwsDatabrewRuleset(BaseModel):
    Name: Optional[str]
    Description: Optional[str]
    TargetArn: Optional[str]
    Rules: Optional[Sequence["_Rule"]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDatabrewRuleset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDatabrewRuleset"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            TargetArn=json_data.get("TargetArn"),
            Rules=deserialize_list(json_data.get("Rules"), Rule),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDatabrewRuleset = AwsDatabrewRuleset


@dataclass
class Rule(BaseModel):
    Name: Optional[str]
    Disabled: Optional[bool]
    CheckExpression: Optional[str]
    SubstitutionMap: Optional[Sequence["_SubstitutionValue"]]
    Threshold: Optional["_Threshold"]
    ColumnSelectors: Optional[Sequence["_ColumnSelector"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Disabled=json_data.get("Disabled"),
            CheckExpression=json_data.get("CheckExpression"),
            SubstitutionMap=deserialize_list(json_data.get("SubstitutionMap"), SubstitutionValue),
            Threshold=Threshold._deserialize(json_data.get("Threshold")),
            ColumnSelectors=deserialize_list(json_data.get("ColumnSelectors"), ColumnSelector),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class SubstitutionValue(BaseModel):
    ValueReference: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubstitutionValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubstitutionValue"]:
        if not json_data:
            return None
        return cls(
            ValueReference=json_data.get("ValueReference"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubstitutionValue = SubstitutionValue


@dataclass
class Threshold(BaseModel):
    Value: Optional[float]
    Type: Optional[str]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Threshold"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Threshold"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Type=json_data.get("Type"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Threshold = Threshold


@dataclass
class ColumnSelector(BaseModel):
    Regex: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnSelector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnSelector"]:
        if not json_data:
            return None
        return cls(
            Regex=json_data.get("Regex"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnSelector = ColumnSelector


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


