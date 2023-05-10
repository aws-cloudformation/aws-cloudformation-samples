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
class AwsEc2Ec2fleet(BaseModel):
    TargetCapacitySpecification: Optional["_TargetCapacitySpecificationRequest"]
    OnDemandOptions: Optional["_OnDemandOptionsRequest"]
    Type: Optional[str]
    ExcessCapacityTerminationPolicy: Optional[str]
    TagSpecifications: Optional[Sequence["_TagSpecification"]]
    SpotOptions: Optional["_SpotOptionsRequest"]
    ValidFrom: Optional[str]
    ReplaceUnhealthyInstances: Optional[bool]
    LaunchTemplateConfigs: Optional[Sequence["_FleetLaunchTemplateConfigRequest"]]
    FleetId: Optional[str]
    TerminateInstancesWithExpiration: Optional[bool]
    ValidUntil: Optional[str]
    Context: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Ec2fleet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Ec2fleet"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            TargetCapacitySpecification=TargetCapacitySpecificationRequest._deserialize(json_data.get("TargetCapacitySpecification")),
            OnDemandOptions=OnDemandOptionsRequest._deserialize(json_data.get("OnDemandOptions")),
            Type=json_data.get("Type"),
            ExcessCapacityTerminationPolicy=json_data.get("ExcessCapacityTerminationPolicy"),
            TagSpecifications=deserialize_list(json_data.get("TagSpecifications"), TagSpecification),
            SpotOptions=SpotOptionsRequest._deserialize(json_data.get("SpotOptions")),
            ValidFrom=json_data.get("ValidFrom"),
            ReplaceUnhealthyInstances=json_data.get("ReplaceUnhealthyInstances"),
            LaunchTemplateConfigs=deserialize_list(json_data.get("LaunchTemplateConfigs"), FleetLaunchTemplateConfigRequest),
            FleetId=json_data.get("FleetId"),
            TerminateInstancesWithExpiration=json_data.get("TerminateInstancesWithExpiration"),
            ValidUntil=json_data.get("ValidUntil"),
            Context=json_data.get("Context"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Ec2fleet = AwsEc2Ec2fleet


@dataclass
class TargetCapacitySpecificationRequest(BaseModel):
    DefaultTargetCapacityType: Optional[str]
    TargetCapacityUnitType: Optional[str]
    TotalTargetCapacity: Optional[int]
    OnDemandTargetCapacity: Optional[int]
    SpotTargetCapacity: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_TargetCapacitySpecificationRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetCapacitySpecificationRequest"]:
        if not json_data:
            return None
        return cls(
            DefaultTargetCapacityType=json_data.get("DefaultTargetCapacityType"),
            TargetCapacityUnitType=json_data.get("TargetCapacityUnitType"),
            TotalTargetCapacity=json_data.get("TotalTargetCapacity"),
            OnDemandTargetCapacity=json_data.get("OnDemandTargetCapacity"),
            SpotTargetCapacity=json_data.get("SpotTargetCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetCapacitySpecificationRequest = TargetCapacitySpecificationRequest


@dataclass
class OnDemandOptionsRequest(BaseModel):
    SingleAvailabilityZone: Optional[bool]
    AllocationStrategy: Optional[str]
    SingleInstanceType: Optional[bool]
    MinTargetCapacity: Optional[int]
    MaxTotalPrice: Optional[str]
    CapacityReservationOptions: Optional["_CapacityReservationOptionsRequest"]

    @classmethod
    def _deserialize(
        cls: Type["_OnDemandOptionsRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnDemandOptionsRequest"]:
        if not json_data:
            return None
        return cls(
            SingleAvailabilityZone=json_data.get("SingleAvailabilityZone"),
            AllocationStrategy=json_data.get("AllocationStrategy"),
            SingleInstanceType=json_data.get("SingleInstanceType"),
            MinTargetCapacity=json_data.get("MinTargetCapacity"),
            MaxTotalPrice=json_data.get("MaxTotalPrice"),
            CapacityReservationOptions=CapacityReservationOptionsRequest._deserialize(json_data.get("CapacityReservationOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnDemandOptionsRequest = OnDemandOptionsRequest


@dataclass
class CapacityReservationOptionsRequest(BaseModel):
    UsageStrategy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityReservationOptionsRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityReservationOptionsRequest"]:
        if not json_data:
            return None
        return cls(
            UsageStrategy=json_data.get("UsageStrategy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityReservationOptionsRequest = CapacityReservationOptionsRequest


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
class SpotOptionsRequest(BaseModel):
    MaintenanceStrategies: Optional["_MaintenanceStrategies"]
    SingleAvailabilityZone: Optional[bool]
    AllocationStrategy: Optional[str]
    SingleInstanceType: Optional[bool]
    MinTargetCapacity: Optional[int]
    MaxTotalPrice: Optional[str]
    InstanceInterruptionBehavior: Optional[str]
    InstancePoolsToUseCount: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_SpotOptionsRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpotOptionsRequest"]:
        if not json_data:
            return None
        return cls(
            MaintenanceStrategies=MaintenanceStrategies._deserialize(json_data.get("MaintenanceStrategies")),
            SingleAvailabilityZone=json_data.get("SingleAvailabilityZone"),
            AllocationStrategy=json_data.get("AllocationStrategy"),
            SingleInstanceType=json_data.get("SingleInstanceType"),
            MinTargetCapacity=json_data.get("MinTargetCapacity"),
            MaxTotalPrice=json_data.get("MaxTotalPrice"),
            InstanceInterruptionBehavior=json_data.get("InstanceInterruptionBehavior"),
            InstancePoolsToUseCount=json_data.get("InstancePoolsToUseCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpotOptionsRequest = SpotOptionsRequest


@dataclass
class MaintenanceStrategies(BaseModel):
    CapacityRebalance: Optional["_CapacityRebalance"]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceStrategies"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceStrategies"]:
        if not json_data:
            return None
        return cls(
            CapacityRebalance=CapacityRebalance._deserialize(json_data.get("CapacityRebalance")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceStrategies = MaintenanceStrategies


@dataclass
class CapacityRebalance(BaseModel):
    ReplacementStrategy: Optional[str]
    TerminationDelay: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityRebalance"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityRebalance"]:
        if not json_data:
            return None
        return cls(
            ReplacementStrategy=json_data.get("ReplacementStrategy"),
            TerminationDelay=json_data.get("TerminationDelay"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityRebalance = CapacityRebalance


@dataclass
class FleetLaunchTemplateConfigRequest(BaseModel):
    LaunchTemplateSpecification: Optional["_FleetLaunchTemplateSpecificationRequest"]
    Overrides: Optional[Sequence["_FleetLaunchTemplateOverridesRequest"]]

    @classmethod
    def _deserialize(
        cls: Type["_FleetLaunchTemplateConfigRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FleetLaunchTemplateConfigRequest"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateSpecification=FleetLaunchTemplateSpecificationRequest._deserialize(json_data.get("LaunchTemplateSpecification")),
            Overrides=deserialize_list(json_data.get("Overrides"), FleetLaunchTemplateOverridesRequest),
        )


# work around possible type aliasing issues when variable has same name as a model
_FleetLaunchTemplateConfigRequest = FleetLaunchTemplateConfigRequest


@dataclass
class FleetLaunchTemplateSpecificationRequest(BaseModel):
    LaunchTemplateName: Optional[str]
    LaunchTemplateId: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FleetLaunchTemplateSpecificationRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FleetLaunchTemplateSpecificationRequest"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateName=json_data.get("LaunchTemplateName"),
            LaunchTemplateId=json_data.get("LaunchTemplateId"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FleetLaunchTemplateSpecificationRequest = FleetLaunchTemplateSpecificationRequest


@dataclass
class FleetLaunchTemplateOverridesRequest(BaseModel):
    WeightedCapacity: Optional[float]
    Placement: Optional["_Placement"]
    Priority: Optional[float]
    AvailabilityZone: Optional[str]
    SubnetId: Optional[str]
    InstanceType: Optional[str]
    InstanceRequirements: Optional["_InstanceRequirementsRequest"]
    MaxPrice: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FleetLaunchTemplateOverridesRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FleetLaunchTemplateOverridesRequest"]:
        if not json_data:
            return None
        return cls(
            WeightedCapacity=json_data.get("WeightedCapacity"),
            Placement=Placement._deserialize(json_data.get("Placement")),
            Priority=json_data.get("Priority"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            SubnetId=json_data.get("SubnetId"),
            InstanceType=json_data.get("InstanceType"),
            InstanceRequirements=InstanceRequirementsRequest._deserialize(json_data.get("InstanceRequirements")),
            MaxPrice=json_data.get("MaxPrice"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FleetLaunchTemplateOverridesRequest = FleetLaunchTemplateOverridesRequest


@dataclass
class Placement(BaseModel):
    GroupName: Optional[str]
    Tenancy: Optional[str]
    SpreadDomain: Optional[str]
    PartitionNumber: Optional[int]
    AvailabilityZone: Optional[str]
    Affinity: Optional[str]
    HostId: Optional[str]
    HostResourceGroupArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Placement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Placement"]:
        if not json_data:
            return None
        return cls(
            GroupName=json_data.get("GroupName"),
            Tenancy=json_data.get("Tenancy"),
            SpreadDomain=json_data.get("SpreadDomain"),
            PartitionNumber=json_data.get("PartitionNumber"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Affinity=json_data.get("Affinity"),
            HostId=json_data.get("HostId"),
            HostResourceGroupArn=json_data.get("HostResourceGroupArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Placement = Placement


@dataclass
class InstanceRequirementsRequest(BaseModel):
    VCpuCount: Optional["_VCpuCountRangeRequest"]
    MemoryMiB: Optional["_MemoryMiBRequest"]
    CpuManufacturers: Optional[Sequence[str]]
    MemoryGiBPerVCpu: Optional["_MemoryGiBPerVCpuRequest"]
    AllowedInstanceTypes: Optional[Sequence[str]]
    ExcludedInstanceTypes: Optional[Sequence[str]]
    InstanceGenerations: Optional[Sequence[str]]
    SpotMaxPricePercentageOverLowestPrice: Optional[int]
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int]
    BareMetal: Optional[str]
    BurstablePerformance: Optional[str]
    RequireHibernateSupport: Optional[bool]
    NetworkBandwidthGbps: Optional["_NetworkBandwidthGbpsRequest"]
    NetworkInterfaceCount: Optional["_NetworkInterfaceCountRequest"]
    LocalStorage: Optional[str]
    LocalStorageTypes: Optional[Sequence[str]]
    TotalLocalStorageGB: Optional["_TotalLocalStorageGBRequest"]
    BaselineEbsBandwidthMbps: Optional["_BaselineEbsBandwidthMbpsRequest"]
    AcceleratorTypes: Optional[Sequence[str]]
    AcceleratorCount: Optional["_AcceleratorCountRequest"]
    AcceleratorManufacturers: Optional[Sequence[str]]
    AcceleratorNames: Optional[Sequence[str]]
    AcceleratorTotalMemoryMiB: Optional["_AcceleratorTotalMemoryMiBRequest"]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceRequirementsRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceRequirementsRequest"]:
        if not json_data:
            return None
        return cls(
            VCpuCount=VCpuCountRangeRequest._deserialize(json_data.get("VCpuCount")),
            MemoryMiB=MemoryMiBRequest._deserialize(json_data.get("MemoryMiB")),
            CpuManufacturers=json_data.get("CpuManufacturers"),
            MemoryGiBPerVCpu=MemoryGiBPerVCpuRequest._deserialize(json_data.get("MemoryGiBPerVCpu")),
            AllowedInstanceTypes=json_data.get("AllowedInstanceTypes"),
            ExcludedInstanceTypes=json_data.get("ExcludedInstanceTypes"),
            InstanceGenerations=json_data.get("InstanceGenerations"),
            SpotMaxPricePercentageOverLowestPrice=json_data.get("SpotMaxPricePercentageOverLowestPrice"),
            OnDemandMaxPricePercentageOverLowestPrice=json_data.get("OnDemandMaxPricePercentageOverLowestPrice"),
            BareMetal=json_data.get("BareMetal"),
            BurstablePerformance=json_data.get("BurstablePerformance"),
            RequireHibernateSupport=json_data.get("RequireHibernateSupport"),
            NetworkBandwidthGbps=NetworkBandwidthGbpsRequest._deserialize(json_data.get("NetworkBandwidthGbps")),
            NetworkInterfaceCount=NetworkInterfaceCountRequest._deserialize(json_data.get("NetworkInterfaceCount")),
            LocalStorage=json_data.get("LocalStorage"),
            LocalStorageTypes=json_data.get("LocalStorageTypes"),
            TotalLocalStorageGB=TotalLocalStorageGBRequest._deserialize(json_data.get("TotalLocalStorageGB")),
            BaselineEbsBandwidthMbps=BaselineEbsBandwidthMbpsRequest._deserialize(json_data.get("BaselineEbsBandwidthMbps")),
            AcceleratorTypes=json_data.get("AcceleratorTypes"),
            AcceleratorCount=AcceleratorCountRequest._deserialize(json_data.get("AcceleratorCount")),
            AcceleratorManufacturers=json_data.get("AcceleratorManufacturers"),
            AcceleratorNames=json_data.get("AcceleratorNames"),
            AcceleratorTotalMemoryMiB=AcceleratorTotalMemoryMiBRequest._deserialize(json_data.get("AcceleratorTotalMemoryMiB")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceRequirementsRequest = InstanceRequirementsRequest


@dataclass
class VCpuCountRangeRequest(BaseModel):
    Min: Optional[int]
    Max: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_VCpuCountRangeRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VCpuCountRangeRequest"]:
        if not json_data:
            return None
        return cls(
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VCpuCountRangeRequest = VCpuCountRangeRequest


@dataclass
class MemoryMiBRequest(BaseModel):
    Min: Optional[int]
    Max: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_MemoryMiBRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemoryMiBRequest"]:
        if not json_data:
            return None
        return cls(
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemoryMiBRequest = MemoryMiBRequest


@dataclass
class MemoryGiBPerVCpuRequest(BaseModel):
    Min: Optional[float]
    Max: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MemoryGiBPerVCpuRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemoryGiBPerVCpuRequest"]:
        if not json_data:
            return None
        return cls(
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemoryGiBPerVCpuRequest = MemoryGiBPerVCpuRequest


@dataclass
class NetworkBandwidthGbpsRequest(BaseModel):
    Min: Optional[float]
    Max: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkBandwidthGbpsRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkBandwidthGbpsRequest"]:
        if not json_data:
            return None
        return cls(
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkBandwidthGbpsRequest = NetworkBandwidthGbpsRequest


@dataclass
class NetworkInterfaceCountRequest(BaseModel):
    Min: Optional[int]
    Max: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterfaceCountRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterfaceCountRequest"]:
        if not json_data:
            return None
        return cls(
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterfaceCountRequest = NetworkInterfaceCountRequest


@dataclass
class TotalLocalStorageGBRequest(BaseModel):
    Min: Optional[float]
    Max: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TotalLocalStorageGBRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TotalLocalStorageGBRequest"]:
        if not json_data:
            return None
        return cls(
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TotalLocalStorageGBRequest = TotalLocalStorageGBRequest


@dataclass
class BaselineEbsBandwidthMbpsRequest(BaseModel):
    Min: Optional[int]
    Max: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_BaselineEbsBandwidthMbpsRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BaselineEbsBandwidthMbpsRequest"]:
        if not json_data:
            return None
        return cls(
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BaselineEbsBandwidthMbpsRequest = BaselineEbsBandwidthMbpsRequest


@dataclass
class AcceleratorCountRequest(BaseModel):
    Min: Optional[int]
    Max: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AcceleratorCountRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AcceleratorCountRequest"]:
        if not json_data:
            return None
        return cls(
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AcceleratorCountRequest = AcceleratorCountRequest


@dataclass
class AcceleratorTotalMemoryMiBRequest(BaseModel):
    Min: Optional[int]
    Max: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AcceleratorTotalMemoryMiBRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AcceleratorTotalMemoryMiBRequest"]:
        if not json_data:
            return None
        return cls(
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AcceleratorTotalMemoryMiBRequest = AcceleratorTotalMemoryMiBRequest


