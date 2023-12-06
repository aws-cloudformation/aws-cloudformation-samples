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
class AwsCodestarconnectionsRepositorylink(BaseModel):
    ConnectionArn: Optional[str]
    ProviderType: Optional[str]
    OwnerId: Optional[str]
    RepositoryName: Optional[str]
    EncryptionKeyArn: Optional[str]
    RepositoryLinkId: Optional[str]
    RepositoryLinkArn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCodestarconnectionsRepositorylink"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCodestarconnectionsRepositorylink"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ConnectionArn=json_data.get("ConnectionArn"),
            ProviderType=json_data.get("ProviderType"),
            OwnerId=json_data.get("OwnerId"),
            RepositoryName=json_data.get("RepositoryName"),
            EncryptionKeyArn=json_data.get("EncryptionKeyArn"),
            RepositoryLinkId=json_data.get("RepositoryLinkId"),
            RepositoryLinkArn=json_data.get("RepositoryLinkArn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCodestarconnectionsRepositorylink = AwsCodestarconnectionsRepositorylink


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


