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
    ResolverEndpointId: Optional[str]
    Protocols: Optional[Sequence[str]]
    OutpostArn: Optional[str]
    ResolverEndpointType: Optional[str]
    Direction: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    Name: Optional[str]
    IpAddresses: Optional[Sequence["_IpAddressRequest"]]
    IpAddressCount: Optional[str]
    PreferredInstanceType: Optional[str]
    Arn: Optional[str]
    HostVPCId: Optional[str]
    Tags: Optional[Any]

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
            ResolverEndpointId=json_data.get("ResolverEndpointId"),
            Protocols=json_data.get("Protocols"),
            OutpostArn=json_data.get("OutpostArn"),
            ResolverEndpointType=json_data.get("ResolverEndpointType"),
            Direction=json_data.get("Direction"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            Name=json_data.get("Name"),
            IpAddresses=deserialize_list(json_data.get("IpAddresses"), IpAddressRequest),
            IpAddressCount=json_data.get("IpAddressCount"),
            PreferredInstanceType=json_data.get("PreferredInstanceType"),
            Arn=json_data.get("Arn"),
            HostVPCId=json_data.get("HostVPCId"),
            Tags=json_data.get("Tags"),
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


