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
class AwsIoteventsAlarmmodel(BaseModel):
    AlarmModelName: Optional[str]
    AlarmModelDescription: Optional[str]
    RoleArn: Optional[str]
    Key: Optional[str]
    Severity: Optional[int]
    AlarmRule: Optional["_AlarmRule"]
    AlarmEventActions: Optional["_AlarmEventActions"]
    AlarmCapabilities: Optional["_AlarmCapabilities"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIoteventsAlarmmodel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIoteventsAlarmmodel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AlarmModelName=json_data.get("AlarmModelName"),
            AlarmModelDescription=json_data.get("AlarmModelDescription"),
            RoleArn=json_data.get("RoleArn"),
            Key=json_data.get("Key"),
            Severity=json_data.get("Severity"),
            AlarmRule=AlarmRule._deserialize(json_data.get("AlarmRule")),
            AlarmEventActions=AlarmEventActions._deserialize(json_data.get("AlarmEventActions")),
            AlarmCapabilities=AlarmCapabilities._deserialize(json_data.get("AlarmCapabilities")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIoteventsAlarmmodel = AwsIoteventsAlarmmodel


@dataclass
class AlarmRule(BaseModel):
    SimpleRule: Optional["_SimpleRule"]

    @classmethod
    def _deserialize(
        cls: Type["_AlarmRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlarmRule"]:
        if not json_data:
            return None
        return cls(
            SimpleRule=SimpleRule._deserialize(json_data.get("SimpleRule")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlarmRule = AlarmRule


@dataclass
class SimpleRule(BaseModel):
    InputProperty: Optional[str]
    ComparisonOperator: Optional[str]
    Threshold: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SimpleRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SimpleRule"]:
        if not json_data:
            return None
        return cls(
            InputProperty=json_data.get("InputProperty"),
            ComparisonOperator=json_data.get("ComparisonOperator"),
            Threshold=json_data.get("Threshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SimpleRule = SimpleRule


@dataclass
class AlarmEventActions(BaseModel):
    AlarmActions: Optional[Sequence["_AlarmAction"]]

    @classmethod
    def _deserialize(
        cls: Type["_AlarmEventActions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlarmEventActions"]:
        if not json_data:
            return None
        return cls(
            AlarmActions=deserialize_list(json_data.get("AlarmActions"), AlarmAction),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlarmEventActions = AlarmEventActions


@dataclass
class AlarmAction(BaseModel):
    DynamoDB: Optional["_DynamoDB"]
    DynamoDBv2: Optional["_DynamoDBv2"]
    Firehose: Optional["_Firehose"]
    IotEvents: Optional["_IotEvents"]
    IotSiteWise: Optional["_IotSiteWise"]
    IotTopicPublish: Optional["_IotTopicPublish"]
    Lambda: Optional["_Lambda"]
    Sns: Optional["_Sns"]
    Sqs: Optional["_Sqs"]

    @classmethod
    def _deserialize(
        cls: Type["_AlarmAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlarmAction"]:
        if not json_data:
            return None
        return cls(
            DynamoDB=DynamoDB._deserialize(json_data.get("DynamoDB")),
            DynamoDBv2=DynamoDBv2._deserialize(json_data.get("DynamoDBv2")),
            Firehose=Firehose._deserialize(json_data.get("Firehose")),
            IotEvents=IotEvents._deserialize(json_data.get("IotEvents")),
            IotSiteWise=IotSiteWise._deserialize(json_data.get("IotSiteWise")),
            IotTopicPublish=IotTopicPublish._deserialize(json_data.get("IotTopicPublish")),
            Lambda=Lambda._deserialize(json_data.get("Lambda")),
            Sns=Sns._deserialize(json_data.get("Sns")),
            Sqs=Sqs._deserialize(json_data.get("Sqs")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlarmAction = AlarmAction


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
class AlarmCapabilities(BaseModel):
    InitializationConfiguration: Optional["_InitializationConfiguration"]
    AcknowledgeFlow: Optional["_AcknowledgeFlow"]

    @classmethod
    def _deserialize(
        cls: Type["_AlarmCapabilities"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlarmCapabilities"]:
        if not json_data:
            return None
        return cls(
            InitializationConfiguration=InitializationConfiguration._deserialize(json_data.get("InitializationConfiguration")),
            AcknowledgeFlow=AcknowledgeFlow._deserialize(json_data.get("AcknowledgeFlow")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlarmCapabilities = AlarmCapabilities


@dataclass
class InitializationConfiguration(BaseModel):
    DisabledOnInitialization: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_InitializationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitializationConfiguration"]:
        if not json_data:
            return None
        return cls(
            DisabledOnInitialization=json_data.get("DisabledOnInitialization"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitializationConfiguration = InitializationConfiguration


@dataclass
class AcknowledgeFlow(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AcknowledgeFlow"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AcknowledgeFlow"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AcknowledgeFlow = AcknowledgeFlow


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


