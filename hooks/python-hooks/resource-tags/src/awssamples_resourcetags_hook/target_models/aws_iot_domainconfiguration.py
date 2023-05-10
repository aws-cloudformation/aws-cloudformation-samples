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
class AwsIotDomainconfiguration(BaseModel):
    DomainConfigurationName: Optional[str]
    AuthorizerConfig: Optional["_AuthorizerConfig"]
    DomainName: Optional[str]
    ServerCertificateArns: Optional[Sequence[str]]
    ServiceType: Optional[str]
    ValidationCertificateArn: Optional[str]
    Arn: Optional[str]
    DomainConfigurationStatus: Optional[str]
    DomainType: Optional[str]
    ServerCertificates: Optional[Sequence["_ServerCertificateSummary"]]
    TlsConfig: Optional["_TlsConfig"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotDomainconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotDomainconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DomainConfigurationName=json_data.get("DomainConfigurationName"),
            AuthorizerConfig=AuthorizerConfig._deserialize(json_data.get("AuthorizerConfig")),
            DomainName=json_data.get("DomainName"),
            ServerCertificateArns=json_data.get("ServerCertificateArns"),
            ServiceType=json_data.get("ServiceType"),
            ValidationCertificateArn=json_data.get("ValidationCertificateArn"),
            Arn=json_data.get("Arn"),
            DomainConfigurationStatus=json_data.get("DomainConfigurationStatus"),
            DomainType=json_data.get("DomainType"),
            ServerCertificates=deserialize_list(json_data.get("ServerCertificates"), ServerCertificateSummary),
            TlsConfig=TlsConfig._deserialize(json_data.get("TlsConfig")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotDomainconfiguration = AwsIotDomainconfiguration


@dataclass
class AuthorizerConfig(BaseModel):
    AllowAuthorizerOverride: Optional[bool]
    DefaultAuthorizerName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthorizerConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthorizerConfig"]:
        if not json_data:
            return None
        return cls(
            AllowAuthorizerOverride=json_data.get("AllowAuthorizerOverride"),
            DefaultAuthorizerName=json_data.get("DefaultAuthorizerName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthorizerConfig = AuthorizerConfig


@dataclass
class ServerCertificateSummary(BaseModel):
    ServerCertificateArn: Optional[str]
    ServerCertificateStatus: Optional[str]
    ServerCertificateStatusDetail: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerCertificateSummary"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerCertificateSummary"]:
        if not json_data:
            return None
        return cls(
            ServerCertificateArn=json_data.get("ServerCertificateArn"),
            ServerCertificateStatus=json_data.get("ServerCertificateStatus"),
            ServerCertificateStatusDetail=json_data.get("ServerCertificateStatusDetail"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerCertificateSummary = ServerCertificateSummary


@dataclass
class TlsConfig(BaseModel):
    SecurityPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TlsConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsConfig"]:
        if not json_data:
            return None
        return cls(
            SecurityPolicy=json_data.get("SecurityPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsConfig = TlsConfig


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


