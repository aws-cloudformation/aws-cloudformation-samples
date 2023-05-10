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
class AwsEc2Ipamscope(BaseModel):
    IpamScopeId: Optional[str]
    Arn: Optional[str]
    IpamId: Optional[str]
    IpamArn: Optional[str]
    IpamScopeType: Optional[str]
    IsDefault: Optional[bool]
    Description: Optional[str]
    PoolCount: Optional[int]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Ipamscope"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Ipamscope"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            IpamScopeId=json_data.get("IpamScopeId"),
            Arn=json_data.get("Arn"),
            IpamId=json_data.get("IpamId"),
            IpamArn=json_data.get("IpamArn"),
            IpamScopeType=json_data.get("IpamScopeType"),
            IsDefault=json_data.get("IsDefault"),
            Description=json_data.get("Description"),
            PoolCount=json_data.get("PoolCount"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Ipamscope = AwsEc2Ipamscope


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


