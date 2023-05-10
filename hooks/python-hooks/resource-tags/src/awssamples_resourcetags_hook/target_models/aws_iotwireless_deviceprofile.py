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
class AwsIotwirelessDeviceprofile(BaseModel):
    Name: Optional[str]
    LoRaWAN: Optional["_LoRaWANDeviceProfile"]
    Tags: Optional[Any]
    Arn: Optional[str]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotwirelessDeviceprofile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotwirelessDeviceprofile"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            LoRaWAN=LoRaWANDeviceProfile._deserialize(json_data.get("LoRaWAN")),
            Tags=json_data.get("Tags"),
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotwirelessDeviceprofile = AwsIotwirelessDeviceprofile


@dataclass
class LoRaWANDeviceProfile(BaseModel):
    SupportsClassB: Optional[bool]
    ClassBTimeout: Optional[int]
    PingSlotPeriod: Optional[int]
    PingSlotDr: Optional[int]
    PingSlotFreq: Optional[int]
    SupportsClassC: Optional[bool]
    ClassCTimeout: Optional[int]
    MacVersion: Optional[str]
    RegParamsRevision: Optional[str]
    RxDelay1: Optional[int]
    RxDrOffset1: Optional[int]
    RxFreq2: Optional[int]
    RxDataRate2: Optional[int]
    FactoryPresetFreqsList: Optional[Sequence[int]]
    MaxEirp: Optional[int]
    MaxDutyCycle: Optional[int]
    SupportsJoin: Optional[bool]
    RfRegion: Optional[str]
    Supports32BitFCnt: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_LoRaWANDeviceProfile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoRaWANDeviceProfile"]:
        if not json_data:
            return None
        return cls(
            SupportsClassB=json_data.get("SupportsClassB"),
            ClassBTimeout=json_data.get("ClassBTimeout"),
            PingSlotPeriod=json_data.get("PingSlotPeriod"),
            PingSlotDr=json_data.get("PingSlotDr"),
            PingSlotFreq=json_data.get("PingSlotFreq"),
            SupportsClassC=json_data.get("SupportsClassC"),
            ClassCTimeout=json_data.get("ClassCTimeout"),
            MacVersion=json_data.get("MacVersion"),
            RegParamsRevision=json_data.get("RegParamsRevision"),
            RxDelay1=json_data.get("RxDelay1"),
            RxDrOffset1=json_data.get("RxDrOffset1"),
            RxFreq2=json_data.get("RxFreq2"),
            RxDataRate2=json_data.get("RxDataRate2"),
            FactoryPresetFreqsList=json_data.get("FactoryPresetFreqsList"),
            MaxEirp=json_data.get("MaxEirp"),
            MaxDutyCycle=json_data.get("MaxDutyCycle"),
            SupportsJoin=json_data.get("SupportsJoin"),
            RfRegion=json_data.get("RfRegion"),
            Supports32BitFCnt=json_data.get("Supports32BitFCnt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoRaWANDeviceProfile = LoRaWANDeviceProfile


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


