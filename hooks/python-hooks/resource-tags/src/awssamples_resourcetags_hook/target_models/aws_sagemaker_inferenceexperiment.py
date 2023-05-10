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
class AwsSagemakerInferenceexperiment(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    Type: Optional[str]
    Description: Optional[str]
    RoleArn: Optional[str]
    EndpointName: Optional[str]
    EndpointMetadata: Optional["_EndpointMetadata"]
    Schedule: Optional["_InferenceExperimentSchedule"]
    KmsKey: Optional[str]
    DataStorageConfig: Optional["_DataStorageConfig"]
    ModelVariants: Optional[Sequence["_ModelVariantConfig"]]
    ShadowModeConfig: Optional["_ShadowModeConfig"]
    Tags: Optional[Any]
    CreationTime: Optional[str]
    LastModifiedTime: Optional[str]
    Status: Optional[str]
    StatusReason: Optional[str]
    DesiredState: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSagemakerInferenceexperiment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSagemakerInferenceexperiment"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Description=json_data.get("Description"),
            RoleArn=json_data.get("RoleArn"),
            EndpointName=json_data.get("EndpointName"),
            EndpointMetadata=EndpointMetadata._deserialize(json_data.get("EndpointMetadata")),
            Schedule=InferenceExperimentSchedule._deserialize(json_data.get("Schedule")),
            KmsKey=json_data.get("KmsKey"),
            DataStorageConfig=DataStorageConfig._deserialize(json_data.get("DataStorageConfig")),
            ModelVariants=deserialize_list(json_data.get("ModelVariants"), ModelVariantConfig),
            ShadowModeConfig=ShadowModeConfig._deserialize(json_data.get("ShadowModeConfig")),
            Tags=json_data.get("Tags"),
            CreationTime=json_data.get("CreationTime"),
            LastModifiedTime=json_data.get("LastModifiedTime"),
            Status=json_data.get("Status"),
            StatusReason=json_data.get("StatusReason"),
            DesiredState=json_data.get("DesiredState"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSagemakerInferenceexperiment = AwsSagemakerInferenceexperiment


@dataclass
class EndpointMetadata(BaseModel):
    EndpointName: Optional[str]
    EndpointConfigName: Optional[str]
    EndpointStatus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointMetadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointMetadata"]:
        if not json_data:
            return None
        return cls(
            EndpointName=json_data.get("EndpointName"),
            EndpointConfigName=json_data.get("EndpointConfigName"),
            EndpointStatus=json_data.get("EndpointStatus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointMetadata = EndpointMetadata


@dataclass
class InferenceExperimentSchedule(BaseModel):
    StartTime: Optional[str]
    EndTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InferenceExperimentSchedule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InferenceExperimentSchedule"]:
        if not json_data:
            return None
        return cls(
            StartTime=json_data.get("StartTime"),
            EndTime=json_data.get("EndTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InferenceExperimentSchedule = InferenceExperimentSchedule


@dataclass
class DataStorageConfig(BaseModel):
    Destination: Optional[str]
    KmsKey: Optional[str]
    ContentType: Optional["_CaptureContentTypeHeader"]

    @classmethod
    def _deserialize(
        cls: Type["_DataStorageConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataStorageConfig"]:
        if not json_data:
            return None
        return cls(
            Destination=json_data.get("Destination"),
            KmsKey=json_data.get("KmsKey"),
            ContentType=CaptureContentTypeHeader._deserialize(json_data.get("ContentType")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataStorageConfig = DataStorageConfig


@dataclass
class CaptureContentTypeHeader(BaseModel):
    CsvContentTypes: Optional[Sequence[str]]
    JsonContentTypes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CaptureContentTypeHeader"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaptureContentTypeHeader"]:
        if not json_data:
            return None
        return cls(
            CsvContentTypes=json_data.get("CsvContentTypes"),
            JsonContentTypes=json_data.get("JsonContentTypes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CaptureContentTypeHeader = CaptureContentTypeHeader


@dataclass
class ModelVariantConfig(BaseModel):
    ModelName: Optional[str]
    VariantName: Optional[str]
    InfrastructureConfig: Optional["_ModelInfrastructureConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_ModelVariantConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ModelVariantConfig"]:
        if not json_data:
            return None
        return cls(
            ModelName=json_data.get("ModelName"),
            VariantName=json_data.get("VariantName"),
            InfrastructureConfig=ModelInfrastructureConfig._deserialize(json_data.get("InfrastructureConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ModelVariantConfig = ModelVariantConfig


@dataclass
class ModelInfrastructureConfig(BaseModel):
    InfrastructureType: Optional[str]
    RealTimeInferenceConfig: Optional["_RealTimeInferenceConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_ModelInfrastructureConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ModelInfrastructureConfig"]:
        if not json_data:
            return None
        return cls(
            InfrastructureType=json_data.get("InfrastructureType"),
            RealTimeInferenceConfig=RealTimeInferenceConfig._deserialize(json_data.get("RealTimeInferenceConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ModelInfrastructureConfig = ModelInfrastructureConfig


@dataclass
class RealTimeInferenceConfig(BaseModel):
    InstanceType: Optional[str]
    InstanceCount: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_RealTimeInferenceConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RealTimeInferenceConfig"]:
        if not json_data:
            return None
        return cls(
            InstanceType=json_data.get("InstanceType"),
            InstanceCount=json_data.get("InstanceCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RealTimeInferenceConfig = RealTimeInferenceConfig


@dataclass
class ShadowModeConfig(BaseModel):
    SourceModelVariantName: Optional[str]
    ShadowModelVariants: Optional[Sequence["_ShadowModelVariantConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ShadowModeConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShadowModeConfig"]:
        if not json_data:
            return None
        return cls(
            SourceModelVariantName=json_data.get("SourceModelVariantName"),
            ShadowModelVariants=deserialize_list(json_data.get("ShadowModelVariants"), ShadowModelVariantConfig),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShadowModeConfig = ShadowModeConfig


@dataclass
class ShadowModelVariantConfig(BaseModel):
    ShadowModelVariantName: Optional[str]
    SamplingPercentage: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ShadowModelVariantConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShadowModelVariantConfig"]:
        if not json_data:
            return None
        return cls(
            ShadowModelVariantName=json_data.get("ShadowModelVariantName"),
            SamplingPercentage=json_data.get("SamplingPercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShadowModelVariantConfig = ShadowModelVariantConfig


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


