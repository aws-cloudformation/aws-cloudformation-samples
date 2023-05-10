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
class AwsRamPermission(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    Version: Optional[str]
    IsResourceTypeDefault: Optional[bool]
    PermissionType: Optional[str]
    ResourceType: Optional[str]
    PolicyTemplate: Optional[MutableMapping[str, Any]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRamPermission"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRamPermission"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            Version=json_data.get("Version"),
            IsResourceTypeDefault=json_data.get("IsResourceTypeDefault"),
            PermissionType=json_data.get("PermissionType"),
            ResourceType=json_data.get("ResourceType"),
            PolicyTemplate=json_data.get("PolicyTemplate"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRamPermission = AwsRamPermission


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


