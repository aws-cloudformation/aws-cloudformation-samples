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
class AwsEksAccessentry(BaseModel):
    ClusterName: Optional[str]
    PrincipalArn: Optional[str]
    Username: Optional[str]
    Tags: Optional[Any]
    AccessEntryArn: Optional[str]
    KubernetesGroups: Optional[AbstractSet[str]]
    AccessPolicies: Optional[AbstractSet["_AccessPolicy"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEksAccessentry"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEksAccessentry"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ClusterName=json_data.get("ClusterName"),
            PrincipalArn=json_data.get("PrincipalArn"),
            Username=json_data.get("Username"),
            Tags=json_data.get("Tags"),
            AccessEntryArn=json_data.get("AccessEntryArn"),
            KubernetesGroups=set_or_none(json_data.get("KubernetesGroups")),
            AccessPolicies=set_or_none(json_data.get("AccessPolicies")),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEksAccessentry = AwsEksAccessentry


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
class AccessPolicy(BaseModel):
    PolicyArn: Optional[str]
    AccessScope: Optional["_AccessScope"]

    @classmethod
    def _deserialize(
        cls: Type["_AccessPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessPolicy"]:
        if not json_data:
            return None
        return cls(
            PolicyArn=json_data.get("PolicyArn"),
            AccessScope=AccessScope._deserialize(json_data.get("AccessScope")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessPolicy = AccessPolicy


@dataclass
class AccessScope(BaseModel):
    Type: Optional[str]
    Namespaces: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AccessScope"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessScope"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Namespaces=set_or_none(json_data.get("Namespaces")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessScope = AccessScope


