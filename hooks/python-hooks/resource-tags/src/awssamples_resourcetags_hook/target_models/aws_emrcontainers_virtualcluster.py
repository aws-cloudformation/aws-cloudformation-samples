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
class AwsEmrcontainersVirtualcluster(BaseModel):
    Arn: Optional[str]
    ContainerProvider: Optional["_ContainerProvider"]
    Id: Optional[str]
    Name: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEmrcontainersVirtualcluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEmrcontainersVirtualcluster"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            ContainerProvider=ContainerProvider._deserialize(json_data.get("ContainerProvider")),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEmrcontainersVirtualcluster = AwsEmrcontainersVirtualcluster


@dataclass
class ContainerProvider(BaseModel):
    Type: Optional[str]
    Id: Optional[str]
    Info: Optional["_ContainerInfo"]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerProvider"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerProvider"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Id=json_data.get("Id"),
            Info=ContainerInfo._deserialize(json_data.get("Info")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerProvider = ContainerProvider


@dataclass
class ContainerInfo(BaseModel):
    EksInfo: Optional["_EksInfo"]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerInfo"]:
        if not json_data:
            return None
        return cls(
            EksInfo=EksInfo._deserialize(json_data.get("EksInfo")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerInfo = ContainerInfo


@dataclass
class EksInfo(BaseModel):
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EksInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EksInfo"]:
        if not json_data:
            return None
        return cls(
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EksInfo = EksInfo


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


