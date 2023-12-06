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
class AwsEntityresolutionIdmappingworkflow(BaseModel):
    WorkflowName: Optional[str]
    Description: Optional[str]
    InputSourceConfig: Optional[Sequence["_IdMappingWorkflowInputSource"]]
    OutputSourceConfig: Optional[Sequence["_IdMappingWorkflowOutputSource"]]
    IdMappingTechniques: Optional["_IdMappingTechniques"]
    RoleArn: Optional[str]
    Tags: Optional[Any]
    WorkflowArn: Optional[str]
    CreatedAt: Optional[str]
    UpdatedAt: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEntityresolutionIdmappingworkflow"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEntityresolutionIdmappingworkflow"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            WorkflowName=json_data.get("WorkflowName"),
            Description=json_data.get("Description"),
            InputSourceConfig=deserialize_list(json_data.get("InputSourceConfig"), IdMappingWorkflowInputSource),
            OutputSourceConfig=deserialize_list(json_data.get("OutputSourceConfig"), IdMappingWorkflowOutputSource),
            IdMappingTechniques=IdMappingTechniques._deserialize(json_data.get("IdMappingTechniques")),
            RoleArn=json_data.get("RoleArn"),
            Tags=json_data.get("Tags"),
            WorkflowArn=json_data.get("WorkflowArn"),
            CreatedAt=json_data.get("CreatedAt"),
            UpdatedAt=json_data.get("UpdatedAt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEntityresolutionIdmappingworkflow = AwsEntityresolutionIdmappingworkflow


@dataclass
class IdMappingWorkflowInputSource(BaseModel):
    InputSourceARN: Optional[str]
    SchemaArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdMappingWorkflowInputSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdMappingWorkflowInputSource"]:
        if not json_data:
            return None
        return cls(
            InputSourceARN=json_data.get("InputSourceARN"),
            SchemaArn=json_data.get("SchemaArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdMappingWorkflowInputSource = IdMappingWorkflowInputSource


@dataclass
class IdMappingWorkflowOutputSource(BaseModel):
    OutputS3Path: Optional[str]
    KMSArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdMappingWorkflowOutputSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdMappingWorkflowOutputSource"]:
        if not json_data:
            return None
        return cls(
            OutputS3Path=json_data.get("OutputS3Path"),
            KMSArn=json_data.get("KMSArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdMappingWorkflowOutputSource = IdMappingWorkflowOutputSource


@dataclass
class IdMappingTechniques(BaseModel):
    IdMappingType: Optional[str]
    ProviderProperties: Optional["_ProviderProperties"]

    @classmethod
    def _deserialize(
        cls: Type["_IdMappingTechniques"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdMappingTechniques"]:
        if not json_data:
            return None
        return cls(
            IdMappingType=json_data.get("IdMappingType"),
            ProviderProperties=ProviderProperties._deserialize(json_data.get("ProviderProperties")),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdMappingTechniques = IdMappingTechniques


@dataclass
class ProviderProperties(BaseModel):
    ProviderServiceArn: Optional[str]
    ProviderConfiguration: Optional[MutableMapping[str, str]]
    IntermediateSourceConfiguration: Optional["_IntermediateSourceConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ProviderProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProviderProperties"]:
        if not json_data:
            return None
        return cls(
            ProviderServiceArn=json_data.get("ProviderServiceArn"),
            ProviderConfiguration=json_data.get("ProviderConfiguration"),
            IntermediateSourceConfiguration=IntermediateSourceConfiguration._deserialize(json_data.get("IntermediateSourceConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProviderProperties = ProviderProperties


@dataclass
class IntermediateSourceConfiguration(BaseModel):
    IntermediateS3Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IntermediateSourceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntermediateSourceConfiguration"]:
        if not json_data:
            return None
        return cls(
            IntermediateS3Path=json_data.get("IntermediateS3Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntermediateSourceConfiguration = IntermediateSourceConfiguration


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


