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
class AwsSagemakerModel(BaseModel):
    ExecutionRoleArn: Optional[str]
    EnableNetworkIsolation: Optional[bool]
    PrimaryContainer: Optional["_ContainerDefinition"]
    ModelName: Optional[str]
    VpcConfig: Optional["_VpcConfig"]
    Containers: Optional[Sequence["_ContainerDefinition"]]
    InferenceExecutionConfig: Optional["_InferenceExecutionConfig"]
    Id: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSagemakerModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSagemakerModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            EnableNetworkIsolation=json_data.get("EnableNetworkIsolation"),
            PrimaryContainer=ContainerDefinition._deserialize(json_data.get("PrimaryContainer")),
            ModelName=json_data.get("ModelName"),
            VpcConfig=VpcConfig._deserialize(json_data.get("VpcConfig")),
            Containers=deserialize_list(json_data.get("Containers"), ContainerDefinition),
            InferenceExecutionConfig=InferenceExecutionConfig._deserialize(json_data.get("InferenceExecutionConfig")),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSagemakerModel = AwsSagemakerModel


@dataclass
class ContainerDefinition(BaseModel):
    ImageConfig: Optional["_ImageConfig"]
    InferenceSpecificationName: Optional[str]
    ContainerHostname: Optional[str]
    ModelPackageName: Optional[str]
    Mode: Optional[str]
    Environment: Optional[MutableMapping[str, Any]]
    ModelDataUrl: Optional[str]
    Image: Optional[str]
    MultiModelConfig: Optional["_MultiModelConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerDefinition"]:
        if not json_data:
            return None
        return cls(
            ImageConfig=ImageConfig._deserialize(json_data.get("ImageConfig")),
            InferenceSpecificationName=json_data.get("InferenceSpecificationName"),
            ContainerHostname=json_data.get("ContainerHostname"),
            ModelPackageName=json_data.get("ModelPackageName"),
            Mode=json_data.get("Mode"),
            Environment=json_data.get("Environment"),
            ModelDataUrl=json_data.get("ModelDataUrl"),
            Image=json_data.get("Image"),
            MultiModelConfig=MultiModelConfig._deserialize(json_data.get("MultiModelConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerDefinition = ContainerDefinition


@dataclass
class ImageConfig(BaseModel):
    RepositoryAuthConfig: Optional["_RepositoryAuthConfig"]
    RepositoryAccessMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImageConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageConfig"]:
        if not json_data:
            return None
        return cls(
            RepositoryAuthConfig=RepositoryAuthConfig._deserialize(json_data.get("RepositoryAuthConfig")),
            RepositoryAccessMode=json_data.get("RepositoryAccessMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageConfig = ImageConfig


@dataclass
class RepositoryAuthConfig(BaseModel):
    RepositoryCredentialsProviderArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RepositoryAuthConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RepositoryAuthConfig"]:
        if not json_data:
            return None
        return cls(
            RepositoryCredentialsProviderArn=json_data.get("RepositoryCredentialsProviderArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RepositoryAuthConfig = RepositoryAuthConfig


@dataclass
class MultiModelConfig(BaseModel):
    ModelCacheSetting: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MultiModelConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MultiModelConfig"]:
        if not json_data:
            return None
        return cls(
            ModelCacheSetting=json_data.get("ModelCacheSetting"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MultiModelConfig = MultiModelConfig


@dataclass
class VpcConfig(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]]
    Subnets: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfig"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            Subnets=json_data.get("Subnets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfig = VpcConfig


@dataclass
class InferenceExecutionConfig(BaseModel):
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InferenceExecutionConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InferenceExecutionConfig"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InferenceExecutionConfig = InferenceExecutionConfig


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


