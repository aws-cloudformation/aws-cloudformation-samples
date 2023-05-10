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
class AwsGameliftGameservergroup(BaseModel):
    AutoScalingGroupArn: Optional[str]
    AutoScalingPolicy: Optional["_AutoScalingPolicy"]
    BalancingStrategy: Optional[str]
    DeleteOption: Optional[str]
    GameServerGroupArn: Optional[str]
    GameServerGroupName: Optional[str]
    GameServerProtectionPolicy: Optional[str]
    InstanceDefinitions: Optional[Sequence["_InstanceDefinition"]]
    LaunchTemplate: Optional["_LaunchTemplate"]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    RoleArn: Optional[str]
    Tags: Optional[Any]
    VpcSubnets: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGameliftGameservergroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGameliftGameservergroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AutoScalingGroupArn=json_data.get("AutoScalingGroupArn"),
            AutoScalingPolicy=AutoScalingPolicy._deserialize(json_data.get("AutoScalingPolicy")),
            BalancingStrategy=json_data.get("BalancingStrategy"),
            DeleteOption=json_data.get("DeleteOption"),
            GameServerGroupArn=json_data.get("GameServerGroupArn"),
            GameServerGroupName=json_data.get("GameServerGroupName"),
            GameServerProtectionPolicy=json_data.get("GameServerProtectionPolicy"),
            InstanceDefinitions=deserialize_list(json_data.get("InstanceDefinitions"), InstanceDefinition),
            LaunchTemplate=LaunchTemplate._deserialize(json_data.get("LaunchTemplate")),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            RoleArn=json_data.get("RoleArn"),
            Tags=json_data.get("Tags"),
            VpcSubnets=json_data.get("VpcSubnets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGameliftGameservergroup = AwsGameliftGameservergroup


@dataclass
class AutoScalingPolicy(BaseModel):
    EstimatedInstanceWarmup: Optional[float]
    TargetTrackingConfiguration: Optional["_TargetTrackingConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AutoScalingPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoScalingPolicy"]:
        if not json_data:
            return None
        return cls(
            EstimatedInstanceWarmup=json_data.get("EstimatedInstanceWarmup"),
            TargetTrackingConfiguration=TargetTrackingConfiguration._deserialize(json_data.get("TargetTrackingConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoScalingPolicy = AutoScalingPolicy


@dataclass
class TargetTrackingConfiguration(BaseModel):
    TargetValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TargetTrackingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetTrackingConfiguration"]:
        if not json_data:
            return None
        return cls(
            TargetValue=json_data.get("TargetValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetTrackingConfiguration = TargetTrackingConfiguration


@dataclass
class InstanceDefinition(BaseModel):
    InstanceType: Optional[str]
    WeightedCapacity: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceDefinition"]:
        if not json_data:
            return None
        return cls(
            InstanceType=json_data.get("InstanceType"),
            WeightedCapacity=json_data.get("WeightedCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceDefinition = InstanceDefinition


@dataclass
class LaunchTemplate(BaseModel):
    LaunchTemplateId: Optional[str]
    LaunchTemplateName: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplate"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateId=json_data.get("LaunchTemplateId"),
            LaunchTemplateName=json_data.get("LaunchTemplateName"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplate = LaunchTemplate


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


