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
class AwsDmsReplicationsubnetgroup(BaseModel):
    ReplicationSubnetGroupDescription: Optional[str]
    Id: Optional[str]
    ReplicationSubnetGroupIdentifier: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDmsReplicationsubnetgroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDmsReplicationsubnetgroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ReplicationSubnetGroupDescription=json_data.get("ReplicationSubnetGroupDescription"),
            Id=json_data.get("Id"),
            ReplicationSubnetGroupIdentifier=json_data.get("ReplicationSubnetGroupIdentifier"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDmsReplicationsubnetgroup = AwsDmsReplicationsubnetgroup


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


