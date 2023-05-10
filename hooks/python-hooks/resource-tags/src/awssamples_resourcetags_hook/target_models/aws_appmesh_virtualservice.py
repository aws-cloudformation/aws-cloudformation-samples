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
class AwsAppmeshVirtualservice(BaseModel):
    Uid: Optional[str]
    MeshName: Optional[str]
    MeshOwner: Optional[str]
    ResourceOwner: Optional[str]
    Id: Optional[str]
    VirtualServiceName: Optional[str]
    Arn: Optional[str]
    Spec: Optional["_VirtualServiceSpec"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppmeshVirtualservice"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppmeshVirtualservice"]:
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
            VirtualServiceName=json_data.get("VirtualServiceName"),
            Arn=json_data.get("Arn"),
            Spec=VirtualServiceSpec._deserialize(json_data.get("Spec")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppmeshVirtualservice = AwsAppmeshVirtualservice


@dataclass
class VirtualServiceSpec(BaseModel):
    Provider: Optional["_VirtualServiceProvider"]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualServiceSpec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualServiceSpec"]:
        if not json_data:
            return None
        return cls(
            Provider=VirtualServiceProvider._deserialize(json_data.get("Provider")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualServiceSpec = VirtualServiceSpec


@dataclass
class VirtualServiceProvider(BaseModel):
    VirtualNode: Optional["_VirtualNodeServiceProvider"]
    VirtualRouter: Optional["_VirtualRouterServiceProvider"]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualServiceProvider"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualServiceProvider"]:
        if not json_data:
            return None
        return cls(
            VirtualNode=VirtualNodeServiceProvider._deserialize(json_data.get("VirtualNode")),
            VirtualRouter=VirtualRouterServiceProvider._deserialize(json_data.get("VirtualRouter")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualServiceProvider = VirtualServiceProvider


@dataclass
class VirtualNodeServiceProvider(BaseModel):
    VirtualNodeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualNodeServiceProvider"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualNodeServiceProvider"]:
        if not json_data:
            return None
        return cls(
            VirtualNodeName=json_data.get("VirtualNodeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualNodeServiceProvider = VirtualNodeServiceProvider


@dataclass
class VirtualRouterServiceProvider(BaseModel):
    VirtualRouterName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualRouterServiceProvider"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualRouterServiceProvider"]:
        if not json_data:
            return None
        return cls(
            VirtualRouterName=json_data.get("VirtualRouterName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualRouterServiceProvider = VirtualRouterServiceProvider


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


