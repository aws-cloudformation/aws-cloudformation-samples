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
class AwsDatasyncLocations3(BaseModel):
    S3Config: Optional["_S3Config"]
    S3BucketArn: Optional[str]
    Subdirectory: Optional[str]
    S3StorageClass: Optional[str]
    Tags: Optional[Any]
    LocationArn: Optional[str]
    LocationUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDatasyncLocations3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDatasyncLocations3"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            S3Config=S3Config._deserialize(json_data.get("S3Config")),
            S3BucketArn=json_data.get("S3BucketArn"),
            Subdirectory=json_data.get("Subdirectory"),
            S3StorageClass=json_data.get("S3StorageClass"),
            Tags=json_data.get("Tags"),
            LocationArn=json_data.get("LocationArn"),
            LocationUri=json_data.get("LocationUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDatasyncLocations3 = AwsDatasyncLocations3


@dataclass
class S3Config(BaseModel):
    BucketAccessRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Config"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Config"]:
        if not json_data:
            return None
        return cls(
            BucketAccessRoleArn=json_data.get("BucketAccessRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Config = S3Config


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


