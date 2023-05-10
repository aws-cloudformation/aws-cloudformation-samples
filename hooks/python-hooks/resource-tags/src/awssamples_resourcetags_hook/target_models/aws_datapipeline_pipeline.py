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
class AwsDatapipelinePipeline(BaseModel):
    Activate: Optional[bool]
    Description: Optional[str]
    Name: Optional[str]
    ParameterObjects: Optional[Sequence["_ParameterObject"]]
    ParameterValues: Optional[Sequence["_ParameterValue"]]
    PipelineObjects: Optional[Sequence["_PipelineObject"]]
    PipelineTags: Optional[Sequence["_PipelineTag"]]
    PipelineId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDatapipelinePipeline"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDatapipelinePipeline"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Activate=json_data.get("Activate"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            ParameterObjects=deserialize_list(json_data.get("ParameterObjects"), ParameterObject),
            ParameterValues=deserialize_list(json_data.get("ParameterValues"), ParameterValue),
            PipelineObjects=deserialize_list(json_data.get("PipelineObjects"), PipelineObject),
            PipelineTags=deserialize_list(json_data.get("PipelineTags"), PipelineTag),
            PipelineId=json_data.get("PipelineId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDatapipelinePipeline = AwsDatapipelinePipeline


@dataclass
class ParameterObject(BaseModel):
    Attributes: Optional[Sequence["_ParameterAttribute"]]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterObject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterObject"]:
        if not json_data:
            return None
        return cls(
            Attributes=deserialize_list(json_data.get("Attributes"), ParameterAttribute),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterObject = ParameterObject


@dataclass
class ParameterAttribute(BaseModel):
    Key: Optional[str]
    StringValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterAttribute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterAttribute"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            StringValue=json_data.get("StringValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterAttribute = ParameterAttribute


@dataclass
class ParameterValue(BaseModel):
    Id: Optional[str]
    StringValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterValue"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            StringValue=json_data.get("StringValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterValue = ParameterValue


@dataclass
class PipelineObject(BaseModel):
    Fields: Optional[Sequence["_Field"]]
    Id: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PipelineObject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipelineObject"]:
        if not json_data:
            return None
        return cls(
            Fields=deserialize_list(json_data.get("Fields"), Field),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipelineObject = PipelineObject


@dataclass
class Field(BaseModel):
    Key: Optional[str]
    RefValue: Optional[str]
    StringValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Field"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Field"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            RefValue=json_data.get("RefValue"),
            StringValue=json_data.get("StringValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Field = Field


@dataclass
class PipelineTag(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PipelineTag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipelineTag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipelineTag = PipelineTag


