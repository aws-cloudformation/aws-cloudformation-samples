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
class AwsAccessanalyzerAnalyzer(BaseModel):
    AnalyzerName: Optional[str]
    ArchiveRules: Optional[Sequence["_ArchiveRule"]]
    Arn: Optional[str]
    Tags: Optional[Any]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAccessanalyzerAnalyzer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAccessanalyzerAnalyzer"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AnalyzerName=json_data.get("AnalyzerName"),
            ArchiveRules=deserialize_list(json_data.get("ArchiveRules"), ArchiveRule),
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAccessanalyzerAnalyzer = AwsAccessanalyzerAnalyzer


@dataclass
class ArchiveRule(BaseModel):
    Filter: Optional[Sequence["_Filter"]]
    RuleName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ArchiveRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArchiveRule"]:
        if not json_data:
            return None
        return cls(
            Filter=deserialize_list(json_data.get("Filter"), Filter),
            RuleName=json_data.get("RuleName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArchiveRule = ArchiveRule


@dataclass
class Filter(BaseModel):
    Contains: Optional[Sequence[str]]
    Eq: Optional[Sequence[str]]
    Exists: Optional[bool]
    Property: Optional[str]
    Neq: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Filter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filter"]:
        if not json_data:
            return None
        return cls(
            Contains=json_data.get("Contains"),
            Eq=json_data.get("Eq"),
            Exists=json_data.get("Exists"),
            Property=json_data.get("Property"),
            Neq=json_data.get("Neq"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Filter = Filter


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


