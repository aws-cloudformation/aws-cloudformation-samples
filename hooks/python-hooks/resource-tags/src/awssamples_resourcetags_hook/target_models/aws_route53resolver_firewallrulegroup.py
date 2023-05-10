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
class AwsRoute53resolverFirewallrulegroup(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]
    Name: Optional[str]
    RuleCount: Optional[int]
    Status: Optional[str]
    StatusMessage: Optional[str]
    OwnerId: Optional[str]
    ShareStatus: Optional[str]
    CreatorRequestId: Optional[str]
    CreationTime: Optional[str]
    ModificationTime: Optional[str]
    FirewallRules: Optional[AbstractSet["_FirewallRule"]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRoute53resolverFirewallrulegroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRoute53resolverFirewallrulegroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            RuleCount=json_data.get("RuleCount"),
            Status=json_data.get("Status"),
            StatusMessage=json_data.get("StatusMessage"),
            OwnerId=json_data.get("OwnerId"),
            ShareStatus=json_data.get("ShareStatus"),
            CreatorRequestId=json_data.get("CreatorRequestId"),
            CreationTime=json_data.get("CreationTime"),
            ModificationTime=json_data.get("ModificationTime"),
            FirewallRules=set_or_none(json_data.get("FirewallRules")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRoute53resolverFirewallrulegroup = AwsRoute53resolverFirewallrulegroup


@dataclass
class FirewallRule(BaseModel):
    FirewallDomainListId: Optional[str]
    Priority: Optional[int]
    Action: Optional[str]
    BlockResponse: Optional[str]
    BlockOverrideDomain: Optional[str]
    BlockOverrideDnsType: Optional[str]
    BlockOverrideTtl: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_FirewallRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FirewallRule"]:
        if not json_data:
            return None
        return cls(
            FirewallDomainListId=json_data.get("FirewallDomainListId"),
            Priority=json_data.get("Priority"),
            Action=json_data.get("Action"),
            BlockResponse=json_data.get("BlockResponse"),
            BlockOverrideDomain=json_data.get("BlockOverrideDomain"),
            BlockOverrideDnsType=json_data.get("BlockOverrideDnsType"),
            BlockOverrideTtl=json_data.get("BlockOverrideTtl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FirewallRule = FirewallRule


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


