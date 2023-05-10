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
class AwsRamResourceshare(BaseModel):
    PermissionArns: Optional[Sequence[str]]
    Principals: Optional[Sequence[str]]
    AllowExternalPrincipals: Optional[bool]
    Id: Optional[str]
    Arn: Optional[str]
    ResourceArns: Optional[Sequence[str]]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRamResourceshare"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRamResourceshare"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            PermissionArns=json_data.get("PermissionArns"),
            Principals=json_data.get("Principals"),
            AllowExternalPrincipals=json_data.get("AllowExternalPrincipals"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            ResourceArns=json_data.get("ResourceArns"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRamResourceshare = AwsRamResourceshare


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


