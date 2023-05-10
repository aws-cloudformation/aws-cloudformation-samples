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
class AwsInternetmonitorMonitor(BaseModel):
    CreatedAt: Optional[str]
    ModifiedAt: Optional[str]
    MonitorArn: Optional[str]
    MonitorName: Optional[str]
    ProcessingStatus: Optional[str]
    ProcessingStatusInfo: Optional[str]
    Resources: Optional[Sequence[str]]
    ResourcesToAdd: Optional[Sequence[str]]
    ResourcesToRemove: Optional[Sequence[str]]
    Status: Optional[str]
    Tags: Optional[Any]
    MaxCityNetworksToMonitor: Optional[int]
    TrafficPercentageToMonitor: Optional[int]
    InternetMeasurementsLogDelivery: Optional["_InternetMeasurementsLogDelivery"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsInternetmonitorMonitor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsInternetmonitorMonitor"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CreatedAt=json_data.get("CreatedAt"),
            ModifiedAt=json_data.get("ModifiedAt"),
            MonitorArn=json_data.get("MonitorArn"),
            MonitorName=json_data.get("MonitorName"),
            ProcessingStatus=json_data.get("ProcessingStatus"),
            ProcessingStatusInfo=json_data.get("ProcessingStatusInfo"),
            Resources=json_data.get("Resources"),
            ResourcesToAdd=json_data.get("ResourcesToAdd"),
            ResourcesToRemove=json_data.get("ResourcesToRemove"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            MaxCityNetworksToMonitor=json_data.get("MaxCityNetworksToMonitor"),
            TrafficPercentageToMonitor=json_data.get("TrafficPercentageToMonitor"),
            InternetMeasurementsLogDelivery=InternetMeasurementsLogDelivery._deserialize(json_data.get("InternetMeasurementsLogDelivery")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsInternetmonitorMonitor = AwsInternetmonitorMonitor


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
class InternetMeasurementsLogDelivery(BaseModel):
    S3Config: Optional["_S3Config"]

    @classmethod
    def _deserialize(
        cls: Type["_InternetMeasurementsLogDelivery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InternetMeasurementsLogDelivery"]:
        if not json_data:
            return None
        return cls(
            S3Config=S3Config._deserialize(json_data.get("S3Config")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InternetMeasurementsLogDelivery = InternetMeasurementsLogDelivery


@dataclass
class S3Config(BaseModel):
    BucketName: Optional[str]
    BucketPrefix: Optional[str]
    LogDeliveryStatus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Config"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Config"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            BucketPrefix=json_data.get("BucketPrefix"),
            LogDeliveryStatus=json_data.get("LogDeliveryStatus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Config = S3Config


