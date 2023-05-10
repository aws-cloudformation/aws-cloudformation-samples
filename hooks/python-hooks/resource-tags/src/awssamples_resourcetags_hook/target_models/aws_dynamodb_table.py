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
class AwsDynamodbTable(BaseModel):
    Arn: Optional[str]
    StreamArn: Optional[str]
    AttributeDefinitions: Optional[Sequence["_AttributeDefinition"]]
    BillingMode: Optional[str]
    DeletionProtectionEnabled: Optional[bool]
    GlobalSecondaryIndexes: Optional[Sequence["_GlobalSecondaryIndex"]]
    KeySchema: Optional[Any]
    LocalSecondaryIndexes: Optional[Sequence["_LocalSecondaryIndex"]]
    PointInTimeRecoverySpecification: Optional["_PointInTimeRecoverySpecification"]
    TableClass: Optional[str]
    ProvisionedThroughput: Optional["_ProvisionedThroughput"]
    SSESpecification: Optional["_SSESpecification"]
    StreamSpecification: Optional["_StreamSpecification"]
    TableName: Optional[str]
    Tags: Optional[Any]
    TimeToLiveSpecification: Optional["_TimeToLiveSpecification"]
    ContributorInsightsSpecification: Optional["_ContributorInsightsSpecification"]
    KinesisStreamSpecification: Optional["_KinesisStreamSpecification"]
    ImportSourceSpecification: Optional["_ImportSourceSpecification"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDynamodbTable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDynamodbTable"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            StreamArn=json_data.get("StreamArn"),
            AttributeDefinitions=deserialize_list(json_data.get("AttributeDefinitions"), AttributeDefinition),
            BillingMode=json_data.get("BillingMode"),
            DeletionProtectionEnabled=json_data.get("DeletionProtectionEnabled"),
            GlobalSecondaryIndexes=deserialize_list(json_data.get("GlobalSecondaryIndexes"), GlobalSecondaryIndex),
            KeySchema=json_data.get("KeySchema"),
            LocalSecondaryIndexes=deserialize_list(json_data.get("LocalSecondaryIndexes"), LocalSecondaryIndex),
            PointInTimeRecoverySpecification=PointInTimeRecoverySpecification._deserialize(json_data.get("PointInTimeRecoverySpecification")),
            TableClass=json_data.get("TableClass"),
            ProvisionedThroughput=ProvisionedThroughput._deserialize(json_data.get("ProvisionedThroughput")),
            SSESpecification=SSESpecification._deserialize(json_data.get("SSESpecification")),
            StreamSpecification=StreamSpecification._deserialize(json_data.get("StreamSpecification")),
            TableName=json_data.get("TableName"),
            Tags=json_data.get("Tags"),
            TimeToLiveSpecification=TimeToLiveSpecification._deserialize(json_data.get("TimeToLiveSpecification")),
            ContributorInsightsSpecification=ContributorInsightsSpecification._deserialize(json_data.get("ContributorInsightsSpecification")),
            KinesisStreamSpecification=KinesisStreamSpecification._deserialize(json_data.get("KinesisStreamSpecification")),
            ImportSourceSpecification=ImportSourceSpecification._deserialize(json_data.get("ImportSourceSpecification")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDynamodbTable = AwsDynamodbTable


@dataclass
class AttributeDefinition(BaseModel):
    AttributeName: Optional[str]
    AttributeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttributeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributeDefinition"]:
        if not json_data:
            return None
        return cls(
            AttributeName=json_data.get("AttributeName"),
            AttributeType=json_data.get("AttributeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributeDefinition = AttributeDefinition


@dataclass
class GlobalSecondaryIndex(BaseModel):
    IndexName: Optional[str]
    KeySchema: Optional[Sequence["_KeySchema"]]
    Projection: Optional["_Projection"]
    ProvisionedThroughput: Optional["_ProvisionedThroughput"]
    ContributorInsightsSpecification: Optional["_ContributorInsightsSpecification"]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalSecondaryIndex"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalSecondaryIndex"]:
        if not json_data:
            return None
        return cls(
            IndexName=json_data.get("IndexName"),
            KeySchema=deserialize_list(json_data.get("KeySchema"), KeySchema),
            Projection=Projection._deserialize(json_data.get("Projection")),
            ProvisionedThroughput=ProvisionedThroughput._deserialize(json_data.get("ProvisionedThroughput")),
            ContributorInsightsSpecification=ContributorInsightsSpecification._deserialize(json_data.get("ContributorInsightsSpecification")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalSecondaryIndex = GlobalSecondaryIndex


@dataclass
class KeySchema(BaseModel):
    AttributeName: Optional[str]
    KeyType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeySchema"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeySchema"]:
        if not json_data:
            return None
        return cls(
            AttributeName=json_data.get("AttributeName"),
            KeyType=json_data.get("KeyType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeySchema = KeySchema


@dataclass
class Projection(BaseModel):
    NonKeyAttributes: Optional[Sequence[str]]
    ProjectionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Projection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Projection"]:
        if not json_data:
            return None
        return cls(
            NonKeyAttributes=json_data.get("NonKeyAttributes"),
            ProjectionType=json_data.get("ProjectionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Projection = Projection


@dataclass
class ProvisionedThroughput(BaseModel):
    ReadCapacityUnits: Optional[int]
    WriteCapacityUnits: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ProvisionedThroughput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProvisionedThroughput"]:
        if not json_data:
            return None
        return cls(
            ReadCapacityUnits=json_data.get("ReadCapacityUnits"),
            WriteCapacityUnits=json_data.get("WriteCapacityUnits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProvisionedThroughput = ProvisionedThroughput


@dataclass
class ContributorInsightsSpecification(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ContributorInsightsSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContributorInsightsSpecification"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContributorInsightsSpecification = ContributorInsightsSpecification


@dataclass
class LocalSecondaryIndex(BaseModel):
    IndexName: Optional[str]
    KeySchema: Optional[Sequence["_KeySchema"]]
    Projection: Optional["_Projection"]

    @classmethod
    def _deserialize(
        cls: Type["_LocalSecondaryIndex"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalSecondaryIndex"]:
        if not json_data:
            return None
        return cls(
            IndexName=json_data.get("IndexName"),
            KeySchema=deserialize_list(json_data.get("KeySchema"), KeySchema),
            Projection=Projection._deserialize(json_data.get("Projection")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalSecondaryIndex = LocalSecondaryIndex


@dataclass
class PointInTimeRecoverySpecification(BaseModel):
    PointInTimeRecoveryEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PointInTimeRecoverySpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PointInTimeRecoverySpecification"]:
        if not json_data:
            return None
        return cls(
            PointInTimeRecoveryEnabled=json_data.get("PointInTimeRecoveryEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PointInTimeRecoverySpecification = PointInTimeRecoverySpecification


@dataclass
class SSESpecification(BaseModel):
    KMSMasterKeyId: Optional[str]
    SSEEnabled: Optional[bool]
    SSEType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SSESpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SSESpecification"]:
        if not json_data:
            return None
        return cls(
            KMSMasterKeyId=json_data.get("KMSMasterKeyId"),
            SSEEnabled=json_data.get("SSEEnabled"),
            SSEType=json_data.get("SSEType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SSESpecification = SSESpecification


@dataclass
class StreamSpecification(BaseModel):
    StreamViewType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StreamSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StreamSpecification"]:
        if not json_data:
            return None
        return cls(
            StreamViewType=json_data.get("StreamViewType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StreamSpecification = StreamSpecification


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
class TimeToLiveSpecification(BaseModel):
    AttributeName: Optional[str]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TimeToLiveSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeToLiveSpecification"]:
        if not json_data:
            return None
        return cls(
            AttributeName=json_data.get("AttributeName"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeToLiveSpecification = TimeToLiveSpecification


@dataclass
class KinesisStreamSpecification(BaseModel):
    StreamArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisStreamSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisStreamSpecification"]:
        if not json_data:
            return None
        return cls(
            StreamArn=json_data.get("StreamArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisStreamSpecification = KinesisStreamSpecification


@dataclass
class ImportSourceSpecification(BaseModel):
    S3BucketSource: Optional["_S3BucketSource"]
    InputFormat: Optional[str]
    InputFormatOptions: Optional["_InputFormatOptions"]
    InputCompressionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImportSourceSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImportSourceSpecification"]:
        if not json_data:
            return None
        return cls(
            S3BucketSource=S3BucketSource._deserialize(json_data.get("S3BucketSource")),
            InputFormat=json_data.get("InputFormat"),
            InputFormatOptions=InputFormatOptions._deserialize(json_data.get("InputFormatOptions")),
            InputCompressionType=json_data.get("InputCompressionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImportSourceSpecification = ImportSourceSpecification


@dataclass
class S3BucketSource(BaseModel):
    S3BucketOwner: Optional[str]
    S3Bucket: Optional[str]
    S3KeyPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3BucketSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3BucketSource"]:
        if not json_data:
            return None
        return cls(
            S3BucketOwner=json_data.get("S3BucketOwner"),
            S3Bucket=json_data.get("S3Bucket"),
            S3KeyPrefix=json_data.get("S3KeyPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3BucketSource = S3BucketSource


@dataclass
class InputFormatOptions(BaseModel):
    Csv: Optional["_Csv"]

    @classmethod
    def _deserialize(
        cls: Type["_InputFormatOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputFormatOptions"]:
        if not json_data:
            return None
        return cls(
            Csv=Csv._deserialize(json_data.get("Csv")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputFormatOptions = InputFormatOptions


@dataclass
class Csv(BaseModel):
    HeaderList: Optional[Sequence[str]]
    Delimiter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Csv"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Csv"]:
        if not json_data:
            return None
        return cls(
            HeaderList=json_data.get("HeaderList"),
            Delimiter=json_data.get("Delimiter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Csv = Csv


