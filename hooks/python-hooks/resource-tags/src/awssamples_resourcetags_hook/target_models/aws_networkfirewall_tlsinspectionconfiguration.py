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
class AwsNetworkfirewallTlsinspectionconfiguration(BaseModel):
    TLSInspectionConfigurationName: Optional[str]
    TLSInspectionConfigurationArn: Optional[str]
    TLSInspectionConfiguration: Optional["_TLSInspectionConfiguration"]
    TLSInspectionConfigurationId: Optional[str]
    Description: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsNetworkfirewallTlsinspectionconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsNetworkfirewallTlsinspectionconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            TLSInspectionConfigurationName=json_data.get("TLSInspectionConfigurationName"),
            TLSInspectionConfigurationArn=json_data.get("TLSInspectionConfigurationArn"),
            TLSInspectionConfiguration=TLSInspectionConfiguration._deserialize(json_data.get("TLSInspectionConfiguration")),
            TLSInspectionConfigurationId=json_data.get("TLSInspectionConfigurationId"),
            Description=json_data.get("Description"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsNetworkfirewallTlsinspectionconfiguration = AwsNetworkfirewallTlsinspectionconfiguration


@dataclass
class TLSInspectionConfiguration(BaseModel):
    ServerCertificateConfigurations: Optional[Sequence["_ServerCertificateConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_TLSInspectionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TLSInspectionConfiguration"]:
        if not json_data:
            return None
        return cls(
            ServerCertificateConfigurations=deserialize_list(json_data.get("ServerCertificateConfigurations"), ServerCertificateConfiguration),
        )


# work around possible type aliasing issues when variable has same name as a model
_TLSInspectionConfiguration = TLSInspectionConfiguration


@dataclass
class ServerCertificateConfiguration(BaseModel):
    ServerCertificates: Optional[AbstractSet["_ServerCertificate"]]
    Scopes: Optional[Sequence["_ServerCertificateScope"]]
    CertificateAuthorityArn: Optional[str]
    CheckCertificateRevocationStatus: Optional["_CheckCertificateRevocationStatus"]

    @classmethod
    def _deserialize(
        cls: Type["_ServerCertificateConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerCertificateConfiguration"]:
        if not json_data:
            return None
        return cls(
            ServerCertificates=set_or_none(json_data.get("ServerCertificates")),
            Scopes=deserialize_list(json_data.get("Scopes"), ServerCertificateScope),
            CertificateAuthorityArn=json_data.get("CertificateAuthorityArn"),
            CheckCertificateRevocationStatus=CheckCertificateRevocationStatus._deserialize(json_data.get("CheckCertificateRevocationStatus")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerCertificateConfiguration = ServerCertificateConfiguration


@dataclass
class ServerCertificate(BaseModel):
    ResourceArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerCertificate"]:
        if not json_data:
            return None
        return cls(
            ResourceArn=json_data.get("ResourceArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerCertificate = ServerCertificate


@dataclass
class ServerCertificateScope(BaseModel):
    Sources: Optional[Sequence["_Address"]]
    Destinations: Optional[Sequence["_Address"]]
    SourcePorts: Optional[Sequence["_PortRange"]]
    DestinationPorts: Optional[Sequence["_PortRange"]]
    Protocols: Optional[Sequence[int]]

    @classmethod
    def _deserialize(
        cls: Type["_ServerCertificateScope"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerCertificateScope"]:
        if not json_data:
            return None
        return cls(
            Sources=deserialize_list(json_data.get("Sources"), Address),
            Destinations=deserialize_list(json_data.get("Destinations"), Address),
            SourcePorts=deserialize_list(json_data.get("SourcePorts"), PortRange),
            DestinationPorts=deserialize_list(json_data.get("DestinationPorts"), PortRange),
            Protocols=json_data.get("Protocols"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerCertificateScope = ServerCertificateScope


@dataclass
class Address(BaseModel):
    AddressDefinition: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Address"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Address"]:
        if not json_data:
            return None
        return cls(
            AddressDefinition=json_data.get("AddressDefinition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Address = Address


@dataclass
class PortRange(BaseModel):
    FromPort: Optional[int]
    ToPort: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_PortRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortRange"]:
        if not json_data:
            return None
        return cls(
            FromPort=json_data.get("FromPort"),
            ToPort=json_data.get("ToPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortRange = PortRange


@dataclass
class CheckCertificateRevocationStatus(BaseModel):
    RevokedStatusAction: Optional[str]
    UnknownStatusAction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CheckCertificateRevocationStatus"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CheckCertificateRevocationStatus"]:
        if not json_data:
            return None
        return cls(
            RevokedStatusAction=json_data.get("RevokedStatusAction"),
            UnknownStatusAction=json_data.get("UnknownStatusAction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CheckCertificateRevocationStatus = CheckCertificateRevocationStatus


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


