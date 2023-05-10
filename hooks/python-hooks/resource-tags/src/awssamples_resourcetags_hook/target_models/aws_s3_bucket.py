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
class AwsS3Bucket(BaseModel):
    AccelerateConfiguration: Optional["_AccelerateConfiguration"]
    AccessControl: Optional[str]
    AnalyticsConfigurations: Optional[Sequence["_AnalyticsConfiguration"]]
    BucketEncryption: Optional["_BucketEncryption"]
    BucketName: Optional[str]
    CorsConfiguration: Optional["_CorsConfiguration"]
    IntelligentTieringConfigurations: Optional[Sequence["_IntelligentTieringConfiguration"]]
    InventoryConfigurations: Optional[Sequence["_InventoryConfiguration"]]
    LifecycleConfiguration: Optional["_LifecycleConfiguration"]
    LoggingConfiguration: Optional["_LoggingConfiguration"]
    MetricsConfigurations: Optional[Sequence["_MetricsConfiguration"]]
    NotificationConfiguration: Optional["_NotificationConfiguration"]
    ObjectLockConfiguration: Optional["_ObjectLockConfiguration"]
    ObjectLockEnabled: Optional[bool]
    OwnershipControls: Optional["_OwnershipControls"]
    PublicAccessBlockConfiguration: Optional["_PublicAccessBlockConfiguration"]
    ReplicationConfiguration: Optional["_ReplicationConfiguration"]
    Tags: Optional[Any]
    VersioningConfiguration: Optional["_VersioningConfiguration"]
    WebsiteConfiguration: Optional["_WebsiteConfiguration"]
    Arn: Optional[str]
    DomainName: Optional[str]
    DualStackDomainName: Optional[str]
    RegionalDomainName: Optional[str]
    WebsiteURL: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsS3Bucket"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsS3Bucket"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AccelerateConfiguration=AccelerateConfiguration._deserialize(json_data.get("AccelerateConfiguration")),
            AccessControl=json_data.get("AccessControl"),
            AnalyticsConfigurations=deserialize_list(json_data.get("AnalyticsConfigurations"), AnalyticsConfiguration),
            BucketEncryption=BucketEncryption._deserialize(json_data.get("BucketEncryption")),
            BucketName=json_data.get("BucketName"),
            CorsConfiguration=CorsConfiguration._deserialize(json_data.get("CorsConfiguration")),
            IntelligentTieringConfigurations=deserialize_list(json_data.get("IntelligentTieringConfigurations"), IntelligentTieringConfiguration),
            InventoryConfigurations=deserialize_list(json_data.get("InventoryConfigurations"), InventoryConfiguration),
            LifecycleConfiguration=LifecycleConfiguration._deserialize(json_data.get("LifecycleConfiguration")),
            LoggingConfiguration=LoggingConfiguration._deserialize(json_data.get("LoggingConfiguration")),
            MetricsConfigurations=deserialize_list(json_data.get("MetricsConfigurations"), MetricsConfiguration),
            NotificationConfiguration=NotificationConfiguration._deserialize(json_data.get("NotificationConfiguration")),
            ObjectLockConfiguration=ObjectLockConfiguration._deserialize(json_data.get("ObjectLockConfiguration")),
            ObjectLockEnabled=json_data.get("ObjectLockEnabled"),
            OwnershipControls=OwnershipControls._deserialize(json_data.get("OwnershipControls")),
            PublicAccessBlockConfiguration=PublicAccessBlockConfiguration._deserialize(json_data.get("PublicAccessBlockConfiguration")),
            ReplicationConfiguration=ReplicationConfiguration._deserialize(json_data.get("ReplicationConfiguration")),
            Tags=json_data.get("Tags"),
            VersioningConfiguration=VersioningConfiguration._deserialize(json_data.get("VersioningConfiguration")),
            WebsiteConfiguration=WebsiteConfiguration._deserialize(json_data.get("WebsiteConfiguration")),
            Arn=json_data.get("Arn"),
            DomainName=json_data.get("DomainName"),
            DualStackDomainName=json_data.get("DualStackDomainName"),
            RegionalDomainName=json_data.get("RegionalDomainName"),
            WebsiteURL=json_data.get("WebsiteURL"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsS3Bucket = AwsS3Bucket


@dataclass
class AccelerateConfiguration(BaseModel):
    AccelerationStatus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccelerateConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccelerateConfiguration"]:
        if not json_data:
            return None
        return cls(
            AccelerationStatus=json_data.get("AccelerationStatus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccelerateConfiguration = AccelerateConfiguration


@dataclass
class AnalyticsConfiguration(BaseModel):
    TagFilters: Optional[Sequence["_TagFilter"]]
    StorageClassAnalysis: Optional["_StorageClassAnalysis"]
    Id: Optional[str]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnalyticsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnalyticsConfiguration"]:
        if not json_data:
            return None
        return cls(
            TagFilters=deserialize_list(json_data.get("TagFilters"), TagFilter),
            StorageClassAnalysis=StorageClassAnalysis._deserialize(json_data.get("StorageClassAnalysis")),
            Id=json_data.get("Id"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnalyticsConfiguration = AnalyticsConfiguration


@dataclass
class TagFilter(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagFilter"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagFilter = TagFilter


@dataclass
class StorageClassAnalysis(BaseModel):
    DataExport: Optional["_DataExport"]

    @classmethod
    def _deserialize(
        cls: Type["_StorageClassAnalysis"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageClassAnalysis"]:
        if not json_data:
            return None
        return cls(
            DataExport=DataExport._deserialize(json_data.get("DataExport")),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageClassAnalysis = StorageClassAnalysis


@dataclass
class DataExport(BaseModel):
    Destination: Optional["_Destination"]
    OutputSchemaVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataExport"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataExport"]:
        if not json_data:
            return None
        return cls(
            Destination=Destination._deserialize(json_data.get("Destination")),
            OutputSchemaVersion=json_data.get("OutputSchemaVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataExport = DataExport


@dataclass
class Destination(BaseModel):
    BucketArn: Optional[str]
    BucketAccountId: Optional[str]
    Format: Optional[str]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Destination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Destination"]:
        if not json_data:
            return None
        return cls(
            BucketArn=json_data.get("BucketArn"),
            BucketAccountId=json_data.get("BucketAccountId"),
            Format=json_data.get("Format"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Destination = Destination


@dataclass
class BucketEncryption(BaseModel):
    ServerSideEncryptionConfiguration: Optional[Sequence["_ServerSideEncryptionRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_BucketEncryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BucketEncryption"]:
        if not json_data:
            return None
        return cls(
            ServerSideEncryptionConfiguration=deserialize_list(json_data.get("ServerSideEncryptionConfiguration"), ServerSideEncryptionRule),
        )


# work around possible type aliasing issues when variable has same name as a model
_BucketEncryption = BucketEncryption


@dataclass
class ServerSideEncryptionRule(BaseModel):
    BucketKeyEnabled: Optional[bool]
    ServerSideEncryptionByDefault: Optional["_ServerSideEncryptionByDefault"]

    @classmethod
    def _deserialize(
        cls: Type["_ServerSideEncryptionRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerSideEncryptionRule"]:
        if not json_data:
            return None
        return cls(
            BucketKeyEnabled=json_data.get("BucketKeyEnabled"),
            ServerSideEncryptionByDefault=ServerSideEncryptionByDefault._deserialize(json_data.get("ServerSideEncryptionByDefault")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerSideEncryptionRule = ServerSideEncryptionRule


@dataclass
class ServerSideEncryptionByDefault(BaseModel):
    KMSMasterKeyID: Optional[str]
    SSEAlgorithm: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerSideEncryptionByDefault"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerSideEncryptionByDefault"]:
        if not json_data:
            return None
        return cls(
            KMSMasterKeyID=json_data.get("KMSMasterKeyID"),
            SSEAlgorithm=json_data.get("SSEAlgorithm"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerSideEncryptionByDefault = ServerSideEncryptionByDefault


@dataclass
class CorsConfiguration(BaseModel):
    CorsRules: Optional[Sequence["_CorsRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_CorsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsConfiguration"]:
        if not json_data:
            return None
        return cls(
            CorsRules=deserialize_list(json_data.get("CorsRules"), CorsRule),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsConfiguration = CorsConfiguration


@dataclass
class CorsRule(BaseModel):
    AllowedHeaders: Optional[Sequence[str]]
    AllowedMethods: Optional[Sequence[str]]
    AllowedOrigins: Optional[Sequence[str]]
    ExposedHeaders: Optional[Sequence[str]]
    Id: Optional[str]
    MaxAge: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_CorsRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsRule"]:
        if not json_data:
            return None
        return cls(
            AllowedHeaders=json_data.get("AllowedHeaders"),
            AllowedMethods=json_data.get("AllowedMethods"),
            AllowedOrigins=json_data.get("AllowedOrigins"),
            ExposedHeaders=json_data.get("ExposedHeaders"),
            Id=json_data.get("Id"),
            MaxAge=json_data.get("MaxAge"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsRule = CorsRule


@dataclass
class IntelligentTieringConfiguration(BaseModel):
    Id: Optional[str]
    Prefix: Optional[str]
    Status: Optional[str]
    TagFilters: Optional[Sequence["_TagFilter"]]
    Tierings: Optional[Sequence["_Tiering"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntelligentTieringConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntelligentTieringConfiguration"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Prefix=json_data.get("Prefix"),
            Status=json_data.get("Status"),
            TagFilters=deserialize_list(json_data.get("TagFilters"), TagFilter),
            Tierings=deserialize_list(json_data.get("Tierings"), Tiering),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntelligentTieringConfiguration = IntelligentTieringConfiguration


@dataclass
class Tiering(BaseModel):
    AccessTier: Optional[str]
    Days: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Tiering"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tiering"]:
        if not json_data:
            return None
        return cls(
            AccessTier=json_data.get("AccessTier"),
            Days=json_data.get("Days"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tiering = Tiering


@dataclass
class InventoryConfiguration(BaseModel):
    Destination: Optional["_Destination"]
    Enabled: Optional[bool]
    Id: Optional[str]
    IncludedObjectVersions: Optional[str]
    OptionalFields: Optional[Sequence[str]]
    Prefix: Optional[str]
    ScheduleFrequency: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InventoryConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InventoryConfiguration"]:
        if not json_data:
            return None
        return cls(
            Destination=Destination._deserialize(json_data.get("Destination")),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            IncludedObjectVersions=json_data.get("IncludedObjectVersions"),
            OptionalFields=json_data.get("OptionalFields"),
            Prefix=json_data.get("Prefix"),
            ScheduleFrequency=json_data.get("ScheduleFrequency"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InventoryConfiguration = InventoryConfiguration


@dataclass
class LifecycleConfiguration(BaseModel):
    Rules: Optional[Sequence["_Rule"]]

    @classmethod
    def _deserialize(
        cls: Type["_LifecycleConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecycleConfiguration"]:
        if not json_data:
            return None
        return cls(
            Rules=deserialize_list(json_data.get("Rules"), Rule),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecycleConfiguration = LifecycleConfiguration


@dataclass
class Rule(BaseModel):
    AbortIncompleteMultipartUpload: Optional["_AbortIncompleteMultipartUpload"]
    ExpirationDate: Optional[str]
    ExpirationInDays: Optional[int]
    ExpiredObjectDeleteMarker: Optional[bool]
    Id: Optional[str]
    NoncurrentVersionExpirationInDays: Optional[int]
    NoncurrentVersionExpiration: Optional["_NoncurrentVersionExpiration"]
    NoncurrentVersionTransition: Optional["_NoncurrentVersionTransition"]
    NoncurrentVersionTransitions: Optional[Sequence["_NoncurrentVersionTransition"]]
    Prefix: Optional[str]
    Status: Optional[str]
    TagFilters: Optional[Sequence["_TagFilter"]]
    ObjectSizeGreaterThan: Optional[str]
    ObjectSizeLessThan: Optional[str]
    Transition: Optional["_Transition"]
    Transitions: Optional[Sequence["_Transition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            AbortIncompleteMultipartUpload=AbortIncompleteMultipartUpload._deserialize(json_data.get("AbortIncompleteMultipartUpload")),
            ExpirationDate=json_data.get("ExpirationDate"),
            ExpirationInDays=json_data.get("ExpirationInDays"),
            ExpiredObjectDeleteMarker=json_data.get("ExpiredObjectDeleteMarker"),
            Id=json_data.get("Id"),
            NoncurrentVersionExpirationInDays=json_data.get("NoncurrentVersionExpirationInDays"),
            NoncurrentVersionExpiration=NoncurrentVersionExpiration._deserialize(json_data.get("NoncurrentVersionExpiration")),
            NoncurrentVersionTransition=NoncurrentVersionTransition._deserialize(json_data.get("NoncurrentVersionTransition")),
            NoncurrentVersionTransitions=deserialize_list(json_data.get("NoncurrentVersionTransitions"), NoncurrentVersionTransition),
            Prefix=json_data.get("Prefix"),
            Status=json_data.get("Status"),
            TagFilters=deserialize_list(json_data.get("TagFilters"), TagFilter),
            ObjectSizeGreaterThan=json_data.get("ObjectSizeGreaterThan"),
            ObjectSizeLessThan=json_data.get("ObjectSizeLessThan"),
            Transition=Transition._deserialize(json_data.get("Transition")),
            Transitions=deserialize_list(json_data.get("Transitions"), Transition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class AbortIncompleteMultipartUpload(BaseModel):
    DaysAfterInitiation: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AbortIncompleteMultipartUpload"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AbortIncompleteMultipartUpload"]:
        if not json_data:
            return None
        return cls(
            DaysAfterInitiation=json_data.get("DaysAfterInitiation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AbortIncompleteMultipartUpload = AbortIncompleteMultipartUpload


@dataclass
class NoncurrentVersionExpiration(BaseModel):
    NoncurrentDays: Optional[int]
    NewerNoncurrentVersions: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_NoncurrentVersionExpiration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NoncurrentVersionExpiration"]:
        if not json_data:
            return None
        return cls(
            NoncurrentDays=json_data.get("NoncurrentDays"),
            NewerNoncurrentVersions=json_data.get("NewerNoncurrentVersions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NoncurrentVersionExpiration = NoncurrentVersionExpiration


@dataclass
class NoncurrentVersionTransition(BaseModel):
    StorageClass: Optional[str]
    TransitionInDays: Optional[int]
    NewerNoncurrentVersions: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_NoncurrentVersionTransition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NoncurrentVersionTransition"]:
        if not json_data:
            return None
        return cls(
            StorageClass=json_data.get("StorageClass"),
            TransitionInDays=json_data.get("TransitionInDays"),
            NewerNoncurrentVersions=json_data.get("NewerNoncurrentVersions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NoncurrentVersionTransition = NoncurrentVersionTransition


@dataclass
class Transition(BaseModel):
    StorageClass: Optional[str]
    TransitionDate: Optional[str]
    TransitionInDays: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Transition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Transition"]:
        if not json_data:
            return None
        return cls(
            StorageClass=json_data.get("StorageClass"),
            TransitionDate=json_data.get("TransitionDate"),
            TransitionInDays=json_data.get("TransitionInDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Transition = Transition


@dataclass
class LoggingConfiguration(BaseModel):
    DestinationBucketName: Optional[str]
    LogFilePrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingConfiguration"]:
        if not json_data:
            return None
        return cls(
            DestinationBucketName=json_data.get("DestinationBucketName"),
            LogFilePrefix=json_data.get("LogFilePrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingConfiguration = LoggingConfiguration


@dataclass
class MetricsConfiguration(BaseModel):
    AccessPointArn: Optional[str]
    Id: Optional[str]
    Prefix: Optional[str]
    TagFilters: Optional[Sequence["_TagFilter"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricsConfiguration"]:
        if not json_data:
            return None
        return cls(
            AccessPointArn=json_data.get("AccessPointArn"),
            Id=json_data.get("Id"),
            Prefix=json_data.get("Prefix"),
            TagFilters=deserialize_list(json_data.get("TagFilters"), TagFilter),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricsConfiguration = MetricsConfiguration


@dataclass
class NotificationConfiguration(BaseModel):
    EventBridgeConfiguration: Optional["_EventBridgeConfiguration"]
    LambdaConfigurations: Optional[Sequence["_LambdaConfiguration"]]
    QueueConfigurations: Optional[Sequence["_QueueConfiguration"]]
    TopicConfigurations: Optional[Sequence["_TopicConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationConfiguration"]:
        if not json_data:
            return None
        return cls(
            EventBridgeConfiguration=EventBridgeConfiguration._deserialize(json_data.get("EventBridgeConfiguration")),
            LambdaConfigurations=deserialize_list(json_data.get("LambdaConfigurations"), LambdaConfiguration),
            QueueConfigurations=deserialize_list(json_data.get("QueueConfigurations"), QueueConfiguration),
            TopicConfigurations=deserialize_list(json_data.get("TopicConfigurations"), TopicConfiguration),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationConfiguration = NotificationConfiguration


@dataclass
class EventBridgeConfiguration(BaseModel):
    EventBridgeEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EventBridgeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventBridgeConfiguration"]:
        if not json_data:
            return None
        return cls(
            EventBridgeEnabled=json_data.get("EventBridgeEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventBridgeConfiguration = EventBridgeConfiguration


@dataclass
class LambdaConfiguration(BaseModel):
    Event: Optional[str]
    Filter: Optional["_NotificationFilter"]
    Function: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaConfiguration"]:
        if not json_data:
            return None
        return cls(
            Event=json_data.get("Event"),
            Filter=NotificationFilter._deserialize(json_data.get("Filter")),
            Function=json_data.get("Function"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaConfiguration = LambdaConfiguration


@dataclass
class NotificationFilter(BaseModel):
    S3Key: Optional["_S3KeyFilter"]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationFilter"]:
        if not json_data:
            return None
        return cls(
            S3Key=S3KeyFilter._deserialize(json_data.get("S3Key")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationFilter = NotificationFilter


@dataclass
class S3KeyFilter(BaseModel):
    Rules: Optional[Sequence["_FilterRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_S3KeyFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3KeyFilter"]:
        if not json_data:
            return None
        return cls(
            Rules=deserialize_list(json_data.get("Rules"), FilterRule),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3KeyFilter = S3KeyFilter


@dataclass
class FilterRule(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterRule"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterRule = FilterRule


@dataclass
class QueueConfiguration(BaseModel):
    Event: Optional[str]
    Filter: Optional["_NotificationFilter"]
    Queue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QueueConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueueConfiguration"]:
        if not json_data:
            return None
        return cls(
            Event=json_data.get("Event"),
            Filter=NotificationFilter._deserialize(json_data.get("Filter")),
            Queue=json_data.get("Queue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueueConfiguration = QueueConfiguration


@dataclass
class TopicConfiguration(BaseModel):
    Event: Optional[str]
    Filter: Optional["_NotificationFilter"]
    Topic: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TopicConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopicConfiguration"]:
        if not json_data:
            return None
        return cls(
            Event=json_data.get("Event"),
            Filter=NotificationFilter._deserialize(json_data.get("Filter")),
            Topic=json_data.get("Topic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopicConfiguration = TopicConfiguration


@dataclass
class ObjectLockConfiguration(BaseModel):
    ObjectLockEnabled: Optional[str]
    Rule: Optional["_ObjectLockRule"]

    @classmethod
    def _deserialize(
        cls: Type["_ObjectLockConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObjectLockConfiguration"]:
        if not json_data:
            return None
        return cls(
            ObjectLockEnabled=json_data.get("ObjectLockEnabled"),
            Rule=ObjectLockRule._deserialize(json_data.get("Rule")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObjectLockConfiguration = ObjectLockConfiguration


@dataclass
class ObjectLockRule(BaseModel):
    DefaultRetention: Optional["_DefaultRetention"]

    @classmethod
    def _deserialize(
        cls: Type["_ObjectLockRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObjectLockRule"]:
        if not json_data:
            return None
        return cls(
            DefaultRetention=DefaultRetention._deserialize(json_data.get("DefaultRetention")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObjectLockRule = ObjectLockRule


@dataclass
class DefaultRetention(BaseModel):
    Years: Optional[int]
    Days: Optional[int]
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultRetention"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultRetention"]:
        if not json_data:
            return None
        return cls(
            Years=json_data.get("Years"),
            Days=json_data.get("Days"),
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultRetention = DefaultRetention


@dataclass
class OwnershipControls(BaseModel):
    Rules: Optional[Sequence["_OwnershipControlsRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_OwnershipControls"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnershipControls"]:
        if not json_data:
            return None
        return cls(
            Rules=deserialize_list(json_data.get("Rules"), OwnershipControlsRule),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnershipControls = OwnershipControls


@dataclass
class OwnershipControlsRule(BaseModel):
    ObjectOwnership: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OwnershipControlsRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnershipControlsRule"]:
        if not json_data:
            return None
        return cls(
            ObjectOwnership=json_data.get("ObjectOwnership"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnershipControlsRule = OwnershipControlsRule


@dataclass
class PublicAccessBlockConfiguration(BaseModel):
    BlockPublicAcls: Optional[bool]
    BlockPublicPolicy: Optional[bool]
    IgnorePublicAcls: Optional[bool]
    RestrictPublicBuckets: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PublicAccessBlockConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicAccessBlockConfiguration"]:
        if not json_data:
            return None
        return cls(
            BlockPublicAcls=json_data.get("BlockPublicAcls"),
            BlockPublicPolicy=json_data.get("BlockPublicPolicy"),
            IgnorePublicAcls=json_data.get("IgnorePublicAcls"),
            RestrictPublicBuckets=json_data.get("RestrictPublicBuckets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicAccessBlockConfiguration = PublicAccessBlockConfiguration


@dataclass
class ReplicationConfiguration(BaseModel):
    Role: Optional[str]
    Rules: Optional[Sequence["_ReplicationRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationConfiguration"]:
        if not json_data:
            return None
        return cls(
            Role=json_data.get("Role"),
            Rules=deserialize_list(json_data.get("Rules"), ReplicationRule),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationConfiguration = ReplicationConfiguration


@dataclass
class ReplicationRule(BaseModel):
    DeleteMarkerReplication: Optional["_DeleteMarkerReplication"]
    Destination: Optional["_ReplicationDestination"]
    Filter: Optional["_ReplicationRuleFilter"]
    Id: Optional[str]
    Prefix: Optional[str]
    Priority: Optional[int]
    SourceSelectionCriteria: Optional["_SourceSelectionCriteria"]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationRule"]:
        if not json_data:
            return None
        return cls(
            DeleteMarkerReplication=DeleteMarkerReplication._deserialize(json_data.get("DeleteMarkerReplication")),
            Destination=ReplicationDestination._deserialize(json_data.get("Destination")),
            Filter=ReplicationRuleFilter._deserialize(json_data.get("Filter")),
            Id=json_data.get("Id"),
            Prefix=json_data.get("Prefix"),
            Priority=json_data.get("Priority"),
            SourceSelectionCriteria=SourceSelectionCriteria._deserialize(json_data.get("SourceSelectionCriteria")),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationRule = ReplicationRule


@dataclass
class DeleteMarkerReplication(BaseModel):
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeleteMarkerReplication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeleteMarkerReplication"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeleteMarkerReplication = DeleteMarkerReplication


@dataclass
class ReplicationDestination(BaseModel):
    AccessControlTranslation: Optional["_AccessControlTranslation"]
    Account: Optional[str]
    Bucket: Optional[str]
    EncryptionConfiguration: Optional["_EncryptionConfiguration"]
    Metrics: Optional["_Metrics"]
    ReplicationTime: Optional["_ReplicationTime"]
    StorageClass: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationDestination"]:
        if not json_data:
            return None
        return cls(
            AccessControlTranslation=AccessControlTranslation._deserialize(json_data.get("AccessControlTranslation")),
            Account=json_data.get("Account"),
            Bucket=json_data.get("Bucket"),
            EncryptionConfiguration=EncryptionConfiguration._deserialize(json_data.get("EncryptionConfiguration")),
            Metrics=Metrics._deserialize(json_data.get("Metrics")),
            ReplicationTime=ReplicationTime._deserialize(json_data.get("ReplicationTime")),
            StorageClass=json_data.get("StorageClass"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationDestination = ReplicationDestination


@dataclass
class AccessControlTranslation(BaseModel):
    Owner: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessControlTranslation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessControlTranslation"]:
        if not json_data:
            return None
        return cls(
            Owner=json_data.get("Owner"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessControlTranslation = AccessControlTranslation


@dataclass
class EncryptionConfiguration(BaseModel):
    ReplicaKmsKeyID: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfiguration"]:
        if not json_data:
            return None
        return cls(
            ReplicaKmsKeyID=json_data.get("ReplicaKmsKeyID"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfiguration = EncryptionConfiguration


@dataclass
class Metrics(BaseModel):
    EventThreshold: Optional["_ReplicationTimeValue"]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metrics"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metrics"]:
        if not json_data:
            return None
        return cls(
            EventThreshold=ReplicationTimeValue._deserialize(json_data.get("EventThreshold")),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metrics = Metrics


@dataclass
class ReplicationTimeValue(BaseModel):
    Minutes: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationTimeValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationTimeValue"]:
        if not json_data:
            return None
        return cls(
            Minutes=json_data.get("Minutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationTimeValue = ReplicationTimeValue


@dataclass
class ReplicationTime(BaseModel):
    Status: Optional[str]
    Time: Optional["_ReplicationTimeValue"]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationTime"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationTime"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            Time=ReplicationTimeValue._deserialize(json_data.get("Time")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationTime = ReplicationTime


@dataclass
class ReplicationRuleFilter(BaseModel):
    And: Optional["_ReplicationRuleAndOperator"]
    Prefix: Optional[str]
    TagFilter: Optional["_TagFilter"]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationRuleFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationRuleFilter"]:
        if not json_data:
            return None
        return cls(
            And=ReplicationRuleAndOperator._deserialize(json_data.get("And")),
            Prefix=json_data.get("Prefix"),
            TagFilter=TagFilter._deserialize(json_data.get("TagFilter")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationRuleFilter = ReplicationRuleFilter


@dataclass
class ReplicationRuleAndOperator(BaseModel):
    Prefix: Optional[str]
    TagFilters: Optional[Sequence["_TagFilter"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationRuleAndOperator"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationRuleAndOperator"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
            TagFilters=deserialize_list(json_data.get("TagFilters"), TagFilter),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationRuleAndOperator = ReplicationRuleAndOperator


@dataclass
class SourceSelectionCriteria(BaseModel):
    ReplicaModifications: Optional["_ReplicaModifications"]
    SseKmsEncryptedObjects: Optional["_SseKmsEncryptedObjects"]

    @classmethod
    def _deserialize(
        cls: Type["_SourceSelectionCriteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceSelectionCriteria"]:
        if not json_data:
            return None
        return cls(
            ReplicaModifications=ReplicaModifications._deserialize(json_data.get("ReplicaModifications")),
            SseKmsEncryptedObjects=SseKmsEncryptedObjects._deserialize(json_data.get("SseKmsEncryptedObjects")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceSelectionCriteria = SourceSelectionCriteria


@dataclass
class ReplicaModifications(BaseModel):
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicaModifications"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicaModifications"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicaModifications = ReplicaModifications


@dataclass
class SseKmsEncryptedObjects(BaseModel):
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SseKmsEncryptedObjects"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SseKmsEncryptedObjects"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SseKmsEncryptedObjects = SseKmsEncryptedObjects


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
class VersioningConfiguration(BaseModel):
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersioningConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersioningConfiguration"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersioningConfiguration = VersioningConfiguration


@dataclass
class WebsiteConfiguration(BaseModel):
    ErrorDocument: Optional[str]
    IndexDocument: Optional[str]
    RoutingRules: Optional[Sequence["_RoutingRule"]]
    RedirectAllRequestsTo: Optional["_RedirectAllRequestsTo"]

    @classmethod
    def _deserialize(
        cls: Type["_WebsiteConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebsiteConfiguration"]:
        if not json_data:
            return None
        return cls(
            ErrorDocument=json_data.get("ErrorDocument"),
            IndexDocument=json_data.get("IndexDocument"),
            RoutingRules=deserialize_list(json_data.get("RoutingRules"), RoutingRule),
            RedirectAllRequestsTo=RedirectAllRequestsTo._deserialize(json_data.get("RedirectAllRequestsTo")),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebsiteConfiguration = WebsiteConfiguration


@dataclass
class RoutingRule(BaseModel):
    RedirectRule: Optional["_RedirectRule"]
    RoutingRuleCondition: Optional["_RoutingRuleCondition"]

    @classmethod
    def _deserialize(
        cls: Type["_RoutingRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutingRule"]:
        if not json_data:
            return None
        return cls(
            RedirectRule=RedirectRule._deserialize(json_data.get("RedirectRule")),
            RoutingRuleCondition=RoutingRuleCondition._deserialize(json_data.get("RoutingRuleCondition")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutingRule = RoutingRule


@dataclass
class RedirectRule(BaseModel):
    HostName: Optional[str]
    HttpRedirectCode: Optional[str]
    Protocol: Optional[str]
    ReplaceKeyPrefixWith: Optional[str]
    ReplaceKeyWith: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedirectRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedirectRule"]:
        if not json_data:
            return None
        return cls(
            HostName=json_data.get("HostName"),
            HttpRedirectCode=json_data.get("HttpRedirectCode"),
            Protocol=json_data.get("Protocol"),
            ReplaceKeyPrefixWith=json_data.get("ReplaceKeyPrefixWith"),
            ReplaceKeyWith=json_data.get("ReplaceKeyWith"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedirectRule = RedirectRule


@dataclass
class RoutingRuleCondition(BaseModel):
    KeyPrefixEquals: Optional[str]
    HttpErrorCodeReturnedEquals: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RoutingRuleCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutingRuleCondition"]:
        if not json_data:
            return None
        return cls(
            KeyPrefixEquals=json_data.get("KeyPrefixEquals"),
            HttpErrorCodeReturnedEquals=json_data.get("HttpErrorCodeReturnedEquals"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutingRuleCondition = RoutingRuleCondition


@dataclass
class RedirectAllRequestsTo(BaseModel):
    HostName: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedirectAllRequestsTo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedirectAllRequestsTo"]:
        if not json_data:
            return None
        return cls(
            HostName=json_data.get("HostName"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedirectAllRequestsTo = RedirectAllRequestsTo


