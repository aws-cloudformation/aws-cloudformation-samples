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
class AwsPinpointCampaign(BaseModel):
    Description: Optional[str]
    SegmentId: Optional[str]
    Priority: Optional[int]
    TemplateConfiguration: Optional["_TemplateConfiguration"]
    IsPaused: Optional[bool]
    AdditionalTreatments: Optional[Sequence["_WriteTreatmentResource"]]
    Name: Optional[str]
    SegmentVersion: Optional[int]
    TreatmentDescription: Optional[str]
    MessageConfiguration: Optional["_MessageConfiguration"]
    Limits: Optional["_Limits"]
    CampaignId: Optional[str]
    HoldoutPercent: Optional[int]
    Schedule: Optional["_Schedule"]
    CustomDeliveryConfiguration: Optional["_CustomDeliveryConfiguration"]
    Arn: Optional[str]
    ApplicationId: Optional[str]
    CampaignHook: Optional["_CampaignHook"]
    Tags: Optional[Any]
    TreatmentName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsPinpointCampaign"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsPinpointCampaign"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            SegmentId=json_data.get("SegmentId"),
            Priority=json_data.get("Priority"),
            TemplateConfiguration=TemplateConfiguration._deserialize(json_data.get("TemplateConfiguration")),
            IsPaused=json_data.get("IsPaused"),
            AdditionalTreatments=deserialize_list(json_data.get("AdditionalTreatments"), WriteTreatmentResource),
            Name=json_data.get("Name"),
            SegmentVersion=json_data.get("SegmentVersion"),
            TreatmentDescription=json_data.get("TreatmentDescription"),
            MessageConfiguration=MessageConfiguration._deserialize(json_data.get("MessageConfiguration")),
            Limits=Limits._deserialize(json_data.get("Limits")),
            CampaignId=json_data.get("CampaignId"),
            HoldoutPercent=json_data.get("HoldoutPercent"),
            Schedule=Schedule._deserialize(json_data.get("Schedule")),
            CustomDeliveryConfiguration=CustomDeliveryConfiguration._deserialize(json_data.get("CustomDeliveryConfiguration")),
            Arn=json_data.get("Arn"),
            ApplicationId=json_data.get("ApplicationId"),
            CampaignHook=CampaignHook._deserialize(json_data.get("CampaignHook")),
            Tags=json_data.get("Tags"),
            TreatmentName=json_data.get("TreatmentName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsPinpointCampaign = AwsPinpointCampaign


@dataclass
class TemplateConfiguration(BaseModel):
    SMSTemplate: Optional["_Template"]
    EmailTemplate: Optional["_Template"]
    PushTemplate: Optional["_Template"]
    VoiceTemplate: Optional["_Template"]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateConfiguration"]:
        if not json_data:
            return None
        return cls(
            SMSTemplate=Template._deserialize(json_data.get("SMSTemplate")),
            EmailTemplate=Template._deserialize(json_data.get("EmailTemplate")),
            PushTemplate=Template._deserialize(json_data.get("PushTemplate")),
            VoiceTemplate=Template._deserialize(json_data.get("VoiceTemplate")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateConfiguration = TemplateConfiguration


@dataclass
class Template(BaseModel):
    Version: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Template"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Template"]:
        if not json_data:
            return None
        return cls(
            Version=json_data.get("Version"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Template = Template


@dataclass
class WriteTreatmentResource(BaseModel):
    TreatmentDescription: Optional[str]
    MessageConfiguration: Optional["_MessageConfiguration"]
    Schedule: Optional["_Schedule"]
    TemplateConfiguration: Optional["_TemplateConfiguration"]
    CustomDeliveryConfiguration: Optional["_CustomDeliveryConfiguration"]
    SizePercent: Optional[int]
    TreatmentName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WriteTreatmentResource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WriteTreatmentResource"]:
        if not json_data:
            return None
        return cls(
            TreatmentDescription=json_data.get("TreatmentDescription"),
            MessageConfiguration=MessageConfiguration._deserialize(json_data.get("MessageConfiguration")),
            Schedule=Schedule._deserialize(json_data.get("Schedule")),
            TemplateConfiguration=TemplateConfiguration._deserialize(json_data.get("TemplateConfiguration")),
            CustomDeliveryConfiguration=CustomDeliveryConfiguration._deserialize(json_data.get("CustomDeliveryConfiguration")),
            SizePercent=json_data.get("SizePercent"),
            TreatmentName=json_data.get("TreatmentName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WriteTreatmentResource = WriteTreatmentResource


@dataclass
class MessageConfiguration(BaseModel):
    APNSMessage: Optional["_Message"]
    BaiduMessage: Optional["_Message"]
    DefaultMessage: Optional["_Message"]
    InAppMessage: Optional["_CampaignInAppMessage"]
    EmailMessage: Optional["_CampaignEmailMessage"]
    GCMMessage: Optional["_Message"]
    SMSMessage: Optional["_CampaignSmsMessage"]
    CustomMessage: Optional["_CampaignCustomMessage"]
    ADMMessage: Optional["_Message"]

    @classmethod
    def _deserialize(
        cls: Type["_MessageConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MessageConfiguration"]:
        if not json_data:
            return None
        return cls(
            APNSMessage=Message._deserialize(json_data.get("APNSMessage")),
            BaiduMessage=Message._deserialize(json_data.get("BaiduMessage")),
            DefaultMessage=Message._deserialize(json_data.get("DefaultMessage")),
            InAppMessage=CampaignInAppMessage._deserialize(json_data.get("InAppMessage")),
            EmailMessage=CampaignEmailMessage._deserialize(json_data.get("EmailMessage")),
            GCMMessage=Message._deserialize(json_data.get("GCMMessage")),
            SMSMessage=CampaignSmsMessage._deserialize(json_data.get("SMSMessage")),
            CustomMessage=CampaignCustomMessage._deserialize(json_data.get("CustomMessage")),
            ADMMessage=Message._deserialize(json_data.get("ADMMessage")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MessageConfiguration = MessageConfiguration


@dataclass
class Message(BaseModel):
    Action: Optional[str]
    MediaUrl: Optional[str]
    TimeToLive: Optional[int]
    ImageSmallIconUrl: Optional[str]
    ImageUrl: Optional[str]
    Title: Optional[str]
    Url: Optional[str]
    JsonBody: Optional[str]
    ImageIconUrl: Optional[str]
    SilentPush: Optional[bool]
    Body: Optional[str]
    RawContent: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Message"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Message"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            MediaUrl=json_data.get("MediaUrl"),
            TimeToLive=json_data.get("TimeToLive"),
            ImageSmallIconUrl=json_data.get("ImageSmallIconUrl"),
            ImageUrl=json_data.get("ImageUrl"),
            Title=json_data.get("Title"),
            Url=json_data.get("Url"),
            JsonBody=json_data.get("JsonBody"),
            ImageIconUrl=json_data.get("ImageIconUrl"),
            SilentPush=json_data.get("SilentPush"),
            Body=json_data.get("Body"),
            RawContent=json_data.get("RawContent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Message = Message


@dataclass
class CampaignInAppMessage(BaseModel):
    CustomConfig: Optional[MutableMapping[str, Any]]
    Layout: Optional[str]
    Content: Optional[Sequence["_InAppMessageContent"]]

    @classmethod
    def _deserialize(
        cls: Type["_CampaignInAppMessage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CampaignInAppMessage"]:
        if not json_data:
            return None
        return cls(
            CustomConfig=json_data.get("CustomConfig"),
            Layout=json_data.get("Layout"),
            Content=deserialize_list(json_data.get("Content"), InAppMessageContent),
        )


# work around possible type aliasing issues when variable has same name as a model
_CampaignInAppMessage = CampaignInAppMessage


@dataclass
class InAppMessageContent(BaseModel):
    BodyConfig: Optional["_InAppMessageBodyConfig"]
    SecondaryBtn: Optional["_InAppMessageButton"]
    ImageUrl: Optional[str]
    PrimaryBtn: Optional["_InAppMessageButton"]
    HeaderConfig: Optional["_InAppMessageHeaderConfig"]
    BackgroundColor: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InAppMessageContent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InAppMessageContent"]:
        if not json_data:
            return None
        return cls(
            BodyConfig=InAppMessageBodyConfig._deserialize(json_data.get("BodyConfig")),
            SecondaryBtn=InAppMessageButton._deserialize(json_data.get("SecondaryBtn")),
            ImageUrl=json_data.get("ImageUrl"),
            PrimaryBtn=InAppMessageButton._deserialize(json_data.get("PrimaryBtn")),
            HeaderConfig=InAppMessageHeaderConfig._deserialize(json_data.get("HeaderConfig")),
            BackgroundColor=json_data.get("BackgroundColor"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InAppMessageContent = InAppMessageContent


@dataclass
class InAppMessageBodyConfig(BaseModel):
    Alignment: Optional[str]
    TextColor: Optional[str]
    Body: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InAppMessageBodyConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InAppMessageBodyConfig"]:
        if not json_data:
            return None
        return cls(
            Alignment=json_data.get("Alignment"),
            TextColor=json_data.get("TextColor"),
            Body=json_data.get("Body"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InAppMessageBodyConfig = InAppMessageBodyConfig


@dataclass
class InAppMessageButton(BaseModel):
    IOS: Optional["_OverrideButtonConfiguration"]
    Web: Optional["_OverrideButtonConfiguration"]
    DefaultConfig: Optional["_DefaultButtonConfiguration"]
    Android: Optional["_OverrideButtonConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_InAppMessageButton"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InAppMessageButton"]:
        if not json_data:
            return None
        return cls(
            IOS=OverrideButtonConfiguration._deserialize(json_data.get("IOS")),
            Web=OverrideButtonConfiguration._deserialize(json_data.get("Web")),
            DefaultConfig=DefaultButtonConfiguration._deserialize(json_data.get("DefaultConfig")),
            Android=OverrideButtonConfiguration._deserialize(json_data.get("Android")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InAppMessageButton = InAppMessageButton


@dataclass
class OverrideButtonConfiguration(BaseModel):
    ButtonAction: Optional[str]
    Link: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OverrideButtonConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverrideButtonConfiguration"]:
        if not json_data:
            return None
        return cls(
            ButtonAction=json_data.get("ButtonAction"),
            Link=json_data.get("Link"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverrideButtonConfiguration = OverrideButtonConfiguration


@dataclass
class DefaultButtonConfiguration(BaseModel):
    ButtonAction: Optional[str]
    BorderRadius: Optional[int]
    Text: Optional[str]
    TextColor: Optional[str]
    Link: Optional[str]
    BackgroundColor: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultButtonConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultButtonConfiguration"]:
        if not json_data:
            return None
        return cls(
            ButtonAction=json_data.get("ButtonAction"),
            BorderRadius=json_data.get("BorderRadius"),
            Text=json_data.get("Text"),
            TextColor=json_data.get("TextColor"),
            Link=json_data.get("Link"),
            BackgroundColor=json_data.get("BackgroundColor"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultButtonConfiguration = DefaultButtonConfiguration


@dataclass
class InAppMessageHeaderConfig(BaseModel):
    Alignment: Optional[str]
    TextColor: Optional[str]
    Header: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InAppMessageHeaderConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InAppMessageHeaderConfig"]:
        if not json_data:
            return None
        return cls(
            Alignment=json_data.get("Alignment"),
            TextColor=json_data.get("TextColor"),
            Header=json_data.get("Header"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InAppMessageHeaderConfig = InAppMessageHeaderConfig


@dataclass
class CampaignEmailMessage(BaseModel):
    Title: Optional[str]
    FromAddress: Optional[str]
    HtmlBody: Optional[str]
    Body: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CampaignEmailMessage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CampaignEmailMessage"]:
        if not json_data:
            return None
        return cls(
            Title=json_data.get("Title"),
            FromAddress=json_data.get("FromAddress"),
            HtmlBody=json_data.get("HtmlBody"),
            Body=json_data.get("Body"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CampaignEmailMessage = CampaignEmailMessage


@dataclass
class CampaignSmsMessage(BaseModel):
    EntityId: Optional[str]
    OriginationNumber: Optional[str]
    SenderId: Optional[str]
    Body: Optional[str]
    MessageType: Optional[str]
    TemplateId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CampaignSmsMessage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CampaignSmsMessage"]:
        if not json_data:
            return None
        return cls(
            EntityId=json_data.get("EntityId"),
            OriginationNumber=json_data.get("OriginationNumber"),
            SenderId=json_data.get("SenderId"),
            Body=json_data.get("Body"),
            MessageType=json_data.get("MessageType"),
            TemplateId=json_data.get("TemplateId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CampaignSmsMessage = CampaignSmsMessage


@dataclass
class CampaignCustomMessage(BaseModel):
    Data: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CampaignCustomMessage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CampaignCustomMessage"]:
        if not json_data:
            return None
        return cls(
            Data=json_data.get("Data"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CampaignCustomMessage = CampaignCustomMessage


@dataclass
class Schedule(BaseModel):
    TimeZone: Optional[str]
    QuietTime: Optional["_QuietTime"]
    EndTime: Optional[str]
    StartTime: Optional[str]
    Frequency: Optional[str]
    EventFilter: Optional["_CampaignEventFilter"]
    IsLocalTime: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Schedule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Schedule"]:
        if not json_data:
            return None
        return cls(
            TimeZone=json_data.get("TimeZone"),
            QuietTime=QuietTime._deserialize(json_data.get("QuietTime")),
            EndTime=json_data.get("EndTime"),
            StartTime=json_data.get("StartTime"),
            Frequency=json_data.get("Frequency"),
            EventFilter=CampaignEventFilter._deserialize(json_data.get("EventFilter")),
            IsLocalTime=json_data.get("IsLocalTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Schedule = Schedule


@dataclass
class QuietTime(BaseModel):
    Start: Optional[str]
    End: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QuietTime"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QuietTime"]:
        if not json_data:
            return None
        return cls(
            Start=json_data.get("Start"),
            End=json_data.get("End"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QuietTime = QuietTime


@dataclass
class CampaignEventFilter(BaseModel):
    Dimensions: Optional["_EventDimensions"]
    FilterType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CampaignEventFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CampaignEventFilter"]:
        if not json_data:
            return None
        return cls(
            Dimensions=EventDimensions._deserialize(json_data.get("Dimensions")),
            FilterType=json_data.get("FilterType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CampaignEventFilter = CampaignEventFilter


@dataclass
class EventDimensions(BaseModel):
    Attributes: Optional[MutableMapping[str, Any]]
    Metrics: Optional[MutableMapping[str, Any]]
    EventType: Optional["_SetDimension"]

    @classmethod
    def _deserialize(
        cls: Type["_EventDimensions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventDimensions"]:
        if not json_data:
            return None
        return cls(
            Attributes=json_data.get("Attributes"),
            Metrics=json_data.get("Metrics"),
            EventType=SetDimension._deserialize(json_data.get("EventType")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventDimensions = EventDimensions


@dataclass
class SetDimension(BaseModel):
    Values: Optional[Sequence[str]]
    DimensionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SetDimension"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SetDimension"]:
        if not json_data:
            return None
        return cls(
            Values=json_data.get("Values"),
            DimensionType=json_data.get("DimensionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SetDimension = SetDimension


@dataclass
class CustomDeliveryConfiguration(BaseModel):
    EndpointTypes: Optional[Sequence[str]]
    DeliveryUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomDeliveryConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomDeliveryConfiguration"]:
        if not json_data:
            return None
        return cls(
            EndpointTypes=json_data.get("EndpointTypes"),
            DeliveryUri=json_data.get("DeliveryUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomDeliveryConfiguration = CustomDeliveryConfiguration


@dataclass
class Limits(BaseModel):
    MessagesPerSecond: Optional[int]
    Daily: Optional[int]
    MaximumDuration: Optional[int]
    Total: Optional[int]
    Session: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Limits"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Limits"]:
        if not json_data:
            return None
        return cls(
            MessagesPerSecond=json_data.get("MessagesPerSecond"),
            Daily=json_data.get("Daily"),
            MaximumDuration=json_data.get("MaximumDuration"),
            Total=json_data.get("Total"),
            Session=json_data.get("Session"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Limits = Limits


@dataclass
class CampaignHook(BaseModel):
    WebUrl: Optional[str]
    LambdaFunctionName: Optional[str]
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CampaignHook"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CampaignHook"]:
        if not json_data:
            return None
        return cls(
            WebUrl=json_data.get("WebUrl"),
            LambdaFunctionName=json_data.get("LambdaFunctionName"),
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CampaignHook = CampaignHook


