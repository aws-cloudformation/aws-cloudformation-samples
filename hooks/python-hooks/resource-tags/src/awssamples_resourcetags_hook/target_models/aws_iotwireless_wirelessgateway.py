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
class AwsIotwirelessWirelessgateway(BaseModel):
    Name: Optional[str]
    Description: Optional[str]
    Tags: Optional[Any]
    LoRaWAN: Optional["_LoRaWANGateway"]
    Arn: Optional[str]
    Id: Optional[str]
    ThingArn: Optional[str]
    ThingName: Optional[str]
    LastUplinkReceivedAt: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotwirelessWirelessgateway"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotwirelessWirelessgateway"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            Tags=json_data.get("Tags"),
            LoRaWAN=LoRaWANGateway._deserialize(json_data.get("LoRaWAN")),
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            ThingArn=json_data.get("ThingArn"),
            ThingName=json_data.get("ThingName"),
            LastUplinkReceivedAt=json_data.get("LastUplinkReceivedAt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotwirelessWirelessgateway = AwsIotwirelessWirelessgateway


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


@dataclass
class LoRaWANGateway(BaseModel):
    GatewayEui: Optional[str]
    RfRegion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoRaWANGateway"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoRaWANGateway"]:
        if not json_data:
            return None
        return cls(
            GatewayEui=json_data.get("GatewayEui"),
            RfRegion=json_data.get("RfRegion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoRaWANGateway = LoRaWANGateway


