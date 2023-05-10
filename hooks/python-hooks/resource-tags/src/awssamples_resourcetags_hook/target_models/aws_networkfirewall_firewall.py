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
class AwsNetworkfirewallFirewall(BaseModel):
    FirewallName: Optional[str]
    FirewallArn: Optional[str]
    FirewallId: Optional[str]
    FirewallPolicyArn: Optional[str]
    VpcId: Optional[str]
    SubnetMappings: Optional[AbstractSet["_SubnetMapping"]]
    DeleteProtection: Optional[bool]
    SubnetChangeProtection: Optional[bool]
    FirewallPolicyChangeProtection: Optional[bool]
    Description: Optional[str]
    EndpointIds: Optional[Sequence[str]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsNetworkfirewallFirewall"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsNetworkfirewallFirewall"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            FirewallName=json_data.get("FirewallName"),
            FirewallArn=json_data.get("FirewallArn"),
            FirewallId=json_data.get("FirewallId"),
            FirewallPolicyArn=json_data.get("FirewallPolicyArn"),
            VpcId=json_data.get("VpcId"),
            SubnetMappings=set_or_none(json_data.get("SubnetMappings")),
            DeleteProtection=json_data.get("DeleteProtection"),
            SubnetChangeProtection=json_data.get("SubnetChangeProtection"),
            FirewallPolicyChangeProtection=json_data.get("FirewallPolicyChangeProtection"),
            Description=json_data.get("Description"),
            EndpointIds=json_data.get("EndpointIds"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsNetworkfirewallFirewall = AwsNetworkfirewallFirewall


@dataclass
class SubnetMapping(BaseModel):
    SubnetId: Optional[str]
    IPAddressType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetMapping"]:
        if not json_data:
            return None
        return cls(
            SubnetId=json_data.get("SubnetId"),
            IPAddressType=json_data.get("IPAddressType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetMapping = SubnetMapping


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


