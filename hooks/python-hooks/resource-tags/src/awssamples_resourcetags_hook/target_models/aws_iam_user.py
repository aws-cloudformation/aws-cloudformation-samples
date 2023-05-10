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
class AwsIamUser(BaseModel):
    Path: Optional[str]
    ManagedPolicyArns: Optional[Sequence[str]]
    Policies: Optional[Sequence["_Policy"]]
    UserName: Optional[str]
    Groups: Optional[Sequence[str]]
    Id: Optional[str]
    Arn: Optional[str]
    LoginProfile: Optional["_LoginProfile"]
    Tags: Optional[Any]
    PermissionsBoundary: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIamUser"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIamUser"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Path=json_data.get("Path"),
            ManagedPolicyArns=json_data.get("ManagedPolicyArns"),
            Policies=deserialize_list(json_data.get("Policies"), Policy),
            UserName=json_data.get("UserName"),
            Groups=json_data.get("Groups"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            LoginProfile=LoginProfile._deserialize(json_data.get("LoginProfile")),
            Tags=json_data.get("Tags"),
            PermissionsBoundary=json_data.get("PermissionsBoundary"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIamUser = AwsIamUser


@dataclass
class Policy(BaseModel):
    PolicyDocument: Optional[MutableMapping[str, Any]]
    PolicyName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Policy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Policy"]:
        if not json_data:
            return None
        return cls(
            PolicyDocument=json_data.get("PolicyDocument"),
            PolicyName=json_data.get("PolicyName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Policy = Policy


@dataclass
class LoginProfile(BaseModel):
    PasswordResetRequired: Optional[bool]
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoginProfile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoginProfile"]:
        if not json_data:
            return None
        return cls(
            PasswordResetRequired=json_data.get("PasswordResetRequired"),
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoginProfile = LoginProfile


@dataclass
class Tag(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


