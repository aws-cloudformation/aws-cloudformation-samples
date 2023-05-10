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
class AwsLookoutequipmentInferencescheduler(BaseModel):
    DataDelayOffsetInMinutes: Optional[int]
    DataInputConfiguration: Optional["_DataInputConfiguration"]
    DataOutputConfiguration: Optional["_DataOutputConfiguration"]
    DataUploadFrequency: Optional[str]
    InferenceSchedulerName: Optional[str]
    ModelName: Optional[str]
    RoleArn: Optional[str]
    ServerSideKmsKeyId: Optional[str]
    Tags: Optional[Any]
    InferenceSchedulerArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLookoutequipmentInferencescheduler"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLookoutequipmentInferencescheduler"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DataDelayOffsetInMinutes=json_data.get("DataDelayOffsetInMinutes"),
            DataInputConfiguration=DataInputConfiguration._deserialize(json_data.get("DataInputConfiguration")),
            DataOutputConfiguration=DataOutputConfiguration._deserialize(json_data.get("DataOutputConfiguration")),
            DataUploadFrequency=json_data.get("DataUploadFrequency"),
            InferenceSchedulerName=json_data.get("InferenceSchedulerName"),
            ModelName=json_data.get("ModelName"),
            RoleArn=json_data.get("RoleArn"),
            ServerSideKmsKeyId=json_data.get("ServerSideKmsKeyId"),
            Tags=json_data.get("Tags"),
            InferenceSchedulerArn=json_data.get("InferenceSchedulerArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLookoutequipmentInferencescheduler = AwsLookoutequipmentInferencescheduler


@dataclass
class DataInputConfiguration(BaseModel):
    InputTimeZoneOffset: Optional[str]
    InferenceInputNameConfiguration: Optional["_InputNameConfiguration"]
    S3InputConfiguration: Optional["_S3InputConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_DataInputConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataInputConfiguration"]:
        if not json_data:
            return None
        return cls(
            InputTimeZoneOffset=json_data.get("InputTimeZoneOffset"),
            InferenceInputNameConfiguration=InputNameConfiguration._deserialize(json_data.get("InferenceInputNameConfiguration")),
            S3InputConfiguration=S3InputConfiguration._deserialize(json_data.get("S3InputConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataInputConfiguration = DataInputConfiguration


@dataclass
class InputNameConfiguration(BaseModel):
    ComponentTimestampDelimiter: Optional[str]
    TimestampFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputNameConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputNameConfiguration"]:
        if not json_data:
            return None
        return cls(
            ComponentTimestampDelimiter=json_data.get("ComponentTimestampDelimiter"),
            TimestampFormat=json_data.get("TimestampFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputNameConfiguration = InputNameConfiguration


@dataclass
class S3InputConfiguration(BaseModel):
    Bucket: Optional[str]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3InputConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3InputConfiguration"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3InputConfiguration = S3InputConfiguration


@dataclass
class DataOutputConfiguration(BaseModel):
    KmsKeyId: Optional[str]
    S3OutputConfiguration: Optional["_S3OutputConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_DataOutputConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataOutputConfiguration"]:
        if not json_data:
            return None
        return cls(
            KmsKeyId=json_data.get("KmsKeyId"),
            S3OutputConfiguration=S3OutputConfiguration._deserialize(json_data.get("S3OutputConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataOutputConfiguration = DataOutputConfiguration


@dataclass
class S3OutputConfiguration(BaseModel):
    Bucket: Optional[str]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3OutputConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3OutputConfiguration"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3OutputConfiguration = S3OutputConfiguration


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


