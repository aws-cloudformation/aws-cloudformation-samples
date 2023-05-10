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
class AwsEksCluster(BaseModel):
    EncryptionConfig: Optional[Sequence["_EncryptionConfig"]]
    KubernetesNetworkConfig: Optional["_KubernetesNetworkConfig"]
    Logging: Optional["_Logging"]
    Name: Optional[str]
    Id: Optional[str]
    ResourcesVpcConfig: Optional["_ResourcesVpcConfig"]
    OutpostConfig: Optional["_OutpostConfig"]
    RoleArn: Optional[str]
    Version: Optional[str]
    Tags: Optional[Any]
    Arn: Optional[str]
    Endpoint: Optional[str]
    CertificateAuthorityData: Optional[str]
    ClusterSecurityGroupId: Optional[str]
    EncryptionConfigKeyArn: Optional[str]
    OpenIdConnectIssuerUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEksCluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEksCluster"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            EncryptionConfig=deserialize_list(json_data.get("EncryptionConfig"), EncryptionConfig),
            KubernetesNetworkConfig=KubernetesNetworkConfig._deserialize(json_data.get("KubernetesNetworkConfig")),
            Logging=Logging._deserialize(json_data.get("Logging")),
            Name=json_data.get("Name"),
            Id=json_data.get("Id"),
            ResourcesVpcConfig=ResourcesVpcConfig._deserialize(json_data.get("ResourcesVpcConfig")),
            OutpostConfig=OutpostConfig._deserialize(json_data.get("OutpostConfig")),
            RoleArn=json_data.get("RoleArn"),
            Version=json_data.get("Version"),
            Tags=json_data.get("Tags"),
            Arn=json_data.get("Arn"),
            Endpoint=json_data.get("Endpoint"),
            CertificateAuthorityData=json_data.get("CertificateAuthorityData"),
            ClusterSecurityGroupId=json_data.get("ClusterSecurityGroupId"),
            EncryptionConfigKeyArn=json_data.get("EncryptionConfigKeyArn"),
            OpenIdConnectIssuerUrl=json_data.get("OpenIdConnectIssuerUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEksCluster = AwsEksCluster


@dataclass
class EncryptionConfig(BaseModel):
    Provider: Optional["_Provider"]
    Resources: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfig"]:
        if not json_data:
            return None
        return cls(
            Provider=Provider._deserialize(json_data.get("Provider")),
            Resources=json_data.get("Resources"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfig = EncryptionConfig


@dataclass
class Provider(BaseModel):
    KeyArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Provider"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Provider"]:
        if not json_data:
            return None
        return cls(
            KeyArn=json_data.get("KeyArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Provider = Provider


@dataclass
class KubernetesNetworkConfig(BaseModel):
    ServiceIpv4Cidr: Optional[str]
    ServiceIpv6Cidr: Optional[str]
    IpFamily: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubernetesNetworkConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubernetesNetworkConfig"]:
        if not json_data:
            return None
        return cls(
            ServiceIpv4Cidr=json_data.get("ServiceIpv4Cidr"),
            ServiceIpv6Cidr=json_data.get("ServiceIpv6Cidr"),
            IpFamily=json_data.get("IpFamily"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubernetesNetworkConfig = KubernetesNetworkConfig


@dataclass
class Logging(BaseModel):
    ClusterLogging: Optional["_ClusterLogging"]

    @classmethod
    def _deserialize(
        cls: Type["_Logging"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Logging"]:
        if not json_data:
            return None
        return cls(
            ClusterLogging=ClusterLogging._deserialize(json_data.get("ClusterLogging")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Logging = Logging


@dataclass
class ClusterLogging(BaseModel):
    EnabledTypes: Optional[Sequence["_LoggingTypeConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterLogging"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterLogging"]:
        if not json_data:
            return None
        return cls(
            EnabledTypes=deserialize_list(json_data.get("EnabledTypes"), LoggingTypeConfig),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterLogging = ClusterLogging


@dataclass
class LoggingTypeConfig(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingTypeConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingTypeConfig"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingTypeConfig = LoggingTypeConfig


@dataclass
class ResourcesVpcConfig(BaseModel):
    EndpointPrivateAccess: Optional[bool]
    EndpointPublicAccess: Optional[bool]
    PublicAccessCidrs: Optional[Sequence[str]]
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourcesVpcConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourcesVpcConfig"]:
        if not json_data:
            return None
        return cls(
            EndpointPrivateAccess=json_data.get("EndpointPrivateAccess"),
            EndpointPublicAccess=json_data.get("EndpointPublicAccess"),
            PublicAccessCidrs=json_data.get("PublicAccessCidrs"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourcesVpcConfig = ResourcesVpcConfig


@dataclass
class OutpostConfig(BaseModel):
    OutpostArns: Optional[Sequence[str]]
    ControlPlaneInstanceType: Optional[str]
    ControlPlanePlacement: Optional["_ControlPlanePlacement"]

    @classmethod
    def _deserialize(
        cls: Type["_OutpostConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutpostConfig"]:
        if not json_data:
            return None
        return cls(
            OutpostArns=json_data.get("OutpostArns"),
            ControlPlaneInstanceType=json_data.get("ControlPlaneInstanceType"),
            ControlPlanePlacement=ControlPlanePlacement._deserialize(json_data.get("ControlPlanePlacement")),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutpostConfig = OutpostConfig


@dataclass
class ControlPlanePlacement(BaseModel):
    GroupName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ControlPlanePlacement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ControlPlanePlacement"]:
        if not json_data:
            return None
        return cls(
            GroupName=json_data.get("GroupName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ControlPlanePlacement = ControlPlanePlacement


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


