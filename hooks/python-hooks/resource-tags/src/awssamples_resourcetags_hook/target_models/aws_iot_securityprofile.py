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
class AwsIotSecurityprofile(BaseModel):
    SecurityProfileName: Optional[str]
    SecurityProfileDescription: Optional[str]
    Behaviors: Optional[AbstractSet["_Behavior"]]
    AlertTargets: Optional[MutableMapping[str, "_AlertTarget"]]
    AdditionalMetricsToRetainV2: Optional[AbstractSet["_MetricToRetain"]]
    Tags: Optional[Any]
    TargetArns: Optional[AbstractSet[str]]
    SecurityProfileArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotSecurityprofile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotSecurityprofile"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            SecurityProfileName=json_data.get("SecurityProfileName"),
            SecurityProfileDescription=json_data.get("SecurityProfileDescription"),
            Behaviors=set_or_none(json_data.get("Behaviors")),
            AlertTargets=json_data.get("AlertTargets"),
            AdditionalMetricsToRetainV2=set_or_none(json_data.get("AdditionalMetricsToRetainV2")),
            Tags=json_data.get("Tags"),
            TargetArns=set_or_none(json_data.get("TargetArns")),
            SecurityProfileArn=json_data.get("SecurityProfileArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotSecurityprofile = AwsIotSecurityprofile


@dataclass
class Behavior(BaseModel):
    Name: Optional[str]
    Metric: Optional[str]
    MetricDimension: Optional["_MetricDimension"]
    Criteria: Optional["_BehaviorCriteria"]
    SuppressAlerts: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Behavior"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Behavior"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Metric=json_data.get("Metric"),
            MetricDimension=MetricDimension._deserialize(json_data.get("MetricDimension")),
            Criteria=BehaviorCriteria._deserialize(json_data.get("Criteria")),
            SuppressAlerts=json_data.get("SuppressAlerts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Behavior = Behavior


@dataclass
class MetricDimension(BaseModel):
    DimensionName: Optional[str]
    Operator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDimension"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDimension"]:
        if not json_data:
            return None
        return cls(
            DimensionName=json_data.get("DimensionName"),
            Operator=json_data.get("Operator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDimension = MetricDimension


@dataclass
class BehaviorCriteria(BaseModel):
    ComparisonOperator: Optional[str]
    Value: Optional["_MetricValue"]
    DurationSeconds: Optional[int]
    ConsecutiveDatapointsToAlarm: Optional[int]
    ConsecutiveDatapointsToClear: Optional[int]
    StatisticalThreshold: Optional["_StatisticalThreshold"]
    MlDetectionConfig: Optional["_MachineLearningDetectionConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_BehaviorCriteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BehaviorCriteria"]:
        if not json_data:
            return None
        return cls(
            ComparisonOperator=json_data.get("ComparisonOperator"),
            Value=MetricValue._deserialize(json_data.get("Value")),
            DurationSeconds=json_data.get("DurationSeconds"),
            ConsecutiveDatapointsToAlarm=json_data.get("ConsecutiveDatapointsToAlarm"),
            ConsecutiveDatapointsToClear=json_data.get("ConsecutiveDatapointsToClear"),
            StatisticalThreshold=StatisticalThreshold._deserialize(json_data.get("StatisticalThreshold")),
            MlDetectionConfig=MachineLearningDetectionConfig._deserialize(json_data.get("MlDetectionConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BehaviorCriteria = BehaviorCriteria


@dataclass
class MetricValue(BaseModel):
    Count: Optional[str]
    Cidrs: Optional[AbstractSet[str]]
    Ports: Optional[AbstractSet[int]]
    Number: Optional[float]
    Numbers: Optional[AbstractSet[float]]
    Strings: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricValue"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Cidrs=set_or_none(json_data.get("Cidrs")),
            Ports=set_or_none(json_data.get("Ports")),
            Number=json_data.get("Number"),
            Numbers=set_or_none(json_data.get("Numbers")),
            Strings=set_or_none(json_data.get("Strings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricValue = MetricValue


@dataclass
class StatisticalThreshold(BaseModel):
    Statistic: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatisticalThreshold"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatisticalThreshold"]:
        if not json_data:
            return None
        return cls(
            Statistic=json_data.get("Statistic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatisticalThreshold = StatisticalThreshold


@dataclass
class MachineLearningDetectionConfig(BaseModel):
    ConfidenceLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MachineLearningDetectionConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MachineLearningDetectionConfig"]:
        if not json_data:
            return None
        return cls(
            ConfidenceLevel=json_data.get("ConfidenceLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MachineLearningDetectionConfig = MachineLearningDetectionConfig


@dataclass
class AlertTarget(BaseModel):
    AlertTargetArn: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AlertTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlertTarget"]:
        if not json_data:
            return None
        return cls(
            AlertTargetArn=json_data.get("AlertTargetArn"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlertTarget = AlertTarget


@dataclass
class MetricToRetain(BaseModel):
    Metric: Optional[str]
    MetricDimension: Optional["_MetricDimension"]

    @classmethod
    def _deserialize(
        cls: Type["_MetricToRetain"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricToRetain"]:
        if not json_data:
            return None
        return cls(
            Metric=json_data.get("Metric"),
            MetricDimension=MetricDimension._deserialize(json_data.get("MetricDimension")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricToRetain = MetricToRetain


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


