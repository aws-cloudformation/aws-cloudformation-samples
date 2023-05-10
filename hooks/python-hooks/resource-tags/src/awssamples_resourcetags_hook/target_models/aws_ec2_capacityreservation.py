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
class AwsEc2Capacityreservation(BaseModel):
    Tenancy: Optional[str]
    EndDateType: Optional[str]
    TagSpecifications: Optional[Sequence["_TagSpecification"]]
    AvailabilityZone: Optional[str]
    TotalInstanceCount: Optional[int]
    EndDate: Optional[str]
    EbsOptimized: Optional[bool]
    OutPostArn: Optional[str]
    InstanceCount: Optional[int]
    PlacementGroupArn: Optional[str]
    AvailableInstanceCount: Optional[int]
    InstancePlatform: Optional[str]
    Id: Optional[str]
    InstanceType: Optional[str]
    EphemeralStorage: Optional[bool]
    InstanceMatchCriteria: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Capacityreservation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Capacityreservation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Tenancy=json_data.get("Tenancy"),
            EndDateType=json_data.get("EndDateType"),
            TagSpecifications=deserialize_list(json_data.get("TagSpecifications"), TagSpecification),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            TotalInstanceCount=json_data.get("TotalInstanceCount"),
            EndDate=json_data.get("EndDate"),
            EbsOptimized=json_data.get("EbsOptimized"),
            OutPostArn=json_data.get("OutPostArn"),
            InstanceCount=json_data.get("InstanceCount"),
            PlacementGroupArn=json_data.get("PlacementGroupArn"),
            AvailableInstanceCount=json_data.get("AvailableInstanceCount"),
            InstancePlatform=json_data.get("InstancePlatform"),
            Id=json_data.get("Id"),
            InstanceType=json_data.get("InstanceType"),
            EphemeralStorage=json_data.get("EphemeralStorage"),
            InstanceMatchCriteria=json_data.get("InstanceMatchCriteria"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Capacityreservation = AwsEc2Capacityreservation


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


