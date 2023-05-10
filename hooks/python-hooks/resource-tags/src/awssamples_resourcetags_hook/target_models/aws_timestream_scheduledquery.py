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
class AwsTimestreamScheduledquery(BaseModel):
    Arn: Optional[str]
    ScheduledQueryName: Optional[str]
    QueryString: Optional[str]
    ScheduleConfiguration: Optional["_ScheduleConfiguration"]
    NotificationConfiguration: Optional["_NotificationConfiguration"]
    ClientToken: Optional[str]
    ScheduledQueryExecutionRoleArn: Optional[str]
    TargetConfiguration: Optional["_TargetConfiguration"]
    ErrorReportConfiguration: Optional["_ErrorReportConfiguration"]
    KmsKeyId: Optional[str]
    SQName: Optional[str]
    SQQueryString: Optional[str]
    SQScheduleConfiguration: Optional[str]
    SQNotificationConfiguration: Optional[str]
    SQScheduledQueryExecutionRoleArn: Optional[str]
    SQTargetConfiguration: Optional[str]
    SQErrorReportConfiguration: Optional[str]
    SQKmsKeyId: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsTimestreamScheduledquery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsTimestreamScheduledquery"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            ScheduledQueryName=json_data.get("ScheduledQueryName"),
            QueryString=json_data.get("QueryString"),
            ScheduleConfiguration=ScheduleConfiguration._deserialize(json_data.get("ScheduleConfiguration")),
            NotificationConfiguration=NotificationConfiguration._deserialize(json_data.get("NotificationConfiguration")),
            ClientToken=json_data.get("ClientToken"),
            ScheduledQueryExecutionRoleArn=json_data.get("ScheduledQueryExecutionRoleArn"),
            TargetConfiguration=TargetConfiguration._deserialize(json_data.get("TargetConfiguration")),
            ErrorReportConfiguration=ErrorReportConfiguration._deserialize(json_data.get("ErrorReportConfiguration")),
            KmsKeyId=json_data.get("KmsKeyId"),
            SQName=json_data.get("SQName"),
            SQQueryString=json_data.get("SQQueryString"),
            SQScheduleConfiguration=json_data.get("SQScheduleConfiguration"),
            SQNotificationConfiguration=json_data.get("SQNotificationConfiguration"),
            SQScheduledQueryExecutionRoleArn=json_data.get("SQScheduledQueryExecutionRoleArn"),
            SQTargetConfiguration=json_data.get("SQTargetConfiguration"),
            SQErrorReportConfiguration=json_data.get("SQErrorReportConfiguration"),
            SQKmsKeyId=json_data.get("SQKmsKeyId"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsTimestreamScheduledquery = AwsTimestreamScheduledquery


@dataclass
class ScheduleConfiguration(BaseModel):
    ScheduleExpression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleConfiguration"]:
        if not json_data:
            return None
        return cls(
            ScheduleExpression=json_data.get("ScheduleExpression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleConfiguration = ScheduleConfiguration


@dataclass
class NotificationConfiguration(BaseModel):
    SnsConfiguration: Optional["_SnsConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationConfiguration"]:
        if not json_data:
            return None
        return cls(
            SnsConfiguration=SnsConfiguration._deserialize(json_data.get("SnsConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationConfiguration = NotificationConfiguration


@dataclass
class SnsConfiguration(BaseModel):
    TopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnsConfiguration"]:
        if not json_data:
            return None
        return cls(
            TopicArn=json_data.get("TopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnsConfiguration = SnsConfiguration


@dataclass
class TargetConfiguration(BaseModel):
    TimestreamConfiguration: Optional["_TimestreamConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_TargetConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetConfiguration"]:
        if not json_data:
            return None
        return cls(
            TimestreamConfiguration=TimestreamConfiguration._deserialize(json_data.get("TimestreamConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetConfiguration = TargetConfiguration


@dataclass
class TimestreamConfiguration(BaseModel):
    DatabaseName: Optional[str]
    TableName: Optional[str]
    TimeColumn: Optional[str]
    DimensionMappings: Optional[Sequence["_DimensionMapping"]]
    MultiMeasureMappings: Optional["_MultiMeasureMappings"]
    MixedMeasureMappings: Optional[Sequence["_MixedMeasureMapping"]]
    MeasureNameColumn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimestreamConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimestreamConfiguration"]:
        if not json_data:
            return None
        return cls(
            DatabaseName=json_data.get("DatabaseName"),
            TableName=json_data.get("TableName"),
            TimeColumn=json_data.get("TimeColumn"),
            DimensionMappings=deserialize_list(json_data.get("DimensionMappings"), DimensionMapping),
            MultiMeasureMappings=MultiMeasureMappings._deserialize(json_data.get("MultiMeasureMappings")),
            MixedMeasureMappings=deserialize_list(json_data.get("MixedMeasureMappings"), MixedMeasureMapping),
            MeasureNameColumn=json_data.get("MeasureNameColumn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimestreamConfiguration = TimestreamConfiguration


@dataclass
class DimensionMapping(BaseModel):
    Name: Optional[str]
    DimensionValueType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionMapping"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            DimensionValueType=json_data.get("DimensionValueType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionMapping = DimensionMapping


@dataclass
class MultiMeasureMappings(BaseModel):
    TargetMultiMeasureName: Optional[str]
    MultiMeasureAttributeMappings: Optional[Sequence["_MultiMeasureAttributeMapping"]]

    @classmethod
    def _deserialize(
        cls: Type["_MultiMeasureMappings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MultiMeasureMappings"]:
        if not json_data:
            return None
        return cls(
            TargetMultiMeasureName=json_data.get("TargetMultiMeasureName"),
            MultiMeasureAttributeMappings=deserialize_list(json_data.get("MultiMeasureAttributeMappings"), MultiMeasureAttributeMapping),
        )


# work around possible type aliasing issues when variable has same name as a model
_MultiMeasureMappings = MultiMeasureMappings


@dataclass
class MultiMeasureAttributeMapping(BaseModel):
    SourceColumn: Optional[str]
    MeasureValueType: Optional[str]
    TargetMultiMeasureAttributeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MultiMeasureAttributeMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MultiMeasureAttributeMapping"]:
        if not json_data:
            return None
        return cls(
            SourceColumn=json_data.get("SourceColumn"),
            MeasureValueType=json_data.get("MeasureValueType"),
            TargetMultiMeasureAttributeName=json_data.get("TargetMultiMeasureAttributeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MultiMeasureAttributeMapping = MultiMeasureAttributeMapping


@dataclass
class MixedMeasureMapping(BaseModel):
    MeasureName: Optional[str]
    SourceColumn: Optional[str]
    TargetMeasureName: Optional[str]
    MeasureValueType: Optional[str]
    MultiMeasureAttributeMappings: Optional[Sequence["_MultiMeasureAttributeMapping"]]

    @classmethod
    def _deserialize(
        cls: Type["_MixedMeasureMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MixedMeasureMapping"]:
        if not json_data:
            return None
        return cls(
            MeasureName=json_data.get("MeasureName"),
            SourceColumn=json_data.get("SourceColumn"),
            TargetMeasureName=json_data.get("TargetMeasureName"),
            MeasureValueType=json_data.get("MeasureValueType"),
            MultiMeasureAttributeMappings=deserialize_list(json_data.get("MultiMeasureAttributeMappings"), MultiMeasureAttributeMapping),
        )


# work around possible type aliasing issues when variable has same name as a model
_MixedMeasureMapping = MixedMeasureMapping


@dataclass
class ErrorReportConfiguration(BaseModel):
    S3Configuration: Optional["_S3Configuration"]

    @classmethod
    def _deserialize(
        cls: Type["_ErrorReportConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ErrorReportConfiguration"]:
        if not json_data:
            return None
        return cls(
            S3Configuration=S3Configuration._deserialize(json_data.get("S3Configuration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ErrorReportConfiguration = ErrorReportConfiguration


@dataclass
class S3Configuration(BaseModel):
    BucketName: Optional[str]
    ObjectKeyPrefix: Optional[str]
    EncryptionOption: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Configuration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Configuration"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            ObjectKeyPrefix=json_data.get("ObjectKeyPrefix"),
            EncryptionOption=json_data.get("EncryptionOption"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Configuration = S3Configuration


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


