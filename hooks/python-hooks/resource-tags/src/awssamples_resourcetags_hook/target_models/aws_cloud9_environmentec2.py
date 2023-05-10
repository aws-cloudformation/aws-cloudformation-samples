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
class AwsCloud9Environmentec2(BaseModel):
    Repositories: Optional[Sequence["_Repository"]]
    OwnerArn: Optional[str]
    Description: Optional[str]
    ConnectionType: Optional[str]
    AutomaticStopTimeMinutes: Optional[int]
    ImageId: Optional[str]
    SubnetId: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    InstanceType: Optional[str]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloud9Environmentec2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloud9Environmentec2"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Repositories=deserialize_list(json_data.get("Repositories"), Repository),
            OwnerArn=json_data.get("OwnerArn"),
            Description=json_data.get("Description"),
            ConnectionType=json_data.get("ConnectionType"),
            AutomaticStopTimeMinutes=json_data.get("AutomaticStopTimeMinutes"),
            ImageId=json_data.get("ImageId"),
            SubnetId=json_data.get("SubnetId"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            InstanceType=json_data.get("InstanceType"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloud9Environmentec2 = AwsCloud9Environmentec2


@dataclass
class Repository(BaseModel):
    RepositoryUrl: Optional[str]
    PathComponent: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Repository"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Repository"]:
        if not json_data:
            return None
        return cls(
            RepositoryUrl=json_data.get("RepositoryUrl"),
            PathComponent=json_data.get("PathComponent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Repository = Repository


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


