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
class AwsAppstreamAppblock(BaseModel):
    Name: Optional[str]
    Arn: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    SourceS3Location: Optional["_S3Location"]
    SetupScriptDetails: Optional["_ScriptDetails"]
    Tags: Optional[Any]
    CreatedTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppstreamAppblock"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppstreamAppblock"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            SourceS3Location=S3Location._deserialize(json_data.get("SourceS3Location")),
            SetupScriptDetails=ScriptDetails._deserialize(json_data.get("SetupScriptDetails")),
            Tags=json_data.get("Tags"),
            CreatedTime=json_data.get("CreatedTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppstreamAppblock = AwsAppstreamAppblock


@dataclass
class S3Location(BaseModel):
    S3Bucket: Optional[str]
    S3Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Location"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Location"]:
        if not json_data:
            return None
        return cls(
            S3Bucket=json_data.get("S3Bucket"),
            S3Key=json_data.get("S3Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Location = S3Location


@dataclass
class ScriptDetails(BaseModel):
    ScriptS3Location: Optional["_S3Location"]
    ExecutablePath: Optional[str]
    ExecutableParameters: Optional[str]
    TimeoutInSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ScriptDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScriptDetails"]:
        if not json_data:
            return None
        return cls(
            ScriptS3Location=S3Location._deserialize(json_data.get("ScriptS3Location")),
            ExecutablePath=json_data.get("ExecutablePath"),
            ExecutableParameters=json_data.get("ExecutableParameters"),
            TimeoutInSeconds=json_data.get("TimeoutInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScriptDetails = ScriptDetails


@dataclass
class Tag(BaseModel):
    TagKey: Optional[str]
    TagValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            TagKey=json_data.get("TagKey"),
            TagValue=json_data.get("TagValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


