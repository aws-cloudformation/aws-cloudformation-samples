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
class AwsMediapackagev2Channel(BaseModel):
    Arn: Optional[str]
    ChannelGroupName: Optional[str]
    ChannelName: Optional[str]
    CreatedAt: Optional[str]
    Description: Optional[str]
    IngestEndpoints: Optional[Sequence["_IngestEndpoint"]]
    ModifiedAt: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMediapackagev2Channel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMediapackagev2Channel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            ChannelGroupName=json_data.get("ChannelGroupName"),
            ChannelName=json_data.get("ChannelName"),
            CreatedAt=json_data.get("CreatedAt"),
            Description=json_data.get("Description"),
            IngestEndpoints=deserialize_list(json_data.get("IngestEndpoints"), IngestEndpoint),
            ModifiedAt=json_data.get("ModifiedAt"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMediapackagev2Channel = AwsMediapackagev2Channel


@dataclass
class IngestEndpoint(BaseModel):
    Id: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IngestEndpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngestEndpoint"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngestEndpoint = IngestEndpoint


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


