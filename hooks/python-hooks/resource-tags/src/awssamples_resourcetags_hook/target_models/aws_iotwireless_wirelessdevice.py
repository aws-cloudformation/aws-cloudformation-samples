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
class AwsIotwirelessWirelessdevice(BaseModel):
    Type: Optional[str]
    Name: Optional[str]
    Description: Optional[str]
    DestinationName: Optional[str]
    LoRaWAN: Optional["_LoRaWANDevice"]
    Tags: Optional[Any]
    Arn: Optional[str]
    Id: Optional[str]
    ThingArn: Optional[str]
    ThingName: Optional[str]
    LastUplinkReceivedAt: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotwirelessWirelessdevice"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotwirelessWirelessdevice"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Type=json_data.get("Type"),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            DestinationName=json_data.get("DestinationName"),
            LoRaWAN=LoRaWANDevice._deserialize(json_data.get("LoRaWAN")),
            Tags=json_data.get("Tags"),
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            ThingArn=json_data.get("ThingArn"),
            ThingName=json_data.get("ThingName"),
            LastUplinkReceivedAt=json_data.get("LastUplinkReceivedAt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotwirelessWirelessdevice = AwsIotwirelessWirelessdevice


@dataclass
class LoRaWANDevice(BaseModel):
    DevEui: Optional[str]
    DeviceProfileId: Optional[str]
    ServiceProfileId: Optional[str]
    OtaaV11: Optional["_OtaaV11"]
    OtaaV10x: Optional["_OtaaV10x"]
    AbpV11: Optional["_AbpV11"]
    AbpV10x: Optional["_AbpV10x"]

    @classmethod
    def _deserialize(
        cls: Type["_LoRaWANDevice"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoRaWANDevice"]:
        if not json_data:
            return None
        return cls(
            DevEui=json_data.get("DevEui"),
            DeviceProfileId=json_data.get("DeviceProfileId"),
            ServiceProfileId=json_data.get("ServiceProfileId"),
            OtaaV11=OtaaV11._deserialize(json_data.get("OtaaV11")),
            OtaaV10x=OtaaV10x._deserialize(json_data.get("OtaaV10x")),
            AbpV11=AbpV11._deserialize(json_data.get("AbpV11")),
            AbpV10x=AbpV10x._deserialize(json_data.get("AbpV10x")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoRaWANDevice = LoRaWANDevice


@dataclass
class OtaaV11(BaseModel):
    AppKey: Optional[str]
    NwkKey: Optional[str]
    JoinEui: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OtaaV11"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OtaaV11"]:
        if not json_data:
            return None
        return cls(
            AppKey=json_data.get("AppKey"),
            NwkKey=json_data.get("NwkKey"),
            JoinEui=json_data.get("JoinEui"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OtaaV11 = OtaaV11


@dataclass
class OtaaV10x(BaseModel):
    AppKey: Optional[str]
    AppEui: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OtaaV10x"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OtaaV10x"]:
        if not json_data:
            return None
        return cls(
            AppKey=json_data.get("AppKey"),
            AppEui=json_data.get("AppEui"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OtaaV10x = OtaaV10x


@dataclass
class AbpV11(BaseModel):
    DevAddr: Optional[str]
    SessionKeys: Optional["_SessionKeysAbpV11"]

    @classmethod
    def _deserialize(
        cls: Type["_AbpV11"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AbpV11"]:
        if not json_data:
            return None
        return cls(
            DevAddr=json_data.get("DevAddr"),
            SessionKeys=SessionKeysAbpV11._deserialize(json_data.get("SessionKeys")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AbpV11 = AbpV11


@dataclass
class SessionKeysAbpV11(BaseModel):
    FNwkSIntKey: Optional[str]
    SNwkSIntKey: Optional[str]
    NwkSEncKey: Optional[str]
    AppSKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SessionKeysAbpV11"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SessionKeysAbpV11"]:
        if not json_data:
            return None
        return cls(
            FNwkSIntKey=json_data.get("FNwkSIntKey"),
            SNwkSIntKey=json_data.get("SNwkSIntKey"),
            NwkSEncKey=json_data.get("NwkSEncKey"),
            AppSKey=json_data.get("AppSKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SessionKeysAbpV11 = SessionKeysAbpV11


@dataclass
class AbpV10x(BaseModel):
    DevAddr: Optional[str]
    SessionKeys: Optional["_SessionKeysAbpV10x"]

    @classmethod
    def _deserialize(
        cls: Type["_AbpV10x"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AbpV10x"]:
        if not json_data:
            return None
        return cls(
            DevAddr=json_data.get("DevAddr"),
            SessionKeys=SessionKeysAbpV10x._deserialize(json_data.get("SessionKeys")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AbpV10x = AbpV10x


@dataclass
class SessionKeysAbpV10x(BaseModel):
    NwkSKey: Optional[str]
    AppSKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SessionKeysAbpV10x"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SessionKeysAbpV10x"]:
        if not json_data:
            return None
        return cls(
            NwkSKey=json_data.get("NwkSKey"),
            AppSKey=json_data.get("AppSKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SessionKeysAbpV10x = SessionKeysAbpV10x


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


