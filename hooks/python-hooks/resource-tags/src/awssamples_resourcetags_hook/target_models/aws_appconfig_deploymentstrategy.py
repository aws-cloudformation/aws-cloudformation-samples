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
class AwsAppconfigDeploymentstrategy(BaseModel):
    ReplicateTo: Optional[str]
    GrowthType: Optional[str]
    Description: Optional[str]
    DeploymentDurationInMinutes: Optional[float]
    GrowthFactor: Optional[float]
    Id: Optional[str]
    FinalBakeTimeInMinutes: Optional[float]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppconfigDeploymentstrategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppconfigDeploymentstrategy"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ReplicateTo=json_data.get("ReplicateTo"),
            GrowthType=json_data.get("GrowthType"),
            Description=json_data.get("Description"),
            DeploymentDurationInMinutes=json_data.get("DeploymentDurationInMinutes"),
            GrowthFactor=json_data.get("GrowthFactor"),
            Id=json_data.get("Id"),
            FinalBakeTimeInMinutes=json_data.get("FinalBakeTimeInMinutes"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppconfigDeploymentstrategy = AwsAppconfigDeploymentstrategy


@dataclass
class Tags(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


