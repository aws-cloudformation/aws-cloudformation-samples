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
class AwsEc2Networkinterface(BaseModel):
    Description: Optional[str]
    PrivateIpAddress: Optional[str]
    PrivateIpAddresses: Optional[Sequence["_PrivateIpAddressSpecification"]]
    SecondaryPrivateIpAddressCount: Optional[int]
    Ipv6PrefixCount: Optional[int]
    PrimaryPrivateIpAddress: Optional[str]
    Ipv4Prefixes: Optional[Sequence["_Ipv4PrefixSpecification"]]
    Ipv4PrefixCount: Optional[int]
    GroupSet: Optional[Sequence[str]]
    Ipv6Addresses: Optional[AbstractSet["_InstanceIpv6Address"]]
    Ipv6Prefixes: Optional[Sequence["_Ipv6PrefixSpecification"]]
    SubnetId: Optional[str]
    SourceDestCheck: Optional[bool]
    InterfaceType: Optional[str]
    SecondaryPrivateIpAddresses: Optional[Sequence[str]]
    Ipv6AddressCount: Optional[int]
    Id: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Networkinterface"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Networkinterface"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            PrivateIpAddresses=deserialize_list(json_data.get("PrivateIpAddresses"), PrivateIpAddressSpecification),
            SecondaryPrivateIpAddressCount=json_data.get("SecondaryPrivateIpAddressCount"),
            Ipv6PrefixCount=json_data.get("Ipv6PrefixCount"),
            PrimaryPrivateIpAddress=json_data.get("PrimaryPrivateIpAddress"),
            Ipv4Prefixes=deserialize_list(json_data.get("Ipv4Prefixes"), Ipv4PrefixSpecification),
            Ipv4PrefixCount=json_data.get("Ipv4PrefixCount"),
            GroupSet=json_data.get("GroupSet"),
            Ipv6Addresses=set_or_none(json_data.get("Ipv6Addresses")),
            Ipv6Prefixes=deserialize_list(json_data.get("Ipv6Prefixes"), Ipv6PrefixSpecification),
            SubnetId=json_data.get("SubnetId"),
            SourceDestCheck=json_data.get("SourceDestCheck"),
            InterfaceType=json_data.get("InterfaceType"),
            SecondaryPrivateIpAddresses=json_data.get("SecondaryPrivateIpAddresses"),
            Ipv6AddressCount=json_data.get("Ipv6AddressCount"),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Networkinterface = AwsEc2Networkinterface


@dataclass
class PrivateIpAddressSpecification(BaseModel):
    PrivateIpAddress: Optional[str]
    Primary: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateIpAddressSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateIpAddressSpecification"]:
        if not json_data:
            return None
        return cls(
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            Primary=json_data.get("Primary"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateIpAddressSpecification = PrivateIpAddressSpecification


@dataclass
class Ipv4PrefixSpecification(BaseModel):
    Ipv4Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv4PrefixSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv4PrefixSpecification"]:
        if not json_data:
            return None
        return cls(
            Ipv4Prefix=json_data.get("Ipv4Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv4PrefixSpecification = Ipv4PrefixSpecification


@dataclass
class InstanceIpv6Address(BaseModel):
    Ipv6Address: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceIpv6Address"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceIpv6Address"]:
        if not json_data:
            return None
        return cls(
            Ipv6Address=json_data.get("Ipv6Address"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceIpv6Address = InstanceIpv6Address


@dataclass
class Ipv6PrefixSpecification(BaseModel):
    Ipv6Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ipv6PrefixSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ipv6PrefixSpecification"]:
        if not json_data:
            return None
        return cls(
            Ipv6Prefix=json_data.get("Ipv6Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ipv6PrefixSpecification = Ipv6PrefixSpecification


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


