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
class AwsOmicsVariantstore(BaseModel):
    CreationTime: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Reference: Optional["_ReferenceItem"]
    SseConfig: Optional["_SseConfig"]
    Status: Optional[str]
    StatusMessage: Optional[str]
    StoreArn: Optional[str]
    StoreSizeBytes: Optional[float]
    Tags: Optional[Any]
    UpdateTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsOmicsVariantstore"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsOmicsVariantstore"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CreationTime=json_data.get("CreationTime"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Reference=ReferenceItem._deserialize(json_data.get("Reference")),
            SseConfig=SseConfig._deserialize(json_data.get("SseConfig")),
            Status=json_data.get("Status"),
            StatusMessage=json_data.get("StatusMessage"),
            StoreArn=json_data.get("StoreArn"),
            StoreSizeBytes=json_data.get("StoreSizeBytes"),
            Tags=json_data.get("Tags"),
            UpdateTime=json_data.get("UpdateTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsOmicsVariantstore = AwsOmicsVariantstore


@dataclass
class ReferenceItem(BaseModel):
    ReferenceArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReferenceItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReferenceItem"]:
        if not json_data:
            return None
        return cls(
            ReferenceArn=json_data.get("ReferenceArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReferenceItem = ReferenceItem


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


