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
class AwsElasticloadbalancingLoadbalancer(BaseModel):
    SecurityGroups: Optional[Sequence[str]]
    ConnectionDrainingPolicy: Optional["_ConnectionDrainingPolicy"]
    Policies: Optional[Sequence["_Policies"]]
    Scheme: Optional[str]
    AvailabilityZones: Optional[Sequence[str]]
    SourceSecurityGroupOwnerAlias: Optional[str]
    HealthCheck: Optional["_HealthCheck"]
    CanonicalHostedZoneNameID: Optional[str]
    CanonicalHostedZoneName: Optional[str]
    DNSName: Optional[str]
    AccessLoggingPolicy: Optional["_AccessLoggingPolicy"]
    Instances: Optional[Sequence[str]]
    LoadBalancerName: Optional[str]
    Listeners: Optional[Sequence["_Listeners"]]
    Subnets: Optional[Sequence[str]]
    CrossZone: Optional[bool]
    AppCookieStickinessPolicy: Optional[Sequence["_AppCookieStickinessPolicy"]]
    LBCookieStickinessPolicy: Optional[Sequence["_LBCookieStickinessPolicy"]]
    Id: Optional[str]
    SourceSecurityGroupGroupName: Optional[str]
    ConnectionSettings: Optional["_ConnectionSettings"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsElasticloadbalancingLoadbalancer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsElasticloadbalancingLoadbalancer"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            SecurityGroups=json_data.get("SecurityGroups"),
            ConnectionDrainingPolicy=ConnectionDrainingPolicy._deserialize(json_data.get("ConnectionDrainingPolicy")),
            Policies=deserialize_list(json_data.get("Policies"), Policies),
            Scheme=json_data.get("Scheme"),
            AvailabilityZones=json_data.get("AvailabilityZones"),
            SourceSecurityGroupOwnerAlias=json_data.get("SourceSecurityGroupOwnerAlias"),
            HealthCheck=HealthCheck._deserialize(json_data.get("HealthCheck")),
            CanonicalHostedZoneNameID=json_data.get("CanonicalHostedZoneNameID"),
            CanonicalHostedZoneName=json_data.get("CanonicalHostedZoneName"),
            DNSName=json_data.get("DNSName"),
            AccessLoggingPolicy=AccessLoggingPolicy._deserialize(json_data.get("AccessLoggingPolicy")),
            Instances=json_data.get("Instances"),
            LoadBalancerName=json_data.get("LoadBalancerName"),
            Listeners=deserialize_list(json_data.get("Listeners"), Listeners),
            Subnets=json_data.get("Subnets"),
            CrossZone=json_data.get("CrossZone"),
            AppCookieStickinessPolicy=deserialize_list(json_data.get("AppCookieStickinessPolicy"), AppCookieStickinessPolicy),
            LBCookieStickinessPolicy=deserialize_list(json_data.get("LBCookieStickinessPolicy"), LBCookieStickinessPolicy),
            Id=json_data.get("Id"),
            SourceSecurityGroupGroupName=json_data.get("SourceSecurityGroupGroupName"),
            ConnectionSettings=ConnectionSettings._deserialize(json_data.get("ConnectionSettings")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsElasticloadbalancingLoadbalancer = AwsElasticloadbalancingLoadbalancer


@dataclass
class ConnectionDrainingPolicy(BaseModel):
    Enabled: Optional[bool]
    Timeout: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionDrainingPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionDrainingPolicy"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionDrainingPolicy = ConnectionDrainingPolicy


@dataclass
class Policies(BaseModel):
    Attributes: Optional[Sequence[MutableMapping[str, Any]]]
    PolicyType: Optional[str]
    LoadBalancerPorts: Optional[Sequence[str]]
    PolicyName: Optional[str]
    InstancePorts: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Policies"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Policies"]:
        if not json_data:
            return None
        return cls(
            Attributes=json_data.get("Attributes"),
            PolicyType=json_data.get("PolicyType"),
            LoadBalancerPorts=json_data.get("LoadBalancerPorts"),
            PolicyName=json_data.get("PolicyName"),
            InstancePorts=json_data.get("InstancePorts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Policies = Policies


@dataclass
class HealthCheck(BaseModel):
    Target: Optional[str]
    UnhealthyThreshold: Optional[str]
    Timeout: Optional[str]
    HealthyThreshold: Optional[str]
    Interval: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheck"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheck"]:
        if not json_data:
            return None
        return cls(
            Target=json_data.get("Target"),
            UnhealthyThreshold=json_data.get("UnhealthyThreshold"),
            Timeout=json_data.get("Timeout"),
            HealthyThreshold=json_data.get("HealthyThreshold"),
            Interval=json_data.get("Interval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheck = HealthCheck


@dataclass
class AccessLoggingPolicy(BaseModel):
    Enabled: Optional[bool]
    S3BucketName: Optional[str]
    EmitInterval: Optional[int]
    S3BucketPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessLoggingPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessLoggingPolicy"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            S3BucketName=json_data.get("S3BucketName"),
            EmitInterval=json_data.get("EmitInterval"),
            S3BucketPrefix=json_data.get("S3BucketPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessLoggingPolicy = AccessLoggingPolicy


@dataclass
class Listeners(BaseModel):
    PolicyNames: Optional[Sequence[str]]
    InstancePort: Optional[str]
    LoadBalancerPort: Optional[str]
    Protocol: Optional[str]
    SSLCertificateId: Optional[str]
    InstanceProtocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Listeners"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Listeners"]:
        if not json_data:
            return None
        return cls(
            PolicyNames=json_data.get("PolicyNames"),
            InstancePort=json_data.get("InstancePort"),
            LoadBalancerPort=json_data.get("LoadBalancerPort"),
            Protocol=json_data.get("Protocol"),
            SSLCertificateId=json_data.get("SSLCertificateId"),
            InstanceProtocol=json_data.get("InstanceProtocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Listeners = Listeners


@dataclass
class AppCookieStickinessPolicy(BaseModel):
    CookieName: Optional[str]
    PolicyName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AppCookieStickinessPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppCookieStickinessPolicy"]:
        if not json_data:
            return None
        return cls(
            CookieName=json_data.get("CookieName"),
            PolicyName=json_data.get("PolicyName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppCookieStickinessPolicy = AppCookieStickinessPolicy


@dataclass
class LBCookieStickinessPolicy(BaseModel):
    CookieExpirationPeriod: Optional[str]
    PolicyName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LBCookieStickinessPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LBCookieStickinessPolicy"]:
        if not json_data:
            return None
        return cls(
            CookieExpirationPeriod=json_data.get("CookieExpirationPeriod"),
            PolicyName=json_data.get("PolicyName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LBCookieStickinessPolicy = LBCookieStickinessPolicy


@dataclass
class ConnectionSettings(BaseModel):
    IdleTimeout: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionSettings"]:
        if not json_data:
            return None
        return cls(
            IdleTimeout=json_data.get("IdleTimeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionSettings = ConnectionSettings


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


