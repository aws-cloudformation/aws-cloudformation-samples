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
class AwsEmrCluster(BaseModel):
    Steps: Optional[Sequence["_StepConfig"]]
    StepConcurrencyLevel: Optional[int]
    EbsRootVolumeSize: Optional[int]
    OSReleaseLabel: Optional[str]
    Name: Optional[str]
    ServiceRole: Optional[str]
    LogUri: Optional[str]
    BootstrapActions: Optional[Sequence["_BootstrapActionConfig"]]
    MasterPublicDNS: Optional[str]
    Configurations: Optional[Sequence["_Configuration"]]
    ReleaseLabel: Optional[str]
    Tags: Optional[Any]
    ManagedScalingPolicy: Optional["_ManagedScalingPolicy"]
    LogEncryptionKmsKeyId: Optional[str]
    AdditionalInfo: Optional[MutableMapping[str, Any]]
    AutoTerminationPolicy: Optional["_AutoTerminationPolicy"]
    KerberosAttributes: Optional["_KerberosAttributes"]
    Applications: Optional[Sequence["_Application"]]
    AutoScalingRole: Optional[str]
    CustomAmiId: Optional[str]
    Instances: Optional["_JobFlowInstancesConfig"]
    ScaleDownBehavior: Optional[str]
    JobFlowRole: Optional[str]
    VisibleToAllUsers: Optional[bool]
    SecurityConfiguration: Optional[str]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEmrCluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEmrCluster"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Steps=deserialize_list(json_data.get("Steps"), StepConfig),
            StepConcurrencyLevel=json_data.get("StepConcurrencyLevel"),
            EbsRootVolumeSize=json_data.get("EbsRootVolumeSize"),
            OSReleaseLabel=json_data.get("OSReleaseLabel"),
            Name=json_data.get("Name"),
            ServiceRole=json_data.get("ServiceRole"),
            LogUri=json_data.get("LogUri"),
            BootstrapActions=deserialize_list(json_data.get("BootstrapActions"), BootstrapActionConfig),
            MasterPublicDNS=json_data.get("MasterPublicDNS"),
            Configurations=deserialize_list(json_data.get("Configurations"), Configuration),
            ReleaseLabel=json_data.get("ReleaseLabel"),
            Tags=json_data.get("Tags"),
            ManagedScalingPolicy=ManagedScalingPolicy._deserialize(json_data.get("ManagedScalingPolicy")),
            LogEncryptionKmsKeyId=json_data.get("LogEncryptionKmsKeyId"),
            AdditionalInfo=json_data.get("AdditionalInfo"),
            AutoTerminationPolicy=AutoTerminationPolicy._deserialize(json_data.get("AutoTerminationPolicy")),
            KerberosAttributes=KerberosAttributes._deserialize(json_data.get("KerberosAttributes")),
            Applications=deserialize_list(json_data.get("Applications"), Application),
            AutoScalingRole=json_data.get("AutoScalingRole"),
            CustomAmiId=json_data.get("CustomAmiId"),
            Instances=JobFlowInstancesConfig._deserialize(json_data.get("Instances")),
            ScaleDownBehavior=json_data.get("ScaleDownBehavior"),
            JobFlowRole=json_data.get("JobFlowRole"),
            VisibleToAllUsers=json_data.get("VisibleToAllUsers"),
            SecurityConfiguration=json_data.get("SecurityConfiguration"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEmrCluster = AwsEmrCluster


@dataclass
class StepConfig(BaseModel):
    HadoopJarStep: Optional["_HadoopJarStepConfig"]
    ActionOnFailure: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StepConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepConfig"]:
        if not json_data:
            return None
        return cls(
            HadoopJarStep=HadoopJarStepConfig._deserialize(json_data.get("HadoopJarStep")),
            ActionOnFailure=json_data.get("ActionOnFailure"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepConfig = StepConfig


@dataclass
class HadoopJarStepConfig(BaseModel):
    Args: Optional[Sequence[str]]
    MainClass: Optional[str]
    Jar: Optional[str]
    StepProperties: Optional[Sequence["_KeyValue"]]

    @classmethod
    def _deserialize(
        cls: Type["_HadoopJarStepConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HadoopJarStepConfig"]:
        if not json_data:
            return None
        return cls(
            Args=json_data.get("Args"),
            MainClass=json_data.get("MainClass"),
            Jar=json_data.get("Jar"),
            StepProperties=deserialize_list(json_data.get("StepProperties"), KeyValue),
        )


# work around possible type aliasing issues when variable has same name as a model
_HadoopJarStepConfig = HadoopJarStepConfig


@dataclass
class KeyValue(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeyValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyValue"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyValue = KeyValue


@dataclass
class BootstrapActionConfig(BaseModel):
    ScriptBootstrapAction: Optional["_ScriptBootstrapActionConfig"]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BootstrapActionConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BootstrapActionConfig"]:
        if not json_data:
            return None
        return cls(
            ScriptBootstrapAction=ScriptBootstrapActionConfig._deserialize(json_data.get("ScriptBootstrapAction")),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BootstrapActionConfig = BootstrapActionConfig


@dataclass
class ScriptBootstrapActionConfig(BaseModel):
    Path: Optional[str]
    Args: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ScriptBootstrapActionConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScriptBootstrapActionConfig"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Args=json_data.get("Args"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScriptBootstrapActionConfig = ScriptBootstrapActionConfig


@dataclass
class Configuration(BaseModel):
    ConfigurationProperties: Optional[MutableMapping[str, str]]
    Configurations: Optional[Sequence["_Configuration"]]
    Classification: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Configuration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Configuration"]:
        if not json_data:
            return None
        return cls(
            ConfigurationProperties=json_data.get("ConfigurationProperties"),
            Configurations=deserialize_list(json_data.get("Configurations"), Configuration),
            Classification=json_data.get("Classification"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Configuration = Configuration


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
class ManagedScalingPolicy(BaseModel):
    ComputeLimits: Optional["_ComputeLimits"]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedScalingPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedScalingPolicy"]:
        if not json_data:
            return None
        return cls(
            ComputeLimits=ComputeLimits._deserialize(json_data.get("ComputeLimits")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagedScalingPolicy = ManagedScalingPolicy


@dataclass
class ComputeLimits(BaseModel):
    MaximumOnDemandCapacityUnits: Optional[int]
    MaximumCapacityUnits: Optional[int]
    MaximumCoreCapacityUnits: Optional[int]
    MinimumCapacityUnits: Optional[int]
    UnitType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComputeLimits"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComputeLimits"]:
        if not json_data:
            return None
        return cls(
            MaximumOnDemandCapacityUnits=json_data.get("MaximumOnDemandCapacityUnits"),
            MaximumCapacityUnits=json_data.get("MaximumCapacityUnits"),
            MaximumCoreCapacityUnits=json_data.get("MaximumCoreCapacityUnits"),
            MinimumCapacityUnits=json_data.get("MinimumCapacityUnits"),
            UnitType=json_data.get("UnitType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComputeLimits = ComputeLimits


@dataclass
class AutoTerminationPolicy(BaseModel):
    IdleTimeout: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AutoTerminationPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoTerminationPolicy"]:
        if not json_data:
            return None
        return cls(
            IdleTimeout=json_data.get("IdleTimeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoTerminationPolicy = AutoTerminationPolicy


@dataclass
class KerberosAttributes(BaseModel):
    KdcAdminPassword: Optional[str]
    Realm: Optional[str]
    ADDomainJoinPassword: Optional[str]
    ADDomainJoinUser: Optional[str]
    CrossRealmTrustPrincipalPassword: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KerberosAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KerberosAttributes"]:
        if not json_data:
            return None
        return cls(
            KdcAdminPassword=json_data.get("KdcAdminPassword"),
            Realm=json_data.get("Realm"),
            ADDomainJoinPassword=json_data.get("ADDomainJoinPassword"),
            ADDomainJoinUser=json_data.get("ADDomainJoinUser"),
            CrossRealmTrustPrincipalPassword=json_data.get("CrossRealmTrustPrincipalPassword"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KerberosAttributes = KerberosAttributes


@dataclass
class Application(BaseModel):
    AdditionalInfo: Optional[MutableMapping[str, str]]
    Args: Optional[Sequence[str]]
    Version: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Application"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Application"]:
        if not json_data:
            return None
        return cls(
            AdditionalInfo=json_data.get("AdditionalInfo"),
            Args=json_data.get("Args"),
            Version=json_data.get("Version"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Application = Application


@dataclass
class JobFlowInstancesConfig(BaseModel):
    MasterInstanceFleet: Optional["_InstanceFleetConfig"]
    AdditionalSlaveSecurityGroups: Optional[Sequence[str]]
    CoreInstanceFleet: Optional["_InstanceFleetConfig"]
    CoreInstanceGroup: Optional["_InstanceGroupConfig"]
    Ec2SubnetIds: Optional[Sequence[str]]
    HadoopVersion: Optional[str]
    TerminationProtected: Optional[bool]
    KeepJobFlowAliveWhenNoSteps: Optional[bool]
    Ec2KeyName: Optional[str]
    MasterInstanceGroup: Optional["_InstanceGroupConfig"]
    Placement: Optional["_PlacementType"]
    TaskInstanceFleets: Optional[Sequence["_InstanceFleetConfig"]]
    Ec2SubnetId: Optional[str]
    TaskInstanceGroups: Optional[Sequence["_InstanceGroupConfig"]]
    ServiceAccessSecurityGroup: Optional[str]
    EmrManagedSlaveSecurityGroup: Optional[str]
    AdditionalMasterSecurityGroups: Optional[Sequence[str]]
    EmrManagedMasterSecurityGroup: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JobFlowInstancesConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JobFlowInstancesConfig"]:
        if not json_data:
            return None
        return cls(
            MasterInstanceFleet=InstanceFleetConfig._deserialize(json_data.get("MasterInstanceFleet")),
            AdditionalSlaveSecurityGroups=json_data.get("AdditionalSlaveSecurityGroups"),
            CoreInstanceFleet=InstanceFleetConfig._deserialize(json_data.get("CoreInstanceFleet")),
            CoreInstanceGroup=InstanceGroupConfig._deserialize(json_data.get("CoreInstanceGroup")),
            Ec2SubnetIds=json_data.get("Ec2SubnetIds"),
            HadoopVersion=json_data.get("HadoopVersion"),
            TerminationProtected=json_data.get("TerminationProtected"),
            KeepJobFlowAliveWhenNoSteps=json_data.get("KeepJobFlowAliveWhenNoSteps"),
            Ec2KeyName=json_data.get("Ec2KeyName"),
            MasterInstanceGroup=InstanceGroupConfig._deserialize(json_data.get("MasterInstanceGroup")),
            Placement=PlacementType._deserialize(json_data.get("Placement")),
            TaskInstanceFleets=deserialize_list(json_data.get("TaskInstanceFleets"), InstanceFleetConfig),
            Ec2SubnetId=json_data.get("Ec2SubnetId"),
            TaskInstanceGroups=deserialize_list(json_data.get("TaskInstanceGroups"), InstanceGroupConfig),
            ServiceAccessSecurityGroup=json_data.get("ServiceAccessSecurityGroup"),
            EmrManagedSlaveSecurityGroup=json_data.get("EmrManagedSlaveSecurityGroup"),
            AdditionalMasterSecurityGroups=json_data.get("AdditionalMasterSecurityGroups"),
            EmrManagedMasterSecurityGroup=json_data.get("EmrManagedMasterSecurityGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JobFlowInstancesConfig = JobFlowInstancesConfig


@dataclass
class InstanceFleetConfig(BaseModel):
    TargetOnDemandCapacity: Optional[int]
    TargetSpotCapacity: Optional[int]
    InstanceTypeConfigs: Optional[Sequence["_InstanceTypeConfig"]]
    LaunchSpecifications: Optional["_InstanceFleetProvisioningSpecifications"]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceFleetConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceFleetConfig"]:
        if not json_data:
            return None
        return cls(
            TargetOnDemandCapacity=json_data.get("TargetOnDemandCapacity"),
            TargetSpotCapacity=json_data.get("TargetSpotCapacity"),
            InstanceTypeConfigs=deserialize_list(json_data.get("InstanceTypeConfigs"), InstanceTypeConfig),
            LaunchSpecifications=InstanceFleetProvisioningSpecifications._deserialize(json_data.get("LaunchSpecifications")),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceFleetConfig = InstanceFleetConfig


@dataclass
class InstanceTypeConfig(BaseModel):
    BidPrice: Optional[str]
    WeightedCapacity: Optional[int]
    EbsConfiguration: Optional["_EbsConfiguration"]
    BidPriceAsPercentageOfOnDemandPrice: Optional[float]
    CustomAmiId: Optional[str]
    Configurations: Optional[Sequence["_Configuration"]]
    InstanceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceTypeConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceTypeConfig"]:
        if not json_data:
            return None
        return cls(
            BidPrice=json_data.get("BidPrice"),
            WeightedCapacity=json_data.get("WeightedCapacity"),
            EbsConfiguration=EbsConfiguration._deserialize(json_data.get("EbsConfiguration")),
            BidPriceAsPercentageOfOnDemandPrice=json_data.get("BidPriceAsPercentageOfOnDemandPrice"),
            CustomAmiId=json_data.get("CustomAmiId"),
            Configurations=deserialize_list(json_data.get("Configurations"), Configuration),
            InstanceType=json_data.get("InstanceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceTypeConfig = InstanceTypeConfig


@dataclass
class EbsConfiguration(BaseModel):
    EbsBlockDeviceConfigs: Optional[Sequence["_EbsBlockDeviceConfig"]]
    EbsOptimized: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EbsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsConfiguration"]:
        if not json_data:
            return None
        return cls(
            EbsBlockDeviceConfigs=deserialize_list(json_data.get("EbsBlockDeviceConfigs"), EbsBlockDeviceConfig),
            EbsOptimized=json_data.get("EbsOptimized"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsConfiguration = EbsConfiguration


@dataclass
class EbsBlockDeviceConfig(BaseModel):
    VolumeSpecification: Optional["_VolumeSpecification"]
    VolumesPerInstance: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_EbsBlockDeviceConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsBlockDeviceConfig"]:
        if not json_data:
            return None
        return cls(
            VolumeSpecification=VolumeSpecification._deserialize(json_data.get("VolumeSpecification")),
            VolumesPerInstance=json_data.get("VolumesPerInstance"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsBlockDeviceConfig = EbsBlockDeviceConfig


@dataclass
class VolumeSpecification(BaseModel):
    SizeInGB: Optional[int]
    VolumeType: Optional[str]
    Iops: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeSpecification"]:
        if not json_data:
            return None
        return cls(
            SizeInGB=json_data.get("SizeInGB"),
            VolumeType=json_data.get("VolumeType"),
            Iops=json_data.get("Iops"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeSpecification = VolumeSpecification


@dataclass
class InstanceFleetProvisioningSpecifications(BaseModel):
    SpotSpecification: Optional["_SpotProvisioningSpecification"]
    OnDemandSpecification: Optional["_OnDemandProvisioningSpecification"]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceFleetProvisioningSpecifications"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceFleetProvisioningSpecifications"]:
        if not json_data:
            return None
        return cls(
            SpotSpecification=SpotProvisioningSpecification._deserialize(json_data.get("SpotSpecification")),
            OnDemandSpecification=OnDemandProvisioningSpecification._deserialize(json_data.get("OnDemandSpecification")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceFleetProvisioningSpecifications = InstanceFleetProvisioningSpecifications


@dataclass
class SpotProvisioningSpecification(BaseModel):
    AllocationStrategy: Optional[str]
    TimeoutDurationMinutes: Optional[int]
    TimeoutAction: Optional[str]
    BlockDurationMinutes: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_SpotProvisioningSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpotProvisioningSpecification"]:
        if not json_data:
            return None
        return cls(
            AllocationStrategy=json_data.get("AllocationStrategy"),
            TimeoutDurationMinutes=json_data.get("TimeoutDurationMinutes"),
            TimeoutAction=json_data.get("TimeoutAction"),
            BlockDurationMinutes=json_data.get("BlockDurationMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpotProvisioningSpecification = SpotProvisioningSpecification


@dataclass
class OnDemandProvisioningSpecification(BaseModel):
    AllocationStrategy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnDemandProvisioningSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnDemandProvisioningSpecification"]:
        if not json_data:
            return None
        return cls(
            AllocationStrategy=json_data.get("AllocationStrategy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnDemandProvisioningSpecification = OnDemandProvisioningSpecification


@dataclass
class InstanceGroupConfig(BaseModel):
    AutoScalingPolicy: Optional["_AutoScalingPolicy"]
    BidPrice: Optional[str]
    InstanceCount: Optional[int]
    EbsConfiguration: Optional["_EbsConfiguration"]
    CustomAmiId: Optional[str]
    Configurations: Optional[Sequence["_Configuration"]]
    InstanceType: Optional[str]
    Market: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceGroupConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceGroupConfig"]:
        if not json_data:
            return None
        return cls(
            AutoScalingPolicy=AutoScalingPolicy._deserialize(json_data.get("AutoScalingPolicy")),
            BidPrice=json_data.get("BidPrice"),
            InstanceCount=json_data.get("InstanceCount"),
            EbsConfiguration=EbsConfiguration._deserialize(json_data.get("EbsConfiguration")),
            CustomAmiId=json_data.get("CustomAmiId"),
            Configurations=deserialize_list(json_data.get("Configurations"), Configuration),
            InstanceType=json_data.get("InstanceType"),
            Market=json_data.get("Market"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceGroupConfig = InstanceGroupConfig


@dataclass
class AutoScalingPolicy(BaseModel):
    Rules: Optional[Sequence["_ScalingRule"]]
    Constraints: Optional["_ScalingConstraints"]

    @classmethod
    def _deserialize(
        cls: Type["_AutoScalingPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoScalingPolicy"]:
        if not json_data:
            return None
        return cls(
            Rules=deserialize_list(json_data.get("Rules"), ScalingRule),
            Constraints=ScalingConstraints._deserialize(json_data.get("Constraints")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoScalingPolicy = AutoScalingPolicy


@dataclass
class ScalingRule(BaseModel):
    Action: Optional["_ScalingAction"]
    Description: Optional[str]
    Trigger: Optional["_ScalingTrigger"]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingRule"]:
        if not json_data:
            return None
        return cls(
            Action=ScalingAction._deserialize(json_data.get("Action")),
            Description=json_data.get("Description"),
            Trigger=ScalingTrigger._deserialize(json_data.get("Trigger")),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingRule = ScalingRule


@dataclass
class ScalingAction(BaseModel):
    Market: Optional[str]
    SimpleScalingPolicyConfiguration: Optional["_SimpleScalingPolicyConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingAction"]:
        if not json_data:
            return None
        return cls(
            Market=json_data.get("Market"),
            SimpleScalingPolicyConfiguration=SimpleScalingPolicyConfiguration._deserialize(json_data.get("SimpleScalingPolicyConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingAction = ScalingAction


@dataclass
class SimpleScalingPolicyConfiguration(BaseModel):
    ScalingAdjustment: Optional[int]
    CoolDown: Optional[int]
    AdjustmentType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SimpleScalingPolicyConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SimpleScalingPolicyConfiguration"]:
        if not json_data:
            return None
        return cls(
            ScalingAdjustment=json_data.get("ScalingAdjustment"),
            CoolDown=json_data.get("CoolDown"),
            AdjustmentType=json_data.get("AdjustmentType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SimpleScalingPolicyConfiguration = SimpleScalingPolicyConfiguration


@dataclass
class ScalingTrigger(BaseModel):
    CloudWatchAlarmDefinition: Optional["_CloudWatchAlarmDefinition"]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingTrigger"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingTrigger"]:
        if not json_data:
            return None
        return cls(
            CloudWatchAlarmDefinition=CloudWatchAlarmDefinition._deserialize(json_data.get("CloudWatchAlarmDefinition")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingTrigger = ScalingTrigger


@dataclass
class CloudWatchAlarmDefinition(BaseModel):
    MetricName: Optional[str]
    ComparisonOperator: Optional[str]
    Statistic: Optional[str]
    Dimensions: Optional[Sequence["_MetricDimension"]]
    Period: Optional[int]
    EvaluationPeriods: Optional[int]
    Unit: Optional[str]
    Namespace: Optional[str]
    Threshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CloudWatchAlarmDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudWatchAlarmDefinition"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            ComparisonOperator=json_data.get("ComparisonOperator"),
            Statistic=json_data.get("Statistic"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), MetricDimension),
            Period=json_data.get("Period"),
            EvaluationPeriods=json_data.get("EvaluationPeriods"),
            Unit=json_data.get("Unit"),
            Namespace=json_data.get("Namespace"),
            Threshold=json_data.get("Threshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudWatchAlarmDefinition = CloudWatchAlarmDefinition


@dataclass
class MetricDimension(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDimension"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDimension"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDimension = MetricDimension


@dataclass
class ScalingConstraints(BaseModel):
    MinCapacity: Optional[int]
    MaxCapacity: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingConstraints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingConstraints"]:
        if not json_data:
            return None
        return cls(
            MinCapacity=json_data.get("MinCapacity"),
            MaxCapacity=json_data.get("MaxCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingConstraints = ScalingConstraints


@dataclass
class PlacementType(BaseModel):
    AvailabilityZone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementType"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZone=json_data.get("AvailabilityZone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementType = PlacementType


