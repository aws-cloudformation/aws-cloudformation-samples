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
class AwsLightsailDisk(BaseModel):
    DiskName: Optional[str]
    DiskArn: Optional[str]
    SupportCode: Optional[str]
    AvailabilityZone: Optional[str]
    Location: Optional["_Location"]
    ResourceType: Optional[str]
    Tags: Optional[Any]
    AddOns: Optional[Sequence["_AddOn"]]
    State: Optional[str]
    AttachmentState: Optional[str]
    SizeInGb: Optional[int]
    Iops: Optional[int]
    IsAttached: Optional[bool]
    Path: Optional[str]
    AttachedTo: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLightsailDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLightsailDisk"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DiskName=json_data.get("DiskName"),
            DiskArn=json_data.get("DiskArn"),
            SupportCode=json_data.get("SupportCode"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Location=Location._deserialize(json_data.get("Location")),
            ResourceType=json_data.get("ResourceType"),
            Tags=json_data.get("Tags"),
            AddOns=deserialize_list(json_data.get("AddOns"), AddOn),
            State=json_data.get("State"),
            AttachmentState=json_data.get("AttachmentState"),
            SizeInGb=json_data.get("SizeInGb"),
            Iops=json_data.get("Iops"),
            IsAttached=json_data.get("IsAttached"),
            Path=json_data.get("Path"),
            AttachedTo=json_data.get("AttachedTo"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLightsailDisk = AwsLightsailDisk


@dataclass
class Location(BaseModel):
    AvailabilityZone: Optional[str]
    RegionName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Location"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Location"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZone=json_data.get("AvailabilityZone"),
            RegionName=json_data.get("RegionName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Location = Location


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
class AddOn(BaseModel):
    AddOnType: Optional[str]
    Status: Optional[str]
    AutoSnapshotAddOnRequest: Optional["_AutoSnapshotAddOn"]

    @classmethod
    def _deserialize(
        cls: Type["_AddOn"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddOn"]:
        if not json_data:
            return None
        return cls(
            AddOnType=json_data.get("AddOnType"),
            Status=json_data.get("Status"),
            AutoSnapshotAddOnRequest=AutoSnapshotAddOn._deserialize(json_data.get("AutoSnapshotAddOnRequest")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddOn = AddOn


@dataclass
class AutoSnapshotAddOn(BaseModel):
    SnapshotTimeOfDay: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutoSnapshotAddOn"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoSnapshotAddOn"]:
        if not json_data:
            return None
        return cls(
            SnapshotTimeOfDay=json_data.get("SnapshotTimeOfDay"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoSnapshotAddOn = AutoSnapshotAddOn


