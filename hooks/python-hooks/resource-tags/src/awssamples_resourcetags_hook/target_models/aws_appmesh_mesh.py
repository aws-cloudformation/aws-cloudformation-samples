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
class AwsAppmeshMesh(BaseModel):
    Uid: Optional[str]
    MeshName: Optional[str]
    MeshOwner: Optional[str]
    ResourceOwner: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    Spec: Optional["_MeshSpec"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppmeshMesh"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppmeshMesh"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Uid=json_data.get("Uid"),
            MeshName=json_data.get("MeshName"),
            MeshOwner=json_data.get("MeshOwner"),
            ResourceOwner=json_data.get("ResourceOwner"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Spec=MeshSpec._deserialize(json_data.get("Spec")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppmeshMesh = AwsAppmeshMesh


@dataclass
class MeshSpec(BaseModel):
    EgressFilter: Optional["_EgressFilter"]
    ServiceDiscovery: Optional["_MeshServiceDiscovery"]

    @classmethod
    def _deserialize(
        cls: Type["_MeshSpec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MeshSpec"]:
        if not json_data:
            return None
        return cls(
            EgressFilter=EgressFilter._deserialize(json_data.get("EgressFilter")),
            ServiceDiscovery=MeshServiceDiscovery._deserialize(json_data.get("ServiceDiscovery")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MeshSpec = MeshSpec


@dataclass
class EgressFilter(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EgressFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EgressFilter"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EgressFilter = EgressFilter


@dataclass
class MeshServiceDiscovery(BaseModel):
    IpPreference: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MeshServiceDiscovery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MeshServiceDiscovery"]:
        if not json_data:
            return None
        return cls(
            IpPreference=json_data.get("IpPreference"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MeshServiceDiscovery = MeshServiceDiscovery


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


