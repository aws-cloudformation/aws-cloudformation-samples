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
class AwsEc2Instanceconnectendpoint(BaseModel):
    Id: Optional[str]
    SubnetId: Optional[str]
    ClientToken: Optional[str]
    PreserveClientIp: Optional[bool]
    Tags: Optional[Any]
    SecurityGroupIds: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Instanceconnectendpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Instanceconnectendpoint"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            SubnetId=json_data.get("SubnetId"),
            ClientToken=json_data.get("ClientToken"),
            PreserveClientIp=json_data.get("PreserveClientIp"),
            Tags=json_data.get("Tags"),
            SecurityGroupIds=set_or_none(json_data.get("SecurityGroupIds")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Instanceconnectendpoint = AwsEc2Instanceconnectendpoint


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


