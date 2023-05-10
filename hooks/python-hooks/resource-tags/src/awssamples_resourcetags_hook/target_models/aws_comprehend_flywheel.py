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
class AwsComprehendFlywheel(BaseModel):
    ActiveModelArn: Optional[str]
    DataAccessRoleArn: Optional[str]
    DataLakeS3Uri: Optional[str]
    DataSecurityConfig: Optional["_DataSecurityConfig"]
    FlywheelName: Optional[str]
    ModelType: Optional[str]
    Tags: Optional[Any]
    TaskConfig: Optional["_TaskConfig"]
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsComprehendFlywheel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsComprehendFlywheel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ActiveModelArn=json_data.get("ActiveModelArn"),
            DataAccessRoleArn=json_data.get("DataAccessRoleArn"),
            DataLakeS3Uri=json_data.get("DataLakeS3Uri"),
            DataSecurityConfig=DataSecurityConfig._deserialize(json_data.get("DataSecurityConfig")),
            FlywheelName=json_data.get("FlywheelName"),
            ModelType=json_data.get("ModelType"),
            Tags=json_data.get("Tags"),
            TaskConfig=TaskConfig._deserialize(json_data.get("TaskConfig")),
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsComprehendFlywheel = AwsComprehendFlywheel


@dataclass
class DataSecurityConfig(BaseModel):
    ModelKmsKeyId: Optional[str]
    VolumeKmsKeyId: Optional[str]
    DataLakeKmsKeyId: Optional[str]
    VpcConfig: Optional["_VpcConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_DataSecurityConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataSecurityConfig"]:
        if not json_data:
            return None
        return cls(
            ModelKmsKeyId=json_data.get("ModelKmsKeyId"),
            VolumeKmsKeyId=json_data.get("VolumeKmsKeyId"),
            DataLakeKmsKeyId=json_data.get("DataLakeKmsKeyId"),
            VpcConfig=VpcConfig._deserialize(json_data.get("VpcConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataSecurityConfig = DataSecurityConfig


@dataclass
class VpcConfig(BaseModel):
    SecurityGroupIds: Optional[AbstractSet[str]]
    Subnets: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfig"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=set_or_none(json_data.get("SecurityGroupIds")),
            Subnets=set_or_none(json_data.get("Subnets")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfig = VpcConfig


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
class TaskConfig(BaseModel):
    LanguageCode: Optional[str]
    DocumentClassificationConfig: Optional["_DocumentClassificationConfig"]
    EntityRecognitionConfig: Optional["_EntityRecognitionConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_TaskConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskConfig"]:
        if not json_data:
            return None
        return cls(
            LanguageCode=json_data.get("LanguageCode"),
            DocumentClassificationConfig=DocumentClassificationConfig._deserialize(json_data.get("DocumentClassificationConfig")),
            EntityRecognitionConfig=EntityRecognitionConfig._deserialize(json_data.get("EntityRecognitionConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskConfig = TaskConfig


@dataclass
class DocumentClassificationConfig(BaseModel):
    Mode: Optional[str]
    Labels: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DocumentClassificationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DocumentClassificationConfig"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
            Labels=set_or_none(json_data.get("Labels")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DocumentClassificationConfig = DocumentClassificationConfig


@dataclass
class EntityRecognitionConfig(BaseModel):
    EntityTypes: Optional[AbstractSet["_EntityTypesListItem"]]

    @classmethod
    def _deserialize(
        cls: Type["_EntityRecognitionConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntityRecognitionConfig"]:
        if not json_data:
            return None
        return cls(
            EntityTypes=set_or_none(json_data.get("EntityTypes")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntityRecognitionConfig = EntityRecognitionConfig


@dataclass
class EntityTypesListItem(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EntityTypesListItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntityTypesListItem"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntityTypesListItem = EntityTypesListItem


