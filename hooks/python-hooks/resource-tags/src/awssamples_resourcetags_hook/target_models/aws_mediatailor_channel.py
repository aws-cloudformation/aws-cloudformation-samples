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
class AwsMediatailorChannel(BaseModel):
    Arn: Optional[str]
    ChannelName: Optional[str]
    FillerSlate: Optional["_SlateSource"]
    LogConfiguration: Optional["_LogConfigurationForChannel"]
    Outputs: Optional[Sequence["_RequestOutputItem"]]
    PlaybackMode: Optional[str]
    Tags: Optional[Any]
    Tier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMediatailorChannel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMediatailorChannel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            ChannelName=json_data.get("ChannelName"),
            FillerSlate=SlateSource._deserialize(json_data.get("FillerSlate")),
            LogConfiguration=LogConfigurationForChannel._deserialize(json_data.get("LogConfiguration")),
            Outputs=deserialize_list(json_data.get("Outputs"), RequestOutputItem),
            PlaybackMode=json_data.get("PlaybackMode"),
            Tags=json_data.get("Tags"),
            Tier=json_data.get("Tier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMediatailorChannel = AwsMediatailorChannel


@dataclass
class SlateSource(BaseModel):
    SourceLocationName: Optional[str]
    VodSourceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SlateSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlateSource"]:
        if not json_data:
            return None
        return cls(
            SourceLocationName=json_data.get("SourceLocationName"),
            VodSourceName=json_data.get("VodSourceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlateSource = SlateSource


@dataclass
class LogConfigurationForChannel(BaseModel):
    LogTypes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_LogConfigurationForChannel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogConfigurationForChannel"]:
        if not json_data:
            return None
        return cls(
            LogTypes=json_data.get("LogTypes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogConfigurationForChannel = LogConfigurationForChannel


@dataclass
class RequestOutputItem(BaseModel):
    DashPlaylistSettings: Optional["_DashPlaylistSettings"]
    HlsPlaylistSettings: Optional["_HlsPlaylistSettings"]
    ManifestName: Optional[str]
    SourceGroup: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestOutputItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestOutputItem"]:
        if not json_data:
            return None
        return cls(
            DashPlaylistSettings=DashPlaylistSettings._deserialize(json_data.get("DashPlaylistSettings")),
            HlsPlaylistSettings=HlsPlaylistSettings._deserialize(json_data.get("HlsPlaylistSettings")),
            ManifestName=json_data.get("ManifestName"),
            SourceGroup=json_data.get("SourceGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestOutputItem = RequestOutputItem


@dataclass
class DashPlaylistSettings(BaseModel):
    ManifestWindowSeconds: Optional[float]
    MinBufferTimeSeconds: Optional[float]
    MinUpdatePeriodSeconds: Optional[float]
    SuggestedPresentationDelaySeconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DashPlaylistSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DashPlaylistSettings"]:
        if not json_data:
            return None
        return cls(
            ManifestWindowSeconds=json_data.get("ManifestWindowSeconds"),
            MinBufferTimeSeconds=json_data.get("MinBufferTimeSeconds"),
            MinUpdatePeriodSeconds=json_data.get("MinUpdatePeriodSeconds"),
            SuggestedPresentationDelaySeconds=json_data.get("SuggestedPresentationDelaySeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DashPlaylistSettings = DashPlaylistSettings


@dataclass
class HlsPlaylistSettings(BaseModel):
    ManifestWindowSeconds: Optional[float]
    AdMarkupType: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HlsPlaylistSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HlsPlaylistSettings"]:
        if not json_data:
            return None
        return cls(
            ManifestWindowSeconds=json_data.get("ManifestWindowSeconds"),
            AdMarkupType=json_data.get("AdMarkupType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HlsPlaylistSettings = HlsPlaylistSettings


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


