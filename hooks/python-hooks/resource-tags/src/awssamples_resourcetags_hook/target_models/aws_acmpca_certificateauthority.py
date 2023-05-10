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
class AwsAcmpcaCertificateauthority(BaseModel):
    Arn: Optional[str]
    Type: Optional[str]
    KeyAlgorithm: Optional[str]
    SigningAlgorithm: Optional[str]
    Subject: Optional["_Subject"]
    RevocationConfiguration: Optional["_RevocationConfiguration"]
    Tags: Optional[Any]
    CertificateSigningRequest: Optional[str]
    CsrExtensions: Optional["_CsrExtensions"]
    KeyStorageSecurityStandard: Optional[str]
    UsageMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAcmpcaCertificateauthority"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAcmpcaCertificateauthority"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Type=json_data.get("Type"),
            KeyAlgorithm=json_data.get("KeyAlgorithm"),
            SigningAlgorithm=json_data.get("SigningAlgorithm"),
            Subject=Subject._deserialize(json_data.get("Subject")),
            RevocationConfiguration=RevocationConfiguration._deserialize(json_data.get("RevocationConfiguration")),
            Tags=json_data.get("Tags"),
            CertificateSigningRequest=json_data.get("CertificateSigningRequest"),
            CsrExtensions=CsrExtensions._deserialize(json_data.get("CsrExtensions")),
            KeyStorageSecurityStandard=json_data.get("KeyStorageSecurityStandard"),
            UsageMode=json_data.get("UsageMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAcmpcaCertificateauthority = AwsAcmpcaCertificateauthority


@dataclass
class Subject(BaseModel):
    Country: Optional[str]
    Organization: Optional[str]
    OrganizationalUnit: Optional[str]
    DistinguishedNameQualifier: Optional[str]
    State: Optional[str]
    CommonName: Optional[str]
    SerialNumber: Optional[str]
    Locality: Optional[str]
    Title: Optional[str]
    Surname: Optional[str]
    GivenName: Optional[str]
    Initials: Optional[str]
    Pseudonym: Optional[str]
    GenerationQualifier: Optional[str]
    CustomAttributes: Optional[Sequence["_CustomAttribute"]]

    @classmethod
    def _deserialize(
        cls: Type["_Subject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Subject"]:
        if not json_data:
            return None
        return cls(
            Country=json_data.get("Country"),
            Organization=json_data.get("Organization"),
            OrganizationalUnit=json_data.get("OrganizationalUnit"),
            DistinguishedNameQualifier=json_data.get("DistinguishedNameQualifier"),
            State=json_data.get("State"),
            CommonName=json_data.get("CommonName"),
            SerialNumber=json_data.get("SerialNumber"),
            Locality=json_data.get("Locality"),
            Title=json_data.get("Title"),
            Surname=json_data.get("Surname"),
            GivenName=json_data.get("GivenName"),
            Initials=json_data.get("Initials"),
            Pseudonym=json_data.get("Pseudonym"),
            GenerationQualifier=json_data.get("GenerationQualifier"),
            CustomAttributes=deserialize_list(json_data.get("CustomAttributes"), CustomAttribute),
        )


# work around possible type aliasing issues when variable has same name as a model
_Subject = Subject


@dataclass
class CustomAttribute(BaseModel):
    ObjectIdentifier: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomAttribute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomAttribute"]:
        if not json_data:
            return None
        return cls(
            ObjectIdentifier=json_data.get("ObjectIdentifier"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomAttribute = CustomAttribute


@dataclass
class RevocationConfiguration(BaseModel):
    CrlConfiguration: Optional["_CrlConfiguration"]
    OcspConfiguration: Optional["_OcspConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_RevocationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RevocationConfiguration"]:
        if not json_data:
            return None
        return cls(
            CrlConfiguration=CrlConfiguration._deserialize(json_data.get("CrlConfiguration")),
            OcspConfiguration=OcspConfiguration._deserialize(json_data.get("OcspConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RevocationConfiguration = RevocationConfiguration


@dataclass
class CrlConfiguration(BaseModel):
    Enabled: Optional[bool]
    ExpirationInDays: Optional[int]
    CustomCname: Optional[str]
    S3BucketName: Optional[str]
    S3ObjectAcl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CrlConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CrlConfiguration"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            ExpirationInDays=json_data.get("ExpirationInDays"),
            CustomCname=json_data.get("CustomCname"),
            S3BucketName=json_data.get("S3BucketName"),
            S3ObjectAcl=json_data.get("S3ObjectAcl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CrlConfiguration = CrlConfiguration


@dataclass
class OcspConfiguration(BaseModel):
    Enabled: Optional[bool]
    OcspCustomCname: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OcspConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OcspConfiguration"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            OcspCustomCname=json_data.get("OcspCustomCname"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OcspConfiguration = OcspConfiguration


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


@dataclass
class CsrExtensions(BaseModel):
    KeyUsage: Optional["_KeyUsage"]
    SubjectInformationAccess: Optional[Sequence["_AccessDescription"]]

    @classmethod
    def _deserialize(
        cls: Type["_CsrExtensions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CsrExtensions"]:
        if not json_data:
            return None
        return cls(
            KeyUsage=KeyUsage._deserialize(json_data.get("KeyUsage")),
            SubjectInformationAccess=deserialize_list(json_data.get("SubjectInformationAccess"), AccessDescription),
        )


# work around possible type aliasing issues when variable has same name as a model
_CsrExtensions = CsrExtensions


@dataclass
class KeyUsage(BaseModel):
    DigitalSignature: Optional[bool]
    NonRepudiation: Optional[bool]
    KeyEncipherment: Optional[bool]
    DataEncipherment: Optional[bool]
    KeyAgreement: Optional[bool]
    KeyCertSign: Optional[bool]
    CRLSign: Optional[bool]
    EncipherOnly: Optional[bool]
    DecipherOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_KeyUsage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyUsage"]:
        if not json_data:
            return None
        return cls(
            DigitalSignature=json_data.get("DigitalSignature"),
            NonRepudiation=json_data.get("NonRepudiation"),
            KeyEncipherment=json_data.get("KeyEncipherment"),
            DataEncipherment=json_data.get("DataEncipherment"),
            KeyAgreement=json_data.get("KeyAgreement"),
            KeyCertSign=json_data.get("KeyCertSign"),
            CRLSign=json_data.get("CRLSign"),
            EncipherOnly=json_data.get("EncipherOnly"),
            DecipherOnly=json_data.get("DecipherOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyUsage = KeyUsage


@dataclass
class AccessDescription(BaseModel):
    AccessMethod: Optional["_AccessMethod"]
    AccessLocation: Optional["_GeneralName"]

    @classmethod
    def _deserialize(
        cls: Type["_AccessDescription"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessDescription"]:
        if not json_data:
            return None
        return cls(
            AccessMethod=AccessMethod._deserialize(json_data.get("AccessMethod")),
            AccessLocation=GeneralName._deserialize(json_data.get("AccessLocation")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessDescription = AccessDescription


@dataclass
class AccessMethod(BaseModel):
    CustomObjectIdentifier: Optional[str]
    AccessMethodType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessMethod"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessMethod"]:
        if not json_data:
            return None
        return cls(
            CustomObjectIdentifier=json_data.get("CustomObjectIdentifier"),
            AccessMethodType=json_data.get("AccessMethodType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessMethod = AccessMethod


@dataclass
class GeneralName(BaseModel):
    OtherName: Optional["_OtherName"]
    Rfc822Name: Optional[str]
    DnsName: Optional[str]
    DirectoryName: Optional["_Subject"]
    EdiPartyName: Optional["_EdiPartyName"]
    UniformResourceIdentifier: Optional[str]
    IpAddress: Optional[str]
    RegisteredId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GeneralName"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeneralName"]:
        if not json_data:
            return None
        return cls(
            OtherName=OtherName._deserialize(json_data.get("OtherName")),
            Rfc822Name=json_data.get("Rfc822Name"),
            DnsName=json_data.get("DnsName"),
            DirectoryName=Subject._deserialize(json_data.get("DirectoryName")),
            EdiPartyName=EdiPartyName._deserialize(json_data.get("EdiPartyName")),
            UniformResourceIdentifier=json_data.get("UniformResourceIdentifier"),
            IpAddress=json_data.get("IpAddress"),
            RegisteredId=json_data.get("RegisteredId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeneralName = GeneralName


@dataclass
class OtherName(BaseModel):
    TypeId: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OtherName"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OtherName"]:
        if not json_data:
            return None
        return cls(
            TypeId=json_data.get("TypeId"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OtherName = OtherName


@dataclass
class EdiPartyName(BaseModel):
    PartyName: Optional[str]
    NameAssigner: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EdiPartyName"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EdiPartyName"]:
        if not json_data:
            return None
        return cls(
            PartyName=json_data.get("PartyName"),
            NameAssigner=json_data.get("NameAssigner"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EdiPartyName = EdiPartyName


