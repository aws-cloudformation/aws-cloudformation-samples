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
class AwsSagemakerFeaturegroup(BaseModel):
    FeatureGroupName: Optional[str]
    RecordIdentifierFeatureName: Optional[str]
    EventTimeFeatureName: Optional[str]
    FeatureDefinitions: Optional[Sequence["_FeatureDefinition"]]
    OnlineStoreConfig: Optional["_OnlineStoreConfig"]
    OfflineStoreConfig: Optional["_OfflineStoreConfig"]
    RoleArn: Optional[str]
    Description: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSagemakerFeaturegroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSagemakerFeaturegroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            FeatureGroupName=json_data.get("FeatureGroupName"),
            RecordIdentifierFeatureName=json_data.get("RecordIdentifierFeatureName"),
            EventTimeFeatureName=json_data.get("EventTimeFeatureName"),
            FeatureDefinitions=deserialize_list(json_data.get("FeatureDefinitions"), FeatureDefinition),
            OnlineStoreConfig=OnlineStoreConfig._deserialize(json_data.get("OnlineStoreConfig")),
            OfflineStoreConfig=OfflineStoreConfig._deserialize(json_data.get("OfflineStoreConfig")),
            RoleArn=json_data.get("RoleArn"),
            Description=json_data.get("Description"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSagemakerFeaturegroup = AwsSagemakerFeaturegroup


@dataclass
class FeatureDefinition(BaseModel):
    FeatureName: Optional[str]
    FeatureType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FeatureDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FeatureDefinition"]:
        if not json_data:
            return None
        return cls(
            FeatureName=json_data.get("FeatureName"),
            FeatureType=json_data.get("FeatureType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FeatureDefinition = FeatureDefinition


@dataclass
class OnlineStoreConfig(BaseModel):
    SecurityConfig: Optional["_OnlineStoreSecurityConfig"]
    EnableOnlineStore: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_OnlineStoreConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnlineStoreConfig"]:
        if not json_data:
            return None
        return cls(
            SecurityConfig=OnlineStoreSecurityConfig._deserialize(json_data.get("SecurityConfig")),
            EnableOnlineStore=json_data.get("EnableOnlineStore"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnlineStoreConfig = OnlineStoreConfig


@dataclass
class OnlineStoreSecurityConfig(BaseModel):
    KmsKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnlineStoreSecurityConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnlineStoreSecurityConfig"]:
        if not json_data:
            return None
        return cls(
            KmsKeyId=json_data.get("KmsKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnlineStoreSecurityConfig = OnlineStoreSecurityConfig


@dataclass
class OfflineStoreConfig(BaseModel):
    S3StorageConfig: Optional["_S3StorageConfig"]
    DisableGlueTableCreation: Optional[bool]
    DataCatalogConfig: Optional["_DataCatalogConfig"]
    TableFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OfflineStoreConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OfflineStoreConfig"]:
        if not json_data:
            return None
        return cls(
            S3StorageConfig=S3StorageConfig._deserialize(json_data.get("S3StorageConfig")),
            DisableGlueTableCreation=json_data.get("DisableGlueTableCreation"),
            DataCatalogConfig=DataCatalogConfig._deserialize(json_data.get("DataCatalogConfig")),
            TableFormat=json_data.get("TableFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OfflineStoreConfig = OfflineStoreConfig


@dataclass
class S3StorageConfig(BaseModel):
    S3Uri: Optional[str]
    KmsKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3StorageConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3StorageConfig"]:
        if not json_data:
            return None
        return cls(
            S3Uri=json_data.get("S3Uri"),
            KmsKeyId=json_data.get("KmsKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3StorageConfig = S3StorageConfig


@dataclass
class DataCatalogConfig(BaseModel):
    TableName: Optional[str]
    Catalog: Optional[str]
    Database: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataCatalogConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataCatalogConfig"]:
        if not json_data:
            return None
        return cls(
            TableName=json_data.get("TableName"),
            Catalog=json_data.get("Catalog"),
            Database=json_data.get("Database"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataCatalogConfig = DataCatalogConfig


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


