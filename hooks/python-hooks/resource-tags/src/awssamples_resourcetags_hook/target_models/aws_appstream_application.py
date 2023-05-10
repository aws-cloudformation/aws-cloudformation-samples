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
class AwsAppstreamApplication(BaseModel):
    Name: Optional[str]
    DisplayName: Optional[str]
    Description: Optional[str]
    LaunchPath: Optional[str]
    LaunchParameters: Optional[str]
    WorkingDirectory: Optional[str]
    InstanceFamilies: Optional[AbstractSet[str]]
    IconS3Location: Optional["_S3Location"]
    Arn: Optional[str]
    AppBlockArn: Optional[str]
    Platforms: Optional[AbstractSet[str]]
    Tags: Optional[Any]
    AttributesToDelete: Optional[AbstractSet[str]]
    CreatedTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppstreamApplication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppstreamApplication"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            DisplayName=json_data.get("DisplayName"),
            Description=json_data.get("Description"),
            LaunchPath=json_data.get("LaunchPath"),
            LaunchParameters=json_data.get("LaunchParameters"),
            WorkingDirectory=json_data.get("WorkingDirectory"),
            InstanceFamilies=set_or_none(json_data.get("InstanceFamilies")),
            IconS3Location=S3Location._deserialize(json_data.get("IconS3Location")),
            Arn=json_data.get("Arn"),
            AppBlockArn=json_data.get("AppBlockArn"),
            Platforms=set_or_none(json_data.get("Platforms")),
            Tags=json_data.get("Tags"),
            AttributesToDelete=set_or_none(json_data.get("AttributesToDelete")),
            CreatedTime=json_data.get("CreatedTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppstreamApplication = AwsAppstreamApplication


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


