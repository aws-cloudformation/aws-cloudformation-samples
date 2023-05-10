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
class AwsEventschemasDiscoverer(BaseModel):
    DiscovererArn: Optional[str]
    DiscovererId: Optional[str]
    CrossAccount: Optional[bool]
    Description: Optional[str]
    SourceArn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEventschemasDiscoverer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEventschemasDiscoverer"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DiscovererArn=json_data.get("DiscovererArn"),
            DiscovererId=json_data.get("DiscovererId"),
            CrossAccount=json_data.get("CrossAccount"),
            Description=json_data.get("Description"),
            SourceArn=json_data.get("SourceArn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEventschemasDiscoverer = AwsEventschemasDiscoverer


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


