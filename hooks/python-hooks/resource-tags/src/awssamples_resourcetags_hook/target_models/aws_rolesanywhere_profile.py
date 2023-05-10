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
class AwsRolesanywhereProfile(BaseModel):
    DurationSeconds: Optional[float]
    Enabled: Optional[bool]
    ManagedPolicyArns: Optional[Sequence[str]]
    Name: Optional[str]
    ProfileArn: Optional[str]
    ProfileId: Optional[str]
    RequireInstanceProperties: Optional[bool]
    RoleArns: Optional[Sequence[str]]
    SessionPolicy: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRolesanywhereProfile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRolesanywhereProfile"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DurationSeconds=json_data.get("DurationSeconds"),
            Enabled=json_data.get("Enabled"),
            ManagedPolicyArns=json_data.get("ManagedPolicyArns"),
            Name=json_data.get("Name"),
            ProfileArn=json_data.get("ProfileArn"),
            ProfileId=json_data.get("ProfileId"),
            RequireInstanceProperties=json_data.get("RequireInstanceProperties"),
            RoleArns=json_data.get("RoleArns"),
            SessionPolicy=json_data.get("SessionPolicy"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRolesanywhereProfile = AwsRolesanywhereProfile


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


