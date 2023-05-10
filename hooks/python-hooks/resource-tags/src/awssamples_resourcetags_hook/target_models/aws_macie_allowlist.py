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
class AwsMacieAllowlist(BaseModel):
    Name: Optional[str]
    Description: Optional[str]
    Criteria: Optional["_Criteria"]
    Id: Optional[str]
    Arn: Optional[str]
    Status: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMacieAllowlist"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMacieAllowlist"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            Criteria=Criteria._deserialize(json_data.get("Criteria")),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMacieAllowlist = AwsMacieAllowlist


@dataclass
class Criteria(BaseModel):
    Regex: Optional[str]
    S3WordsList: Optional["_S3WordsList"]

    @classmethod
    def _deserialize(
        cls: Type["_Criteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Criteria"]:
        if not json_data:
            return None
        return cls(
            Regex=json_data.get("Regex"),
            S3WordsList=S3WordsList._deserialize(json_data.get("S3WordsList")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Criteria = Criteria


@dataclass
class S3WordsList(BaseModel):
    BucketName: Optional[str]
    ObjectKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3WordsList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3WordsList"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            ObjectKey=json_data.get("ObjectKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3WordsList = S3WordsList


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


