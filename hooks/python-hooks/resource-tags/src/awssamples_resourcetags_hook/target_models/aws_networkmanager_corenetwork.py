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
class AwsNetworkmanagerCorenetwork(BaseModel):
    GlobalNetworkId: Optional[str]
    CoreNetworkId: Optional[str]
    CoreNetworkArn: Optional[str]
    PolicyDocument: Optional[MutableMapping[str, Any]]
    Description: Optional[str]
    CreatedAt: Optional[str]
    State: Optional[str]
    Segments: Optional[Sequence["_CoreNetworkSegment"]]
    Edges: Optional[Sequence["_CoreNetworkEdge"]]
    OwnerAccount: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsNetworkmanagerCorenetwork"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsNetworkmanagerCorenetwork"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            GlobalNetworkId=json_data.get("GlobalNetworkId"),
            CoreNetworkId=json_data.get("CoreNetworkId"),
            CoreNetworkArn=json_data.get("CoreNetworkArn"),
            PolicyDocument=json_data.get("PolicyDocument"),
            Description=json_data.get("Description"),
            CreatedAt=json_data.get("CreatedAt"),
            State=json_data.get("State"),
            Segments=deserialize_list(json_data.get("Segments"), CoreNetworkSegment),
            Edges=deserialize_list(json_data.get("Edges"), CoreNetworkEdge),
            OwnerAccount=json_data.get("OwnerAccount"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsNetworkmanagerCorenetwork = AwsNetworkmanagerCorenetwork


@dataclass
class CoreNetworkSegment(BaseModel):
    Name: Optional[str]
    EdgeLocations: Optional[Sequence[str]]
    SharedSegments: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CoreNetworkSegment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CoreNetworkSegment"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            EdgeLocations=json_data.get("EdgeLocations"),
            SharedSegments=json_data.get("SharedSegments"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CoreNetworkSegment = CoreNetworkSegment


@dataclass
class CoreNetworkEdge(BaseModel):
    EdgeLocation: Optional[str]
    Asn: Optional[float]
    InsideCidrBlocks: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CoreNetworkEdge"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CoreNetworkEdge"]:
        if not json_data:
            return None
        return cls(
            EdgeLocation=json_data.get("EdgeLocation"),
            Asn=json_data.get("Asn"),
            InsideCidrBlocks=json_data.get("InsideCidrBlocks"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CoreNetworkEdge = CoreNetworkEdge


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


