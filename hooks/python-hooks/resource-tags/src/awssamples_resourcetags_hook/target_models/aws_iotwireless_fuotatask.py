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
class AwsIotwirelessFuotatask(BaseModel):
    Name: Optional[str]
    Description: Optional[str]
    LoRaWAN: Optional["_LoRaWAN"]
    FirmwareUpdateImage: Optional[str]
    FirmwareUpdateRole: Optional[str]
    Arn: Optional[str]
    Id: Optional[str]
    Tags: Optional[Any]
    FuotaTaskStatus: Optional[str]
    AssociateWirelessDevice: Optional[str]
    DisassociateWirelessDevice: Optional[str]
    AssociateMulticastGroup: Optional[str]
    DisassociateMulticastGroup: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotwirelessFuotatask"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotwirelessFuotatask"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            LoRaWAN=LoRaWAN._deserialize(json_data.get("LoRaWAN")),
            FirmwareUpdateImage=json_data.get("FirmwareUpdateImage"),
            FirmwareUpdateRole=json_data.get("FirmwareUpdateRole"),
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
            FuotaTaskStatus=json_data.get("FuotaTaskStatus"),
            AssociateWirelessDevice=json_data.get("AssociateWirelessDevice"),
            DisassociateWirelessDevice=json_data.get("DisassociateWirelessDevice"),
            AssociateMulticastGroup=json_data.get("AssociateMulticastGroup"),
            DisassociateMulticastGroup=json_data.get("DisassociateMulticastGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotwirelessFuotatask = AwsIotwirelessFuotatask


@dataclass
class LoRaWAN(BaseModel):
    StartTime: Optional[str]
    RfRegion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoRaWAN"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoRaWAN"]:
        if not json_data:
            return None
        return cls(
            StartTime=json_data.get("StartTime"),
            RfRegion=json_data.get("RfRegion"),
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


