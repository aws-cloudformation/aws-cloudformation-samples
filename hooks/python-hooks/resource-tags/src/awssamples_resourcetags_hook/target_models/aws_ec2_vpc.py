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
class AwsEc2Vpc(BaseModel):
    VpcId: Optional[str]
    CidrBlock: Optional[str]
    CidrBlockAssociations: Optional[Sequence[str]]
    DefaultNetworkAcl: Optional[str]
    DefaultSecurityGroup: Optional[str]
    Ipv6CidrBlocks: Optional[Sequence[str]]
    EnableDnsHostnames: Optional[bool]
    EnableDnsSupport: Optional[bool]
    InstanceTenancy: Optional[str]
    Ipv4IpamPoolId: Optional[str]
    Ipv4NetmaskLength: Optional[int]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Vpc"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Vpc"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            VpcId=json_data.get("VpcId"),
            CidrBlock=json_data.get("CidrBlock"),
            CidrBlockAssociations=json_data.get("CidrBlockAssociations"),
            DefaultNetworkAcl=json_data.get("DefaultNetworkAcl"),
            DefaultSecurityGroup=json_data.get("DefaultSecurityGroup"),
            Ipv6CidrBlocks=json_data.get("Ipv6CidrBlocks"),
            EnableDnsHostnames=json_data.get("EnableDnsHostnames"),
            EnableDnsSupport=json_data.get("EnableDnsSupport"),
            InstanceTenancy=json_data.get("InstanceTenancy"),
            Ipv4IpamPoolId=json_data.get("Ipv4IpamPoolId"),
            Ipv4NetmaskLength=json_data.get("Ipv4NetmaskLength"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Vpc = AwsEc2Vpc


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


