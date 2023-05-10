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
class AwsEvidentlyExperiment(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    Description: Optional[str]
    RunningStatus: Optional["_RunningStatusObject"]
    RandomizationSalt: Optional[str]
    Treatments: Optional[Sequence["_TreatmentObject"]]
    MetricGoals: Optional[Sequence["_MetricGoalObject"]]
    SamplingRate: Optional[int]
    OnlineAbConfig: Optional["_OnlineAbConfigObject"]
    Segment: Optional[str]
    RemoveSegment: Optional[bool]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEvidentlyExperiment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEvidentlyExperiment"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Description=json_data.get("Description"),
            RunningStatus=RunningStatusObject._deserialize(json_data.get("RunningStatus")),
            RandomizationSalt=json_data.get("RandomizationSalt"),
            Treatments=deserialize_list(json_data.get("Treatments"), TreatmentObject),
            MetricGoals=deserialize_list(json_data.get("MetricGoals"), MetricGoalObject),
            SamplingRate=json_data.get("SamplingRate"),
            OnlineAbConfig=OnlineAbConfigObject._deserialize(json_data.get("OnlineAbConfig")),
            Segment=json_data.get("Segment"),
            RemoveSegment=json_data.get("RemoveSegment"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEvidentlyExperiment = AwsEvidentlyExperiment


@dataclass
class RunningStatusObject(BaseModel):
    Status: Optional[str]
    AnalysisCompleteTime: Optional[str]
    Reason: Optional[str]
    DesiredState: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RunningStatusObject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RunningStatusObject"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            AnalysisCompleteTime=json_data.get("AnalysisCompleteTime"),
            Reason=json_data.get("Reason"),
            DesiredState=json_data.get("DesiredState"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RunningStatusObject = RunningStatusObject


@dataclass
class TreatmentObject(BaseModel):
    TreatmentName: Optional[str]
    Description: Optional[str]
    Feature: Optional[str]
    Variation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TreatmentObject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TreatmentObject"]:
        if not json_data:
            return None
        return cls(
            TreatmentName=json_data.get("TreatmentName"),
            Description=json_data.get("Description"),
            Feature=json_data.get("Feature"),
            Variation=json_data.get("Variation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TreatmentObject = TreatmentObject


@dataclass
class MetricGoalObject(BaseModel):
    MetricName: Optional[str]
    EntityIdKey: Optional[str]
    ValueKey: Optional[str]
    EventPattern: Optional[str]
    UnitLabel: Optional[str]
    DesiredChange: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricGoalObject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricGoalObject"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            EntityIdKey=json_data.get("EntityIdKey"),
            ValueKey=json_data.get("ValueKey"),
            EventPattern=json_data.get("EventPattern"),
            UnitLabel=json_data.get("UnitLabel"),
            DesiredChange=json_data.get("DesiredChange"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricGoalObject = MetricGoalObject


@dataclass
class OnlineAbConfigObject(BaseModel):
    ControlTreatmentName: Optional[str]
    TreatmentWeights: Optional[AbstractSet["_TreatmentToWeight"]]

    @classmethod
    def _deserialize(
        cls: Type["_OnlineAbConfigObject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnlineAbConfigObject"]:
        if not json_data:
            return None
        return cls(
            ControlTreatmentName=json_data.get("ControlTreatmentName"),
            TreatmentWeights=set_or_none(json_data.get("TreatmentWeights")),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnlineAbConfigObject = OnlineAbConfigObject


@dataclass
class TreatmentToWeight(BaseModel):
    Treatment: Optional[str]
    SplitWeight: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_TreatmentToWeight"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TreatmentToWeight"]:
        if not json_data:
            return None
        return cls(
            Treatment=json_data.get("Treatment"),
            SplitWeight=json_data.get("SplitWeight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TreatmentToWeight = TreatmentToWeight


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


