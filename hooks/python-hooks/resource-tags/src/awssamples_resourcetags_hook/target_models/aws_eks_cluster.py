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
    Logging: Optional["_Logging"]
    EncryptionConfigKeyArn: Optional[str]
    CertificateAuthorityData: Optional[str]
    EncryptionConfig: Optional[Sequence["_EncryptionConfig"]]
    KubernetesNetworkConfig: Optional["_KubernetesNetworkConfig"]
    RoleArn: Optional[str]
    Name: Optional[str]
    Endpoint: Optional[str]
    Version: Optional[str]
    ClusterSecurityGroupId: Optional[str]
    Id: Optional[str]
    OutpostConfig: Optional["_OutpostConfig"]
    Arn: Optional[str]
    ResourcesVpcConfig: Optional["_ResourcesVpcConfig"]
    Tags: Optional[Any]
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
            Logging=Logging._deserialize(json_data.get("Logging")),
            EncryptionConfigKeyArn=json_data.get("EncryptionConfigKeyArn"),
            CertificateAuthorityData=json_data.get("CertificateAuthorityData"),
            EncryptionConfig=deserialize_list(json_data.get("EncryptionConfig"), EncryptionConfig),
            KubernetesNetworkConfig=KubernetesNetworkConfig._deserialize(json_data.get("KubernetesNetworkConfig")),
            RoleArn=json_data.get("RoleArn"),
            Name=json_data.get("Name"),
            Endpoint=json_data.get("Endpoint"),
            Version=json_data.get("Version"),
            ClusterSecurityGroupId=json_data.get("ClusterSecurityGroupId"),
            Id=json_data.get("Id"),
            OutpostConfig=OutpostConfig._deserialize(json_data.get("OutpostConfig")),
            Arn=json_data.get("Arn"),
            ResourcesVpcConfig=ResourcesVpcConfig._deserialize(json_data.get("ResourcesVpcConfig")),
            Tags=json_data.get("Tags"),
            OpenIdConnectIssuerUrl=json_data.get("OpenIdConnectIssuerUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEksCluster = AwsEksCluster


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
class EncryptionConfig(BaseModel):
    Resources: Optional[Sequence[str]]
    Provider: Optional["_Provider"]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfig"]:
        if not json_data:
            return None
        return cls(
            Resources=json_data.get("Resources"),
            Provider=Provider._deserialize(json_data.get("Provider")),
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
class OutpostConfig(BaseModel):
    OutpostArns: Optional[Sequence[str]]
    ControlPlanePlacement: Optional["_ControlPlanePlacement"]
    ControlPlaneInstanceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutpostConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutpostConfig"]:
        if not json_data:
            return None
        return cls(
            OutpostArns=json_data.get("OutpostArns"),
            ControlPlanePlacement=ControlPlanePlacement._deserialize(json_data.get("ControlPlanePlacement")),
            ControlPlaneInstanceType=json_data.get("ControlPlaneInstanceType"),
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
class ResourcesVpcConfig(BaseModel):
    EndpointPublicAccess: Optional[bool]
    PublicAccessCidrs: Optional[Sequence[str]]
    EndpointPrivateAccess: Optional[bool]
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
            EndpointPublicAccess=json_data.get("EndpointPublicAccess"),
            PublicAccessCidrs=json_data.get("PublicAccessCidrs"),
            EndpointPrivateAccess=json_data.get("EndpointPrivateAccess"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourcesVpcConfig = ResourcesVpcConfig


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


