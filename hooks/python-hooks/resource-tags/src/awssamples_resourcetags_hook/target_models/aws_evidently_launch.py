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
class AwsEvidentlyLaunch(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    Description: Optional[str]
    RandomizationSalt: Optional[str]
    ScheduledSplitsConfig: Optional[Sequence["_StepConfig"]]
    Groups: Optional[Sequence["_LaunchGroupObject"]]
    MetricMonitors: Optional[Sequence["_MetricDefinitionObject"]]
    Tags: Optional[Any]
    ExecutionStatus: Optional["_ExecutionStatusObject"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEvidentlyLaunch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEvidentlyLaunch"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Description=json_data.get("Description"),
            RandomizationSalt=json_data.get("RandomizationSalt"),
            ScheduledSplitsConfig=deserialize_list(json_data.get("ScheduledSplitsConfig"), StepConfig),
            Groups=deserialize_list(json_data.get("Groups"), LaunchGroupObject),
            MetricMonitors=deserialize_list(json_data.get("MetricMonitors"), MetricDefinitionObject),
            Tags=json_data.get("Tags"),
            ExecutionStatus=ExecutionStatusObject._deserialize(json_data.get("ExecutionStatus")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEvidentlyLaunch = AwsEvidentlyLaunch


@dataclass
class StepConfig(BaseModel):
    StartTime: Optional[str]
    GroupWeights: Optional[AbstractSet["_GroupToWeight"]]
    SegmentOverrides: Optional[AbstractSet["_SegmentOverride"]]

    @classmethod
    def _deserialize(
        cls: Type["_StepConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepConfig"]:
        if not json_data:
            return None
        return cls(
            StartTime=json_data.get("StartTime"),
            GroupWeights=set_or_none(json_data.get("GroupWeights")),
            SegmentOverrides=set_or_none(json_data.get("SegmentOverrides")),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepConfig = StepConfig


@dataclass
class GroupToWeight(BaseModel):
    GroupName: Optional[str]
    SplitWeight: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_GroupToWeight"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupToWeight"]:
        if not json_data:
            return None
        return cls(
            GroupName=json_data.get("GroupName"),
            SplitWeight=json_data.get("SplitWeight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupToWeight = GroupToWeight


@dataclass
class SegmentOverride(BaseModel):
    Segment: Optional[str]
    EvaluationOrder: Optional[int]
    Weights: Optional[AbstractSet["_GroupToWeight"]]

    @classmethod
    def _deserialize(
        cls: Type["_SegmentOverride"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SegmentOverride"]:
        if not json_data:
            return None
        return cls(
            Segment=json_data.get("Segment"),
            EvaluationOrder=json_data.get("EvaluationOrder"),
            Weights=set_or_none(json_data.get("Weights")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SegmentOverride = SegmentOverride


@dataclass
class LaunchGroupObject(BaseModel):
    GroupName: Optional[str]
    Description: Optional[str]
    Feature: Optional[str]
    Variation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchGroupObject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchGroupObject"]:
        if not json_data:
            return None
        return cls(
            GroupName=json_data.get("GroupName"),
            Description=json_data.get("Description"),
            Feature=json_data.get("Feature"),
            Variation=json_data.get("Variation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchGroupObject = LaunchGroupObject


@dataclass
class MetricDefinitionObject(BaseModel):
    MetricName: Optional[str]
    EntityIdKey: Optional[str]
    ValueKey: Optional[str]
    EventPattern: Optional[str]
    UnitLabel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDefinitionObject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDefinitionObject"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            EntityIdKey=json_data.get("EntityIdKey"),
            ValueKey=json_data.get("ValueKey"),
            EventPattern=json_data.get("EventPattern"),
            UnitLabel=json_data.get("UnitLabel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDefinitionObject = MetricDefinitionObject


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
class ExecutionStatusObject(BaseModel):
    Status: Optional[str]
    DesiredState: Optional[str]
    Reason: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExecutionStatusObject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExecutionStatusObject"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            DesiredState=json_data.get("DesiredState"),
            Reason=json_data.get("Reason"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExecutionStatusObject = ExecutionStatusObject


