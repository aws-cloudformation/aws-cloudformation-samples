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
class AwsOmicsSequencestore(BaseModel):
    Arn: Optional[str]
    CreationTime: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    FallbackLocation: Optional[str]
    SequenceStoreId: Optional[str]
    SseConfig: Optional["_SseConfig"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsOmicsSequencestore"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsOmicsSequencestore"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            CreationTime=json_data.get("CreationTime"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            FallbackLocation=json_data.get("FallbackLocation"),
            SequenceStoreId=json_data.get("SequenceStoreId"),
            SseConfig=SseConfig._deserialize(json_data.get("SseConfig")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsOmicsSequencestore = AwsOmicsSequencestore


@dataclass
class SseConfig(BaseModel):
    Type: Optional[str]
    KeyArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SseConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SseConfig"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            KeyArn=json_data.get("KeyArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SseConfig = SseConfig


