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
class AwsBatchComputeenvironment(BaseModel):
    ComputeEnvironmentArn: Optional[str]
    ComputeEnvironmentName: Optional[str]
    ComputeResources: Optional["_ComputeResources"]
    ReplaceComputeEnvironment: Optional[bool]
    ServiceRole: Optional[str]
    State: Optional[str]
    Tags: Optional[Any]
    Type: Optional[str]
    UpdatePolicy: Optional["_UpdatePolicy"]
    UnmanagedvCpus: Optional[int]
    EksConfiguration: Optional["_EksConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsBatchComputeenvironment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsBatchComputeenvironment"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ComputeEnvironmentArn=json_data.get("ComputeEnvironmentArn"),
            ComputeEnvironmentName=json_data.get("ComputeEnvironmentName"),
            ComputeResources=ComputeResources._deserialize(json_data.get("ComputeResources")),
            ReplaceComputeEnvironment=json_data.get("ReplaceComputeEnvironment"),
            ServiceRole=json_data.get("ServiceRole"),
            State=json_data.get("State"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            UpdatePolicy=UpdatePolicy._deserialize(json_data.get("UpdatePolicy")),
            UnmanagedvCpus=json_data.get("UnmanagedvCpus"),
            EksConfiguration=EksConfiguration._deserialize(json_data.get("EksConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsBatchComputeenvironment = AwsBatchComputeenvironment


@dataclass
class ComputeResources(BaseModel):
    AllocationStrategy: Optional[str]
    BidPercentage: Optional[int]
    DesiredvCpus: Optional[int]
    Ec2Configuration: Optional[Sequence["_Ec2ConfigurationObject"]]
    Ec2KeyPair: Optional[str]
    ImageId: Optional[str]
    InstanceRole: Optional[str]
    InstanceTypes: Optional[Sequence[str]]
    LaunchTemplate: Optional["_LaunchTemplateSpecification"]
    MaxvCpus: Optional[int]
    MinvCpus: Optional[int]
    PlacementGroup: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    SpotIamFleetRole: Optional[str]
    Subnets: Optional[Sequence[str]]
    Tags: Optional[MutableMapping[str, str]]
    Type: Optional[str]
    UpdateToLatestImageVersion: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ComputeResources"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComputeResources"]:
        if not json_data:
            return None
        return cls(
            AllocationStrategy=json_data.get("AllocationStrategy"),
            BidPercentage=json_data.get("BidPercentage"),
            DesiredvCpus=json_data.get("DesiredvCpus"),
            Ec2Configuration=deserialize_list(json_data.get("Ec2Configuration"), Ec2ConfigurationObject),
            Ec2KeyPair=json_data.get("Ec2KeyPair"),
            ImageId=json_data.get("ImageId"),
            InstanceRole=json_data.get("InstanceRole"),
            InstanceTypes=json_data.get("InstanceTypes"),
            LaunchTemplate=LaunchTemplateSpecification._deserialize(json_data.get("LaunchTemplate")),
            MaxvCpus=json_data.get("MaxvCpus"),
            MinvCpus=json_data.get("MinvCpus"),
            PlacementGroup=json_data.get("PlacementGroup"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SpotIamFleetRole=json_data.get("SpotIamFleetRole"),
            Subnets=json_data.get("Subnets"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            UpdateToLatestImageVersion=json_data.get("UpdateToLatestImageVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComputeResources = ComputeResources


@dataclass
class Ec2ConfigurationObject(BaseModel):
    ImageIdOverride: Optional[str]
    ImageType: Optional[str]
    ImageKubernetesVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ec2ConfigurationObject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ec2ConfigurationObject"]:
        if not json_data:
            return None
        return cls(
            ImageIdOverride=json_data.get("ImageIdOverride"),
            ImageType=json_data.get("ImageType"),
            ImageKubernetesVersion=json_data.get("ImageKubernetesVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ec2ConfigurationObject = Ec2ConfigurationObject


@dataclass
class LaunchTemplateSpecification(BaseModel):
    LaunchTemplateId: Optional[str]
    LaunchTemplateName: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateSpecification"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateId=json_data.get("LaunchTemplateId"),
            LaunchTemplateName=json_data.get("LaunchTemplateName"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateSpecification = LaunchTemplateSpecification


@dataclass
class UpdatePolicy(BaseModel):
    TerminateJobsOnUpdate: Optional[bool]
    JobExecutionTimeoutMinutes: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_UpdatePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpdatePolicy"]:
        if not json_data:
            return None
        return cls(
            TerminateJobsOnUpdate=json_data.get("TerminateJobsOnUpdate"),
            JobExecutionTimeoutMinutes=json_data.get("JobExecutionTimeoutMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpdatePolicy = UpdatePolicy


@dataclass
class EksConfiguration(BaseModel):
    EksClusterArn: Optional[str]
    KubernetesNamespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EksConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EksConfiguration"]:
        if not json_data:
            return None
        return cls(
            EksClusterArn=json_data.get("EksClusterArn"),
            KubernetesNamespace=json_data.get("KubernetesNamespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EksConfiguration = EksConfiguration


