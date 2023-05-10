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
class AwsTimestreamTable(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    DatabaseName: Optional[str]
    TableName: Optional[str]
    RetentionProperties: Optional["_RetentionProperties"]
    MagneticStoreWriteProperties: Optional["_MagneticStoreWriteProperties"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsTimestreamTable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsTimestreamTable"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            DatabaseName=json_data.get("DatabaseName"),
            TableName=json_data.get("TableName"),
            RetentionProperties=RetentionProperties._deserialize(json_data.get("RetentionProperties")),
            MagneticStoreWriteProperties=MagneticStoreWriteProperties._deserialize(json_data.get("MagneticStoreWriteProperties")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsTimestreamTable = AwsTimestreamTable


@dataclass
class RetentionProperties(BaseModel):
    MemoryStoreRetentionPeriodInHours: Optional[str]
    MagneticStoreRetentionPeriodInDays: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionProperties"]:
        if not json_data:
            return None
        return cls(
            MemoryStoreRetentionPeriodInHours=json_data.get("MemoryStoreRetentionPeriodInHours"),
            MagneticStoreRetentionPeriodInDays=json_data.get("MagneticStoreRetentionPeriodInDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionProperties = RetentionProperties


@dataclass
class MagneticStoreWriteProperties(BaseModel):
    EnableMagneticStoreWrites: Optional[bool]
    MagneticStoreRejectedDataLocation: Optional["_MagneticStoreRejectedDataLocation"]

    @classmethod
    def _deserialize(
        cls: Type["_MagneticStoreWriteProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MagneticStoreWriteProperties"]:
        if not json_data:
            return None
        return cls(
            EnableMagneticStoreWrites=json_data.get("EnableMagneticStoreWrites"),
            MagneticStoreRejectedDataLocation=MagneticStoreRejectedDataLocation._deserialize(json_data.get("MagneticStoreRejectedDataLocation")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MagneticStoreWriteProperties = MagneticStoreWriteProperties


@dataclass
class MagneticStoreRejectedDataLocation(BaseModel):
    S3Configuration: Optional["_S3Configuration"]

    @classmethod
    def _deserialize(
        cls: Type["_MagneticStoreRejectedDataLocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MagneticStoreRejectedDataLocation"]:
        if not json_data:
            return None
        return cls(
            S3Configuration=S3Configuration._deserialize(json_data.get("S3Configuration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MagneticStoreRejectedDataLocation = MagneticStoreRejectedDataLocation


@dataclass
class S3Configuration(BaseModel):
    BucketName: Optional[str]
    ObjectKeyPrefix: Optional[str]
    EncryptionOption: Optional[str]
    KmsKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Configuration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Configuration"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            ObjectKeyPrefix=json_data.get("ObjectKeyPrefix"),
            EncryptionOption=json_data.get("EncryptionOption"),
            KmsKeyId=json_data.get("KmsKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Configuration = S3Configuration


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


