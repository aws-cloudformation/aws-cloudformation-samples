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
class AwsMediapackageAsset(BaseModel):
    Arn: Optional[str]
    CreatedAt: Optional[str]
    EgressEndpoints: Optional[Sequence["_EgressEndpoint"]]
    Id: Optional[str]
    PackagingGroupId: Optional[str]
    ResourceId: Optional[str]
    SourceArn: Optional[str]
    SourceRoleArn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMediapackageAsset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMediapackageAsset"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            CreatedAt=json_data.get("CreatedAt"),
            EgressEndpoints=deserialize_list(json_data.get("EgressEndpoints"), EgressEndpoint),
            Id=json_data.get("Id"),
            PackagingGroupId=json_data.get("PackagingGroupId"),
            ResourceId=json_data.get("ResourceId"),
            SourceArn=json_data.get("SourceArn"),
            SourceRoleArn=json_data.get("SourceRoleArn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMediapackageAsset = AwsMediapackageAsset


@dataclass
class EgressEndpoint(BaseModel):
    PackagingConfigurationId: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EgressEndpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EgressEndpoint"]:
        if not json_data:
            return None
        return cls(
            PackagingConfigurationId=json_data.get("PackagingConfigurationId"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EgressEndpoint = EgressEndpoint


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


