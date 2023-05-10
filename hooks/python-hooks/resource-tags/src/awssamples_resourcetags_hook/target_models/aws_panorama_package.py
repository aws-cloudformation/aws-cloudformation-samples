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
class AwsPanoramaPackage(BaseModel):
    PackageName: Optional[str]
    PackageId: Optional[str]
    Arn: Optional[str]
    StorageLocation: Optional["_StorageLocation"]
    CreatedTime: Optional[int]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsPanoramaPackage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsPanoramaPackage"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            PackageName=json_data.get("PackageName"),
            PackageId=json_data.get("PackageId"),
            Arn=json_data.get("Arn"),
            StorageLocation=StorageLocation._deserialize(json_data.get("StorageLocation")),
            CreatedTime=json_data.get("CreatedTime"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsPanoramaPackage = AwsPanoramaPackage


@dataclass
class StorageLocation(BaseModel):
    Bucket: Optional[str]
    RepoPrefixLocation: Optional[str]
    GeneratedPrefixLocation: Optional[str]
    BinaryPrefixLocation: Optional[str]
    ManifestPrefixLocation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageLocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageLocation"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            RepoPrefixLocation=json_data.get("RepoPrefixLocation"),
            GeneratedPrefixLocation=json_data.get("GeneratedPrefixLocation"),
            BinaryPrefixLocation=json_data.get("BinaryPrefixLocation"),
            ManifestPrefixLocation=json_data.get("ManifestPrefixLocation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageLocation = StorageLocation


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


