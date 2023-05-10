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
class AwsIotwirelessMulticastgroup(BaseModel):
    Name: Optional[str]
    Description: Optional[str]
    LoRaWAN: Optional["_LoRaWAN"]
    Arn: Optional[str]
    Id: Optional[str]
    Tags: Optional[Any]
    Status: Optional[str]
    AssociateWirelessDevice: Optional[str]
    DisassociateWirelessDevice: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotwirelessMulticastgroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotwirelessMulticastgroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            LoRaWAN=LoRaWAN._deserialize(json_data.get("LoRaWAN")),
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
            Status=json_data.get("Status"),
            AssociateWirelessDevice=json_data.get("AssociateWirelessDevice"),
            DisassociateWirelessDevice=json_data.get("DisassociateWirelessDevice"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotwirelessMulticastgroup = AwsIotwirelessMulticastgroup


@dataclass
class LoRaWAN(BaseModel):
    RfRegion: Optional[str]
    DlClass: Optional[str]
    NumberOfDevicesRequested: Optional[int]
    NumberOfDevicesInGroup: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_LoRaWAN"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoRaWAN"]:
        if not json_data:
            return None
        return cls(
            RfRegion=json_data.get("RfRegion"),
            DlClass=json_data.get("DlClass"),
            NumberOfDevicesRequested=json_data.get("NumberOfDevicesRequested"),
            NumberOfDevicesInGroup=json_data.get("NumberOfDevicesInGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoRaWAN = LoRaWAN


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


