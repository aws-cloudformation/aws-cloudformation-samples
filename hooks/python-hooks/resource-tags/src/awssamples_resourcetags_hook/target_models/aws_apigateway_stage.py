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
class AwsApigatewayStage(BaseModel):
    AccessLogSetting: Optional["_AccessLogSetting"]
    CacheClusterEnabled: Optional[bool]
    CacheClusterSize: Optional[str]
    CanarySetting: Optional["_CanarySetting"]
    ClientCertificateId: Optional[str]
    DeploymentId: Optional[str]
    Description: Optional[str]
    DocumentationVersion: Optional[str]
    MethodSettings: Optional[AbstractSet["_MethodSetting"]]
    RestApiId: Optional[str]
    StageName: Optional[str]
    Tags: Optional[Any]
    TracingEnabled: Optional[bool]
    Variables: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayStage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayStage"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AccessLogSetting=AccessLogSetting._deserialize(json_data.get("AccessLogSetting")),
            CacheClusterEnabled=json_data.get("CacheClusterEnabled"),
            CacheClusterSize=json_data.get("CacheClusterSize"),
            CanarySetting=CanarySetting._deserialize(json_data.get("CanarySetting")),
            ClientCertificateId=json_data.get("ClientCertificateId"),
            DeploymentId=json_data.get("DeploymentId"),
            Description=json_data.get("Description"),
            DocumentationVersion=json_data.get("DocumentationVersion"),
            MethodSettings=set_or_none(json_data.get("MethodSettings")),
            RestApiId=json_data.get("RestApiId"),
            StageName=json_data.get("StageName"),
            Tags=json_data.get("Tags"),
            TracingEnabled=json_data.get("TracingEnabled"),
            Variables=json_data.get("Variables"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayStage = AwsApigatewayStage


@dataclass
class AccessLogSetting(BaseModel):
    DestinationArn: Optional[str]
    Format: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessLogSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessLogSetting"]:
        if not json_data:
            return None
        return cls(
            DestinationArn=json_data.get("DestinationArn"),
            Format=json_data.get("Format"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessLogSetting = AccessLogSetting


@dataclass
class CanarySetting(BaseModel):
    DeploymentId: Optional[str]
    PercentTraffic: Optional[float]
    StageVariableOverrides: Optional[MutableMapping[str, str]]
    UseStageCache: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CanarySetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CanarySetting"]:
        if not json_data:
            return None
        return cls(
            DeploymentId=json_data.get("DeploymentId"),
            PercentTraffic=json_data.get("PercentTraffic"),
            StageVariableOverrides=json_data.get("StageVariableOverrides"),
            UseStageCache=json_data.get("UseStageCache"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CanarySetting = CanarySetting


@dataclass
class MethodSetting(BaseModel):
    CacheDataEncrypted: Optional[bool]
    CacheTtlInSeconds: Optional[int]
    CachingEnabled: Optional[bool]
    DataTraceEnabled: Optional[bool]
    HttpMethod: Optional[str]
    LoggingLevel: Optional[str]
    MetricsEnabled: Optional[bool]
    ResourcePath: Optional[str]
    ThrottlingBurstLimit: Optional[int]
    ThrottlingRateLimit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MethodSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MethodSetting"]:
        if not json_data:
            return None
        return cls(
            CacheDataEncrypted=json_data.get("CacheDataEncrypted"),
            CacheTtlInSeconds=json_data.get("CacheTtlInSeconds"),
            CachingEnabled=json_data.get("CachingEnabled"),
            DataTraceEnabled=json_data.get("DataTraceEnabled"),
            HttpMethod=json_data.get("HttpMethod"),
            LoggingLevel=json_data.get("LoggingLevel"),
            MetricsEnabled=json_data.get("MetricsEnabled"),
            ResourcePath=json_data.get("ResourcePath"),
            ThrottlingBurstLimit=json_data.get("ThrottlingBurstLimit"),
            ThrottlingRateLimit=json_data.get("ThrottlingRateLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MethodSetting = MethodSetting


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


