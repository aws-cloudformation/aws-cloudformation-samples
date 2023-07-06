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
class AwsSagemakerEndpointconfig(BaseModel):
    ShadowProductionVariants: Optional[Sequence["_ProductionVariant"]]
    DataCaptureConfig: Optional["_DataCaptureConfig"]
    ProductionVariants: Optional[Sequence["_ProductionVariant"]]
    KmsKeyId: Optional[str]
    AsyncInferenceConfig: Optional["_AsyncInferenceConfig"]
    EndpointConfigName: Optional[str]
    ExplainerConfig: Optional["_ExplainerConfig"]
    Id: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSagemakerEndpointconfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSagemakerEndpointconfig"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ShadowProductionVariants=deserialize_list(json_data.get("ShadowProductionVariants"), ProductionVariant),
            DataCaptureConfig=DataCaptureConfig._deserialize(json_data.get("DataCaptureConfig")),
            ProductionVariants=deserialize_list(json_data.get("ProductionVariants"), ProductionVariant),
            KmsKeyId=json_data.get("KmsKeyId"),
            AsyncInferenceConfig=AsyncInferenceConfig._deserialize(json_data.get("AsyncInferenceConfig")),
            EndpointConfigName=json_data.get("EndpointConfigName"),
            ExplainerConfig=ExplainerConfig._deserialize(json_data.get("ExplainerConfig")),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSagemakerEndpointconfig = AwsSagemakerEndpointconfig


