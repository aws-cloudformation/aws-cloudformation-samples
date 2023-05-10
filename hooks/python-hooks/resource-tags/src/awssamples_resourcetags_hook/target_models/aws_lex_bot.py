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
class AwsLexBot(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]
    Name: Optional[str]
    Description: Optional[str]
    RoleArn: Optional[str]
    DataPrivacy: Optional["_DataPrivacy"]
    IdleSessionTTLInSeconds: Optional[int]
    BotLocales: Optional[AbstractSet["_BotLocale"]]
    BotFileS3Location: Optional["_S3Location"]
    BotTags: Optional[AbstractSet["_Tag"]]
    TestBotAliasTags: Optional[AbstractSet["_Tag"]]
    AutoBuildBotLocales: Optional[bool]
    TestBotAliasSettings: Optional["_TestBotAliasSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLexBot"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLexBot"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            RoleArn=json_data.get("RoleArn"),
            DataPrivacy=DataPrivacy._deserialize(json_data.get("DataPrivacy")),
            IdleSessionTTLInSeconds=json_data.get("IdleSessionTTLInSeconds"),
            BotLocales=set_or_none(json_data.get("BotLocales")),
            BotFileS3Location=S3Location._deserialize(json_data.get("BotFileS3Location")),
            BotTags=set_or_none(json_data.get("BotTags")),
            TestBotAliasTags=set_or_none(json_data.get("TestBotAliasTags")),
            AutoBuildBotLocales=json_data.get("AutoBuildBotLocales"),
            TestBotAliasSettings=TestBotAliasSettings._deserialize(json_data.get("TestBotAliasSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLexBot = AwsLexBot


@dataclass
class DataPrivacy(BaseModel):
    ChildDirected: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DataPrivacy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataPrivacy"]:
        if not json_data:
            return None
        return cls(
            ChildDirected=json_data.get("ChildDirected"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataPrivacy = DataPrivacy


@dataclass
class BotLocale(BaseModel):
    LocaleId: Optional[str]
    Description: Optional[str]
    VoiceSettings: Optional["_VoiceSettings"]
    NluConfidenceThreshold: Optional[float]
    Intents: Optional[AbstractSet["_Intent"]]
    SlotTypes: Optional[AbstractSet["_SlotType"]]
    CustomVocabulary: Optional["_CustomVocabulary"]

    @classmethod
    def _deserialize(
        cls: Type["_BotLocale"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BotLocale"]:
        if not json_data:
            return None
        return cls(
            LocaleId=json_data.get("LocaleId"),
            Description=json_data.get("Description"),
            VoiceSettings=VoiceSettings._deserialize(json_data.get("VoiceSettings")),
            NluConfidenceThreshold=json_data.get("NluConfidenceThreshold"),
            Intents=set_or_none(json_data.get("Intents")),
            SlotTypes=set_or_none(json_data.get("SlotTypes")),
            CustomVocabulary=CustomVocabulary._deserialize(json_data.get("CustomVocabulary")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BotLocale = BotLocale


@dataclass
class VoiceSettings(BaseModel):
    VoiceId: Optional[str]
    Engine: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VoiceSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VoiceSettings"]:
        if not json_data:
            return None
        return cls(
            VoiceId=json_data.get("VoiceId"),
            Engine=json_data.get("Engine"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VoiceSettings = VoiceSettings


@dataclass
class Intent(BaseModel):
    Name: Optional[str]
    Description: Optional[str]
    ParentIntentSignature: Optional[str]
    SampleUtterances: Optional[Sequence["_SampleUtterance"]]
    DialogCodeHook: Optional["_DialogCodeHookSetting"]
    FulfillmentCodeHook: Optional["_FulfillmentCodeHookSetting"]
    IntentConfirmationSetting: Optional["_IntentConfirmationSetting"]
    IntentClosingSetting: Optional["_IntentClosingSetting"]
    InitialResponseSetting: Optional["_InitialResponseSetting"]
    InputContexts: Optional[Sequence["_InputContext"]]
    OutputContexts: Optional[Sequence["_OutputContext"]]
    KendraConfiguration: Optional["_KendraConfiguration"]
    SlotPriorities: Optional[Sequence["_SlotPriority"]]
    Slots: Optional[AbstractSet["_Slot"]]

    @classmethod
    def _deserialize(
        cls: Type["_Intent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Intent"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            ParentIntentSignature=json_data.get("ParentIntentSignature"),
            SampleUtterances=deserialize_list(json_data.get("SampleUtterances"), SampleUtterance),
            DialogCodeHook=DialogCodeHookSetting._deserialize(json_data.get("DialogCodeHook")),
            FulfillmentCodeHook=FulfillmentCodeHookSetting._deserialize(json_data.get("FulfillmentCodeHook")),
            IntentConfirmationSetting=IntentConfirmationSetting._deserialize(json_data.get("IntentConfirmationSetting")),
            IntentClosingSetting=IntentClosingSetting._deserialize(json_data.get("IntentClosingSetting")),
            InitialResponseSetting=InitialResponseSetting._deserialize(json_data.get("InitialResponseSetting")),
            InputContexts=deserialize_list(json_data.get("InputContexts"), InputContext),
            OutputContexts=deserialize_list(json_data.get("OutputContexts"), OutputContext),
            KendraConfiguration=KendraConfiguration._deserialize(json_data.get("KendraConfiguration")),
            SlotPriorities=deserialize_list(json_data.get("SlotPriorities"), SlotPriority),
            Slots=set_or_none(json_data.get("Slots")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Intent = Intent


@dataclass
class SampleUtterance(BaseModel):
    Utterance: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SampleUtterance"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SampleUtterance"]:
        if not json_data:
            return None
        return cls(
            Utterance=json_data.get("Utterance"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SampleUtterance = SampleUtterance


@dataclass
class DialogCodeHookSetting(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DialogCodeHookSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DialogCodeHookSetting"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DialogCodeHookSetting = DialogCodeHookSetting


@dataclass
class FulfillmentCodeHookSetting(BaseModel):
    FulfillmentUpdatesSpecification: Optional["_FulfillmentUpdatesSpecification"]
    PostFulfillmentStatusSpecification: Optional["_PostFulfillmentStatusSpecification"]
    Enabled: Optional[bool]
    IsActive: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_FulfillmentCodeHookSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FulfillmentCodeHookSetting"]:
        if not json_data:
            return None
        return cls(
            FulfillmentUpdatesSpecification=FulfillmentUpdatesSpecification._deserialize(json_data.get("FulfillmentUpdatesSpecification")),
            PostFulfillmentStatusSpecification=PostFulfillmentStatusSpecification._deserialize(json_data.get("PostFulfillmentStatusSpecification")),
            Enabled=json_data.get("Enabled"),
            IsActive=json_data.get("IsActive"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FulfillmentCodeHookSetting = FulfillmentCodeHookSetting


@dataclass
class FulfillmentUpdatesSpecification(BaseModel):
    StartResponse: Optional["_FulfillmentStartResponseSpecification"]
    UpdateResponse: Optional["_FulfillmentUpdateResponseSpecification"]
    TimeoutInSeconds: Optional[int]
    Active: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_FulfillmentUpdatesSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FulfillmentUpdatesSpecification"]:
        if not json_data:
            return None
        return cls(
            StartResponse=FulfillmentStartResponseSpecification._deserialize(json_data.get("StartResponse")),
            UpdateResponse=FulfillmentUpdateResponseSpecification._deserialize(json_data.get("UpdateResponse")),
            TimeoutInSeconds=json_data.get("TimeoutInSeconds"),
            Active=json_data.get("Active"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FulfillmentUpdatesSpecification = FulfillmentUpdatesSpecification


@dataclass
class FulfillmentStartResponseSpecification(BaseModel):
    MessageGroups: Optional[Sequence["_MessageGroup"]]
    DelayInSeconds: Optional[int]
    AllowInterrupt: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_FulfillmentStartResponseSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FulfillmentStartResponseSpecification"]:
        if not json_data:
            return None
        return cls(
            MessageGroups=deserialize_list(json_data.get("MessageGroups"), MessageGroup),
            DelayInSeconds=json_data.get("DelayInSeconds"),
            AllowInterrupt=json_data.get("AllowInterrupt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FulfillmentStartResponseSpecification = FulfillmentStartResponseSpecification


@dataclass
class MessageGroup(BaseModel):
    Message: Optional["_Message"]
    Variations: Optional[Sequence["_Message"]]

    @classmethod
    def _deserialize(
        cls: Type["_MessageGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MessageGroup"]:
        if not json_data:
            return None
        return cls(
            Message=Message._deserialize(json_data.get("Message")),
            Variations=deserialize_list(json_data.get("Variations"), Message),
        )


# work around possible type aliasing issues when variable has same name as a model
_MessageGroup = MessageGroup


@dataclass
class Message(BaseModel):
    PlainTextMessage: Optional["_PlainTextMessage"]
    CustomPayload: Optional["_CustomPayload"]
    SSMLMessage: Optional["_SSMLMessage"]
    ImageResponseCard: Optional["_ImageResponseCard"]

    @classmethod
    def _deserialize(
        cls: Type["_Message"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Message"]:
        if not json_data:
            return None
        return cls(
            PlainTextMessage=PlainTextMessage._deserialize(json_data.get("PlainTextMessage")),
            CustomPayload=CustomPayload._deserialize(json_data.get("CustomPayload")),
            SSMLMessage=SSMLMessage._deserialize(json_data.get("SSMLMessage")),
            ImageResponseCard=ImageResponseCard._deserialize(json_data.get("ImageResponseCard")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Message = Message


@dataclass
class PlainTextMessage(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlainTextMessage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlainTextMessage"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlainTextMessage = PlainTextMessage


@dataclass
class CustomPayload(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomPayload"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomPayload"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomPayload = CustomPayload


@dataclass
class SSMLMessage(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SSMLMessage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SSMLMessage"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SSMLMessage = SSMLMessage


@dataclass
class ImageResponseCard(BaseModel):
    Title: Optional[str]
    Subtitle: Optional[str]
    ImageUrl: Optional[str]
    Buttons: Optional[Sequence["_Button"]]

    @classmethod
    def _deserialize(
        cls: Type["_ImageResponseCard"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageResponseCard"]:
        if not json_data:
            return None
        return cls(
            Title=json_data.get("Title"),
            Subtitle=json_data.get("Subtitle"),
            ImageUrl=json_data.get("ImageUrl"),
            Buttons=deserialize_list(json_data.get("Buttons"), Button),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageResponseCard = ImageResponseCard


@dataclass
class Button(BaseModel):
    Text: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Button"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Button"]:
        if not json_data:
            return None
        return cls(
            Text=json_data.get("Text"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Button = Button


@dataclass
class FulfillmentUpdateResponseSpecification(BaseModel):
    MessageGroups: Optional[Sequence["_MessageGroup"]]
    FrequencyInSeconds: Optional[int]
    AllowInterrupt: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_FulfillmentUpdateResponseSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FulfillmentUpdateResponseSpecification"]:
        if not json_data:
            return None
        return cls(
            MessageGroups=deserialize_list(json_data.get("MessageGroups"), MessageGroup),
            FrequencyInSeconds=json_data.get("FrequencyInSeconds"),
            AllowInterrupt=json_data.get("AllowInterrupt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FulfillmentUpdateResponseSpecification = FulfillmentUpdateResponseSpecification


@dataclass
class PostFulfillmentStatusSpecification(BaseModel):
    SuccessResponse: Optional["_ResponseSpecification"]
    SuccessNextStep: Optional["_DialogState"]
    SuccessConditional: Optional["_ConditionalSpecification"]
    FailureResponse: Optional["_ResponseSpecification"]
    FailureNextStep: Optional["_DialogState"]
    FailureConditional: Optional["_ConditionalSpecification"]
    TimeoutResponse: Optional["_ResponseSpecification"]
    TimeoutNextStep: Optional["_DialogState"]
    TimeoutConditional: Optional["_ConditionalSpecification"]

    @classmethod
    def _deserialize(
        cls: Type["_PostFulfillmentStatusSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PostFulfillmentStatusSpecification"]:
        if not json_data:
            return None
        return cls(
            SuccessResponse=ResponseSpecification._deserialize(json_data.get("SuccessResponse")),
            SuccessNextStep=DialogState._deserialize(json_data.get("SuccessNextStep")),
            SuccessConditional=ConditionalSpecification._deserialize(json_data.get("SuccessConditional")),
            FailureResponse=ResponseSpecification._deserialize(json_data.get("FailureResponse")),
            FailureNextStep=DialogState._deserialize(json_data.get("FailureNextStep")),
            FailureConditional=ConditionalSpecification._deserialize(json_data.get("FailureConditional")),
            TimeoutResponse=ResponseSpecification._deserialize(json_data.get("TimeoutResponse")),
            TimeoutNextStep=DialogState._deserialize(json_data.get("TimeoutNextStep")),
            TimeoutConditional=ConditionalSpecification._deserialize(json_data.get("TimeoutConditional")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PostFulfillmentStatusSpecification = PostFulfillmentStatusSpecification


@dataclass
class ResponseSpecification(BaseModel):
    MessageGroupsList: Optional[Sequence["_MessageGroup"]]
    AllowInterrupt: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseSpecification"]:
        if not json_data:
            return None
        return cls(
            MessageGroupsList=deserialize_list(json_data.get("MessageGroupsList"), MessageGroup),
            AllowInterrupt=json_data.get("AllowInterrupt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseSpecification = ResponseSpecification


@dataclass
class DialogState(BaseModel):
    DialogAction: Optional["_DialogAction"]
    Intent: Optional["_IntentOverride"]
    SessionAttributes: Optional[Sequence["_SessionAttribute"]]

    @classmethod
    def _deserialize(
        cls: Type["_DialogState"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DialogState"]:
        if not json_data:
            return None
        return cls(
            DialogAction=DialogAction._deserialize(json_data.get("DialogAction")),
            Intent=IntentOverride._deserialize(json_data.get("Intent")),
            SessionAttributes=deserialize_list(json_data.get("SessionAttributes"), SessionAttribute),
        )


# work around possible type aliasing issues when variable has same name as a model
_DialogState = DialogState


@dataclass
class DialogAction(BaseModel):
    Type: Optional[str]
    SlotToElicit: Optional[str]
    SuppressNextMessage: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DialogAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DialogAction"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            SlotToElicit=json_data.get("SlotToElicit"),
            SuppressNextMessage=json_data.get("SuppressNextMessage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DialogAction = DialogAction


@dataclass
class IntentOverride(BaseModel):
    Name: Optional[str]
    Slots: Optional[Sequence["_SlotValueOverrideMap"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntentOverride"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntentOverride"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Slots=deserialize_list(json_data.get("Slots"), SlotValueOverrideMap),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntentOverride = IntentOverride


@dataclass
class SlotValueOverrideMap(BaseModel):
    SlotName: Optional[str]
    SlotValueOverride: Optional["_SlotValueOverride"]

    @classmethod
    def _deserialize(
        cls: Type["_SlotValueOverrideMap"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlotValueOverrideMap"]:
        if not json_data:
            return None
        return cls(
            SlotName=json_data.get("SlotName"),
            SlotValueOverride=SlotValueOverride._deserialize(json_data.get("SlotValueOverride")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlotValueOverrideMap = SlotValueOverrideMap


@dataclass
class SlotValueOverride(BaseModel):
    Shape: Optional[str]
    Value: Optional["_SlotValue"]
    Values: Optional[Sequence["_SlotValueOverride"]]

    @classmethod
    def _deserialize(
        cls: Type["_SlotValueOverride"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlotValueOverride"]:
        if not json_data:
            return None
        return cls(
            Shape=json_data.get("Shape"),
            Value=SlotValue._deserialize(json_data.get("Value")),
            Values=deserialize_list(json_data.get("Values"), SlotValueOverride),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlotValueOverride = SlotValueOverride


@dataclass
class SlotValue(BaseModel):
    InterpretedValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SlotValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlotValue"]:
        if not json_data:
            return None
        return cls(
            InterpretedValue=json_data.get("InterpretedValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlotValue = SlotValue


@dataclass
class SessionAttribute(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SessionAttribute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SessionAttribute"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SessionAttribute = SessionAttribute


@dataclass
class ConditionalSpecification(BaseModel):
    IsActive: Optional[bool]
    ConditionalBranches: Optional[Sequence["_ConditionalBranch"]]
    DefaultBranch: Optional["_DefaultConditionalBranch"]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionalSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionalSpecification"]:
        if not json_data:
            return None
        return cls(
            IsActive=json_data.get("IsActive"),
            ConditionalBranches=deserialize_list(json_data.get("ConditionalBranches"), ConditionalBranch),
            DefaultBranch=DefaultConditionalBranch._deserialize(json_data.get("DefaultBranch")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionalSpecification = ConditionalSpecification


@dataclass
class ConditionalBranch(BaseModel):
    Name: Optional[str]
    Condition: Optional["_Condition"]
    NextStep: Optional["_DialogState"]
    Response: Optional["_ResponseSpecification"]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionalBranch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionalBranch"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Condition=Condition._deserialize(json_data.get("Condition")),
            NextStep=DialogState._deserialize(json_data.get("NextStep")),
            Response=ResponseSpecification._deserialize(json_data.get("Response")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionalBranch = ConditionalBranch


@dataclass
class Condition(BaseModel):
    ExpressionString: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Condition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Condition"]:
        if not json_data:
            return None
        return cls(
            ExpressionString=json_data.get("ExpressionString"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Condition = Condition


@dataclass
class DefaultConditionalBranch(BaseModel):
    NextStep: Optional["_DialogState"]
    Response: Optional["_ResponseSpecification"]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultConditionalBranch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultConditionalBranch"]:
        if not json_data:
            return None
        return cls(
            NextStep=DialogState._deserialize(json_data.get("NextStep")),
            Response=ResponseSpecification._deserialize(json_data.get("Response")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultConditionalBranch = DefaultConditionalBranch


@dataclass
class IntentConfirmationSetting(BaseModel):
    PromptSpecification: Optional["_PromptSpecification"]
    IsActive: Optional[bool]
    ConfirmationResponse: Optional["_ResponseSpecification"]
    ConfirmationNextStep: Optional["_DialogState"]
    ConfirmationConditional: Optional["_ConditionalSpecification"]
    DeclinationResponse: Optional["_ResponseSpecification"]
    DeclinationNextStep: Optional["_DialogState"]
    DeclinationConditional: Optional["_ConditionalSpecification"]
    FailureResponse: Optional["_ResponseSpecification"]
    FailureNextStep: Optional["_DialogState"]
    FailureConditional: Optional["_ConditionalSpecification"]
    CodeHook: Optional["_DialogCodeHookInvocationSetting"]
    ElicitationCodeHook: Optional["_ElicitationCodeHookInvocationSetting"]

    @classmethod
    def _deserialize(
        cls: Type["_IntentConfirmationSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntentConfirmationSetting"]:
        if not json_data:
            return None
        return cls(
            PromptSpecification=PromptSpecification._deserialize(json_data.get("PromptSpecification")),
            IsActive=json_data.get("IsActive"),
            ConfirmationResponse=ResponseSpecification._deserialize(json_data.get("ConfirmationResponse")),
            ConfirmationNextStep=DialogState._deserialize(json_data.get("ConfirmationNextStep")),
            ConfirmationConditional=ConditionalSpecification._deserialize(json_data.get("ConfirmationConditional")),
            DeclinationResponse=ResponseSpecification._deserialize(json_data.get("DeclinationResponse")),
            DeclinationNextStep=DialogState._deserialize(json_data.get("DeclinationNextStep")),
            DeclinationConditional=ConditionalSpecification._deserialize(json_data.get("DeclinationConditional")),
            FailureResponse=ResponseSpecification._deserialize(json_data.get("FailureResponse")),
            FailureNextStep=DialogState._deserialize(json_data.get("FailureNextStep")),
            FailureConditional=ConditionalSpecification._deserialize(json_data.get("FailureConditional")),
            CodeHook=DialogCodeHookInvocationSetting._deserialize(json_data.get("CodeHook")),
            ElicitationCodeHook=ElicitationCodeHookInvocationSetting._deserialize(json_data.get("ElicitationCodeHook")),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntentConfirmationSetting = IntentConfirmationSetting


@dataclass
class PromptSpecification(BaseModel):
    MessageGroupsList: Optional[Sequence["_MessageGroup"]]
    MaxRetries: Optional[int]
    AllowInterrupt: Optional[bool]
    MessageSelectionStrategy: Optional[str]
    PromptAttemptsSpecification: Optional[MutableMapping[str, "_PromptAttemptSpecification"]]

    @classmethod
    def _deserialize(
        cls: Type["_PromptSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PromptSpecification"]:
        if not json_data:
            return None
        return cls(
            MessageGroupsList=deserialize_list(json_data.get("MessageGroupsList"), MessageGroup),
            MaxRetries=json_data.get("MaxRetries"),
            AllowInterrupt=json_data.get("AllowInterrupt"),
            MessageSelectionStrategy=json_data.get("MessageSelectionStrategy"),
            PromptAttemptsSpecification=json_data.get("PromptAttemptsSpecification"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PromptSpecification = PromptSpecification


@dataclass
class PromptAttemptSpecification(BaseModel):
    AllowedInputTypes: Optional["_AllowedInputTypes"]
    AllowInterrupt: Optional[bool]
    AudioAndDTMFInputSpecification: Optional["_AudioAndDTMFInputSpecification"]
    TextInputSpecification: Optional["_TextInputSpecification"]

    @classmethod
    def _deserialize(
        cls: Type["_PromptAttemptSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PromptAttemptSpecification"]:
        if not json_data:
            return None
        return cls(
            AllowedInputTypes=AllowedInputTypes._deserialize(json_data.get("AllowedInputTypes")),
            AllowInterrupt=json_data.get("AllowInterrupt"),
            AudioAndDTMFInputSpecification=AudioAndDTMFInputSpecification._deserialize(json_data.get("AudioAndDTMFInputSpecification")),
            TextInputSpecification=TextInputSpecification._deserialize(json_data.get("TextInputSpecification")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PromptAttemptSpecification = PromptAttemptSpecification


@dataclass
class AllowedInputTypes(BaseModel):
    AllowAudioInput: Optional[bool]
    AllowDTMFInput: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AllowedInputTypes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowedInputTypes"]:
        if not json_data:
            return None
        return cls(
            AllowAudioInput=json_data.get("AllowAudioInput"),
            AllowDTMFInput=json_data.get("AllowDTMFInput"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowedInputTypes = AllowedInputTypes


@dataclass
class AudioAndDTMFInputSpecification(BaseModel):
    StartTimeoutMs: Optional[int]
    DTMFSpecification: Optional["_DTMFSpecification"]
    AudioSpecification: Optional["_AudioSpecification"]

    @classmethod
    def _deserialize(
        cls: Type["_AudioAndDTMFInputSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioAndDTMFInputSpecification"]:
        if not json_data:
            return None
        return cls(
            StartTimeoutMs=json_data.get("StartTimeoutMs"),
            DTMFSpecification=DTMFSpecification._deserialize(json_data.get("DTMFSpecification")),
            AudioSpecification=AudioSpecification._deserialize(json_data.get("AudioSpecification")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioAndDTMFInputSpecification = AudioAndDTMFInputSpecification


@dataclass
class DTMFSpecification(BaseModel):
    DeletionCharacter: Optional[str]
    EndCharacter: Optional[str]
    EndTimeoutMs: Optional[int]
    MaxLength: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_DTMFSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DTMFSpecification"]:
        if not json_data:
            return None
        return cls(
            DeletionCharacter=json_data.get("DeletionCharacter"),
            EndCharacter=json_data.get("EndCharacter"),
            EndTimeoutMs=json_data.get("EndTimeoutMs"),
            MaxLength=json_data.get("MaxLength"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DTMFSpecification = DTMFSpecification


@dataclass
class AudioSpecification(BaseModel):
    EndTimeoutMs: Optional[int]
    MaxLengthMs: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AudioSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioSpecification"]:
        if not json_data:
            return None
        return cls(
            EndTimeoutMs=json_data.get("EndTimeoutMs"),
            MaxLengthMs=json_data.get("MaxLengthMs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioSpecification = AudioSpecification


@dataclass
class TextInputSpecification(BaseModel):
    StartTimeoutMs: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_TextInputSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TextInputSpecification"]:
        if not json_data:
            return None
        return cls(
            StartTimeoutMs=json_data.get("StartTimeoutMs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TextInputSpecification = TextInputSpecification


@dataclass
class DialogCodeHookInvocationSetting(BaseModel):
    EnableCodeHookInvocation: Optional[bool]
    IsActive: Optional[bool]
    InvocationLabel: Optional[str]
    PostCodeHookSpecification: Optional["_PostDialogCodeHookInvocationSpecification"]

    @classmethod
    def _deserialize(
        cls: Type["_DialogCodeHookInvocationSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DialogCodeHookInvocationSetting"]:
        if not json_data:
            return None
        return cls(
            EnableCodeHookInvocation=json_data.get("EnableCodeHookInvocation"),
            IsActive=json_data.get("IsActive"),
            InvocationLabel=json_data.get("InvocationLabel"),
            PostCodeHookSpecification=PostDialogCodeHookInvocationSpecification._deserialize(json_data.get("PostCodeHookSpecification")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DialogCodeHookInvocationSetting = DialogCodeHookInvocationSetting


@dataclass
class PostDialogCodeHookInvocationSpecification(BaseModel):
    SuccessResponse: Optional["_ResponseSpecification"]
    SuccessNextStep: Optional["_DialogState"]
    SuccessConditional: Optional["_ConditionalSpecification"]
    FailureResponse: Optional["_ResponseSpecification"]
    FailureNextStep: Optional["_DialogState"]
    FailureConditional: Optional["_ConditionalSpecification"]
    TimeoutResponse: Optional["_ResponseSpecification"]
    TimeoutNextStep: Optional["_DialogState"]
    TimeoutConditional: Optional["_ConditionalSpecification"]

    @classmethod
    def _deserialize(
        cls: Type["_PostDialogCodeHookInvocationSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PostDialogCodeHookInvocationSpecification"]:
        if not json_data:
            return None
        return cls(
            SuccessResponse=ResponseSpecification._deserialize(json_data.get("SuccessResponse")),
            SuccessNextStep=DialogState._deserialize(json_data.get("SuccessNextStep")),
            SuccessConditional=ConditionalSpecification._deserialize(json_data.get("SuccessConditional")),
            FailureResponse=ResponseSpecification._deserialize(json_data.get("FailureResponse")),
            FailureNextStep=DialogState._deserialize(json_data.get("FailureNextStep")),
            FailureConditional=ConditionalSpecification._deserialize(json_data.get("FailureConditional")),
            TimeoutResponse=ResponseSpecification._deserialize(json_data.get("TimeoutResponse")),
            TimeoutNextStep=DialogState._deserialize(json_data.get("TimeoutNextStep")),
            TimeoutConditional=ConditionalSpecification._deserialize(json_data.get("TimeoutConditional")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PostDialogCodeHookInvocationSpecification = PostDialogCodeHookInvocationSpecification


@dataclass
class ElicitationCodeHookInvocationSetting(BaseModel):
    EnableCodeHookInvocation: Optional[bool]
    InvocationLabel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElicitationCodeHookInvocationSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElicitationCodeHookInvocationSetting"]:
        if not json_data:
            return None
        return cls(
            EnableCodeHookInvocation=json_data.get("EnableCodeHookInvocation"),
            InvocationLabel=json_data.get("InvocationLabel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElicitationCodeHookInvocationSetting = ElicitationCodeHookInvocationSetting


@dataclass
class IntentClosingSetting(BaseModel):
    ClosingResponse: Optional["_ResponseSpecification"]
    IsActive: Optional[bool]
    Conditional: Optional["_ConditionalSpecification"]
    NextStep: Optional["_DialogState"]

    @classmethod
    def _deserialize(
        cls: Type["_IntentClosingSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntentClosingSetting"]:
        if not json_data:
            return None
        return cls(
            ClosingResponse=ResponseSpecification._deserialize(json_data.get("ClosingResponse")),
            IsActive=json_data.get("IsActive"),
            Conditional=ConditionalSpecification._deserialize(json_data.get("Conditional")),
            NextStep=DialogState._deserialize(json_data.get("NextStep")),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntentClosingSetting = IntentClosingSetting


@dataclass
class InitialResponseSetting(BaseModel):
    InitialResponse: Optional["_ResponseSpecification"]
    NextStep: Optional["_DialogState"]
    Conditional: Optional["_ConditionalSpecification"]
    CodeHook: Optional["_DialogCodeHookInvocationSetting"]

    @classmethod
    def _deserialize(
        cls: Type["_InitialResponseSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitialResponseSetting"]:
        if not json_data:
            return None
        return cls(
            InitialResponse=ResponseSpecification._deserialize(json_data.get("InitialResponse")),
            NextStep=DialogState._deserialize(json_data.get("NextStep")),
            Conditional=ConditionalSpecification._deserialize(json_data.get("Conditional")),
            CodeHook=DialogCodeHookInvocationSetting._deserialize(json_data.get("CodeHook")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitialResponseSetting = InitialResponseSetting


@dataclass
class InputContext(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputContext"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputContext"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputContext = InputContext


@dataclass
class OutputContext(BaseModel):
    Name: Optional[str]
    TimeToLiveInSeconds: Optional[int]
    TurnsToLive: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_OutputContext"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputContext"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            TimeToLiveInSeconds=json_data.get("TimeToLiveInSeconds"),
            TurnsToLive=json_data.get("TurnsToLive"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputContext = OutputContext


@dataclass
class KendraConfiguration(BaseModel):
    KendraIndex: Optional[str]
    QueryFilterStringEnabled: Optional[bool]
    QueryFilterString: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KendraConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KendraConfiguration"]:
        if not json_data:
            return None
        return cls(
            KendraIndex=json_data.get("KendraIndex"),
            QueryFilterStringEnabled=json_data.get("QueryFilterStringEnabled"),
            QueryFilterString=json_data.get("QueryFilterString"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KendraConfiguration = KendraConfiguration


@dataclass
class SlotPriority(BaseModel):
    Priority: Optional[int]
    SlotName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SlotPriority"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlotPriority"]:
        if not json_data:
            return None
        return cls(
            Priority=json_data.get("Priority"),
            SlotName=json_data.get("SlotName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlotPriority = SlotPriority


@dataclass
class Slot(BaseModel):
    Name: Optional[str]
    Description: Optional[str]
    SlotTypeName: Optional[str]
    ValueElicitationSetting: Optional["_SlotValueElicitationSetting"]
    ObfuscationSetting: Optional["_ObfuscationSetting"]
    MultipleValuesSetting: Optional["_MultipleValuesSetting"]

    @classmethod
    def _deserialize(
        cls: Type["_Slot"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Slot"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            SlotTypeName=json_data.get("SlotTypeName"),
            ValueElicitationSetting=SlotValueElicitationSetting._deserialize(json_data.get("ValueElicitationSetting")),
            ObfuscationSetting=ObfuscationSetting._deserialize(json_data.get("ObfuscationSetting")),
            MultipleValuesSetting=MultipleValuesSetting._deserialize(json_data.get("MultipleValuesSetting")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Slot = Slot


@dataclass
class SlotValueElicitationSetting(BaseModel):
    DefaultValueSpecification: Optional["_SlotDefaultValueSpecification"]
    SlotConstraint: Optional[str]
    PromptSpecification: Optional["_PromptSpecification"]
    SampleUtterances: Optional[Sequence["_SampleUtterance"]]
    WaitAndContinueSpecification: Optional["_WaitAndContinueSpecification"]
    SlotCaptureSetting: Optional["_SlotCaptureSetting"]

    @classmethod
    def _deserialize(
        cls: Type["_SlotValueElicitationSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlotValueElicitationSetting"]:
        if not json_data:
            return None
        return cls(
            DefaultValueSpecification=SlotDefaultValueSpecification._deserialize(json_data.get("DefaultValueSpecification")),
            SlotConstraint=json_data.get("SlotConstraint"),
            PromptSpecification=PromptSpecification._deserialize(json_data.get("PromptSpecification")),
            SampleUtterances=deserialize_list(json_data.get("SampleUtterances"), SampleUtterance),
            WaitAndContinueSpecification=WaitAndContinueSpecification._deserialize(json_data.get("WaitAndContinueSpecification")),
            SlotCaptureSetting=SlotCaptureSetting._deserialize(json_data.get("SlotCaptureSetting")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlotValueElicitationSetting = SlotValueElicitationSetting


@dataclass
class SlotDefaultValueSpecification(BaseModel):
    DefaultValueList: Optional[Sequence["_SlotDefaultValue"]]

    @classmethod
    def _deserialize(
        cls: Type["_SlotDefaultValueSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlotDefaultValueSpecification"]:
        if not json_data:
            return None
        return cls(
            DefaultValueList=deserialize_list(json_data.get("DefaultValueList"), SlotDefaultValue),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlotDefaultValueSpecification = SlotDefaultValueSpecification


@dataclass
class SlotDefaultValue(BaseModel):
    DefaultValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SlotDefaultValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlotDefaultValue"]:
        if not json_data:
            return None
        return cls(
            DefaultValue=json_data.get("DefaultValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlotDefaultValue = SlotDefaultValue


@dataclass
class WaitAndContinueSpecification(BaseModel):
    WaitingResponse: Optional["_ResponseSpecification"]
    ContinueResponse: Optional["_ResponseSpecification"]
    StillWaitingResponse: Optional["_StillWaitingResponseSpecification"]
    IsActive: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_WaitAndContinueSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WaitAndContinueSpecification"]:
        if not json_data:
            return None
        return cls(
            WaitingResponse=ResponseSpecification._deserialize(json_data.get("WaitingResponse")),
            ContinueResponse=ResponseSpecification._deserialize(json_data.get("ContinueResponse")),
            StillWaitingResponse=StillWaitingResponseSpecification._deserialize(json_data.get("StillWaitingResponse")),
            IsActive=json_data.get("IsActive"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WaitAndContinueSpecification = WaitAndContinueSpecification


@dataclass
class StillWaitingResponseSpecification(BaseModel):
    MessageGroupsList: Optional[Sequence["_MessageGroup"]]
    FrequencyInSeconds: Optional[int]
    TimeoutInSeconds: Optional[int]
    AllowInterrupt: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_StillWaitingResponseSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StillWaitingResponseSpecification"]:
        if not json_data:
            return None
        return cls(
            MessageGroupsList=deserialize_list(json_data.get("MessageGroupsList"), MessageGroup),
            FrequencyInSeconds=json_data.get("FrequencyInSeconds"),
            TimeoutInSeconds=json_data.get("TimeoutInSeconds"),
            AllowInterrupt=json_data.get("AllowInterrupt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StillWaitingResponseSpecification = StillWaitingResponseSpecification


@dataclass
class SlotCaptureSetting(BaseModel):
    CaptureResponse: Optional["_ResponseSpecification"]
    CaptureNextStep: Optional["_DialogState"]
    CaptureConditional: Optional["_ConditionalSpecification"]
    FailureResponse: Optional["_ResponseSpecification"]
    FailureNextStep: Optional["_DialogState"]
    FailureConditional: Optional["_ConditionalSpecification"]
    CodeHook: Optional["_DialogCodeHookInvocationSetting"]
    ElicitationCodeHook: Optional["_ElicitationCodeHookInvocationSetting"]

    @classmethod
    def _deserialize(
        cls: Type["_SlotCaptureSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlotCaptureSetting"]:
        if not json_data:
            return None
        return cls(
            CaptureResponse=ResponseSpecification._deserialize(json_data.get("CaptureResponse")),
            CaptureNextStep=DialogState._deserialize(json_data.get("CaptureNextStep")),
            CaptureConditional=ConditionalSpecification._deserialize(json_data.get("CaptureConditional")),
            FailureResponse=ResponseSpecification._deserialize(json_data.get("FailureResponse")),
            FailureNextStep=DialogState._deserialize(json_data.get("FailureNextStep")),
            FailureConditional=ConditionalSpecification._deserialize(json_data.get("FailureConditional")),
            CodeHook=DialogCodeHookInvocationSetting._deserialize(json_data.get("CodeHook")),
            ElicitationCodeHook=ElicitationCodeHookInvocationSetting._deserialize(json_data.get("ElicitationCodeHook")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlotCaptureSetting = SlotCaptureSetting


@dataclass
class ObfuscationSetting(BaseModel):
    ObfuscationSettingType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ObfuscationSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObfuscationSetting"]:
        if not json_data:
            return None
        return cls(
            ObfuscationSettingType=json_data.get("ObfuscationSettingType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObfuscationSetting = ObfuscationSetting


@dataclass
class MultipleValuesSetting(BaseModel):
    AllowMultipleValues: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_MultipleValuesSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MultipleValuesSetting"]:
        if not json_data:
            return None
        return cls(
            AllowMultipleValues=json_data.get("AllowMultipleValues"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MultipleValuesSetting = MultipleValuesSetting


@dataclass
class SlotType(BaseModel):
    Name: Optional[str]
    Description: Optional[str]
    ParentSlotTypeSignature: Optional[str]
    SlotTypeValues: Optional[Sequence["_SlotTypeValue"]]
    ValueSelectionSetting: Optional["_SlotValueSelectionSetting"]
    ExternalSourceSetting: Optional["_ExternalSourceSetting"]

    @classmethod
    def _deserialize(
        cls: Type["_SlotType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlotType"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            ParentSlotTypeSignature=json_data.get("ParentSlotTypeSignature"),
            SlotTypeValues=deserialize_list(json_data.get("SlotTypeValues"), SlotTypeValue),
            ValueSelectionSetting=SlotValueSelectionSetting._deserialize(json_data.get("ValueSelectionSetting")),
            ExternalSourceSetting=ExternalSourceSetting._deserialize(json_data.get("ExternalSourceSetting")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlotType = SlotType


@dataclass
class SlotTypeValue(BaseModel):
    SampleValue: Optional["_SampleValue"]
    Synonyms: Optional[Sequence["_SampleValue"]]

    @classmethod
    def _deserialize(
        cls: Type["_SlotTypeValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlotTypeValue"]:
        if not json_data:
            return None
        return cls(
            SampleValue=SampleValue._deserialize(json_data.get("SampleValue")),
            Synonyms=deserialize_list(json_data.get("Synonyms"), SampleValue),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlotTypeValue = SlotTypeValue


@dataclass
class SampleValue(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SampleValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SampleValue"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SampleValue = SampleValue


@dataclass
class SlotValueSelectionSetting(BaseModel):
    ResolutionStrategy: Optional[str]
    RegexFilter: Optional["_SlotValueRegexFilter"]
    AdvancedRecognitionSetting: Optional["_AdvancedRecognitionSetting"]

    @classmethod
    def _deserialize(
        cls: Type["_SlotValueSelectionSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlotValueSelectionSetting"]:
        if not json_data:
            return None
        return cls(
            ResolutionStrategy=json_data.get("ResolutionStrategy"),
            RegexFilter=SlotValueRegexFilter._deserialize(json_data.get("RegexFilter")),
            AdvancedRecognitionSetting=AdvancedRecognitionSetting._deserialize(json_data.get("AdvancedRecognitionSetting")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlotValueSelectionSetting = SlotValueSelectionSetting


@dataclass
class SlotValueRegexFilter(BaseModel):
    Pattern: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SlotValueRegexFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlotValueRegexFilter"]:
        if not json_data:
            return None
        return cls(
            Pattern=json_data.get("Pattern"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlotValueRegexFilter = SlotValueRegexFilter


@dataclass
class AdvancedRecognitionSetting(BaseModel):
    AudioRecognitionStrategy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedRecognitionSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedRecognitionSetting"]:
        if not json_data:
            return None
        return cls(
            AudioRecognitionStrategy=json_data.get("AudioRecognitionStrategy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedRecognitionSetting = AdvancedRecognitionSetting


@dataclass
class ExternalSourceSetting(BaseModel):
    GrammarSlotTypeSetting: Optional["_GrammarSlotTypeSetting"]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalSourceSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalSourceSetting"]:
        if not json_data:
            return None
        return cls(
            GrammarSlotTypeSetting=GrammarSlotTypeSetting._deserialize(json_data.get("GrammarSlotTypeSetting")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalSourceSetting = ExternalSourceSetting


@dataclass
class GrammarSlotTypeSetting(BaseModel):
    Source: Optional["_GrammarSlotTypeSource"]

    @classmethod
    def _deserialize(
        cls: Type["_GrammarSlotTypeSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrammarSlotTypeSetting"]:
        if not json_data:
            return None
        return cls(
            Source=GrammarSlotTypeSource._deserialize(json_data.get("Source")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrammarSlotTypeSetting = GrammarSlotTypeSetting


@dataclass
class GrammarSlotTypeSource(BaseModel):
    S3BucketName: Optional[str]
    S3ObjectKey: Optional[str]
    KmsKeyArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GrammarSlotTypeSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrammarSlotTypeSource"]:
        if not json_data:
            return None
        return cls(
            S3BucketName=json_data.get("S3BucketName"),
            S3ObjectKey=json_data.get("S3ObjectKey"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrammarSlotTypeSource = GrammarSlotTypeSource


@dataclass
class CustomVocabulary(BaseModel):
    CustomVocabularyItems: Optional[AbstractSet["_CustomVocabularyItem"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomVocabulary"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomVocabulary"]:
        if not json_data:
            return None
        return cls(
            CustomVocabularyItems=set_or_none(json_data.get("CustomVocabularyItems")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomVocabulary = CustomVocabulary


@dataclass
class CustomVocabularyItem(BaseModel):
    Phrase: Optional[str]
    Weight: Optional[int]
    DisplayAs: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomVocabularyItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomVocabularyItem"]:
        if not json_data:
            return None
        return cls(
            Phrase=json_data.get("Phrase"),
            Weight=json_data.get("Weight"),
            DisplayAs=json_data.get("DisplayAs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomVocabularyItem = CustomVocabularyItem


@dataclass
class S3Location(BaseModel):
    S3Bucket: Optional[str]
    S3ObjectKey: Optional[str]
    S3ObjectVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Location"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Location"]:
        if not json_data:
            return None
        return cls(
            S3Bucket=json_data.get("S3Bucket"),
            S3ObjectKey=json_data.get("S3ObjectKey"),
            S3ObjectVersion=json_data.get("S3ObjectVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Location = S3Location


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
class TestBotAliasSettings(BaseModel):
    BotAliasLocaleSettings: Optional[AbstractSet["_BotAliasLocaleSettingsItem"]]
    ConversationLogSettings: Optional["_ConversationLogSettings"]
    Description: Optional[str]
    SentimentAnalysisSettings: Optional["_SentimentAnalysisSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_TestBotAliasSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TestBotAliasSettings"]:
        if not json_data:
            return None
        return cls(
            BotAliasLocaleSettings=set_or_none(json_data.get("BotAliasLocaleSettings")),
            ConversationLogSettings=ConversationLogSettings._deserialize(json_data.get("ConversationLogSettings")),
            Description=json_data.get("Description"),
            SentimentAnalysisSettings=SentimentAnalysisSettings._deserialize(json_data.get("SentimentAnalysisSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TestBotAliasSettings = TestBotAliasSettings


@dataclass
class BotAliasLocaleSettingsItem(BaseModel):
    LocaleId: Optional[str]
    BotAliasLocaleSetting: Optional["_BotAliasLocaleSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_BotAliasLocaleSettingsItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BotAliasLocaleSettingsItem"]:
        if not json_data:
            return None
        return cls(
            LocaleId=json_data.get("LocaleId"),
            BotAliasLocaleSetting=BotAliasLocaleSettings._deserialize(json_data.get("BotAliasLocaleSetting")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BotAliasLocaleSettingsItem = BotAliasLocaleSettingsItem


@dataclass
class BotAliasLocaleSettings(BaseModel):
    CodeHookSpecification: Optional["_CodeHookSpecification"]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_BotAliasLocaleSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BotAliasLocaleSettings"]:
        if not json_data:
            return None
        return cls(
            CodeHookSpecification=CodeHookSpecification._deserialize(json_data.get("CodeHookSpecification")),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BotAliasLocaleSettings = BotAliasLocaleSettings


@dataclass
class CodeHookSpecification(BaseModel):
    LambdaCodeHook: Optional["_LambdaCodeHook"]

    @classmethod
    def _deserialize(
        cls: Type["_CodeHookSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CodeHookSpecification"]:
        if not json_data:
            return None
        return cls(
            LambdaCodeHook=LambdaCodeHook._deserialize(json_data.get("LambdaCodeHook")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CodeHookSpecification = CodeHookSpecification


@dataclass
class LambdaCodeHook(BaseModel):
    CodeHookInterfaceVersion: Optional[str]
    LambdaArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaCodeHook"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaCodeHook"]:
        if not json_data:
            return None
        return cls(
            CodeHookInterfaceVersion=json_data.get("CodeHookInterfaceVersion"),
            LambdaArn=json_data.get("LambdaArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaCodeHook = LambdaCodeHook


@dataclass
class ConversationLogSettings(BaseModel):
    AudioLogSettings: Optional[AbstractSet["_AudioLogSetting"]]
    TextLogSettings: Optional[AbstractSet["_TextLogSetting"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConversationLogSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConversationLogSettings"]:
        if not json_data:
            return None
        return cls(
            AudioLogSettings=set_or_none(json_data.get("AudioLogSettings")),
            TextLogSettings=set_or_none(json_data.get("TextLogSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConversationLogSettings = ConversationLogSettings


@dataclass
class AudioLogSetting(BaseModel):
    Destination: Optional["_AudioLogDestination"]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AudioLogSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioLogSetting"]:
        if not json_data:
            return None
        return cls(
            Destination=AudioLogDestination._deserialize(json_data.get("Destination")),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioLogSetting = AudioLogSetting


@dataclass
class AudioLogDestination(BaseModel):
    S3Bucket: Optional["_S3BucketLogDestination"]

    @classmethod
    def _deserialize(
        cls: Type["_AudioLogDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AudioLogDestination"]:
        if not json_data:
            return None
        return cls(
            S3Bucket=S3BucketLogDestination._deserialize(json_data.get("S3Bucket")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AudioLogDestination = AudioLogDestination


@dataclass
class S3BucketLogDestination(BaseModel):
    S3BucketArn: Optional[str]
    LogPrefix: Optional[str]
    KmsKeyArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3BucketLogDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3BucketLogDestination"]:
        if not json_data:
            return None
        return cls(
            S3BucketArn=json_data.get("S3BucketArn"),
            LogPrefix=json_data.get("LogPrefix"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3BucketLogDestination = S3BucketLogDestination


@dataclass
class TextLogSetting(BaseModel):
    Destination: Optional["_TextLogDestination"]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TextLogSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TextLogSetting"]:
        if not json_data:
            return None
        return cls(
            Destination=TextLogDestination._deserialize(json_data.get("Destination")),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TextLogSetting = TextLogSetting


@dataclass
class TextLogDestination(BaseModel):
    CloudWatch: Optional["_CloudWatchLogGroupLogDestination"]

    @classmethod
    def _deserialize(
        cls: Type["_TextLogDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TextLogDestination"]:
        if not json_data:
            return None
        return cls(
            CloudWatch=CloudWatchLogGroupLogDestination._deserialize(json_data.get("CloudWatch")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TextLogDestination = TextLogDestination


@dataclass
class CloudWatchLogGroupLogDestination(BaseModel):
    CloudWatchLogGroupArn: Optional[str]
    LogPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudWatchLogGroupLogDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudWatchLogGroupLogDestination"]:
        if not json_data:
            return None
        return cls(
            CloudWatchLogGroupArn=json_data.get("CloudWatchLogGroupArn"),
            LogPrefix=json_data.get("LogPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudWatchLogGroupLogDestination = CloudWatchLogGroupLogDestination


@dataclass
class SentimentAnalysisSettings(BaseModel):
    DetectSentiment: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SentimentAnalysisSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SentimentAnalysisSettings"]:
        if not json_data:
            return None
        return cls(
            DetectSentiment=json_data.get("DetectSentiment"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SentimentAnalysisSettings = SentimentAnalysisSettings


