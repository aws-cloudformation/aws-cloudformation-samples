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
class AwsSagemakerModelpackage(BaseModel):
    Tags: Optional[Any]
    AdditionalInferenceSpecifications: Optional[Sequence["_AdditionalInferenceSpecificationDefinition"]]
    AdditionalInferenceSpecificationDefinition: Optional["_AdditionalInferenceSpecificationDefinition"]
    CertifyForMarketplace: Optional[bool]
    ClientToken: Optional[str]
    CustomerMetadataProperties: Optional[MutableMapping[str, Any]]
    Domain: Optional[str]
    DriftCheckBaselines: Optional["_DriftCheckBaselines"]
    InferenceSpecification: Optional["_InferenceSpecification"]
    MetadataProperties: Optional["_MetadataProperties"]
    ModelApprovalStatus: Optional[str]
    ModelMetrics: Optional["_ModelMetrics"]
    ModelPackageDescription: Optional[str]
    ModelPackageGroupName: Optional[str]
    ModelPackageName: Optional[str]
    SamplePayloadUrl: Optional[str]
    SourceAlgorithmSpecification: Optional["_SourceAlgorithmSpecification"]
    Task: Optional[str]
    ValidationSpecification: Optional["_ValidationSpecification"]
    ModelPackageArn: Optional[str]
    ApprovalDescription: Optional[str]
    CreationTime: Optional[str]
    LastModifiedBy: Optional["_UserContext"]
    LastModifiedTime: Optional[str]
    ModelPackageStatus: Optional[str]
    ModelPackageVersion: Optional[int]
    AdditionalInferenceSpecificationsToAdd: Optional[Sequence["_AdditionalInferenceSpecificationDefinition"]]
    ModelPackageStatusDetails: Optional["_ModelPackageStatusDetails"]
    ModelPackageStatusItem: Optional["_ModelPackageStatusItem"]
    CreatedBy: Optional["_UserContext"]
    Environment: Optional[MutableMapping[str, Any]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSagemakerModelpackage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSagemakerModelpackage"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Tags=json_data.get("Tags"),
            AdditionalInferenceSpecifications=deserialize_list(json_data.get("AdditionalInferenceSpecifications"), AdditionalInferenceSpecificationDefinition),
            AdditionalInferenceSpecificationDefinition=AdditionalInferenceSpecificationDefinition._deserialize(json_data.get("AdditionalInferenceSpecificationDefinition")),
            CertifyForMarketplace=json_data.get("CertifyForMarketplace"),
            ClientToken=json_data.get("ClientToken"),
            CustomerMetadataProperties=json_data.get("CustomerMetadataProperties"),
            Domain=json_data.get("Domain"),
            DriftCheckBaselines=DriftCheckBaselines._deserialize(json_data.get("DriftCheckBaselines")),
            InferenceSpecification=InferenceSpecification._deserialize(json_data.get("InferenceSpecification")),
            MetadataProperties=MetadataProperties._deserialize(json_data.get("MetadataProperties")),
            ModelApprovalStatus=json_data.get("ModelApprovalStatus"),
            ModelMetrics=ModelMetrics._deserialize(json_data.get("ModelMetrics")),
            ModelPackageDescription=json_data.get("ModelPackageDescription"),
            ModelPackageGroupName=json_data.get("ModelPackageGroupName"),
            ModelPackageName=json_data.get("ModelPackageName"),
            SamplePayloadUrl=json_data.get("SamplePayloadUrl"),
            SourceAlgorithmSpecification=SourceAlgorithmSpecification._deserialize(json_data.get("SourceAlgorithmSpecification")),
            Task=json_data.get("Task"),
            ValidationSpecification=ValidationSpecification._deserialize(json_data.get("ValidationSpecification")),
            ModelPackageArn=json_data.get("ModelPackageArn"),
            ApprovalDescription=json_data.get("ApprovalDescription"),
            CreationTime=json_data.get("CreationTime"),
            LastModifiedBy=UserContext._deserialize(json_data.get("LastModifiedBy")),
            LastModifiedTime=json_data.get("LastModifiedTime"),
            ModelPackageStatus=json_data.get("ModelPackageStatus"),
            ModelPackageVersion=json_data.get("ModelPackageVersion"),
            AdditionalInferenceSpecificationsToAdd=deserialize_list(json_data.get("AdditionalInferenceSpecificationsToAdd"), AdditionalInferenceSpecificationDefinition),
            ModelPackageStatusDetails=ModelPackageStatusDetails._deserialize(json_data.get("ModelPackageStatusDetails")),
            ModelPackageStatusItem=ModelPackageStatusItem._deserialize(json_data.get("ModelPackageStatusItem")),
            CreatedBy=UserContext._deserialize(json_data.get("CreatedBy")),
            Environment=json_data.get("Environment"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSagemakerModelpackage = AwsSagemakerModelpackage


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
class AdditionalInferenceSpecificationDefinition(BaseModel):
    Containers: Optional[Sequence["_ModelPackageContainerDefinition"]]
    Description: Optional[str]
    Name: Optional[str]
    SupportedContentTypes: Optional[Sequence[str]]
    SupportedRealtimeInferenceInstanceTypes: Optional[Sequence[str]]
    SupportedResponseMIMETypes: Optional[Sequence[str]]
    SupportedTransformInstanceTypes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalInferenceSpecificationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalInferenceSpecificationDefinition"]:
        if not json_data:
            return None
        return cls(
            Containers=deserialize_list(json_data.get("Containers"), ModelPackageContainerDefinition),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            SupportedContentTypes=json_data.get("SupportedContentTypes"),
            SupportedRealtimeInferenceInstanceTypes=json_data.get("SupportedRealtimeInferenceInstanceTypes"),
            SupportedResponseMIMETypes=json_data.get("SupportedResponseMIMETypes"),
            SupportedTransformInstanceTypes=json_data.get("SupportedTransformInstanceTypes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalInferenceSpecificationDefinition = AdditionalInferenceSpecificationDefinition


@dataclass
class ModelPackageContainerDefinition(BaseModel):
    ContainerHostname: Optional[str]
    Environment: Optional[MutableMapping[str, Any]]
    ModelInput: Optional["_ModelInput"]
    Image: Optional[str]
    ImageDigest: Optional[str]
    ModelDataUrl: Optional[str]
    ProductId: Optional[str]
    Framework: Optional[str]
    FrameworkVersion: Optional[str]
    NearestModelName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ModelPackageContainerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ModelPackageContainerDefinition"]:
        if not json_data:
            return None
        return cls(
            ContainerHostname=json_data.get("ContainerHostname"),
            Environment=json_data.get("Environment"),
            ModelInput=ModelInput._deserialize(json_data.get("ModelInput")),
            Image=json_data.get("Image"),
            ImageDigest=json_data.get("ImageDigest"),
            ModelDataUrl=json_data.get("ModelDataUrl"),
            ProductId=json_data.get("ProductId"),
            Framework=json_data.get("Framework"),
            FrameworkVersion=json_data.get("FrameworkVersion"),
            NearestModelName=json_data.get("NearestModelName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ModelPackageContainerDefinition = ModelPackageContainerDefinition


@dataclass
class ModelInput(BaseModel):
    DataInputConfig: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ModelInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ModelInput"]:
        if not json_data:
            return None
        return cls(
            DataInputConfig=json_data.get("DataInputConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ModelInput = ModelInput


@dataclass
class DriftCheckBaselines(BaseModel):
    Bias: Optional["_DriftCheckBias"]
    Explainability: Optional["_DriftCheckExplainability"]
    ModelDataQuality: Optional["_DriftCheckModelDataQuality"]
    ModelQuality: Optional["_DriftCheckModelQuality"]

    @classmethod
    def _deserialize(
        cls: Type["_DriftCheckBaselines"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DriftCheckBaselines"]:
        if not json_data:
            return None
        return cls(
            Bias=DriftCheckBias._deserialize(json_data.get("Bias")),
            Explainability=DriftCheckExplainability._deserialize(json_data.get("Explainability")),
            ModelDataQuality=DriftCheckModelDataQuality._deserialize(json_data.get("ModelDataQuality")),
            ModelQuality=DriftCheckModelQuality._deserialize(json_data.get("ModelQuality")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DriftCheckBaselines = DriftCheckBaselines


@dataclass
class DriftCheckBias(BaseModel):
    PostTrainingConstraints: Optional["_MetricsSource"]
    PreTrainingConstraints: Optional["_MetricsSource"]
    ConfigFile: Optional["_FileSource"]

    @classmethod
    def _deserialize(
        cls: Type["_DriftCheckBias"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DriftCheckBias"]:
        if not json_data:
            return None
        return cls(
            PostTrainingConstraints=MetricsSource._deserialize(json_data.get("PostTrainingConstraints")),
            PreTrainingConstraints=MetricsSource._deserialize(json_data.get("PreTrainingConstraints")),
            ConfigFile=FileSource._deserialize(json_data.get("ConfigFile")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DriftCheckBias = DriftCheckBias


@dataclass
class MetricsSource(BaseModel):
    ContentDigest: Optional[str]
    ContentType: Optional[str]
    S3Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricsSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricsSource"]:
        if not json_data:
            return None
        return cls(
            ContentDigest=json_data.get("ContentDigest"),
            ContentType=json_data.get("ContentType"),
            S3Uri=json_data.get("S3Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricsSource = MetricsSource


@dataclass
class FileSource(BaseModel):
    ContentDigest: Optional[str]
    ContentType: Optional[str]
    S3Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FileSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileSource"]:
        if not json_data:
            return None
        return cls(
            ContentDigest=json_data.get("ContentDigest"),
            ContentType=json_data.get("ContentType"),
            S3Uri=json_data.get("S3Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileSource = FileSource


@dataclass
class DriftCheckExplainability(BaseModel):
    Constraints: Optional["_MetricsSource"]
    ConfigFile: Optional["_FileSource"]

    @classmethod
    def _deserialize(
        cls: Type["_DriftCheckExplainability"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DriftCheckExplainability"]:
        if not json_data:
            return None
        return cls(
            Constraints=MetricsSource._deserialize(json_data.get("Constraints")),
            ConfigFile=FileSource._deserialize(json_data.get("ConfigFile")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DriftCheckExplainability = DriftCheckExplainability


@dataclass
class DriftCheckModelDataQuality(BaseModel):
    Constraints: Optional["_MetricsSource"]
    Statistics: Optional["_MetricsSource"]

    @classmethod
    def _deserialize(
        cls: Type["_DriftCheckModelDataQuality"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DriftCheckModelDataQuality"]:
        if not json_data:
            return None
        return cls(
            Constraints=MetricsSource._deserialize(json_data.get("Constraints")),
            Statistics=MetricsSource._deserialize(json_data.get("Statistics")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DriftCheckModelDataQuality = DriftCheckModelDataQuality


@dataclass
class DriftCheckModelQuality(BaseModel):
    Constraints: Optional["_MetricsSource"]
    Statistics: Optional["_MetricsSource"]

    @classmethod
    def _deserialize(
        cls: Type["_DriftCheckModelQuality"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DriftCheckModelQuality"]:
        if not json_data:
            return None
        return cls(
            Constraints=MetricsSource._deserialize(json_data.get("Constraints")),
            Statistics=MetricsSource._deserialize(json_data.get("Statistics")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DriftCheckModelQuality = DriftCheckModelQuality


@dataclass
class InferenceSpecification(BaseModel):
    Containers: Optional[Sequence["_ModelPackageContainerDefinition"]]
    SupportedContentTypes: Optional[Sequence[str]]
    SupportedRealtimeInferenceInstanceTypes: Optional[Sequence[str]]
    SupportedResponseMIMETypes: Optional[Sequence[str]]
    SupportedTransformInstanceTypes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_InferenceSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InferenceSpecification"]:
        if not json_data:
            return None
        return cls(
            Containers=deserialize_list(json_data.get("Containers"), ModelPackageContainerDefinition),
            SupportedContentTypes=json_data.get("SupportedContentTypes"),
            SupportedRealtimeInferenceInstanceTypes=json_data.get("SupportedRealtimeInferenceInstanceTypes"),
            SupportedResponseMIMETypes=json_data.get("SupportedResponseMIMETypes"),
            SupportedTransformInstanceTypes=json_data.get("SupportedTransformInstanceTypes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InferenceSpecification = InferenceSpecification


@dataclass
class MetadataProperties(BaseModel):
    CommitId: Optional[str]
    GeneratedBy: Optional[str]
    ProjectId: Optional[str]
    Repository: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataProperties"]:
        if not json_data:
            return None
        return cls(
            CommitId=json_data.get("CommitId"),
            GeneratedBy=json_data.get("GeneratedBy"),
            ProjectId=json_data.get("ProjectId"),
            Repository=json_data.get("Repository"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataProperties = MetadataProperties


@dataclass
class ModelMetrics(BaseModel):
    Bias: Optional["_Bias"]
    Explainability: Optional["_Explainability"]
    ModelDataQuality: Optional["_ModelDataQuality"]
    ModelQuality: Optional["_ModelQuality"]

    @classmethod
    def _deserialize(
        cls: Type["_ModelMetrics"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ModelMetrics"]:
        if not json_data:
            return None
        return cls(
            Bias=Bias._deserialize(json_data.get("Bias")),
            Explainability=Explainability._deserialize(json_data.get("Explainability")),
            ModelDataQuality=ModelDataQuality._deserialize(json_data.get("ModelDataQuality")),
            ModelQuality=ModelQuality._deserialize(json_data.get("ModelQuality")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ModelMetrics = ModelMetrics


@dataclass
class Bias(BaseModel):
    Report: Optional["_MetricsSource"]
    PreTrainingReport: Optional["_MetricsSource"]
    PostTrainingReport: Optional["_MetricsSource"]

    @classmethod
    def _deserialize(
        cls: Type["_Bias"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Bias"]:
        if not json_data:
            return None
        return cls(
            Report=MetricsSource._deserialize(json_data.get("Report")),
            PreTrainingReport=MetricsSource._deserialize(json_data.get("PreTrainingReport")),
            PostTrainingReport=MetricsSource._deserialize(json_data.get("PostTrainingReport")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Bias = Bias


@dataclass
class Explainability(BaseModel):
    Report: Optional["_MetricsSource"]

    @classmethod
    def _deserialize(
        cls: Type["_Explainability"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Explainability"]:
        if not json_data:
            return None
        return cls(
            Report=MetricsSource._deserialize(json_data.get("Report")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Explainability = Explainability


@dataclass
class ModelDataQuality(BaseModel):
    Constraints: Optional["_MetricsSource"]
    Statistics: Optional["_MetricsSource"]

    @classmethod
    def _deserialize(
        cls: Type["_ModelDataQuality"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ModelDataQuality"]:
        if not json_data:
            return None
        return cls(
            Constraints=MetricsSource._deserialize(json_data.get("Constraints")),
            Statistics=MetricsSource._deserialize(json_data.get("Statistics")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ModelDataQuality = ModelDataQuality


@dataclass
class ModelQuality(BaseModel):
    Constraints: Optional["_MetricsSource"]
    Statistics: Optional["_MetricsSource"]

    @classmethod
    def _deserialize(
        cls: Type["_ModelQuality"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ModelQuality"]:
        if not json_data:
            return None
        return cls(
            Constraints=MetricsSource._deserialize(json_data.get("Constraints")),
            Statistics=MetricsSource._deserialize(json_data.get("Statistics")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ModelQuality = ModelQuality


@dataclass
class SourceAlgorithmSpecification(BaseModel):
    SourceAlgorithms: Optional[Sequence["_SourceAlgorithm"]]

    @classmethod
    def _deserialize(
        cls: Type["_SourceAlgorithmSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceAlgorithmSpecification"]:
        if not json_data:
            return None
        return cls(
            SourceAlgorithms=deserialize_list(json_data.get("SourceAlgorithms"), SourceAlgorithm),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceAlgorithmSpecification = SourceAlgorithmSpecification


@dataclass
class SourceAlgorithm(BaseModel):
    AlgorithmName: Optional[str]
    ModelDataUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceAlgorithm"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceAlgorithm"]:
        if not json_data:
            return None
        return cls(
            AlgorithmName=json_data.get("AlgorithmName"),
            ModelDataUrl=json_data.get("ModelDataUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceAlgorithm = SourceAlgorithm


@dataclass
class ValidationSpecification(BaseModel):
    ValidationProfiles: Optional[Sequence["_ValidationProfile"]]
    ValidationRole: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValidationSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValidationSpecification"]:
        if not json_data:
            return None
        return cls(
            ValidationProfiles=deserialize_list(json_data.get("ValidationProfiles"), ValidationProfile),
            ValidationRole=json_data.get("ValidationRole"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValidationSpecification = ValidationSpecification


@dataclass
class ValidationProfile(BaseModel):
    TransformJobDefinition: Optional["_TransformJobDefinition"]
    ProfileName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValidationProfile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValidationProfile"]:
        if not json_data:
            return None
        return cls(
            TransformJobDefinition=TransformJobDefinition._deserialize(json_data.get("TransformJobDefinition")),
            ProfileName=json_data.get("ProfileName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValidationProfile = ValidationProfile


@dataclass
class TransformJobDefinition(BaseModel):
    Environment: Optional[MutableMapping[str, Any]]
    BatchStrategy: Optional[str]
    MaxConcurrentTransforms: Optional[int]
    MaxPayloadInMB: Optional[int]
    TransformInput: Optional["_TransformInput"]
    TransformOutput: Optional["_TransformOutput"]
    TransformResources: Optional["_TransformResources"]

    @classmethod
    def _deserialize(
        cls: Type["_TransformJobDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransformJobDefinition"]:
        if not json_data:
            return None
        return cls(
            Environment=json_data.get("Environment"),
            BatchStrategy=json_data.get("BatchStrategy"),
            MaxConcurrentTransforms=json_data.get("MaxConcurrentTransforms"),
            MaxPayloadInMB=json_data.get("MaxPayloadInMB"),
            TransformInput=TransformInput._deserialize(json_data.get("TransformInput")),
            TransformOutput=TransformOutput._deserialize(json_data.get("TransformOutput")),
            TransformResources=TransformResources._deserialize(json_data.get("TransformResources")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransformJobDefinition = TransformJobDefinition


@dataclass
class TransformInput(BaseModel):
    CompressionType: Optional[str]
    ContentType: Optional[str]
    DataSource: Optional["_DataSource"]
    SplitType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TransformInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransformInput"]:
        if not json_data:
            return None
        return cls(
            CompressionType=json_data.get("CompressionType"),
            ContentType=json_data.get("ContentType"),
            DataSource=DataSource._deserialize(json_data.get("DataSource")),
            SplitType=json_data.get("SplitType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransformInput = TransformInput


@dataclass
class DataSource(BaseModel):
    S3DataSource: Optional["_S3DataSource"]

    @classmethod
    def _deserialize(
        cls: Type["_DataSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataSource"]:
        if not json_data:
            return None
        return cls(
            S3DataSource=S3DataSource._deserialize(json_data.get("S3DataSource")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataSource = DataSource


@dataclass
class S3DataSource(BaseModel):
    S3DataType: Optional[str]
    S3Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3DataSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3DataSource"]:
        if not json_data:
            return None
        return cls(
            S3DataType=json_data.get("S3DataType"),
            S3Uri=json_data.get("S3Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3DataSource = S3DataSource


@dataclass
class TransformOutput(BaseModel):
    Accept: Optional[str]
    KmsKeyId: Optional[str]
    S3OutputPath: Optional[str]
    AssembleWith: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TransformOutput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransformOutput"]:
        if not json_data:
            return None
        return cls(
            Accept=json_data.get("Accept"),
            KmsKeyId=json_data.get("KmsKeyId"),
            S3OutputPath=json_data.get("S3OutputPath"),
            AssembleWith=json_data.get("AssembleWith"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransformOutput = TransformOutput


@dataclass
class TransformResources(BaseModel):
    InstanceCount: Optional[int]
    InstanceType: Optional[str]
    VolumeKmsKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TransformResources"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransformResources"]:
        if not json_data:
            return None
        return cls(
            InstanceCount=json_data.get("InstanceCount"),
            InstanceType=json_data.get("InstanceType"),
            VolumeKmsKeyId=json_data.get("VolumeKmsKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransformResources = TransformResources


@dataclass
class UserContext(BaseModel):
    DomainId: Optional[str]
    UserProfileArn: Optional[str]
    UserProfileName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserContext"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserContext"]:
        if not json_data:
            return None
        return cls(
            DomainId=json_data.get("DomainId"),
            UserProfileArn=json_data.get("UserProfileArn"),
            UserProfileName=json_data.get("UserProfileName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserContext = UserContext


@dataclass
class ModelPackageStatusDetails(BaseModel):
    ImageScanStatuses: Optional[Sequence["_ModelPackageStatusItem"]]
    ValidationStatuses: Optional[Sequence["_ModelPackageStatusItem"]]

    @classmethod
    def _deserialize(
        cls: Type["_ModelPackageStatusDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ModelPackageStatusDetails"]:
        if not json_data:
            return None
        return cls(
            ImageScanStatuses=deserialize_list(json_data.get("ImageScanStatuses"), ModelPackageStatusItem),
            ValidationStatuses=deserialize_list(json_data.get("ValidationStatuses"), ModelPackageStatusItem),
        )


# work around possible type aliasing issues when variable has same name as a model
_ModelPackageStatusDetails = ModelPackageStatusDetails


@dataclass
class ModelPackageStatusItem(BaseModel):
    FailureReason: Optional[str]
    Name: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ModelPackageStatusItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ModelPackageStatusItem"]:
        if not json_data:
            return None
        return cls(
            FailureReason=json_data.get("FailureReason"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ModelPackageStatusItem = ModelPackageStatusItem


