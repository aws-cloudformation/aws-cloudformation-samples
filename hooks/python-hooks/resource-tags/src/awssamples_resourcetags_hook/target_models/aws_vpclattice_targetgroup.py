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
class AwsVpclatticeTargetgroup(BaseModel):
    Arn: Optional[str]
    Config: Optional["_TargetGroupConfig"]
    CreatedAt: Optional[str]
    Id: Optional[str]
    LastUpdatedAt: Optional[str]
    Name: Optional[str]
    Status: Optional[str]
    Type: Optional[str]
    Targets: Optional[Sequence["_Target"]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsVpclatticeTargetgroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsVpclatticeTargetgroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Config=TargetGroupConfig._deserialize(json_data.get("Config")),
            CreatedAt=json_data.get("CreatedAt"),
            Id=json_data.get("Id"),
            LastUpdatedAt=json_data.get("LastUpdatedAt"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
            Targets=deserialize_list(json_data.get("Targets"), Target),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsVpclatticeTargetgroup = AwsVpclatticeTargetgroup


@dataclass
class TargetGroupConfig(BaseModel):
    Port: Optional[int]
    Protocol: Optional[str]
    ProtocolVersion: Optional[str]
    IpAddressType: Optional[str]
    VpcIdentifier: Optional[str]
    HealthCheck: Optional["_HealthCheckConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_TargetGroupConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetGroupConfig"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            ProtocolVersion=json_data.get("ProtocolVersion"),
            IpAddressType=json_data.get("IpAddressType"),
            VpcIdentifier=json_data.get("VpcIdentifier"),
            HealthCheck=HealthCheckConfig._deserialize(json_data.get("HealthCheck")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetGroupConfig = TargetGroupConfig


@dataclass
class HealthCheckConfig(BaseModel):
    Enabled: Optional[bool]
    Protocol: Optional[str]
    ProtocolVersion: Optional[str]
    Port: Optional[int]
    Path: Optional[str]
    HealthCheckIntervalSeconds: Optional[int]
    HealthCheckTimeoutSeconds: Optional[int]
    HealthyThresholdCount: Optional[int]
    UnhealthyThresholdCount: Optional[int]
    Matcher: Optional["_Matcher"]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckConfig"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Protocol=json_data.get("Protocol"),
            ProtocolVersion=json_data.get("ProtocolVersion"),
            Port=json_data.get("Port"),
            Path=json_data.get("Path"),
            HealthCheckIntervalSeconds=json_data.get("HealthCheckIntervalSeconds"),
            HealthCheckTimeoutSeconds=json_data.get("HealthCheckTimeoutSeconds"),
            HealthyThresholdCount=json_data.get("HealthyThresholdCount"),
            UnhealthyThresholdCount=json_data.get("UnhealthyThresholdCount"),
            Matcher=Matcher._deserialize(json_data.get("Matcher")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckConfig = HealthCheckConfig


@dataclass
class Matcher(BaseModel):
    HttpCode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Matcher"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Matcher"]:
        if not json_data:
            return None
        return cls(
            HttpCode=json_data.get("HttpCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Matcher = Matcher


@dataclass
class Target(BaseModel):
    Id: Optional[str]
    Port: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Target"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Target"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Target = Target


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


