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
class AwsCodecommitRepository(BaseModel):
    CloneUrlHttp: Optional[str]
    CloneUrlSsh: Optional[str]
    RepositoryName: Optional[str]
    Triggers: Optional[Sequence["_RepositoryTrigger"]]
    Id: Optional[str]
    Arn: Optional[str]
    Code: Optional["_Code"]
    RepositoryDescription: Optional[str]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCodecommitRepository"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCodecommitRepository"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CloneUrlHttp=json_data.get("CloneUrlHttp"),
            CloneUrlSsh=json_data.get("CloneUrlSsh"),
            RepositoryName=json_data.get("RepositoryName"),
            Triggers=deserialize_list(json_data.get("Triggers"), RepositoryTrigger),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Code=Code._deserialize(json_data.get("Code")),
            RepositoryDescription=json_data.get("RepositoryDescription"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCodecommitRepository = AwsCodecommitRepository


@dataclass
class RepositoryTrigger(BaseModel):
    CustomData: Optional[str]
    Events: Optional[Sequence[str]]
    Branches: Optional[Sequence[str]]
    DestinationArn: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RepositoryTrigger"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RepositoryTrigger"]:
        if not json_data:
            return None
        return cls(
            CustomData=json_data.get("CustomData"),
            Events=json_data.get("Events"),
            Branches=json_data.get("Branches"),
            DestinationArn=json_data.get("DestinationArn"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RepositoryTrigger = RepositoryTrigger


@dataclass
class Code(BaseModel):
    S3: Optional["_S3"]
    BranchName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Code"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Code"]:
        if not json_data:
            return None
        return cls(
            S3=S3._deserialize(json_data.get("S3")),
            BranchName=json_data.get("BranchName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Code = Code


@dataclass
class S3(BaseModel):
    ObjectVersion: Optional[str]
    Bucket: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3"]:
        if not json_data:
            return None
        return cls(
            ObjectVersion=json_data.get("ObjectVersion"),
            Bucket=json_data.get("Bucket"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3 = S3


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


