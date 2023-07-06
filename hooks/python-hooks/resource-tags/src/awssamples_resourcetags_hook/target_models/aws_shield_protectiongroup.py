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
class AwsShieldProtectiongroup(BaseModel):
    ProtectionGroupId: Optional[str]
    ProtectionGroupArn: Optional[str]
    Aggregation: Optional[str]
    Pattern: Optional[str]
    Members: Optional[Sequence[str]]
    ResourceType: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsShieldProtectiongroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsShieldProtectiongroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ProtectionGroupId=json_data.get("ProtectionGroupId"),
            ProtectionGroupArn=json_data.get("ProtectionGroupArn"),
            Aggregation=json_data.get("Aggregation"),
            Pattern=json_data.get("Pattern"),
            Members=json_data.get("Members"),
            ResourceType=json_data.get("ResourceType"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsShieldProtectiongroup = AwsShieldProtectiongroup


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


