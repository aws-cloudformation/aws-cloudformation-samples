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
class AwsMacieFindingsfilter(BaseModel):
    Name: Optional[str]
    Description: Optional[str]
    FindingCriteria: Optional["_FindingCriteria"]
    Action: Optional[str]
    Position: Optional[int]
    Id: Optional[str]
    Arn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMacieFindingsfilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMacieFindingsfilter"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            FindingCriteria=FindingCriteria._deserialize(json_data.get("FindingCriteria")),
            Action=json_data.get("Action"),
            Position=json_data.get("Position"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMacieFindingsfilter = AwsMacieFindingsfilter


@dataclass
class FindingCriteria(BaseModel):
    Criterion: Optional[MutableMapping[str, "_CriterionAdditionalProperties"]]

    @classmethod
    def _deserialize(
        cls: Type["_FindingCriteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FindingCriteria"]:
        if not json_data:
            return None
        return cls(
            Criterion=json_data.get("Criterion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FindingCriteria = FindingCriteria


@dataclass
class CriterionAdditionalProperties(BaseModel):
    gt: Optional[int]
    gte: Optional[int]
    lt: Optional[int]
    lte: Optional[int]
    eq: Optional[Sequence[str]]
    neq: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CriterionAdditionalProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CriterionAdditionalProperties"]:
        if not json_data:
            return None
        return cls(
            gt=json_data.get("gt"),
            gte=json_data.get("gte"),
            lt=json_data.get("lt"),
            lte=json_data.get("lte"),
            eq=json_data.get("eq"),
            neq=json_data.get("neq"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CriterionAdditionalProperties = CriterionAdditionalProperties


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


