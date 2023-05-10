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
class AwsMediapackagePackagingconfiguration(BaseModel):
    Id: Optional[str]
    PackagingGroupId: Optional[str]
    Arn: Optional[str]
    CmafPackage: Optional["_CmafPackage"]
    DashPackage: Optional["_DashPackage"]
    HlsPackage: Optional["_HlsPackage"]
    MssPackage: Optional["_MssPackage"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMediapackagePackagingconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMediapackagePackagingconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            PackagingGroupId=json_data.get("PackagingGroupId"),
            Arn=json_data.get("Arn"),
            CmafPackage=CmafPackage._deserialize(json_data.get("CmafPackage")),
            DashPackage=DashPackage._deserialize(json_data.get("DashPackage")),
            HlsPackage=HlsPackage._deserialize(json_data.get("HlsPackage")),
            MssPackage=MssPackage._deserialize(json_data.get("MssPackage")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMediapackagePackagingconfiguration = AwsMediapackagePackagingconfiguration


@dataclass
class CmafPackage(BaseModel):
    Encryption: Optional["_CmafEncryption"]
    HlsManifests: Optional[Sequence["_HlsManifest"]]
    SegmentDurationSeconds: Optional[int]
    IncludeEncoderConfigurationInSegments: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CmafPackage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CmafPackage"]:
        if not json_data:
            return None
        return cls(
            Encryption=CmafEncryption._deserialize(json_data.get("Encryption")),
            HlsManifests=deserialize_list(json_data.get("HlsManifests"), HlsManifest),
            SegmentDurationSeconds=json_data.get("SegmentDurationSeconds"),
            IncludeEncoderConfigurationInSegments=json_data.get("IncludeEncoderConfigurationInSegments"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CmafPackage = CmafPackage


@dataclass
class CmafEncryption(BaseModel):
    SpekeKeyProvider: Optional["_SpekeKeyProvider"]

    @classmethod
    def _deserialize(
        cls: Type["_CmafEncryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CmafEncryption"]:
        if not json_data:
            return None
        return cls(
            SpekeKeyProvider=SpekeKeyProvider._deserialize(json_data.get("SpekeKeyProvider")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CmafEncryption = CmafEncryption


@dataclass
class SpekeKeyProvider(BaseModel):
    EncryptionContractConfiguration: Optional["_EncryptionContractConfiguration"]
    RoleArn: Optional[str]
    SystemIds: Optional[Sequence[str]]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SpekeKeyProvider"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpekeKeyProvider"]:
        if not json_data:
            return None
        return cls(
            EncryptionContractConfiguration=EncryptionContractConfiguration._deserialize(json_data.get("EncryptionContractConfiguration")),
            RoleArn=json_data.get("RoleArn"),
            SystemIds=json_data.get("SystemIds"),
            Url=json_data.get("Url"),
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
class HlsManifest(BaseModel):
    AdMarkers: Optional[str]
    IncludeIframeOnlyStream: Optional[bool]
    ManifestName: Optional[str]
    ProgramDateTimeIntervalSeconds: Optional[int]
    RepeatExtXKey: Optional[bool]
    StreamSelection: Optional["_StreamSelection"]

    @classmethod
    def _deserialize(
        cls: Type["_HlsManifest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HlsManifest"]:
        if not json_data:
            return None
        return cls(
            AdMarkers=json_data.get("AdMarkers"),
            IncludeIframeOnlyStream=json_data.get("IncludeIframeOnlyStream"),
            ManifestName=json_data.get("ManifestName"),
            ProgramDateTimeIntervalSeconds=json_data.get("ProgramDateTimeIntervalSeconds"),
            RepeatExtXKey=json_data.get("RepeatExtXKey"),
            StreamSelection=StreamSelection._deserialize(json_data.get("StreamSelection")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HlsManifest = HlsManifest


@dataclass
class StreamSelection(BaseModel):
    MaxVideoBitsPerSecond: Optional[int]
    MinVideoBitsPerSecond: Optional[int]
    StreamOrder: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StreamSelection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StreamSelection"]:
        if not json_data:
            return None
        return cls(
            MaxVideoBitsPerSecond=json_data.get("MaxVideoBitsPerSecond"),
            MinVideoBitsPerSecond=json_data.get("MinVideoBitsPerSecond"),
            StreamOrder=json_data.get("StreamOrder"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StreamSelection = StreamSelection


@dataclass
class DashPackage(BaseModel):
    DashManifests: Optional[Sequence["_DashManifest"]]
    Encryption: Optional["_DashEncryption"]
    PeriodTriggers: Optional[Sequence[str]]
    SegmentDurationSeconds: Optional[int]
    SegmentTemplateFormat: Optional[str]
    IncludeEncoderConfigurationInSegments: Optional[bool]
    IncludeIframeOnlyStream: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DashPackage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DashPackage"]:
        if not json_data:
            return None
        return cls(
            DashManifests=deserialize_list(json_data.get("DashManifests"), DashManifest),
            Encryption=DashEncryption._deserialize(json_data.get("Encryption")),
            PeriodTriggers=json_data.get("PeriodTriggers"),
            SegmentDurationSeconds=json_data.get("SegmentDurationSeconds"),
            SegmentTemplateFormat=json_data.get("SegmentTemplateFormat"),
            IncludeEncoderConfigurationInSegments=json_data.get("IncludeEncoderConfigurationInSegments"),
            IncludeIframeOnlyStream=json_data.get("IncludeIframeOnlyStream"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DashPackage = DashPackage


@dataclass
class DashManifest(BaseModel):
    ManifestLayout: Optional[str]
    ManifestName: Optional[str]
    MinBufferTimeSeconds: Optional[int]
    Profile: Optional[str]
    ScteMarkersSource: Optional[str]
    StreamSelection: Optional["_StreamSelection"]

    @classmethod
    def _deserialize(
        cls: Type["_DashManifest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DashManifest"]:
        if not json_data:
            return None
        return cls(
            ManifestLayout=json_data.get("ManifestLayout"),
            ManifestName=json_data.get("ManifestName"),
            MinBufferTimeSeconds=json_data.get("MinBufferTimeSeconds"),
            Profile=json_data.get("Profile"),
            ScteMarkersSource=json_data.get("ScteMarkersSource"),
            StreamSelection=StreamSelection._deserialize(json_data.get("StreamSelection")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DashManifest = DashManifest


@dataclass
class DashEncryption(BaseModel):
    SpekeKeyProvider: Optional["_SpekeKeyProvider"]

    @classmethod
    def _deserialize(
        cls: Type["_DashEncryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DashEncryption"]:
        if not json_data:
            return None
        return cls(
            SpekeKeyProvider=SpekeKeyProvider._deserialize(json_data.get("SpekeKeyProvider")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DashEncryption = DashEncryption


@dataclass
class HlsPackage(BaseModel):
    Encryption: Optional["_HlsEncryption"]
    HlsManifests: Optional[Sequence["_HlsManifest"]]
    IncludeDvbSubtitles: Optional[bool]
    SegmentDurationSeconds: Optional[int]
    UseAudioRenditionGroup: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_HlsPackage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HlsPackage"]:
        if not json_data:
            return None
        return cls(
            Encryption=HlsEncryption._deserialize(json_data.get("Encryption")),
            HlsManifests=deserialize_list(json_data.get("HlsManifests"), HlsManifest),
            IncludeDvbSubtitles=json_data.get("IncludeDvbSubtitles"),
            SegmentDurationSeconds=json_data.get("SegmentDurationSeconds"),
            UseAudioRenditionGroup=json_data.get("UseAudioRenditionGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HlsPackage = HlsPackage


@dataclass
class HlsEncryption(BaseModel):
    ConstantInitializationVector: Optional[str]
    EncryptionMethod: Optional[str]
    SpekeKeyProvider: Optional["_SpekeKeyProvider"]

    @classmethod
    def _deserialize(
        cls: Type["_HlsEncryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HlsEncryption"]:
        if not json_data:
            return None
        return cls(
            ConstantInitializationVector=json_data.get("ConstantInitializationVector"),
            EncryptionMethod=json_data.get("EncryptionMethod"),
            SpekeKeyProvider=SpekeKeyProvider._deserialize(json_data.get("SpekeKeyProvider")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HlsEncryption = HlsEncryption


@dataclass
class MssPackage(BaseModel):
    Encryption: Optional["_MssEncryption"]
    MssManifests: Optional[Sequence["_MssManifest"]]
    SegmentDurationSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_MssPackage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MssPackage"]:
        if not json_data:
            return None
        return cls(
            Encryption=MssEncryption._deserialize(json_data.get("Encryption")),
            MssManifests=deserialize_list(json_data.get("MssManifests"), MssManifest),
            SegmentDurationSeconds=json_data.get("SegmentDurationSeconds"),
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
class MssManifest(BaseModel):
    ManifestName: Optional[str]
    StreamSelection: Optional["_StreamSelection"]

    @classmethod
    def _deserialize(
        cls: Type["_MssManifest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MssManifest"]:
        if not json_data:
            return None
        return cls(
            ManifestName=json_data.get("ManifestName"),
            StreamSelection=StreamSelection._deserialize(json_data.get("StreamSelection")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MssManifest = MssManifest


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


