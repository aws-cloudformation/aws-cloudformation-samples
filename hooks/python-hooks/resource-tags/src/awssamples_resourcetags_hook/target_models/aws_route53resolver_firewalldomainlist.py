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
class AwsRoute53resolverFirewalldomainlist(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]
    Name: Optional[str]
    DomainCount: Optional[int]
    Status: Optional[str]
    StatusMessage: Optional[str]
    ManagedOwnerName: Optional[str]
    CreatorRequestId: Optional[str]
    CreationTime: Optional[str]
    ModificationTime: Optional[str]
    Domains: Optional[Sequence[str]]
    DomainFileUrl: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRoute53resolverFirewalldomainlist"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRoute53resolverFirewalldomainlist"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            DomainCount=json_data.get("DomainCount"),
            Status=json_data.get("Status"),
            StatusMessage=json_data.get("StatusMessage"),
            ManagedOwnerName=json_data.get("ManagedOwnerName"),
            CreatorRequestId=json_data.get("CreatorRequestId"),
            CreationTime=json_data.get("CreationTime"),
            ModificationTime=json_data.get("ModificationTime"),
            Domains=json_data.get("Domains"),
            DomainFileUrl=json_data.get("DomainFileUrl"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRoute53resolverFirewalldomainlist = AwsRoute53resolverFirewalldomainlist


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


