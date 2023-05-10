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
class AwsApigatewayv2Stage(BaseModel):
    DeploymentId: Optional[str]
    Description: Optional[str]
    AutoDeploy: Optional[bool]
    RouteSettings: Optional[MutableMapping[str, Any]]
    StageName: Optional[str]
    StageVariables: Optional[MutableMapping[str, Any]]
    AccessPolicyId: Optional[str]
    ClientCertificateId: Optional[str]
    AccessLogSettings: Optional["_AccessLogSettings"]
    Id: Optional[str]
    ApiId: Optional[str]
    DefaultRouteSettings: Optional["_RouteSettings"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayv2Stage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayv2Stage"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DeploymentId=json_data.get("DeploymentId"),
            Description=json_data.get("Description"),
            AutoDeploy=json_data.get("AutoDeploy"),
            RouteSettings=json_data.get("RouteSettings"),
            StageName=json_data.get("StageName"),
            StageVariables=json_data.get("StageVariables"),
            AccessPolicyId=json_data.get("AccessPolicyId"),
            ClientCertificateId=json_data.get("ClientCertificateId"),
            AccessLogSettings=AccessLogSettings._deserialize(json_data.get("AccessLogSettings")),
            Id=json_data.get("Id"),
            ApiId=json_data.get("ApiId"),
            DefaultRouteSettings=RouteSettings._deserialize(json_data.get("DefaultRouteSettings")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayv2Stage = AwsApigatewayv2Stage


@dataclass
class AccessLogSettings(BaseModel):
    DestinationArn: Optional[str]
    Format: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessLogSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessLogSettings"]:
        if not json_data:
            return None
        return cls(
            DestinationArn=json_data.get("DestinationArn"),
            Format=json_data.get("Format"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessLogSettings = AccessLogSettings


@dataclass
class RouteSettings(BaseModel):
    DetailedMetricsEnabled: Optional[bool]
    LoggingLevel: Optional[str]
    DataTraceEnabled: Optional[bool]
    ThrottlingBurstLimit: Optional[int]
    ThrottlingRateLimit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RouteSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteSettings"]:
        if not json_data:
            return None
        return cls(
            DetailedMetricsEnabled=json_data.get("DetailedMetricsEnabled"),
            LoggingLevel=json_data.get("LoggingLevel"),
            DataTraceEnabled=json_data.get("DataTraceEnabled"),
            ThrottlingBurstLimit=json_data.get("ThrottlingBurstLimit"),
            ThrottlingRateLimit=json_data.get("ThrottlingRateLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteSettings = RouteSettings


