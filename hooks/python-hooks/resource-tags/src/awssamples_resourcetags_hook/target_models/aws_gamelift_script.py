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
class AwsGameliftScript(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]
    StorageLocation: Optional["_S3Location"]
    Version: Optional[str]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGameliftScript"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGameliftScript"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            StorageLocation=S3Location._deserialize(json_data.get("StorageLocation")),
            Version=json_data.get("Version"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGameliftScript = AwsGameliftScript


@dataclass
class S3Location(BaseModel):
    ObjectVersion: Optional[str]
    Bucket: Optional[str]
    Key: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Location"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Location"]:
        if not json_data:
            return None
        return cls(
            ObjectVersion=json_data.get("ObjectVersion"),
            Bucket=json_data.get("Bucket"),
            Key=json_data.get("Key"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Location = S3Location


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


