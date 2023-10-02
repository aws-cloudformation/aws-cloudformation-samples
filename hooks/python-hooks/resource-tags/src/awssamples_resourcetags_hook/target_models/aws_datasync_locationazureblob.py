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
class AwsDatasyncLocationazureblob(BaseModel):
    AgentArns: Optional[Sequence[str]]
    AzureBlobAuthenticationType: Optional[str]
    AzureBlobSasConfiguration: Optional["_AzureBlobSasConfiguration"]
    AzureBlobContainerUrl: Optional[str]
    AzureBlobType: Optional[str]
    AzureAccessTier: Optional[str]
    Subdirectory: Optional[str]
    Tags: Optional[Any]
    LocationArn: Optional[str]
    LocationUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDatasyncLocationazureblob"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDatasyncLocationazureblob"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AgentArns=json_data.get("AgentArns"),
            AzureBlobAuthenticationType=json_data.get("AzureBlobAuthenticationType"),
            AzureBlobSasConfiguration=AzureBlobSasConfiguration._deserialize(json_data.get("AzureBlobSasConfiguration")),
            AzureBlobContainerUrl=json_data.get("AzureBlobContainerUrl"),
            AzureBlobType=json_data.get("AzureBlobType"),
            AzureAccessTier=json_data.get("AzureAccessTier"),
            Subdirectory=json_data.get("Subdirectory"),
            Tags=json_data.get("Tags"),
            LocationArn=json_data.get("LocationArn"),
            LocationUri=json_data.get("LocationUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDatasyncLocationazureblob = AwsDatasyncLocationazureblob


@dataclass
class AzureBlobSasConfiguration(BaseModel):
    AzureBlobSasToken: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureBlobSasConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureBlobSasConfiguration"]:
        if not json_data:
            return None
        return cls(
            AzureBlobSasToken=json_data.get("AzureBlobSasToken"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureBlobSasConfiguration = AzureBlobSasConfiguration


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


