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
class AwsRoute53resolverResolverendpoint(BaseModel):
    IpAddresses: Optional[Sequence["_IpAddressRequest"]]
    ResolverEndpointId: Optional[str]
    IpAddressCount: Optional[str]
    OutpostArn: Optional[str]
    PreferredInstanceType: Optional[str]
    ResolverEndpointType: Optional[str]
    Arn: Optional[str]
    Direction: Optional[str]
    HostVPCId: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRoute53resolverResolverendpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRoute53resolverResolverendpoint"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            IpAddresses=deserialize_list(json_data.get("IpAddresses"), IpAddressRequest),
            ResolverEndpointId=json_data.get("ResolverEndpointId"),
            IpAddressCount=json_data.get("IpAddressCount"),
            OutpostArn=json_data.get("OutpostArn"),
            PreferredInstanceType=json_data.get("PreferredInstanceType"),
            ResolverEndpointType=json_data.get("ResolverEndpointType"),
            Arn=json_data.get("Arn"),
            Direction=json_data.get("Direction"),
            HostVPCId=json_data.get("HostVPCId"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRoute53resolverResolverendpoint = AwsRoute53resolverResolverendpoint


@dataclass
class IpAddressRequest(BaseModel):
    SubnetId: Optional[str]
    Ipv6: Optional[str]
    Ip: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddressRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddressRequest"]:
        if not json_data:
            return None
        return cls(
            SubnetId=json_data.get("SubnetId"),
            Ipv6=json_data.get("Ipv6"),
            Ip=json_data.get("Ip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddressRequest = IpAddressRequest


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


