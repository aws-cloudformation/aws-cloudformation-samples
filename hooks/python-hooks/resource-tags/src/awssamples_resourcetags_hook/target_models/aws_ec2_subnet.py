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
class AwsEc2Subnet(BaseModel):
    AssignIpv6AddressOnCreation: Optional[bool]
    VpcId: Optional[str]
    MapPublicIpOnLaunch: Optional[bool]
    NetworkAclAssociationId: Optional[str]
    AvailabilityZone: Optional[str]
    AvailabilityZoneId: Optional[str]
    CidrBlock: Optional[str]
    SubnetId: Optional[str]
    Ipv6CidrBlocks: Optional[Sequence[str]]
    Ipv6CidrBlock: Optional[str]
    OutpostArn: Optional[str]
    Ipv6Native: Optional[bool]
    EnableDns64: Optional[bool]
    PrivateDnsNameOptionsOnLaunch: Optional["_PrivateDnsNameOptionsOnLaunch"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Subnet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Subnet"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AssignIpv6AddressOnCreation=json_data.get("AssignIpv6AddressOnCreation"),
            VpcId=json_data.get("VpcId"),
            MapPublicIpOnLaunch=json_data.get("MapPublicIpOnLaunch"),
            NetworkAclAssociationId=json_data.get("NetworkAclAssociationId"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            AvailabilityZoneId=json_data.get("AvailabilityZoneId"),
            CidrBlock=json_data.get("CidrBlock"),
            SubnetId=json_data.get("SubnetId"),
            Ipv6CidrBlocks=json_data.get("Ipv6CidrBlocks"),
            Ipv6CidrBlock=json_data.get("Ipv6CidrBlock"),
            OutpostArn=json_data.get("OutpostArn"),
            Ipv6Native=json_data.get("Ipv6Native"),
            EnableDns64=json_data.get("EnableDns64"),
            PrivateDnsNameOptionsOnLaunch=PrivateDnsNameOptionsOnLaunch._deserialize(json_data.get("PrivateDnsNameOptionsOnLaunch")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Subnet = AwsEc2Subnet


@dataclass
class PrivateDnsNameOptionsOnLaunch(BaseModel):
    HostnameType: Optional[str]
    EnableResourceNameDnsARecord: Optional[bool]
    EnableResourceNameDnsAAAARecord: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateDnsNameOptionsOnLaunch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateDnsNameOptionsOnLaunch"]:
        if not json_data:
            return None
        return cls(
            HostnameType=json_data.get("HostnameType"),
            EnableResourceNameDnsARecord=json_data.get("EnableResourceNameDnsARecord"),
            EnableResourceNameDnsAAAARecord=json_data.get("EnableResourceNameDnsAAAARecord"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateDnsNameOptionsOnLaunch = PrivateDnsNameOptionsOnLaunch


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


