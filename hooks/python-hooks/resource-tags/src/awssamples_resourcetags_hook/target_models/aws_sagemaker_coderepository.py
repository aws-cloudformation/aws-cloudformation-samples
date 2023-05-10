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
class AwsSagemakerCoderepository(BaseModel):
    GitConfig: Optional["_GitConfig"]
    CodeRepositoryName: Optional[str]
    Id: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSagemakerCoderepository"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSagemakerCoderepository"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            GitConfig=GitConfig._deserialize(json_data.get("GitConfig")),
            CodeRepositoryName=json_data.get("CodeRepositoryName"),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSagemakerCoderepository = AwsSagemakerCoderepository


@dataclass
class GitConfig(BaseModel):
    SecretArn: Optional[str]
    RepositoryUrl: Optional[str]
    Branch: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GitConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GitConfig"]:
        if not json_data:
            return None
        return cls(
            SecretArn=json_data.get("SecretArn"),
            RepositoryUrl=json_data.get("RepositoryUrl"),
            Branch=json_data.get("Branch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GitConfig = GitConfig


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


