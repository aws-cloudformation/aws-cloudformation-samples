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
class AwsEc2Capacityreservationfleet(BaseModel):
    AllocationStrategy: Optional[str]
    TagSpecifications: Optional[Sequence["_TagSpecification"]]
    InstanceTypeSpecifications: Optional[AbstractSet["_InstanceTypeSpecification"]]
    TotalTargetCapacity: Optional[int]
    EndDate: Optional[str]
    InstanceMatchCriteria: Optional[str]
    CapacityReservationFleetId: Optional[str]
    Tenancy: Optional[str]
    RemoveEndDate: Optional[bool]
    NoRemoveEndDate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Capacityreservationfleet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Capacityreservationfleet"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AllocationStrategy=json_data.get("AllocationStrategy"),
            TagSpecifications=deserialize_list(json_data.get("TagSpecifications"), TagSpecification),
            InstanceTypeSpecifications=set_or_none(json_data.get("InstanceTypeSpecifications")),
            TotalTargetCapacity=json_data.get("TotalTargetCapacity"),
            EndDate=json_data.get("EndDate"),
            InstanceMatchCriteria=json_data.get("InstanceMatchCriteria"),
            CapacityReservationFleetId=json_data.get("CapacityReservationFleetId"),
            Tenancy=json_data.get("Tenancy"),
            RemoveEndDate=json_data.get("RemoveEndDate"),
            NoRemoveEndDate=json_data.get("NoRemoveEndDate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Capacityreservationfleet = AwsEc2Capacityreservationfleet


@dataclass
class TagSpecification(BaseModel):
    ResourceType: Optional[str]
    Tags: Optional[Sequence["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_TagSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagSpecification"]:
        if not json_data:
            return None
        return cls(
            ResourceType=json_data.get("ResourceType"),
            Tags=deserialize_list(json_data.get("Tags"), Tag),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagSpecification = TagSpecification


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
class InstanceTypeSpecification(BaseModel):
    InstanceType: Optional[str]
    InstancePlatform: Optional[str]
    Weight: Optional[float]
    AvailabilityZone: Optional[str]
    AvailabilityZoneId: Optional[str]
    EbsOptimized: Optional[bool]
    Priority: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceTypeSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceTypeSpecification"]:
        if not json_data:
            return None
        return cls(
            InstanceType=json_data.get("InstanceType"),
            InstancePlatform=json_data.get("InstancePlatform"),
            Weight=json_data.get("Weight"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            AvailabilityZoneId=json_data.get("AvailabilityZoneId"),
            EbsOptimized=json_data.get("EbsOptimized"),
            Priority=json_data.get("Priority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceTypeSpecification = InstanceTypeSpecification


