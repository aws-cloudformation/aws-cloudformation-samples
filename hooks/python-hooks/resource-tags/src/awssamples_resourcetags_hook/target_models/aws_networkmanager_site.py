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
class AwsNetworkmanagerSite(BaseModel):
    SiteArn: Optional[str]
    SiteId: Optional[str]
    Description: Optional[str]
    Tags: Optional[Any]
    GlobalNetworkId: Optional[str]
    Location: Optional["_Location"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsNetworkmanagerSite"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsNetworkmanagerSite"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            SiteArn=json_data.get("SiteArn"),
            SiteId=json_data.get("SiteId"),
            Description=json_data.get("Description"),
            Tags=json_data.get("Tags"),
            GlobalNetworkId=json_data.get("GlobalNetworkId"),
            Location=Location._deserialize(json_data.get("Location")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsNetworkmanagerSite = AwsNetworkmanagerSite


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


@dataclass
class Location(BaseModel):
    Address: Optional[str]
    Latitude: Optional[str]
    Longitude: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Location"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Location"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Latitude=json_data.get("Latitude"),
            Longitude=json_data.get("Longitude"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Location = Location


