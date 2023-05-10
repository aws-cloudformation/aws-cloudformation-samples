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
class AwsEcrPublicrepository(BaseModel):
    RepositoryName: Optional[str]
    RepositoryPolicyText: Optional[Any]
    Arn: Optional[str]
    RepositoryCatalogData: Optional["_RepositoryCatalogData"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEcrPublicrepository"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEcrPublicrepository"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            RepositoryName=json_data.get("RepositoryName"),
            RepositoryPolicyText=json_data.get("RepositoryPolicyText"),
            Arn=json_data.get("Arn"),
            RepositoryCatalogData=RepositoryCatalogData._deserialize(json_data.get("RepositoryCatalogData")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEcrPublicrepository = AwsEcrPublicrepository


@dataclass
class RepositoryCatalogData(BaseModel):
    RepositoryDescription: Optional[str]
    Architectures: Optional[AbstractSet[str]]
    OperatingSystems: Optional[AbstractSet[str]]
    AboutText: Optional[str]
    UsageText: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RepositoryCatalogData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RepositoryCatalogData"]:
        if not json_data:
            return None
        return cls(
            RepositoryDescription=json_data.get("RepositoryDescription"),
            Architectures=set_or_none(json_data.get("Architectures")),
            OperatingSystems=set_or_none(json_data.get("OperatingSystems")),
            AboutText=json_data.get("AboutText"),
            UsageText=json_data.get("UsageText"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RepositoryCatalogData = RepositoryCatalogData


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


