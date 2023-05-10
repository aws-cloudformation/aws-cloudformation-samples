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
class AwsNetworkmanagerLink(BaseModel):
    LinkArn: Optional[str]
    LinkId: Optional[str]
    GlobalNetworkId: Optional[str]
    SiteId: Optional[str]
    Bandwidth: Optional["_Bandwidth"]
    Provider: Optional[str]
    Description: Optional[str]
    Tags: Optional[Any]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsNetworkmanagerLink"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsNetworkmanagerLink"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            LinkArn=json_data.get("LinkArn"),
            LinkId=json_data.get("LinkId"),
            GlobalNetworkId=json_data.get("GlobalNetworkId"),
            SiteId=json_data.get("SiteId"),
            Bandwidth=Bandwidth._deserialize(json_data.get("Bandwidth")),
            Provider=json_data.get("Provider"),
            Description=json_data.get("Description"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsNetworkmanagerLink = AwsNetworkmanagerLink


@dataclass
class Bandwidth(BaseModel):
    DownloadSpeed: Optional[int]
    UploadSpeed: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Bandwidth"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Bandwidth"]:
        if not json_data:
            return None
        return cls(
            DownloadSpeed=json_data.get("DownloadSpeed"),
            UploadSpeed=json_data.get("UploadSpeed"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Bandwidth = Bandwidth


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


