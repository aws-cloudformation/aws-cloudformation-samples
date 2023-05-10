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
class AwsIamRole(BaseModel):
    Arn: Optional[str]
    AssumeRolePolicyDocument: Optional[Any]
    Description: Optional[str]
    ManagedPolicyArns: Optional[AbstractSet[str]]
    MaxSessionDuration: Optional[int]
    Path: Optional[str]
    PermissionsBoundary: Optional[str]
    Policies: Optional[Sequence["_Policy"]]
    RoleId: Optional[str]
    RoleName: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIamRole"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIamRole"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            AssumeRolePolicyDocument=json_data.get("AssumeRolePolicyDocument"),
            Description=json_data.get("Description"),
            ManagedPolicyArns=set_or_none(json_data.get("ManagedPolicyArns")),
            MaxSessionDuration=json_data.get("MaxSessionDuration"),
            Path=json_data.get("Path"),
            PermissionsBoundary=json_data.get("PermissionsBoundary"),
            Policies=deserialize_list(json_data.get("Policies"), Policy),
            RoleId=json_data.get("RoleId"),
            RoleName=json_data.get("RoleName"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIamRole = AwsIamRole


@dataclass
class Policy(BaseModel):
    PolicyDocument: Optional[Any]
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


