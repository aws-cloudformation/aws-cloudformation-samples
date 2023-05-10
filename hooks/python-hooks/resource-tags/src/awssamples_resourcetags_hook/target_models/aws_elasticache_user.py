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
class AwsElasticacheUser(BaseModel):
    Status: Optional[str]
    UserId: Optional[str]
    UserName: Optional[str]
    Engine: Optional[str]
    AccessString: Optional[str]
    NoPasswordRequired: Optional[bool]
    Passwords: Optional[Sequence[str]]
    Arn: Optional[str]
    AuthenticationMode: Optional["_AuthenticationMode"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsElasticacheUser"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsElasticacheUser"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Status=json_data.get("Status"),
            UserId=json_data.get("UserId"),
            UserName=json_data.get("UserName"),
            Engine=json_data.get("Engine"),
            AccessString=json_data.get("AccessString"),
            NoPasswordRequired=json_data.get("NoPasswordRequired"),
            Passwords=json_data.get("Passwords"),
            Arn=json_data.get("Arn"),
            AuthenticationMode=AuthenticationMode._deserialize(json_data.get("AuthenticationMode")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsElasticacheUser = AwsElasticacheUser


@dataclass
class AuthenticationMode(BaseModel):
    Type: Optional[str]
    Passwords: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationMode"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationMode"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Passwords=json_data.get("Passwords"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationMode = AuthenticationMode


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


