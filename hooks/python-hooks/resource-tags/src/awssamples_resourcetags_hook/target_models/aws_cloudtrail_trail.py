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
class AwsCloudtrailTrail(BaseModel):
    CloudWatchLogsLogGroupArn: Optional[str]
    CloudWatchLogsRoleArn: Optional[str]
    EnableLogFileValidation: Optional[bool]
    AdvancedEventSelectors: Optional[AbstractSet["_AdvancedEventSelector"]]
    EventSelectors: Optional[AbstractSet["_EventSelector"]]
    IncludeGlobalServiceEvents: Optional[bool]
    IsLogging: Optional[bool]
    IsMultiRegionTrail: Optional[bool]
    IsOrganizationTrail: Optional[bool]
    KMSKeyId: Optional[str]
    S3BucketName: Optional[str]
    S3KeyPrefix: Optional[str]
    SnsTopicName: Optional[str]
    Tags: Optional[Any]
    TrailName: Optional[str]
    Arn: Optional[str]
    SnsTopicArn: Optional[str]
    InsightSelectors: Optional[AbstractSet["_InsightSelector"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudtrailTrail"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudtrailTrail"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CloudWatchLogsLogGroupArn=json_data.get("CloudWatchLogsLogGroupArn"),
            CloudWatchLogsRoleArn=json_data.get("CloudWatchLogsRoleArn"),
            EnableLogFileValidation=json_data.get("EnableLogFileValidation"),
            AdvancedEventSelectors=set_or_none(json_data.get("AdvancedEventSelectors")),
            EventSelectors=set_or_none(json_data.get("EventSelectors")),
            IncludeGlobalServiceEvents=json_data.get("IncludeGlobalServiceEvents"),
            IsLogging=json_data.get("IsLogging"),
            IsMultiRegionTrail=json_data.get("IsMultiRegionTrail"),
            IsOrganizationTrail=json_data.get("IsOrganizationTrail"),
            KMSKeyId=json_data.get("KMSKeyId"),
            S3BucketName=json_data.get("S3BucketName"),
            S3KeyPrefix=json_data.get("S3KeyPrefix"),
            SnsTopicName=json_data.get("SnsTopicName"),
            Tags=json_data.get("Tags"),
            TrailName=json_data.get("TrailName"),
            Arn=json_data.get("Arn"),
            SnsTopicArn=json_data.get("SnsTopicArn"),
            InsightSelectors=set_or_none(json_data.get("InsightSelectors")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudtrailTrail = AwsCloudtrailTrail


@dataclass
class AdvancedEventSelector(BaseModel):
    Name: Optional[str]
    FieldSelectors: Optional[AbstractSet["_AdvancedFieldSelector"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedEventSelector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedEventSelector"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            FieldSelectors=set_or_none(json_data.get("FieldSelectors")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedEventSelector = AdvancedEventSelector


@dataclass
class AdvancedFieldSelector(BaseModel):
    Field: Optional[str]
    Equals: Optional[AbstractSet[str]]
    StartsWith: Optional[AbstractSet[str]]
    EndsWith: Optional[AbstractSet[str]]
    NotEquals: Optional[AbstractSet[str]]
    NotStartsWith: Optional[AbstractSet[str]]
    NotEndsWith: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedFieldSelector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedFieldSelector"]:
        if not json_data:
            return None
        return cls(
            Field=json_data.get("Field"),
            Equals=set_or_none(json_data.get("Equals")),
            StartsWith=set_or_none(json_data.get("StartsWith")),
            EndsWith=set_or_none(json_data.get("EndsWith")),
            NotEquals=set_or_none(json_data.get("NotEquals")),
            NotStartsWith=set_or_none(json_data.get("NotStartsWith")),
            NotEndsWith=set_or_none(json_data.get("NotEndsWith")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedFieldSelector = AdvancedFieldSelector


@dataclass
class EventSelector(BaseModel):
    DataResources: Optional[AbstractSet["_DataResource"]]
    IncludeManagementEvents: Optional[bool]
    ReadWriteType: Optional[str]
    ExcludeManagementEventSources: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_EventSelector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventSelector"]:
        if not json_data:
            return None
        return cls(
            DataResources=set_or_none(json_data.get("DataResources")),
            IncludeManagementEvents=json_data.get("IncludeManagementEvents"),
            ReadWriteType=json_data.get("ReadWriteType"),
            ExcludeManagementEventSources=set_or_none(json_data.get("ExcludeManagementEventSources")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventSelector = EventSelector


@dataclass
class DataResource(BaseModel):
    Type: Optional[str]
    Values: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DataResource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataResource"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Values=set_or_none(json_data.get("Values")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataResource = DataResource


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
class InsightSelector(BaseModel):
    InsightType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InsightSelector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InsightSelector"]:
        if not json_data:
            return None
        return cls(
            InsightType=json_data.get("InsightType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InsightSelector = InsightSelector


