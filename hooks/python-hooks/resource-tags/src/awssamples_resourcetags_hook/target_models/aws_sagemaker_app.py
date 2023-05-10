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
class AwsSagemakerApp(BaseModel):
    AppArn: Optional[str]
    AppName: Optional[str]
    AppType: Optional[str]
    DomainId: Optional[str]
    ResourceSpec: Optional["_ResourceSpec"]
    Tags: Optional[Any]
    UserProfileName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSagemakerApp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSagemakerApp"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AppArn=json_data.get("AppArn"),
            AppName=json_data.get("AppName"),
            AppType=json_data.get("AppType"),
            DomainId=json_data.get("DomainId"),
            ResourceSpec=ResourceSpec._deserialize(json_data.get("ResourceSpec")),
            Tags=json_data.get("Tags"),
            UserProfileName=json_data.get("UserProfileName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSagemakerApp = AwsSagemakerApp


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


