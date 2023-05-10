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
class AwsDatabrewProject(BaseModel):
    DatasetName: Optional[str]
    Name: Optional[str]
    RecipeName: Optional[str]
    RoleArn: Optional[str]
    Sample: Optional["_Sample"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDatabrewProject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDatabrewProject"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DatasetName=json_data.get("DatasetName"),
            Name=json_data.get("Name"),
            RecipeName=json_data.get("RecipeName"),
            RoleArn=json_data.get("RoleArn"),
            Sample=Sample._deserialize(json_data.get("Sample")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDatabrewProject = AwsDatabrewProject


@dataclass
class Sample(BaseModel):
    Size: Optional[int]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Sample"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sample"]:
        if not json_data:
            return None
        return cls(
            Size=json_data.get("Size"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sample = Sample


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


