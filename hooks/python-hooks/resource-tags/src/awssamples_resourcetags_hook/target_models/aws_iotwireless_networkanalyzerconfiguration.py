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
class AwsIotwirelessNetworkanalyzerconfiguration(BaseModel):
    Name: Optional[str]
    Description: Optional[str]
    TraceContent: Optional["_TraceContent"]
    WirelessDevices: Optional[Sequence[str]]
    WirelessGateways: Optional[Sequence[str]]
    Arn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotwirelessNetworkanalyzerconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotwirelessNetworkanalyzerconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            TraceContent=TraceContent._deserialize(json_data.get("TraceContent")),
            WirelessDevices=json_data.get("WirelessDevices"),
            WirelessGateways=json_data.get("WirelessGateways"),
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotwirelessNetworkanalyzerconfiguration = AwsIotwirelessNetworkanalyzerconfiguration


@dataclass
class TraceContent(BaseModel):
    WirelessDeviceFrameInfo: Optional[str]
    LogLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TraceContent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TraceContent"]:
        if not json_data:
            return None
        return cls(
            WirelessDeviceFrameInfo=json_data.get("WirelessDeviceFrameInfo"),
            LogLevel=json_data.get("LogLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TraceContent = TraceContent


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