@dataclass
class ProductionVariant(BaseModel):
    ModelDataDownloadTimeoutInSeconds: Optional[int]
    ModelName: Optional[str]
    VolumeSizeInGB: Optional[int]
    EnableSSMAccess: Optional[bool]
    VariantName: Optional[str]
    ContainerStartupHealthCheckTimeoutInSeconds: Optional[int]
    InitialInstanceCount: Optional[int]
    ServerlessConfig: Optional["_ServerlessConfig"]
    InstanceType: Optional[str]
    AcceleratorType: Optional[str]
    InitialVariantWeight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ProductionVariant"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProductionVariant"]:
        if not json_data:
            return None
        return cls(
            ModelDataDownloadTimeoutInSeconds=json_data.get("ModelDataDownloadTimeoutInSeconds"),
            ModelName=json_data.get("ModelName"),
            VolumeSizeInGB=json_data.get("VolumeSizeInGB"),
            EnableSSMAccess=json_data.get("EnableSSMAccess"),
            VariantName=json_data.get("VariantName"),
            ContainerStartupHealthCheckTimeoutInSeconds=json_data.get("ContainerStartupHealthCheckTimeoutInSeconds"),
            InitialInstanceCount=json_data.get("InitialInstanceCount"),
            ServerlessConfig=ServerlessConfig._deserialize(json_data.get("ServerlessConfig")),
            InstanceType=json_data.get("InstanceType"),
            AcceleratorType=json_data.get("AcceleratorType"),
            InitialVariantWeight=json_data.get("InitialVariantWeight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProductionVariant = ProductionVariant


@dataclass
class ServerlessConfig(BaseModel):
    MaxConcurrency: Optional[int]
    MemorySizeInMB: Optional[int]
    ProvisionedConcurrency: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ServerlessConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerlessConfig"]:
        if not json_data:
            return None
        return cls(
            MaxConcurrency=json_data.get("MaxConcurrency"),
            MemorySizeInMB=json_data.get("MemorySizeInMB"),
            ProvisionedConcurrency=json_data.get("ProvisionedConcurrency"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerlessConfig = ServerlessConfig


@dataclass
class DataCaptureConfig(BaseModel):
    CaptureOptions: Optional[Sequence["_CaptureOption"]]
    KmsKeyId: Optional[str]
    DestinationS3Uri: Optional[str]
    InitialSamplingPercentage: Optional[int]
    CaptureContentTypeHeader: Optional["_CaptureContentTypeHeader"]
    EnableCapture: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DataCaptureConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataCaptureConfig"]:
        if not json_data:
            return None
        return cls(
            CaptureOptions=deserialize_list(json_data.get("CaptureOptions"), CaptureOption),
            KmsKeyId=json_data.get("KmsKeyId"),
            DestinationS3Uri=json_data.get("DestinationS3Uri"),
            InitialSamplingPercentage=json_data.get("InitialSamplingPercentage"),
            CaptureContentTypeHeader=CaptureContentTypeHeader._deserialize(json_data.get("CaptureContentTypeHeader")),
            EnableCapture=json_data.get("EnableCapture"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataCaptureConfig = DataCaptureConfig


@dataclass
class CaptureOption(BaseModel):
    CaptureMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CaptureOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaptureOption"]:
        if not json_data:
            return None
        return cls(
            CaptureMode=json_data.get("CaptureMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CaptureOption = CaptureOption


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
class AsyncInferenceConfig(BaseModel):
    ClientConfig: Optional["_AsyncInferenceClientConfig"]
    OutputConfig: Optional["_AsyncInferenceOutputConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_AsyncInferenceConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AsyncInferenceConfig"]:
        if not json_data:
            return None
        return cls(
            ClientConfig=AsyncInferenceClientConfig._deserialize(json_data.get("ClientConfig")),
            OutputConfig=AsyncInferenceOutputConfig._deserialize(json_data.get("OutputConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AsyncInferenceConfig = AsyncInferenceConfig


@dataclass
class AsyncInferenceClientConfig(BaseModel):
    MaxConcurrentInvocationsPerInstance: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AsyncInferenceClientConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AsyncInferenceClientConfig"]:
        if not json_data:
            return None
        return cls(
            MaxConcurrentInvocationsPerInstance=json_data.get("MaxConcurrentInvocationsPerInstance"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AsyncInferenceClientConfig = AsyncInferenceClientConfig


@dataclass
class AsyncInferenceOutputConfig(BaseModel):
    NotificationConfig: Optional["_AsyncInferenceNotificationConfig"]
    KmsKeyId: Optional[str]
    S3OutputPath: Optional[str]
    S3FailurePath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AsyncInferenceOutputConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AsyncInferenceOutputConfig"]:
        if not json_data:
            return None
        return cls(
            NotificationConfig=AsyncInferenceNotificationConfig._deserialize(json_data.get("NotificationConfig")),
            KmsKeyId=json_data.get("KmsKeyId"),
            S3OutputPath=json_data.get("S3OutputPath"),
            S3FailurePath=json_data.get("S3FailurePath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AsyncInferenceOutputConfig = AsyncInferenceOutputConfig


@dataclass
class AsyncInferenceNotificationConfig(BaseModel):
    IncludeInferenceResponseIn: Optional[Sequence[str]]
    SuccessTopic: Optional[str]
    ErrorTopic: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AsyncInferenceNotificationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AsyncInferenceNotificationConfig"]:
        if not json_data:
            return None
        return cls(
            IncludeInferenceResponseIn=json_data.get("IncludeInferenceResponseIn"),
            SuccessTopic=json_data.get("SuccessTopic"),
            ErrorTopic=json_data.get("ErrorTopic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AsyncInferenceNotificationConfig = AsyncInferenceNotificationConfig


@dataclass
class ExplainerConfig(BaseModel):
    ClarifyExplainerConfig: Optional["_ClarifyExplainerConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_ExplainerConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExplainerConfig"]:
        if not json_data:
            return None
        return cls(
            ClarifyExplainerConfig=ClarifyExplainerConfig._deserialize(json_data.get("ClarifyExplainerConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExplainerConfig = ExplainerConfig


@dataclass
class ClarifyExplainerConfig(BaseModel):
    EnableExplanations: Optional[str]
    ShapConfig: Optional["_ClarifyShapConfig"]
    InferenceConfig: Optional["_ClarifyInferenceConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_ClarifyExplainerConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClarifyExplainerConfig"]:
        if not json_data:
            return None
        return cls(
            EnableExplanations=json_data.get("EnableExplanations"),
            ShapConfig=ClarifyShapConfig._deserialize(json_data.get("ShapConfig")),
            InferenceConfig=ClarifyInferenceConfig._deserialize(json_data.get("InferenceConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClarifyExplainerConfig = ClarifyExplainerConfig


@dataclass
class ClarifyShapConfig(BaseModel):
    TextConfig: Optional["_ClarifyTextConfig"]
    UseLogit: Optional[bool]
    Seed: Optional[int]
    ShapBaselineConfig: Optional["_ClarifyShapBaselineConfig"]
    NumberOfSamples: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ClarifyShapConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClarifyShapConfig"]:
        if not json_data:
            return None
        return cls(
            TextConfig=ClarifyTextConfig._deserialize(json_data.get("TextConfig")),
            UseLogit=json_data.get("UseLogit"),
            Seed=json_data.get("Seed"),
            ShapBaselineConfig=ClarifyShapBaselineConfig._deserialize(json_data.get("ShapBaselineConfig")),
            NumberOfSamples=json_data.get("NumberOfSamples"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClarifyShapConfig = ClarifyShapConfig


@dataclass
class ClarifyTextConfig(BaseModel):
    Language: Optional[str]
    Granularity: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClarifyTextConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClarifyTextConfig"]:
        if not json_data:
            return None
        return cls(
            Language=json_data.get("Language"),
            Granularity=json_data.get("Granularity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClarifyTextConfig = ClarifyTextConfig


@dataclass
class ClarifyShapBaselineConfig(BaseModel):
    MimeType: Optional[str]
    ShapBaseline: Optional[str]
    ShapBaselineUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClarifyShapBaselineConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClarifyShapBaselineConfig"]:
        if not json_data:
            return None
        return cls(
            MimeType=json_data.get("MimeType"),
            ShapBaseline=json_data.get("ShapBaseline"),
            ShapBaselineUri=json_data.get("ShapBaselineUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClarifyShapBaselineConfig = ClarifyShapBaselineConfig


@dataclass
class ClarifyInferenceConfig(BaseModel):
    ContentTemplate: Optional[str]
    LabelHeaders: Optional[Sequence[MutableMapping[str, Any]]]
    MaxPayloadInMB: Optional[int]
    ProbabilityIndex: Optional[int]
    LabelAttribute: Optional[str]
    FeatureTypes: Optional[Sequence[MutableMapping[str, Any]]]
    FeatureHeaders: Optional[Sequence[MutableMapping[str, Any]]]
    LabelIndex: Optional[int]
    ProbabilityAttribute: Optional[str]
    FeaturesAttribute: Optional[str]
    MaxRecordCount: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ClarifyInferenceConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClarifyInferenceConfig"]:
        if not json_data:
            return None
        return cls(
            ContentTemplate=json_data.get("ContentTemplate"),
            LabelHeaders=json_data.get("LabelHeaders"),
            MaxPayloadInMB=json_data.get("MaxPayloadInMB"),
            ProbabilityIndex=json_data.get("ProbabilityIndex"),
            LabelAttribute=json_data.get("LabelAttribute"),
            FeatureTypes=json_data.get("FeatureTypes"),
            FeatureHeaders=json_data.get("FeatureHeaders"),
            LabelIndex=json_data.get("LabelIndex"),
            ProbabilityAttribute=json_data.get("ProbabilityAttribute"),
            FeaturesAttribute=json_data.get("FeaturesAttribute"),
            MaxRecordCount=json_data.get("MaxRecordCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClarifyInferenceConfig = ClarifyInferenceConfig


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


