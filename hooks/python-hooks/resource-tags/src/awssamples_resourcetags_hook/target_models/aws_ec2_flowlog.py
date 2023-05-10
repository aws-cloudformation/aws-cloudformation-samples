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
class AwsEc2Flowlog(BaseModel):
    Id: Optional[str]
    DeliverLogsPermissionArn: Optional[str]
    LogDestination: Optional[str]
    LogDestinationType: Optional[str]
    LogFormat: Optional[str]
    LogGroupName: Optional[str]
    MaxAggregationInterval: Optional[int]
    ResourceId: Optional[str]
    ResourceType: Optional[str]
    Tags: Optional[Any]
    TrafficType: Optional[str]
    DestinationOptions: Optional["_DestinationOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Flowlog"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Flowlog"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            DeliverLogsPermissionArn=json_data.get("DeliverLogsPermissionArn"),
            LogDestination=json_data.get("LogDestination"),
            LogDestinationType=json_data.get("LogDestinationType"),
            LogFormat=json_data.get("LogFormat"),
            LogGroupName=json_data.get("LogGroupName"),
            MaxAggregationInterval=json_data.get("MaxAggregationInterval"),
            ResourceId=json_data.get("ResourceId"),
            ResourceType=json_data.get("ResourceType"),
            Tags=json_data.get("Tags"),
            TrafficType=json_data.get("TrafficType"),
            DestinationOptions=DestinationOptions._deserialize(json_data.get("DestinationOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Flowlog = AwsEc2Flowlog


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


@dataclass
class DestinationOptions(BaseModel):
    FileFormat: Optional[str]
    HiveCompatiblePartitions: Optional[bool]
    PerHourPartition: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationOptions"]:
        if not json_data:
            return None
        return cls(
            FileFormat=json_data.get("FileFormat"),
            HiveCompatiblePartitions=json_data.get("HiveCompatiblePartitions"),
            PerHourPartition=json_data.get("PerHourPartition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationOptions = DestinationOptions


