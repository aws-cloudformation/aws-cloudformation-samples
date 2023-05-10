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
class AwsLightsailContainer(BaseModel):
    ServiceName: Optional[str]
    Power: Optional[str]
    ContainerArn: Optional[str]
    Scale: Optional[int]
    PublicDomainNames: Optional[AbstractSet["_PublicDomainName"]]
    ContainerServiceDeployment: Optional["_ContainerServiceDeployment"]
    IsDisabled: Optional[bool]
    Url: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLightsailContainer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLightsailContainer"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ServiceName=json_data.get("ServiceName"),
            Power=json_data.get("Power"),
            ContainerArn=json_data.get("ContainerArn"),
            Scale=json_data.get("Scale"),
            PublicDomainNames=set_or_none(json_data.get("PublicDomainNames")),
            ContainerServiceDeployment=ContainerServiceDeployment._deserialize(json_data.get("ContainerServiceDeployment")),
            IsDisabled=json_data.get("IsDisabled"),
            Url=json_data.get("Url"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLightsailContainer = AwsLightsailContainer


@dataclass
class PublicDomainName(BaseModel):
    CertificateName: Optional[str]
    DomainNames: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PublicDomainName"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicDomainName"]:
        if not json_data:
            return None
        return cls(
            CertificateName=json_data.get("CertificateName"),
            DomainNames=set_or_none(json_data.get("DomainNames")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicDomainName = PublicDomainName


@dataclass
class ContainerServiceDeployment(BaseModel):
    Containers: Optional[AbstractSet["_Container"]]
    PublicEndpoint: Optional["_PublicEndpoint"]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerServiceDeployment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerServiceDeployment"]:
        if not json_data:
            return None
        return cls(
            Containers=set_or_none(json_data.get("Containers")),
            PublicEndpoint=PublicEndpoint._deserialize(json_data.get("PublicEndpoint")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerServiceDeployment = ContainerServiceDeployment


@dataclass
class Container(BaseModel):
    ContainerName: Optional[str]
    Command: Optional[AbstractSet[str]]
    Environment: Optional[AbstractSet["_EnvironmentVariable"]]
    Image: Optional[str]
    Ports: Optional[AbstractSet["_PortInfo"]]

    @classmethod
    def _deserialize(
        cls: Type["_Container"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Container"]:
        if not json_data:
            return None
        return cls(
            ContainerName=json_data.get("ContainerName"),
            Command=set_or_none(json_data.get("Command")),
            Environment=set_or_none(json_data.get("Environment")),
            Image=json_data.get("Image"),
            Ports=set_or_none(json_data.get("Ports")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Container = Container


@dataclass
class EnvironmentVariable(BaseModel):
    Variable: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentVariable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentVariable"]:
        if not json_data:
            return None
        return cls(
            Variable=json_data.get("Variable"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentVariable = EnvironmentVariable


@dataclass
class PortInfo(BaseModel):
    Port: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PortInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortInfo"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortInfo = PortInfo


@dataclass
class PublicEndpoint(BaseModel):
    ContainerName: Optional[str]
    ContainerPort: Optional[int]
    HealthCheckConfig: Optional["_HealthCheckConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_PublicEndpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicEndpoint"]:
        if not json_data:
            return None
        return cls(
            ContainerName=json_data.get("ContainerName"),
            ContainerPort=json_data.get("ContainerPort"),
            HealthCheckConfig=HealthCheckConfig._deserialize(json_data.get("HealthCheckConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicEndpoint = PublicEndpoint


@dataclass
class HealthCheckConfig(BaseModel):
    HealthyThreshold: Optional[int]
    IntervalSeconds: Optional[int]
    Path: Optional[str]
    SuccessCodes: Optional[str]
    TimeoutSeconds: Optional[int]
    UnhealthyThreshold: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckConfig"]:
        if not json_data:
            return None
        return cls(
            HealthyThreshold=json_data.get("HealthyThreshold"),
            IntervalSeconds=json_data.get("IntervalSeconds"),
            Path=json_data.get("Path"),
            SuccessCodes=json_data.get("SuccessCodes"),
            TimeoutSeconds=json_data.get("TimeoutSeconds"),
            UnhealthyThreshold=json_data.get("UnhealthyThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckConfig = HealthCheckConfig


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


