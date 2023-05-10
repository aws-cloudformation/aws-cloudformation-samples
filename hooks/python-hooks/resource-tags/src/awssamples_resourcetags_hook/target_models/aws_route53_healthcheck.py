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
class AwsRoute53Healthcheck(BaseModel):
    HealthCheckId: Optional[str]
    HealthCheckConfig: Optional["_HealthCheckConfig"]
    HealthCheckTags: Optional[AbstractSet["_HealthCheckTag"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRoute53Healthcheck"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRoute53Healthcheck"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            HealthCheckId=json_data.get("HealthCheckId"),
            HealthCheckConfig=HealthCheckConfig._deserialize(json_data.get("HealthCheckConfig")),
            HealthCheckTags=set_or_none(json_data.get("HealthCheckTags")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRoute53Healthcheck = AwsRoute53Healthcheck


@dataclass
class HealthCheckConfig(BaseModel):
    AlarmIdentifier: Optional["_AlarmIdentifier"]
    ChildHealthChecks: Optional[Sequence[str]]
    EnableSNI: Optional[bool]
    FailureThreshold: Optional[int]
    FullyQualifiedDomainName: Optional[str]
    HealthThreshold: Optional[int]
    InsufficientDataHealthStatus: Optional[str]
    Inverted: Optional[bool]
    IPAddress: Optional[str]
    MeasureLatency: Optional[bool]
    Port: Optional[int]
    Regions: Optional[Sequence[str]]
    RequestInterval: Optional[int]
    ResourcePath: Optional[str]
    SearchString: Optional[str]
    RoutingControlArn: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckConfig"]:
        if not json_data:
            return None
        return cls(
            AlarmIdentifier=AlarmIdentifier._deserialize(json_data.get("AlarmIdentifier")),
            ChildHealthChecks=json_data.get("ChildHealthChecks"),
            EnableSNI=json_data.get("EnableSNI"),
            FailureThreshold=json_data.get("FailureThreshold"),
            FullyQualifiedDomainName=json_data.get("FullyQualifiedDomainName"),
            HealthThreshold=json_data.get("HealthThreshold"),
            InsufficientDataHealthStatus=json_data.get("InsufficientDataHealthStatus"),
            Inverted=json_data.get("Inverted"),
            IPAddress=json_data.get("IPAddress"),
            MeasureLatency=json_data.get("MeasureLatency"),
            Port=json_data.get("Port"),
            Regions=json_data.get("Regions"),
            RequestInterval=json_data.get("RequestInterval"),
            ResourcePath=json_data.get("ResourcePath"),
            SearchString=json_data.get("SearchString"),
            RoutingControlArn=json_data.get("RoutingControlArn"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckConfig = HealthCheckConfig


@dataclass
class AlarmIdentifier(BaseModel):
    Name: Optional[str]
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AlarmIdentifier"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlarmIdentifier"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlarmIdentifier = AlarmIdentifier


@dataclass
class HealthCheckTag(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckTag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckTag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckTag = HealthCheckTag


