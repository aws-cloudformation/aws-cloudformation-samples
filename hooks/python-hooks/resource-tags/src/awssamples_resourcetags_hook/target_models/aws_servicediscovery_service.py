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
class AwsServicediscoveryService(BaseModel):
    Type: Optional[str]
    Description: Optional[str]
    HealthCheckCustomConfig: Optional["_HealthCheckCustomConfig"]
    DnsConfig: Optional["_DnsConfig"]
    Id: Optional[str]
    NamespaceId: Optional[str]
    HealthCheckConfig: Optional["_HealthCheckConfig"]
    Arn: Optional[str]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsServicediscoveryService"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsServicediscoveryService"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Type=json_data.get("Type"),
            Description=json_data.get("Description"),
            HealthCheckCustomConfig=HealthCheckCustomConfig._deserialize(json_data.get("HealthCheckCustomConfig")),
            DnsConfig=DnsConfig._deserialize(json_data.get("DnsConfig")),
            Id=json_data.get("Id"),
            NamespaceId=json_data.get("NamespaceId"),
            HealthCheckConfig=HealthCheckConfig._deserialize(json_data.get("HealthCheckConfig")),
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsServicediscoveryService = AwsServicediscoveryService


@dataclass
class HealthCheckCustomConfig(BaseModel):
    FailureThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckCustomConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckCustomConfig"]:
        if not json_data:
            return None
        return cls(
            FailureThreshold=json_data.get("FailureThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckCustomConfig = HealthCheckCustomConfig


@dataclass
class DnsConfig(BaseModel):
    DnsRecords: Optional[Sequence["_DnsRecord"]]
    RoutingPolicy: Optional[str]
    NamespaceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnsConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsConfig"]:
        if not json_data:
            return None
        return cls(
            DnsRecords=deserialize_list(json_data.get("DnsRecords"), DnsRecord),
            RoutingPolicy=json_data.get("RoutingPolicy"),
            NamespaceId=json_data.get("NamespaceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsConfig = DnsConfig


@dataclass
class DnsRecord(BaseModel):
    TTL: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnsRecord"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsRecord"]:
        if not json_data:
            return None
        return cls(
            TTL=json_data.get("TTL"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsRecord = DnsRecord


@dataclass
class HealthCheckConfig(BaseModel):
    Type: Optional[str]
    ResourcePath: Optional[str]
    FailureThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckConfig"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            ResourcePath=json_data.get("ResourcePath"),
            FailureThreshold=json_data.get("FailureThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckConfig = HealthCheckConfig


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


