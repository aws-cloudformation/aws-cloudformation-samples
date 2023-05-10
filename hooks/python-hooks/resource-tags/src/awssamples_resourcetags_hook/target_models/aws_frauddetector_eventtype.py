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
class AwsFrauddetectorEventtype(BaseModel):
    Name: Optional[str]
    Tags: Optional[Any]
    Description: Optional[str]
    EventVariables: Optional[Sequence["_EventVariable"]]
    Labels: Optional[Sequence["_Label"]]
    EntityTypes: Optional[Sequence["_EntityType"]]
    Arn: Optional[str]
    CreatedTime: Optional[str]
    LastUpdatedTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsFrauddetectorEventtype"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsFrauddetectorEventtype"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Description=json_data.get("Description"),
            EventVariables=deserialize_list(json_data.get("EventVariables"), EventVariable),
            Labels=deserialize_list(json_data.get("Labels"), Label),
            EntityTypes=deserialize_list(json_data.get("EntityTypes"), EntityType),
            Arn=json_data.get("Arn"),
            CreatedTime=json_data.get("CreatedTime"),
            LastUpdatedTime=json_data.get("LastUpdatedTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsFrauddetectorEventtype = AwsFrauddetectorEventtype


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
class EventVariable(BaseModel):
    Arn: Optional[str]
    Inline: Optional[bool]
    Name: Optional[str]
    DataSource: Optional[str]
    DataType: Optional[str]
    DefaultValue: Optional[str]
    VariableType: Optional[str]
    Description: Optional[str]
    Tags: Optional[Sequence["_Tag"]]
    CreatedTime: Optional[str]
    LastUpdatedTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EventVariable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventVariable"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            Inline=json_data.get("Inline"),
            Name=json_data.get("Name"),
            DataSource=json_data.get("DataSource"),
            DataType=json_data.get("DataType"),
            DefaultValue=json_data.get("DefaultValue"),
            VariableType=json_data.get("VariableType"),
            Description=json_data.get("Description"),
            Tags=deserialize_list(json_data.get("Tags"), Tag),
            CreatedTime=json_data.get("CreatedTime"),
            LastUpdatedTime=json_data.get("LastUpdatedTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventVariable = EventVariable


@dataclass
class Label(BaseModel):
    Arn: Optional[str]
    Inline: Optional[bool]
    Name: Optional[str]
    Description: Optional[str]
    Tags: Optional[Sequence["_Tag"]]
    CreatedTime: Optional[str]
    LastUpdatedTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Label"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Label"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            Inline=json_data.get("Inline"),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            Tags=deserialize_list(json_data.get("Tags"), Tag),
            CreatedTime=json_data.get("CreatedTime"),
            LastUpdatedTime=json_data.get("LastUpdatedTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Label = Label


@dataclass
class EntityType(BaseModel):
    Arn: Optional[str]
    Inline: Optional[bool]
    Name: Optional[str]
    Description: Optional[str]
    Tags: Optional[Sequence["_Tag"]]
    CreatedTime: Optional[str]
    LastUpdatedTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EntityType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntityType"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            Inline=json_data.get("Inline"),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            Tags=deserialize_list(json_data.get("Tags"), Tag),
            CreatedTime=json_data.get("CreatedTime"),
            LastUpdatedTime=json_data.get("LastUpdatedTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntityType = EntityType


