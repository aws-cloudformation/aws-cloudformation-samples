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
class AwsCloudwatchMetricstream(BaseModel):
    Arn: Optional[str]
    CreationDate: Optional[str]
    ExcludeFilters: Optional[Sequence["_MetricStreamFilter"]]
    FirehoseArn: Optional[str]
    IncludeFilters: Optional[Sequence["_MetricStreamFilter"]]
    LastUpdateDate: Optional[str]
    Name: Optional[str]
    RoleArn: Optional[str]
    State: Optional[str]
    OutputFormat: Optional[str]
    StatisticsConfigurations: Optional[Sequence["_MetricStreamStatisticsConfiguration"]]
    Tags: Optional[Any]
    IncludeLinkedAccountsMetrics: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudwatchMetricstream"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudwatchMetricstream"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            CreationDate=json_data.get("CreationDate"),
            ExcludeFilters=deserialize_list(json_data.get("ExcludeFilters"), MetricStreamFilter),
            FirehoseArn=json_data.get("FirehoseArn"),
            IncludeFilters=deserialize_list(json_data.get("IncludeFilters"), MetricStreamFilter),
            LastUpdateDate=json_data.get("LastUpdateDate"),
            Name=json_data.get("Name"),
            RoleArn=json_data.get("RoleArn"),
            State=json_data.get("State"),
            OutputFormat=json_data.get("OutputFormat"),
            StatisticsConfigurations=deserialize_list(json_data.get("StatisticsConfigurations"), MetricStreamStatisticsConfiguration),
            Tags=json_data.get("Tags"),
            IncludeLinkedAccountsMetrics=json_data.get("IncludeLinkedAccountsMetrics"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudwatchMetricstream = AwsCloudwatchMetricstream


@dataclass
class MetricStreamFilter(BaseModel):
    Namespace: Optional[str]
    MetricNames: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricStreamFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricStreamFilter"]:
        if not json_data:
            return None
        return cls(
            Namespace=json_data.get("Namespace"),
            MetricNames=json_data.get("MetricNames"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricStreamFilter = MetricStreamFilter


@dataclass
class MetricStreamStatisticsConfiguration(BaseModel):
    AdditionalStatistics: Optional[Sequence[str]]
    IncludeMetrics: Optional[Sequence["_MetricStreamStatisticsMetric"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricStreamStatisticsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricStreamStatisticsConfiguration"]:
        if not json_data:
            return None
        return cls(
            AdditionalStatistics=json_data.get("AdditionalStatistics"),
            IncludeMetrics=deserialize_list(json_data.get("IncludeMetrics"), MetricStreamStatisticsMetric),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricStreamStatisticsConfiguration = MetricStreamStatisticsConfiguration


@dataclass
class MetricStreamStatisticsMetric(BaseModel):
    MetricName: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricStreamStatisticsMetric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricStreamStatisticsMetric"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricStreamStatisticsMetric = MetricStreamStatisticsMetric


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


