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
    DhcpOptionsId: Optional[str]
    DomainName: Optional[str]
    DomainNameServers: Optional[Sequence[str]]
    NetbiosNameServers: Optional[Sequence[str]]
    NetbiosNodeType: Optional[int]
    NtpServers: Optional[Sequence[str]]
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
            DhcpOptionsId=json_data.get("DhcpOptionsId"),
            DomainName=json_data.get("DomainName"),
            DomainNameServers=json_data.get("DomainNameServers"),
            NetbiosNameServers=json_data.get("NetbiosNameServers"),
            NetbiosNodeType=json_data.get("NetbiosNodeType"),
            NtpServers=json_data.get("NtpServers"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Dhcpoptions = AwsEc2Dhcpoptions


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


