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
class AwsKinesisStream(BaseModel):
    StreamModeDetails: Optional["_StreamModeDetails"]
    StreamEncryption: Optional["_StreamEncryption"]
    Arn: Optional[str]
    RetentionPeriodHours: Optional[int]
    Tags: Optional[Any]
    Name: Optional[str]
    ShardCount: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AwsKinesisStream"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsKinesisStream"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            StreamModeDetails=StreamModeDetails._deserialize(json_data.get("StreamModeDetails")),
            StreamEncryption=StreamEncryption._deserialize(json_data.get("StreamEncryption")),
            Arn=json_data.get("Arn"),
            RetentionPeriodHours=json_data.get("RetentionPeriodHours"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
            ShardCount=json_data.get("ShardCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsKinesisStream = AwsKinesisStream


@dataclass
class StreamModeDetails(BaseModel):
    StreamMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StreamModeDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StreamModeDetails"]:
        if not json_data:
            return None
        return cls(
            StreamMode=json_data.get("StreamMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StreamModeDetails = StreamModeDetails


@dataclass
class StreamEncryption(BaseModel):
    EncryptionType: Optional[str]
    KeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StreamEncryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StreamEncryption"]:
        if not json_data:
            return None
        return cls(
            EncryptionType=json_data.get("EncryptionType"),
            KeyId=json_data.get("KeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StreamEncryption = StreamEncryption


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


