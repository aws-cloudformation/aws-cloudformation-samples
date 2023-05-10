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
class AwsCodeartifactDomain(BaseModel):
    DomainName: Optional[str]
    Name: Optional[str]
    Owner: Optional[str]
    EncryptionKey: Optional[str]
    PermissionsPolicyDocument: Optional[MutableMapping[str, Any]]
    Tags: Optional[Any]
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCodeartifactDomain"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCodeartifactDomain"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DomainName=json_data.get("DomainName"),
            Name=json_data.get("Name"),
            Owner=json_data.get("Owner"),
            EncryptionKey=json_data.get("EncryptionKey"),
            PermissionsPolicyDocument=json_data.get("PermissionsPolicyDocument"),
            Tags=json_data.get("Tags"),
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCodeartifactDomain = AwsCodeartifactDomain


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


