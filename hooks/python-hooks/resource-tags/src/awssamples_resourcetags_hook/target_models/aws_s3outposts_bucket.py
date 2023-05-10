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
class AwsS3outpostsBucket(BaseModel):
    Arn: Optional[str]
    BucketName: Optional[str]
    OutpostId: Optional[str]
    Tags: Optional[Any]
    LifecycleConfiguration: Optional["_LifecycleConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsS3outpostsBucket"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsS3outpostsBucket"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            BucketName=json_data.get("BucketName"),
            OutpostId=json_data.get("OutpostId"),
            Tags=json_data.get("Tags"),
            LifecycleConfiguration=LifecycleConfiguration._deserialize(json_data.get("LifecycleConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsS3outpostsBucket = AwsS3outpostsBucket


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
class LifecycleConfiguration(BaseModel):
    Rules: Optional[AbstractSet["_Rule"]]

    @classmethod
    def _deserialize(
        cls: Type["_LifecycleConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecycleConfiguration"]:
        if not json_data:
            return None
        return cls(
            Rules=set_or_none(json_data.get("Rules")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecycleConfiguration = LifecycleConfiguration


@dataclass
class Rule(BaseModel):
    Status: Optional[str]
    Id: Optional[str]
    AbortIncompleteMultipartUpload: Optional["_AbortIncompleteMultipartUpload"]
    ExpirationDate: Optional[str]
    ExpirationInDays: Optional[int]
    Filter: Optional["_Filter"]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            Id=json_data.get("Id"),
            AbortIncompleteMultipartUpload=AbortIncompleteMultipartUpload._deserialize(json_data.get("AbortIncompleteMultipartUpload")),
            ExpirationDate=json_data.get("ExpirationDate"),
            ExpirationInDays=json_data.get("ExpirationInDays"),
            Filter=Filter._deserialize(json_data.get("Filter")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class AbortIncompleteMultipartUpload(BaseModel):
    DaysAfterInitiation: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AbortIncompleteMultipartUpload"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AbortIncompleteMultipartUpload"]:
        if not json_data:
            return None
        return cls(
            DaysAfterInitiation=json_data.get("DaysAfterInitiation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AbortIncompleteMultipartUpload = AbortIncompleteMultipartUpload


@dataclass
class Filter(BaseModel):
    Prefix: Optional[str]
    Tag: Optional["_FilterTag"]
    AndOperator: Optional["_FilterAndOperator"]

    @classmethod
    def _deserialize(
        cls: Type["_Filter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filter"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
            Tag=FilterTag._deserialize(json_data.get("Tag")),
            AndOperator=FilterAndOperator._deserialize(json_data.get("AndOperator")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Filter = Filter


@dataclass
class FilterTag(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterTag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterTag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterTag = FilterTag


@dataclass
class FilterAndOperator(BaseModel):
    Prefix: Optional[str]
    Tags: Optional[AbstractSet["_FilterTag"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterAndOperator"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterAndOperator"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
            Tags=set_or_none(json_data.get("Tags")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterAndOperator = FilterAndOperator


