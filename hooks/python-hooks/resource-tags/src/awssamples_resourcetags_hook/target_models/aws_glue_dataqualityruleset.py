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
class AwsGlueDataqualityruleset(BaseModel):
    Ruleset: Optional[str]
    Description: Optional[str]
    TargetTable: Optional["_DataQualityTargetTable"]
    Id: Optional[str]
    ClientToken: Optional[str]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGlueDataqualityruleset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGlueDataqualityruleset"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Ruleset=json_data.get("Ruleset"),
            Description=json_data.get("Description"),
            TargetTable=DataQualityTargetTable._deserialize(json_data.get("TargetTable")),
            Id=json_data.get("Id"),
            ClientToken=json_data.get("ClientToken"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGlueDataqualityruleset = AwsGlueDataqualityruleset


@dataclass
class DataQualityTargetTable(BaseModel):
    DatabaseName: Optional[str]
    TableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataQualityTargetTable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataQualityTargetTable"]:
        if not json_data:
            return None
        return cls(
            DatabaseName=json_data.get("DatabaseName"),
            TableName=json_data.get("TableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataQualityTargetTable = DataQualityTargetTable


