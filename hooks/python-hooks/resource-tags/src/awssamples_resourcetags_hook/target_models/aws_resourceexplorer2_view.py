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
class AwsResourceexplorer2View(BaseModel):
    Filters: Optional["_SearchFilter"]
    IncludedProperties: Optional[Sequence["_IncludedProperty"]]
    Scope: Optional[str]
    Tags: Optional[Any]
    ViewArn: Optional[str]
    ViewName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsResourceexplorer2View"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsResourceexplorer2View"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Filters=SearchFilter._deserialize(json_data.get("Filters")),
            IncludedProperties=deserialize_list(json_data.get("IncludedProperties"), IncludedProperty),
            Scope=json_data.get("Scope"),
            Tags=json_data.get("Tags"),
            ViewArn=json_data.get("ViewArn"),
            ViewName=json_data.get("ViewName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsResourceexplorer2View = AwsResourceexplorer2View


@dataclass
class SearchFilter(BaseModel):
    FilterString: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SearchFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SearchFilter"]:
        if not json_data:
            return None
        return cls(
            FilterString=json_data.get("FilterString"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SearchFilter = SearchFilter


@dataclass
class IncludedProperty(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IncludedProperty"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IncludedProperty"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IncludedProperty = IncludedProperty


