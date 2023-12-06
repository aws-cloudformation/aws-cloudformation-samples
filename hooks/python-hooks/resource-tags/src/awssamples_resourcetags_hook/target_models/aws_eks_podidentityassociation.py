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
class AwsEksPodidentityassociation(BaseModel):
    ClusterName: Optional[str]
    RoleArn: Optional[str]
    Namespace: Optional[str]
    ServiceAccount: Optional[str]
    AssociationArn: Optional[str]
    AssociationId: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEksPodidentityassociation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEksPodidentityassociation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ClusterName=json_data.get("ClusterName"),
            RoleArn=json_data.get("RoleArn"),
            Namespace=json_data.get("Namespace"),
            ServiceAccount=json_data.get("ServiceAccount"),
            AssociationArn=json_data.get("AssociationArn"),
            AssociationId=json_data.get("AssociationId"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEksPodidentityassociation = AwsEksPodidentityassociation


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


