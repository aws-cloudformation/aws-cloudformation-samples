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
class AwsS3Storagelensgroup(BaseModel):
    Name: Optional[str]
    Filter: Optional["_Filter"]
    StorageLensGroupArn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsS3Storagelensgroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsS3Storagelensgroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Filter=Filter._deserialize(json_data.get("Filter")),
            StorageLensGroupArn=json_data.get("StorageLensGroupArn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsS3Storagelensgroup = AwsS3Storagelensgroup


@dataclass
class Filter(BaseModel):
    MatchAnyPrefix: Optional[AbstractSet[str]]
    MatchAnySuffix: Optional[AbstractSet[str]]
    MatchAnyTag: Optional[AbstractSet["_Tag"]]
    MatchObjectSize: Optional["_MatchObjectSize"]
    MatchObjectAge: Optional["_MatchObjectAge"]
    And: Optional["_And"]
    Or: Optional["_Or"]

    @classmethod
    def _deserialize(
        cls: Type["_Filter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filter"]:
        if not json_data:
            return None
        return cls(
            MatchAnyPrefix=set_or_none(json_data.get("MatchAnyPrefix")),
            MatchAnySuffix=set_or_none(json_data.get("MatchAnySuffix")),
            MatchAnyTag=set_or_none(json_data.get("MatchAnyTag")),
            MatchObjectSize=MatchObjectSize._deserialize(json_data.get("MatchObjectSize")),
            MatchObjectAge=MatchObjectAge._deserialize(json_data.get("MatchObjectAge")),
            And=And._deserialize(json_data.get("And")),
            Or=Or._deserialize(json_data.get("Or")),
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


@dataclass
class MatchObjectSize(BaseModel):
    BytesGreaterThan: Optional[int]
    BytesLessThan: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_MatchObjectSize"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchObjectSize"]:
        if not json_data:
            return None
        return cls(
            BytesGreaterThan=json_data.get("BytesGreaterThan"),
            BytesLessThan=json_data.get("BytesLessThan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchObjectSize = MatchObjectSize


@dataclass
class MatchObjectAge(BaseModel):
    DaysGreaterThan: Optional[int]
    DaysLessThan: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_MatchObjectAge"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchObjectAge"]:
        if not json_data:
            return None
        return cls(
            DaysGreaterThan=json_data.get("DaysGreaterThan"),
            DaysLessThan=json_data.get("DaysLessThan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchObjectAge = MatchObjectAge


@dataclass
class And(BaseModel):
    MatchAnyPrefix: Optional[AbstractSet[str]]
    MatchAnySuffix: Optional[AbstractSet[str]]
    MatchAnyTag: Optional[AbstractSet["_Tag"]]
    MatchObjectSize: Optional["_MatchObjectSize"]
    MatchObjectAge: Optional["_MatchObjectAge"]

    @classmethod
    def _deserialize(
        cls: Type["_And"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_And"]:
        if not json_data:
            return None
        return cls(
            MatchAnyPrefix=set_or_none(json_data.get("MatchAnyPrefix")),
            MatchAnySuffix=set_or_none(json_data.get("MatchAnySuffix")),
            MatchAnyTag=set_or_none(json_data.get("MatchAnyTag")),
            MatchObjectSize=MatchObjectSize._deserialize(json_data.get("MatchObjectSize")),
            MatchObjectAge=MatchObjectAge._deserialize(json_data.get("MatchObjectAge")),
        )


# work around possible type aliasing issues when variable has same name as a model
_And = And


@dataclass
class Or(BaseModel):
    MatchAnyPrefix: Optional[AbstractSet[str]]
    MatchAnySuffix: Optional[AbstractSet[str]]
    MatchAnyTag: Optional[AbstractSet["_Tag"]]
    MatchObjectSize: Optional["_MatchObjectSize"]
    MatchObjectAge: Optional["_MatchObjectAge"]

    @classmethod
    def _deserialize(
        cls: Type["_Or"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Or"]:
        if not json_data:
            return None
        return cls(
            MatchAnyPrefix=set_or_none(json_data.get("MatchAnyPrefix")),
            MatchAnySuffix=set_or_none(json_data.get("MatchAnySuffix")),
            MatchAnyTag=set_or_none(json_data.get("MatchAnyTag")),
            MatchObjectSize=MatchObjectSize._deserialize(json_data.get("MatchObjectSize")),
            MatchObjectAge=MatchObjectAge._deserialize(json_data.get("MatchObjectAge")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Or = Or


