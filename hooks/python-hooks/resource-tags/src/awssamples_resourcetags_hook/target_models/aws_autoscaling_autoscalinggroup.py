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
class AwsAutoscalingAutoscalinggroup(BaseModel):
    LifecycleHookSpecificationList: Optional[Sequence["_LifecycleHookSpecification"]]
    LoadBalancerNames: Optional[Sequence[str]]
    LaunchConfigurationName: Optional[str]
    ServiceLinkedRoleARN: Optional[str]
    TargetGroupARNs: Optional[Sequence[str]]
    Cooldown: Optional[str]
    NotificationConfigurations: Optional[Sequence["_NotificationConfiguration"]]
    DesiredCapacity: Optional[str]
    HealthCheckGracePeriod: Optional[int]
    DefaultInstanceWarmup: Optional[int]
    NewInstancesProtectedFromScaleIn: Optional[bool]
    LaunchTemplate: Optional["_LaunchTemplateSpecification"]
    MixedInstancesPolicy: Optional["_MixedInstancesPolicy"]
    VPCZoneIdentifier: Optional[Sequence[str]]
    Tags: Optional[Any]
    Context: Optional[str]
    CapacityRebalance: Optional[bool]
    InstanceId: Optional[str]
    AvailabilityZones: Optional[Sequence[str]]
    NotificationConfiguration: Optional["_NotificationConfiguration"]
    MetricsCollection: Optional[Sequence["_MetricsCollection"]]
    InstanceMaintenancePolicy: Optional["_InstanceMaintenancePolicy"]
    MaxSize: Optional[str]
    MinSize: Optional[str]
    TerminationPolicies: Optional[Sequence[str]]
    AutoScalingGroupName: Optional[str]
    DesiredCapacityType: Optional[str]
    PlacementGroup: Optional[str]
    HealthCheckType: Optional[str]
    MaxInstanceLifetime: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAutoscalingAutoscalinggroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAutoscalingAutoscalinggroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            LifecycleHookSpecificationList=deserialize_list(json_data.get("LifecycleHookSpecificationList"), LifecycleHookSpecification),
            LoadBalancerNames=json_data.get("LoadBalancerNames"),
            LaunchConfigurationName=json_data.get("LaunchConfigurationName"),
            ServiceLinkedRoleARN=json_data.get("ServiceLinkedRoleARN"),
            TargetGroupARNs=json_data.get("TargetGroupARNs"),
            Cooldown=json_data.get("Cooldown"),
            NotificationConfigurations=deserialize_list(json_data.get("NotificationConfigurations"), NotificationConfiguration),
            DesiredCapacity=json_data.get("DesiredCapacity"),
            HealthCheckGracePeriod=json_data.get("HealthCheckGracePeriod"),
            DefaultInstanceWarmup=json_data.get("DefaultInstanceWarmup"),
            NewInstancesProtectedFromScaleIn=json_data.get("NewInstancesProtectedFromScaleIn"),
            LaunchTemplate=LaunchTemplateSpecification._deserialize(json_data.get("LaunchTemplate")),
            MixedInstancesPolicy=MixedInstancesPolicy._deserialize(json_data.get("MixedInstancesPolicy")),
            VPCZoneIdentifier=json_data.get("VPCZoneIdentifier"),
            Tags=json_data.get("Tags"),
            Context=json_data.get("Context"),
            CapacityRebalance=json_data.get("CapacityRebalance"),
            InstanceId=json_data.get("InstanceId"),
            AvailabilityZones=json_data.get("AvailabilityZones"),
            NotificationConfiguration=NotificationConfiguration._deserialize(json_data.get("NotificationConfiguration")),
            MetricsCollection=deserialize_list(json_data.get("MetricsCollection"), MetricsCollection),
            InstanceMaintenancePolicy=InstanceMaintenancePolicy._deserialize(json_data.get("InstanceMaintenancePolicy")),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            TerminationPolicies=json_data.get("TerminationPolicies"),
            AutoScalingGroupName=json_data.get("AutoScalingGroupName"),
            DesiredCapacityType=json_data.get("DesiredCapacityType"),
            PlacementGroup=json_data.get("PlacementGroup"),
            HealthCheckType=json_data.get("HealthCheckType"),
            MaxInstanceLifetime=json_data.get("MaxInstanceLifetime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAutoscalingAutoscalinggroup = AwsAutoscalingAutoscalinggroup


@dataclass
class LifecycleHookSpecification(BaseModel):
    LifecycleHookName: Optional[str]
    LifecycleTransition: Optional[str]
    HeartbeatTimeout: Optional[int]
    NotificationMetadata: Optional[str]
    DefaultResult: Optional[str]
    NotificationTargetARN: Optional[str]
    RoleARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LifecycleHookSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecycleHookSpecification"]:
        if not json_data:
            return None
        return cls(
            LifecycleHookName=json_data.get("LifecycleHookName"),
            LifecycleTransition=json_data.get("LifecycleTransition"),
            HeartbeatTimeout=json_data.get("HeartbeatTimeout"),
            NotificationMetadata=json_data.get("NotificationMetadata"),
            DefaultResult=json_data.get("DefaultResult"),
            NotificationTargetARN=json_data.get("NotificationTargetARN"),
            RoleARN=json_data.get("RoleARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecycleHookSpecification = LifecycleHookSpecification


@dataclass
class NotificationConfiguration(BaseModel):
    TopicARN: Optional[Any]
    NotificationTypes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationConfiguration"]:
        if not json_data:
            return None
        return cls(
            TopicARN=json_data.get("TopicARN"),
            NotificationTypes=json_data.get("NotificationTypes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationConfiguration = NotificationConfiguration


@dataclass
class LaunchTemplateSpecification(BaseModel):
    LaunchTemplateName: Optional[str]
    Version: Optional[str]
    LaunchTemplateId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateSpecification"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateName=json_data.get("LaunchTemplateName"),
            Version=json_data.get("Version"),
            LaunchTemplateId=json_data.get("LaunchTemplateId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateSpecification = LaunchTemplateSpecification


@dataclass
class MixedInstancesPolicy(BaseModel):
    InstancesDistribution: Optional["_InstancesDistribution"]
    LaunchTemplate: Optional["_LaunchTemplate"]

    @classmethod
    def _deserialize(
        cls: Type["_MixedInstancesPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MixedInstancesPolicy"]:
        if not json_data:
            return None
        return cls(
            InstancesDistribution=InstancesDistribution._deserialize(json_data.get("InstancesDistribution")),
            LaunchTemplate=LaunchTemplate._deserialize(json_data.get("LaunchTemplate")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MixedInstancesPolicy = MixedInstancesPolicy


@dataclass
class InstancesDistribution(BaseModel):
    OnDemandAllocationStrategy: Optional[str]
    OnDemandBaseCapacity: Optional[int]
    OnDemandPercentageAboveBaseCapacity: Optional[int]
    SpotInstancePools: Optional[int]
    SpotAllocationStrategy: Optional[str]
    SpotMaxPrice: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstancesDistribution"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstancesDistribution"]:
        if not json_data:
            return None
        return cls(
            OnDemandAllocationStrategy=json_data.get("OnDemandAllocationStrategy"),
            OnDemandBaseCapacity=json_data.get("OnDemandBaseCapacity"),
            OnDemandPercentageAboveBaseCapacity=json_data.get("OnDemandPercentageAboveBaseCapacity"),
            SpotInstancePools=json_data.get("SpotInstancePools"),
            SpotAllocationStrategy=json_data.get("SpotAllocationStrategy"),
            SpotMaxPrice=json_data.get("SpotMaxPrice"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstancesDistribution = InstancesDistribution


@dataclass
class LaunchTemplate(BaseModel):
    LaunchTemplateSpecification: Optional["_LaunchTemplateSpecification"]
    Overrides: Optional[Sequence["_LaunchTemplateOverrides"]]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplate"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateSpecification=LaunchTemplateSpecification._deserialize(json_data.get("LaunchTemplateSpecification")),
            Overrides=deserialize_list(json_data.get("Overrides"), LaunchTemplateOverrides),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplate = LaunchTemplate


@dataclass
class LaunchTemplateOverrides(BaseModel):
    LaunchTemplateSpecification: Optional["_LaunchTemplateSpecification"]
    WeightedCapacity: Optional[str]
    InstanceRequirements: Optional["_InstanceRequirements"]
    InstanceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateOverrides"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateOverrides"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateSpecification=LaunchTemplateSpecification._deserialize(json_data.get("LaunchTemplateSpecification")),
            WeightedCapacity=json_data.get("WeightedCapacity"),
            InstanceRequirements=InstanceRequirements._deserialize(json_data.get("InstanceRequirements")),
            InstanceType=json_data.get("InstanceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateOverrides = LaunchTemplateOverrides


@dataclass
class InstanceRequirements(BaseModel):
    LocalStorageTypes: Optional[AbstractSet[str]]
    InstanceGenerations: Optional[AbstractSet[str]]
    NetworkInterfaceCount: Optional["_NetworkInterfaceCountRequest"]
    AcceleratorTypes: Optional[AbstractSet[str]]
    MemoryGiBPerVCpu: Optional["_MemoryGiBPerVCpuRequest"]
    AcceleratorManufacturers: Optional[AbstractSet[str]]
    ExcludedInstanceTypes: Optional[Sequence[str]]
    VCpuCount: Optional["_VCpuCountRequest"]
    AllowedInstanceTypes: Optional[Sequence[str]]
    LocalStorage: Optional[str]
    CpuManufacturers: Optional[AbstractSet[str]]
    AcceleratorCount: Optional["_AcceleratorCountRequest"]
    NetworkBandwidthGbps: Optional["_NetworkBandwidthGbpsRequest"]
    BareMetal: Optional[str]
    RequireHibernateSupport: Optional[bool]
    BaselineEbsBandwidthMbps: Optional["_BaselineEbsBandwidthMbpsRequest"]
    SpotMaxPricePercentageOverLowestPrice: Optional[int]
    AcceleratorNames: Optional[AbstractSet[str]]
    AcceleratorTotalMemoryMiB: Optional["_AcceleratorTotalMemoryMiBRequest"]
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int]
    BurstablePerformance: Optional[str]
    MemoryMiB: Optional["_MemoryMiBRequest"]
    TotalLocalStorageGB: Optional["_TotalLocalStorageGBRequest"]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceRequirements"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceRequirements"]:
        if not json_data:
            return None
        return cls(
            LocalStorageTypes=set_or_none(json_data.get("LocalStorageTypes")),
            InstanceGenerations=set_or_none(json_data.get("InstanceGenerations")),
            NetworkInterfaceCount=NetworkInterfaceCountRequest._deserialize(json_data.get("NetworkInterfaceCount")),
            AcceleratorTypes=set_or_none(json_data.get("AcceleratorTypes")),
            MemoryGiBPerVCpu=MemoryGiBPerVCpuRequest._deserialize(json_data.get("MemoryGiBPerVCpu")),
            AcceleratorManufacturers=set_or_none(json_data.get("AcceleratorManufacturers")),
            ExcludedInstanceTypes=json_data.get("ExcludedInstanceTypes"),
            VCpuCount=VCpuCountRequest._deserialize(json_data.get("VCpuCount")),
            AllowedInstanceTypes=json_data.get("AllowedInstanceTypes"),
            LocalStorage=json_data.get("LocalStorage"),
            CpuManufacturers=set_or_none(json_data.get("CpuManufacturers")),
            AcceleratorCount=AcceleratorCountRequest._deserialize(json_data.get("AcceleratorCount")),
            NetworkBandwidthGbps=NetworkBandwidthGbpsRequest._deserialize(json_data.get("NetworkBandwidthGbps")),
            BareMetal=json_data.get("BareMetal"),
            RequireHibernateSupport=json_data.get("RequireHibernateSupport"),
            BaselineEbsBandwidthMbps=BaselineEbsBandwidthMbpsRequest._deserialize(json_data.get("BaselineEbsBandwidthMbps")),
            SpotMaxPricePercentageOverLowestPrice=json_data.get("SpotMaxPricePercentageOverLowestPrice"),
            AcceleratorNames=set_or_none(json_data.get("AcceleratorNames")),
            AcceleratorTotalMemoryMiB=AcceleratorTotalMemoryMiBRequest._deserialize(json_data.get("AcceleratorTotalMemoryMiB")),
            OnDemandMaxPricePercentageOverLowestPrice=json_data.get("OnDemandMaxPricePercentageOverLowestPrice"),
            BurstablePerformance=json_data.get("BurstablePerformance"),
            MemoryMiB=MemoryMiBRequest._deserialize(json_data.get("MemoryMiB")),
            TotalLocalStorageGB=TotalLocalStorageGBRequest._deserialize(json_data.get("TotalLocalStorageGB")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceRequirements = InstanceRequirements


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
class VCpuCountRequest(BaseModel):
    Min: Optional[int]
    Max: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_VCpuCountRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VCpuCountRequest"]:
        if not json_data:
            return None
        return cls(
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VCpuCountRequest = VCpuCountRequest


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
class TagProperty(BaseModel):
    Value: Optional[str]
    Key: Optional[str]
    PropagateAtLaunch: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TagProperty"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagProperty"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
            PropagateAtLaunch=json_data.get("PropagateAtLaunch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagProperty = TagProperty


@dataclass
class MetricsCollection(BaseModel):
    Metrics: Optional[Sequence[str]]
    Granularity: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricsCollection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricsCollection"]:
        if not json_data:
            return None
        return cls(
            Metrics=json_data.get("Metrics"),
            Granularity=json_data.get("Granularity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricsCollection = MetricsCollection


@dataclass
class InstanceMaintenancePolicy(BaseModel):
    MaxHealthyPercentage: Optional[int]
    MinHealthyPercentage: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceMaintenancePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceMaintenancePolicy"]:
        if not json_data:
            return None
        return cls(
            MaxHealthyPercentage=json_data.get("MaxHealthyPercentage"),
            MinHealthyPercentage=json_data.get("MinHealthyPercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceMaintenancePolicy = InstanceMaintenancePolicy


