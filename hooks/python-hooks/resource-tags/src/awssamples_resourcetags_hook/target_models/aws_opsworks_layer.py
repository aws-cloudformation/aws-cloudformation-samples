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
class AwsOpsworksLayer(BaseModel):
    Id: Optional[str]
    Attributes: Optional[MutableMapping[str, str]]
    AutoAssignElasticIps: Optional[bool]
    AutoAssignPublicIps: Optional[bool]
    CustomInstanceProfileArn: Optional[str]
    CustomJson: Optional[MutableMapping[str, Any]]
    CustomRecipes: Optional["_Recipes"]
    CustomSecurityGroupIds: Optional[Sequence[str]]
    EnableAutoHealing: Optional[bool]
    InstallUpdatesOnBoot: Optional[bool]
    LifecycleEventConfiguration: Optional["_LifecycleEventConfiguration"]
    LoadBasedAutoScaling: Optional["_LoadBasedAutoScaling"]
    Name: Optional[str]
    Packages: Optional[Sequence[str]]
    Shortname: Optional[str]
    StackId: Optional[str]
    Tags: Optional[Any]
    Type: Optional[str]
    UseEbsOptimizedInstances: Optional[bool]
    VolumeConfigurations: Optional[Sequence["_VolumeConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsOpsworksLayer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsOpsworksLayer"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Attributes=json_data.get("Attributes"),
            AutoAssignElasticIps=json_data.get("AutoAssignElasticIps"),
            AutoAssignPublicIps=json_data.get("AutoAssignPublicIps"),
            CustomInstanceProfileArn=json_data.get("CustomInstanceProfileArn"),
            CustomJson=json_data.get("CustomJson"),
            CustomRecipes=Recipes._deserialize(json_data.get("CustomRecipes")),
            CustomSecurityGroupIds=json_data.get("CustomSecurityGroupIds"),
            EnableAutoHealing=json_data.get("EnableAutoHealing"),
            InstallUpdatesOnBoot=json_data.get("InstallUpdatesOnBoot"),
            LifecycleEventConfiguration=LifecycleEventConfiguration._deserialize(json_data.get("LifecycleEventConfiguration")),
            LoadBasedAutoScaling=LoadBasedAutoScaling._deserialize(json_data.get("LoadBasedAutoScaling")),
            Name=json_data.get("Name"),
            Packages=json_data.get("Packages"),
            Shortname=json_data.get("Shortname"),
            StackId=json_data.get("StackId"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            UseEbsOptimizedInstances=json_data.get("UseEbsOptimizedInstances"),
            VolumeConfigurations=deserialize_list(json_data.get("VolumeConfigurations"), VolumeConfiguration),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsOpsworksLayer = AwsOpsworksLayer


@dataclass
class Recipes(BaseModel):
    Configure: Optional[Sequence[str]]
    Deploy: Optional[Sequence[str]]
    Setup: Optional[Sequence[str]]
    Shutdown: Optional[Sequence[str]]
    Undeploy: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Recipes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Recipes"]:
        if not json_data:
            return None
        return cls(
            Configure=json_data.get("Configure"),
            Deploy=json_data.get("Deploy"),
            Setup=json_data.get("Setup"),
            Shutdown=json_data.get("Shutdown"),
            Undeploy=json_data.get("Undeploy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Recipes = Recipes


@dataclass
class LifecycleEventConfiguration(BaseModel):
    ShutdownEventConfiguration: Optional["_ShutdownEventConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_LifecycleEventConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecycleEventConfiguration"]:
        if not json_data:
            return None
        return cls(
            ShutdownEventConfiguration=ShutdownEventConfiguration._deserialize(json_data.get("ShutdownEventConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecycleEventConfiguration = LifecycleEventConfiguration


@dataclass
class ShutdownEventConfiguration(BaseModel):
    DelayUntilElbConnectionsDrained: Optional[bool]
    ExecutionTimeout: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ShutdownEventConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShutdownEventConfiguration"]:
        if not json_data:
            return None
        return cls(
            DelayUntilElbConnectionsDrained=json_data.get("DelayUntilElbConnectionsDrained"),
            ExecutionTimeout=json_data.get("ExecutionTimeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShutdownEventConfiguration = ShutdownEventConfiguration


@dataclass
class LoadBasedAutoScaling(BaseModel):
    DownScaling: Optional["_AutoScalingThresholds"]
    Enable: Optional[bool]
    UpScaling: Optional["_AutoScalingThresholds"]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBasedAutoScaling"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBasedAutoScaling"]:
        if not json_data:
            return None
        return cls(
            DownScaling=AutoScalingThresholds._deserialize(json_data.get("DownScaling")),
            Enable=json_data.get("Enable"),
            UpScaling=AutoScalingThresholds._deserialize(json_data.get("UpScaling")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBasedAutoScaling = LoadBasedAutoScaling


@dataclass
class AutoScalingThresholds(BaseModel):
    CpuThreshold: Optional[float]
    IgnoreMetricsTime: Optional[int]
    InstanceCount: Optional[int]
    LoadThreshold: Optional[float]
    MemoryThreshold: Optional[float]
    ThresholdsWaitTime: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AutoScalingThresholds"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoScalingThresholds"]:
        if not json_data:
            return None
        return cls(
            CpuThreshold=json_data.get("CpuThreshold"),
            IgnoreMetricsTime=json_data.get("IgnoreMetricsTime"),
            InstanceCount=json_data.get("InstanceCount"),
            LoadThreshold=json_data.get("LoadThreshold"),
            MemoryThreshold=json_data.get("MemoryThreshold"),
            ThresholdsWaitTime=json_data.get("ThresholdsWaitTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoScalingThresholds = AutoScalingThresholds


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
class VolumeConfiguration(BaseModel):
    Encrypted: Optional[bool]
    Iops: Optional[int]
    MountPoint: Optional[str]
    NumberOfDisks: Optional[int]
    RaidLevel: Optional[int]
    Size: Optional[int]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeConfiguration"]:
        if not json_data:
            return None
        return cls(
            Encrypted=json_data.get("Encrypted"),
            Iops=json_data.get("Iops"),
            MountPoint=json_data.get("MountPoint"),
            NumberOfDisks=json_data.get("NumberOfDisks"),
            RaidLevel=json_data.get("RaidLevel"),
            Size=json_data.get("Size"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeConfiguration = VolumeConfiguration


