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
class AwsMediapackagev2Originendpoint(BaseModel):
    Arn: Optional[str]
    ChannelGroupName: Optional[str]
    ChannelName: Optional[str]
    ContainerType: Optional[str]
    CreatedAt: Optional[str]
    Description: Optional[str]
    HlsManifests: Optional[Sequence["_HlsManifestConfiguration"]]
    LowLatencyHlsManifests: Optional[Sequence["_LowLatencyHlsManifestConfiguration"]]
    ModifiedAt: Optional[str]
    OriginEndpointName: Optional[str]
    Segment: Optional["_Segment"]
    StartoverWindowSeconds: Optional[int]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMediapackagev2Originendpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMediapackagev2Originendpoint"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            ChannelGroupName=json_data.get("ChannelGroupName"),
            ChannelName=json_data.get("ChannelName"),
            ContainerType=json_data.get("ContainerType"),
            CreatedAt=json_data.get("CreatedAt"),
            Description=json_data.get("Description"),
            HlsManifests=deserialize_list(json_data.get("HlsManifests"), HlsManifestConfiguration),
            LowLatencyHlsManifests=deserialize_list(json_data.get("LowLatencyHlsManifests"), LowLatencyHlsManifestConfiguration),
            ModifiedAt=json_data.get("ModifiedAt"),
            OriginEndpointName=json_data.get("OriginEndpointName"),
            Segment=Segment._deserialize(json_data.get("Segment")),
            StartoverWindowSeconds=json_data.get("StartoverWindowSeconds"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMediapackagev2Originendpoint = AwsMediapackagev2Originendpoint


@dataclass
class HlsManifestConfiguration(BaseModel):
    ManifestName: Optional[str]
    Url: Optional[str]
    ChildManifestName: Optional[str]
    ManifestWindowSeconds: Optional[int]
    ProgramDateTimeIntervalSeconds: Optional[int]
    ScteHls: Optional["_ScteHls"]

    @classmethod
    def _deserialize(
        cls: Type["_HlsManifestConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HlsManifestConfiguration"]:
        if not json_data:
            return None
        return cls(
            ManifestName=json_data.get("ManifestName"),
            Url=json_data.get("Url"),
            ChildManifestName=json_data.get("ChildManifestName"),
            ManifestWindowSeconds=json_data.get("ManifestWindowSeconds"),
            ProgramDateTimeIntervalSeconds=json_data.get("ProgramDateTimeIntervalSeconds"),
            ScteHls=ScteHls._deserialize(json_data.get("ScteHls")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HlsManifestConfiguration = HlsManifestConfiguration


@dataclass
class ScteHls(BaseModel):
    AdMarkerHls: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScteHls"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScteHls"]:
        if not json_data:
            return None
        return cls(
            AdMarkerHls=json_data.get("AdMarkerHls"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScteHls = ScteHls


@dataclass
class LowLatencyHlsManifestConfiguration(BaseModel):
    ManifestName: Optional[str]
    Url: Optional[str]
    ChildManifestName: Optional[str]
    ManifestWindowSeconds: Optional[int]
    ProgramDateTimeIntervalSeconds: Optional[int]
    ScteHls: Optional["_ScteHls"]

    @classmethod
    def _deserialize(
        cls: Type["_LowLatencyHlsManifestConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LowLatencyHlsManifestConfiguration"]:
        if not json_data:
            return None
        return cls(
            ManifestName=json_data.get("ManifestName"),
            Url=json_data.get("Url"),
            ChildManifestName=json_data.get("ChildManifestName"),
            ManifestWindowSeconds=json_data.get("ManifestWindowSeconds"),
            ProgramDateTimeIntervalSeconds=json_data.get("ProgramDateTimeIntervalSeconds"),
            ScteHls=ScteHls._deserialize(json_data.get("ScteHls")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LowLatencyHlsManifestConfiguration = LowLatencyHlsManifestConfiguration


@dataclass
class Segment(BaseModel):
    SegmentDurationSeconds: Optional[int]
    SegmentName: Optional[str]
    TsUseAudioRenditionGroup: Optional[bool]
    IncludeIframeOnlyStreams: Optional[bool]
    TsIncludeDvbSubtitles: Optional[bool]
    Scte: Optional["_Scte"]
    Encryption: Optional["_Encryption"]

    @classmethod
    def _deserialize(
        cls: Type["_Segment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Segment"]:
        if not json_data:
            return None
        return cls(
            SegmentDurationSeconds=json_data.get("SegmentDurationSeconds"),
            SegmentName=json_data.get("SegmentName"),
            TsUseAudioRenditionGroup=json_data.get("TsUseAudioRenditionGroup"),
            IncludeIframeOnlyStreams=json_data.get("IncludeIframeOnlyStreams"),
            TsIncludeDvbSubtitles=json_data.get("TsIncludeDvbSubtitles"),
            Scte=Scte._deserialize(json_data.get("Scte")),
            Encryption=Encryption._deserialize(json_data.get("Encryption")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Segment = Segment


@dataclass
class Scte(BaseModel):
    ScteFilter: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Scte"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Scte"]:
        if not json_data:
            return None
        return cls(
            ScteFilter=json_data.get("ScteFilter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Scte = Scte


@dataclass
class Encryption(BaseModel):
    ConstantInitializationVector: Optional[str]
    EncryptionMethod: Optional["_EncryptionMethod"]
    KeyRotationIntervalSeconds: Optional[int]
    SpekeKeyProvider: Optional["_SpekeKeyProvider"]

    @classmethod
    def _deserialize(
        cls: Type["_Encryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Encryption"]:
        if not json_data:
            return None
        return cls(
            ConstantInitializationVector=json_data.get("ConstantInitializationVector"),
            EncryptionMethod=EncryptionMethod._deserialize(json_data.get("EncryptionMethod")),
            KeyRotationIntervalSeconds=json_data.get("KeyRotationIntervalSeconds"),
            SpekeKeyProvider=SpekeKeyProvider._deserialize(json_data.get("SpekeKeyProvider")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Encryption = Encryption


@dataclass
class EncryptionMethod(BaseModel):
    TsEncryptionMethod: Optional[str]
    CmafEncryptionMethod: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionMethod"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionMethod"]:
        if not json_data:
            return None
        return cls(
            TsEncryptionMethod=json_data.get("TsEncryptionMethod"),
            CmafEncryptionMethod=json_data.get("CmafEncryptionMethod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionMethod = EncryptionMethod


@dataclass
class SpekeKeyProvider(BaseModel):
    EncryptionContractConfiguration: Optional["_EncryptionContractConfiguration"]
    ResourceId: Optional[str]
    DrmSystems: Optional[Sequence[str]]
    RoleArn: Optional[str]
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
            ResourceId=json_data.get("ResourceId"),
            DrmSystems=json_data.get("DrmSystems"),
            RoleArn=json_data.get("RoleArn"),
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


