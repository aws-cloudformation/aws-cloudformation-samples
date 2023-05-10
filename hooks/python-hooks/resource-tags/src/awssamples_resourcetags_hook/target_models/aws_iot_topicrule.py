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
class AwsIotTopicrule(BaseModel):
    Arn: Optional[str]
    RuleName: Optional[str]
    TopicRulePayload: Optional["_TopicRulePayload"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotTopicrule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotTopicrule"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            RuleName=json_data.get("RuleName"),
            TopicRulePayload=TopicRulePayload._deserialize(json_data.get("TopicRulePayload")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotTopicrule = AwsIotTopicrule


@dataclass
class TopicRulePayload(BaseModel):
    RuleDisabled: Optional[bool]
    ErrorAction: Optional["_Action"]
    Description: Optional[str]
    AwsIotSqlVersion: Optional[str]
    Actions: Optional[Sequence["_Action"]]
    Sql: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TopicRulePayload"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopicRulePayload"]:
        if not json_data:
            return None
        return cls(
            RuleDisabled=json_data.get("RuleDisabled"),
            ErrorAction=Action._deserialize(json_data.get("ErrorAction")),
            Description=json_data.get("Description"),
            AwsIotSqlVersion=json_data.get("AwsIotSqlVersion"),
            Actions=deserialize_list(json_data.get("Actions"), Action),
            Sql=json_data.get("Sql"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopicRulePayload = TopicRulePayload


@dataclass
class Action(BaseModel):
    S3: Optional["_S3Action"]
    CloudwatchAlarm: Optional["_CloudwatchAlarmAction"]
    CloudwatchLogs: Optional["_CloudwatchLogsAction"]
    IotEvents: Optional["_IotEventsAction"]
    Firehose: Optional["_FirehoseAction"]
    Republish: Optional["_RepublishAction"]
    StepFunctions: Optional["_StepFunctionsAction"]
    DynamoDB: Optional["_DynamoDBAction"]
    Http: Optional["_HttpAction"]
    DynamoDBv2: Optional["_DynamoDBv2Action"]
    CloudwatchMetric: Optional["_CloudwatchMetricAction"]
    IotSiteWise: Optional["_IotSiteWiseAction"]
    Elasticsearch: Optional["_ElasticsearchAction"]
    Sqs: Optional["_SqsAction"]
    Kinesis: Optional["_KinesisAction"]
    IotAnalytics: Optional["_IotAnalyticsAction"]
    Sns: Optional["_SnsAction"]
    Lambda: Optional["_LambdaAction"]
    Timestream: Optional["_TimestreamAction"]
    Kafka: Optional["_KafkaAction"]
    OpenSearch: Optional["_OpenSearchAction"]
    Location: Optional["_LocationAction"]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            S3=S3Action._deserialize(json_data.get("S3")),
            CloudwatchAlarm=CloudwatchAlarmAction._deserialize(json_data.get("CloudwatchAlarm")),
            CloudwatchLogs=CloudwatchLogsAction._deserialize(json_data.get("CloudwatchLogs")),
            IotEvents=IotEventsAction._deserialize(json_data.get("IotEvents")),
            Firehose=FirehoseAction._deserialize(json_data.get("Firehose")),
            Republish=RepublishAction._deserialize(json_data.get("Republish")),
            StepFunctions=StepFunctionsAction._deserialize(json_data.get("StepFunctions")),
            DynamoDB=DynamoDBAction._deserialize(json_data.get("DynamoDB")),
            Http=HttpAction._deserialize(json_data.get("Http")),
            DynamoDBv2=DynamoDBv2Action._deserialize(json_data.get("DynamoDBv2")),
            CloudwatchMetric=CloudwatchMetricAction._deserialize(json_data.get("CloudwatchMetric")),
            IotSiteWise=IotSiteWiseAction._deserialize(json_data.get("IotSiteWise")),
            Elasticsearch=ElasticsearchAction._deserialize(json_data.get("Elasticsearch")),
            Sqs=SqsAction._deserialize(json_data.get("Sqs")),
            Kinesis=KinesisAction._deserialize(json_data.get("Kinesis")),
            IotAnalytics=IotAnalyticsAction._deserialize(json_data.get("IotAnalytics")),
            Sns=SnsAction._deserialize(json_data.get("Sns")),
            Lambda=LambdaAction._deserialize(json_data.get("Lambda")),
            Timestream=TimestreamAction._deserialize(json_data.get("Timestream")),
            Kafka=KafkaAction._deserialize(json_data.get("Kafka")),
            OpenSearch=OpenSearchAction._deserialize(json_data.get("OpenSearch")),
            Location=LocationAction._deserialize(json_data.get("Location")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class S3Action(BaseModel):
    BucketName: Optional[str]
    Key: Optional[str]
    RoleArn: Optional[str]
    CannedAcl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Action"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            Key=json_data.get("Key"),
            RoleArn=json_data.get("RoleArn"),
            CannedAcl=json_data.get("CannedAcl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Action = S3Action


@dataclass
class CloudwatchAlarmAction(BaseModel):
    StateValue: Optional[str]
    AlarmName: Optional[str]
    StateReason: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchAlarmAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchAlarmAction"]:
        if not json_data:
            return None
        return cls(
            StateValue=json_data.get("StateValue"),
            AlarmName=json_data.get("AlarmName"),
            StateReason=json_data.get("StateReason"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchAlarmAction = CloudwatchAlarmAction


@dataclass
class CloudwatchLogsAction(BaseModel):
    LogGroupName: Optional[str]
    RoleArn: Optional[str]
    BatchMode: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchLogsAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchLogsAction"]:
        if not json_data:
            return None
        return cls(
            LogGroupName=json_data.get("LogGroupName"),
            RoleArn=json_data.get("RoleArn"),
            BatchMode=json_data.get("BatchMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchLogsAction = CloudwatchLogsAction


@dataclass
class IotEventsAction(BaseModel):
    InputName: Optional[str]
    RoleArn: Optional[str]
    MessageId: Optional[str]
    BatchMode: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_IotEventsAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IotEventsAction"]:
        if not json_data:
            return None
        return cls(
            InputName=json_data.get("InputName"),
            RoleArn=json_data.get("RoleArn"),
            MessageId=json_data.get("MessageId"),
            BatchMode=json_data.get("BatchMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IotEventsAction = IotEventsAction


@dataclass
class FirehoseAction(BaseModel):
    DeliveryStreamName: Optional[str]
    RoleArn: Optional[str]
    Separator: Optional[str]
    BatchMode: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_FirehoseAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FirehoseAction"]:
        if not json_data:
            return None
        return cls(
            DeliveryStreamName=json_data.get("DeliveryStreamName"),
            RoleArn=json_data.get("RoleArn"),
            Separator=json_data.get("Separator"),
            BatchMode=json_data.get("BatchMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FirehoseAction = FirehoseAction


@dataclass
class RepublishAction(BaseModel):
    Qos: Optional[int]
    Topic: Optional[str]
    RoleArn: Optional[str]
    Headers: Optional["_RepublishActionHeaders"]

    @classmethod
    def _deserialize(
        cls: Type["_RepublishAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RepublishAction"]:
        if not json_data:
            return None
        return cls(
            Qos=json_data.get("Qos"),
            Topic=json_data.get("Topic"),
            RoleArn=json_data.get("RoleArn"),
            Headers=RepublishActionHeaders._deserialize(json_data.get("Headers")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RepublishAction = RepublishAction


@dataclass
class RepublishActionHeaders(BaseModel):
    PayloadFormatIndicator: Optional[str]
    ContentType: Optional[str]
    ResponseTopic: Optional[str]
    CorrelationData: Optional[str]
    MessageExpiry: Optional[str]
    UserProperties: Optional[Sequence["_UserProperty"]]

    @classmethod
    def _deserialize(
        cls: Type["_RepublishActionHeaders"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RepublishActionHeaders"]:
        if not json_data:
            return None
        return cls(
            PayloadFormatIndicator=json_data.get("PayloadFormatIndicator"),
            ContentType=json_data.get("ContentType"),
            ResponseTopic=json_data.get("ResponseTopic"),
            CorrelationData=json_data.get("CorrelationData"),
            MessageExpiry=json_data.get("MessageExpiry"),
            UserProperties=deserialize_list(json_data.get("UserProperties"), UserProperty),
        )


# work around possible type aliasing issues when variable has same name as a model
_RepublishActionHeaders = RepublishActionHeaders


@dataclass
class UserProperty(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserProperty"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserProperty"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserProperty = UserProperty


@dataclass
class StepFunctionsAction(BaseModel):
    ExecutionNamePrefix: Optional[str]
    StateMachineName: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StepFunctionsAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepFunctionsAction"]:
        if not json_data:
            return None
        return cls(
            ExecutionNamePrefix=json_data.get("ExecutionNamePrefix"),
            StateMachineName=json_data.get("StateMachineName"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepFunctionsAction = StepFunctionsAction


@dataclass
class DynamoDBAction(BaseModel):
    TableName: Optional[str]
    PayloadField: Optional[str]
    RangeKeyField: Optional[str]
    HashKeyField: Optional[str]
    RangeKeyValue: Optional[str]
    RangeKeyType: Optional[str]
    HashKeyType: Optional[str]
    HashKeyValue: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DynamoDBAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamoDBAction"]:
        if not json_data:
            return None
        return cls(
            TableName=json_data.get("TableName"),
            PayloadField=json_data.get("PayloadField"),
            RangeKeyField=json_data.get("RangeKeyField"),
            HashKeyField=json_data.get("HashKeyField"),
            RangeKeyValue=json_data.get("RangeKeyValue"),
            RangeKeyType=json_data.get("RangeKeyType"),
            HashKeyType=json_data.get("HashKeyType"),
            HashKeyValue=json_data.get("HashKeyValue"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamoDBAction = DynamoDBAction


@dataclass
class HttpAction(BaseModel):
    ConfirmationUrl: Optional[str]
    Headers: Optional[Sequence["_HttpActionHeader"]]
    Url: Optional[str]
    Auth: Optional["_HttpAuthorization"]

    @classmethod
    def _deserialize(
        cls: Type["_HttpAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpAction"]:
        if not json_data:
            return None
        return cls(
            ConfirmationUrl=json_data.get("ConfirmationUrl"),
            Headers=deserialize_list(json_data.get("Headers"), HttpActionHeader),
            Url=json_data.get("Url"),
            Auth=HttpAuthorization._deserialize(json_data.get("Auth")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpAction = HttpAction


@dataclass
class HttpActionHeader(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpActionHeader"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpActionHeader"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpActionHeader = HttpActionHeader


@dataclass
class HttpAuthorization(BaseModel):
    Sigv4: Optional["_SigV4Authorization"]

    @classmethod
    def _deserialize(
        cls: Type["_HttpAuthorization"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpAuthorization"]:
        if not json_data:
            return None
        return cls(
            Sigv4=SigV4Authorization._deserialize(json_data.get("Sigv4")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpAuthorization = HttpAuthorization


@dataclass
class SigV4Authorization(BaseModel):
    ServiceName: Optional[str]
    SigningRegion: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SigV4Authorization"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SigV4Authorization"]:
        if not json_data:
            return None
        return cls(
            ServiceName=json_data.get("ServiceName"),
            SigningRegion=json_data.get("SigningRegion"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SigV4Authorization = SigV4Authorization


@dataclass
class DynamoDBv2Action(BaseModel):
    PutItem: Optional["_PutItemInput"]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DynamoDBv2Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamoDBv2Action"]:
        if not json_data:
            return None
        return cls(
            PutItem=PutItemInput._deserialize(json_data.get("PutItem")),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamoDBv2Action = DynamoDBv2Action


@dataclass
class PutItemInput(BaseModel):
    TableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PutItemInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PutItemInput"]:
        if not json_data:
            return None
        return cls(
            TableName=json_data.get("TableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PutItemInput = PutItemInput


@dataclass
class CloudwatchMetricAction(BaseModel):
    MetricName: Optional[str]
    MetricValue: Optional[str]
    MetricNamespace: Optional[str]
    MetricUnit: Optional[str]
    RoleArn: Optional[str]
    MetricTimestamp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchMetricAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchMetricAction"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            MetricValue=json_data.get("MetricValue"),
            MetricNamespace=json_data.get("MetricNamespace"),
            MetricUnit=json_data.get("MetricUnit"),
            RoleArn=json_data.get("RoleArn"),
            MetricTimestamp=json_data.get("MetricTimestamp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchMetricAction = CloudwatchMetricAction


@dataclass
class IotSiteWiseAction(BaseModel):
    RoleArn: Optional[str]
    PutAssetPropertyValueEntries: Optional[Sequence["_PutAssetPropertyValueEntry"]]

    @classmethod
    def _deserialize(
        cls: Type["_IotSiteWiseAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IotSiteWiseAction"]:
        if not json_data:
            return None
        return cls(
            RoleArn=json_data.get("RoleArn"),
            PutAssetPropertyValueEntries=deserialize_list(json_data.get("PutAssetPropertyValueEntries"), PutAssetPropertyValueEntry),
        )


# work around possible type aliasing issues when variable has same name as a model
_IotSiteWiseAction = IotSiteWiseAction


@dataclass
class PutAssetPropertyValueEntry(BaseModel):
    PropertyAlias: Optional[str]
    PropertyValues: Optional[Sequence["_AssetPropertyValue"]]
    AssetId: Optional[str]
    EntryId: Optional[str]
    PropertyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PutAssetPropertyValueEntry"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PutAssetPropertyValueEntry"]:
        if not json_data:
            return None
        return cls(
            PropertyAlias=json_data.get("PropertyAlias"),
            PropertyValues=deserialize_list(json_data.get("PropertyValues"), AssetPropertyValue),
            AssetId=json_data.get("AssetId"),
            EntryId=json_data.get("EntryId"),
            PropertyId=json_data.get("PropertyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PutAssetPropertyValueEntry = PutAssetPropertyValueEntry


@dataclass
class AssetPropertyValue(BaseModel):
    Value: Optional["_AssetPropertyVariant"]
    Timestamp: Optional["_AssetPropertyTimestamp"]
    Quality: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssetPropertyValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssetPropertyValue"]:
        if not json_data:
            return None
        return cls(
            Value=AssetPropertyVariant._deserialize(json_data.get("Value")),
            Timestamp=AssetPropertyTimestamp._deserialize(json_data.get("Timestamp")),
            Quality=json_data.get("Quality"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssetPropertyValue = AssetPropertyValue


@dataclass
class AssetPropertyVariant(BaseModel):
    StringValue: Optional[str]
    DoubleValue: Optional[str]
    BooleanValue: Optional[str]
    IntegerValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssetPropertyVariant"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssetPropertyVariant"]:
        if not json_data:
            return None
        return cls(
            StringValue=json_data.get("StringValue"),
            DoubleValue=json_data.get("DoubleValue"),
            BooleanValue=json_data.get("BooleanValue"),
            IntegerValue=json_data.get("IntegerValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssetPropertyVariant = AssetPropertyVariant


@dataclass
class AssetPropertyTimestamp(BaseModel):
    TimeInSeconds: Optional[str]
    OffsetInNanos: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssetPropertyTimestamp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssetPropertyTimestamp"]:
        if not json_data:
            return None
        return cls(
            TimeInSeconds=json_data.get("TimeInSeconds"),
            OffsetInNanos=json_data.get("OffsetInNanos"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssetPropertyTimestamp = AssetPropertyTimestamp


@dataclass
class ElasticsearchAction(BaseModel):
    Type: Optional[str]
    Index: Optional[str]
    Id: Optional[str]
    Endpoint: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticsearchAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticsearchAction"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Index=json_data.get("Index"),
            Id=json_data.get("Id"),
            Endpoint=json_data.get("Endpoint"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticsearchAction = ElasticsearchAction


@dataclass
class SqsAction(BaseModel):
    RoleArn: Optional[str]
    UseBase64: Optional[bool]
    QueueUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SqsAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SqsAction"]:
        if not json_data:
            return None
        return cls(
            RoleArn=json_data.get("RoleArn"),
            UseBase64=json_data.get("UseBase64"),
            QueueUrl=json_data.get("QueueUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SqsAction = SqsAction


@dataclass
class KinesisAction(BaseModel):
    PartitionKey: Optional[str]
    StreamName: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisAction"]:
        if not json_data:
            return None
        return cls(
            PartitionKey=json_data.get("PartitionKey"),
            StreamName=json_data.get("StreamName"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisAction = KinesisAction


@dataclass
class IotAnalyticsAction(BaseModel):
    RoleArn: Optional[str]
    ChannelName: Optional[str]
    BatchMode: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_IotAnalyticsAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IotAnalyticsAction"]:
        if not json_data:
            return None
        return cls(
            RoleArn=json_data.get("RoleArn"),
            ChannelName=json_data.get("ChannelName"),
            BatchMode=json_data.get("BatchMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IotAnalyticsAction = IotAnalyticsAction


@dataclass
class SnsAction(BaseModel):
    TargetArn: Optional[str]
    MessageFormat: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnsAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnsAction"]:
        if not json_data:
            return None
        return cls(
            TargetArn=json_data.get("TargetArn"),
            MessageFormat=json_data.get("MessageFormat"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnsAction = SnsAction


@dataclass
class LambdaAction(BaseModel):
    FunctionArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaAction"]:
        if not json_data:
            return None
        return cls(
            FunctionArn=json_data.get("FunctionArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaAction = LambdaAction


@dataclass
class TimestreamAction(BaseModel):
    RoleArn: Optional[str]
    DatabaseName: Optional[str]
    TableName: Optional[str]
    Dimensions: Optional[Sequence["_TimestreamDimension"]]
    Timestamp: Optional["_TimestreamTimestamp"]

    @classmethod
    def _deserialize(
        cls: Type["_TimestreamAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimestreamAction"]:
        if not json_data:
            return None
        return cls(
            RoleArn=json_data.get("RoleArn"),
            DatabaseName=json_data.get("DatabaseName"),
            TableName=json_data.get("TableName"),
            Dimensions=deserialize_list(json_data.get("Dimensions"), TimestreamDimension),
            Timestamp=TimestreamTimestamp._deserialize(json_data.get("Timestamp")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimestreamAction = TimestreamAction


@dataclass
class TimestreamDimension(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimestreamDimension"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimestreamDimension"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimestreamDimension = TimestreamDimension


@dataclass
class TimestreamTimestamp(BaseModel):
    Value: Optional[str]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimestreamTimestamp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimestreamTimestamp"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimestreamTimestamp = TimestreamTimestamp


@dataclass
class KafkaAction(BaseModel):
    DestinationArn: Optional[str]
    Topic: Optional[str]
    Key: Optional[str]
    Partition: Optional[str]
    ClientProperties: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_KafkaAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KafkaAction"]:
        if not json_data:
            return None
        return cls(
            DestinationArn=json_data.get("DestinationArn"),
            Topic=json_data.get("Topic"),
            Key=json_data.get("Key"),
            Partition=json_data.get("Partition"),
            ClientProperties=json_data.get("ClientProperties"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KafkaAction = KafkaAction


@dataclass
class OpenSearchAction(BaseModel):
    Type: Optional[str]
    Index: Optional[str]
    Id: Optional[str]
    Endpoint: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OpenSearchAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenSearchAction"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Index=json_data.get("Index"),
            Id=json_data.get("Id"),
            Endpoint=json_data.get("Endpoint"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenSearchAction = OpenSearchAction


@dataclass
class LocationAction(BaseModel):
    RoleArn: Optional[str]
    TrackerName: Optional[str]
    DeviceId: Optional[str]
    Latitude: Optional[str]
    Longitude: Optional[str]
    Timestamp: Optional["_Timestamp"]

    @classmethod
    def _deserialize(
        cls: Type["_LocationAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocationAction"]:
        if not json_data:
            return None
        return cls(
            RoleArn=json_data.get("RoleArn"),
            TrackerName=json_data.get("TrackerName"),
            DeviceId=json_data.get("DeviceId"),
            Latitude=json_data.get("Latitude"),
            Longitude=json_data.get("Longitude"),
            Timestamp=Timestamp._deserialize(json_data.get("Timestamp")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocationAction = LocationAction


@dataclass
class Timestamp(BaseModel):
    Value: Optional[str]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timestamp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timestamp"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timestamp = Timestamp


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


