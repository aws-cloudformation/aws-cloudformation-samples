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
    ServiceArn: Optional[str]
    CapacityProviderStrategy: Optional[Sequence["_CapacityProviderStrategyItem"]]
    Cluster: Optional[str]
    DeploymentConfiguration: Optional["_DeploymentConfiguration"]
    DeploymentController: Optional["_DeploymentController"]
    DesiredCount: Optional[int]
    EnableECSManagedTags: Optional[bool]
    EnableExecuteCommand: Optional[bool]
    HealthCheckGracePeriodSeconds: Optional[int]
    LaunchType: Optional[str]
    LoadBalancers: Optional[Sequence["_LoadBalancer"]]
    Name: Optional[str]
    NetworkConfiguration: Optional["_NetworkConfiguration"]
    PlacementConstraints: Optional[Sequence["_PlacementConstraint"]]
    PlacementStrategies: Optional[Sequence["_PlacementStrategy"]]
    PlatformVersion: Optional[str]
    PropagateTags: Optional[str]
    Role: Optional[str]
    SchedulingStrategy: Optional[str]
    ServiceConnectConfiguration: Optional["_ServiceConnectConfiguration"]
    ServiceName: Optional[str]
    ServiceRegistries: Optional[Sequence["_ServiceRegistry"]]
    Tags: Optional[Any]
    TaskDefinition: Optional[str]

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
            ServiceArn=json_data.get("ServiceArn"),
            CapacityProviderStrategy=deserialize_list(json_data.get("CapacityProviderStrategy"), CapacityProviderStrategyItem),
            Cluster=json_data.get("Cluster"),
            DeploymentConfiguration=DeploymentConfiguration._deserialize(json_data.get("DeploymentConfiguration")),
            DeploymentController=DeploymentController._deserialize(json_data.get("DeploymentController")),
            DesiredCount=json_data.get("DesiredCount"),
            EnableECSManagedTags=json_data.get("EnableECSManagedTags"),
            EnableExecuteCommand=json_data.get("EnableExecuteCommand"),
            HealthCheckGracePeriodSeconds=json_data.get("HealthCheckGracePeriodSeconds"),
            LaunchType=json_data.get("LaunchType"),
            LoadBalancers=deserialize_list(json_data.get("LoadBalancers"), LoadBalancer),
            Name=json_data.get("Name"),
            NetworkConfiguration=NetworkConfiguration._deserialize(json_data.get("NetworkConfiguration")),
            PlacementConstraints=deserialize_list(json_data.get("PlacementConstraints"), PlacementConstraint),
            PlacementStrategies=deserialize_list(json_data.get("PlacementStrategies"), PlacementStrategy),
            PlatformVersion=json_data.get("PlatformVersion"),
            PropagateTags=json_data.get("PropagateTags"),
            Role=json_data.get("Role"),
            SchedulingStrategy=json_data.get("SchedulingStrategy"),
            ServiceConnectConfiguration=ServiceConnectConfiguration._deserialize(json_data.get("ServiceConnectConfiguration")),
            ServiceName=json_data.get("ServiceName"),
            ServiceRegistries=deserialize_list(json_data.get("ServiceRegistries"), ServiceRegistry),
            Tags=json_data.get("Tags"),
            TaskDefinition=json_data.get("TaskDefinition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEcsService = AwsEcsService


@dataclass
class CapacityProviderStrategyItem(BaseModel):
    Base: Optional[int]
    CapacityProvider: Optional[str]
    Weight: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityProviderStrategyItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityProviderStrategyItem"]:
        if not json_data:
            return None
        return cls(
            Base=json_data.get("Base"),
            CapacityProvider=json_data.get("CapacityProvider"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityProviderStrategyItem = CapacityProviderStrategyItem


@dataclass
class DeploymentConfiguration(BaseModel):
    DeploymentCircuitBreaker: Optional["_DeploymentCircuitBreaker"]
    MaximumPercent: Optional[int]
    MinimumHealthyPercent: Optional[int]
    Alarms: Optional["_DeploymentAlarms"]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentConfiguration"]:
        if not json_data:
            return None
        return cls(
            DeploymentCircuitBreaker=DeploymentCircuitBreaker._deserialize(json_data.get("DeploymentCircuitBreaker")),
            MaximumPercent=json_data.get("MaximumPercent"),
            MinimumHealthyPercent=json_data.get("MinimumHealthyPercent"),
            Alarms=DeploymentAlarms._deserialize(json_data.get("Alarms")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentConfiguration = DeploymentConfiguration


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
class DeploymentAlarms(BaseModel):
    AlarmNames: Optional[Sequence[str]]
    Rollback: Optional[bool]
    Enable: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentAlarms"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentAlarms"]:
        if not json_data:
            return None
        return cls(
            AlarmNames=json_data.get("AlarmNames"),
            Rollback=json_data.get("Rollback"),
            Enable=json_data.get("Enable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentAlarms = DeploymentAlarms


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
class LoadBalancer(BaseModel):
    ContainerName: Optional[str]
    ContainerPort: Optional[int]
    LoadBalancerName: Optional[str]
    TargetGroupArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancer"]:
        if not json_data:
            return None
        return cls(
            ContainerName=json_data.get("ContainerName"),
            ContainerPort=json_data.get("ContainerPort"),
            LoadBalancerName=json_data.get("LoadBalancerName"),
            TargetGroupArn=json_data.get("TargetGroupArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancer = LoadBalancer


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
    AssignPublicIp: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    Subnets: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsVpcConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsVpcConfiguration"]:
        if not json_data:
            return None
        return cls(
            AssignPublicIp=json_data.get("AssignPublicIp"),
            SecurityGroups=json_data.get("SecurityGroups"),
            Subnets=json_data.get("Subnets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsVpcConfiguration = AwsVpcConfiguration


@dataclass
class PlacementConstraint(BaseModel):
    Expression: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementConstraint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementConstraint"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementConstraint = PlacementConstraint


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
class ServiceConnectConfiguration(BaseModel):
    Enabled: Optional[bool]
    Namespace: Optional[str]
    Services: Optional[Sequence["_ServiceConnectService"]]
    LogConfiguration: Optional["_LogConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceConnectConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceConnectConfiguration"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Namespace=json_data.get("Namespace"),
            Services=deserialize_list(json_data.get("Services"), ServiceConnectService),
            LogConfiguration=LogConfiguration._deserialize(json_data.get("LogConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceConnectConfiguration = ServiceConnectConfiguration


@dataclass
class ServiceConnectService(BaseModel):
    PortName: Optional[str]
    DiscoveryName: Optional[str]
    ClientAliases: Optional[Sequence["_ServiceConnectClientAlias"]]
    IngressPortOverride: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceConnectService"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceConnectService"]:
        if not json_data:
            return None
        return cls(
            PortName=json_data.get("PortName"),
            DiscoveryName=json_data.get("DiscoveryName"),
            ClientAliases=deserialize_list(json_data.get("ClientAliases"), ServiceConnectClientAlias),
            IngressPortOverride=json_data.get("IngressPortOverride"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceConnectService = ServiceConnectService


@dataclass
class ServiceConnectClientAlias(BaseModel):
    Port: Optional[int]
    DnsName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceConnectClientAlias"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceConnectClientAlias"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            DnsName=json_data.get("DnsName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceConnectClientAlias = ServiceConnectClientAlias


@dataclass
class LogConfiguration(BaseModel):
    LogDriver: Optional[str]
    Options: Optional[MutableMapping[str, str]]
    SecretOptions: Optional[Sequence["_Secret"]]

    @classmethod
    def _deserialize(
        cls: Type["_LogConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogConfiguration"]:
        if not json_data:
            return None
        return cls(
            LogDriver=json_data.get("LogDriver"),
            Options=json_data.get("Options"),
            SecretOptions=deserialize_list(json_data.get("SecretOptions"), Secret),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogConfiguration = LogConfiguration


@dataclass
class Secret(BaseModel):
    Name: Optional[str]
    ValueFrom: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Secret"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Secret"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            ValueFrom=json_data.get("ValueFrom"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Secret = Secret


@dataclass
class ServiceRegistry(BaseModel):
    ContainerName: Optional[str]
    ContainerPort: Optional[int]
    Port: Optional[int]
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
            ContainerPort=json_data.get("ContainerPort"),
            Port=json_data.get("Port"),
            RegistryArn=json_data.get("RegistryArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceRegistry = ServiceRegistry


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


