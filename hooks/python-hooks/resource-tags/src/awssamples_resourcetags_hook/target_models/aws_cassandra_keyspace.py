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
class AwsCassandraKeyspace(BaseModel):
    KeyspaceName: Optional[str]
    Tags: Optional[Any]
    ReplicationSpecification: Optional["_ReplicationSpecification"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCassandraKeyspace"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCassandraKeyspace"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            KeyspaceName=json_data.get("KeyspaceName"),
            Tags=json_data.get("Tags"),
            ReplicationSpecification=ReplicationSpecification._deserialize(json_data.get("ReplicationSpecification")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCassandraKeyspace = AwsCassandraKeyspace


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
class ReplicationSpecification(BaseModel):
    ReplicationStrategy: Optional[str]
    RegionList: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationSpecification"]:
        if not json_data:
            return None
        return cls(
            ReplicationStrategy=json_data.get("ReplicationStrategy"),
            RegionList=set_or_none(json_data.get("RegionList")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationSpecification = ReplicationSpecification


