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
class AwsMedialiveMultiplex(BaseModel):
    Arn: Optional[str]
    AvailabilityZones: Optional[Sequence[str]]
    Destinations: Optional[Sequence["_MultiplexOutputDestination"]]
    Id: Optional[str]
    MultiplexSettings: Optional["_MultiplexSettings"]
    Name: Optional[str]
    PipelinesRunningCount: Optional[int]
    ProgramCount: Optional[int]
    State: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMedialiveMultiplex"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMedialiveMultiplex"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            AvailabilityZones=json_data.get("AvailabilityZones"),
            Destinations=deserialize_list(json_data.get("Destinations"), MultiplexOutputDestination),
            Id=json_data.get("Id"),
            MultiplexSettings=MultiplexSettings._deserialize(json_data.get("MultiplexSettings")),
            Name=json_data.get("Name"),
            PipelinesRunningCount=json_data.get("PipelinesRunningCount"),
            ProgramCount=json_data.get("ProgramCount"),
            State=json_data.get("State"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMedialiveMultiplex = AwsMedialiveMultiplex


@dataclass
class MultiplexOutputDestination(BaseModel):
    MultiplexMediaConnectOutputDestinationSettings: Optional["_MultiplexMediaConnectOutputDestinationSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_MultiplexOutputDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MultiplexOutputDestination"]:
        if not json_data:
            return None
        return cls(
            MultiplexMediaConnectOutputDestinationSettings=MultiplexMediaConnectOutputDestinationSettings._deserialize(json_data.get("MultiplexMediaConnectOutputDestinationSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MultiplexOutputDestination = MultiplexOutputDestination


@dataclass
class MultiplexMediaConnectOutputDestinationSettings(BaseModel):
    EntitlementArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MultiplexMediaConnectOutputDestinationSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MultiplexMediaConnectOutputDestinationSettings"]:
        if not json_data:
            return None
        return cls(
            EntitlementArn=json_data.get("EntitlementArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MultiplexMediaConnectOutputDestinationSettings = MultiplexMediaConnectOutputDestinationSettings


@dataclass
class MultiplexSettings(BaseModel):
    MaximumVideoBufferDelayMilliseconds: Optional[int]
    TransportStreamBitrate: Optional[int]
    TransportStreamId: Optional[int]
    TransportStreamReservedBitrate: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_MultiplexSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MultiplexSettings"]:
        if not json_data:
            return None
        return cls(
            MaximumVideoBufferDelayMilliseconds=json_data.get("MaximumVideoBufferDelayMilliseconds"),
            TransportStreamBitrate=json_data.get("TransportStreamBitrate"),
            TransportStreamId=json_data.get("TransportStreamId"),
            TransportStreamReservedBitrate=json_data.get("TransportStreamReservedBitrate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MultiplexSettings = MultiplexSettings


@dataclass
class Tags(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


