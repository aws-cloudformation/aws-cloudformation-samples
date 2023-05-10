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
class AwsMemorydbUser(BaseModel):
    Status: Optional[str]
    UserName: Optional[str]
    AccessString: Optional[str]
    AuthenticationMode: Optional["_AuthenticationMode"]
    Arn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMemorydbUser"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMemorydbUser"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Status=json_data.get("Status"),
            UserName=json_data.get("UserName"),
            AccessString=json_data.get("AccessString"),
            AuthenticationMode=AuthenticationMode._deserialize(json_data.get("AuthenticationMode")),
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMemorydbUser = AwsMemorydbUser


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


