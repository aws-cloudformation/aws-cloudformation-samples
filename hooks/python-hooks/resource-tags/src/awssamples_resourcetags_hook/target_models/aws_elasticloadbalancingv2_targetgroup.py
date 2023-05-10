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
class AwsElasticloadbalancingv2Targetgroup(BaseModel):
    IpAddressType: Optional[str]
    HealthCheckIntervalSeconds: Optional[int]
    LoadBalancerArns: Optional[Sequence[str]]
    Matcher: Optional["_Matcher"]
    HealthCheckPath: Optional[str]
    Port: Optional[int]
    Targets: Optional[AbstractSet["_TargetDescription"]]
    HealthCheckEnabled: Optional[bool]
    ProtocolVersion: Optional[str]
    UnhealthyThresholdCount: Optional[int]
    HealthCheckTimeoutSeconds: Optional[int]
    Name: Optional[str]
    VpcId: Optional[str]
    TargetGroupFullName: Optional[str]
    HealthyThresholdCount: Optional[int]
    HealthCheckProtocol: Optional[str]
    TargetGroupAttributes: Optional[AbstractSet["_TargetGroupAttribute"]]
    TargetType: Optional[str]
    HealthCheckPort: Optional[str]
    TargetGroupArn: Optional[str]
    Protocol: Optional[str]
    TargetGroupName: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsElasticloadbalancingv2Targetgroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsElasticloadbalancingv2Targetgroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            IpAddressType=json_data.get("IpAddressType"),
            HealthCheckIntervalSeconds=json_data.get("HealthCheckIntervalSeconds"),
            LoadBalancerArns=json_data.get("LoadBalancerArns"),
            Matcher=Matcher._deserialize(json_data.get("Matcher")),
            HealthCheckPath=json_data.get("HealthCheckPath"),
            Port=json_data.get("Port"),
            Targets=set_or_none(json_data.get("Targets")),
            HealthCheckEnabled=json_data.get("HealthCheckEnabled"),
            ProtocolVersion=json_data.get("ProtocolVersion"),
            UnhealthyThresholdCount=json_data.get("UnhealthyThresholdCount"),
            HealthCheckTimeoutSeconds=json_data.get("HealthCheckTimeoutSeconds"),
            Name=json_data.get("Name"),
            VpcId=json_data.get("VpcId"),
            TargetGroupFullName=json_data.get("TargetGroupFullName"),
            HealthyThresholdCount=json_data.get("HealthyThresholdCount"),
            HealthCheckProtocol=json_data.get("HealthCheckProtocol"),
            TargetGroupAttributes=set_or_none(json_data.get("TargetGroupAttributes")),
            TargetType=json_data.get("TargetType"),
            HealthCheckPort=json_data.get("HealthCheckPort"),
            TargetGroupArn=json_data.get("TargetGroupArn"),
            Protocol=json_data.get("Protocol"),
            TargetGroupName=json_data.get("TargetGroupName"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsElasticloadbalancingv2Targetgroup = AwsElasticloadbalancingv2Targetgroup


@dataclass
class Matcher(BaseModel):
    GrpcCode: Optional[str]
    HttpCode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Matcher"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Matcher"]:
        if not json_data:
            return None
        return cls(
            GrpcCode=json_data.get("GrpcCode"),
            HttpCode=json_data.get("HttpCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Matcher = Matcher


@dataclass
class TargetDescription(BaseModel):
    AvailabilityZone: Optional[str]
    Id: Optional[str]
    Port: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_TargetDescription"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetDescription"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Id=json_data.get("Id"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetDescription = TargetDescription


@dataclass
class TargetGroupAttribute(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetGroupAttribute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetGroupAttribute"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetGroupAttribute = TargetGroupAttribute


@dataclass
class Tag(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


