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
class AwsEntityresolutionSchemamapping(BaseModel):
    SchemaName: Optional[str]
    Description: Optional[str]
    MappedInputFields: Optional[Sequence["_SchemaInputAttribute"]]
    Tags: Optional[Any]
    SchemaArn: Optional[str]
    CreatedAt: Optional[str]
    UpdatedAt: Optional[str]
    HasWorkflows: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEntityresolutionSchemamapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEntityresolutionSchemamapping"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            SchemaName=json_data.get("SchemaName"),
            Description=json_data.get("Description"),
            MappedInputFields=deserialize_list(json_data.get("MappedInputFields"), SchemaInputAttribute),
            Tags=json_data.get("Tags"),
            SchemaArn=json_data.get("SchemaArn"),
            CreatedAt=json_data.get("CreatedAt"),
            UpdatedAt=json_data.get("UpdatedAt"),
            HasWorkflows=json_data.get("HasWorkflows"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEntityresolutionSchemamapping = AwsEntityresolutionSchemamapping


@dataclass
class SchemaInputAttribute(BaseModel):
    FieldName: Optional[str]
    Type: Optional[str]
    SubType: Optional[str]
    GroupName: Optional[str]
    MatchKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaInputAttribute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaInputAttribute"]:
        if not json_data:
            return None
        return cls(
            FieldName=json_data.get("FieldName"),
            Type=json_data.get("Type"),
            SubType=json_data.get("SubType"),
            GroupName=json_data.get("GroupName"),
            MatchKey=json_data.get("MatchKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaInputAttribute = SchemaInputAttribute


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


