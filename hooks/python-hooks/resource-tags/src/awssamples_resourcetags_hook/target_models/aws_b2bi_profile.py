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
class AwsB2biProfile(BaseModel):
    BusinessName: Optional[str]
    CreatedAt: Optional[str]
    Email: Optional[str]
    LogGroupName: Optional[str]
    Logging: Optional[str]
    ModifiedAt: Optional[str]
    Name: Optional[str]
    Phone: Optional[str]
    ProfileArn: Optional[str]
    ProfileId: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsB2biProfile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsB2biProfile"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            BusinessName=json_data.get("BusinessName"),
            CreatedAt=json_data.get("CreatedAt"),
            Email=json_data.get("Email"),
            LogGroupName=json_data.get("LogGroupName"),
            Logging=json_data.get("Logging"),
            ModifiedAt=json_data.get("ModifiedAt"),
            Name=json_data.get("Name"),
            Phone=json_data.get("Phone"),
            ProfileArn=json_data.get("ProfileArn"),
            ProfileId=json_data.get("ProfileId"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsB2biProfile = AwsB2biProfile


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


