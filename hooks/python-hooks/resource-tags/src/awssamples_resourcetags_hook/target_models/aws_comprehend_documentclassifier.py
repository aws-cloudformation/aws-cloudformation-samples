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
class AwsComprehendDocumentclassifier(BaseModel):
    DataAccessRoleArn: Optional[str]
    InputDataConfig: Optional["_DocumentClassifierInputDataConfig"]
    OutputDataConfig: Optional["_DocumentClassifierOutputDataConfig"]
    LanguageCode: Optional[str]
    ModelKmsKeyId: Optional[str]
    ModelPolicy: Optional[str]
    DocumentClassifierName: Optional[str]
    Mode: Optional[str]
    Tags: Optional[Any]
    VersionName: Optional[str]
    VolumeKmsKeyId: Optional[str]
    VpcConfig: Optional["_VpcConfig"]
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsComprehendDocumentclassifier"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsComprehendDocumentclassifier"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DataAccessRoleArn=json_data.get("DataAccessRoleArn"),
            InputDataConfig=DocumentClassifierInputDataConfig._deserialize(json_data.get("InputDataConfig")),
            OutputDataConfig=DocumentClassifierOutputDataConfig._deserialize(json_data.get("OutputDataConfig")),
            LanguageCode=json_data.get("LanguageCode"),
            ModelKmsKeyId=json_data.get("ModelKmsKeyId"),
            ModelPolicy=json_data.get("ModelPolicy"),
            DocumentClassifierName=json_data.get("DocumentClassifierName"),
            Mode=json_data.get("Mode"),
            Tags=json_data.get("Tags"),
            VersionName=json_data.get("VersionName"),
            VolumeKmsKeyId=json_data.get("VolumeKmsKeyId"),
            VpcConfig=VpcConfig._deserialize(json_data.get("VpcConfig")),
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsComprehendDocumentclassifier = AwsComprehendDocumentclassifier


@dataclass
class DocumentClassifierInputDataConfig(BaseModel):
    AugmentedManifests: Optional[AbstractSet["_AugmentedManifestsListItem"]]
    DataFormat: Optional[str]
    LabelDelimiter: Optional[str]
    DocumentType: Optional[str]
    Documents: Optional["_DocumentClassifierDocuments"]
    DocumentReaderConfig: Optional["_DocumentReaderConfig"]
    S3Uri: Optional[str]
    TestS3Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DocumentClassifierInputDataConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DocumentClassifierInputDataConfig"]:
        if not json_data:
            return None
        return cls(
            AugmentedManifests=set_or_none(json_data.get("AugmentedManifests")),
            DataFormat=json_data.get("DataFormat"),
            LabelDelimiter=json_data.get("LabelDelimiter"),
            DocumentType=json_data.get("DocumentType"),
            Documents=DocumentClassifierDocuments._deserialize(json_data.get("Documents")),
            DocumentReaderConfig=DocumentReaderConfig._deserialize(json_data.get("DocumentReaderConfig")),
            S3Uri=json_data.get("S3Uri"),
            TestS3Uri=json_data.get("TestS3Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DocumentClassifierInputDataConfig = DocumentClassifierInputDataConfig


@dataclass
class AugmentedManifestsListItem(BaseModel):
    AttributeNames: Optional[AbstractSet[str]]
    S3Uri: Optional[str]
    Split: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AugmentedManifestsListItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AugmentedManifestsListItem"]:
        if not json_data:
            return None
        return cls(
            AttributeNames=set_or_none(json_data.get("AttributeNames")),
            S3Uri=json_data.get("S3Uri"),
            Split=json_data.get("Split"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AugmentedManifestsListItem = AugmentedManifestsListItem


@dataclass
class DocumentClassifierDocuments(BaseModel):
    S3Uri: Optional[str]
    TestS3Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DocumentClassifierDocuments"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DocumentClassifierDocuments"]:
        if not json_data:
            return None
        return cls(
            S3Uri=json_data.get("S3Uri"),
            TestS3Uri=json_data.get("TestS3Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DocumentClassifierDocuments = DocumentClassifierDocuments


@dataclass
class DocumentReaderConfig(BaseModel):
    DocumentReadAction: Optional[str]
    DocumentReadMode: Optional[str]
    FeatureTypes: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DocumentReaderConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DocumentReaderConfig"]:
        if not json_data:
            return None
        return cls(
            DocumentReadAction=json_data.get("DocumentReadAction"),
            DocumentReadMode=json_data.get("DocumentReadMode"),
            FeatureTypes=set_or_none(json_data.get("FeatureTypes")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DocumentReaderConfig = DocumentReaderConfig


@dataclass
class DocumentClassifierOutputDataConfig(BaseModel):
    KmsKeyId: Optional[str]
    S3Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DocumentClassifierOutputDataConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DocumentClassifierOutputDataConfig"]:
        if not json_data:
            return None
        return cls(
            KmsKeyId=json_data.get("KmsKeyId"),
            S3Uri=json_data.get("S3Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DocumentClassifierOutputDataConfig = DocumentClassifierOutputDataConfig


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


