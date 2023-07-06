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
class AwsGlueCrawler(BaseModel):
    Classifiers: Optional[Sequence[str]]
    Description: Optional[str]
    SchemaChangePolicy: Optional["_SchemaChangePolicy"]
    Configuration: Optional[str]
    RecrawlPolicy: Optional["_RecrawlPolicy"]
    DatabaseName: Optional[str]
    Targets: Optional["_Targets"]
    CrawlerSecurityConfiguration: Optional[str]
    Name: Optional[str]
    Role: Optional[str]
    Schedule: Optional["_Schedule"]
    Id: Optional[str]
    TablePrefix: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGlueCrawler"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGlueCrawler"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Classifiers=json_data.get("Classifiers"),
            Description=json_data.get("Description"),
            SchemaChangePolicy=SchemaChangePolicy._deserialize(json_data.get("SchemaChangePolicy")),
            Configuration=json_data.get("Configuration"),
            RecrawlPolicy=RecrawlPolicy._deserialize(json_data.get("RecrawlPolicy")),
            DatabaseName=json_data.get("DatabaseName"),
            Targets=Targets._deserialize(json_data.get("Targets")),
            CrawlerSecurityConfiguration=json_data.get("CrawlerSecurityConfiguration"),
            Name=json_data.get("Name"),
            Role=json_data.get("Role"),
            Schedule=Schedule._deserialize(json_data.get("Schedule")),
            Id=json_data.get("Id"),
            TablePrefix=json_data.get("TablePrefix"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGlueCrawler = AwsGlueCrawler


@dataclass
class SchemaChangePolicy(BaseModel):
    UpdateBehavior: Optional[str]
    DeleteBehavior: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaChangePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaChangePolicy"]:
        if not json_data:
            return None
        return cls(
            UpdateBehavior=json_data.get("UpdateBehavior"),
            DeleteBehavior=json_data.get("DeleteBehavior"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaChangePolicy = SchemaChangePolicy


@dataclass
class RecrawlPolicy(BaseModel):
    RecrawlBehavior: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecrawlPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecrawlPolicy"]:
        if not json_data:
            return None
        return cls(
            RecrawlBehavior=json_data.get("RecrawlBehavior"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecrawlPolicy = RecrawlPolicy


@dataclass
class Targets(BaseModel):
    S3Targets: Optional[Sequence["_S3Target"]]
    CatalogTargets: Optional[Sequence["_CatalogTarget"]]
    DeltaTargets: Optional[Sequence["_DeltaTarget"]]
    MongoDBTargets: Optional[Sequence["_MongoDBTarget"]]
    JdbcTargets: Optional[Sequence["_JdbcTarget"]]
    DynamoDBTargets: Optional[Sequence["_DynamoDBTarget"]]

    @classmethod
    def _deserialize(
        cls: Type["_Targets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Targets"]:
        if not json_data:
            return None
        return cls(
            S3Targets=deserialize_list(json_data.get("S3Targets"), S3Target),
            CatalogTargets=deserialize_list(json_data.get("CatalogTargets"), CatalogTarget),
            DeltaTargets=deserialize_list(json_data.get("DeltaTargets"), DeltaTarget),
            MongoDBTargets=deserialize_list(json_data.get("MongoDBTargets"), MongoDBTarget),
            JdbcTargets=deserialize_list(json_data.get("JdbcTargets"), JdbcTarget),
            DynamoDBTargets=deserialize_list(json_data.get("DynamoDBTargets"), DynamoDBTarget),
        )


# work around possible type aliasing issues when variable has same name as a model
_Targets = Targets


@dataclass
class S3Target(BaseModel):
    ConnectionName: Optional[str]
    Path: Optional[str]
    SampleSize: Optional[int]
    Exclusions: Optional[Sequence[str]]
    DlqEventQueueArn: Optional[str]
    EventQueueArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Target"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Target"]:
        if not json_data:
            return None
        return cls(
            ConnectionName=json_data.get("ConnectionName"),
            Path=json_data.get("Path"),
            SampleSize=json_data.get("SampleSize"),
            Exclusions=json_data.get("Exclusions"),
            DlqEventQueueArn=json_data.get("DlqEventQueueArn"),
            EventQueueArn=json_data.get("EventQueueArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Target = S3Target


@dataclass
class CatalogTarget(BaseModel):
    ConnectionName: Optional[str]
    DatabaseName: Optional[str]
    DlqEventQueueArn: Optional[str]
    Tables: Optional[Sequence[str]]
    EventQueueArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CatalogTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CatalogTarget"]:
        if not json_data:
            return None
        return cls(
            ConnectionName=json_data.get("ConnectionName"),
            DatabaseName=json_data.get("DatabaseName"),
            DlqEventQueueArn=json_data.get("DlqEventQueueArn"),
            Tables=json_data.get("Tables"),
            EventQueueArn=json_data.get("EventQueueArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CatalogTarget = CatalogTarget


@dataclass
class DeltaTarget(BaseModel):
    ConnectionName: Optional[str]
    CreateNativeDeltaTable: Optional[bool]
    WriteManifest: Optional[bool]
    DeltaTables: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DeltaTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeltaTarget"]:
        if not json_data:
            return None
        return cls(
            ConnectionName=json_data.get("ConnectionName"),
            CreateNativeDeltaTable=json_data.get("CreateNativeDeltaTable"),
            WriteManifest=json_data.get("WriteManifest"),
            DeltaTables=json_data.get("DeltaTables"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeltaTarget = DeltaTarget


@dataclass
class MongoDBTarget(BaseModel):
    ConnectionName: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MongoDBTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MongoDBTarget"]:
        if not json_data:
            return None
        return cls(
            ConnectionName=json_data.get("ConnectionName"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MongoDBTarget = MongoDBTarget


@dataclass
class JdbcTarget(BaseModel):
    ConnectionName: Optional[str]
    Path: Optional[str]
    Exclusions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_JdbcTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JdbcTarget"]:
        if not json_data:
            return None
        return cls(
            ConnectionName=json_data.get("ConnectionName"),
            Path=json_data.get("Path"),
            Exclusions=json_data.get("Exclusions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JdbcTarget = JdbcTarget


@dataclass
class DynamoDBTarget(BaseModel):
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DynamoDBTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamoDBTarget"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamoDBTarget = DynamoDBTarget


@dataclass
class Schedule(BaseModel):
    ScheduleExpression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Schedule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Schedule"]:
        if not json_data:
            return None
        return cls(
            ScheduleExpression=json_data.get("ScheduleExpression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Schedule = Schedule


