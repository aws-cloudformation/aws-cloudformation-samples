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
class AwsMediatailorPlaybackconfiguration(BaseModel):
    AdDecisionServerUrl: Optional[str]
    AvailSuppression: Optional["_AvailSuppression"]
    Bumper: Optional["_Bumper"]
    CdnConfiguration: Optional["_CdnConfiguration"]
    ConfigurationAliases: Optional[MutableMapping[str, MutableMapping[str, Any]]]
    DashConfiguration: Optional["_DashConfiguration"]
    LivePreRollConfiguration: Optional["_LivePreRollConfiguration"]
    ManifestProcessingRules: Optional["_ManifestProcessingRules"]
    Name: Optional[str]
    PersonalizationThresholdSeconds: Optional[int]
    SessionInitializationEndpointPrefix: Optional[str]
    HlsConfiguration: Optional["_HlsConfiguration"]
    PlaybackConfigurationArn: Optional[str]
    PlaybackEndpointPrefix: Optional[str]
    SlateAdUrl: Optional[str]
    Tags: Optional[Any]
    TranscodeProfileName: Optional[str]
    VideoContentSourceUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMediatailorPlaybackconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMediatailorPlaybackconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AdDecisionServerUrl=json_data.get("AdDecisionServerUrl"),
            AvailSuppression=AvailSuppression._deserialize(json_data.get("AvailSuppression")),
            Bumper=Bumper._deserialize(json_data.get("Bumper")),
            CdnConfiguration=CdnConfiguration._deserialize(json_data.get("CdnConfiguration")),
            ConfigurationAliases=json_data.get("ConfigurationAliases"),
            DashConfiguration=DashConfiguration._deserialize(json_data.get("DashConfiguration")),
            LivePreRollConfiguration=LivePreRollConfiguration._deserialize(json_data.get("LivePreRollConfiguration")),
            ManifestProcessingRules=ManifestProcessingRules._deserialize(json_data.get("ManifestProcessingRules")),
            Name=json_data.get("Name"),
            PersonalizationThresholdSeconds=json_data.get("PersonalizationThresholdSeconds"),
            SessionInitializationEndpointPrefix=json_data.get("SessionInitializationEndpointPrefix"),
            HlsConfiguration=HlsConfiguration._deserialize(json_data.get("HlsConfiguration")),
            PlaybackConfigurationArn=json_data.get("PlaybackConfigurationArn"),
            PlaybackEndpointPrefix=json_data.get("PlaybackEndpointPrefix"),
            SlateAdUrl=json_data.get("SlateAdUrl"),
            Tags=json_data.get("Tags"),
            TranscodeProfileName=json_data.get("TranscodeProfileName"),
            VideoContentSourceUrl=json_data.get("VideoContentSourceUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMediatailorPlaybackconfiguration = AwsMediatailorPlaybackconfiguration


@dataclass
class AvailSuppression(BaseModel):
    Mode: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AvailSuppression"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AvailSuppression"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AvailSuppression = AvailSuppression


@dataclass
class Bumper(BaseModel):
    StartUrl: Optional[str]
    EndUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Bumper"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Bumper"]:
        if not json_data:
            return None
        return cls(
            StartUrl=json_data.get("StartUrl"),
            EndUrl=json_data.get("EndUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Bumper = Bumper


@dataclass
class CdnConfiguration(BaseModel):
    AdSegmentUrlPrefix: Optional[str]
    ContentSegmentUrlPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CdnConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CdnConfiguration"]:
        if not json_data:
            return None
        return cls(
            AdSegmentUrlPrefix=json_data.get("AdSegmentUrlPrefix"),
            ContentSegmentUrlPrefix=json_data.get("ContentSegmentUrlPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CdnConfiguration = CdnConfiguration


@dataclass
class DashConfiguration(BaseModel):
    MpdLocation: Optional[str]
    OriginManifestType: Optional[str]
    ManifestEndpointPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DashConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DashConfiguration"]:
        if not json_data:
            return None
        return cls(
            MpdLocation=json_data.get("MpdLocation"),
            OriginManifestType=json_data.get("OriginManifestType"),
            ManifestEndpointPrefix=json_data.get("ManifestEndpointPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DashConfiguration = DashConfiguration


@dataclass
class LivePreRollConfiguration(BaseModel):
    AdDecisionServerUrl: Optional[str]
    MaxDurationSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_LivePreRollConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LivePreRollConfiguration"]:
        if not json_data:
            return None
        return cls(
            AdDecisionServerUrl=json_data.get("AdDecisionServerUrl"),
            MaxDurationSeconds=json_data.get("MaxDurationSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LivePreRollConfiguration = LivePreRollConfiguration


@dataclass
class ManifestProcessingRules(BaseModel):
    AdMarkerPassthrough: Optional["_AdMarkerPassthrough"]

    @classmethod
    def _deserialize(
        cls: Type["_ManifestProcessingRules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManifestProcessingRules"]:
        if not json_data:
            return None
        return cls(
            AdMarkerPassthrough=AdMarkerPassthrough._deserialize(json_data.get("AdMarkerPassthrough")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManifestProcessingRules = ManifestProcessingRules


@dataclass
class AdMarkerPassthrough(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AdMarkerPassthrough"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdMarkerPassthrough"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdMarkerPassthrough = AdMarkerPassthrough


@dataclass
class HlsConfiguration(BaseModel):
    ManifestEndpointPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HlsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HlsConfiguration"]:
        if not json_data:
            return None
        return cls(
            ManifestEndpointPrefix=json_data.get("ManifestEndpointPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HlsConfiguration = HlsConfiguration


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


