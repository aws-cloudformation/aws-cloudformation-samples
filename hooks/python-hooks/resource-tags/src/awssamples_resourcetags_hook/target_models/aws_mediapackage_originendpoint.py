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
class AwsMediapackageOriginendpoint(BaseModel):
    Arn: Optional[str]
    Url: Optional[str]
    Id: Optional[str]
    ChannelId: Optional[str]
    Description: Optional[str]
    Whitelist: Optional[Sequence[str]]
    StartoverWindowSeconds: Optional[int]
    TimeDelaySeconds: Optional[int]
    ManifestName: Optional[str]
    Origination: Optional[str]
    Authorization: Optional["_Authorization"]
    HlsPackage: Optional["_HlsPackage"]
    DashPackage: Optional["_DashPackage"]
    MssPackage: Optional["_MssPackage"]
    CmafPackage: Optional["_CmafPackage"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMediapackageOriginendpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMediapackageOriginendpoint"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Url=json_data.get("Url"),
            Id=json_data.get("Id"),
            ChannelId=json_data.get("ChannelId"),
            Description=json_data.get("Description"),
            Whitelist=json_data.get("Whitelist"),
            StartoverWindowSeconds=json_data.get("StartoverWindowSeconds"),
            TimeDelaySeconds=json_data.get("TimeDelaySeconds"),
            ManifestName=json_data.get("ManifestName"),
            Origination=json_data.get("Origination"),
            Authorization=Authorization._deserialize(json_data.get("Authorization")),
            HlsPackage=HlsPackage._deserialize(json_data.get("HlsPackage")),
            DashPackage=DashPackage._deserialize(json_data.get("DashPackage")),
            MssPackage=MssPackage._deserialize(json_data.get("MssPackage")),
            CmafPackage=CmafPackage._deserialize(json_data.get("CmafPackage")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMediapackageOriginendpoint = AwsMediapackageOriginendpoint


@dataclass
class Authorization(BaseModel):
    SecretsRoleArn: Optional[str]
    CdnIdentifierSecret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Authorization"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Authorization"]:
        if not json_data:
            return None
        return cls(
            SecretsRoleArn=json_data.get("SecretsRoleArn"),
            CdnIdentifierSecret=json_data.get("CdnIdentifierSecret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Authorization = Authorization


@dataclass
class HlsPackage(BaseModel):
    SegmentDurationSeconds: Optional[int]
    PlaylistWindowSeconds: Optional[int]
    PlaylistType: Optional[str]
    AdMarkers: Optional[str]
    AdTriggers: Optional[Sequence[str]]
    AdsOnDeliveryRestrictions: Optional[str]
    ProgramDateTimeIntervalSeconds: Optional[int]
    IncludeIframeOnlyStream: Optional[bool]
    UseAudioRenditionGroup: Optional[bool]
    IncludeDvbSubtitles: Optional[bool]
    Encryption: Optional["_HlsEncryption"]
    StreamSelection: Optional["_StreamSelection"]

    @classmethod
    def _deserialize(
        cls: Type["_HlsPackage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HlsPackage"]:
        if not json_data:
            return None
        return cls(
            SegmentDurationSeconds=json_data.get("SegmentDurationSeconds"),
            PlaylistWindowSeconds=json_data.get("PlaylistWindowSeconds"),
            PlaylistType=json_data.get("PlaylistType"),
            AdMarkers=json_data.get("AdMarkers"),
            AdTriggers=json_data.get("AdTriggers"),
            AdsOnDeliveryRestrictions=json_data.get("AdsOnDeliveryRestrictions"),
            ProgramDateTimeIntervalSeconds=json_data.get("ProgramDateTimeIntervalSeconds"),
            IncludeIframeOnlyStream=json_data.get("IncludeIframeOnlyStream"),
            UseAudioRenditionGroup=json_data.get("UseAudioRenditionGroup"),
            IncludeDvbSubtitles=json_data.get("IncludeDvbSubtitles"),
            Encryption=HlsEncryption._deserialize(json_data.get("Encryption")),
            StreamSelection=StreamSelection._deserialize(json_data.get("StreamSelection")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HlsPackage = HlsPackage


@dataclass
class HlsEncryption(BaseModel):
    EncryptionMethod: Optional[str]
    ConstantInitializationVector: Optional[str]
    KeyRotationIntervalSeconds: Optional[int]
    RepeatExtXKey: Optional[bool]
    SpekeKeyProvider: Optional["_SpekeKeyProvider"]

    @classmethod
    def _deserialize(
        cls: Type["_HlsEncryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HlsEncryption"]:
        if not json_data:
            return None
        return cls(
            EncryptionMethod=json_data.get("EncryptionMethod"),
            ConstantInitializationVector=json_data.get("ConstantInitializationVector"),
            KeyRotationIntervalSeconds=json_data.get("KeyRotationIntervalSeconds"),
            RepeatExtXKey=json_data.get("RepeatExtXKey"),
            SpekeKeyProvider=SpekeKeyProvider._deserialize(json_data.get("SpekeKeyProvider")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HlsEncryption = HlsEncryption


@dataclass
class SpekeKeyProvider(BaseModel):
    ResourceId: Optional[str]
    SystemIds: Optional[Sequence[str]]
    Url: Optional[str]
    RoleArn: Optional[str]
    CertificateArn: Optional[str]
    EncryptionContractConfiguration: Optional["_EncryptionContractConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_SpekeKeyProvider"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpekeKeyProvider"]:
        if not json_data:
            return None
        return cls(
            ResourceId=json_data.get("ResourceId"),
            SystemIds=json_data.get("SystemIds"),
            Url=json_data.get("Url"),
            RoleArn=json_data.get("RoleArn"),
            CertificateArn=json_data.get("CertificateArn"),
            EncryptionContractConfiguration=EncryptionContractConfiguration._deserialize(json_data.get("EncryptionContractConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpekeKeyProvider = SpekeKeyProvider


@dataclass
class EncryptionContractConfiguration(BaseModel):
    PresetSpeke20Audio: Optional[str]
    PresetSpeke20Video: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionContractConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionContractConfiguration"]:
        if not json_data:
            return None
        return cls(
            PresetSpeke20Audio=json_data.get("PresetSpeke20Audio"),
            PresetSpeke20Video=json_data.get("PresetSpeke20Video"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionContractConfiguration = EncryptionContractConfiguration


@dataclass
class StreamSelection(BaseModel):
    MinVideoBitsPerSecond: Optional[int]
    MaxVideoBitsPerSecond: Optional[int]
    StreamOrder: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StreamSelection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StreamSelection"]:
        if not json_data:
            return None
        return cls(
            MinVideoBitsPerSecond=json_data.get("MinVideoBitsPerSecond"),
            MaxVideoBitsPerSecond=json_data.get("MaxVideoBitsPerSecond"),
            StreamOrder=json_data.get("StreamOrder"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StreamSelection = StreamSelection


@dataclass
class DashPackage(BaseModel):
    SegmentDurationSeconds: Optional[int]
    ManifestWindowSeconds: Optional[int]
    Profile: Optional[str]
    MinUpdatePeriodSeconds: Optional[int]
    MinBufferTimeSeconds: Optional[int]
    SuggestedPresentationDelaySeconds: Optional[int]
    PeriodTriggers: Optional[Sequence[str]]
    IncludeIframeOnlyStream: Optional[bool]
    ManifestLayout: Optional[str]
    SegmentTemplateFormat: Optional[str]
    AdTriggers: Optional[Sequence[str]]
    AdsOnDeliveryRestrictions: Optional[str]
    Encryption: Optional["_DashEncryption"]
    StreamSelection: Optional["_StreamSelection"]
    UtcTiming: Optional[str]
    UtcTimingUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DashPackage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DashPackage"]:
        if not json_data:
            return None
        return cls(
            SegmentDurationSeconds=json_data.get("SegmentDurationSeconds"),
            ManifestWindowSeconds=json_data.get("ManifestWindowSeconds"),
            Profile=json_data.get("Profile"),
            MinUpdatePeriodSeconds=json_data.get("MinUpdatePeriodSeconds"),
            MinBufferTimeSeconds=json_data.get("MinBufferTimeSeconds"),
            SuggestedPresentationDelaySeconds=json_data.get("SuggestedPresentationDelaySeconds"),
            PeriodTriggers=json_data.get("PeriodTriggers"),
            IncludeIframeOnlyStream=json_data.get("IncludeIframeOnlyStream"),
            ManifestLayout=json_data.get("ManifestLayout"),
            SegmentTemplateFormat=json_data.get("SegmentTemplateFormat"),
            AdTriggers=json_data.get("AdTriggers"),
            AdsOnDeliveryRestrictions=json_data.get("AdsOnDeliveryRestrictions"),
            Encryption=DashEncryption._deserialize(json_data.get("Encryption")),
            StreamSelection=StreamSelection._deserialize(json_data.get("StreamSelection")),
            UtcTiming=json_data.get("UtcTiming"),
            UtcTimingUri=json_data.get("UtcTimingUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DashPackage = DashPackage


@dataclass
class DashEncryption(BaseModel):
    KeyRotationIntervalSeconds: Optional[int]
    SpekeKeyProvider: Optional["_SpekeKeyProvider"]

    @classmethod
    def _deserialize(
        cls: Type["_DashEncryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DashEncryption"]:
        if not json_data:
            return None
        return cls(
            KeyRotationIntervalSeconds=json_data.get("KeyRotationIntervalSeconds"),
            SpekeKeyProvider=SpekeKeyProvider._deserialize(json_data.get("SpekeKeyProvider")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DashEncryption = DashEncryption


@dataclass
class MssPackage(BaseModel):
    ManifestWindowSeconds: Optional[int]
    SegmentDurationSeconds: Optional[int]
    Encryption: Optional["_MssEncryption"]
    StreamSelection: Optional["_StreamSelection"]

    @classmethod
    def _deserialize(
        cls: Type["_MssPackage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MssPackage"]:
        if not json_data:
            return None
        return cls(
            ManifestWindowSeconds=json_data.get("ManifestWindowSeconds"),
            SegmentDurationSeconds=json_data.get("SegmentDurationSeconds"),
            Encryption=MssEncryption._deserialize(json_data.get("Encryption")),
            StreamSelection=StreamSelection._deserialize(json_data.get("StreamSelection")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MssPackage = MssPackage


@dataclass
class MssEncryption(BaseModel):
    SpekeKeyProvider: Optional["_SpekeKeyProvider"]

    @classmethod
    def _deserialize(
        cls: Type["_MssEncryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MssEncryption"]:
        if not json_data:
            return None
        return cls(
            SpekeKeyProvider=SpekeKeyProvider._deserialize(json_data.get("SpekeKeyProvider")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MssEncryption = MssEncryption


@dataclass
class CmafPackage(BaseModel):
    SegmentDurationSeconds: Optional[int]
    SegmentPrefix: Optional[str]
    Encryption: Optional["_CmafEncryption"]
    StreamSelection: Optional["_StreamSelection"]
    HlsManifests: Optional[Sequence["_HlsManifest"]]

    @classmethod
    def _deserialize(
        cls: Type["_CmafPackage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CmafPackage"]:
        if not json_data:
            return None
        return cls(
            SegmentDurationSeconds=json_data.get("SegmentDurationSeconds"),
            SegmentPrefix=json_data.get("SegmentPrefix"),
            Encryption=CmafEncryption._deserialize(json_data.get("Encryption")),
            StreamSelection=StreamSelection._deserialize(json_data.get("StreamSelection")),
            HlsManifests=deserialize_list(json_data.get("HlsManifests"), HlsManifest),
        )


# work around possible type aliasing issues when variable has same name as a model
_CmafPackage = CmafPackage


@dataclass
class CmafEncryption(BaseModel):
    KeyRotationIntervalSeconds: Optional[int]
    SpekeKeyProvider: Optional["_SpekeKeyProvider"]
    ConstantInitializationVector: Optional[str]
    EncryptionMethod: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CmafEncryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CmafEncryption"]:
        if not json_data:
            return None
        return cls(
            KeyRotationIntervalSeconds=json_data.get("KeyRotationIntervalSeconds"),
            SpekeKeyProvider=SpekeKeyProvider._deserialize(json_data.get("SpekeKeyProvider")),
            ConstantInitializationVector=json_data.get("ConstantInitializationVector"),
            EncryptionMethod=json_data.get("EncryptionMethod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CmafEncryption = CmafEncryption


@dataclass
class HlsManifest(BaseModel):
    Id: Optional[str]
    ManifestName: Optional[str]
    Url: Optional[str]
    PlaylistWindowSeconds: Optional[int]
    PlaylistType: Optional[str]
    AdMarkers: Optional[str]
    ProgramDateTimeIntervalSeconds: Optional[int]
    IncludeIframeOnlyStream: Optional[bool]
    AdTriggers: Optional[Sequence[str]]
    AdsOnDeliveryRestrictions: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HlsManifest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HlsManifest"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            ManifestName=json_data.get("ManifestName"),
            Url=json_data.get("Url"),
            PlaylistWindowSeconds=json_data.get("PlaylistWindowSeconds"),
            PlaylistType=json_data.get("PlaylistType"),
            AdMarkers=json_data.get("AdMarkers"),
            ProgramDateTimeIntervalSeconds=json_data.get("ProgramDateTimeIntervalSeconds"),
            IncludeIframeOnlyStream=json_data.get("IncludeIframeOnlyStream"),
            AdTriggers=json_data.get("AdTriggers"),
            AdsOnDeliveryRestrictions=json_data.get("AdsOnDeliveryRestrictions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HlsManifest = HlsManifest


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


