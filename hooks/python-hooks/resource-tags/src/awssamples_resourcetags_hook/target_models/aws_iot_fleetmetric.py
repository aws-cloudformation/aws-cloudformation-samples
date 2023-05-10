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
class AwsIotFleetmetric(BaseModel):
    MetricName: Optional[str]
    Description: Optional[str]
    QueryString: Optional[str]
    Period: Optional[int]
    AggregationField: Optional[str]
    QueryVersion: Optional[str]
    IndexName: Optional[str]
    Unit: Optional[str]
    AggregationType: Optional["_AggregationType"]
    MetricArn: Optional[str]
    CreationDate: Optional[float]
    LastModifiedDate: Optional[float]
    Version: Optional[float]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotFleetmetric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotFleetmetric"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            MetricName=json_data.get("MetricName"),
            Description=json_data.get("Description"),
            QueryString=json_data.get("QueryString"),
            Period=json_data.get("Period"),
            AggregationField=json_data.get("AggregationField"),
            QueryVersion=json_data.get("QueryVersion"),
            IndexName=json_data.get("IndexName"),
            Unit=json_data.get("Unit"),
            AggregationType=AggregationType._deserialize(json_data.get("AggregationType")),
            MetricArn=json_data.get("MetricArn"),
            CreationDate=json_data.get("CreationDate"),
            LastModifiedDate=json_data.get("LastModifiedDate"),
            Version=json_data.get("Version"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotFleetmetric = AwsIotFleetmetric


@dataclass
class AggregationType(BaseModel):
    Name: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AggregationType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AggregationType"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AggregationType = AggregationType


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


