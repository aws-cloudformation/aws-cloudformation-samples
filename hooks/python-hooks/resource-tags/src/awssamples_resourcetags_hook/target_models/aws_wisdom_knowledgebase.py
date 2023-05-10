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
class AwsWisdomKnowledgebase(BaseModel):
    Description: Optional[str]
    KnowledgeBaseArn: Optional[str]
    KnowledgeBaseId: Optional[str]
    KnowledgeBaseType: Optional[str]
    Name: Optional[str]
    RenderingConfiguration: Optional["_RenderingConfiguration"]
    ServerSideEncryptionConfiguration: Optional["_ServerSideEncryptionConfiguration"]
    SourceConfiguration: Optional["_SourceConfiguration"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsWisdomKnowledgebase"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsWisdomKnowledgebase"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            KnowledgeBaseArn=json_data.get("KnowledgeBaseArn"),
            KnowledgeBaseId=json_data.get("KnowledgeBaseId"),
            KnowledgeBaseType=json_data.get("KnowledgeBaseType"),
            Name=json_data.get("Name"),
            RenderingConfiguration=RenderingConfiguration._deserialize(json_data.get("RenderingConfiguration")),
            ServerSideEncryptionConfiguration=ServerSideEncryptionConfiguration._deserialize(json_data.get("ServerSideEncryptionConfiguration")),
            SourceConfiguration=SourceConfiguration._deserialize(json_data.get("SourceConfiguration")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsWisdomKnowledgebase = AwsWisdomKnowledgebase


@dataclass
class RenderingConfiguration(BaseModel):
    TemplateUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RenderingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RenderingConfiguration"]:
        if not json_data:
            return None
        return cls(
            TemplateUri=json_data.get("TemplateUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RenderingConfiguration = RenderingConfiguration


@dataclass
class ServerSideEncryptionConfiguration(BaseModel):
    KmsKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerSideEncryptionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerSideEncryptionConfiguration"]:
        if not json_data:
            return None
        return cls(
            KmsKeyId=json_data.get("KmsKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerSideEncryptionConfiguration = ServerSideEncryptionConfiguration


@dataclass
class SourceConfiguration(BaseModel):
    AppIntegrations: Optional["_AppIntegrationsConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_SourceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceConfiguration"]:
        if not json_data:
            return None
        return cls(
            AppIntegrations=AppIntegrationsConfiguration._deserialize(json_data.get("AppIntegrations")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceConfiguration = SourceConfiguration


@dataclass
class AppIntegrationsConfiguration(BaseModel):
    ObjectFields: Optional[Sequence[str]]
    AppIntegrationArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AppIntegrationsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppIntegrationsConfiguration"]:
        if not json_data:
            return None
        return cls(
            ObjectFields=json_data.get("ObjectFields"),
            AppIntegrationArn=json_data.get("AppIntegrationArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppIntegrationsConfiguration = AppIntegrationsConfiguration


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


