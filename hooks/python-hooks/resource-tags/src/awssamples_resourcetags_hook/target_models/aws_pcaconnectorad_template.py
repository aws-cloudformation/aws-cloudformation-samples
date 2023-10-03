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
class AwsPcaconnectoradTemplate(BaseModel):
    ConnectorArn: Optional[str]
    Definition: Optional["_TemplateDefinition"]
    Name: Optional[str]
    ReenrollAllCertificateHolders: Optional[bool]
    Tags: Optional[Any]
    TemplateArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsPcaconnectoradTemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsPcaconnectoradTemplate"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ConnectorArn=json_data.get("ConnectorArn"),
            Definition=TemplateDefinition._deserialize(json_data.get("Definition")),
            Name=json_data.get("Name"),
            ReenrollAllCertificateHolders=json_data.get("ReenrollAllCertificateHolders"),
            Tags=json_data.get("Tags"),
            TemplateArn=json_data.get("TemplateArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsPcaconnectoradTemplate = AwsPcaconnectoradTemplate


@dataclass
class TemplateDefinition(BaseModel):
    TemplateV2: Optional["_TemplateV2"]
    TemplateV3: Optional["_TemplateV3"]
    TemplateV4: Optional["_TemplateV4"]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateDefinition"]:
        if not json_data:
            return None
        return cls(
            TemplateV2=TemplateV2._deserialize(json_data.get("TemplateV2")),
            TemplateV3=TemplateV3._deserialize(json_data.get("TemplateV3")),
            TemplateV4=TemplateV4._deserialize(json_data.get("TemplateV4")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateDefinition = TemplateDefinition


@dataclass
class TemplateV2(BaseModel):
    CertificateValidity: Optional["_CertificateValidity"]
    SupersededTemplates: Optional[Sequence[str]]
    PrivateKeyAttributes: Optional["_PrivateKeyAttributesV2"]
    PrivateKeyFlags: Optional["_PrivateKeyFlagsV2"]
    EnrollmentFlags: Optional["_EnrollmentFlagsV2"]
    SubjectNameFlags: Optional["_SubjectNameFlagsV2"]
    GeneralFlags: Optional["_GeneralFlagsV2"]
    Extensions: Optional["_ExtensionsV2"]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateV2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateV2"]:
        if not json_data:
            return None
        return cls(
            CertificateValidity=CertificateValidity._deserialize(json_data.get("CertificateValidity")),
            SupersededTemplates=json_data.get("SupersededTemplates"),
            PrivateKeyAttributes=PrivateKeyAttributesV2._deserialize(json_data.get("PrivateKeyAttributes")),
            PrivateKeyFlags=PrivateKeyFlagsV2._deserialize(json_data.get("PrivateKeyFlags")),
            EnrollmentFlags=EnrollmentFlagsV2._deserialize(json_data.get("EnrollmentFlags")),
            SubjectNameFlags=SubjectNameFlagsV2._deserialize(json_data.get("SubjectNameFlags")),
            GeneralFlags=GeneralFlagsV2._deserialize(json_data.get("GeneralFlags")),
            Extensions=ExtensionsV2._deserialize(json_data.get("Extensions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateV2 = TemplateV2


@dataclass
class CertificateValidity(BaseModel):
    ValidityPeriod: Optional["_ValidityPeriod"]
    RenewalPeriod: Optional["_ValidityPeriod"]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateValidity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateValidity"]:
        if not json_data:
            return None
        return cls(
            ValidityPeriod=ValidityPeriod._deserialize(json_data.get("ValidityPeriod")),
            RenewalPeriod=ValidityPeriod._deserialize(json_data.get("RenewalPeriod")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateValidity = CertificateValidity


@dataclass
class ValidityPeriod(BaseModel):
    PeriodType: Optional[str]
    Period: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ValidityPeriod"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValidityPeriod"]:
        if not json_data:
            return None
        return cls(
            PeriodType=json_data.get("PeriodType"),
            Period=json_data.get("Period"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValidityPeriod = ValidityPeriod


@dataclass
class PrivateKeyAttributesV2(BaseModel):
    MinimalKeyLength: Optional[float]
    KeySpec: Optional[str]
    CryptoProviders: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateKeyAttributesV2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateKeyAttributesV2"]:
        if not json_data:
            return None
        return cls(
            MinimalKeyLength=json_data.get("MinimalKeyLength"),
            KeySpec=json_data.get("KeySpec"),
            CryptoProviders=json_data.get("CryptoProviders"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateKeyAttributesV2 = PrivateKeyAttributesV2


@dataclass
class PrivateKeyFlagsV2(BaseModel):
    ExportableKey: Optional[bool]
    StrongKeyProtectionRequired: Optional[bool]
    ClientVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateKeyFlagsV2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateKeyFlagsV2"]:
        if not json_data:
            return None
        return cls(
            ExportableKey=json_data.get("ExportableKey"),
            StrongKeyProtectionRequired=json_data.get("StrongKeyProtectionRequired"),
            ClientVersion=json_data.get("ClientVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateKeyFlagsV2 = PrivateKeyFlagsV2


@dataclass
class EnrollmentFlagsV2(BaseModel):
    IncludeSymmetricAlgorithms: Optional[bool]
    UserInteractionRequired: Optional[bool]
    RemoveInvalidCertificateFromPersonalStore: Optional[bool]
    NoSecurityExtension: Optional[bool]
    EnableKeyReuseOnNtTokenKeysetStorageFull: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EnrollmentFlagsV2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnrollmentFlagsV2"]:
        if not json_data:
            return None
        return cls(
            IncludeSymmetricAlgorithms=json_data.get("IncludeSymmetricAlgorithms"),
            UserInteractionRequired=json_data.get("UserInteractionRequired"),
            RemoveInvalidCertificateFromPersonalStore=json_data.get("RemoveInvalidCertificateFromPersonalStore"),
            NoSecurityExtension=json_data.get("NoSecurityExtension"),
            EnableKeyReuseOnNtTokenKeysetStorageFull=json_data.get("EnableKeyReuseOnNtTokenKeysetStorageFull"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnrollmentFlagsV2 = EnrollmentFlagsV2


@dataclass
class SubjectNameFlagsV2(BaseModel):
    SanRequireDomainDns: Optional[bool]
    SanRequireSpn: Optional[bool]
    SanRequireDirectoryGuid: Optional[bool]
    SanRequireUpn: Optional[bool]
    SanRequireEmail: Optional[bool]
    SanRequireDns: Optional[bool]
    RequireDnsAsCn: Optional[bool]
    RequireEmail: Optional[bool]
    RequireCommonName: Optional[bool]
    RequireDirectoryPath: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SubjectNameFlagsV2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubjectNameFlagsV2"]:
        if not json_data:
            return None
        return cls(
            SanRequireDomainDns=json_data.get("SanRequireDomainDns"),
            SanRequireSpn=json_data.get("SanRequireSpn"),
            SanRequireDirectoryGuid=json_data.get("SanRequireDirectoryGuid"),
            SanRequireUpn=json_data.get("SanRequireUpn"),
            SanRequireEmail=json_data.get("SanRequireEmail"),
            SanRequireDns=json_data.get("SanRequireDns"),
            RequireDnsAsCn=json_data.get("RequireDnsAsCn"),
            RequireEmail=json_data.get("RequireEmail"),
            RequireCommonName=json_data.get("RequireCommonName"),
            RequireDirectoryPath=json_data.get("RequireDirectoryPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubjectNameFlagsV2 = SubjectNameFlagsV2


@dataclass
class GeneralFlagsV2(BaseModel):
    AutoEnrollment: Optional[bool]
    MachineType: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GeneralFlagsV2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeneralFlagsV2"]:
        if not json_data:
            return None
        return cls(
            AutoEnrollment=json_data.get("AutoEnrollment"),
            MachineType=json_data.get("MachineType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeneralFlagsV2 = GeneralFlagsV2


@dataclass
class ExtensionsV2(BaseModel):
    KeyUsage: Optional["_KeyUsage"]
    ApplicationPolicies: Optional["_ApplicationPolicies"]

    @classmethod
    def _deserialize(
        cls: Type["_ExtensionsV2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtensionsV2"]:
        if not json_data:
            return None
        return cls(
            KeyUsage=KeyUsage._deserialize(json_data.get("KeyUsage")),
            ApplicationPolicies=ApplicationPolicies._deserialize(json_data.get("ApplicationPolicies")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtensionsV2 = ExtensionsV2


@dataclass
class KeyUsage(BaseModel):
    Critical: Optional[bool]
    UsageFlags: Optional["_KeyUsageFlags"]

    @classmethod
    def _deserialize(
        cls: Type["_KeyUsage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyUsage"]:
        if not json_data:
            return None
        return cls(
            Critical=json_data.get("Critical"),
            UsageFlags=KeyUsageFlags._deserialize(json_data.get("UsageFlags")),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyUsage = KeyUsage


@dataclass
class KeyUsageFlags(BaseModel):
    DigitalSignature: Optional[bool]
    NonRepudiation: Optional[bool]
    KeyEncipherment: Optional[bool]
    DataEncipherment: Optional[bool]
    KeyAgreement: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_KeyUsageFlags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyUsageFlags"]:
        if not json_data:
            return None
        return cls(
            DigitalSignature=json_data.get("DigitalSignature"),
            NonRepudiation=json_data.get("NonRepudiation"),
            KeyEncipherment=json_data.get("KeyEncipherment"),
            DataEncipherment=json_data.get("DataEncipherment"),
            KeyAgreement=json_data.get("KeyAgreement"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyUsageFlags = KeyUsageFlags


@dataclass
class ApplicationPolicies(BaseModel):
    Critical: Optional[bool]
    Policies: Optional[Sequence["_ApplicationPolicy"]]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationPolicies"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationPolicies"]:
        if not json_data:
            return None
        return cls(
            Critical=json_data.get("Critical"),
            Policies=deserialize_list(json_data.get("Policies"), ApplicationPolicy),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationPolicies = ApplicationPolicies


@dataclass
class ApplicationPolicy(BaseModel):
    PolicyType: Optional[str]
    PolicyObjectIdentifier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationPolicy"]:
        if not json_data:
            return None
        return cls(
            PolicyType=json_data.get("PolicyType"),
            PolicyObjectIdentifier=json_data.get("PolicyObjectIdentifier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationPolicy = ApplicationPolicy


@dataclass
class TemplateV3(BaseModel):
    CertificateValidity: Optional["_CertificateValidity"]
    SupersededTemplates: Optional[Sequence[str]]
    PrivateKeyAttributes: Optional["_PrivateKeyAttributesV3"]
    PrivateKeyFlags: Optional["_PrivateKeyFlagsV3"]
    EnrollmentFlags: Optional["_EnrollmentFlagsV3"]
    SubjectNameFlags: Optional["_SubjectNameFlagsV3"]
    GeneralFlags: Optional["_GeneralFlagsV3"]
    HashAlgorithm: Optional[str]
    Extensions: Optional["_ExtensionsV3"]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateV3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateV3"]:
        if not json_data:
            return None
        return cls(
            CertificateValidity=CertificateValidity._deserialize(json_data.get("CertificateValidity")),
            SupersededTemplates=json_data.get("SupersededTemplates"),
            PrivateKeyAttributes=PrivateKeyAttributesV3._deserialize(json_data.get("PrivateKeyAttributes")),
            PrivateKeyFlags=PrivateKeyFlagsV3._deserialize(json_data.get("PrivateKeyFlags")),
            EnrollmentFlags=EnrollmentFlagsV3._deserialize(json_data.get("EnrollmentFlags")),
            SubjectNameFlags=SubjectNameFlagsV3._deserialize(json_data.get("SubjectNameFlags")),
            GeneralFlags=GeneralFlagsV3._deserialize(json_data.get("GeneralFlags")),
            HashAlgorithm=json_data.get("HashAlgorithm"),
            Extensions=ExtensionsV3._deserialize(json_data.get("Extensions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateV3 = TemplateV3


@dataclass
class PrivateKeyAttributesV3(BaseModel):
    MinimalKeyLength: Optional[float]
    KeySpec: Optional[str]
    CryptoProviders: Optional[Sequence[str]]
    KeyUsageProperty: Optional["_KeyUsageProperty"]
    Algorithm: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateKeyAttributesV3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateKeyAttributesV3"]:
        if not json_data:
            return None
        return cls(
            MinimalKeyLength=json_data.get("MinimalKeyLength"),
            KeySpec=json_data.get("KeySpec"),
            CryptoProviders=json_data.get("CryptoProviders"),
            KeyUsageProperty=KeyUsageProperty._deserialize(json_data.get("KeyUsageProperty")),
            Algorithm=json_data.get("Algorithm"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateKeyAttributesV3 = PrivateKeyAttributesV3


@dataclass
class KeyUsageProperty(BaseModel):
    PropertyType: Optional[str]
    PropertyFlags: Optional["_KeyUsagePropertyFlags"]

    @classmethod
    def _deserialize(
        cls: Type["_KeyUsageProperty"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyUsageProperty"]:
        if not json_data:
            return None
        return cls(
            PropertyType=json_data.get("PropertyType"),
            PropertyFlags=KeyUsagePropertyFlags._deserialize(json_data.get("PropertyFlags")),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyUsageProperty = KeyUsageProperty


@dataclass
class KeyUsagePropertyFlags(BaseModel):
    Decrypt: Optional[bool]
    KeyAgreement: Optional[bool]
    Sign: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_KeyUsagePropertyFlags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyUsagePropertyFlags"]:
        if not json_data:
            return None
        return cls(
            Decrypt=json_data.get("Decrypt"),
            KeyAgreement=json_data.get("KeyAgreement"),
            Sign=json_data.get("Sign"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyUsagePropertyFlags = KeyUsagePropertyFlags


@dataclass
class PrivateKeyFlagsV3(BaseModel):
    ExportableKey: Optional[bool]
    StrongKeyProtectionRequired: Optional[bool]
    RequireAlternateSignatureAlgorithm: Optional[bool]
    ClientVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateKeyFlagsV3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateKeyFlagsV3"]:
        if not json_data:
            return None
        return cls(
            ExportableKey=json_data.get("ExportableKey"),
            StrongKeyProtectionRequired=json_data.get("StrongKeyProtectionRequired"),
            RequireAlternateSignatureAlgorithm=json_data.get("RequireAlternateSignatureAlgorithm"),
            ClientVersion=json_data.get("ClientVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateKeyFlagsV3 = PrivateKeyFlagsV3


@dataclass
class EnrollmentFlagsV3(BaseModel):
    IncludeSymmetricAlgorithms: Optional[bool]
    UserInteractionRequired: Optional[bool]
    RemoveInvalidCertificateFromPersonalStore: Optional[bool]
    NoSecurityExtension: Optional[bool]
    EnableKeyReuseOnNtTokenKeysetStorageFull: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EnrollmentFlagsV3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnrollmentFlagsV3"]:
        if not json_data:
            return None
        return cls(
            IncludeSymmetricAlgorithms=json_data.get("IncludeSymmetricAlgorithms"),
            UserInteractionRequired=json_data.get("UserInteractionRequired"),
            RemoveInvalidCertificateFromPersonalStore=json_data.get("RemoveInvalidCertificateFromPersonalStore"),
            NoSecurityExtension=json_data.get("NoSecurityExtension"),
            EnableKeyReuseOnNtTokenKeysetStorageFull=json_data.get("EnableKeyReuseOnNtTokenKeysetStorageFull"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnrollmentFlagsV3 = EnrollmentFlagsV3


@dataclass
class SubjectNameFlagsV3(BaseModel):
    SanRequireDomainDns: Optional[bool]
    SanRequireSpn: Optional[bool]
    SanRequireDirectoryGuid: Optional[bool]
    SanRequireUpn: Optional[bool]
    SanRequireEmail: Optional[bool]
    SanRequireDns: Optional[bool]
    RequireDnsAsCn: Optional[bool]
    RequireEmail: Optional[bool]
    RequireCommonName: Optional[bool]
    RequireDirectoryPath: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SubjectNameFlagsV3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubjectNameFlagsV3"]:
        if not json_data:
            return None
        return cls(
            SanRequireDomainDns=json_data.get("SanRequireDomainDns"),
            SanRequireSpn=json_data.get("SanRequireSpn"),
            SanRequireDirectoryGuid=json_data.get("SanRequireDirectoryGuid"),
            SanRequireUpn=json_data.get("SanRequireUpn"),
            SanRequireEmail=json_data.get("SanRequireEmail"),
            SanRequireDns=json_data.get("SanRequireDns"),
            RequireDnsAsCn=json_data.get("RequireDnsAsCn"),
            RequireEmail=json_data.get("RequireEmail"),
            RequireCommonName=json_data.get("RequireCommonName"),
            RequireDirectoryPath=json_data.get("RequireDirectoryPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubjectNameFlagsV3 = SubjectNameFlagsV3


@dataclass
class GeneralFlagsV3(BaseModel):
    AutoEnrollment: Optional[bool]
    MachineType: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GeneralFlagsV3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeneralFlagsV3"]:
        if not json_data:
            return None
        return cls(
            AutoEnrollment=json_data.get("AutoEnrollment"),
            MachineType=json_data.get("MachineType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeneralFlagsV3 = GeneralFlagsV3


@dataclass
class ExtensionsV3(BaseModel):
    KeyUsage: Optional["_KeyUsage"]
    ApplicationPolicies: Optional["_ApplicationPolicies"]

    @classmethod
    def _deserialize(
        cls: Type["_ExtensionsV3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtensionsV3"]:
        if not json_data:
            return None
        return cls(
            KeyUsage=KeyUsage._deserialize(json_data.get("KeyUsage")),
            ApplicationPolicies=ApplicationPolicies._deserialize(json_data.get("ApplicationPolicies")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtensionsV3 = ExtensionsV3


@dataclass
class TemplateV4(BaseModel):
    CertificateValidity: Optional["_CertificateValidity"]
    SupersededTemplates: Optional[Sequence[str]]
    PrivateKeyAttributes: Optional["_PrivateKeyAttributesV4"]
    PrivateKeyFlags: Optional["_PrivateKeyFlagsV4"]
    EnrollmentFlags: Optional["_EnrollmentFlagsV4"]
    SubjectNameFlags: Optional["_SubjectNameFlagsV4"]
    GeneralFlags: Optional["_GeneralFlagsV4"]
    HashAlgorithm: Optional[str]
    Extensions: Optional["_ExtensionsV4"]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateV4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateV4"]:
        if not json_data:
            return None
        return cls(
            CertificateValidity=CertificateValidity._deserialize(json_data.get("CertificateValidity")),
            SupersededTemplates=json_data.get("SupersededTemplates"),
            PrivateKeyAttributes=PrivateKeyAttributesV4._deserialize(json_data.get("PrivateKeyAttributes")),
            PrivateKeyFlags=PrivateKeyFlagsV4._deserialize(json_data.get("PrivateKeyFlags")),
            EnrollmentFlags=EnrollmentFlagsV4._deserialize(json_data.get("EnrollmentFlags")),
            SubjectNameFlags=SubjectNameFlagsV4._deserialize(json_data.get("SubjectNameFlags")),
            GeneralFlags=GeneralFlagsV4._deserialize(json_data.get("GeneralFlags")),
            HashAlgorithm=json_data.get("HashAlgorithm"),
            Extensions=ExtensionsV4._deserialize(json_data.get("Extensions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateV4 = TemplateV4


@dataclass
class PrivateKeyAttributesV4(BaseModel):
    MinimalKeyLength: Optional[float]
    KeySpec: Optional[str]
    CryptoProviders: Optional[Sequence[str]]
    KeyUsageProperty: Optional["_KeyUsageProperty"]
    Algorithm: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateKeyAttributesV4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateKeyAttributesV4"]:
        if not json_data:
            return None
        return cls(
            MinimalKeyLength=json_data.get("MinimalKeyLength"),
            KeySpec=json_data.get("KeySpec"),
            CryptoProviders=json_data.get("CryptoProviders"),
            KeyUsageProperty=KeyUsageProperty._deserialize(json_data.get("KeyUsageProperty")),
            Algorithm=json_data.get("Algorithm"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateKeyAttributesV4 = PrivateKeyAttributesV4


@dataclass
class PrivateKeyFlagsV4(BaseModel):
    ExportableKey: Optional[bool]
    StrongKeyProtectionRequired: Optional[bool]
    RequireAlternateSignatureAlgorithm: Optional[bool]
    RequireSameKeyRenewal: Optional[bool]
    UseLegacyProvider: Optional[bool]
    ClientVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateKeyFlagsV4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateKeyFlagsV4"]:
        if not json_data:
            return None
        return cls(
            ExportableKey=json_data.get("ExportableKey"),
            StrongKeyProtectionRequired=json_data.get("StrongKeyProtectionRequired"),
            RequireAlternateSignatureAlgorithm=json_data.get("RequireAlternateSignatureAlgorithm"),
            RequireSameKeyRenewal=json_data.get("RequireSameKeyRenewal"),
            UseLegacyProvider=json_data.get("UseLegacyProvider"),
            ClientVersion=json_data.get("ClientVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateKeyFlagsV4 = PrivateKeyFlagsV4


@dataclass
class EnrollmentFlagsV4(BaseModel):
    IncludeSymmetricAlgorithms: Optional[bool]
    UserInteractionRequired: Optional[bool]
    RemoveInvalidCertificateFromPersonalStore: Optional[bool]
    NoSecurityExtension: Optional[bool]
    EnableKeyReuseOnNtTokenKeysetStorageFull: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EnrollmentFlagsV4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnrollmentFlagsV4"]:
        if not json_data:
            return None
        return cls(
            IncludeSymmetricAlgorithms=json_data.get("IncludeSymmetricAlgorithms"),
            UserInteractionRequired=json_data.get("UserInteractionRequired"),
            RemoveInvalidCertificateFromPersonalStore=json_data.get("RemoveInvalidCertificateFromPersonalStore"),
            NoSecurityExtension=json_data.get("NoSecurityExtension"),
            EnableKeyReuseOnNtTokenKeysetStorageFull=json_data.get("EnableKeyReuseOnNtTokenKeysetStorageFull"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnrollmentFlagsV4 = EnrollmentFlagsV4


@dataclass
class SubjectNameFlagsV4(BaseModel):
    SanRequireDomainDns: Optional[bool]
    SanRequireSpn: Optional[bool]
    SanRequireDirectoryGuid: Optional[bool]
    SanRequireUpn: Optional[bool]
    SanRequireEmail: Optional[bool]
    SanRequireDns: Optional[bool]
    RequireDnsAsCn: Optional[bool]
    RequireEmail: Optional[bool]
    RequireCommonName: Optional[bool]
    RequireDirectoryPath: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SubjectNameFlagsV4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubjectNameFlagsV4"]:
        if not json_data:
            return None
        return cls(
            SanRequireDomainDns=json_data.get("SanRequireDomainDns"),
            SanRequireSpn=json_data.get("SanRequireSpn"),
            SanRequireDirectoryGuid=json_data.get("SanRequireDirectoryGuid"),
            SanRequireUpn=json_data.get("SanRequireUpn"),
            SanRequireEmail=json_data.get("SanRequireEmail"),
            SanRequireDns=json_data.get("SanRequireDns"),
            RequireDnsAsCn=json_data.get("RequireDnsAsCn"),
            RequireEmail=json_data.get("RequireEmail"),
            RequireCommonName=json_data.get("RequireCommonName"),
            RequireDirectoryPath=json_data.get("RequireDirectoryPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubjectNameFlagsV4 = SubjectNameFlagsV4


@dataclass
class GeneralFlagsV4(BaseModel):
    AutoEnrollment: Optional[bool]
    MachineType: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GeneralFlagsV4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeneralFlagsV4"]:
        if not json_data:
            return None
        return cls(
            AutoEnrollment=json_data.get("AutoEnrollment"),
            MachineType=json_data.get("MachineType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeneralFlagsV4 = GeneralFlagsV4


@dataclass
class ExtensionsV4(BaseModel):
    KeyUsage: Optional["_KeyUsage"]
    ApplicationPolicies: Optional["_ApplicationPolicies"]

    @classmethod
    def _deserialize(
        cls: Type["_ExtensionsV4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtensionsV4"]:
        if not json_data:
            return None
        return cls(
            KeyUsage=KeyUsage._deserialize(json_data.get("KeyUsage")),
            ApplicationPolicies=ApplicationPolicies._deserialize(json_data.get("ApplicationPolicies")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtensionsV4 = ExtensionsV4


