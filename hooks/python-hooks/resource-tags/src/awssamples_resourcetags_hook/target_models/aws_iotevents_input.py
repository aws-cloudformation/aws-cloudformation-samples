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
class AwsIoteventsInput(BaseModel):
    InputDefinition: Optional["_InputDefinition"]
    InputDescription: Optional[str]
    InputName: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIoteventsInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIoteventsInput"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            InputDefinition=InputDefinition._deserialize(json_data.get("InputDefinition")),
            InputDescription=json_data.get("InputDescription"),
            InputName=json_data.get("InputName"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIoteventsInput = AwsIoteventsInput


@dataclass
class InputDefinition(BaseModel):
    Attributes: Optional[AbstractSet["_Attribute"]]

    @classmethod
    def _deserialize(
        cls: Type["_InputDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputDefinition"]:
        if not json_data:
            return None
        return cls(
            Attributes=set_or_none(json_data.get("Attributes")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputDefinition = InputDefinition


@dataclass
class Attribute(BaseModel):
    JsonPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Attribute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Attribute"]:
        if not json_data:
            return None
        return cls(
            JsonPath=json_data.get("JsonPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Attribute = Attribute


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


