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
class AwsIvsRecordingconfiguration(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    State: Optional[str]
    RecordingReconnectWindowSeconds: Optional[int]
    DestinationConfiguration: Optional["_DestinationConfiguration"]
    Tags: Optional[Any]
    ThumbnailConfiguration: Optional["_ThumbnailConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIvsRecordingconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIvsRecordingconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            State=json_data.get("State"),
            RecordingReconnectWindowSeconds=json_data.get("RecordingReconnectWindowSeconds"),
            DestinationConfiguration=DestinationConfiguration._deserialize(json_data.get("DestinationConfiguration")),
            Tags=json_data.get("Tags"),
            ThumbnailConfiguration=ThumbnailConfiguration._deserialize(json_data.get("ThumbnailConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIvsRecordingconfiguration = AwsIvsRecordingconfiguration


@dataclass
class DestinationConfiguration(BaseModel):
    S3: Optional["_S3DestinationConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationConfiguration"]:
        if not json_data:
            return None
        return cls(
            S3=S3DestinationConfiguration._deserialize(json_data.get("S3")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationConfiguration = DestinationConfiguration


@dataclass
class S3DestinationConfiguration(BaseModel):
    BucketName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3DestinationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3DestinationConfiguration"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3DestinationConfiguration = S3DestinationConfiguration


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
class ThumbnailConfiguration(BaseModel):
    RecordingMode: Optional[str]
    TargetIntervalSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ThumbnailConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThumbnailConfiguration"]:
        if not json_data:
            return None
        return cls(
            RecordingMode=json_data.get("RecordingMode"),
            TargetIntervalSeconds=json_data.get("TargetIntervalSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThumbnailConfiguration = ThumbnailConfiguration


