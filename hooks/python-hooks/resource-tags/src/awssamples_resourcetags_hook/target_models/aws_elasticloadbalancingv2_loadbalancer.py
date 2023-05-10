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
class AwsElasticloadbalancingv2Loadbalancer(BaseModel):
    IpAddressType: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    LoadBalancerAttributes: Optional[Sequence["_LoadBalancerAttribute"]]
    Scheme: Optional[str]
    DNSName: Optional[str]
    Name: Optional[str]
    LoadBalancerName: Optional[str]
    Subnets: Optional[Sequence[str]]
    Type: Optional[str]
    CanonicalHostedZoneID: Optional[str]
    Id: Optional[str]
    Tags: Optional[Any]
    LoadBalancerFullName: Optional[str]
    SubnetMappings: Optional[Sequence["_SubnetMapping"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsElasticloadbalancingv2Loadbalancer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsElasticloadbalancingv2Loadbalancer"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            IpAddressType=json_data.get("IpAddressType"),
            SecurityGroups=json_data.get("SecurityGroups"),
            LoadBalancerAttributes=deserialize_list(json_data.get("LoadBalancerAttributes"), LoadBalancerAttribute),
            Scheme=json_data.get("Scheme"),
            DNSName=json_data.get("DNSName"),
            Name=json_data.get("Name"),
            LoadBalancerName=json_data.get("LoadBalancerName"),
            Subnets=json_data.get("Subnets"),
            Type=json_data.get("Type"),
            CanonicalHostedZoneID=json_data.get("CanonicalHostedZoneID"),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
            LoadBalancerFullName=json_data.get("LoadBalancerFullName"),
            SubnetMappings=deserialize_list(json_data.get("SubnetMappings"), SubnetMapping),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsElasticloadbalancingv2Loadbalancer = AwsElasticloadbalancingv2Loadbalancer


@dataclass
class LoadBalancerAttribute(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancerAttribute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancerAttribute"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancerAttribute = LoadBalancerAttribute


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


@dataclass
class SubnetMapping(BaseModel):
    IPv6Address: Optional[str]
    SubnetId: Optional[str]
    AllocationId: Optional[str]
    PrivateIPv4Address: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetMapping"]:
        if not json_data:
            return None
        return cls(
            IPv6Address=json_data.get("IPv6Address"),
            SubnetId=json_data.get("SubnetId"),
            AllocationId=json_data.get("AllocationId"),
            PrivateIPv4Address=json_data.get("PrivateIPv4Address"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetMapping = SubnetMapping


