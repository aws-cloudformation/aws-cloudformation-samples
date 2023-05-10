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
class AwsSagemakerPipeline(BaseModel):
    PipelineName: Optional[str]
    PipelineDisplayName: Optional[str]
    PipelineDescription: Optional[str]
    PipelineDefinition: Optional["_PipelineDefinition"]
    RoleArn: Optional[str]
    Tags: Optional[Any]
    ParallelismConfiguration: Optional["_ParallelismConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSagemakerPipeline"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSagemakerPipeline"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            PipelineName=json_data.get("PipelineName"),
            PipelineDisplayName=json_data.get("PipelineDisplayName"),
            PipelineDescription=json_data.get("PipelineDescription"),
            PipelineDefinition=PipelineDefinition._deserialize(json_data.get("PipelineDefinition")),
            RoleArn=json_data.get("RoleArn"),
            Tags=json_data.get("Tags"),
            ParallelismConfiguration=ParallelismConfiguration._deserialize(json_data.get("ParallelismConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSagemakerPipeline = AwsSagemakerPipeline


@dataclass
class PipelineDefinition(BaseModel):
    PipelineDefinitionBody: Optional[str]
    PipelineDefinitionS3Location: Optional["_S3Location"]

    @classmethod
    def _deserialize(
        cls: Type["_PipelineDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipelineDefinition"]:
        if not json_data:
            return None
        return cls(
            PipelineDefinitionBody=json_data.get("PipelineDefinitionBody"),
            PipelineDefinitionS3Location=S3Location._deserialize(json_data.get("PipelineDefinitionS3Location")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipelineDefinition = PipelineDefinition


@dataclass
class S3Location(BaseModel):
    Bucket: Optional[str]
    Key: Optional[str]
    Version: Optional[str]
    ETag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Location"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Location"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Key=json_data.get("Key"),
            Version=json_data.get("Version"),
            ETag=json_data.get("ETag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Location = S3Location


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


@dataclass
class ParallelismConfiguration(BaseModel):
    MaxParallelExecutionSteps: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ParallelismConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParallelismConfiguration"]:
        if not json_data:
            return None
        return cls(
            MaxParallelExecutionSteps=json_data.get("MaxParallelExecutionSteps"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParallelismConfiguration = ParallelismConfiguration


