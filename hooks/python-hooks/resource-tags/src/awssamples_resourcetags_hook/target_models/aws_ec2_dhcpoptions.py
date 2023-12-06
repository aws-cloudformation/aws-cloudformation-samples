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
class AwsEc2Dhcpoptions(BaseModel):
    NetbiosNameServers: Optional[Sequence[str]]
    NtpServers: Optional[Sequence[str]]
    DhcpOptionsId: Optional[str]
    DomainName: Optional[str]
    NetbiosNodeType: Optional[int]
    DomainNameServers: Optional[Sequence[str]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Dhcpoptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Dhcpoptions"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            NetbiosNameServers=json_data.get("NetbiosNameServers"),
            NtpServers=json_data.get("NtpServers"),
            DhcpOptionsId=json_data.get("DhcpOptionsId"),
            DomainName=json_data.get("DomainName"),
            NetbiosNodeType=json_data.get("NetbiosNodeType"),
            DomainNameServers=json_data.get("DomainNameServers"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Dhcpoptions = AwsEc2Dhcpoptions


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


