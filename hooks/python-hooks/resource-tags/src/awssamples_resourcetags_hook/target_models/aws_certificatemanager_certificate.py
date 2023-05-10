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
class AwsCertificatemanagerCertificate(BaseModel):
    CertificateAuthorityArn: Optional[str]
    DomainValidationOptions: Optional[Sequence["_DomainValidationOption"]]
    CertificateTransparencyLoggingPreference: Optional[str]
    DomainName: Optional[str]
    ValidationMethod: Optional[str]
    SubjectAlternativeNames: Optional[Sequence[str]]
    Id: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCertificatemanagerCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCertificatemanagerCertificate"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CertificateAuthorityArn=json_data.get("CertificateAuthorityArn"),
            DomainValidationOptions=deserialize_list(json_data.get("DomainValidationOptions"), DomainValidationOption),
            CertificateTransparencyLoggingPreference=json_data.get("CertificateTransparencyLoggingPreference"),
            DomainName=json_data.get("DomainName"),
            ValidationMethod=json_data.get("ValidationMethod"),
            SubjectAlternativeNames=json_data.get("SubjectAlternativeNames"),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCertificatemanagerCertificate = AwsCertificatemanagerCertificate


@dataclass
class DomainValidationOption(BaseModel):
    DomainName: Optional[str]
    ValidationDomain: Optional[str]
    HostedZoneId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DomainValidationOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainValidationOption"]:
        if not json_data:
            return None
        return cls(
            DomainName=json_data.get("DomainName"),
            ValidationDomain=json_data.get("ValidationDomain"),
            HostedZoneId=json_data.get("HostedZoneId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainValidationOption = DomainValidationOption


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


