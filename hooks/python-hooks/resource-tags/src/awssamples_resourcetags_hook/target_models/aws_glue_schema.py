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
class AwsGlueSchema(BaseModel):
    Arn: Optional[str]
    Registry: Optional["_Registry"]
    Name: Optional[str]
    Description: Optional[str]
    DataFormat: Optional[str]
    Compatibility: Optional[str]
    SchemaDefinition: Optional[str]
    CheckpointVersion: Optional["_SchemaVersion"]
    Tags: Optional[Any]
    InitialSchemaVersionId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGlueSchema"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGlueSchema"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Registry=Registry._deserialize(json_data.get("Registry")),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            DataFormat=json_data.get("DataFormat"),
            Compatibility=json_data.get("Compatibility"),
            SchemaDefinition=json_data.get("SchemaDefinition"),
            CheckpointVersion=SchemaVersion._deserialize(json_data.get("CheckpointVersion")),
            Tags=json_data.get("Tags"),
            InitialSchemaVersionId=json_data.get("InitialSchemaVersionId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGlueSchema = AwsGlueSchema


@dataclass
class Registry(BaseModel):
    Name: Optional[str]
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Registry"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Registry"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Registry = Registry


@dataclass
class SchemaVersion(BaseModel):
    IsLatest: Optional[bool]
    VersionNumber: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaVersion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaVersion"]:
        if not json_data:
            return None
        return cls(
            IsLatest=json_data.get("IsLatest"),
            VersionNumber=json_data.get("VersionNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaVersion = SchemaVersion


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


