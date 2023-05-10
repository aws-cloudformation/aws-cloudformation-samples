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
class AwsIoteventsDetectormodel(BaseModel):
    DetectorModelDefinition: Optional["_DetectorModelDefinition"]
    DetectorModelDescription: Optional[str]
    DetectorModelName: Optional[str]
    EvaluationMethod: Optional[str]
    Key: Optional[str]
    RoleArn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIoteventsDetectormodel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIoteventsDetectormodel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DetectorModelDefinition=DetectorModelDefinition._deserialize(json_data.get("DetectorModelDefinition")),
            DetectorModelDescription=json_data.get("DetectorModelDescription"),
            DetectorModelName=json_data.get("DetectorModelName"),
            EvaluationMethod=json_data.get("EvaluationMethod"),
            Key=json_data.get("Key"),
            RoleArn=json_data.get("RoleArn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIoteventsDetectormodel = AwsIoteventsDetectormodel


@dataclass
class DetectorModelDefinition(BaseModel):
    InitialStateName: Optional[str]
    States: Optional[Sequence["_State"]]

    @classmethod
    def _deserialize(
        cls: Type["_DetectorModelDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DetectorModelDefinition"]:
        if not json_data:
            return None
        return cls(
            InitialStateName=json_data.get("InitialStateName"),
            States=deserialize_list(json_data.get("States"), State),
        )


# work around possible type aliasing issues when variable has same name as a model
_DetectorModelDefinition = DetectorModelDefinition


@dataclass
class State(BaseModel):
    OnEnter: Optional["_OnEnter"]
    OnExit: Optional["_OnExit"]
    OnInput: Optional["_OnInput"]
    StateName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_State"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_State"]:
        if not json_data:
            return None
        return cls(
            OnEnter=OnEnter._deserialize(json_data.get("OnEnter")),
            OnExit=OnExit._deserialize(json_data.get("OnExit")),
            OnInput=OnInput._deserialize(json_data.get("OnInput")),
            StateName=json_data.get("StateName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_State = State


@dataclass
class OnEnter(BaseModel):
    Events: Optional[Sequence["_Event"]]

    @classmethod
    def _deserialize(
        cls: Type["_OnEnter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnEnter"]:
        if not json_data:
            return None
        return cls(
            Events=deserialize_list(json_data.get("Events"), Event),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnEnter = OnEnter


@dataclass
class Event(BaseModel):
    Actions: Optional[Sequence["_Action"]]
    Condition: Optional[str]
    EventName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Event"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Event"]:
        if not json_data:
            return None
        return cls(
            Actions=deserialize_list(json_data.get("Actions"), Action),
            Condition=json_data.get("Condition"),
            EventName=json_data.get("EventName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Event = Event


@dataclass
class Action(BaseModel):
    ClearTimer: Optional["_ClearTimer"]
    DynamoDB: Optional["_DynamoDB"]
    DynamoDBv2: Optional["_DynamoDBv2"]
    Firehose: Optional["_Firehose"]
    IotEvents: Optional["_IotEvents"]
    IotSiteWise: Optional["_IotSiteWise"]
    IotTopicPublish: Optional["_IotTopicPublish"]
    Lambda: Optional["_Lambda"]
    ResetTimer: Optional["_ResetTimer"]
    SetTimer: Optional["_SetTimer"]
    SetVariable: Optional["_SetVariable"]
    Sns: Optional["_Sns"]
    Sqs: Optional["_Sqs"]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            ClearTimer=ClearTimer._deserialize(json_data.get("ClearTimer")),
            DynamoDB=DynamoDB._deserialize(json_data.get("DynamoDB")),
            DynamoDBv2=DynamoDBv2._deserialize(json_data.get("DynamoDBv2")),
            Firehose=Firehose._deserialize(json_data.get("Firehose")),
            IotEvents=IotEvents._deserialize(json_data.get("IotEvents")),
            IotSiteWise=IotSiteWise._deserialize(json_data.get("IotSiteWise")),
            IotTopicPublish=IotTopicPublish._deserialize(json_data.get("IotTopicPublish")),
            Lambda=Lambda._deserialize(json_data.get("Lambda")),
            ResetTimer=ResetTimer._deserialize(json_data.get("ResetTimer")),
            SetTimer=SetTimer._deserialize(json_data.get("SetTimer")),
            SetVariable=SetVariable._deserialize(json_data.get("SetVariable")),
            Sns=Sns._deserialize(json_data.get("Sns")),
            Sqs=Sqs._deserialize(json_data.get("Sqs")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class ClearTimer(BaseModel):
    TimerName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClearTimer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClearTimer"]:
        if not json_data:
            return None
        return cls(
            TimerName=json_data.get("TimerName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClearTimer = ClearTimer


@dataclass
class DynamoDB(BaseModel):
    HashKeyField: Optional[str]
    HashKeyType: Optional[str]
    HashKeyValue: Optional[str]
    Operation: Optional[str]
    Payload: Optional["_Payload"]
    PayloadField: Optional[str]
    RangeKeyField: Optional[str]
    RangeKeyType: Optional[str]
    RangeKeyValue: Optional[str]
    TableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DynamoDB"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamoDB"]:
        if not json_data:
            return None
        return cls(
            HashKeyField=json_data.get("HashKeyField"),
            HashKeyType=json_data.get("HashKeyType"),
            HashKeyValue=json_data.get("HashKeyValue"),
            Operation=json_data.get("Operation"),
            Payload=Payload._deserialize(json_data.get("Payload")),
            PayloadField=json_data.get("PayloadField"),
            RangeKeyField=json_data.get("RangeKeyField"),
            RangeKeyType=json_data.get("RangeKeyType"),
            RangeKeyValue=json_data.get("RangeKeyValue"),
            TableName=json_data.get("TableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamoDB = DynamoDB


@dataclass
class Payload(BaseModel):
    ContentExpression: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Payload"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Payload"]:
        if not json_data:
            return None
        return cls(
            ContentExpression=json_data.get("ContentExpression"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Payload = Payload


@dataclass
class DynamoDBv2(BaseModel):
    Payload: Optional["_Payload"]
    TableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DynamoDBv2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamoDBv2"]:
        if not json_data:
            return None
        return cls(
            Payload=Payload._deserialize(json_data.get("Payload")),
            TableName=json_data.get("TableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamoDBv2 = DynamoDBv2


@dataclass
class Firehose(BaseModel):
    DeliveryStreamName: Optional[str]
    Payload: Optional["_Payload"]
    Separator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Firehose"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Firehose"]:
        if not json_data:
            return None
        return cls(
            DeliveryStreamName=json_data.get("DeliveryStreamName"),
            Payload=Payload._deserialize(json_data.get("Payload")),
            Separator=json_data.get("Separator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Firehose = Firehose


@dataclass
class IotEvents(BaseModel):
    InputName: Optional[str]
    Payload: Optional["_Payload"]

    @classmethod
    def _deserialize(
        cls: Type["_IotEvents"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IotEvents"]:
        if not json_data:
            return None
        return cls(
            InputName=json_data.get("InputName"),
            Payload=Payload._deserialize(json_data.get("Payload")),
        )


# work around possible type aliasing issues when variable has same name as a model
_IotEvents = IotEvents


@dataclass
class IotSiteWise(BaseModel):
    AssetId: Optional[str]
    EntryId: Optional[str]
    PropertyAlias: Optional[str]
    PropertyId: Optional[str]
    PropertyValue: Optional["_AssetPropertyValue"]

    @classmethod
    def _deserialize(
        cls: Type["_IotSiteWise"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IotSiteWise"]:
        if not json_data:
            return None
        return cls(
            AssetId=json_data.get("AssetId"),
            EntryId=json_data.get("EntryId"),
            PropertyAlias=json_data.get("PropertyAlias"),
            PropertyId=json_data.get("PropertyId"),
            PropertyValue=AssetPropertyValue._deserialize(json_data.get("PropertyValue")),
        )


# work around possible type aliasing issues when variable has same name as a model
_IotSiteWise = IotSiteWise


@dataclass
class AssetPropertyValue(BaseModel):
    Quality: Optional[str]
    Timestamp: Optional["_AssetPropertyTimestamp"]
    Value: Optional["_AssetPropertyVariant"]

    @classmethod
    def _deserialize(
        cls: Type["_AssetPropertyValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssetPropertyValue"]:
        if not json_data:
            return None
        return cls(
            Quality=json_data.get("Quality"),
            Timestamp=AssetPropertyTimestamp._deserialize(json_data.get("Timestamp")),
            Value=AssetPropertyVariant._deserialize(json_data.get("Value")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssetPropertyValue = AssetPropertyValue


@dataclass
class AssetPropertyTimestamp(BaseModel):
    OffsetInNanos: Optional[str]
    TimeInSeconds: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssetPropertyTimestamp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssetPropertyTimestamp"]:
        if not json_data:
            return None
        return cls(
            OffsetInNanos=json_data.get("OffsetInNanos"),
            TimeInSeconds=json_data.get("TimeInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssetPropertyTimestamp = AssetPropertyTimestamp


@dataclass
class AssetPropertyVariant(BaseModel):
    BooleanValue: Optional[str]
    DoubleValue: Optional[str]
    IntegerValue: Optional[str]
    StringValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssetPropertyVariant"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssetPropertyVariant"]:
        if not json_data:
            return None
        return cls(
            BooleanValue=json_data.get("BooleanValue"),
            DoubleValue=json_data.get("DoubleValue"),
            IntegerValue=json_data.get("IntegerValue"),
            StringValue=json_data.get("StringValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssetPropertyVariant = AssetPropertyVariant


@dataclass
class IotTopicPublish(BaseModel):
    MqttTopic: Optional[str]
    Payload: Optional["_Payload"]

    @classmethod
    def _deserialize(
        cls: Type["_IotTopicPublish"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IotTopicPublish"]:
        if not json_data:
            return None
        return cls(
            MqttTopic=json_data.get("MqttTopic"),
            Payload=Payload._deserialize(json_data.get("Payload")),
        )


# work around possible type aliasing issues when variable has same name as a model
_IotTopicPublish = IotTopicPublish


@dataclass
class Lambda(BaseModel):
    FunctionArn: Optional[str]
    Payload: Optional["_Payload"]

    @classmethod
    def _deserialize(
        cls: Type["_Lambda"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Lambda"]:
        if not json_data:
            return None
        return cls(
            FunctionArn=json_data.get("FunctionArn"),
            Payload=Payload._deserialize(json_data.get("Payload")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Lambda = Lambda


@dataclass
class ResetTimer(BaseModel):
    TimerName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResetTimer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResetTimer"]:
        if not json_data:
            return None
        return cls(
            TimerName=json_data.get("TimerName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResetTimer = ResetTimer


@dataclass
class SetTimer(BaseModel):
    DurationExpression: Optional[str]
    Seconds: Optional[int]
    TimerName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SetTimer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SetTimer"]:
        if not json_data:
            return None
        return cls(
            DurationExpression=json_data.get("DurationExpression"),
            Seconds=json_data.get("Seconds"),
            TimerName=json_data.get("TimerName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SetTimer = SetTimer


@dataclass
class SetVariable(BaseModel):
    Value: Optional[str]
    VariableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SetVariable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SetVariable"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            VariableName=json_data.get("VariableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SetVariable = SetVariable


@dataclass
class Sns(BaseModel):
    Payload: Optional["_Payload"]
    TargetArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Sns"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sns"]:
        if not json_data:
            return None
        return cls(
            Payload=Payload._deserialize(json_data.get("Payload")),
            TargetArn=json_data.get("TargetArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sns = Sns


@dataclass
class Sqs(BaseModel):
    Payload: Optional["_Payload"]
    QueueUrl: Optional[str]
    UseBase64: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Sqs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sqs"]:
        if not json_data:
            return None
        return cls(
            Payload=Payload._deserialize(json_data.get("Payload")),
            QueueUrl=json_data.get("QueueUrl"),
            UseBase64=json_data.get("UseBase64"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sqs = Sqs


@dataclass
class OnExit(BaseModel):
    Events: Optional[Sequence["_Event"]]

    @classmethod
    def _deserialize(
        cls: Type["_OnExit"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnExit"]:
        if not json_data:
            return None
        return cls(
            Events=deserialize_list(json_data.get("Events"), Event),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnExit = OnExit


@dataclass
class OnInput(BaseModel):
    Events: Optional[Sequence["_Event"]]
    TransitionEvents: Optional[Sequence["_TransitionEvent"]]

    @classmethod
    def _deserialize(
        cls: Type["_OnInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnInput"]:
        if not json_data:
            return None
        return cls(
            Events=deserialize_list(json_data.get("Events"), Event),
            TransitionEvents=deserialize_list(json_data.get("TransitionEvents"), TransitionEvent),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnInput = OnInput


@dataclass
class TransitionEvent(BaseModel):
    Actions: Optional[Sequence["_Action"]]
    Condition: Optional[str]
    EventName: Optional[str]
    NextState: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TransitionEvent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransitionEvent"]:
        if not json_data:
            return None
        return cls(
            Actions=deserialize_list(json_data.get("Actions"), Action),
            Condition=json_data.get("Condition"),
            EventName=json_data.get("EventName"),
            NextState=json_data.get("NextState"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransitionEvent = TransitionEvent


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


