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
class AwsB2biTransformer(BaseModel):
    CreatedAt: Optional[str]
    EdiType: Optional["_EdiType"]
    FileFormat: Optional[str]
    MappingTemplate: Optional[str]
    ModifiedAt: Optional[str]
    Name: Optional[str]
    SampleDocument: Optional[str]
    Status: Optional[str]
    Tags: Optional[Any]
    TransformerArn: Optional[str]
    TransformerId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsB2biTransformer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsB2biTransformer"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CreatedAt=json_data.get("CreatedAt"),
            EdiType=EdiType._deserialize(json_data.get("EdiType")),
            FileFormat=json_data.get("FileFormat"),
            MappingTemplate=json_data.get("MappingTemplate"),
            ModifiedAt=json_data.get("ModifiedAt"),
            Name=json_data.get("Name"),
            SampleDocument=json_data.get("SampleDocument"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            TransformerArn=json_data.get("TransformerArn"),
            TransformerId=json_data.get("TransformerId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsB2biTransformer = AwsB2biTransformer


@dataclass
class EdiType(BaseModel):
    X12Details: Optional["_X12Details"]

    @classmethod
    def _deserialize(
        cls: Type["_EdiType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EdiType"]:
        if not json_data:
            return None
        return cls(
            X12Details=X12Details._deserialize(json_data.get("X12Details")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EdiType = EdiType


@dataclass
class X12Details(BaseModel):
    TransactionSet: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_X12Details"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_X12Details"]:
        if not json_data:
            return None
        return cls(
            TransactionSet=json_data.get("TransactionSet"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_X12Details = X12Details


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


