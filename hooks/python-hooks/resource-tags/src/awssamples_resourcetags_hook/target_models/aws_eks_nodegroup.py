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
class AwsEksNodegroup(BaseModel):
    AmiType: Optional[str]
    CapacityType: Optional[str]
    ClusterName: Optional[str]
    DiskSize: Optional[int]
    ForceUpdateEnabled: Optional[bool]
    InstanceTypes: Optional[Sequence[str]]
    Labels: Optional[MutableMapping[str, str]]
    LaunchTemplate: Optional["_LaunchTemplateSpecification"]
    NodegroupName: Optional[str]
    NodeRole: Optional[str]
    ReleaseVersion: Optional[str]
    RemoteAccess: Optional["_RemoteAccess"]
    ScalingConfig: Optional["_ScalingConfig"]
    Subnets: Optional[Sequence[str]]
    Tags: Optional[Any]
    Taints: Optional[Sequence["_Taint"]]
    UpdateConfig: Optional["_UpdateConfig"]
    Version: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEksNodegroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEksNodegroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AmiType=json_data.get("AmiType"),
            CapacityType=json_data.get("CapacityType"),
            ClusterName=json_data.get("ClusterName"),
            DiskSize=json_data.get("DiskSize"),
            ForceUpdateEnabled=json_data.get("ForceUpdateEnabled"),
            InstanceTypes=json_data.get("InstanceTypes"),
            Labels=json_data.get("Labels"),
            LaunchTemplate=LaunchTemplateSpecification._deserialize(json_data.get("LaunchTemplate")),
            NodegroupName=json_data.get("NodegroupName"),
            NodeRole=json_data.get("NodeRole"),
            ReleaseVersion=json_data.get("ReleaseVersion"),
            RemoteAccess=RemoteAccess._deserialize(json_data.get("RemoteAccess")),
            ScalingConfig=ScalingConfig._deserialize(json_data.get("ScalingConfig")),
            Subnets=json_data.get("Subnets"),
            Tags=json_data.get("Tags"),
            Taints=deserialize_list(json_data.get("Taints"), Taint),
            UpdateConfig=UpdateConfig._deserialize(json_data.get("UpdateConfig")),
            Version=json_data.get("Version"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEksNodegroup = AwsEksNodegroup


@dataclass
class LaunchTemplateSpecification(BaseModel):
    Id: Optional[str]
    Version: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateSpecification"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Version=json_data.get("Version"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateSpecification = LaunchTemplateSpecification


@dataclass
class RemoteAccess(BaseModel):
    SourceSecurityGroups: Optional[Sequence[str]]
    Ec2SshKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RemoteAccess"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RemoteAccess"]:
        if not json_data:
            return None
        return cls(
            SourceSecurityGroups=json_data.get("SourceSecurityGroups"),
            Ec2SshKey=json_data.get("Ec2SshKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RemoteAccess = RemoteAccess


@dataclass
class ScalingConfig(BaseModel):
    MinSize: Optional[int]
    DesiredSize: Optional[int]
    MaxSize: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingConfig"]:
        if not json_data:
            return None
        return cls(
            MinSize=json_data.get("MinSize"),
            DesiredSize=json_data.get("DesiredSize"),
            MaxSize=json_data.get("MaxSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingConfig = ScalingConfig


@dataclass
class Taint(BaseModel):
    Key: Optional[str]
    Value: Optional[str]
    Effect: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Taint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Taint"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
            Effect=json_data.get("Effect"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Taint = Taint


@dataclass
class UpdateConfig(BaseModel):
    MaxUnavailable: Optional[float]
    MaxUnavailablePercentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_UpdateConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpdateConfig"]:
        if not json_data:
            return None
        return cls(
            MaxUnavailable=json_data.get("MaxUnavailable"),
            MaxUnavailablePercentage=json_data.get("MaxUnavailablePercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpdateConfig = UpdateConfig


