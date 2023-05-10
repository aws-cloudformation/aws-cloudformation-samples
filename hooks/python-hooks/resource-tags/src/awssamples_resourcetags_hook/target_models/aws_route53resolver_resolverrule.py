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
class AwsRoute53resolverResolverrule(BaseModel):
    ResolverEndpointId: Optional[str]
    DomainName: Optional[str]
    Name: Optional[str]
    RuleType: Optional[str]
    Tags: Optional[Any]
    TargetIps: Optional[Sequence["_TargetAddress"]]
    Arn: Optional[str]
    ResolverRuleId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRoute53resolverResolverrule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRoute53resolverResolverrule"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ResolverEndpointId=json_data.get("ResolverEndpointId"),
            DomainName=json_data.get("DomainName"),
            Name=json_data.get("Name"),
            RuleType=json_data.get("RuleType"),
            Tags=json_data.get("Tags"),
            TargetIps=deserialize_list(json_data.get("TargetIps"), TargetAddress),
            Arn=json_data.get("Arn"),
            ResolverRuleId=json_data.get("ResolverRuleId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRoute53resolverResolverrule = AwsRoute53resolverResolverrule


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


@dataclass
class TargetAddress(BaseModel):
    Ip: Optional[str]
    Ipv6: Optional[str]
    Port: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetAddress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetAddress"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            Ipv6=json_data.get("Ipv6"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetAddress = TargetAddress


