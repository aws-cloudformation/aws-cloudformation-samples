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
class AwsIvschatLoggingconfiguration(BaseModel):
    Arn: Optional[str]
    Id: Optional[str]
    DestinationConfiguration: Optional["_DestinationConfiguration"]
    Name: Optional[str]
    State: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIvschatLoggingconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIvschatLoggingconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            DestinationConfiguration=DestinationConfiguration._deserialize(json_data.get("DestinationConfiguration")),
            Name=json_data.get("Name"),
            State=json_data.get("State"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIvschatLoggingconfiguration = AwsIvschatLoggingconfiguration


@dataclass
class DestinationConfiguration(BaseModel):
    CloudWatchLogs: Optional["_CloudWatchLogsDestinationConfiguration"]
    Firehose: Optional["_FirehoseDestinationConfiguration"]
    S3: Optional["_S3DestinationConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationConfiguration"]:
        if not json_data:
            return None
        return cls(
            CloudWatchLogs=CloudWatchLogsDestinationConfiguration._deserialize(json_data.get("CloudWatchLogs")),
            Firehose=FirehoseDestinationConfiguration._deserialize(json_data.get("Firehose")),
            S3=S3DestinationConfiguration._deserialize(json_data.get("S3")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationConfiguration = DestinationConfiguration


@dataclass
class CloudWatchLogsDestinationConfiguration(BaseModel):
    LogGroupName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudWatchLogsDestinationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudWatchLogsDestinationConfiguration"]:
        if not json_data:
            return None
        return cls(
            LogGroupName=json_data.get("LogGroupName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudWatchLogsDestinationConfiguration = CloudWatchLogsDestinationConfiguration


@dataclass
class FirehoseDestinationConfiguration(BaseModel):
    DeliveryStreamName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FirehoseDestinationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FirehoseDestinationConfiguration"]:
        if not json_data:
            return None
        return cls(
            DeliveryStreamName=json_data.get("DeliveryStreamName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FirehoseDestinationConfiguration = FirehoseDestinationConfiguration


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


