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
class AwsEcsService(BaseModel):
    PlatformVersion: Optional[str]
    HealthCheckGracePeriodSeconds: Optional[int]
    EnableECSManagedTags: Optional[bool]
    EnableExecuteCommand: Optional[bool]
    PlacementConstraints: Optional[Sequence["_PlacementConstraint"]]
    PropagateTags: Optional[str]
    Cluster: Optional[str]
    LoadBalancers: Optional[Sequence["_LoadBalancer"]]
    ServiceConnectConfiguration: Optional["_ServiceConnectConfiguration"]
    ServiceArn: Optional[str]
    DesiredCount: Optional[int]
    PlacementStrategies: Optional[Sequence["_PlacementStrategy"]]
    DeploymentController: Optional["_DeploymentController"]
    ServiceRegistries: Optional[Sequence["_ServiceRegistry"]]
    CapacityProviderStrategy: Optional[Sequence["_CapacityProviderStrategyItem"]]
    LaunchType: Optional[str]
    Name: Optional[str]
    Role: Optional[str]
    SchedulingStrategy: Optional[str]
    TaskDefinition: Optional[str]
    ServiceName: Optional[str]
    NetworkConfiguration: Optional["_NetworkConfiguration"]
    DeploymentConfiguration: Optional["_DeploymentConfiguration"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEcsService"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEcsService"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            PlatformVersion=json_data.get("PlatformVersion"),
            HealthCheckGracePeriodSeconds=json_data.get("HealthCheckGracePeriodSeconds"),
            EnableECSManagedTags=json_data.get("EnableECSManagedTags"),
            EnableExecuteCommand=json_data.get("EnableExecuteCommand"),
            PlacementConstraints=deserialize_list(json_data.get("PlacementConstraints"), PlacementConstraint),
            PropagateTags=json_data.get("PropagateTags"),
            Cluster=json_data.get("Cluster"),
            LoadBalancers=deserialize_list(json_data.get("LoadBalancers"), LoadBalancer),
            ServiceConnectConfiguration=ServiceConnectConfiguration._deserialize(json_data.get("ServiceConnectConfiguration")),
            ServiceArn=json_data.get("ServiceArn"),
            DesiredCount=json_data.get("DesiredCount"),
            PlacementStrategies=deserialize_list(json_data.get("PlacementStrategies"), PlacementStrategy),
            DeploymentController=DeploymentController._deserialize(json_data.get("DeploymentController")),
            ServiceRegistries=deserialize_list(json_data.get("ServiceRegistries"), ServiceRegistry),
            CapacityProviderStrategy=deserialize_list(json_data.get("CapacityProviderStrategy"), CapacityProviderStrategyItem),
            LaunchType=json_data.get("LaunchType"),
            Name=json_data.get("Name"),
            Role=json_data.get("Role"),
            SchedulingStrategy=json_data.get("SchedulingStrategy"),
            TaskDefinition=json_data.get("TaskDefinition"),
            ServiceName=json_data.get("ServiceName"),
            NetworkConfiguration=NetworkConfiguration._deserialize(json_data.get("NetworkConfiguration")),
            DeploymentConfiguration=DeploymentConfiguration._deserialize(json_data.get("DeploymentConfiguration")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEcsService = AwsEcsService


@dataclass
class PlacementConstraint(BaseModel):
    Type: Optional[str]
    Expression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementConstraint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementConstraint"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Expression=json_data.get("Expression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementConstraint = PlacementConstraint


@dataclass
class LoadBalancer(BaseModel):
    TargetGroupArn: Optional[str]
    LoadBalancerName: Optional[str]
    ContainerName: Optional[str]
    ContainerPort: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancer"]:
        if not json_data:
            return None
        return cls(
            TargetGroupArn=json_data.get("TargetGroupArn"),
            LoadBalancerName=json_data.get("LoadBalancerName"),
            ContainerName=json_data.get("ContainerName"),
            ContainerPort=json_data.get("ContainerPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancer = LoadBalancer


@dataclass
class ServiceConnectConfiguration(BaseModel):
    Services: Optional[Sequence["_ServiceConnectService"]]
    Enabled: Optional[bool]
    LogConfiguration: Optional["_LogConfiguration"]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceConnectConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceConnectConfiguration"]:
        if not json_data:
            return None
        return cls(
            Services=deserialize_list(json_data.get("Services"), ServiceConnectService),
            Enabled=json_data.get("Enabled"),
            LogConfiguration=LogConfiguration._deserialize(json_data.get("LogConfiguration")),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceConnectConfiguration = ServiceConnectConfiguration


@dataclass
class ServiceConnectService(BaseModel):
    IngressPortOverride: Optional[int]
    ClientAliases: Optional[Sequence["_ServiceConnectClientAlias"]]
    DiscoveryName: Optional[str]
    PortName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceConnectService"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceConnectService"]:
        if not json_data:
            return None
        return cls(
            IngressPortOverride=json_data.get("IngressPortOverride"),
            ClientAliases=deserialize_list(json_data.get("ClientAliases"), ServiceConnectClientAlias),
            DiscoveryName=json_data.get("DiscoveryName"),
            PortName=json_data.get("PortName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceConnectService = ServiceConnectService


@dataclass
class ServiceConnectClientAlias(BaseModel):
    DnsName: Optional[str]
    Port: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceConnectClientAlias"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceConnectClientAlias"]:
        if not json_data:
            return None
        return cls(
            DnsName=json_data.get("DnsName"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceConnectClientAlias = ServiceConnectClientAlias


@dataclass
class LogConfiguration(BaseModel):
    SecretOptions: Optional[Sequence["_Secret"]]
    Options: Optional[MutableMapping[str, str]]
    LogDriver: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogConfiguration"]:
        if not json_data:
            return None
        return cls(
            SecretOptions=deserialize_list(json_data.get("SecretOptions"), Secret),
            Options=json_data.get("Options"),
            LogDriver=json_data.get("LogDriver"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogConfiguration = LogConfiguration


@dataclass
class Secret(BaseModel):
    ValueFrom: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Secret"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Secret"]:
        if not json_data:
            return None
        return cls(
            ValueFrom=json_data.get("ValueFrom"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Secret = Secret


@dataclass
class PlacementStrategy(BaseModel):
    Field: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementStrategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementStrategy"]:
        if not json_data:
            return None
        return cls(
            Field=json_data.get("Field"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementStrategy = PlacementStrategy


@dataclass
class DeploymentController(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentController"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentController"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentController = DeploymentController


@dataclass
class ServiceRegistry(BaseModel):
    ContainerName: Optional[str]
    Port: Optional[int]
    ContainerPort: Optional[int]
    RegistryArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceRegistry"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceRegistry"]:
        if not json_data:
            return None
        return cls(
            ContainerName=json_data.get("ContainerName"),
            Port=json_data.get("Port"),
            ContainerPort=json_data.get("ContainerPort"),
            RegistryArn=json_data.get("RegistryArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceRegistry = ServiceRegistry


@dataclass
class CapacityProviderStrategyItem(BaseModel):
    CapacityProvider: Optional[str]
    Base: Optional[int]
    Weight: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityProviderStrategyItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityProviderStrategyItem"]:
        if not json_data:
            return None
        return cls(
            CapacityProvider=json_data.get("CapacityProvider"),
            Base=json_data.get("Base"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityProviderStrategyItem = CapacityProviderStrategyItem


@dataclass
class NetworkConfiguration(BaseModel):
    AwsvpcConfiguration: Optional["_AwsVpcConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkConfiguration"]:
        if not json_data:
            return None
        return cls(
            AwsvpcConfiguration=AwsVpcConfiguration._deserialize(json_data.get("AwsvpcConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkConfiguration = NetworkConfiguration


@dataclass
class AwsVpcConfiguration(BaseModel):
    SecurityGroups: Optional[Sequence[str]]
    Subnets: Optional[Sequence[str]]
    AssignPublicIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsVpcConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsVpcConfiguration"]:
        if not json_data:
            return None
        return cls(
            SecurityGroups=json_data.get("SecurityGroups"),
            Subnets=json_data.get("Subnets"),
            AssignPublicIp=json_data.get("AssignPublicIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsVpcConfiguration = AwsVpcConfiguration


@dataclass
class DeploymentConfiguration(BaseModel):
    Alarms: Optional["_DeploymentAlarms"]
    DeploymentCircuitBreaker: Optional["_DeploymentCircuitBreaker"]
    MaximumPercent: Optional[int]
    MinimumHealthyPercent: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentConfiguration"]:
        if not json_data:
            return None
        return cls(
            Alarms=DeploymentAlarms._deserialize(json_data.get("Alarms")),
            DeploymentCircuitBreaker=DeploymentCircuitBreaker._deserialize(json_data.get("DeploymentCircuitBreaker")),
            MaximumPercent=json_data.get("MaximumPercent"),
            MinimumHealthyPercent=json_data.get("MinimumHealthyPercent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentConfiguration = DeploymentConfiguration


@dataclass
class DeploymentAlarms(BaseModel):
    AlarmNames: Optional[Sequence[str]]
    Enable: Optional[bool]
    Rollback: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentAlarms"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentAlarms"]:
        if not json_data:
            return None
        return cls(
            AlarmNames=json_data.get("AlarmNames"),
            Enable=json_data.get("Enable"),
            Rollback=json_data.get("Rollback"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentAlarms = DeploymentAlarms


@dataclass
class DeploymentCircuitBreaker(BaseModel):
    Enable: Optional[bool]
    Rollback: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentCircuitBreaker"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentCircuitBreaker"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
            Rollback=json_data.get("Rollback"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentCircuitBreaker = DeploymentCircuitBreaker


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


