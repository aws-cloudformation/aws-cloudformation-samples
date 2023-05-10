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
class AwsRoute53recoverycontrolCluster(BaseModel):
    Name: Optional[str]
    ClusterArn: Optional[str]
    Status: Optional[str]
    ClusterEndpoints: Optional[Sequence["_ClusterEndpoint"]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRoute53recoverycontrolCluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRoute53recoverycontrolCluster"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            ClusterArn=json_data.get("ClusterArn"),
            Status=json_data.get("Status"),
            ClusterEndpoints=deserialize_list(json_data.get("ClusterEndpoints"), ClusterEndpoint),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRoute53recoverycontrolCluster = AwsRoute53recoverycontrolCluster


@dataclass
class ClusterEndpoint(BaseModel):
    Endpoint: Optional[str]
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterEndpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterEndpoint"]:
        if not json_data:
            return None
        return cls(
            Endpoint=json_data.get("Endpoint"),
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterEndpoint = ClusterEndpoint


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


