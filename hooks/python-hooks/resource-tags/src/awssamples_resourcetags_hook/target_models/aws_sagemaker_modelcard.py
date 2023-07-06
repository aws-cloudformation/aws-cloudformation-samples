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
class AwsSagemakerModelcard(BaseModel):
    ModelCardArn: Optional[str]
    ModelCardVersion: Optional[int]
    ModelCardName: Optional[str]
    SecurityConfig: Optional["_SecurityConfig"]
    ModelCardStatus: Optional[str]
    Content: Optional["_Content"]
    CreationTime: Optional[str]
    CreatedBy: Optional["_UserContext"]
    LastModifiedTime: Optional[str]
    LastModifiedBy: Optional["_UserContext"]
    ModelCardProcessingStatus: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSagemakerModelcard"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSagemakerModelcard"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ModelCardArn=json_data.get("ModelCardArn"),
            ModelCardVersion=json_data.get("ModelCardVersion"),
            ModelCardName=json_data.get("ModelCardName"),
            SecurityConfig=SecurityConfig._deserialize(json_data.get("SecurityConfig")),
            ModelCardStatus=json_data.get("ModelCardStatus"),
            Content=Content._deserialize(json_data.get("Content")),
            CreationTime=json_data.get("CreationTime"),
            CreatedBy=UserContext._deserialize(json_data.get("CreatedBy")),
            LastModifiedTime=json_data.get("LastModifiedTime"),
            LastModifiedBy=UserContext._deserialize(json_data.get("LastModifiedBy")),
            ModelCardProcessingStatus=json_data.get("ModelCardProcessingStatus"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSagemakerModelcard = AwsSagemakerModelcard


@dataclass
class SecurityConfig(BaseModel):
    KmsKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityConfig"]:
        if not json_data:
            return None
        return cls(
            KmsKeyId=json_data.get("KmsKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecurityConfig = SecurityConfig


@dataclass
class Content(BaseModel):
    ModelOverview: Optional["_ModelOverview"]
    ModelPackageDetails: Optional["_ModelPackageDetails"]
    IntendedUses: Optional["_IntendedUses"]
    BusinessDetails: Optional["_BusinessDetails"]
    TrainingDetails: Optional["_TrainingDetails"]
    EvaluationDetails: Optional[Sequence["_EvaluationDetail"]]
    AdditionalInformation: Optional["_AdditionalInformation"]

    @classmethod
    def _deserialize(
        cls: Type["_Content"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Content"]:
        if not json_data:
            return None
        return cls(
            ModelOverview=ModelOverview._deserialize(json_data.get("ModelOverview")),
            ModelPackageDetails=ModelPackageDetails._deserialize(json_data.get("ModelPackageDetails")),
            IntendedUses=IntendedUses._deserialize(json_data.get("IntendedUses")),
            BusinessDetails=BusinessDetails._deserialize(json_data.get("BusinessDetails")),
            TrainingDetails=TrainingDetails._deserialize(json_data.get("TrainingDetails")),
            EvaluationDetails=deserialize_list(json_data.get("EvaluationDetails"), EvaluationDetail),
            AdditionalInformation=AdditionalInformation._deserialize(json_data.get("AdditionalInformation")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Content = Content


@dataclass
class ModelOverview(BaseModel):
    ModelDescription: Optional[str]
    ModelOwner: Optional[str]
    ModelCreator: Optional[str]
    ProblemType: Optional[str]
    AlgorithmType: Optional[str]
    ModelId: Optional[str]
    ModelArtifact: Optional[Sequence[str]]
    ModelName: Optional[str]
    ModelVersion: Optional[float]
    InferenceEnvironment: Optional["_InferenceEnvironment"]

    @classmethod
    def _deserialize(
        cls: Type["_ModelOverview"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ModelOverview"]:
        if not json_data:
            return None
        return cls(
            ModelDescription=json_data.get("ModelDescription"),
            ModelOwner=json_data.get("ModelOwner"),
            ModelCreator=json_data.get("ModelCreator"),
            ProblemType=json_data.get("ProblemType"),
            AlgorithmType=json_data.get("AlgorithmType"),
            ModelId=json_data.get("ModelId"),
            ModelArtifact=json_data.get("ModelArtifact"),
            ModelName=json_data.get("ModelName"),
            ModelVersion=json_data.get("ModelVersion"),
            InferenceEnvironment=InferenceEnvironment._deserialize(json_data.get("InferenceEnvironment")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ModelOverview = ModelOverview


@dataclass
class InferenceEnvironment(BaseModel):
    ContainerImage: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_InferenceEnvironment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InferenceEnvironment"]:
        if not json_data:
            return None
        return cls(
            ContainerImage=json_data.get("ContainerImage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InferenceEnvironment = InferenceEnvironment


@dataclass
class ModelPackageDetails(BaseModel):
    ModelPackageDescription: Optional[str]
    ModelPackageArn: Optional[str]
    CreatedBy: Optional["_ModelPackageCreator"]
    ModelPackageStatus: Optional[str]
    ModelApprovalStatus: Optional[str]
    ApprovalDescription: Optional[str]
    ModelPackageGroupName: Optional[str]
    ModelPackageName: Optional[str]
    ModelPackageVersion: Optional[float]
    Domain: Optional[str]
    Task: Optional[str]
    SourceAlgorithms: Optional[Sequence["_SourceAlgorithm"]]
    InferenceSpecification: Optional["_InferenceSpecification"]

    @classmethod
    def _deserialize(
        cls: Type["_ModelPackageDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ModelPackageDetails"]:
        if not json_data:
            return None
        return cls(
            ModelPackageDescription=json_data.get("ModelPackageDescription"),
            ModelPackageArn=json_data.get("ModelPackageArn"),
            CreatedBy=ModelPackageCreator._deserialize(json_data.get("CreatedBy")),
            ModelPackageStatus=json_data.get("ModelPackageStatus"),
            ModelApprovalStatus=json_data.get("ModelApprovalStatus"),
            ApprovalDescription=json_data.get("ApprovalDescription"),
            ModelPackageGroupName=json_data.get("ModelPackageGroupName"),
            ModelPackageName=json_data.get("ModelPackageName"),
            ModelPackageVersion=json_data.get("ModelPackageVersion"),
            Domain=json_data.get("Domain"),
            Task=json_data.get("Task"),
            SourceAlgorithms=deserialize_list(json_data.get("SourceAlgorithms"), SourceAlgorithm),
            InferenceSpecification=InferenceSpecification._deserialize(json_data.get("InferenceSpecification")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ModelPackageDetails = ModelPackageDetails


@dataclass
class ModelPackageCreator(BaseModel):
    UserProfileName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ModelPackageCreator"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ModelPackageCreator"]:
        if not json_data:
            return None
        return cls(
            UserProfileName=json_data.get("UserProfileName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ModelPackageCreator = ModelPackageCreator


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
class InferenceSpecification(BaseModel):
    Containers: Optional[Sequence["_Container"]]

    @classmethod
    def _deserialize(
        cls: Type["_InferenceSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InferenceSpecification"]:
        if not json_data:
            return None
        return cls(
            Containers=deserialize_list(json_data.get("Containers"), Container),
        )


# work around possible type aliasing issues when variable has same name as a model
_InferenceSpecification = InferenceSpecification


@dataclass
class Container(BaseModel):
    ModelDataUrl: Optional[str]
    Image: Optional[str]
    NearestModelName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Container"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Container"]:
        if not json_data:
            return None
        return cls(
            ModelDataUrl=json_data.get("ModelDataUrl"),
            Image=json_data.get("Image"),
            NearestModelName=json_data.get("NearestModelName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Container = Container


@dataclass
class IntendedUses(BaseModel):
    PurposeOfModel: Optional[str]
    IntendedUses: Optional[str]
    FactorsAffectingModelEfficiency: Optional[str]
    RiskRating: Optional[str]
    ExplanationsForRiskRating: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IntendedUses"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntendedUses"]:
        if not json_data:
            return None
        return cls(
            PurposeOfModel=json_data.get("PurposeOfModel"),
            IntendedUses=json_data.get("IntendedUses"),
            FactorsAffectingModelEfficiency=json_data.get("FactorsAffectingModelEfficiency"),
            RiskRating=json_data.get("RiskRating"),
            ExplanationsForRiskRating=json_data.get("ExplanationsForRiskRating"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntendedUses = IntendedUses


@dataclass
class BusinessDetails(BaseModel):
    BusinessProblem: Optional[str]
    BusinessStakeholders: Optional[str]
    LineOfBusiness: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BusinessDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BusinessDetails"]:
        if not json_data:
            return None
        return cls(
            BusinessProblem=json_data.get("BusinessProblem"),
            BusinessStakeholders=json_data.get("BusinessStakeholders"),
            LineOfBusiness=json_data.get("LineOfBusiness"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BusinessDetails = BusinessDetails


@dataclass
class TrainingDetails(BaseModel):
    ObjectiveFunction: Optional["_ObjectiveFunction"]
    TrainingObservations: Optional[str]
    TrainingJobDetails: Optional["_TrainingJobDetails"]

    @classmethod
    def _deserialize(
        cls: Type["_TrainingDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrainingDetails"]:
        if not json_data:
            return None
        return cls(
            ObjectiveFunction=ObjectiveFunction._deserialize(json_data.get("ObjectiveFunction")),
            TrainingObservations=json_data.get("TrainingObservations"),
            TrainingJobDetails=TrainingJobDetails._deserialize(json_data.get("TrainingJobDetails")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrainingDetails = TrainingDetails


@dataclass
class ObjectiveFunction(BaseModel):
    Function: Optional["_Function"]
    Notes: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ObjectiveFunction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObjectiveFunction"]:
        if not json_data:
            return None
        return cls(
            Function=Function._deserialize(json_data.get("Function")),
            Notes=json_data.get("Notes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObjectiveFunction = ObjectiveFunction


@dataclass
class Function(BaseModel):
    Function: Optional[str]
    Facet: Optional[str]
    Condition: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Function"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Function"]:
        if not json_data:
            return None
        return cls(
            Function=json_data.get("Function"),
            Facet=json_data.get("Facet"),
            Condition=json_data.get("Condition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Function = Function


@dataclass
class TrainingJobDetails(BaseModel):
    TrainingArn: Optional[str]
    TrainingDatasets: Optional[Sequence[str]]
    TrainingEnvironment: Optional["_TrainingEnvironment"]
    TrainingMetrics: Optional[Sequence["_TrainingMetric"]]
    UserProvidedTrainingMetrics: Optional[Sequence["_TrainingMetric"]]
    HyperParameters: Optional[Sequence["_TrainingHyperParameter"]]
    UserProvidedHyperParameters: Optional[Sequence["_TrainingHyperParameter"]]

    @classmethod
    def _deserialize(
        cls: Type["_TrainingJobDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrainingJobDetails"]:
        if not json_data:
            return None
        return cls(
            TrainingArn=json_data.get("TrainingArn"),
            TrainingDatasets=json_data.get("TrainingDatasets"),
            TrainingEnvironment=TrainingEnvironment._deserialize(json_data.get("TrainingEnvironment")),
            TrainingMetrics=deserialize_list(json_data.get("TrainingMetrics"), TrainingMetric),
            UserProvidedTrainingMetrics=deserialize_list(json_data.get("UserProvidedTrainingMetrics"), TrainingMetric),
            HyperParameters=deserialize_list(json_data.get("HyperParameters"), TrainingHyperParameter),
            UserProvidedHyperParameters=deserialize_list(json_data.get("UserProvidedHyperParameters"), TrainingHyperParameter),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrainingJobDetails = TrainingJobDetails


@dataclass
class TrainingEnvironment(BaseModel):
    ContainerImage: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TrainingEnvironment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrainingEnvironment"]:
        if not json_data:
            return None
        return cls(
            ContainerImage=json_data.get("ContainerImage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrainingEnvironment = TrainingEnvironment


@dataclass
class TrainingMetric(BaseModel):
    Name: Optional[str]
    Notes: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TrainingMetric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrainingMetric"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrainingMetric = TrainingMetric


@dataclass
class TrainingHyperParameter(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrainingHyperParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrainingHyperParameter"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrainingHyperParameter = TrainingHyperParameter


@dataclass
class EvaluationDetail(BaseModel):
    Name: Optional[str]
    EvaluationObservation: Optional[str]
    EvaluationJobArn: Optional[str]
    Datasets: Optional[Sequence[str]]
    Metadata: Optional[MutableMapping[str, str]]
    MetricGroups: Optional[Sequence["_MetricGroup"]]

    @classmethod
    def _deserialize(
        cls: Type["_EvaluationDetail"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EvaluationDetail"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            EvaluationObservation=json_data.get("EvaluationObservation"),
            EvaluationJobArn=json_data.get("EvaluationJobArn"),
            Datasets=json_data.get("Datasets"),
            Metadata=json_data.get("Metadata"),
            MetricGroups=deserialize_list(json_data.get("MetricGroups"), MetricGroup),
        )


# work around possible type aliasing issues when variable has same name as a model
_EvaluationDetail = EvaluationDetail


@dataclass
class MetricGroup(BaseModel):
    Name: Optional[str]
    MetricData: Optional[Sequence[Any]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricGroup"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            MetricData=json_data.get("MetricData"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricGroup = MetricGroup


@dataclass
class SimpleMetric(BaseModel):
    Name: Optional[str]
    Notes: Optional[str]
    Type: Optional[str]
    Value: Optional[Any]
    XAxisName: Optional[str]
    YAxisName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SimpleMetric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SimpleMetric"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
            XAxisName=json_data.get("XAxisName"),
            YAxisName=json_data.get("YAxisName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SimpleMetric = SimpleMetric


@dataclass
class LinearGraphMetric(BaseModel):
    Name: Optional[str]
    Notes: Optional[str]
    Type: Optional[str]
    Value: Optional[Sequence[Sequence[float]]]
    XAxisName: Optional[str]
    YAxisName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LinearGraphMetric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinearGraphMetric"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
            XAxisName=json_data.get("XAxisName"),
            YAxisName=json_data.get("YAxisName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinearGraphMetric = LinearGraphMetric


@dataclass
class BarChartMetric(BaseModel):
    Name: Optional[str]
    Notes: Optional[str]
    Type: Optional[str]
    Value: Optional[Sequence[float]]
    XAxisName: Optional[Sequence[str]]
    YAxisName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BarChartMetric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BarChartMetric"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
            XAxisName=json_data.get("XAxisName"),
            YAxisName=json_data.get("YAxisName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BarChartMetric = BarChartMetric


@dataclass
class MatrixMetric(BaseModel):
    Name: Optional[str]
    Notes: Optional[str]
    Type: Optional[str]
    Value: Optional[Sequence[Sequence[float]]]
    XAxisName: Optional[Sequence[str]]
    YAxisName: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MatrixMetric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatrixMetric"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Notes=json_data.get("Notes"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
            XAxisName=json_data.get("XAxisName"),
            YAxisName=json_data.get("YAxisName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatrixMetric = MatrixMetric


@dataclass
class AdditionalInformation(BaseModel):
    EthicalConsiderations: Optional[str]
    CaveatsAndRecommendations: Optional[str]
    CustomDetails: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalInformation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalInformation"]:
        if not json_data:
            return None
        return cls(
            EthicalConsiderations=json_data.get("EthicalConsiderations"),
            CaveatsAndRecommendations=json_data.get("CaveatsAndRecommendations"),
            CustomDetails=json_data.get("CustomDetails"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalInformation = AdditionalInformation


@dataclass
class UserContext(BaseModel):
    UserProfileArn: Optional[str]
    UserProfileName: Optional[str]
    DomainId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserContext"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserContext"]:
        if not json_data:
            return None
        return cls(
            UserProfileArn=json_data.get("UserProfileArn"),
            UserProfileName=json_data.get("UserProfileName"),
            DomainId=json_data.get("DomainId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserContext = UserContext


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


