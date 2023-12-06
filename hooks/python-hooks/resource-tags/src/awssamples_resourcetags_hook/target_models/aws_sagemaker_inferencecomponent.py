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
class AwsSagemakerInferencecomponent(BaseModel):
    InferenceComponentArn: Optional[str]
    InferenceComponentName: Optional[str]
    EndpointArn: Optional[str]
    EndpointName: Optional[str]
    VariantName: Optional[str]
    FailureReason: Optional[str]
    Specification: Optional["_InferenceComponentSpecification"]
    RuntimeConfig: Optional["_InferenceComponentRuntimeConfig"]
    InferenceComponentStatus: Optional[str]
    CreationTime: Optional[str]
    LastModifiedTime: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSagemakerInferencecomponent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSagemakerInferencecomponent"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            InferenceComponentArn=json_data.get("InferenceComponentArn"),
            InferenceComponentName=json_data.get("InferenceComponentName"),
            EndpointArn=json_data.get("EndpointArn"),
            EndpointName=json_data.get("EndpointName"),
            VariantName=json_data.get("VariantName"),
            FailureReason=json_data.get("FailureReason"),
            Specification=InferenceComponentSpecification._deserialize(json_data.get("Specification")),
            RuntimeConfig=InferenceComponentRuntimeConfig._deserialize(json_data.get("RuntimeConfig")),
            InferenceComponentStatus=json_data.get("InferenceComponentStatus"),
            CreationTime=json_data.get("CreationTime"),
            LastModifiedTime=json_data.get("LastModifiedTime"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSagemakerInferencecomponent = AwsSagemakerInferencecomponent


@dataclass
class InferenceComponentSpecification(BaseModel):
    ModelName: Optional[str]
    Container: Optional["_InferenceComponentContainerSpecification"]
    StartupParameters: Optional["_InferenceComponentStartupParameters"]
    ComputeResourceRequirements: Optional["_InferenceComponentComputeResourceRequirements"]

    @classmethod
    def _deserialize(
        cls: Type["_InferenceComponentSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InferenceComponentSpecification"]:
        if not json_data:
            return None
        return cls(
            ModelName=json_data.get("ModelName"),
            Container=InferenceComponentContainerSpecification._deserialize(json_data.get("Container")),
            StartupParameters=InferenceComponentStartupParameters._deserialize(json_data.get("StartupParameters")),
            ComputeResourceRequirements=InferenceComponentComputeResourceRequirements._deserialize(json_data.get("ComputeResourceRequirements")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InferenceComponentSpecification = InferenceComponentSpecification


@dataclass
class InferenceComponentContainerSpecification(BaseModel):
    DeployedImage: Optional["_DeployedImage"]
    Image: Optional[str]
    ArtifactUrl: Optional[str]
    Environment: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_InferenceComponentContainerSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InferenceComponentContainerSpecification"]:
        if not json_data:
            return None
        return cls(
            DeployedImage=DeployedImage._deserialize(json_data.get("DeployedImage")),
            Image=json_data.get("Image"),
            ArtifactUrl=json_data.get("ArtifactUrl"),
            Environment=json_data.get("Environment"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InferenceComponentContainerSpecification = InferenceComponentContainerSpecification


@dataclass
class DeployedImage(BaseModel):
    SpecifiedImage: Optional[str]
    ResolvedImage: Optional[str]
    ResolutionTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeployedImage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeployedImage"]:
        if not json_data:
            return None
        return cls(
            SpecifiedImage=json_data.get("SpecifiedImage"),
            ResolvedImage=json_data.get("ResolvedImage"),
            ResolutionTime=json_data.get("ResolutionTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeployedImage = DeployedImage


@dataclass
class InferenceComponentStartupParameters(BaseModel):
    ModelDataDownloadTimeoutInSeconds: Optional[int]
    ContainerStartupHealthCheckTimeoutInSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_InferenceComponentStartupParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InferenceComponentStartupParameters"]:
        if not json_data:
            return None
        return cls(
            ModelDataDownloadTimeoutInSeconds=json_data.get("ModelDataDownloadTimeoutInSeconds"),
            ContainerStartupHealthCheckTimeoutInSeconds=json_data.get("ContainerStartupHealthCheckTimeoutInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InferenceComponentStartupParameters = InferenceComponentStartupParameters


@dataclass
class InferenceComponentComputeResourceRequirements(BaseModel):
    NumberOfCpuCoresRequired: Optional[float]
    NumberOfAcceleratorDevicesRequired: Optional[float]
    MinMemoryRequiredInMb: Optional[int]
    MaxMemoryRequiredInMb: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_InferenceComponentComputeResourceRequirements"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InferenceComponentComputeResourceRequirements"]:
        if not json_data:
            return None
        return cls(
            NumberOfCpuCoresRequired=json_data.get("NumberOfCpuCoresRequired"),
            NumberOfAcceleratorDevicesRequired=json_data.get("NumberOfAcceleratorDevicesRequired"),
            MinMemoryRequiredInMb=json_data.get("MinMemoryRequiredInMb"),
            MaxMemoryRequiredInMb=json_data.get("MaxMemoryRequiredInMb"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InferenceComponentComputeResourceRequirements = InferenceComponentComputeResourceRequirements


@dataclass
class InferenceComponentRuntimeConfig(BaseModel):
    CopyCount: Optional[int]
    DesiredCopyCount: Optional[int]
    CurrentCopyCount: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_InferenceComponentRuntimeConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InferenceComponentRuntimeConfig"]:
        if not json_data:
            return None
        return cls(
            CopyCount=json_data.get("CopyCount"),
            DesiredCopyCount=json_data.get("DesiredCopyCount"),
            CurrentCopyCount=json_data.get("CurrentCopyCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InferenceComponentRuntimeConfig = InferenceComponentRuntimeConfig


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


