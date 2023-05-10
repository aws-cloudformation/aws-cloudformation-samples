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
class AwsOrganizationsPolicy(BaseModel):
    Name: Optional[str]
    Type: Optional[str]
    Content: Optional[Any]
    Description: Optional[str]
    TargetIds: Optional[AbstractSet[str]]
    Tags: Optional[Any]
    Id: Optional[str]
    Arn: Optional[str]
    AwsManaged: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AwsOrganizationsPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsOrganizationsPolicy"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Content=json_data.get("Content"),
            Description=json_data.get("Description"),
            TargetIds=set_or_none(json_data.get("TargetIds")),
            Tags=json_data.get("Tags"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            AwsManaged=json_data.get("AwsManaged"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsOrganizationsPolicy = AwsOrganizationsPolicy


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


