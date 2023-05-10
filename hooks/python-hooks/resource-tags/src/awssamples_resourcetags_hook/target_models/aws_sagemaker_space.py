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
class AwsSagemakerSpace(BaseModel):
    SpaceArn: Optional[str]
    DomainId: Optional[str]
    SpaceName: Optional[str]
    SpaceSettings: Optional["_SpaceSettings"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSagemakerSpace"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSagemakerSpace"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            SpaceArn=json_data.get("SpaceArn"),
            DomainId=json_data.get("DomainId"),
            SpaceName=json_data.get("SpaceName"),
            SpaceSettings=SpaceSettings._deserialize(json_data.get("SpaceSettings")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSagemakerSpace = AwsSagemakerSpace


@dataclass
class SpaceSettings(BaseModel):
    JupyterServerAppSettings: Optional["_JupyterServerAppSettings"]
    KernelGatewayAppSettings: Optional["_KernelGatewayAppSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_SpaceSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpaceSettings"]:
        if not json_data:
            return None
        return cls(
            JupyterServerAppSettings=JupyterServerAppSettings._deserialize(json_data.get("JupyterServerAppSettings")),
            KernelGatewayAppSettings=KernelGatewayAppSettings._deserialize(json_data.get("KernelGatewayAppSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpaceSettings = SpaceSettings


@dataclass
class JupyterServerAppSettings(BaseModel):
    DefaultResourceSpec: Optional["_ResourceSpec"]

    @classmethod
    def _deserialize(
        cls: Type["_JupyterServerAppSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JupyterServerAppSettings"]:
        if not json_data:
            return None
        return cls(
            DefaultResourceSpec=ResourceSpec._deserialize(json_data.get("DefaultResourceSpec")),
        )


# work around possible type aliasing issues when variable has same name as a model
_JupyterServerAppSettings = JupyterServerAppSettings


@dataclass
class ResourceSpec(BaseModel):
    InstanceType: Optional[str]
    SageMakerImageArn: Optional[str]
    SageMakerImageVersionArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceSpec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceSpec"]:
        if not json_data:
            return None
        return cls(
            InstanceType=json_data.get("InstanceType"),
            SageMakerImageArn=json_data.get("SageMakerImageArn"),
            SageMakerImageVersionArn=json_data.get("SageMakerImageVersionArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceSpec = ResourceSpec


@dataclass
class KernelGatewayAppSettings(BaseModel):
    CustomImages: Optional[Sequence["_CustomImage"]]
    DefaultResourceSpec: Optional["_ResourceSpec"]

    @classmethod
    def _deserialize(
        cls: Type["_KernelGatewayAppSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KernelGatewayAppSettings"]:
        if not json_data:
            return None
        return cls(
            CustomImages=deserialize_list(json_data.get("CustomImages"), CustomImage),
            DefaultResourceSpec=ResourceSpec._deserialize(json_data.get("DefaultResourceSpec")),
        )


# work around possible type aliasing issues when variable has same name as a model
_KernelGatewayAppSettings = KernelGatewayAppSettings


@dataclass
class CustomImage(BaseModel):
    AppImageConfigName: Optional[str]
    ImageName: Optional[str]
    ImageVersionNumber: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_CustomImage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomImage"]:
        if not json_data:
            return None
        return cls(
            AppImageConfigName=json_data.get("AppImageConfigName"),
            ImageName=json_data.get("ImageName"),
            ImageVersionNumber=json_data.get("ImageVersionNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomImage = CustomImage


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


