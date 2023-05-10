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
class AwsSagemakerDevicefleet(BaseModel):
    Description: Optional[str]
    DeviceFleetName: Optional[str]
    OutputConfig: Optional["_EdgeOutputConfig"]
    RoleArn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSagemakerDevicefleet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSagemakerDevicefleet"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            DeviceFleetName=json_data.get("DeviceFleetName"),
            OutputConfig=EdgeOutputConfig._deserialize(json_data.get("OutputConfig")),
            RoleArn=json_data.get("RoleArn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSagemakerDevicefleet = AwsSagemakerDevicefleet


@dataclass
class EdgeOutputConfig(BaseModel):
    S3OutputLocation: Optional[str]
    KmsKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EdgeOutputConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EdgeOutputConfig"]:
        if not json_data:
            return None
        return cls(
            S3OutputLocation=json_data.get("S3OutputLocation"),
            KmsKeyId=json_data.get("KmsKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EdgeOutputConfig = EdgeOutputConfig


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


