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
class AwsHealthlakeFhirdatastore(BaseModel):
    CreatedAt: Optional["_CreatedAt"]
    DatastoreArn: Optional[str]
    DatastoreEndpoint: Optional[str]
    DatastoreId: Optional[str]
    DatastoreName: Optional[str]
    DatastoreStatus: Optional[str]
    DatastoreTypeVersion: Optional[str]
    PreloadDataConfig: Optional["_PreloadDataConfig"]
    SseConfiguration: Optional["_SseConfiguration"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsHealthlakeFhirdatastore"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsHealthlakeFhirdatastore"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CreatedAt=CreatedAt._deserialize(json_data.get("CreatedAt")),
            DatastoreArn=json_data.get("DatastoreArn"),
            DatastoreEndpoint=json_data.get("DatastoreEndpoint"),
            DatastoreId=json_data.get("DatastoreId"),
            DatastoreName=json_data.get("DatastoreName"),
            DatastoreStatus=json_data.get("DatastoreStatus"),
            DatastoreTypeVersion=json_data.get("DatastoreTypeVersion"),
            PreloadDataConfig=PreloadDataConfig._deserialize(json_data.get("PreloadDataConfig")),
            SseConfiguration=SseConfiguration._deserialize(json_data.get("SseConfiguration")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsHealthlakeFhirdatastore = AwsHealthlakeFhirdatastore


@dataclass
class CreatedAt(BaseModel):
    Seconds: Optional[str]
    Nanos: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_CreatedAt"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreatedAt"]:
        if not json_data:
            return None
        return cls(
            Seconds=json_data.get("Seconds"),
            Nanos=json_data.get("Nanos"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreatedAt = CreatedAt


@dataclass
class PreloadDataConfig(BaseModel):
    PreloadDataType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PreloadDataConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PreloadDataConfig"]:
        if not json_data:
            return None
        return cls(
            PreloadDataType=json_data.get("PreloadDataType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PreloadDataConfig = PreloadDataConfig


@dataclass
class SseConfiguration(BaseModel):
    KmsEncryptionConfig: Optional["_KmsEncryptionConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_SseConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SseConfiguration"]:
        if not json_data:
            return None
        return cls(
            KmsEncryptionConfig=KmsEncryptionConfig._deserialize(json_data.get("KmsEncryptionConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SseConfiguration = SseConfiguration


@dataclass
class KmsEncryptionConfig(BaseModel):
    CmkType: Optional[str]
    KmsKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KmsEncryptionConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KmsEncryptionConfig"]:
        if not json_data:
            return None
        return cls(
            CmkType=json_data.get("CmkType"),
            KmsKeyId=json_data.get("KmsKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KmsEncryptionConfig = KmsEncryptionConfig


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


