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
class AwsAppconfigExtension(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]
    VersionNumber: Optional[int]
    Name: Optional[str]
    Description: Optional[str]
    Actions: Optional[MutableMapping[str, AbstractSet["_Action"]]]
    Parameters: Optional[MutableMapping[str, "_Parameter"]]
    LatestVersionNumber: Optional[int]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppconfigExtension"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppconfigExtension"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            VersionNumber=json_data.get("VersionNumber"),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            Actions=json_data.get("Actions"),
            Parameters=json_data.get("Parameters"),
            LatestVersionNumber=json_data.get("LatestVersionNumber"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppconfigExtension = AwsAppconfigExtension


@dataclass
class Action(BaseModel):
    Name: Optional[str]
    Description: Optional[str]
    Uri: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            Uri=json_data.get("Uri"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class Parameter(BaseModel):
    Description: Optional[str]
    Required: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Parameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Parameter"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Required=json_data.get("Required"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Parameter = Parameter


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


