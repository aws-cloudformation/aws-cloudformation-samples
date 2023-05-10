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
class AwsEc2Clientvpnendpoint(BaseModel):
    ClientCidrBlock: Optional[str]
    ClientConnectOptions: Optional["_ClientConnectOptions"]
    Description: Optional[str]
    TagSpecifications: Optional[Sequence["_TagSpecification"]]
    AuthenticationOptions: Optional[Sequence["_ClientAuthenticationRequest"]]
    ServerCertificateArn: Optional[str]
    SessionTimeoutHours: Optional[int]
    DnsServers: Optional[Sequence[str]]
    SecurityGroupIds: Optional[Sequence[str]]
    ConnectionLogOptions: Optional["_ConnectionLogOptions"]
    SplitTunnel: Optional[bool]
    ClientLoginBannerOptions: Optional["_ClientLoginBannerOptions"]
    VpcId: Optional[str]
    SelfServicePortal: Optional[str]
    TransportProtocol: Optional[str]
    Id: Optional[str]
    VpnPort: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Clientvpnendpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Clientvpnendpoint"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ClientCidrBlock=json_data.get("ClientCidrBlock"),
            ClientConnectOptions=ClientConnectOptions._deserialize(json_data.get("ClientConnectOptions")),
            Description=json_data.get("Description"),
            TagSpecifications=deserialize_list(json_data.get("TagSpecifications"), TagSpecification),
            AuthenticationOptions=deserialize_list(json_data.get("AuthenticationOptions"), ClientAuthenticationRequest),
            ServerCertificateArn=json_data.get("ServerCertificateArn"),
            SessionTimeoutHours=json_data.get("SessionTimeoutHours"),
            DnsServers=json_data.get("DnsServers"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            ConnectionLogOptions=ConnectionLogOptions._deserialize(json_data.get("ConnectionLogOptions")),
            SplitTunnel=json_data.get("SplitTunnel"),
            ClientLoginBannerOptions=ClientLoginBannerOptions._deserialize(json_data.get("ClientLoginBannerOptions")),
            VpcId=json_data.get("VpcId"),
            SelfServicePortal=json_data.get("SelfServicePortal"),
            TransportProtocol=json_data.get("TransportProtocol"),
            Id=json_data.get("Id"),
            VpnPort=json_data.get("VpnPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Clientvpnendpoint = AwsEc2Clientvpnendpoint


@dataclass
class ClientConnectOptions(BaseModel):
    Enabled: Optional[bool]
    LambdaFunctionArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientConnectOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientConnectOptions"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            LambdaFunctionArn=json_data.get("LambdaFunctionArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientConnectOptions = ClientConnectOptions


@dataclass
class TagSpecification(BaseModel):
    ResourceType: Optional[str]
    Tags: Optional[Sequence["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_TagSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagSpecification"]:
        if not json_data:
            return None
        return cls(
            ResourceType=json_data.get("ResourceType"),
            Tags=deserialize_list(json_data.get("Tags"), Tag),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagSpecification = TagSpecification


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
class ClientAuthenticationRequest(BaseModel):
    MutualAuthentication: Optional["_CertificateAuthenticationRequest"]
    Type: Optional[str]
    ActiveDirectory: Optional["_DirectoryServiceAuthenticationRequest"]
    FederatedAuthentication: Optional["_FederatedAuthenticationRequest"]

    @classmethod
    def _deserialize(
        cls: Type["_ClientAuthenticationRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientAuthenticationRequest"]:
        if not json_data:
            return None
        return cls(
            MutualAuthentication=CertificateAuthenticationRequest._deserialize(json_data.get("MutualAuthentication")),
            Type=json_data.get("Type"),
            ActiveDirectory=DirectoryServiceAuthenticationRequest._deserialize(json_data.get("ActiveDirectory")),
            FederatedAuthentication=FederatedAuthenticationRequest._deserialize(json_data.get("FederatedAuthentication")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientAuthenticationRequest = ClientAuthenticationRequest


@dataclass
class CertificateAuthenticationRequest(BaseModel):
    ClientRootCertificateChainArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateAuthenticationRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateAuthenticationRequest"]:
        if not json_data:
            return None
        return cls(
            ClientRootCertificateChainArn=json_data.get("ClientRootCertificateChainArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateAuthenticationRequest = CertificateAuthenticationRequest


@dataclass
class DirectoryServiceAuthenticationRequest(BaseModel):
    DirectoryId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DirectoryServiceAuthenticationRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DirectoryServiceAuthenticationRequest"]:
        if not json_data:
            return None
        return cls(
            DirectoryId=json_data.get("DirectoryId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DirectoryServiceAuthenticationRequest = DirectoryServiceAuthenticationRequest


@dataclass
class FederatedAuthenticationRequest(BaseModel):
    SAMLProviderArn: Optional[str]
    SelfServiceSAMLProviderArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FederatedAuthenticationRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FederatedAuthenticationRequest"]:
        if not json_data:
            return None
        return cls(
            SAMLProviderArn=json_data.get("SAMLProviderArn"),
            SelfServiceSAMLProviderArn=json_data.get("SelfServiceSAMLProviderArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FederatedAuthenticationRequest = FederatedAuthenticationRequest


@dataclass
class ConnectionLogOptions(BaseModel):
    Enabled: Optional[bool]
    CloudwatchLogGroup: Optional[str]
    CloudwatchLogStream: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionLogOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionLogOptions"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            CloudwatchLogGroup=json_data.get("CloudwatchLogGroup"),
            CloudwatchLogStream=json_data.get("CloudwatchLogStream"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionLogOptions = ConnectionLogOptions


@dataclass
class ClientLoginBannerOptions(BaseModel):
    Enabled: Optional[bool]
    BannerText: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientLoginBannerOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientLoginBannerOptions"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            BannerText=json_data.get("BannerText"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientLoginBannerOptions = ClientLoginBannerOptions


