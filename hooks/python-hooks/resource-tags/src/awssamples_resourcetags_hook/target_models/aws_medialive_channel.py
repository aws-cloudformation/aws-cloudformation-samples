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
class AwsMedialiveChannel(BaseModel):
    InputAttachments: Optional[Sequence["_InputAttachment"]]
    InputSpecification: Optional["_InputSpecification"]
    Destinations: Optional[Sequence["_OutputDestination"]]
    Vpc: Optional["_VpcOutputSettings"]
    Maintenance: Optional["_MaintenanceCreateSettings"]
    LogLevel: Optional[str]
    RoleArn: Optional[str]
    Name: Optional[str]
    ChannelClass: Optional[str]
    EncoderSettings: Optional["_EncoderSettings"]
    CdiInputSpecification: Optional["_CdiInputSpecification"]
    Id: Optional[str]
    Arn: Optional[str]
    Inputs: Optional[Sequence[str]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMedialiveChannel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMedialiveChannel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            InputAttachments=deserialize_list(json_data.get("InputAttachments"), InputAttachment),
            InputSpecification=InputSpecification._deserialize(json_data.get("InputSpecification")),
            Destinations=deserialize_list(json_data.get("Destinations"), OutputDestination),
            Vpc=VpcOutputSettings._deserialize(json_data.get("Vpc")),
            Maintenance=MaintenanceCreateSettings._deserialize(json_data.get("Maintenance")),
            LogLevel=json_data.get("LogLevel"),
            RoleArn=json_data.get("RoleArn"),
            Name=json_data.get("Name"),
            ChannelClass=json_data.get("ChannelClass"),
            EncoderSettings=EncoderSettings._deserialize(json_data.get("EncoderSettings")),
            CdiInputSpecification=CdiInputSpecification._deserialize(json_data.get("CdiInputSpecification")),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Inputs=json_data.get("Inputs"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMedialiveChannel = AwsMedialiveChannel


@dataclass
class InputAttachment(BaseModel):
    InputAttachmentName: Optional[str]
    InputId: Optional[str]
    AutomaticInputFailoverSettings: Optional["_AutomaticInputFailoverSettings"]
    InputSettings: Optional["_InputSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_InputAttachment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputAttachment"]:
        if not json_data:
            return None
        return cls(
            InputAttachmentName=json_data.get("InputAttachmentName"),
            InputId=json_data.get("InputId"),
            AutomaticInputFailoverSettings=AutomaticInputFailoverSettings._deserialize(json_data.get("AutomaticInputFailoverSettings")),
            InputSettings=InputSettings._deserialize(json_data.get("InputSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputAttachment = InputAttachment


@dataclass
class AutomaticInputFailoverSettings(BaseModel):
    ErrorClearTimeMsec: Optional[int]
    FailoverConditions: Optional[Sequence["_FailoverCondition"]]
    InputPreference: Optional[str]
    SecondaryInputId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutomaticInputFailoverSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutomaticInputFailoverSettings"]:
        if not json_data:
            return None
        return cls(
            ErrorClearTimeMsec=json_data.get("ErrorClearTimeMsec"),
            FailoverConditions=deserialize_list(json_data.get("FailoverConditions"), FailoverCondition),
            InputPreference=json_data.get("InputPreference"),
            SecondaryInputId=json_data.get("SecondaryInputId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutomaticInputFailoverSettings = AutomaticInputFailoverSettings


@dataclass
class FailoverCondition(BaseModel):
    FailoverConditionSettings: Optional["_FailoverConditionSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_FailoverCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FailoverCondition"]:
        if not json_data:
            return None
        return cls(
            FailoverConditionSettings=FailoverConditionSettings._deserialize(json_data.get("FailoverConditionSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FailoverCondition = FailoverCondition


@dataclass
class FailoverConditionSettings(BaseModel):
    AudioSilenceSettings: Optional["_AudioSilenceFailoverSettings"]
    VideoBlackSettings: Optional["_VideoBlackFailoverSettings"]
    InputLossSettings: Optional["_InputLossFailoverSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_FailoverConditionSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FailoverConditionSettings"]:
        if not json_data:
            return None
        return cls(
            AudioSilenceSettings=AudioSilenceFailoverSettings._deserialize(json_data.get("AudioSilenceSettings")),
            VideoBlackSettings=VideoBlackFailoverSettings._deserialize(json_data.get("VideoBlackSettings")),
            InputLossSettings=InputLossFailoverSettings._deserialize(json_data.get("InputLossSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FailoverConditionSettings = FailoverConditionSettings


@dataclass
class AudioSilenceFailoverSettings(BaseModel):
    AudioSelectorName: Optional[str]
    AudioSilenceThresholdMsec: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AudioSilenceFailoverSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioSilenceFailoverSettings"]:
        if not json_data:
            return None
        return cls(
            AudioSelectorName=json_data.get("AudioSelectorName"),
            AudioSilenceThresholdMsec=json_data.get("AudioSilenceThresholdMsec"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioSilenceFailoverSettings = AudioSilenceFailoverSettings


@dataclass
class VideoBlackFailoverSettings(BaseModel):
    BlackDetectThreshold: Optional[float]
    VideoBlackThresholdMsec: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_VideoBlackFailoverSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VideoBlackFailoverSettings"]:
        if not json_data:
            return None
        return cls(
            BlackDetectThreshold=json_data.get("BlackDetectThreshold"),
            VideoBlackThresholdMsec=json_data.get("VideoBlackThresholdMsec"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VideoBlackFailoverSettings = VideoBlackFailoverSettings


@dataclass
class InputLossFailoverSettings(BaseModel):
    InputLossThresholdMsec: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_InputLossFailoverSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputLossFailoverSettings"]:
        if not json_data:
            return None
        return cls(
            InputLossThresholdMsec=json_data.get("InputLossThresholdMsec"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputLossFailoverSettings = InputLossFailoverSettings


@dataclass
class InputSettings(BaseModel):
    Scte35Pid: Optional[int]
    DeblockFilter: Optional[str]
    FilterStrength: Optional[int]
    InputFilter: Optional[str]
    SourceEndBehavior: Optional[str]
    VideoSelector: Optional["_VideoSelector"]
    Smpte2038DataPreference: Optional[str]
    AudioSelectors: Optional[Sequence["_AudioSelector"]]
    CaptionSelectors: Optional[Sequence["_CaptionSelector"]]
    DenoiseFilter: Optional[str]
    NetworkInputSettings: Optional["_NetworkInputSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_InputSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputSettings"]:
        if not json_data:
            return None
        return cls(
            Scte35Pid=json_data.get("Scte35Pid"),
            DeblockFilter=json_data.get("DeblockFilter"),
            FilterStrength=json_data.get("FilterStrength"),
            InputFilter=json_data.get("InputFilter"),
            SourceEndBehavior=json_data.get("SourceEndBehavior"),
            VideoSelector=VideoSelector._deserialize(json_data.get("VideoSelector")),
            Smpte2038DataPreference=json_data.get("Smpte2038DataPreference"),
            AudioSelectors=deserialize_list(json_data.get("AudioSelectors"), AudioSelector),
            CaptionSelectors=deserialize_list(json_data.get("CaptionSelectors"), CaptionSelector),
            DenoiseFilter=json_data.get("DenoiseFilter"),
            NetworkInputSettings=NetworkInputSettings._deserialize(json_data.get("NetworkInputSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputSettings = InputSettings


@dataclass
class VideoSelector(BaseModel):
    ColorSpaceSettings: Optional["_VideoSelectorColorSpaceSettings"]
    ColorSpaceUsage: Optional[str]
    SelectorSettings: Optional["_VideoSelectorSettings"]
    ColorSpace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VideoSelector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VideoSelector"]:
        if not json_data:
            return None
        return cls(
            ColorSpaceSettings=VideoSelectorColorSpaceSettings._deserialize(json_data.get("ColorSpaceSettings")),
            ColorSpaceUsage=json_data.get("ColorSpaceUsage"),
            SelectorSettings=VideoSelectorSettings._deserialize(json_data.get("SelectorSettings")),
            ColorSpace=json_data.get("ColorSpace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VideoSelector = VideoSelector


@dataclass
class VideoSelectorColorSpaceSettings(BaseModel):
    Hdr10Settings: Optional["_Hdr10Settings"]

    @classmethod
    def _deserialize(
        cls: Type["_VideoSelectorColorSpaceSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VideoSelectorColorSpaceSettings"]:
        if not json_data:
            return None
        return cls(
            Hdr10Settings=Hdr10Settings._deserialize(json_data.get("Hdr10Settings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VideoSelectorColorSpaceSettings = VideoSelectorColorSpaceSettings


@dataclass
class Hdr10Settings(BaseModel):
    MaxCll: Optional[int]
    MaxFall: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Hdr10Settings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Hdr10Settings"]:
        if not json_data:
            return None
        return cls(
            MaxCll=json_data.get("MaxCll"),
            MaxFall=json_data.get("MaxFall"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Hdr10Settings = Hdr10Settings


@dataclass
class VideoSelectorSettings(BaseModel):
    VideoSelectorProgramId: Optional["_VideoSelectorProgramId"]
    VideoSelectorPid: Optional["_VideoSelectorPid"]

    @classmethod
    def _deserialize(
        cls: Type["_VideoSelectorSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VideoSelectorSettings"]:
        if not json_data:
            return None
        return cls(
            VideoSelectorProgramId=VideoSelectorProgramId._deserialize(json_data.get("VideoSelectorProgramId")),
            VideoSelectorPid=VideoSelectorPid._deserialize(json_data.get("VideoSelectorPid")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VideoSelectorSettings = VideoSelectorSettings


@dataclass
class VideoSelectorProgramId(BaseModel):
    ProgramId: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_VideoSelectorProgramId"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VideoSelectorProgramId"]:
        if not json_data:
            return None
        return cls(
            ProgramId=json_data.get("ProgramId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VideoSelectorProgramId = VideoSelectorProgramId


@dataclass
class VideoSelectorPid(BaseModel):
    Pid: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_VideoSelectorPid"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VideoSelectorPid"]:
        if not json_data:
            return None
        return cls(
            Pid=json_data.get("Pid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VideoSelectorPid = VideoSelectorPid


@dataclass
class AudioSelector(BaseModel):
    SelectorSettings: Optional["_AudioSelectorSettings"]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AudioSelector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioSelector"]:
        if not json_data:
            return None
        return cls(
            SelectorSettings=AudioSelectorSettings._deserialize(json_data.get("SelectorSettings")),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioSelector = AudioSelector


@dataclass
class AudioSelectorSettings(BaseModel):
    AudioLanguageSelection: Optional["_AudioLanguageSelection"]
    AudioTrackSelection: Optional["_AudioTrackSelection"]
    AudioPidSelection: Optional["_AudioPidSelection"]
    AudioHlsRenditionSelection: Optional["_AudioHlsRenditionSelection"]

    @classmethod
    def _deserialize(
        cls: Type["_AudioSelectorSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioSelectorSettings"]:
        if not json_data:
            return None
        return cls(
            AudioLanguageSelection=AudioLanguageSelection._deserialize(json_data.get("AudioLanguageSelection")),
            AudioTrackSelection=AudioTrackSelection._deserialize(json_data.get("AudioTrackSelection")),
            AudioPidSelection=AudioPidSelection._deserialize(json_data.get("AudioPidSelection")),
            AudioHlsRenditionSelection=AudioHlsRenditionSelection._deserialize(json_data.get("AudioHlsRenditionSelection")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioSelectorSettings = AudioSelectorSettings


@dataclass
class AudioLanguageSelection(BaseModel):
    LanguageCode: Optional[str]
    LanguageSelectionPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AudioLanguageSelection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioLanguageSelection"]:
        if not json_data:
            return None
        return cls(
            LanguageCode=json_data.get("LanguageCode"),
            LanguageSelectionPolicy=json_data.get("LanguageSelectionPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioLanguageSelection = AudioLanguageSelection


@dataclass
class AudioTrackSelection(BaseModel):
    DolbyEDecode: Optional["_AudioDolbyEDecode"]
    Tracks: Optional[Sequence["_AudioTrack"]]

    @classmethod
    def _deserialize(
        cls: Type["_AudioTrackSelection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioTrackSelection"]:
        if not json_data:
            return None
        return cls(
            DolbyEDecode=AudioDolbyEDecode._deserialize(json_data.get("DolbyEDecode")),
            Tracks=deserialize_list(json_data.get("Tracks"), AudioTrack),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioTrackSelection = AudioTrackSelection


@dataclass
class AudioDolbyEDecode(BaseModel):
    ProgramSelection: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AudioDolbyEDecode"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioDolbyEDecode"]:
        if not json_data:
            return None
        return cls(
            ProgramSelection=json_data.get("ProgramSelection"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioDolbyEDecode = AudioDolbyEDecode


@dataclass
class AudioTrack(BaseModel):
    Track: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AudioTrack"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioTrack"]:
        if not json_data:
            return None
        return cls(
            Track=json_data.get("Track"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioTrack = AudioTrack


@dataclass
class AudioPidSelection(BaseModel):
    Pid: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AudioPidSelection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioPidSelection"]:
        if not json_data:
            return None
        return cls(
            Pid=json_data.get("Pid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioPidSelection = AudioPidSelection


@dataclass
class AudioHlsRenditionSelection(BaseModel):
    GroupId: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AudioHlsRenditionSelection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioHlsRenditionSelection"]:
        if not json_data:
            return None
        return cls(
            GroupId=json_data.get("GroupId"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioHlsRenditionSelection = AudioHlsRenditionSelection


@dataclass
class CaptionSelector(BaseModel):
    LanguageCode: Optional[str]
    SelectorSettings: Optional["_CaptionSelectorSettings"]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CaptionSelector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaptionSelector"]:
        if not json_data:
            return None
        return cls(
            LanguageCode=json_data.get("LanguageCode"),
            SelectorSettings=CaptionSelectorSettings._deserialize(json_data.get("SelectorSettings")),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CaptionSelector = CaptionSelector


@dataclass
class CaptionSelectorSettings(BaseModel):
    DvbSubSourceSettings: Optional["_DvbSubSourceSettings"]
    Scte27SourceSettings: Optional["_Scte27SourceSettings"]
    AribSourceSettings: Optional[MutableMapping[str, Any]]
    EmbeddedSourceSettings: Optional["_EmbeddedSourceSettings"]
    Scte20SourceSettings: Optional["_Scte20SourceSettings"]
    TeletextSourceSettings: Optional["_TeletextSourceSettings"]
    AncillarySourceSettings: Optional["_AncillarySourceSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_CaptionSelectorSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaptionSelectorSettings"]:
        if not json_data:
            return None
        return cls(
            DvbSubSourceSettings=DvbSubSourceSettings._deserialize(json_data.get("DvbSubSourceSettings")),
            Scte27SourceSettings=Scte27SourceSettings._deserialize(json_data.get("Scte27SourceSettings")),
            AribSourceSettings=json_data.get("AribSourceSettings"),
            EmbeddedSourceSettings=EmbeddedSourceSettings._deserialize(json_data.get("EmbeddedSourceSettings")),
            Scte20SourceSettings=Scte20SourceSettings._deserialize(json_data.get("Scte20SourceSettings")),
            TeletextSourceSettings=TeletextSourceSettings._deserialize(json_data.get("TeletextSourceSettings")),
            AncillarySourceSettings=AncillarySourceSettings._deserialize(json_data.get("AncillarySourceSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CaptionSelectorSettings = CaptionSelectorSettings


@dataclass
class DvbSubSourceSettings(BaseModel):
    OcrLanguage: Optional[str]
    Pid: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_DvbSubSourceSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DvbSubSourceSettings"]:
        if not json_data:
            return None
        return cls(
            OcrLanguage=json_data.get("OcrLanguage"),
            Pid=json_data.get("Pid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DvbSubSourceSettings = DvbSubSourceSettings


@dataclass
class Scte27SourceSettings(BaseModel):
    OcrLanguage: Optional[str]
    Pid: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Scte27SourceSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Scte27SourceSettings"]:
        if not json_data:
            return None
        return cls(
            OcrLanguage=json_data.get("OcrLanguage"),
            Pid=json_data.get("Pid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Scte27SourceSettings = Scte27SourceSettings


@dataclass
class EmbeddedSourceSettings(BaseModel):
    Source608ChannelNumber: Optional[int]
    Scte20Detection: Optional[str]
    Source608TrackNumber: Optional[int]
    Convert608To708: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EmbeddedSourceSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmbeddedSourceSettings"]:
        if not json_data:
            return None
        return cls(
            Source608ChannelNumber=json_data.get("Source608ChannelNumber"),
            Scte20Detection=json_data.get("Scte20Detection"),
            Source608TrackNumber=json_data.get("Source608TrackNumber"),
            Convert608To708=json_data.get("Convert608To708"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmbeddedSourceSettings = EmbeddedSourceSettings


@dataclass
class Scte20SourceSettings(BaseModel):
    Source608ChannelNumber: Optional[int]
    Convert608To708: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Scte20SourceSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Scte20SourceSettings"]:
        if not json_data:
            return None
        return cls(
            Source608ChannelNumber=json_data.get("Source608ChannelNumber"),
            Convert608To708=json_data.get("Convert608To708"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Scte20SourceSettings = Scte20SourceSettings


@dataclass
class TeletextSourceSettings(BaseModel):
    OutputRectangle: Optional["_CaptionRectangle"]
    PageNumber: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TeletextSourceSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TeletextSourceSettings"]:
        if not json_data:
            return None
        return cls(
            OutputRectangle=CaptionRectangle._deserialize(json_data.get("OutputRectangle")),
            PageNumber=json_data.get("PageNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TeletextSourceSettings = TeletextSourceSettings


@dataclass
class CaptionRectangle(BaseModel):
    Height: Optional[float]
    TopOffset: Optional[float]
    Width: Optional[float]
    LeftOffset: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CaptionRectangle"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaptionRectangle"]:
        if not json_data:
            return None
        return cls(
            Height=json_data.get("Height"),
            TopOffset=json_data.get("TopOffset"),
            Width=json_data.get("Width"),
            LeftOffset=json_data.get("LeftOffset"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CaptionRectangle = CaptionRectangle


@dataclass
class AncillarySourceSettings(BaseModel):
    SourceAncillaryChannelNumber: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AncillarySourceSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AncillarySourceSettings"]:
        if not json_data:
            return None
        return cls(
            SourceAncillaryChannelNumber=json_data.get("SourceAncillaryChannelNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AncillarySourceSettings = AncillarySourceSettings


@dataclass
class NetworkInputSettings(BaseModel):
    ServerValidation: Optional[str]
    HlsInputSettings: Optional["_HlsInputSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInputSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInputSettings"]:
        if not json_data:
            return None
        return cls(
            ServerValidation=json_data.get("ServerValidation"),
            HlsInputSettings=HlsInputSettings._deserialize(json_data.get("HlsInputSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInputSettings = NetworkInputSettings


@dataclass
class HlsInputSettings(BaseModel):
    Scte35Source: Optional[str]
    BufferSegments: Optional[int]
    RetryInterval: Optional[int]
    Retries: Optional[int]
    Bandwidth: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_HlsInputSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HlsInputSettings"]:
        if not json_data:
            return None
        return cls(
            Scte35Source=json_data.get("Scte35Source"),
            BufferSegments=json_data.get("BufferSegments"),
            RetryInterval=json_data.get("RetryInterval"),
            Retries=json_data.get("Retries"),
            Bandwidth=json_data.get("Bandwidth"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HlsInputSettings = HlsInputSettings


@dataclass
class InputSpecification(BaseModel):
    Codec: Optional[str]
    MaximumBitrate: Optional[str]
    Resolution: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputSpecification"]:
        if not json_data:
            return None
        return cls(
            Codec=json_data.get("Codec"),
            MaximumBitrate=json_data.get("MaximumBitrate"),
            Resolution=json_data.get("Resolution"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputSpecification = InputSpecification


@dataclass
class OutputDestination(BaseModel):
    Id: Optional[str]
    MultiplexSettings: Optional["_MultiplexProgramChannelDestinationSettings"]
    Settings: Optional[Sequence["_OutputDestinationSettings"]]
    MediaPackageSettings: Optional[Sequence["_MediaPackageOutputDestinationSettings"]]

    @classmethod
    def _deserialize(
        cls: Type["_OutputDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputDestination"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            MultiplexSettings=MultiplexProgramChannelDestinationSettings._deserialize(json_data.get("MultiplexSettings")),
            Settings=deserialize_list(json_data.get("Settings"), OutputDestinationSettings),
            MediaPackageSettings=deserialize_list(json_data.get("MediaPackageSettings"), MediaPackageOutputDestinationSettings),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputDestination = OutputDestination


@dataclass
class MultiplexProgramChannelDestinationSettings(BaseModel):
    ProgramName: Optional[str]
    MultiplexId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MultiplexProgramChannelDestinationSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MultiplexProgramChannelDestinationSettings"]:
        if not json_data:
            return None
        return cls(
            ProgramName=json_data.get("ProgramName"),
            MultiplexId=json_data.get("MultiplexId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MultiplexProgramChannelDestinationSettings = MultiplexProgramChannelDestinationSettings


@dataclass
class OutputDestinationSettings(BaseModel):
    StreamName: Optional[str]
    PasswordParam: Optional[str]
    Username: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutputDestinationSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputDestinationSettings"]:
        if not json_data:
            return None
        return cls(
            StreamName=json_data.get("StreamName"),
            PasswordParam=json_data.get("PasswordParam"),
            Username=json_data.get("Username"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputDestinationSettings = OutputDestinationSettings


@dataclass
class MediaPackageOutputDestinationSettings(BaseModel):
    ChannelId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MediaPackageOutputDestinationSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MediaPackageOutputDestinationSettings"]:
        if not json_data:
            return None
        return cls(
            ChannelId=json_data.get("ChannelId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MediaPackageOutputDestinationSettings = MediaPackageOutputDestinationSettings


@dataclass
class VpcOutputSettings(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]
    PublicAddressAllocationIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcOutputSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcOutputSettings"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
            PublicAddressAllocationIds=json_data.get("PublicAddressAllocationIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcOutputSettings = VpcOutputSettings


@dataclass
class MaintenanceCreateSettings(BaseModel):
    MaintenanceDay: Optional[str]
    MaintenanceStartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceCreateSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceCreateSettings"]:
        if not json_data:
            return None
        return cls(
            MaintenanceDay=json_data.get("MaintenanceDay"),
            MaintenanceStartTime=json_data.get("MaintenanceStartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceCreateSettings = MaintenanceCreateSettings


@dataclass
class EncoderSettings(BaseModel):
    AudioDescriptions: Optional[Sequence["_AudioDescription"]]
    VideoDescriptions: Optional[Sequence["_VideoDescription"]]
    GlobalConfiguration: Optional["_GlobalConfiguration"]
    MotionGraphicsConfiguration: Optional["_MotionGraphicsConfiguration"]
    FeatureActivations: Optional["_FeatureActivations"]
    CaptionDescriptions: Optional[Sequence["_CaptionDescription"]]
    AvailConfiguration: Optional["_AvailConfiguration"]
    OutputGroups: Optional[Sequence["_OutputGroup"]]
    AvailBlanking: Optional["_AvailBlanking"]
    NielsenConfiguration: Optional["_NielsenConfiguration"]
    BlackoutSlate: Optional["_BlackoutSlate"]
    TimecodeConfig: Optional["_TimecodeConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_EncoderSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncoderSettings"]:
        if not json_data:
            return None
        return cls(
            AudioDescriptions=deserialize_list(json_data.get("AudioDescriptions"), AudioDescription),
            VideoDescriptions=deserialize_list(json_data.get("VideoDescriptions"), VideoDescription),
            GlobalConfiguration=GlobalConfiguration._deserialize(json_data.get("GlobalConfiguration")),
            MotionGraphicsConfiguration=MotionGraphicsConfiguration._deserialize(json_data.get("MotionGraphicsConfiguration")),
            FeatureActivations=FeatureActivations._deserialize(json_data.get("FeatureActivations")),
            CaptionDescriptions=deserialize_list(json_data.get("CaptionDescriptions"), CaptionDescription),
            AvailConfiguration=AvailConfiguration._deserialize(json_data.get("AvailConfiguration")),
            OutputGroups=deserialize_list(json_data.get("OutputGroups"), OutputGroup),
            AvailBlanking=AvailBlanking._deserialize(json_data.get("AvailBlanking")),
            NielsenConfiguration=NielsenConfiguration._deserialize(json_data.get("NielsenConfiguration")),
            BlackoutSlate=BlackoutSlate._deserialize(json_data.get("BlackoutSlate")),
            TimecodeConfig=TimecodeConfig._deserialize(json_data.get("TimecodeConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncoderSettings = EncoderSettings


@dataclass
class AudioDescription(BaseModel):
    AudioNormalizationSettings: Optional["_AudioNormalizationSettings"]
    LanguageCode: Optional[str]
    RemixSettings: Optional["_RemixSettings"]
    AudioSelectorName: Optional[str]
    StreamName: Optional[str]
    LanguageCodeControl: Optional[str]
    AudioType: Optional[str]
    AudioTypeControl: Optional[str]
    CodecSettings: Optional["_AudioCodecSettings"]
    Name: Optional[str]
    AudioWatermarkingSettings: Optional["_AudioWatermarkSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_AudioDescription"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioDescription"]:
        if not json_data:
            return None
        return cls(
            AudioNormalizationSettings=AudioNormalizationSettings._deserialize(json_data.get("AudioNormalizationSettings")),
            LanguageCode=json_data.get("LanguageCode"),
            RemixSettings=RemixSettings._deserialize(json_data.get("RemixSettings")),
            AudioSelectorName=json_data.get("AudioSelectorName"),
            StreamName=json_data.get("StreamName"),
            LanguageCodeControl=json_data.get("LanguageCodeControl"),
            AudioType=json_data.get("AudioType"),
            AudioTypeControl=json_data.get("AudioTypeControl"),
            CodecSettings=AudioCodecSettings._deserialize(json_data.get("CodecSettings")),
            Name=json_data.get("Name"),
            AudioWatermarkingSettings=AudioWatermarkSettings._deserialize(json_data.get("AudioWatermarkingSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioDescription = AudioDescription


@dataclass
class AudioNormalizationSettings(BaseModel):
    TargetLkfs: Optional[float]
    Algorithm: Optional[str]
    AlgorithmControl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AudioNormalizationSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioNormalizationSettings"]:
        if not json_data:
            return None
        return cls(
            TargetLkfs=json_data.get("TargetLkfs"),
            Algorithm=json_data.get("Algorithm"),
            AlgorithmControl=json_data.get("AlgorithmControl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioNormalizationSettings = AudioNormalizationSettings


@dataclass
class RemixSettings(BaseModel):
    ChannelsOut: Optional[int]
    ChannelsIn: Optional[int]
    ChannelMappings: Optional[Sequence["_AudioChannelMapping"]]

    @classmethod
    def _deserialize(
        cls: Type["_RemixSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RemixSettings"]:
        if not json_data:
            return None
        return cls(
            ChannelsOut=json_data.get("ChannelsOut"),
            ChannelsIn=json_data.get("ChannelsIn"),
            ChannelMappings=deserialize_list(json_data.get("ChannelMappings"), AudioChannelMapping),
        )


# work around possible type aliasing issues when variable has same name as a model
_RemixSettings = RemixSettings


@dataclass
class AudioChannelMapping(BaseModel):
    InputChannelLevels: Optional[Sequence["_InputChannelLevel"]]
    OutputChannel: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AudioChannelMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioChannelMapping"]:
        if not json_data:
            return None
        return cls(
            InputChannelLevels=deserialize_list(json_data.get("InputChannelLevels"), InputChannelLevel),
            OutputChannel=json_data.get("OutputChannel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioChannelMapping = AudioChannelMapping


@dataclass
class InputChannelLevel(BaseModel):
    InputChannel: Optional[int]
    Gain: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_InputChannelLevel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputChannelLevel"]:
        if not json_data:
            return None
        return cls(
            InputChannel=json_data.get("InputChannel"),
            Gain=json_data.get("Gain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputChannelLevel = InputChannelLevel


@dataclass
class AudioCodecSettings(BaseModel):
    Eac3Settings: Optional["_Eac3Settings"]
    Ac3Settings: Optional["_Ac3Settings"]
    Mp2Settings: Optional["_Mp2Settings"]
    Eac3AtmosSettings: Optional["_Eac3AtmosSettings"]
    PassThroughSettings: Optional[MutableMapping[str, Any]]
    WavSettings: Optional["_WavSettings"]
    AacSettings: Optional["_AacSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_AudioCodecSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioCodecSettings"]:
        if not json_data:
            return None
        return cls(
            Eac3Settings=Eac3Settings._deserialize(json_data.get("Eac3Settings")),
            Ac3Settings=Ac3Settings._deserialize(json_data.get("Ac3Settings")),
            Mp2Settings=Mp2Settings._deserialize(json_data.get("Mp2Settings")),
            Eac3AtmosSettings=Eac3AtmosSettings._deserialize(json_data.get("Eac3AtmosSettings")),
            PassThroughSettings=json_data.get("PassThroughSettings"),
            WavSettings=WavSettings._deserialize(json_data.get("WavSettings")),
            AacSettings=AacSettings._deserialize(json_data.get("AacSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioCodecSettings = AudioCodecSettings


@dataclass
class Eac3Settings(BaseModel):
    CodingMode: Optional[str]
    SurroundMode: Optional[str]
    PassthroughControl: Optional[str]
    Dialnorm: Optional[int]
    LoRoSurroundMixLevel: Optional[float]
    PhaseControl: Optional[str]
    LtRtCenterMixLevel: Optional[float]
    LfeFilter: Optional[str]
    LfeControl: Optional[str]
    Bitrate: Optional[float]
    DrcLine: Optional[str]
    DcFilter: Optional[str]
    MetadataControl: Optional[str]
    LtRtSurroundMixLevel: Optional[float]
    LoRoCenterMixLevel: Optional[float]
    DrcRf: Optional[str]
    AttenuationControl: Optional[str]
    BitstreamMode: Optional[str]
    SurroundExMode: Optional[str]
    StereoDownmix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Eac3Settings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Eac3Settings"]:
        if not json_data:
            return None
        return cls(
            CodingMode=json_data.get("CodingMode"),
            SurroundMode=json_data.get("SurroundMode"),
            PassthroughControl=json_data.get("PassthroughControl"),
            Dialnorm=json_data.get("Dialnorm"),
            LoRoSurroundMixLevel=json_data.get("LoRoSurroundMixLevel"),
            PhaseControl=json_data.get("PhaseControl"),
            LtRtCenterMixLevel=json_data.get("LtRtCenterMixLevel"),
            LfeFilter=json_data.get("LfeFilter"),
            LfeControl=json_data.get("LfeControl"),
            Bitrate=json_data.get("Bitrate"),
            DrcLine=json_data.get("DrcLine"),
            DcFilter=json_data.get("DcFilter"),
            MetadataControl=json_data.get("MetadataControl"),
            LtRtSurroundMixLevel=json_data.get("LtRtSurroundMixLevel"),
            LoRoCenterMixLevel=json_data.get("LoRoCenterMixLevel"),
            DrcRf=json_data.get("DrcRf"),
            AttenuationControl=json_data.get("AttenuationControl"),
            BitstreamMode=json_data.get("BitstreamMode"),
            SurroundExMode=json_data.get("SurroundExMode"),
            StereoDownmix=json_data.get("StereoDownmix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Eac3Settings = Eac3Settings


@dataclass
class Ac3Settings(BaseModel):
    CodingMode: Optional[str]
    DrcProfile: Optional[str]
    MetadataControl: Optional[str]
    Dialnorm: Optional[int]
    LfeFilter: Optional[str]
    BitstreamMode: Optional[str]
    Bitrate: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Ac3Settings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ac3Settings"]:
        if not json_data:
            return None
        return cls(
            CodingMode=json_data.get("CodingMode"),
            DrcProfile=json_data.get("DrcProfile"),
            MetadataControl=json_data.get("MetadataControl"),
            Dialnorm=json_data.get("Dialnorm"),
            LfeFilter=json_data.get("LfeFilter"),
            BitstreamMode=json_data.get("BitstreamMode"),
            Bitrate=json_data.get("Bitrate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ac3Settings = Ac3Settings


@dataclass
class Mp2Settings(BaseModel):
    CodingMode: Optional[str]
    SampleRate: Optional[float]
    Bitrate: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Mp2Settings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Mp2Settings"]:
        if not json_data:
            return None
        return cls(
            CodingMode=json_data.get("CodingMode"),
            SampleRate=json_data.get("SampleRate"),
            Bitrate=json_data.get("Bitrate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Mp2Settings = Mp2Settings


@dataclass
class Eac3AtmosSettings(BaseModel):
    CodingMode: Optional[str]
    Dialnorm: Optional[int]
    SurroundTrim: Optional[float]
    DrcRf: Optional[str]
    Bitrate: Optional[float]
    DrcLine: Optional[str]
    HeightTrim: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Eac3AtmosSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Eac3AtmosSettings"]:
        if not json_data:
            return None
        return cls(
            CodingMode=json_data.get("CodingMode"),
            Dialnorm=json_data.get("Dialnorm"),
            SurroundTrim=json_data.get("SurroundTrim"),
            DrcRf=json_data.get("DrcRf"),
            Bitrate=json_data.get("Bitrate"),
            DrcLine=json_data.get("DrcLine"),
            HeightTrim=json_data.get("HeightTrim"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Eac3AtmosSettings = Eac3AtmosSettings


@dataclass
class WavSettings(BaseModel):
    CodingMode: Optional[str]
    SampleRate: Optional[float]
    BitDepth: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_WavSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WavSettings"]:
        if not json_data:
            return None
        return cls(
            CodingMode=json_data.get("CodingMode"),
            SampleRate=json_data.get("SampleRate"),
            BitDepth=json_data.get("BitDepth"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WavSettings = WavSettings


@dataclass
class AacSettings(BaseModel):
    CodingMode: Optional[str]
    RateControlMode: Optional[str]
    SampleRate: Optional[float]
    InputType: Optional[str]
    VbrQuality: Optional[str]
    RawFormat: Optional[str]
    Spec: Optional[str]
    Bitrate: Optional[float]
    Profile: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AacSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AacSettings"]:
        if not json_data:
            return None
        return cls(
            CodingMode=json_data.get("CodingMode"),
            RateControlMode=json_data.get("RateControlMode"),
            SampleRate=json_data.get("SampleRate"),
            InputType=json_data.get("InputType"),
            VbrQuality=json_data.get("VbrQuality"),
            RawFormat=json_data.get("RawFormat"),
            Spec=json_data.get("Spec"),
            Bitrate=json_data.get("Bitrate"),
            Profile=json_data.get("Profile"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AacSettings = AacSettings


@dataclass
class AudioWatermarkSettings(BaseModel):
    NielsenWatermarksSettings: Optional["_NielsenWatermarksSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_AudioWatermarkSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioWatermarkSettings"]:
        if not json_data:
            return None
        return cls(
            NielsenWatermarksSettings=NielsenWatermarksSettings._deserialize(json_data.get("NielsenWatermarksSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioWatermarkSettings = AudioWatermarkSettings


@dataclass
class NielsenWatermarksSettings(BaseModel):
    NielsenNaesIiNwSettings: Optional["_NielsenNaesIiNw"]
    NielsenDistributionType: Optional[str]
    NielsenCbetSettings: Optional["_NielsenCBET"]

    @classmethod
    def _deserialize(
        cls: Type["_NielsenWatermarksSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NielsenWatermarksSettings"]:
        if not json_data:
            return None
        return cls(
            NielsenNaesIiNwSettings=NielsenNaesIiNw._deserialize(json_data.get("NielsenNaesIiNwSettings")),
            NielsenDistributionType=json_data.get("NielsenDistributionType"),
            NielsenCbetSettings=NielsenCBET._deserialize(json_data.get("NielsenCbetSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NielsenWatermarksSettings = NielsenWatermarksSettings


@dataclass
class NielsenNaesIiNw(BaseModel):
    Timezone: Optional[str]
    CheckDigitString: Optional[str]
    Sid: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NielsenNaesIiNw"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NielsenNaesIiNw"]:
        if not json_data:
            return None
        return cls(
            Timezone=json_data.get("Timezone"),
            CheckDigitString=json_data.get("CheckDigitString"),
            Sid=json_data.get("Sid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NielsenNaesIiNw = NielsenNaesIiNw


@dataclass
class NielsenCBET(BaseModel):
    CbetStepaside: Optional[str]
    CbetCheckDigitString: Optional[str]
    Csid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NielsenCBET"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NielsenCBET"]:
        if not json_data:
            return None
        return cls(
            CbetStepaside=json_data.get("CbetStepaside"),
            CbetCheckDigitString=json_data.get("CbetCheckDigitString"),
            Csid=json_data.get("Csid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NielsenCBET = NielsenCBET


@dataclass
class VideoDescription(BaseModel):
    ScalingBehavior: Optional[str]
    RespondToAfd: Optional[str]
    Height: Optional[int]
    Sharpness: Optional[int]
    Width: Optional[int]
    CodecSettings: Optional["_VideoCodecSettings"]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VideoDescription"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VideoDescription"]:
        if not json_data:
            return None
        return cls(
            ScalingBehavior=json_data.get("ScalingBehavior"),
            RespondToAfd=json_data.get("RespondToAfd"),
            Height=json_data.get("Height"),
            Sharpness=json_data.get("Sharpness"),
            Width=json_data.get("Width"),
            CodecSettings=VideoCodecSettings._deserialize(json_data.get("CodecSettings")),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VideoDescription = VideoDescription


@dataclass
class VideoCodecSettings(BaseModel):
    FrameCaptureSettings: Optional["_FrameCaptureSettings"]
    H264Settings: Optional["_H264Settings"]
    Mpeg2Settings: Optional["_Mpeg2Settings"]
    H265Settings: Optional["_H265Settings"]

    @classmethod
    def _deserialize(
        cls: Type["_VideoCodecSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VideoCodecSettings"]:
        if not json_data:
            return None
        return cls(
            FrameCaptureSettings=FrameCaptureSettings._deserialize(json_data.get("FrameCaptureSettings")),
            H264Settings=H264Settings._deserialize(json_data.get("H264Settings")),
            Mpeg2Settings=Mpeg2Settings._deserialize(json_data.get("Mpeg2Settings")),
            H265Settings=H265Settings._deserialize(json_data.get("H265Settings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VideoCodecSettings = VideoCodecSettings


@dataclass
class FrameCaptureSettings(BaseModel):
    TimecodeBurninSettings: Optional["_TimecodeBurninSettings"]
    CaptureIntervalUnits: Optional[str]
    CaptureInterval: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_FrameCaptureSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FrameCaptureSettings"]:
        if not json_data:
            return None
        return cls(
            TimecodeBurninSettings=TimecodeBurninSettings._deserialize(json_data.get("TimecodeBurninSettings")),
            CaptureIntervalUnits=json_data.get("CaptureIntervalUnits"),
            CaptureInterval=json_data.get("CaptureInterval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FrameCaptureSettings = FrameCaptureSettings


@dataclass
class TimecodeBurninSettings(BaseModel):
    Prefix: Optional[str]
    FontSize: Optional[str]
    Position: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimecodeBurninSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimecodeBurninSettings"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
            FontSize=json_data.get("FontSize"),
            Position=json_data.get("Position"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimecodeBurninSettings = TimecodeBurninSettings


@dataclass
class H264Settings(BaseModel):
    TimecodeBurninSettings: Optional["_TimecodeBurninSettings"]
    NumRefFrames: Optional[int]
    TemporalAq: Optional[str]
    Slices: Optional[int]
    FramerateControl: Optional[str]
    QvbrQualityLevel: Optional[int]
    FramerateNumerator: Optional[int]
    ParControl: Optional[str]
    GopClosedCadence: Optional[int]
    FlickerAq: Optional[str]
    Profile: Optional[str]
    QualityLevel: Optional[str]
    MinIInterval: Optional[int]
    SceneChangeDetect: Optional[str]
    ForceFieldPictures: Optional[str]
    FramerateDenominator: Optional[int]
    Softness: Optional[int]
    GopSize: Optional[float]
    AdaptiveQuantization: Optional[str]
    FilterSettings: Optional["_H264FilterSettings"]
    ColorSpaceSettings: Optional["_H264ColorSpaceSettings"]
    EntropyEncoding: Optional[str]
    SpatialAq: Optional[str]
    ParDenominator: Optional[int]
    FixedAfd: Optional[str]
    GopSizeUnits: Optional[str]
    AfdSignaling: Optional[str]
    Bitrate: Optional[int]
    ParNumerator: Optional[int]
    RateControlMode: Optional[str]
    ScanType: Optional[str]
    BufSize: Optional[int]
    TimecodeInsertion: Optional[str]
    ColorMetadata: Optional[str]
    BufFillPct: Optional[int]
    GopBReference: Optional[str]
    LookAheadRateControl: Optional[str]
    Level: Optional[str]
    MaxBitrate: Optional[int]
    Syntax: Optional[str]
    SubgopLength: Optional[str]
    GopNumBFrames: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_H264Settings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_H264Settings"]:
        if not json_data:
            return None
        return cls(
            TimecodeBurninSettings=TimecodeBurninSettings._deserialize(json_data.get("TimecodeBurninSettings")),
            NumRefFrames=json_data.get("NumRefFrames"),
            TemporalAq=json_data.get("TemporalAq"),
            Slices=json_data.get("Slices"),
            FramerateControl=json_data.get("FramerateControl"),
            QvbrQualityLevel=json_data.get("QvbrQualityLevel"),
            FramerateNumerator=json_data.get("FramerateNumerator"),
            ParControl=json_data.get("ParControl"),
            GopClosedCadence=json_data.get("GopClosedCadence"),
            FlickerAq=json_data.get("FlickerAq"),
            Profile=json_data.get("Profile"),
            QualityLevel=json_data.get("QualityLevel"),
            MinIInterval=json_data.get("MinIInterval"),
            SceneChangeDetect=json_data.get("SceneChangeDetect"),
            ForceFieldPictures=json_data.get("ForceFieldPictures"),
            FramerateDenominator=json_data.get("FramerateDenominator"),
            Softness=json_data.get("Softness"),
            GopSize=json_data.get("GopSize"),
            AdaptiveQuantization=json_data.get("AdaptiveQuantization"),
            FilterSettings=H264FilterSettings._deserialize(json_data.get("FilterSettings")),
            ColorSpaceSettings=H264ColorSpaceSettings._deserialize(json_data.get("ColorSpaceSettings")),
            EntropyEncoding=json_data.get("EntropyEncoding"),
            SpatialAq=json_data.get("SpatialAq"),
            ParDenominator=json_data.get("ParDenominator"),
            FixedAfd=json_data.get("FixedAfd"),
            GopSizeUnits=json_data.get("GopSizeUnits"),
            AfdSignaling=json_data.get("AfdSignaling"),
            Bitrate=json_data.get("Bitrate"),
            ParNumerator=json_data.get("ParNumerator"),
            RateControlMode=json_data.get("RateControlMode"),
            ScanType=json_data.get("ScanType"),
            BufSize=json_data.get("BufSize"),
            TimecodeInsertion=json_data.get("TimecodeInsertion"),
            ColorMetadata=json_data.get("ColorMetadata"),
            BufFillPct=json_data.get("BufFillPct"),
            GopBReference=json_data.get("GopBReference"),
            LookAheadRateControl=json_data.get("LookAheadRateControl"),
            Level=json_data.get("Level"),
            MaxBitrate=json_data.get("MaxBitrate"),
            Syntax=json_data.get("Syntax"),
            SubgopLength=json_data.get("SubgopLength"),
            GopNumBFrames=json_data.get("GopNumBFrames"),
        )


# work around possible type aliasing issues when variable has same name as a model
_H264Settings = H264Settings


@dataclass
class H264FilterSettings(BaseModel):
    TemporalFilterSettings: Optional["_TemporalFilterSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_H264FilterSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_H264FilterSettings"]:
        if not json_data:
            return None
        return cls(
            TemporalFilterSettings=TemporalFilterSettings._deserialize(json_data.get("TemporalFilterSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_H264FilterSettings = H264FilterSettings


@dataclass
class TemporalFilterSettings(BaseModel):
    PostFilterSharpening: Optional[str]
    Strength: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TemporalFilterSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemporalFilterSettings"]:
        if not json_data:
            return None
        return cls(
            PostFilterSharpening=json_data.get("PostFilterSharpening"),
            Strength=json_data.get("Strength"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemporalFilterSettings = TemporalFilterSettings


@dataclass
class H264ColorSpaceSettings(BaseModel):
    Rec601Settings: Optional[MutableMapping[str, Any]]
    Rec709Settings: Optional[MutableMapping[str, Any]]
    ColorSpacePassthroughSettings: Optional[MutableMapping[str, Any]]

    @classmethod
    def _deserialize(
        cls: Type["_H264ColorSpaceSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_H264ColorSpaceSettings"]:
        if not json_data:
            return None
        return cls(
            Rec601Settings=json_data.get("Rec601Settings"),
            Rec709Settings=json_data.get("Rec709Settings"),
            ColorSpacePassthroughSettings=json_data.get("ColorSpacePassthroughSettings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_H264ColorSpaceSettings = H264ColorSpaceSettings


@dataclass
class Mpeg2Settings(BaseModel):
    TimecodeBurninSettings: Optional["_TimecodeBurninSettings"]
    ColorSpace: Optional[str]
    FixedAfd: Optional[str]
    GopSizeUnits: Optional[str]
    FramerateNumerator: Optional[int]
    GopClosedCadence: Optional[int]
    AfdSignaling: Optional[str]
    DisplayAspectRatio: Optional[str]
    ScanType: Optional[str]
    TimecodeInsertion: Optional[str]
    ColorMetadata: Optional[str]
    FramerateDenominator: Optional[int]
    GopSize: Optional[float]
    AdaptiveQuantization: Optional[str]
    SubgopLength: Optional[str]
    FilterSettings: Optional["_Mpeg2FilterSettings"]
    GopNumBFrames: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Mpeg2Settings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Mpeg2Settings"]:
        if not json_data:
            return None
        return cls(
            TimecodeBurninSettings=TimecodeBurninSettings._deserialize(json_data.get("TimecodeBurninSettings")),
            ColorSpace=json_data.get("ColorSpace"),
            FixedAfd=json_data.get("FixedAfd"),
            GopSizeUnits=json_data.get("GopSizeUnits"),
            FramerateNumerator=json_data.get("FramerateNumerator"),
            GopClosedCadence=json_data.get("GopClosedCadence"),
            AfdSignaling=json_data.get("AfdSignaling"),
            DisplayAspectRatio=json_data.get("DisplayAspectRatio"),
            ScanType=json_data.get("ScanType"),
            TimecodeInsertion=json_data.get("TimecodeInsertion"),
            ColorMetadata=json_data.get("ColorMetadata"),
            FramerateDenominator=json_data.get("FramerateDenominator"),
            GopSize=json_data.get("GopSize"),
            AdaptiveQuantization=json_data.get("AdaptiveQuantization"),
            SubgopLength=json_data.get("SubgopLength"),
            FilterSettings=Mpeg2FilterSettings._deserialize(json_data.get("FilterSettings")),
            GopNumBFrames=json_data.get("GopNumBFrames"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Mpeg2Settings = Mpeg2Settings


@dataclass
class Mpeg2FilterSettings(BaseModel):
    TemporalFilterSettings: Optional["_TemporalFilterSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_Mpeg2FilterSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Mpeg2FilterSettings"]:
        if not json_data:
            return None
        return cls(
            TemporalFilterSettings=TemporalFilterSettings._deserialize(json_data.get("TemporalFilterSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Mpeg2FilterSettings = Mpeg2FilterSettings


@dataclass
class H265Settings(BaseModel):
    TimecodeBurninSettings: Optional["_TimecodeBurninSettings"]
    Slices: Optional[int]
    QvbrQualityLevel: Optional[int]
    FramerateNumerator: Optional[int]
    GopClosedCadence: Optional[int]
    FlickerAq: Optional[str]
    Profile: Optional[str]
    MinIInterval: Optional[int]
    SceneChangeDetect: Optional[str]
    FramerateDenominator: Optional[int]
    GopSize: Optional[float]
    AdaptiveQuantization: Optional[str]
    FilterSettings: Optional["_H265FilterSettings"]
    AlternativeTransferFunction: Optional[str]
    ColorSpaceSettings: Optional["_H265ColorSpaceSettings"]
    Tier: Optional[str]
    ParDenominator: Optional[int]
    FixedAfd: Optional[str]
    GopSizeUnits: Optional[str]
    AfdSignaling: Optional[str]
    Bitrate: Optional[int]
    ParNumerator: Optional[int]
    RateControlMode: Optional[str]
    ScanType: Optional[str]
    BufSize: Optional[int]
    TimecodeInsertion: Optional[str]
    ColorMetadata: Optional[str]
    LookAheadRateControl: Optional[str]
    Level: Optional[str]
    MaxBitrate: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_H265Settings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_H265Settings"]:
        if not json_data:
            return None
        return cls(
            TimecodeBurninSettings=TimecodeBurninSettings._deserialize(json_data.get("TimecodeBurninSettings")),
            Slices=json_data.get("Slices"),
            QvbrQualityLevel=json_data.get("QvbrQualityLevel"),
            FramerateNumerator=json_data.get("FramerateNumerator"),
            GopClosedCadence=json_data.get("GopClosedCadence"),
            FlickerAq=json_data.get("FlickerAq"),
            Profile=json_data.get("Profile"),
            MinIInterval=json_data.get("MinIInterval"),
            SceneChangeDetect=json_data.get("SceneChangeDetect"),
            FramerateDenominator=json_data.get("FramerateDenominator"),
            GopSize=json_data.get("GopSize"),
            AdaptiveQuantization=json_data.get("AdaptiveQuantization"),
            FilterSettings=H265FilterSettings._deserialize(json_data.get("FilterSettings")),
            AlternativeTransferFunction=json_data.get("AlternativeTransferFunction"),
            ColorSpaceSettings=H265ColorSpaceSettings._deserialize(json_data.get("ColorSpaceSettings")),
            Tier=json_data.get("Tier"),
            ParDenominator=json_data.get("ParDenominator"),
            FixedAfd=json_data.get("FixedAfd"),
            GopSizeUnits=json_data.get("GopSizeUnits"),
            AfdSignaling=json_data.get("AfdSignaling"),
            Bitrate=json_data.get("Bitrate"),
            ParNumerator=json_data.get("ParNumerator"),
            RateControlMode=json_data.get("RateControlMode"),
            ScanType=json_data.get("ScanType"),
            BufSize=json_data.get("BufSize"),
            TimecodeInsertion=json_data.get("TimecodeInsertion"),
            ColorMetadata=json_data.get("ColorMetadata"),
            LookAheadRateControl=json_data.get("LookAheadRateControl"),
            Level=json_data.get("Level"),
            MaxBitrate=json_data.get("MaxBitrate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_H265Settings = H265Settings


@dataclass
class H265FilterSettings(BaseModel):
    TemporalFilterSettings: Optional["_TemporalFilterSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_H265FilterSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_H265FilterSettings"]:
        if not json_data:
            return None
        return cls(
            TemporalFilterSettings=TemporalFilterSettings._deserialize(json_data.get("TemporalFilterSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_H265FilterSettings = H265FilterSettings


@dataclass
class H265ColorSpaceSettings(BaseModel):
    Rec601Settings: Optional[MutableMapping[str, Any]]
    Rec709Settings: Optional[MutableMapping[str, Any]]
    ColorSpacePassthroughSettings: Optional[MutableMapping[str, Any]]
    DolbyVision81Settings: Optional[MutableMapping[str, Any]]
    Hdr10Settings: Optional["_Hdr10Settings"]

    @classmethod
    def _deserialize(
        cls: Type["_H265ColorSpaceSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_H265ColorSpaceSettings"]:
        if not json_data:
            return None
        return cls(
            Rec601Settings=json_data.get("Rec601Settings"),
            Rec709Settings=json_data.get("Rec709Settings"),
            ColorSpacePassthroughSettings=json_data.get("ColorSpacePassthroughSettings"),
            DolbyVision81Settings=json_data.get("DolbyVision81Settings"),
            Hdr10Settings=Hdr10Settings._deserialize(json_data.get("Hdr10Settings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_H265ColorSpaceSettings = H265ColorSpaceSettings


@dataclass
class GlobalConfiguration(BaseModel):
    InputEndAction: Optional[str]
    OutputTimingSource: Optional[str]
    OutputLockingMode: Optional[str]
    SupportLowFramerateInputs: Optional[str]
    InitialAudioGain: Optional[int]
    InputLossBehavior: Optional["_InputLossBehavior"]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalConfiguration"]:
        if not json_data:
            return None
        return cls(
            InputEndAction=json_data.get("InputEndAction"),
            OutputTimingSource=json_data.get("OutputTimingSource"),
            OutputLockingMode=json_data.get("OutputLockingMode"),
            SupportLowFramerateInputs=json_data.get("SupportLowFramerateInputs"),
            InitialAudioGain=json_data.get("InitialAudioGain"),
            InputLossBehavior=InputLossBehavior._deserialize(json_data.get("InputLossBehavior")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalConfiguration = GlobalConfiguration


@dataclass
class InputLossBehavior(BaseModel):
    InputLossImageType: Optional[str]
    InputLossImageSlate: Optional["_InputLocation"]
    InputLossImageColor: Optional[str]
    RepeatFrameMsec: Optional[int]
    BlackFrameMsec: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_InputLossBehavior"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputLossBehavior"]:
        if not json_data:
            return None
        return cls(
            InputLossImageType=json_data.get("InputLossImageType"),
            InputLossImageSlate=InputLocation._deserialize(json_data.get("InputLossImageSlate")),
            InputLossImageColor=json_data.get("InputLossImageColor"),
            RepeatFrameMsec=json_data.get("RepeatFrameMsec"),
            BlackFrameMsec=json_data.get("BlackFrameMsec"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputLossBehavior = InputLossBehavior


@dataclass
class InputLocation(BaseModel):
    PasswordParam: Optional[str]
    Username: Optional[str]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputLocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputLocation"]:
        if not json_data:
            return None
        return cls(
            PasswordParam=json_data.get("PasswordParam"),
            Username=json_data.get("Username"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputLocation = InputLocation


@dataclass
class MotionGraphicsConfiguration(BaseModel):
    MotionGraphicsSettings: Optional["_MotionGraphicsSettings"]
    MotionGraphicsInsertion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MotionGraphicsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MotionGraphicsConfiguration"]:
        if not json_data:
            return None
        return cls(
            MotionGraphicsSettings=MotionGraphicsSettings._deserialize(json_data.get("MotionGraphicsSettings")),
            MotionGraphicsInsertion=json_data.get("MotionGraphicsInsertion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MotionGraphicsConfiguration = MotionGraphicsConfiguration


@dataclass
class MotionGraphicsSettings(BaseModel):
    HtmlMotionGraphicsSettings: Optional[MutableMapping[str, Any]]

    @classmethod
    def _deserialize(
        cls: Type["_MotionGraphicsSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MotionGraphicsSettings"]:
        if not json_data:
            return None
        return cls(
            HtmlMotionGraphicsSettings=json_data.get("HtmlMotionGraphicsSettings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MotionGraphicsSettings = MotionGraphicsSettings


@dataclass
class FeatureActivations(BaseModel):
    InputPrepareScheduleActions: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FeatureActivations"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FeatureActivations"]:
        if not json_data:
            return None
        return cls(
            InputPrepareScheduleActions=json_data.get("InputPrepareScheduleActions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FeatureActivations = FeatureActivations


@dataclass
class CaptionDescription(BaseModel):
    DestinationSettings: Optional["_CaptionDestinationSettings"]
    LanguageCode: Optional[str]
    LanguageDescription: Optional[str]
    Accessibility: Optional[str]
    CaptionSelectorName: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CaptionDescription"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaptionDescription"]:
        if not json_data:
            return None
        return cls(
            DestinationSettings=CaptionDestinationSettings._deserialize(json_data.get("DestinationSettings")),
            LanguageCode=json_data.get("LanguageCode"),
            LanguageDescription=json_data.get("LanguageDescription"),
            Accessibility=json_data.get("Accessibility"),
            CaptionSelectorName=json_data.get("CaptionSelectorName"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CaptionDescription = CaptionDescription


@dataclass
class CaptionDestinationSettings(BaseModel):
    AribDestinationSettings: Optional[MutableMapping[str, Any]]
    EbuTtDDestinationSettings: Optional["_EbuTtDDestinationSettings"]
    SmpteTtDestinationSettings: Optional[MutableMapping[str, Any]]
    EmbeddedPlusScte20DestinationSettings: Optional[MutableMapping[str, Any]]
    TtmlDestinationSettings: Optional["_TtmlDestinationSettings"]
    Scte20PlusEmbeddedDestinationSettings: Optional[MutableMapping[str, Any]]
    DvbSubDestinationSettings: Optional["_DvbSubDestinationSettings"]
    TeletextDestinationSettings: Optional[MutableMapping[str, Any]]
    BurnInDestinationSettings: Optional["_BurnInDestinationSettings"]
    WebvttDestinationSettings: Optional["_WebvttDestinationSettings"]
    EmbeddedDestinationSettings: Optional[MutableMapping[str, Any]]
    RtmpCaptionInfoDestinationSettings: Optional[MutableMapping[str, Any]]
    Scte27DestinationSettings: Optional[MutableMapping[str, Any]]

    @classmethod
    def _deserialize(
        cls: Type["_CaptionDestinationSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaptionDestinationSettings"]:
        if not json_data:
            return None
        return cls(
            AribDestinationSettings=json_data.get("AribDestinationSettings"),
            EbuTtDDestinationSettings=EbuTtDDestinationSettings._deserialize(json_data.get("EbuTtDDestinationSettings")),
            SmpteTtDestinationSettings=json_data.get("SmpteTtDestinationSettings"),
            EmbeddedPlusScte20DestinationSettings=json_data.get("EmbeddedPlusScte20DestinationSettings"),
            TtmlDestinationSettings=TtmlDestinationSettings._deserialize(json_data.get("TtmlDestinationSettings")),
            Scte20PlusEmbeddedDestinationSettings=json_data.get("Scte20PlusEmbeddedDestinationSettings"),
            DvbSubDestinationSettings=DvbSubDestinationSettings._deserialize(json_data.get("DvbSubDestinationSettings")),
            TeletextDestinationSettings=json_data.get("TeletextDestinationSettings"),
            BurnInDestinationSettings=BurnInDestinationSettings._deserialize(json_data.get("BurnInDestinationSettings")),
            WebvttDestinationSettings=WebvttDestinationSettings._deserialize(json_data.get("WebvttDestinationSettings")),
            EmbeddedDestinationSettings=json_data.get("EmbeddedDestinationSettings"),
            RtmpCaptionInfoDestinationSettings=json_data.get("RtmpCaptionInfoDestinationSettings"),
            Scte27DestinationSettings=json_data.get("Scte27DestinationSettings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CaptionDestinationSettings = CaptionDestinationSettings


@dataclass
class EbuTtDDestinationSettings(BaseModel):
    FontFamily: Optional[str]
    StyleControl: Optional[str]
    CopyrightHolder: Optional[str]
    FillLineGap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EbuTtDDestinationSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbuTtDDestinationSettings"]:
        if not json_data:
            return None
        return cls(
            FontFamily=json_data.get("FontFamily"),
            StyleControl=json_data.get("StyleControl"),
            CopyrightHolder=json_data.get("CopyrightHolder"),
            FillLineGap=json_data.get("FillLineGap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbuTtDDestinationSettings = EbuTtDDestinationSettings


@dataclass
class TtmlDestinationSettings(BaseModel):
    StyleControl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TtmlDestinationSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TtmlDestinationSettings"]:
        if not json_data:
            return None
        return cls(
            StyleControl=json_data.get("StyleControl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TtmlDestinationSettings = TtmlDestinationSettings


@dataclass
class DvbSubDestinationSettings(BaseModel):
    BackgroundOpacity: Optional[int]
    FontResolution: Optional[int]
    OutlineColor: Optional[str]
    FontColor: Optional[str]
    ShadowColor: Optional[str]
    ShadowOpacity: Optional[int]
    Font: Optional["_InputLocation"]
    ShadowYOffset: Optional[int]
    Alignment: Optional[str]
    XPosition: Optional[int]
    FontSize: Optional[str]
    YPosition: Optional[int]
    OutlineSize: Optional[int]
    TeletextGridControl: Optional[str]
    FontOpacity: Optional[int]
    ShadowXOffset: Optional[int]
    BackgroundColor: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DvbSubDestinationSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DvbSubDestinationSettings"]:
        if not json_data:
            return None
        return cls(
            BackgroundOpacity=json_data.get("BackgroundOpacity"),
            FontResolution=json_data.get("FontResolution"),
            OutlineColor=json_data.get("OutlineColor"),
            FontColor=json_data.get("FontColor"),
            ShadowColor=json_data.get("ShadowColor"),
            ShadowOpacity=json_data.get("ShadowOpacity"),
            Font=InputLocation._deserialize(json_data.get("Font")),
            ShadowYOffset=json_data.get("ShadowYOffset"),
            Alignment=json_data.get("Alignment"),
            XPosition=json_data.get("XPosition"),
            FontSize=json_data.get("FontSize"),
            YPosition=json_data.get("YPosition"),
            OutlineSize=json_data.get("OutlineSize"),
            TeletextGridControl=json_data.get("TeletextGridControl"),
            FontOpacity=json_data.get("FontOpacity"),
            ShadowXOffset=json_data.get("ShadowXOffset"),
            BackgroundColor=json_data.get("BackgroundColor"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DvbSubDestinationSettings = DvbSubDestinationSettings


@dataclass
class BurnInDestinationSettings(BaseModel):
    BackgroundOpacity: Optional[int]
    FontResolution: Optional[int]
    OutlineColor: Optional[str]
    FontColor: Optional[str]
    ShadowColor: Optional[str]
    ShadowOpacity: Optional[int]
    Font: Optional["_InputLocation"]
    ShadowYOffset: Optional[int]
    Alignment: Optional[str]
    XPosition: Optional[int]
    FontSize: Optional[str]
    YPosition: Optional[int]
    OutlineSize: Optional[int]
    TeletextGridControl: Optional[str]
    FontOpacity: Optional[int]
    ShadowXOffset: Optional[int]
    BackgroundColor: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BurnInDestinationSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BurnInDestinationSettings"]:
        if not json_data:
            return None
        return cls(
            BackgroundOpacity=json_data.get("BackgroundOpacity"),
            FontResolution=json_data.get("FontResolution"),
            OutlineColor=json_data.get("OutlineColor"),
            FontColor=json_data.get("FontColor"),
            ShadowColor=json_data.get("ShadowColor"),
            ShadowOpacity=json_data.get("ShadowOpacity"),
            Font=InputLocation._deserialize(json_data.get("Font")),
            ShadowYOffset=json_data.get("ShadowYOffset"),
            Alignment=json_data.get("Alignment"),
            XPosition=json_data.get("XPosition"),
            FontSize=json_data.get("FontSize"),
            YPosition=json_data.get("YPosition"),
            OutlineSize=json_data.get("OutlineSize"),
            TeletextGridControl=json_data.get("TeletextGridControl"),
            FontOpacity=json_data.get("FontOpacity"),
            ShadowXOffset=json_data.get("ShadowXOffset"),
            BackgroundColor=json_data.get("BackgroundColor"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BurnInDestinationSettings = BurnInDestinationSettings


@dataclass
class WebvttDestinationSettings(BaseModel):
    StyleControl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WebvttDestinationSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebvttDestinationSettings"]:
        if not json_data:
            return None
        return cls(
            StyleControl=json_data.get("StyleControl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebvttDestinationSettings = WebvttDestinationSettings


@dataclass
class AvailConfiguration(BaseModel):
    AvailSettings: Optional["_AvailSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_AvailConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AvailConfiguration"]:
        if not json_data:
            return None
        return cls(
            AvailSettings=AvailSettings._deserialize(json_data.get("AvailSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AvailConfiguration = AvailConfiguration


@dataclass
class AvailSettings(BaseModel):
    Scte35SpliceInsert: Optional["_Scte35SpliceInsert"]
    Scte35TimeSignalApos: Optional["_Scte35TimeSignalApos"]
    Esam: Optional["_Esam"]

    @classmethod
    def _deserialize(
        cls: Type["_AvailSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AvailSettings"]:
        if not json_data:
            return None
        return cls(
            Scte35SpliceInsert=Scte35SpliceInsert._deserialize(json_data.get("Scte35SpliceInsert")),
            Scte35TimeSignalApos=Scte35TimeSignalApos._deserialize(json_data.get("Scte35TimeSignalApos")),
            Esam=Esam._deserialize(json_data.get("Esam")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AvailSettings = AvailSettings


@dataclass
class Scte35SpliceInsert(BaseModel):
    AdAvailOffset: Optional[int]
    WebDeliveryAllowedFlag: Optional[str]
    NoRegionalBlackoutFlag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Scte35SpliceInsert"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Scte35SpliceInsert"]:
        if not json_data:
            return None
        return cls(
            AdAvailOffset=json_data.get("AdAvailOffset"),
            WebDeliveryAllowedFlag=json_data.get("WebDeliveryAllowedFlag"),
            NoRegionalBlackoutFlag=json_data.get("NoRegionalBlackoutFlag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Scte35SpliceInsert = Scte35SpliceInsert


@dataclass
class Scte35TimeSignalApos(BaseModel):
    AdAvailOffset: Optional[int]
    WebDeliveryAllowedFlag: Optional[str]
    NoRegionalBlackoutFlag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Scte35TimeSignalApos"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Scte35TimeSignalApos"]:
        if not json_data:
            return None
        return cls(
            AdAvailOffset=json_data.get("AdAvailOffset"),
            WebDeliveryAllowedFlag=json_data.get("WebDeliveryAllowedFlag"),
            NoRegionalBlackoutFlag=json_data.get("NoRegionalBlackoutFlag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Scte35TimeSignalApos = Scte35TimeSignalApos


@dataclass
class Esam(BaseModel):
    AdAvailOffset: Optional[int]
    ZoneIdentity: Optional[str]
    AcquisitionPointId: Optional[str]
    PoisEndpoint: Optional[str]
    Username: Optional[str]
    PasswordParam: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Esam"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Esam"]:
        if not json_data:
            return None
        return cls(
            AdAvailOffset=json_data.get("AdAvailOffset"),
            ZoneIdentity=json_data.get("ZoneIdentity"),
            AcquisitionPointId=json_data.get("AcquisitionPointId"),
            PoisEndpoint=json_data.get("PoisEndpoint"),
            Username=json_data.get("Username"),
            PasswordParam=json_data.get("PasswordParam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Esam = Esam


@dataclass
class OutputGroup(BaseModel):
    Outputs: Optional[Sequence["_Output"]]
    OutputGroupSettings: Optional["_OutputGroupSettings"]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutputGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputGroup"]:
        if not json_data:
            return None
        return cls(
            Outputs=deserialize_list(json_data.get("Outputs"), Output),
            OutputGroupSettings=OutputGroupSettings._deserialize(json_data.get("OutputGroupSettings")),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputGroup = OutputGroup


@dataclass
class Output(BaseModel):
    OutputSettings: Optional["_OutputSettings"]
    CaptionDescriptionNames: Optional[Sequence[str]]
    AudioDescriptionNames: Optional[Sequence[str]]
    OutputName: Optional[str]
    VideoDescriptionName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Output"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Output"]:
        if not json_data:
            return None
        return cls(
            OutputSettings=OutputSettings._deserialize(json_data.get("OutputSettings")),
            CaptionDescriptionNames=json_data.get("CaptionDescriptionNames"),
            AudioDescriptionNames=json_data.get("AudioDescriptionNames"),
            OutputName=json_data.get("OutputName"),
            VideoDescriptionName=json_data.get("VideoDescriptionName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Output = Output


@dataclass
class OutputSettings(BaseModel):
    MediaPackageOutputSettings: Optional[MutableMapping[str, Any]]
    MsSmoothOutputSettings: Optional["_MsSmoothOutputSettings"]
    FrameCaptureOutputSettings: Optional["_FrameCaptureOutputSettings"]
    HlsOutputSettings: Optional["_HlsOutputSettings"]
    RtmpOutputSettings: Optional["_RtmpOutputSettings"]
    UdpOutputSettings: Optional["_UdpOutputSettings"]
    MultiplexOutputSettings: Optional["_MultiplexOutputSettings"]
    ArchiveOutputSettings: Optional["_ArchiveOutputSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_OutputSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputSettings"]:
        if not json_data:
            return None
        return cls(
            MediaPackageOutputSettings=json_data.get("MediaPackageOutputSettings"),
            MsSmoothOutputSettings=MsSmoothOutputSettings._deserialize(json_data.get("MsSmoothOutputSettings")),
            FrameCaptureOutputSettings=FrameCaptureOutputSettings._deserialize(json_data.get("FrameCaptureOutputSettings")),
            HlsOutputSettings=HlsOutputSettings._deserialize(json_data.get("HlsOutputSettings")),
            RtmpOutputSettings=RtmpOutputSettings._deserialize(json_data.get("RtmpOutputSettings")),
            UdpOutputSettings=UdpOutputSettings._deserialize(json_data.get("UdpOutputSettings")),
            MultiplexOutputSettings=MultiplexOutputSettings._deserialize(json_data.get("MultiplexOutputSettings")),
            ArchiveOutputSettings=ArchiveOutputSettings._deserialize(json_data.get("ArchiveOutputSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputSettings = OutputSettings


@dataclass
class MsSmoothOutputSettings(BaseModel):
    NameModifier: Optional[str]
    H265PackagingType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MsSmoothOutputSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MsSmoothOutputSettings"]:
        if not json_data:
            return None
        return cls(
            NameModifier=json_data.get("NameModifier"),
            H265PackagingType=json_data.get("H265PackagingType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MsSmoothOutputSettings = MsSmoothOutputSettings


@dataclass
class FrameCaptureOutputSettings(BaseModel):
    NameModifier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FrameCaptureOutputSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FrameCaptureOutputSettings"]:
        if not json_data:
            return None
        return cls(
            NameModifier=json_data.get("NameModifier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FrameCaptureOutputSettings = FrameCaptureOutputSettings


@dataclass
class HlsOutputSettings(BaseModel):
    HlsSettings: Optional["_HlsSettings"]
    NameModifier: Optional[str]
    H265PackagingType: Optional[str]
    SegmentModifier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HlsOutputSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HlsOutputSettings"]:
        if not json_data:
            return None
        return cls(
            HlsSettings=HlsSettings._deserialize(json_data.get("HlsSettings")),
            NameModifier=json_data.get("NameModifier"),
            H265PackagingType=json_data.get("H265PackagingType"),
            SegmentModifier=json_data.get("SegmentModifier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HlsOutputSettings = HlsOutputSettings


@dataclass
class HlsSettings(BaseModel):
    Fmp4HlsSettings: Optional["_Fmp4HlsSettings"]
    FrameCaptureHlsSettings: Optional[MutableMapping[str, Any]]
    StandardHlsSettings: Optional["_StandardHlsSettings"]
    AudioOnlyHlsSettings: Optional["_AudioOnlyHlsSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_HlsSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HlsSettings"]:
        if not json_data:
            return None
        return cls(
            Fmp4HlsSettings=Fmp4HlsSettings._deserialize(json_data.get("Fmp4HlsSettings")),
            FrameCaptureHlsSettings=json_data.get("FrameCaptureHlsSettings"),
            StandardHlsSettings=StandardHlsSettings._deserialize(json_data.get("StandardHlsSettings")),
            AudioOnlyHlsSettings=AudioOnlyHlsSettings._deserialize(json_data.get("AudioOnlyHlsSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HlsSettings = HlsSettings


@dataclass
class Fmp4HlsSettings(BaseModel):
    AudioRenditionSets: Optional[str]
    NielsenId3Behavior: Optional[str]
    TimedMetadataBehavior: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Fmp4HlsSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Fmp4HlsSettings"]:
        if not json_data:
            return None
        return cls(
            AudioRenditionSets=json_data.get("AudioRenditionSets"),
            NielsenId3Behavior=json_data.get("NielsenId3Behavior"),
            TimedMetadataBehavior=json_data.get("TimedMetadataBehavior"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Fmp4HlsSettings = Fmp4HlsSettings


@dataclass
class StandardHlsSettings(BaseModel):
    AudioRenditionSets: Optional[str]
    M3u8Settings: Optional["_M3u8Settings"]

    @classmethod
    def _deserialize(
        cls: Type["_StandardHlsSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StandardHlsSettings"]:
        if not json_data:
            return None
        return cls(
            AudioRenditionSets=json_data.get("AudioRenditionSets"),
            M3u8Settings=M3u8Settings._deserialize(json_data.get("M3u8Settings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_StandardHlsSettings = StandardHlsSettings


@dataclass
class M3u8Settings(BaseModel):
    PatInterval: Optional[int]
    ProgramNum: Optional[int]
    PcrPeriod: Optional[int]
    PmtInterval: Optional[int]
    NielsenId3Behavior: Optional[str]
    PcrPid: Optional[str]
    VideoPid: Optional[str]
    AudioFramesPerPes: Optional[int]
    TransportStreamId: Optional[int]
    PmtPid: Optional[str]
    Scte35Pid: Optional[str]
    Scte35Behavior: Optional[str]
    EcmPid: Optional[str]
    TimedMetadataPid: Optional[str]
    AudioPids: Optional[str]
    PcrControl: Optional[str]
    TimedMetadataBehavior: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_M3u8Settings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_M3u8Settings"]:
        if not json_data:
            return None
        return cls(
            PatInterval=json_data.get("PatInterval"),
            ProgramNum=json_data.get("ProgramNum"),
            PcrPeriod=json_data.get("PcrPeriod"),
            PmtInterval=json_data.get("PmtInterval"),
            NielsenId3Behavior=json_data.get("NielsenId3Behavior"),
            PcrPid=json_data.get("PcrPid"),
            VideoPid=json_data.get("VideoPid"),
            AudioFramesPerPes=json_data.get("AudioFramesPerPes"),
            TransportStreamId=json_data.get("TransportStreamId"),
            PmtPid=json_data.get("PmtPid"),
            Scte35Pid=json_data.get("Scte35Pid"),
            Scte35Behavior=json_data.get("Scte35Behavior"),
            EcmPid=json_data.get("EcmPid"),
            TimedMetadataPid=json_data.get("TimedMetadataPid"),
            AudioPids=json_data.get("AudioPids"),
            PcrControl=json_data.get("PcrControl"),
            TimedMetadataBehavior=json_data.get("TimedMetadataBehavior"),
        )


# work around possible type aliasing issues when variable has same name as a model
_M3u8Settings = M3u8Settings


@dataclass
class AudioOnlyHlsSettings(BaseModel):
    SegmentType: Optional[str]
    AudioTrackType: Optional[str]
    AudioGroupId: Optional[str]
    AudioOnlyImage: Optional["_InputLocation"]

    @classmethod
    def _deserialize(
        cls: Type["_AudioOnlyHlsSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioOnlyHlsSettings"]:
        if not json_data:
            return None
        return cls(
            SegmentType=json_data.get("SegmentType"),
            AudioTrackType=json_data.get("AudioTrackType"),
            AudioGroupId=json_data.get("AudioGroupId"),
            AudioOnlyImage=InputLocation._deserialize(json_data.get("AudioOnlyImage")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioOnlyHlsSettings = AudioOnlyHlsSettings


@dataclass
class RtmpOutputSettings(BaseModel):
    Destination: Optional["_OutputLocationRef"]
    CertificateMode: Optional[str]
    NumRetries: Optional[int]
    ConnectionRetryInterval: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_RtmpOutputSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RtmpOutputSettings"]:
        if not json_data:
            return None
        return cls(
            Destination=OutputLocationRef._deserialize(json_data.get("Destination")),
            CertificateMode=json_data.get("CertificateMode"),
            NumRetries=json_data.get("NumRetries"),
            ConnectionRetryInterval=json_data.get("ConnectionRetryInterval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RtmpOutputSettings = RtmpOutputSettings


@dataclass
class OutputLocationRef(BaseModel):
    DestinationRefId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutputLocationRef"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputLocationRef"]:
        if not json_data:
            return None
        return cls(
            DestinationRefId=json_data.get("DestinationRefId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputLocationRef = OutputLocationRef


@dataclass
class UdpOutputSettings(BaseModel):
    Destination: Optional["_OutputLocationRef"]
    FecOutputSettings: Optional["_FecOutputSettings"]
    BufferMsec: Optional[int]
    ContainerSettings: Optional["_UdpContainerSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_UdpOutputSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UdpOutputSettings"]:
        if not json_data:
            return None
        return cls(
            Destination=OutputLocationRef._deserialize(json_data.get("Destination")),
            FecOutputSettings=FecOutputSettings._deserialize(json_data.get("FecOutputSettings")),
            BufferMsec=json_data.get("BufferMsec"),
            ContainerSettings=UdpContainerSettings._deserialize(json_data.get("ContainerSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_UdpOutputSettings = UdpOutputSettings


@dataclass
class FecOutputSettings(BaseModel):
    ColumnDepth: Optional[int]
    IncludeFec: Optional[str]
    RowLength: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_FecOutputSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FecOutputSettings"]:
        if not json_data:
            return None
        return cls(
            ColumnDepth=json_data.get("ColumnDepth"),
            IncludeFec=json_data.get("IncludeFec"),
            RowLength=json_data.get("RowLength"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FecOutputSettings = FecOutputSettings


@dataclass
class UdpContainerSettings(BaseModel):
    M2tsSettings: Optional["_M2tsSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_UdpContainerSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UdpContainerSettings"]:
        if not json_data:
            return None
        return cls(
            M2tsSettings=M2tsSettings._deserialize(json_data.get("M2tsSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_UdpContainerSettings = UdpContainerSettings


@dataclass
class M2tsSettings(BaseModel):
    EtvPlatformPid: Optional[str]
    AribCaptionsPid: Optional[str]
    EbpPlacement: Optional[str]
    DvbSubPids: Optional[str]
    SegmentationStyle: Optional[str]
    Klv: Optional[str]
    Scte35PrerollPullupMilliseconds: Optional[float]
    TimedMetadataBehavior: Optional[str]
    DvbTeletextPid: Optional[str]
    Scte35Control: Optional[str]
    PcrPeriod: Optional[int]
    SegmentationTime: Optional[float]
    CcDescriptor: Optional[str]
    PmtPid: Optional[str]
    DvbNitSettings: Optional["_DvbNitSettings"]
    EtvSignalPid: Optional[str]
    Arib: Optional[str]
    TimedMetadataPid: Optional[str]
    AudioPids: Optional[str]
    AudioBufferModel: Optional[str]
    Ebif: Optional[str]
    PcrControl: Optional[str]
    PatInterval: Optional[int]
    ProgramNum: Optional[int]
    RateMode: Optional[str]
    KlvDataPids: Optional[str]
    NullPacketBitrate: Optional[float]
    PmtInterval: Optional[int]
    EsRateInPes: Optional[str]
    VideoPid: Optional[str]
    TransportStreamId: Optional[int]
    Scte35Pid: Optional[str]
    AudioStreamType: Optional[str]
    EbpLookaheadMs: Optional[int]
    DvbTdtSettings: Optional["_DvbTdtSettings"]
    EbpAudioInterval: Optional[str]
    FragmentTime: Optional[float]
    NielsenId3Behavior: Optional[str]
    PcrPid: Optional[str]
    AudioFramesPerPes: Optional[int]
    AbsentInputAudioBehavior: Optional[str]
    Bitrate: Optional[int]
    Scte27Pids: Optional[str]
    SegmentationMarkers: Optional[str]
    DvbSdtSettings: Optional["_DvbSdtSettings"]
    BufferModel: Optional[str]
    EcmPid: Optional[str]
    AribCaptionsPidControl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_M2tsSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_M2tsSettings"]:
        if not json_data:
            return None
        return cls(
            EtvPlatformPid=json_data.get("EtvPlatformPid"),
            AribCaptionsPid=json_data.get("AribCaptionsPid"),
            EbpPlacement=json_data.get("EbpPlacement"),
            DvbSubPids=json_data.get("DvbSubPids"),
            SegmentationStyle=json_data.get("SegmentationStyle"),
            Klv=json_data.get("Klv"),
            Scte35PrerollPullupMilliseconds=json_data.get("Scte35PrerollPullupMilliseconds"),
            TimedMetadataBehavior=json_data.get("TimedMetadataBehavior"),
            DvbTeletextPid=json_data.get("DvbTeletextPid"),
            Scte35Control=json_data.get("Scte35Control"),
            PcrPeriod=json_data.get("PcrPeriod"),
            SegmentationTime=json_data.get("SegmentationTime"),
            CcDescriptor=json_data.get("CcDescriptor"),
            PmtPid=json_data.get("PmtPid"),
            DvbNitSettings=DvbNitSettings._deserialize(json_data.get("DvbNitSettings")),
            EtvSignalPid=json_data.get("EtvSignalPid"),
            Arib=json_data.get("Arib"),
            TimedMetadataPid=json_data.get("TimedMetadataPid"),
            AudioPids=json_data.get("AudioPids"),
            AudioBufferModel=json_data.get("AudioBufferModel"),
            Ebif=json_data.get("Ebif"),
            PcrControl=json_data.get("PcrControl"),
            PatInterval=json_data.get("PatInterval"),
            ProgramNum=json_data.get("ProgramNum"),
            RateMode=json_data.get("RateMode"),
            KlvDataPids=json_data.get("KlvDataPids"),
            NullPacketBitrate=json_data.get("NullPacketBitrate"),
            PmtInterval=json_data.get("PmtInterval"),
            EsRateInPes=json_data.get("EsRateInPes"),
            VideoPid=json_data.get("VideoPid"),
            TransportStreamId=json_data.get("TransportStreamId"),
            Scte35Pid=json_data.get("Scte35Pid"),
            AudioStreamType=json_data.get("AudioStreamType"),
            EbpLookaheadMs=json_data.get("EbpLookaheadMs"),
            DvbTdtSettings=DvbTdtSettings._deserialize(json_data.get("DvbTdtSettings")),
            EbpAudioInterval=json_data.get("EbpAudioInterval"),
            FragmentTime=json_data.get("FragmentTime"),
            NielsenId3Behavior=json_data.get("NielsenId3Behavior"),
            PcrPid=json_data.get("PcrPid"),
            AudioFramesPerPes=json_data.get("AudioFramesPerPes"),
            AbsentInputAudioBehavior=json_data.get("AbsentInputAudioBehavior"),
            Bitrate=json_data.get("Bitrate"),
            Scte27Pids=json_data.get("Scte27Pids"),
            SegmentationMarkers=json_data.get("SegmentationMarkers"),
            DvbSdtSettings=DvbSdtSettings._deserialize(json_data.get("DvbSdtSettings")),
            BufferModel=json_data.get("BufferModel"),
            EcmPid=json_data.get("EcmPid"),
            AribCaptionsPidControl=json_data.get("AribCaptionsPidControl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_M2tsSettings = M2tsSettings


@dataclass
class DvbNitSettings(BaseModel):
    NetworkName: Optional[str]
    NetworkId: Optional[int]
    RepInterval: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_DvbNitSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DvbNitSettings"]:
        if not json_data:
            return None
        return cls(
            NetworkName=json_data.get("NetworkName"),
            NetworkId=json_data.get("NetworkId"),
            RepInterval=json_data.get("RepInterval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DvbNitSettings = DvbNitSettings


@dataclass
class DvbTdtSettings(BaseModel):
    RepInterval: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_DvbTdtSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DvbTdtSettings"]:
        if not json_data:
            return None
        return cls(
            RepInterval=json_data.get("RepInterval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DvbTdtSettings = DvbTdtSettings


@dataclass
class DvbSdtSettings(BaseModel):
    ServiceProviderName: Optional[str]
    OutputSdt: Optional[str]
    ServiceName: Optional[str]
    RepInterval: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_DvbSdtSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DvbSdtSettings"]:
        if not json_data:
            return None
        return cls(
            ServiceProviderName=json_data.get("ServiceProviderName"),
            OutputSdt=json_data.get("OutputSdt"),
            ServiceName=json_data.get("ServiceName"),
            RepInterval=json_data.get("RepInterval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DvbSdtSettings = DvbSdtSettings


@dataclass
class MultiplexOutputSettings(BaseModel):
    Destination: Optional["_OutputLocationRef"]

    @classmethod
    def _deserialize(
        cls: Type["_MultiplexOutputSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MultiplexOutputSettings"]:
        if not json_data:
            return None
        return cls(
            Destination=OutputLocationRef._deserialize(json_data.get("Destination")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MultiplexOutputSettings = MultiplexOutputSettings


@dataclass
class ArchiveOutputSettings(BaseModel):
    Extension: Optional[str]
    NameModifier: Optional[str]
    ContainerSettings: Optional["_ArchiveContainerSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_ArchiveOutputSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArchiveOutputSettings"]:
        if not json_data:
            return None
        return cls(
            Extension=json_data.get("Extension"),
            NameModifier=json_data.get("NameModifier"),
            ContainerSettings=ArchiveContainerSettings._deserialize(json_data.get("ContainerSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArchiveOutputSettings = ArchiveOutputSettings


@dataclass
class ArchiveContainerSettings(BaseModel):
    M2tsSettings: Optional["_M2tsSettings"]
    RawSettings: Optional[MutableMapping[str, Any]]

    @classmethod
    def _deserialize(
        cls: Type["_ArchiveContainerSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArchiveContainerSettings"]:
        if not json_data:
            return None
        return cls(
            M2tsSettings=M2tsSettings._deserialize(json_data.get("M2tsSettings")),
            RawSettings=json_data.get("RawSettings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArchiveContainerSettings = ArchiveContainerSettings


@dataclass
class OutputGroupSettings(BaseModel):
    HlsGroupSettings: Optional["_HlsGroupSettings"]
    FrameCaptureGroupSettings: Optional["_FrameCaptureGroupSettings"]
    MultiplexGroupSettings: Optional[MutableMapping[str, Any]]
    ArchiveGroupSettings: Optional["_ArchiveGroupSettings"]
    MediaPackageGroupSettings: Optional["_MediaPackageGroupSettings"]
    UdpGroupSettings: Optional["_UdpGroupSettings"]
    MsSmoothGroupSettings: Optional["_MsSmoothGroupSettings"]
    RtmpGroupSettings: Optional["_RtmpGroupSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_OutputGroupSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputGroupSettings"]:
        if not json_data:
            return None
        return cls(
            HlsGroupSettings=HlsGroupSettings._deserialize(json_data.get("HlsGroupSettings")),
            FrameCaptureGroupSettings=FrameCaptureGroupSettings._deserialize(json_data.get("FrameCaptureGroupSettings")),
            MultiplexGroupSettings=json_data.get("MultiplexGroupSettings"),
            ArchiveGroupSettings=ArchiveGroupSettings._deserialize(json_data.get("ArchiveGroupSettings")),
            MediaPackageGroupSettings=MediaPackageGroupSettings._deserialize(json_data.get("MediaPackageGroupSettings")),
            UdpGroupSettings=UdpGroupSettings._deserialize(json_data.get("UdpGroupSettings")),
            MsSmoothGroupSettings=MsSmoothGroupSettings._deserialize(json_data.get("MsSmoothGroupSettings")),
            RtmpGroupSettings=RtmpGroupSettings._deserialize(json_data.get("RtmpGroupSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputGroupSettings = OutputGroupSettings


@dataclass
class HlsGroupSettings(BaseModel):
    SegmentationMode: Optional[str]
    Destination: Optional["_OutputLocationRef"]
    CodecSpecification: Optional[str]
    IvSource: Optional[str]
    TimedMetadataId3Frame: Optional[str]
    KeyFormatVersions: Optional[str]
    RedundantManifest: Optional[str]
    OutputSelection: Optional[str]
    KeyProviderSettings: Optional["_KeyProviderSettings"]
    StreamInfResolution: Optional[str]
    CaptionLanguageMappings: Optional[Sequence["_CaptionLanguageMapping"]]
    HlsId3SegmentTagging: Optional[str]
    IFrameOnlyPlaylists: Optional[str]
    CaptionLanguageSetting: Optional[str]
    KeepSegments: Optional[int]
    ConstantIv: Optional[str]
    DirectoryStructure: Optional[str]
    EncryptionType: Optional[str]
    AdMarkers: Optional[Sequence[str]]
    HlsCdnSettings: Optional["_HlsCdnSettings"]
    IndexNSegments: Optional[int]
    DiscontinuityTags: Optional[str]
    InputLossAction: Optional[str]
    Mode: Optional[str]
    TsFileMode: Optional[str]
    BaseUrlManifest1: Optional[str]
    ClientCache: Optional[str]
    MinSegmentLength: Optional[int]
    KeyFormat: Optional[str]
    IvInManifest: Optional[str]
    BaseUrlContent1: Optional[str]
    ProgramDateTimeClock: Optional[str]
    ManifestCompression: Optional[str]
    ManifestDurationFormat: Optional[str]
    TimedMetadataId3Period: Optional[int]
    IncompleteSegmentBehavior: Optional[str]
    ProgramDateTimePeriod: Optional[int]
    SegmentLength: Optional[int]
    TimestampDeltaMilliseconds: Optional[int]
    ProgramDateTime: Optional[str]
    SegmentsPerSubdirectory: Optional[int]
    BaseUrlContent: Optional[str]
    BaseUrlManifest: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HlsGroupSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HlsGroupSettings"]:
        if not json_data:
            return None
        return cls(
            SegmentationMode=json_data.get("SegmentationMode"),
            Destination=OutputLocationRef._deserialize(json_data.get("Destination")),
            CodecSpecification=json_data.get("CodecSpecification"),
            IvSource=json_data.get("IvSource"),
            TimedMetadataId3Frame=json_data.get("TimedMetadataId3Frame"),
            KeyFormatVersions=json_data.get("KeyFormatVersions"),
            RedundantManifest=json_data.get("RedundantManifest"),
            OutputSelection=json_data.get("OutputSelection"),
            KeyProviderSettings=KeyProviderSettings._deserialize(json_data.get("KeyProviderSettings")),
            StreamInfResolution=json_data.get("StreamInfResolution"),
            CaptionLanguageMappings=deserialize_list(json_data.get("CaptionLanguageMappings"), CaptionLanguageMapping),
            HlsId3SegmentTagging=json_data.get("HlsId3SegmentTagging"),
            IFrameOnlyPlaylists=json_data.get("IFrameOnlyPlaylists"),
            CaptionLanguageSetting=json_data.get("CaptionLanguageSetting"),
            KeepSegments=json_data.get("KeepSegments"),
            ConstantIv=json_data.get("ConstantIv"),
            DirectoryStructure=json_data.get("DirectoryStructure"),
            EncryptionType=json_data.get("EncryptionType"),
            AdMarkers=json_data.get("AdMarkers"),
            HlsCdnSettings=HlsCdnSettings._deserialize(json_data.get("HlsCdnSettings")),
            IndexNSegments=json_data.get("IndexNSegments"),
            DiscontinuityTags=json_data.get("DiscontinuityTags"),
            InputLossAction=json_data.get("InputLossAction"),
            Mode=json_data.get("Mode"),
            TsFileMode=json_data.get("TsFileMode"),
            BaseUrlManifest1=json_data.get("BaseUrlManifest1"),
            ClientCache=json_data.get("ClientCache"),
            MinSegmentLength=json_data.get("MinSegmentLength"),
            KeyFormat=json_data.get("KeyFormat"),
            IvInManifest=json_data.get("IvInManifest"),
            BaseUrlContent1=json_data.get("BaseUrlContent1"),
            ProgramDateTimeClock=json_data.get("ProgramDateTimeClock"),
            ManifestCompression=json_data.get("ManifestCompression"),
            ManifestDurationFormat=json_data.get("ManifestDurationFormat"),
            TimedMetadataId3Period=json_data.get("TimedMetadataId3Period"),
            IncompleteSegmentBehavior=json_data.get("IncompleteSegmentBehavior"),
            ProgramDateTimePeriod=json_data.get("ProgramDateTimePeriod"),
            SegmentLength=json_data.get("SegmentLength"),
            TimestampDeltaMilliseconds=json_data.get("TimestampDeltaMilliseconds"),
            ProgramDateTime=json_data.get("ProgramDateTime"),
            SegmentsPerSubdirectory=json_data.get("SegmentsPerSubdirectory"),
            BaseUrlContent=json_data.get("BaseUrlContent"),
            BaseUrlManifest=json_data.get("BaseUrlManifest"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HlsGroupSettings = HlsGroupSettings


@dataclass
class KeyProviderSettings(BaseModel):
    StaticKeySettings: Optional["_StaticKeySettings"]

    @classmethod
    def _deserialize(
        cls: Type["_KeyProviderSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyProviderSettings"]:
        if not json_data:
            return None
        return cls(
            StaticKeySettings=StaticKeySettings._deserialize(json_data.get("StaticKeySettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyProviderSettings = KeyProviderSettings


@dataclass
class StaticKeySettings(BaseModel):
    KeyProviderServer: Optional["_InputLocation"]
    StaticKeyValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StaticKeySettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticKeySettings"]:
        if not json_data:
            return None
        return cls(
            KeyProviderServer=InputLocation._deserialize(json_data.get("KeyProviderServer")),
            StaticKeyValue=json_data.get("StaticKeyValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticKeySettings = StaticKeySettings


@dataclass
class CaptionLanguageMapping(BaseModel):
    LanguageCode: Optional[str]
    LanguageDescription: Optional[str]
    CaptionChannel: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_CaptionLanguageMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaptionLanguageMapping"]:
        if not json_data:
            return None
        return cls(
            LanguageCode=json_data.get("LanguageCode"),
            LanguageDescription=json_data.get("LanguageDescription"),
            CaptionChannel=json_data.get("CaptionChannel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CaptionLanguageMapping = CaptionLanguageMapping


@dataclass
class HlsCdnSettings(BaseModel):
    HlsWebdavSettings: Optional["_HlsWebdavSettings"]
    HlsS3Settings: Optional["_HlsS3Settings"]
    HlsBasicPutSettings: Optional["_HlsBasicPutSettings"]
    HlsMediaStoreSettings: Optional["_HlsMediaStoreSettings"]
    HlsAkamaiSettings: Optional["_HlsAkamaiSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_HlsCdnSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HlsCdnSettings"]:
        if not json_data:
            return None
        return cls(
            HlsWebdavSettings=HlsWebdavSettings._deserialize(json_data.get("HlsWebdavSettings")),
            HlsS3Settings=HlsS3Settings._deserialize(json_data.get("HlsS3Settings")),
            HlsBasicPutSettings=HlsBasicPutSettings._deserialize(json_data.get("HlsBasicPutSettings")),
            HlsMediaStoreSettings=HlsMediaStoreSettings._deserialize(json_data.get("HlsMediaStoreSettings")),
            HlsAkamaiSettings=HlsAkamaiSettings._deserialize(json_data.get("HlsAkamaiSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HlsCdnSettings = HlsCdnSettings


@dataclass
class HlsWebdavSettings(BaseModel):
    FilecacheDuration: Optional[int]
    RestartDelay: Optional[int]
    NumRetries: Optional[int]
    ConnectionRetryInterval: Optional[int]
    HttpTransferMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HlsWebdavSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HlsWebdavSettings"]:
        if not json_data:
            return None
        return cls(
            FilecacheDuration=json_data.get("FilecacheDuration"),
            RestartDelay=json_data.get("RestartDelay"),
            NumRetries=json_data.get("NumRetries"),
            ConnectionRetryInterval=json_data.get("ConnectionRetryInterval"),
            HttpTransferMode=json_data.get("HttpTransferMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HlsWebdavSettings = HlsWebdavSettings


@dataclass
class HlsS3Settings(BaseModel):
    CannedAcl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HlsS3Settings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HlsS3Settings"]:
        if not json_data:
            return None
        return cls(
            CannedAcl=json_data.get("CannedAcl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HlsS3Settings = HlsS3Settings


@dataclass
class HlsBasicPutSettings(BaseModel):
    FilecacheDuration: Optional[int]
    RestartDelay: Optional[int]
    NumRetries: Optional[int]
    ConnectionRetryInterval: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_HlsBasicPutSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HlsBasicPutSettings"]:
        if not json_data:
            return None
        return cls(
            FilecacheDuration=json_data.get("FilecacheDuration"),
            RestartDelay=json_data.get("RestartDelay"),
            NumRetries=json_data.get("NumRetries"),
            ConnectionRetryInterval=json_data.get("ConnectionRetryInterval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HlsBasicPutSettings = HlsBasicPutSettings


@dataclass
class HlsMediaStoreSettings(BaseModel):
    FilecacheDuration: Optional[int]
    MediaStoreStorageClass: Optional[str]
    RestartDelay: Optional[int]
    NumRetries: Optional[int]
    ConnectionRetryInterval: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_HlsMediaStoreSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HlsMediaStoreSettings"]:
        if not json_data:
            return None
        return cls(
            FilecacheDuration=json_data.get("FilecacheDuration"),
            MediaStoreStorageClass=json_data.get("MediaStoreStorageClass"),
            RestartDelay=json_data.get("RestartDelay"),
            NumRetries=json_data.get("NumRetries"),
            ConnectionRetryInterval=json_data.get("ConnectionRetryInterval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HlsMediaStoreSettings = HlsMediaStoreSettings


@dataclass
class HlsAkamaiSettings(BaseModel):
    Salt: Optional[str]
    FilecacheDuration: Optional[int]
    NumRetries: Optional[int]
    Token: Optional[str]
    RestartDelay: Optional[int]
    ConnectionRetryInterval: Optional[int]
    HttpTransferMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HlsAkamaiSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HlsAkamaiSettings"]:
        if not json_data:
            return None
        return cls(
            Salt=json_data.get("Salt"),
            FilecacheDuration=json_data.get("FilecacheDuration"),
            NumRetries=json_data.get("NumRetries"),
            Token=json_data.get("Token"),
            RestartDelay=json_data.get("RestartDelay"),
            ConnectionRetryInterval=json_data.get("ConnectionRetryInterval"),
            HttpTransferMode=json_data.get("HttpTransferMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HlsAkamaiSettings = HlsAkamaiSettings


@dataclass
class FrameCaptureGroupSettings(BaseModel):
    FrameCaptureCdnSettings: Optional["_FrameCaptureCdnSettings"]
    Destination: Optional["_OutputLocationRef"]

    @classmethod
    def _deserialize(
        cls: Type["_FrameCaptureGroupSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FrameCaptureGroupSettings"]:
        if not json_data:
            return None
        return cls(
            FrameCaptureCdnSettings=FrameCaptureCdnSettings._deserialize(json_data.get("FrameCaptureCdnSettings")),
            Destination=OutputLocationRef._deserialize(json_data.get("Destination")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FrameCaptureGroupSettings = FrameCaptureGroupSettings


@dataclass
class FrameCaptureCdnSettings(BaseModel):
    FrameCaptureS3Settings: Optional["_FrameCaptureS3Settings"]

    @classmethod
    def _deserialize(
        cls: Type["_FrameCaptureCdnSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FrameCaptureCdnSettings"]:
        if not json_data:
            return None
        return cls(
            FrameCaptureS3Settings=FrameCaptureS3Settings._deserialize(json_data.get("FrameCaptureS3Settings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FrameCaptureCdnSettings = FrameCaptureCdnSettings


@dataclass
class FrameCaptureS3Settings(BaseModel):
    CannedAcl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FrameCaptureS3Settings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FrameCaptureS3Settings"]:
        if not json_data:
            return None
        return cls(
            CannedAcl=json_data.get("CannedAcl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FrameCaptureS3Settings = FrameCaptureS3Settings


@dataclass
class ArchiveGroupSettings(BaseModel):
    Destination: Optional["_OutputLocationRef"]
    ArchiveCdnSettings: Optional["_ArchiveCdnSettings"]
    RolloverInterval: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ArchiveGroupSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArchiveGroupSettings"]:
        if not json_data:
            return None
        return cls(
            Destination=OutputLocationRef._deserialize(json_data.get("Destination")),
            ArchiveCdnSettings=ArchiveCdnSettings._deserialize(json_data.get("ArchiveCdnSettings")),
            RolloverInterval=json_data.get("RolloverInterval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArchiveGroupSettings = ArchiveGroupSettings


@dataclass
class ArchiveCdnSettings(BaseModel):
    ArchiveS3Settings: Optional["_ArchiveS3Settings"]

    @classmethod
    def _deserialize(
        cls: Type["_ArchiveCdnSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArchiveCdnSettings"]:
        if not json_data:
            return None
        return cls(
            ArchiveS3Settings=ArchiveS3Settings._deserialize(json_data.get("ArchiveS3Settings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArchiveCdnSettings = ArchiveCdnSettings


@dataclass
class ArchiveS3Settings(BaseModel):
    CannedAcl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ArchiveS3Settings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArchiveS3Settings"]:
        if not json_data:
            return None
        return cls(
            CannedAcl=json_data.get("CannedAcl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArchiveS3Settings = ArchiveS3Settings


@dataclass
class MediaPackageGroupSettings(BaseModel):
    Destination: Optional["_OutputLocationRef"]

    @classmethod
    def _deserialize(
        cls: Type["_MediaPackageGroupSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MediaPackageGroupSettings"]:
        if not json_data:
            return None
        return cls(
            Destination=OutputLocationRef._deserialize(json_data.get("Destination")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MediaPackageGroupSettings = MediaPackageGroupSettings


@dataclass
class UdpGroupSettings(BaseModel):
    TimedMetadataId3Frame: Optional[str]
    TimedMetadataId3Period: Optional[int]
    InputLossAction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UdpGroupSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UdpGroupSettings"]:
        if not json_data:
            return None
        return cls(
            TimedMetadataId3Frame=json_data.get("TimedMetadataId3Frame"),
            TimedMetadataId3Period=json_data.get("TimedMetadataId3Period"),
            InputLossAction=json_data.get("InputLossAction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UdpGroupSettings = UdpGroupSettings


@dataclass
class MsSmoothGroupSettings(BaseModel):
    SegmentationMode: Optional[str]
    Destination: Optional["_OutputLocationRef"]
    EventStopBehavior: Optional[str]
    FilecacheDuration: Optional[int]
    CertificateMode: Optional[str]
    AcquisitionPointId: Optional[str]
    StreamManifestBehavior: Optional[str]
    InputLossAction: Optional[str]
    FragmentLength: Optional[int]
    RestartDelay: Optional[int]
    SparseTrackType: Optional[str]
    EventIdMode: Optional[str]
    TimestampOffsetMode: Optional[str]
    AudioOnlyTimecodeControl: Optional[str]
    NumRetries: Optional[int]
    TimestampOffset: Optional[str]
    EventId: Optional[str]
    SendDelayMs: Optional[int]
    ConnectionRetryInterval: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_MsSmoothGroupSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MsSmoothGroupSettings"]:
        if not json_data:
            return None
        return cls(
            SegmentationMode=json_data.get("SegmentationMode"),
            Destination=OutputLocationRef._deserialize(json_data.get("Destination")),
            EventStopBehavior=json_data.get("EventStopBehavior"),
            FilecacheDuration=json_data.get("FilecacheDuration"),
            CertificateMode=json_data.get("CertificateMode"),
            AcquisitionPointId=json_data.get("AcquisitionPointId"),
            StreamManifestBehavior=json_data.get("StreamManifestBehavior"),
            InputLossAction=json_data.get("InputLossAction"),
            FragmentLength=json_data.get("FragmentLength"),
            RestartDelay=json_data.get("RestartDelay"),
            SparseTrackType=json_data.get("SparseTrackType"),
            EventIdMode=json_data.get("EventIdMode"),
            TimestampOffsetMode=json_data.get("TimestampOffsetMode"),
            AudioOnlyTimecodeControl=json_data.get("AudioOnlyTimecodeControl"),
            NumRetries=json_data.get("NumRetries"),
            TimestampOffset=json_data.get("TimestampOffset"),
            EventId=json_data.get("EventId"),
            SendDelayMs=json_data.get("SendDelayMs"),
            ConnectionRetryInterval=json_data.get("ConnectionRetryInterval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MsSmoothGroupSettings = MsSmoothGroupSettings


@dataclass
class RtmpGroupSettings(BaseModel):
    AuthenticationScheme: Optional[str]
    CacheLength: Optional[int]
    AdMarkers: Optional[Sequence[str]]
    InputLossAction: Optional[str]
    RestartDelay: Optional[int]
    CaptionData: Optional[str]
    CacheFullBehavior: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RtmpGroupSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RtmpGroupSettings"]:
        if not json_data:
            return None
        return cls(
            AuthenticationScheme=json_data.get("AuthenticationScheme"),
            CacheLength=json_data.get("CacheLength"),
            AdMarkers=json_data.get("AdMarkers"),
            InputLossAction=json_data.get("InputLossAction"),
            RestartDelay=json_data.get("RestartDelay"),
            CaptionData=json_data.get("CaptionData"),
            CacheFullBehavior=json_data.get("CacheFullBehavior"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RtmpGroupSettings = RtmpGroupSettings


@dataclass
class AvailBlanking(BaseModel):
    State: Optional[str]
    AvailBlankingImage: Optional["_InputLocation"]

    @classmethod
    def _deserialize(
        cls: Type["_AvailBlanking"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AvailBlanking"]:
        if not json_data:
            return None
        return cls(
            State=json_data.get("State"),
            AvailBlankingImage=InputLocation._deserialize(json_data.get("AvailBlankingImage")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AvailBlanking = AvailBlanking


@dataclass
class NielsenConfiguration(BaseModel):
    DistributorId: Optional[str]
    NielsenPcmToId3Tagging: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NielsenConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NielsenConfiguration"]:
        if not json_data:
            return None
        return cls(
            DistributorId=json_data.get("DistributorId"),
            NielsenPcmToId3Tagging=json_data.get("NielsenPcmToId3Tagging"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NielsenConfiguration = NielsenConfiguration


@dataclass
class BlackoutSlate(BaseModel):
    NetworkId: Optional[str]
    NetworkEndBlackoutImage: Optional["_InputLocation"]
    NetworkEndBlackout: Optional[str]
    State: Optional[str]
    BlackoutSlateImage: Optional["_InputLocation"]

    @classmethod
    def _deserialize(
        cls: Type["_BlackoutSlate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlackoutSlate"]:
        if not json_data:
            return None
        return cls(
            NetworkId=json_data.get("NetworkId"),
            NetworkEndBlackoutImage=InputLocation._deserialize(json_data.get("NetworkEndBlackoutImage")),
            NetworkEndBlackout=json_data.get("NetworkEndBlackout"),
            State=json_data.get("State"),
            BlackoutSlateImage=InputLocation._deserialize(json_data.get("BlackoutSlateImage")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlackoutSlate = BlackoutSlate


@dataclass
class TimecodeConfig(BaseModel):
    SyncThreshold: Optional[int]
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimecodeConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimecodeConfig"]:
        if not json_data:
            return None
        return cls(
            SyncThreshold=json_data.get("SyncThreshold"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimecodeConfig = TimecodeConfig


@dataclass
class CdiInputSpecification(BaseModel):
    Resolution: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CdiInputSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CdiInputSpecification"]:
        if not json_data:
            return None
        return cls(
            Resolution=json_data.get("Resolution"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CdiInputSpecification = CdiInputSpecification


