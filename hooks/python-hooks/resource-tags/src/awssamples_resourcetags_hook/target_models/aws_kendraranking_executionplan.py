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
class AwsKendrarankingExecutionplan(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]
    Description: Optional[str]
    Tags: Optional[Any]
    Name: Optional[str]
    CapacityUnits: Optional["_CapacityUnitsConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsKendrarankingExecutionplan"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsKendrarankingExecutionplan"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
            CapacityUnits=CapacityUnitsConfiguration._deserialize(json_data.get("CapacityUnits")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsKendrarankingExecutionplan = AwsKendrarankingExecutionplan


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
class CapacityUnitsConfiguration(BaseModel):
    RescoreCapacityUnits: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityUnitsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityUnitsConfiguration"]:
        if not json_data:
            return None
        return cls(
            RescoreCapacityUnits=json_data.get("RescoreCapacityUnits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityUnitsConfiguration = CapacityUnitsConfiguration


