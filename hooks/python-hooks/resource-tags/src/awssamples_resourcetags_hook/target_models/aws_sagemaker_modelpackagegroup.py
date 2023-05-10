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
class AwsSagemakerModelpackagegroup(BaseModel):
    Tags: Optional[Any]
    ModelPackageGroupArn: Optional[str]
    ModelPackageGroupName: Optional[str]
    ModelPackageGroupDescription: Optional[str]
    ModelPackageGroupPolicy: Optional[Any]
    CreationTime: Optional[str]
    ModelPackageGroupStatus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSagemakerModelpackagegroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSagemakerModelpackagegroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Tags=json_data.get("Tags"),
            ModelPackageGroupArn=json_data.get("ModelPackageGroupArn"),
            ModelPackageGroupName=json_data.get("ModelPackageGroupName"),
            ModelPackageGroupDescription=json_data.get("ModelPackageGroupDescription"),
            ModelPackageGroupPolicy=json_data.get("ModelPackageGroupPolicy"),
            CreationTime=json_data.get("CreationTime"),
            ModelPackageGroupStatus=json_data.get("ModelPackageGroupStatus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSagemakerModelpackagegroup = AwsSagemakerModelpackagegroup


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


