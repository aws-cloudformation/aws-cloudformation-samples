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
class AwsSsoPermissionset(BaseModel):
    Name: Optional[str]
    PermissionSetArn: Optional[str]
    Description: Optional[str]
    InstanceArn: Optional[str]
    SessionDuration: Optional[str]
    RelayStateType: Optional[str]
    ManagedPolicies: Optional[Sequence[str]]
    InlinePolicy: Optional[Any]
    Tags: Optional[Any]
    CustomerManagedPolicyReferences: Optional[Sequence["_CustomerManagedPolicyReference"]]
    PermissionsBoundary: Optional["_PermissionsBoundary"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSsoPermissionset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSsoPermissionset"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            PermissionSetArn=json_data.get("PermissionSetArn"),
            Description=json_data.get("Description"),
            InstanceArn=json_data.get("InstanceArn"),
            SessionDuration=json_data.get("SessionDuration"),
            RelayStateType=json_data.get("RelayStateType"),
            ManagedPolicies=json_data.get("ManagedPolicies"),
            InlinePolicy=json_data.get("InlinePolicy"),
            Tags=json_data.get("Tags"),
            CustomerManagedPolicyReferences=deserialize_list(json_data.get("CustomerManagedPolicyReferences"), CustomerManagedPolicyReference),
            PermissionsBoundary=PermissionsBoundary._deserialize(json_data.get("PermissionsBoundary")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSsoPermissionset = AwsSsoPermissionset


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
class CustomerManagedPolicyReference(BaseModel):
    Name: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomerManagedPolicyReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomerManagedPolicyReference"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomerManagedPolicyReference = CustomerManagedPolicyReference


@dataclass
class PermissionsBoundary(BaseModel):
    CustomerManagedPolicyReference: Optional["_CustomerManagedPolicyReference"]
    ManagedPolicyArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PermissionsBoundary"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PermissionsBoundary"]:
        if not json_data:
            return None
        return cls(
            CustomerManagedPolicyReference=CustomerManagedPolicyReference._deserialize(json_data.get("CustomerManagedPolicyReference")),
            ManagedPolicyArn=json_data.get("ManagedPolicyArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PermissionsBoundary = PermissionsBoundary


