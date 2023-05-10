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
class AwsApigatewayDomainname(BaseModel):
    DomainName: Optional[str]
    DistributionDomainName: Optional[str]
    DistributionHostedZoneId: Optional[str]
    EndpointConfiguration: Optional["_EndpointConfiguration"]
    MutualTlsAuthentication: Optional["_MutualTlsAuthentication"]
    RegionalDomainName: Optional[str]
    RegionalHostedZoneId: Optional[str]
    CertificateArn: Optional[str]
    RegionalCertificateArn: Optional[str]
    OwnershipVerificationCertificateArn: Optional[str]
    SecurityPolicy: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayDomainname"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayDomainname"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DomainName=json_data.get("DomainName"),
            DistributionDomainName=json_data.get("DistributionDomainName"),
            DistributionHostedZoneId=json_data.get("DistributionHostedZoneId"),
            EndpointConfiguration=EndpointConfiguration._deserialize(json_data.get("EndpointConfiguration")),
            MutualTlsAuthentication=MutualTlsAuthentication._deserialize(json_data.get("MutualTlsAuthentication")),
            RegionalDomainName=json_data.get("RegionalDomainName"),
            RegionalHostedZoneId=json_data.get("RegionalHostedZoneId"),
            CertificateArn=json_data.get("CertificateArn"),
            RegionalCertificateArn=json_data.get("RegionalCertificateArn"),
            OwnershipVerificationCertificateArn=json_data.get("OwnershipVerificationCertificateArn"),
            SecurityPolicy=json_data.get("SecurityPolicy"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayDomainname = AwsApigatewayDomainname


@dataclass
class EndpointConfiguration(BaseModel):
    Types: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointConfiguration"]:
        if not json_data:
            return None
        return cls(
            Types=json_data.get("Types"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointConfiguration = EndpointConfiguration


@dataclass
class MutualTlsAuthentication(BaseModel):
    TruststoreUri: Optional[str]
    TruststoreVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MutualTlsAuthentication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MutualTlsAuthentication"]:
        if not json_data:
            return None
        return cls(
            TruststoreUri=json_data.get("TruststoreUri"),
            TruststoreVersion=json_data.get("TruststoreVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MutualTlsAuthentication = MutualTlsAuthentication


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


