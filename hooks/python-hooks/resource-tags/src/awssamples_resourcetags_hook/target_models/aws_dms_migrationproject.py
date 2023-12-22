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
class AwsDmsMigrationproject(BaseModel):
    MigrationProjectName: Optional[str]
    MigrationProjectIdentifier: Optional[str]
    MigrationProjectArn: Optional[str]
    MigrationProjectCreationTime: Optional[str]
    InstanceProfileIdentifier: Optional[str]
    InstanceProfileName: Optional[str]
    InstanceProfileArn: Optional[str]
    TransformationRules: Optional[str]
    Description: Optional[str]
    SchemaConversionApplicationAttributes: Optional["_SchemaConversionApplicationAttributes"]
    SourceDataProviderDescriptors: Optional[AbstractSet["_DataProviderDescriptor"]]
    TargetDataProviderDescriptors: Optional[AbstractSet["_DataProviderDescriptor"]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDmsMigrationproject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDmsMigrationproject"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            MigrationProjectName=json_data.get("MigrationProjectName"),
            MigrationProjectIdentifier=json_data.get("MigrationProjectIdentifier"),
            MigrationProjectArn=json_data.get("MigrationProjectArn"),
            MigrationProjectCreationTime=json_data.get("MigrationProjectCreationTime"),
            InstanceProfileIdentifier=json_data.get("InstanceProfileIdentifier"),
            InstanceProfileName=json_data.get("InstanceProfileName"),
            InstanceProfileArn=json_data.get("InstanceProfileArn"),
            TransformationRules=json_data.get("TransformationRules"),
            Description=json_data.get("Description"),
            SchemaConversionApplicationAttributes=SchemaConversionApplicationAttributes._deserialize(json_data.get("SchemaConversionApplicationAttributes")),
            SourceDataProviderDescriptors=set_or_none(json_data.get("SourceDataProviderDescriptors")),
            TargetDataProviderDescriptors=set_or_none(json_data.get("TargetDataProviderDescriptors")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDmsMigrationproject = AwsDmsMigrationproject


@dataclass
class SchemaConversionApplicationAttributes(BaseModel):
    S3BucketPath: Optional[str]
    S3BucketRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaConversionApplicationAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaConversionApplicationAttributes"]:
        if not json_data:
            return None
        return cls(
            S3BucketPath=json_data.get("S3BucketPath"),
            S3BucketRoleArn=json_data.get("S3BucketRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaConversionApplicationAttributes = SchemaConversionApplicationAttributes


@dataclass
class DataProviderDescriptor(BaseModel):
    DataProviderIdentifier: Optional[str]
    DataProviderName: Optional[str]
    DataProviderArn: Optional[str]
    SecretsManagerSecretId: Optional[str]
    SecretsManagerAccessRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataProviderDescriptor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataProviderDescriptor"]:
        if not json_data:
            return None
        return cls(
            DataProviderIdentifier=json_data.get("DataProviderIdentifier"),
            DataProviderName=json_data.get("DataProviderName"),
            DataProviderArn=json_data.get("DataProviderArn"),
            SecretsManagerSecretId=json_data.get("SecretsManagerSecretId"),
            SecretsManagerAccessRoleArn=json_data.get("SecretsManagerAccessRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataProviderDescriptor = DataProviderDescriptor


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


