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
class AwsGuarddutyFilter(BaseModel):
    Action: Optional[str]
    Description: Optional[str]
    DetectorId: Optional[str]
    FindingCriteria: Optional["_FindingCriteria"]
    Rank: Optional[int]
    Id: Optional[str]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGuarddutyFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGuarddutyFilter"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Action=json_data.get("Action"),
            Description=json_data.get("Description"),
            DetectorId=json_data.get("DetectorId"),
            FindingCriteria=FindingCriteria._deserialize(json_data.get("FindingCriteria")),
            Rank=json_data.get("Rank"),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGuarddutyFilter = AwsGuarddutyFilter


@dataclass
class FindingCriteria(BaseModel):
    Criterion: Optional[MutableMapping[str, Any]]
    ItemType: Optional["_Condition"]

    @classmethod
    def _deserialize(
        cls: Type["_FindingCriteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FindingCriteria"]:
        if not json_data:
            return None
        return cls(
            Criterion=json_data.get("Criterion"),
            ItemType=Condition._deserialize(json_data.get("ItemType")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FindingCriteria = FindingCriteria


@dataclass
class Condition(BaseModel):
    LessThanOrEqual: Optional[int]
    Lt: Optional[int]
    GreaterThanOrEqual: Optional[int]
    Eq: Optional[Sequence[str]]
    Gt: Optional[int]
    NotEquals: Optional[Sequence[str]]
    Equals: Optional[Sequence[str]]
    LessThan: Optional[int]
    GreaterThan: Optional[int]
    Gte: Optional[int]
    Neq: Optional[Sequence[str]]
    Lte: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Condition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Condition"]:
        if not json_data:
            return None
        return cls(
            LessThanOrEqual=json_data.get("LessThanOrEqual"),
            Lt=json_data.get("Lt"),
            GreaterThanOrEqual=json_data.get("GreaterThanOrEqual"),
            Eq=json_data.get("Eq"),
            Gt=json_data.get("Gt"),
            NotEquals=json_data.get("NotEquals"),
            Equals=json_data.get("Equals"),
            LessThan=json_data.get("LessThan"),
            GreaterThan=json_data.get("GreaterThan"),
            Gte=json_data.get("Gte"),
            Neq=json_data.get("Neq"),
            Lte=json_data.get("Lte"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Condition = Condition


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


