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
class AwsCloudtrailChannel(BaseModel):
    Name: Optional[str]
    Source: Optional[str]
    Destinations: Optional[AbstractSet["_Destination"]]
    ChannelArn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudtrailChannel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudtrailChannel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Source=json_data.get("Source"),
            Destinations=set_or_none(json_data.get("Destinations")),
            ChannelArn=json_data.get("ChannelArn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudtrailChannel = AwsCloudtrailChannel


@dataclass
class Destination(BaseModel):
    Type: Optional[str]
    Location: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Destination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Destination"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Location=json_data.get("Location"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Destination = Destination


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


