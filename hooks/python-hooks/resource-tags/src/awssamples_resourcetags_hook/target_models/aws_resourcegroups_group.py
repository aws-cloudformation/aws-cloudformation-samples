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
class AwsResourcegroupsGroup(BaseModel):
    Name: Optional[str]
    Description: Optional[str]
    ResourceQuery: Optional["_ResourceQuery"]
    Tags: Optional[Any]
    Arn: Optional[str]
    Configuration: Optional[Sequence["_ConfigurationItem"]]
    Resources: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsResourcegroupsGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsResourcegroupsGroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            ResourceQuery=ResourceQuery._deserialize(json_data.get("ResourceQuery")),
            Tags=json_data.get("Tags"),
            Arn=json_data.get("Arn"),
            Configuration=deserialize_list(json_data.get("Configuration"), ConfigurationItem),
            Resources=json_data.get("Resources"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsResourcegroupsGroup = AwsResourcegroupsGroup


@dataclass
class ResourceQuery(BaseModel):
    Type: Optional[str]
    Query: Optional["_Query"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceQuery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceQuery"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Query=Query._deserialize(json_data.get("Query")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceQuery = ResourceQuery


@dataclass
class Query(BaseModel):
    ResourceTypeFilters: Optional[Sequence[str]]
    StackIdentifier: Optional[str]
    TagFilters: Optional[Sequence["_TagFilter"]]

    @classmethod
    def _deserialize(
        cls: Type["_Query"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Query"]:
        if not json_data:
            return None
        return cls(
            ResourceTypeFilters=json_data.get("ResourceTypeFilters"),
            StackIdentifier=json_data.get("StackIdentifier"),
            TagFilters=deserialize_list(json_data.get("TagFilters"), TagFilter),
        )


# work around possible type aliasing issues when variable has same name as a model
_Query = Query


@dataclass
class TagFilter(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TagFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagFilter"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagFilter = TagFilter


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
class ConfigurationItem(BaseModel):
    Type: Optional[str]
    Parameters: Optional[Sequence["_ConfigurationParameter"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationItem"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Parameters=deserialize_list(json_data.get("Parameters"), ConfigurationParameter),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationItem = ConfigurationItem


@dataclass
class ConfigurationParameter(BaseModel):
    Name: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationParameter"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationParameter = ConfigurationParameter


