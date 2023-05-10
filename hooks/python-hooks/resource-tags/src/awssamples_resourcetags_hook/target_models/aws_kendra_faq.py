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
class AwsKendraFaq(BaseModel):
    Id: Optional[str]
    IndexId: Optional[str]
    Name: Optional[str]
    Description: Optional[str]
    FileFormat: Optional[str]
    S3Path: Optional["_S3Path"]
    RoleArn: Optional[str]
    Tags: Optional[Any]
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsKendraFaq"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsKendraFaq"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            IndexId=json_data.get("IndexId"),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            FileFormat=json_data.get("FileFormat"),
            S3Path=S3Path._deserialize(json_data.get("S3Path")),
            RoleArn=json_data.get("RoleArn"),
            Tags=json_data.get("Tags"),
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsKendraFaq = AwsKendraFaq


@dataclass
class S3Path(BaseModel):
    Bucket: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Path"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Path"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Path = S3Path


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


