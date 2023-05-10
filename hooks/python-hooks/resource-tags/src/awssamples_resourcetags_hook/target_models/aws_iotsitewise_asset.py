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
class AwsIotsitewiseAsset(BaseModel):
    AssetId: Optional[str]
    AssetModelId: Optional[str]
    AssetArn: Optional[str]
    AssetName: Optional[str]
    AssetDescription: Optional[str]
    AssetProperties: Optional[Sequence["_AssetProperty"]]
    AssetHierarchies: Optional[Sequence["_AssetHierarchy"]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotsitewiseAsset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotsitewiseAsset"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AssetId=json_data.get("AssetId"),
            AssetModelId=json_data.get("AssetModelId"),
            AssetArn=json_data.get("AssetArn"),
            AssetName=json_data.get("AssetName"),
            AssetDescription=json_data.get("AssetDescription"),
            AssetProperties=deserialize_list(json_data.get("AssetProperties"), AssetProperty),
            AssetHierarchies=deserialize_list(json_data.get("AssetHierarchies"), AssetHierarchy),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotsitewiseAsset = AwsIotsitewiseAsset


@dataclass
class AssetProperty(BaseModel):
    LogicalId: Optional[str]
    Alias: Optional[str]
    NotificationState: Optional[str]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssetProperty"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssetProperty"]:
        if not json_data:
            return None
        return cls(
            LogicalId=json_data.get("LogicalId"),
            Alias=json_data.get("Alias"),
            NotificationState=json_data.get("NotificationState"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssetProperty = AssetProperty


@dataclass
class AssetHierarchy(BaseModel):
    LogicalId: Optional[str]
    ChildAssetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssetHierarchy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssetHierarchy"]:
        if not json_data:
            return None
        return cls(
            LogicalId=json_data.get("LogicalId"),
            ChildAssetId=json_data.get("ChildAssetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssetHierarchy = AssetHierarchy


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


