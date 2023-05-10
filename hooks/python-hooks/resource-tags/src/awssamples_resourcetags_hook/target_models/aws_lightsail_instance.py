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
class AwsLightsailInstance(BaseModel):
    SupportCode: Optional[str]
    ResourceType: Optional[str]
    IsStaticIp: Optional[bool]
    PrivateIpAddress: Optional[str]
    PublicIpAddress: Optional[str]
    Location: Optional["_Location"]
    Hardware: Optional["_Hardware"]
    State: Optional["_State"]
    Networking: Optional["_Networking"]
    UserName: Optional[str]
    SshKeyName: Optional[str]
    InstanceName: Optional[str]
    AvailabilityZone: Optional[str]
    BundleId: Optional[str]
    BlueprintId: Optional[str]
    AddOns: Optional[Sequence["_AddOn"]]
    UserData: Optional[str]
    KeyPairName: Optional[str]
    Tags: Optional[Any]
    InstanceArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLightsailInstance"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLightsailInstance"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            SupportCode=json_data.get("SupportCode"),
            ResourceType=json_data.get("ResourceType"),
            IsStaticIp=json_data.get("IsStaticIp"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            PublicIpAddress=json_data.get("PublicIpAddress"),
            Location=Location._deserialize(json_data.get("Location")),
            Hardware=Hardware._deserialize(json_data.get("Hardware")),
            State=State._deserialize(json_data.get("State")),
            Networking=Networking._deserialize(json_data.get("Networking")),
            UserName=json_data.get("UserName"),
            SshKeyName=json_data.get("SshKeyName"),
            InstanceName=json_data.get("InstanceName"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            BundleId=json_data.get("BundleId"),
            BlueprintId=json_data.get("BlueprintId"),
            AddOns=deserialize_list(json_data.get("AddOns"), AddOn),
            UserData=json_data.get("UserData"),
            KeyPairName=json_data.get("KeyPairName"),
            Tags=json_data.get("Tags"),
            InstanceArn=json_data.get("InstanceArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLightsailInstance = AwsLightsailInstance


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
class Hardware(BaseModel):
    CpuCount: Optional[int]
    RamSizeInGb: Optional[int]
    Disks: Optional[AbstractSet["_Disk"]]

    @classmethod
    def _deserialize(
        cls: Type["_Hardware"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Hardware"]:
        if not json_data:
            return None
        return cls(
            CpuCount=json_data.get("CpuCount"),
            RamSizeInGb=json_data.get("RamSizeInGb"),
            Disks=set_or_none(json_data.get("Disks")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Hardware = Hardware


@dataclass
class Disk(BaseModel):
    DiskName: Optional[str]
    SizeInGb: Optional[str]
    IsSystemDisk: Optional[bool]
    IOPS: Optional[int]
    Path: Optional[str]
    AttachedTo: Optional[str]
    AttachmentState: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Disk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Disk"]:
        if not json_data:
            return None
        return cls(
            DiskName=json_data.get("DiskName"),
            SizeInGb=json_data.get("SizeInGb"),
            IsSystemDisk=json_data.get("IsSystemDisk"),
            IOPS=json_data.get("IOPS"),
            Path=json_data.get("Path"),
            AttachedTo=json_data.get("AttachedTo"),
            AttachmentState=json_data.get("AttachmentState"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Disk = Disk


@dataclass
class State(BaseModel):
    Code: Optional[int]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_State"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_State"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_State = State


@dataclass
class Networking(BaseModel):
    Ports: Optional[AbstractSet["_Port"]]
    MonthlyTransfer: Optional["_MonthlyTransfer"]

    @classmethod
    def _deserialize(
        cls: Type["_Networking"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Networking"]:
        if not json_data:
            return None
        return cls(
            Ports=set_or_none(json_data.get("Ports")),
            MonthlyTransfer=MonthlyTransfer._deserialize(json_data.get("MonthlyTransfer")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Networking = Networking


@dataclass
class Port(BaseModel):
    FromPort: Optional[int]
    ToPort: Optional[int]
    Protocol: Optional[str]
    AccessFrom: Optional[str]
    AccessType: Optional[str]
    CommonName: Optional[str]
    AccessDirection: Optional[str]
    Ipv6Cidrs: Optional[Sequence[str]]
    CidrListAliases: Optional[Sequence[str]]
    Cidrs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Port"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Port"]:
        if not json_data:
            return None
        return cls(
            FromPort=json_data.get("FromPort"),
            ToPort=json_data.get("ToPort"),
            Protocol=json_data.get("Protocol"),
            AccessFrom=json_data.get("AccessFrom"),
            AccessType=json_data.get("AccessType"),
            CommonName=json_data.get("CommonName"),
            AccessDirection=json_data.get("AccessDirection"),
            Ipv6Cidrs=json_data.get("Ipv6Cidrs"),
            CidrListAliases=json_data.get("CidrListAliases"),
            Cidrs=json_data.get("Cidrs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Port = Port


@dataclass
class MonthlyTransfer(BaseModel):
    GbPerMonthAllocated: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MonthlyTransfer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonthlyTransfer"]:
        if not json_data:
            return None
        return cls(
            GbPerMonthAllocated=json_data.get("GbPerMonthAllocated"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonthlyTransfer = MonthlyTransfer


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


