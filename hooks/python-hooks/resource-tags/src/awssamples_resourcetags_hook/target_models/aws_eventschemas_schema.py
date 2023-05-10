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
class AwsEventschemasSchema(BaseModel):
    Type: Optional[str]
    Description: Optional[str]
    SchemaVersion: Optional[str]
    Content: Optional[str]
    RegistryName: Optional[str]
    Id: Optional[str]
    SchemaArn: Optional[str]
    SchemaName: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEventschemasSchema"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEventschemasSchema"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Type=json_data.get("Type"),
            Description=json_data.get("Description"),
            SchemaVersion=json_data.get("SchemaVersion"),
            Content=json_data.get("Content"),
            RegistryName=json_data.get("RegistryName"),
            Id=json_data.get("Id"),
            SchemaArn=json_data.get("SchemaArn"),
            SchemaName=json_data.get("SchemaName"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEventschemasSchema = AwsEventschemasSchema


@dataclass
class TagsEntry(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsEntry"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsEntry"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsEntry = TagsEntry


