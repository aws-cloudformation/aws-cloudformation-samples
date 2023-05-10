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
class AwsGlobalacceleratorAccelerator(BaseModel):
    Name: Optional[str]
    IpAddressType: Optional[str]
    IpAddresses: Optional[Sequence[str]]
    Enabled: Optional[bool]
    DnsName: Optional[str]
    Ipv4Addresses: Optional[Sequence[str]]
    Ipv6Addresses: Optional[Sequence[str]]
    DualStackDnsName: Optional[str]
    AcceleratorArn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGlobalacceleratorAccelerator"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGlobalacceleratorAccelerator"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            IpAddressType=json_data.get("IpAddressType"),
            IpAddresses=json_data.get("IpAddresses"),
            Enabled=json_data.get("Enabled"),
            DnsName=json_data.get("DnsName"),
            Ipv4Addresses=json_data.get("Ipv4Addresses"),
            Ipv6Addresses=json_data.get("Ipv6Addresses"),
            DualStackDnsName=json_data.get("DualStackDnsName"),
            AcceleratorArn=json_data.get("AcceleratorArn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGlobalacceleratorAccelerator = AwsGlobalacceleratorAccelerator


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


