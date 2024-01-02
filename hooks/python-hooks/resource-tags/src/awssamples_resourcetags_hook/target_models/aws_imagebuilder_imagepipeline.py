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
class AwsImagebuilderImagepipeline(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    Description: Optional[str]
    ImageTestsConfiguration: Optional["_ImageTestsConfiguration"]
    Status: Optional[str]
    Schedule: Optional["_Schedule"]
    ImageRecipeArn: Optional[str]
    ContainerRecipeArn: Optional[str]
    DistributionConfigurationArn: Optional[str]
    InfrastructureConfigurationArn: Optional[str]
    Workflows: Optional[Sequence["_WorkflowConfiguration"]]
    EnhancedImageMetadataEnabled: Optional[bool]
    ImageScanningConfiguration: Optional["_ImageScanningConfiguration"]
    ExecutionRole: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsImagebuilderImagepipeline"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsImagebuilderImagepipeline"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            ImageTestsConfiguration=ImageTestsConfiguration._deserialize(json_data.get("ImageTestsConfiguration")),
            Status=json_data.get("Status"),
            Schedule=Schedule._deserialize(json_data.get("Schedule")),
            ImageRecipeArn=json_data.get("ImageRecipeArn"),
            ContainerRecipeArn=json_data.get("ContainerRecipeArn"),
            DistributionConfigurationArn=json_data.get("DistributionConfigurationArn"),
            InfrastructureConfigurationArn=json_data.get("InfrastructureConfigurationArn"),
            Workflows=deserialize_list(json_data.get("Workflows"), WorkflowConfiguration),
            EnhancedImageMetadataEnabled=json_data.get("EnhancedImageMetadataEnabled"),
            ImageScanningConfiguration=ImageScanningConfiguration._deserialize(json_data.get("ImageScanningConfiguration")),
            ExecutionRole=json_data.get("ExecutionRole"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsImagebuilderImagepipeline = AwsImagebuilderImagepipeline


@dataclass
class ImageTestsConfiguration(BaseModel):
    ImageTestsEnabled: Optional[bool]
    TimeoutMinutes: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ImageTestsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageTestsConfiguration"]:
        if not json_data:
            return None
        return cls(
            ImageTestsEnabled=json_data.get("ImageTestsEnabled"),
            TimeoutMinutes=json_data.get("TimeoutMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageTestsConfiguration = ImageTestsConfiguration


@dataclass
class Schedule(BaseModel):
    ScheduleExpression: Optional[str]
    PipelineExecutionStartCondition: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Schedule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Schedule"]:
        if not json_data:
            return None
        return cls(
            ScheduleExpression=json_data.get("ScheduleExpression"),
            PipelineExecutionStartCondition=json_data.get("PipelineExecutionStartCondition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Schedule = Schedule


@dataclass
class WorkflowConfiguration(BaseModel):
    WorkflowArn: Optional[str]
    Parameters: Optional[Sequence["_WorkflowParameter"]]
    ParallelGroup: Optional[str]
    OnFailure: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkflowConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkflowConfiguration"]:
        if not json_data:
            return None
        return cls(
            WorkflowArn=json_data.get("WorkflowArn"),
            Parameters=deserialize_list(json_data.get("Parameters"), WorkflowParameter),
            ParallelGroup=json_data.get("ParallelGroup"),
            OnFailure=json_data.get("OnFailure"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkflowConfiguration = WorkflowConfiguration


@dataclass
class WorkflowParameter(BaseModel):
    Name: Optional[str]
    Value: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_WorkflowParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkflowParameter"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkflowParameter = WorkflowParameter


@dataclass
class ImageScanningConfiguration(BaseModel):
    EcrConfiguration: Optional["_EcrConfiguration"]
    ImageScanningEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ImageScanningConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageScanningConfiguration"]:
        if not json_data:
            return None
        return cls(
            EcrConfiguration=EcrConfiguration._deserialize(json_data.get("EcrConfiguration")),
            ImageScanningEnabled=json_data.get("ImageScanningEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageScanningConfiguration = ImageScanningConfiguration


@dataclass
class EcrConfiguration(BaseModel):
    ContainerTags: Optional[Sequence[str]]
    RepositoryName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EcrConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EcrConfiguration"]:
        if not json_data:
            return None
        return cls(
            ContainerTags=json_data.get("ContainerTags"),
            RepositoryName=json_data.get("RepositoryName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EcrConfiguration = EcrConfiguration


