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
class AwsApigatewayv2Domainname(BaseModel):
    MutualTlsAuthentication: Optional["_MutualTlsAuthentication"]
    RegionalHostedZoneId: Optional[str]
    RegionalDomainName: Optional[str]
    DomainName: Optional[str]
    DomainNameConfigurations: Optional[Sequence["_DomainNameConfiguration"]]
    Id: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayv2Domainname"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayv2Domainname"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            MutualTlsAuthentication=MutualTlsAuthentication._deserialize(json_data.get("MutualTlsAuthentication")),
            RegionalHostedZoneId=json_data.get("RegionalHostedZoneId"),
            RegionalDomainName=json_data.get("RegionalDomainName"),
            DomainName=json_data.get("DomainName"),
            DomainNameConfigurations=deserialize_list(json_data.get("DomainNameConfigurations"), DomainNameConfiguration),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayv2Domainname = AwsApigatewayv2Domainname


@dataclass
class MutualTlsAuthentication(BaseModel):
    TruststoreVersion: Optional[str]
    TruststoreUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MutualTlsAuthentication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MutualTlsAuthentication"]:
        if not json_data:
            return None
        return cls(
            TruststoreVersion=json_data.get("TruststoreVersion"),
            TruststoreUri=json_data.get("TruststoreUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MutualTlsAuthentication = MutualTlsAuthentication


@dataclass
class DomainNameConfiguration(BaseModel):
    OwnershipVerificationCertificateArn: Optional[str]
    EndpointType: Optional[str]
    CertificateName: Optional[str]
    SecurityPolicy: Optional[str]
    CertificateArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DomainNameConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainNameConfiguration"]:
        if not json_data:
            return None
        return cls(
            OwnershipVerificationCertificateArn=json_data.get("OwnershipVerificationCertificateArn"),
            EndpointType=json_data.get("EndpointType"),
            CertificateName=json_data.get("CertificateName"),
            SecurityPolicy=json_data.get("SecurityPolicy"),
            CertificateArn=json_data.get("CertificateArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainNameConfiguration = DomainNameConfiguration


