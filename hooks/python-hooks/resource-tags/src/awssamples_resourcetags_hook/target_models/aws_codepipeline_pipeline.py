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
class AwsCodepipelinePipeline(BaseModel):
    ArtifactStores: Optional[Sequence["_ArtifactStoreMap"]]
    DisableInboundStageTransitions: Optional[Sequence["_StageTransition"]]
    Stages: Optional[Sequence["_StageDeclaration"]]
    RestartExecutionOnUpdate: Optional[bool]
    Triggers: Optional[Sequence["_PipelineTriggerDeclaration"]]
    RoleArn: Optional[str]
    Name: Optional[str]
    Variables: Optional[Sequence["_VariableDeclaration"]]
    Version: Optional[str]
    ArtifactStore: Optional["_ArtifactStore"]
    PipelineType: Optional[str]
    Id: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCodepipelinePipeline"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCodepipelinePipeline"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ArtifactStores=deserialize_list(json_data.get("ArtifactStores"), ArtifactStoreMap),
            DisableInboundStageTransitions=deserialize_list(json_data.get("DisableInboundStageTransitions"), StageTransition),
            Stages=deserialize_list(json_data.get("Stages"), StageDeclaration),
            RestartExecutionOnUpdate=json_data.get("RestartExecutionOnUpdate"),
            Triggers=deserialize_list(json_data.get("Triggers"), PipelineTriggerDeclaration),
            RoleArn=json_data.get("RoleArn"),
            Name=json_data.get("Name"),
            Variables=deserialize_list(json_data.get("Variables"), VariableDeclaration),
            Version=json_data.get("Version"),
            ArtifactStore=ArtifactStore._deserialize(json_data.get("ArtifactStore")),
            PipelineType=json_data.get("PipelineType"),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCodepipelinePipeline = AwsCodepipelinePipeline


@dataclass
class ArtifactStoreMap(BaseModel):
    ArtifactStore: Optional["_ArtifactStore"]
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ArtifactStoreMap"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArtifactStoreMap"]:
        if not json_data:
            return None
        return cls(
            ArtifactStore=ArtifactStore._deserialize(json_data.get("ArtifactStore")),
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArtifactStoreMap = ArtifactStoreMap


@dataclass
class ArtifactStore(BaseModel):
    Type: Optional[str]
    EncryptionKey: Optional["_EncryptionKey"]
    Location: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ArtifactStore"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArtifactStore"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            EncryptionKey=EncryptionKey._deserialize(json_data.get("EncryptionKey")),
            Location=json_data.get("Location"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArtifactStore = ArtifactStore


@dataclass
class EncryptionKey(BaseModel):
    Type: Optional[str]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionKey"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionKey = EncryptionKey


@dataclass
class StageTransition(BaseModel):
    StageName: Optional[str]
    Reason: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StageTransition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StageTransition"]:
        if not json_data:
            return None
        return cls(
            StageName=json_data.get("StageName"),
            Reason=json_data.get("Reason"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StageTransition = StageTransition


@dataclass
class StageDeclaration(BaseModel):
    Blockers: Optional[Sequence["_BlockerDeclaration"]]
    Actions: Optional[Sequence["_ActionDeclaration"]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StageDeclaration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StageDeclaration"]:
        if not json_data:
            return None
        return cls(
            Blockers=deserialize_list(json_data.get("Blockers"), BlockerDeclaration),
            Actions=deserialize_list(json_data.get("Actions"), ActionDeclaration),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StageDeclaration = StageDeclaration


@dataclass
class BlockerDeclaration(BaseModel):
    Type: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BlockerDeclaration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlockerDeclaration"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlockerDeclaration = BlockerDeclaration


@dataclass
class ActionDeclaration(BaseModel):
    ActionTypeId: Optional["_ActionTypeId"]
    Configuration: Optional[MutableMapping[str, Any]]
    InputArtifacts: Optional[Sequence["_InputArtifact"]]
    OutputArtifacts: Optional[Sequence["_OutputArtifact"]]
    Region: Optional[str]
    Namespace: Optional[str]
    RoleArn: Optional[str]
    RunOrder: Optional[int]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDeclaration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDeclaration"]:
        if not json_data:
            return None
        return cls(
            ActionTypeId=ActionTypeId._deserialize(json_data.get("ActionTypeId")),
            Configuration=json_data.get("Configuration"),
            InputArtifacts=deserialize_list(json_data.get("InputArtifacts"), InputArtifact),
            OutputArtifacts=deserialize_list(json_data.get("OutputArtifacts"), OutputArtifact),
            Region=json_data.get("Region"),
            Namespace=json_data.get("Namespace"),
            RoleArn=json_data.get("RoleArn"),
            RunOrder=json_data.get("RunOrder"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDeclaration = ActionDeclaration


@dataclass
class ActionTypeId(BaseModel):
    Owner: Optional[str]
    Category: Optional[str]
    Version: Optional[str]
    Provider: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActionTypeId"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionTypeId"]:
        if not json_data:
            return None
        return cls(
            Owner=json_data.get("Owner"),
            Category=json_data.get("Category"),
            Version=json_data.get("Version"),
            Provider=json_data.get("Provider"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionTypeId = ActionTypeId


@dataclass
class InputArtifact(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputArtifact"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputArtifact"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputArtifact = InputArtifact


@dataclass
class OutputArtifact(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutputArtifact"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputArtifact"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputArtifact = OutputArtifact


@dataclass
class PipelineTriggerDeclaration(BaseModel):
    GitConfiguration: Optional["_GitConfiguration"]
    ProviderType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PipelineTriggerDeclaration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipelineTriggerDeclaration"]:
        if not json_data:
            return None
        return cls(
            GitConfiguration=GitConfiguration._deserialize(json_data.get("GitConfiguration")),
            ProviderType=json_data.get("ProviderType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipelineTriggerDeclaration = PipelineTriggerDeclaration


@dataclass
class GitConfiguration(BaseModel):
    Push: Optional[Sequence["_GitPushFilter"]]
    SourceActionName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GitConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GitConfiguration"]:
        if not json_data:
            return None
        return cls(
            Push=deserialize_list(json_data.get("Push"), GitPushFilter),
            SourceActionName=json_data.get("SourceActionName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GitConfiguration = GitConfiguration


@dataclass
class GitPushFilter(BaseModel):
    Tags: Optional["_GitTagFilterCriteria"]

    @classmethod
    def _deserialize(
        cls: Type["_GitPushFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GitPushFilter"]:
        if not json_data:
            return None
        return cls(
            Tags=GitTagFilterCriteria._deserialize(json_data.get("Tags")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GitPushFilter = GitPushFilter


@dataclass
class GitTagFilterCriteria(BaseModel):
    Includes: Optional[Sequence[str]]
    Excludes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_GitTagFilterCriteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GitTagFilterCriteria"]:
        if not json_data:
            return None
        return cls(
            Includes=json_data.get("Includes"),
            Excludes=json_data.get("Excludes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GitTagFilterCriteria = GitTagFilterCriteria


@dataclass
class VariableDeclaration(BaseModel):
    DefaultValue: Optional[str]
    Description: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VariableDeclaration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VariableDeclaration"]:
        if not json_data:
            return None
        return cls(
            DefaultValue=json_data.get("DefaultValue"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VariableDeclaration = VariableDeclaration


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


