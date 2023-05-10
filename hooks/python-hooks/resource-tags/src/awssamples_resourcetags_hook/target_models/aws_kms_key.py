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
class AwsKmsKey(BaseModel):
    Description: Optional[str]
    Enabled: Optional[bool]
    EnableKeyRotation: Optional[bool]
    KeyPolicy: Optional[Any]
    KeyUsage: Optional[str]
    KeySpec: Optional[str]
    MultiRegion: Optional[bool]
    PendingWindowInDays: Optional[int]
    Tags: Optional[Any]
    Arn: Optional[str]
    KeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsKmsKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsKmsKey"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            EnableKeyRotation=json_data.get("EnableKeyRotation"),
            KeyPolicy=json_data.get("KeyPolicy"),
            KeyUsage=json_data.get("KeyUsage"),
            KeySpec=json_data.get("KeySpec"),
            MultiRegion=json_data.get("MultiRegion"),
            PendingWindowInDays=json_data.get("PendingWindowInDays"),
            Tags=json_data.get("Tags"),
            Arn=json_data.get("Arn"),
            KeyId=json_data.get("KeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsKmsKey = AwsKmsKey


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


