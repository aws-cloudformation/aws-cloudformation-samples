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
class AwsWorkspacesConnectionalias(BaseModel):
    Associations: Optional[Sequence["_ConnectionAliasAssociation"]]
    AliasId: Optional[str]
    ConnectionString: Optional[str]
    ConnectionAliasState: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsWorkspacesConnectionalias"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsWorkspacesConnectionalias"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Associations=deserialize_list(json_data.get("Associations"), ConnectionAliasAssociation),
            AliasId=json_data.get("AliasId"),
            ConnectionString=json_data.get("ConnectionString"),
            ConnectionAliasState=json_data.get("ConnectionAliasState"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsWorkspacesConnectionalias = AwsWorkspacesConnectionalias


@dataclass
class ConnectionAliasAssociation(BaseModel):
    AssociationStatus: Optional[str]
    AssociatedAccountId: Optional[str]
    ResourceId: Optional[str]
    ConnectionIdentifier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionAliasAssociation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionAliasAssociation"]:
        if not json_data:
            return None
        return cls(
            AssociationStatus=json_data.get("AssociationStatus"),
            AssociatedAccountId=json_data.get("AssociatedAccountId"),
            ResourceId=json_data.get("ResourceId"),
            ConnectionIdentifier=json_data.get("ConnectionIdentifier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionAliasAssociation = ConnectionAliasAssociation


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


