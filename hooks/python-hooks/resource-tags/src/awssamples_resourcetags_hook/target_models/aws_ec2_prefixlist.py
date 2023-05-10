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
class AwsEc2Prefixlist(BaseModel):
    PrefixListName: Optional[str]
    PrefixListId: Optional[str]
    OwnerId: Optional[str]
    AddressFamily: Optional[str]
    MaxEntries: Optional[int]
    Version: Optional[int]
    Tags: Optional[Any]
    Entries: Optional[Sequence["_Entry"]]
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Prefixlist"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Prefixlist"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            PrefixListName=json_data.get("PrefixListName"),
            PrefixListId=json_data.get("PrefixListId"),
            OwnerId=json_data.get("OwnerId"),
            AddressFamily=json_data.get("AddressFamily"),
            MaxEntries=json_data.get("MaxEntries"),
            Version=json_data.get("Version"),
            Tags=json_data.get("Tags"),
            Entries=deserialize_list(json_data.get("Entries"), Entry),
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Prefixlist = AwsEc2Prefixlist


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


@dataclass
class Entry(BaseModel):
    Cidr: Optional[str]
    Description: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Entry"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Entry"]:
        if not json_data:
            return None
        return cls(
            Cidr=json_data.get("Cidr"),
            Description=json_data.get("Description"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Entry = Entry


