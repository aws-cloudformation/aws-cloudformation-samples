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
class AwsServicediscoveryPrivatednsnamespace(BaseModel):
    Description: Optional[str]
    HostedZoneId: Optional[str]
    Vpc: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    Properties: Optional["_Properties"]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsServicediscoveryPrivatednsnamespace"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsServicediscoveryPrivatednsnamespace"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            HostedZoneId=json_data.get("HostedZoneId"),
            Vpc=json_data.get("Vpc"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Properties=Properties._deserialize(json_data.get("Properties")),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsServicediscoveryPrivatednsnamespace = AwsServicediscoveryPrivatednsnamespace


@dataclass
class Properties(BaseModel):
    DnsProperties: Optional["_PrivateDnsPropertiesMutable"]

    @classmethod
    def _deserialize(
        cls: Type["_Properties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Properties"]:
        if not json_data:
            return None
        return cls(
            DnsProperties=PrivateDnsPropertiesMutable._deserialize(json_data.get("DnsProperties")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Properties = Properties


@dataclass
class PrivateDnsPropertiesMutable(BaseModel):
    SOA: Optional["_SOA"]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateDnsPropertiesMutable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateDnsPropertiesMutable"]:
        if not json_data:
            return None
        return cls(
            SOA=SOA._deserialize(json_data.get("SOA")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateDnsPropertiesMutable = PrivateDnsPropertiesMutable


@dataclass
class SOA(BaseModel):
    TTL: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SOA"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SOA"]:
        if not json_data:
            return None
        return cls(
            TTL=json_data.get("TTL"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SOA = SOA


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


