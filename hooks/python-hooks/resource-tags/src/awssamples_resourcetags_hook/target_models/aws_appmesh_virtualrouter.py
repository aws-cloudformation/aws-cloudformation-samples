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
class AwsAppmeshVirtualrouter(BaseModel):
    Uid: Optional[str]
    MeshName: Optional[str]
    VirtualRouterName: Optional[str]
    MeshOwner: Optional[str]
    ResourceOwner: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    Spec: Optional["_VirtualRouterSpec"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppmeshVirtualrouter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppmeshVirtualrouter"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Uid=json_data.get("Uid"),
            MeshName=json_data.get("MeshName"),
            VirtualRouterName=json_data.get("VirtualRouterName"),
            MeshOwner=json_data.get("MeshOwner"),
            ResourceOwner=json_data.get("ResourceOwner"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Spec=VirtualRouterSpec._deserialize(json_data.get("Spec")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppmeshVirtualrouter = AwsAppmeshVirtualrouter


@dataclass
class VirtualRouterSpec(BaseModel):
    Listeners: Optional[Sequence["_VirtualRouterListener"]]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualRouterSpec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualRouterSpec"]:
        if not json_data:
            return None
        return cls(
            Listeners=deserialize_list(json_data.get("Listeners"), VirtualRouterListener),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualRouterSpec = VirtualRouterSpec


@dataclass
class VirtualRouterListener(BaseModel):
    PortMapping: Optional["_PortMapping"]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualRouterListener"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualRouterListener"]:
        if not json_data:
            return None
        return cls(
            PortMapping=PortMapping._deserialize(json_data.get("PortMapping")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualRouterListener = VirtualRouterListener


@dataclass
class PortMapping(BaseModel):
    Protocol: Optional[str]
    Port: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_PortMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortMapping"]:
        if not json_data:
            return None
        return cls(
            Protocol=json_data.get("Protocol"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortMapping = PortMapping


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


