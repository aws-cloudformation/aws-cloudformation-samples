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
class AwsWisdomAssistant(BaseModel):
    Type: Optional[str]
    Description: Optional[str]
    AssistantArn: Optional[str]
    AssistantId: Optional[str]
    ServerSideEncryptionConfiguration: Optional["_ServerSideEncryptionConfiguration"]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsWisdomAssistant"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsWisdomAssistant"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Type=json_data.get("Type"),
            Description=json_data.get("Description"),
            AssistantArn=json_data.get("AssistantArn"),
            AssistantId=json_data.get("AssistantId"),
            ServerSideEncryptionConfiguration=ServerSideEncryptionConfiguration._deserialize(json_data.get("ServerSideEncryptionConfiguration")),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsWisdomAssistant = AwsWisdomAssistant


@dataclass
class ServerSideEncryptionConfiguration(BaseModel):
    KmsKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerSideEncryptionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerSideEncryptionConfiguration"]:
        if not json_data:
            return None
        return cls(
            KmsKeyId=json_data.get("KmsKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerSideEncryptionConfiguration = ServerSideEncryptionConfiguration


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


