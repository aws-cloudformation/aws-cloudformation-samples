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
class AwsSagemakerAppimageconfig(BaseModel):
    AppImageConfigArn: Optional[str]
    AppImageConfigName: Optional[str]
    KernelGatewayImageConfig: Optional["_KernelGatewayImageConfig"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSagemakerAppimageconfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSagemakerAppimageconfig"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AppImageConfigArn=json_data.get("AppImageConfigArn"),
            AppImageConfigName=json_data.get("AppImageConfigName"),
            KernelGatewayImageConfig=KernelGatewayImageConfig._deserialize(json_data.get("KernelGatewayImageConfig")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSagemakerAppimageconfig = AwsSagemakerAppimageconfig


@dataclass
class KernelGatewayImageConfig(BaseModel):
    FileSystemConfig: Optional["_FileSystemConfig"]
    KernelSpecs: Optional[Sequence["_KernelSpec"]]

    @classmethod
    def _deserialize(
        cls: Type["_KernelGatewayImageConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KernelGatewayImageConfig"]:
        if not json_data:
            return None
        return cls(
            FileSystemConfig=FileSystemConfig._deserialize(json_data.get("FileSystemConfig")),
            KernelSpecs=deserialize_list(json_data.get("KernelSpecs"), KernelSpec),
        )


# work around possible type aliasing issues when variable has same name as a model
_KernelGatewayImageConfig = KernelGatewayImageConfig


@dataclass
class FileSystemConfig(BaseModel):
    DefaultGid: Optional[int]
    DefaultUid: Optional[int]
    MountPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FileSystemConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileSystemConfig"]:
        if not json_data:
            return None
        return cls(
            DefaultGid=json_data.get("DefaultGid"),
            DefaultUid=json_data.get("DefaultUid"),
            MountPath=json_data.get("MountPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileSystemConfig = FileSystemConfig


@dataclass
class KernelSpec(BaseModel):
    DisplayName: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KernelSpec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KernelSpec"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KernelSpec = KernelSpec


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


