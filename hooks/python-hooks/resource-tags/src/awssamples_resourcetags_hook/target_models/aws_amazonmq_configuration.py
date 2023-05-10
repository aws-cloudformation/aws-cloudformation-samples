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
class AwsAmazonmqConfiguration(BaseModel):
    EngineVersion: Optional[str]
    Description: Optional[str]
    Revision: Optional[int]
    AuthenticationStrategy: Optional[str]
    EngineType: Optional[str]
    Data: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAmazonmqConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAmazonmqConfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            EngineVersion=json_data.get("EngineVersion"),
            Description=json_data.get("Description"),
            Revision=json_data.get("Revision"),
            AuthenticationStrategy=json_data.get("AuthenticationStrategy"),
            EngineType=json_data.get("EngineType"),
            Data=json_data.get("Data"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAmazonmqConfiguration = AwsAmazonmqConfiguration


@dataclass
class TagsEntry(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsEntry"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsEntry"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsEntry = TagsEntry


