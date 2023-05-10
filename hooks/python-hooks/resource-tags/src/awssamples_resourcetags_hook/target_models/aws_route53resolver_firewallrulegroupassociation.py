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
class AwsRoute53resolverFirewallrulegroupassociation(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]
    FirewallRuleGroupId: Optional[str]
    VpcId: Optional[str]
    Name: Optional[str]
    Priority: Optional[int]
    MutationProtection: Optional[str]
    ManagedOwnerName: Optional[str]
    Status: Optional[str]
    StatusMessage: Optional[str]
    CreatorRequestId: Optional[str]
    CreationTime: Optional[str]
    ModificationTime: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRoute53resolverFirewallrulegroupassociation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRoute53resolverFirewallrulegroupassociation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            FirewallRuleGroupId=json_data.get("FirewallRuleGroupId"),
            VpcId=json_data.get("VpcId"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            MutationProtection=json_data.get("MutationProtection"),
            ManagedOwnerName=json_data.get("ManagedOwnerName"),
            Status=json_data.get("Status"),
            StatusMessage=json_data.get("StatusMessage"),
            CreatorRequestId=json_data.get("CreatorRequestId"),
            CreationTime=json_data.get("CreationTime"),
            ModificationTime=json_data.get("ModificationTime"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRoute53resolverFirewallrulegroupassociation = AwsRoute53resolverFirewallrulegroupassociation


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


