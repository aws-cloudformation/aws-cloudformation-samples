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
    PrimaryPrivateIpAddress: Optional[str]
    EnablePrimaryIpv6: Optional[bool]
    GroupSet: Optional[Sequence[str]]
    Ipv6Addresses: Optional[AbstractSet["_InstanceIpv6Address"]]
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
            PrimaryPrivateIpAddress=json_data.get("PrimaryPrivateIpAddress"),
            EnablePrimaryIpv6=json_data.get("EnablePrimaryIpv6"),
            GroupSet=json_data.get("GroupSet"),
            Ipv6Addresses=set_or_none(json_data.get("Ipv6Addresses")),
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


