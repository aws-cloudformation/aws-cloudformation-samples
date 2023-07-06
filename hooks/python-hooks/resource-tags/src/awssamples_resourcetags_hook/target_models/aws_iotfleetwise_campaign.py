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
class AwsIotfleetwiseCampaign(BaseModel):
    Status: Optional[str]
    Action: Optional[str]
    CreationTime: Optional[str]
    Compression: Optional[str]
    Description: Optional[str]
    Priority: Optional[int]
    SignalsToCollect: Optional[Sequence["_SignalInformation"]]
    DataDestinationConfigs: Optional[Sequence["_DataDestinationConfig"]]
    StartTime: Optional[str]
    Name: Optional[str]
    ExpiryTime: Optional[str]
    LastModificationTime: Optional[str]
    SpoolingMode: Optional[str]
    SignalCatalogArn: Optional[str]
    PostTriggerCollectionDuration: Optional[float]
    DataExtraDimensions: Optional[Sequence[str]]
    DiagnosticsMode: Optional[str]
    TargetArn: Optional[str]
    Arn: Optional[str]
    CollectionScheme: Optional["_CollectionScheme"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotfleetwiseCampaign"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotfleetwiseCampaign"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Status=json_data.get("Status"),
            Action=json_data.get("Action"),
            CreationTime=json_data.get("CreationTime"),
            Compression=json_data.get("Compression"),
            Description=json_data.get("Description"),
            Priority=json_data.get("Priority"),
            SignalsToCollect=deserialize_list(json_data.get("SignalsToCollect"), SignalInformation),
            DataDestinationConfigs=deserialize_list(json_data.get("DataDestinationConfigs"), DataDestinationConfig),
            StartTime=json_data.get("StartTime"),
            Name=json_data.get("Name"),
            ExpiryTime=json_data.get("ExpiryTime"),
            LastModificationTime=json_data.get("LastModificationTime"),
            SpoolingMode=json_data.get("SpoolingMode"),
            SignalCatalogArn=json_data.get("SignalCatalogArn"),
            PostTriggerCollectionDuration=json_data.get("PostTriggerCollectionDuration"),
            DataExtraDimensions=json_data.get("DataExtraDimensions"),
            DiagnosticsMode=json_data.get("DiagnosticsMode"),
            TargetArn=json_data.get("TargetArn"),
            Arn=json_data.get("Arn"),
            CollectionScheme=CollectionScheme._deserialize(json_data.get("CollectionScheme")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotfleetwiseCampaign = AwsIotfleetwiseCampaign


@dataclass
class SignalInformation(BaseModel):
    MaxSampleCount: Optional[float]
    Name: Optional[str]
    MinimumSamplingIntervalMs: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SignalInformation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SignalInformation"]:
        if not json_data:
            return None
        return cls(
            MaxSampleCount=json_data.get("MaxSampleCount"),
            Name=json_data.get("Name"),
            MinimumSamplingIntervalMs=json_data.get("MinimumSamplingIntervalMs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SignalInformation = SignalInformation


@dataclass
class DataDestinationConfig(BaseModel):
    S3Config: Optional["_S3Config"]
    TimestreamConfig: Optional["_TimestreamConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_DataDestinationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDestinationConfig"]:
        if not json_data:
            return None
        return cls(
            S3Config=S3Config._deserialize(json_data.get("S3Config")),
            TimestreamConfig=TimestreamConfig._deserialize(json_data.get("TimestreamConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDestinationConfig = DataDestinationConfig


@dataclass
class S3Config(BaseModel):
    BucketArn: Optional[str]
    DataFormat: Optional[str]
    StorageCompressionFormat: Optional[str]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Config"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Config"]:
        if not json_data:
            return None
        return cls(
            BucketArn=json_data.get("BucketArn"),
            DataFormat=json_data.get("DataFormat"),
            StorageCompressionFormat=json_data.get("StorageCompressionFormat"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Config = S3Config


@dataclass
class TimestreamConfig(BaseModel):
    TimestreamTableArn: Optional[str]
    ExecutionRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimestreamConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimestreamConfig"]:
        if not json_data:
            return None
        return cls(
            TimestreamTableArn=json_data.get("TimestreamTableArn"),
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimestreamConfig = TimestreamConfig


@dataclass
class CollectionScheme(BaseModel):
    TimeBasedCollectionScheme: Optional["_TimeBasedCollectionScheme"]
    ConditionBasedCollectionScheme: Optional["_ConditionBasedCollectionScheme"]

    @classmethod
    def _deserialize(
        cls: Type["_CollectionScheme"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CollectionScheme"]:
        if not json_data:
            return None
        return cls(
            TimeBasedCollectionScheme=TimeBasedCollectionScheme._deserialize(json_data.get("TimeBasedCollectionScheme")),
            ConditionBasedCollectionScheme=ConditionBasedCollectionScheme._deserialize(json_data.get("ConditionBasedCollectionScheme")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CollectionScheme = CollectionScheme


@dataclass
class TimeBasedCollectionScheme(BaseModel):
    PeriodMs: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TimeBasedCollectionScheme"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeBasedCollectionScheme"]:
        if not json_data:
            return None
        return cls(
            PeriodMs=json_data.get("PeriodMs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeBasedCollectionScheme = TimeBasedCollectionScheme


@dataclass
class ConditionBasedCollectionScheme(BaseModel):
    MinimumTriggerIntervalMs: Optional[float]
    Expression: Optional[str]
    TriggerMode: Optional[str]
    ConditionLanguageVersion: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionBasedCollectionScheme"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionBasedCollectionScheme"]:
        if not json_data:
            return None
        return cls(
            MinimumTriggerIntervalMs=json_data.get("MinimumTriggerIntervalMs"),
            Expression=json_data.get("Expression"),
            TriggerMode=json_data.get("TriggerMode"),
            ConditionLanguageVersion=json_data.get("ConditionLanguageVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionBasedCollectionScheme = ConditionBasedCollectionScheme


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


