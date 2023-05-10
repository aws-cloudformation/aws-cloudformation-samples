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
class AwsIotwirelessServiceprofile(BaseModel):
    Name: Optional[str]
    LoRaWAN: Optional["_LoRaWANServiceProfile"]
    Tags: Optional[Any]
    Arn: Optional[str]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotwirelessServiceprofile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotwirelessServiceprofile"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            LoRaWAN=LoRaWANServiceProfile._deserialize(json_data.get("LoRaWAN")),
            Tags=json_data.get("Tags"),
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotwirelessServiceprofile = AwsIotwirelessServiceprofile


@dataclass
class LoRaWANServiceProfile(BaseModel):
    UlRate: Optional[int]
    UlBucketSize: Optional[int]
    UlRatePolicy: Optional[str]
    DlRate: Optional[int]
    DlBucketSize: Optional[int]
    DlRatePolicy: Optional[str]
    AddGwMetadata: Optional[bool]
    DevStatusReqFreq: Optional[int]
    ReportDevStatusBattery: Optional[bool]
    ReportDevStatusMargin: Optional[bool]
    DrMin: Optional[int]
    DrMax: Optional[int]
    ChannelMask: Optional[str]
    PrAllowed: Optional[bool]
    HrAllowed: Optional[bool]
    RaAllowed: Optional[bool]
    NwkGeoLoc: Optional[bool]
    TargetPer: Optional[int]
    MinGwDiversity: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_LoRaWANServiceProfile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoRaWANServiceProfile"]:
        if not json_data:
            return None
        return cls(
            UlRate=json_data.get("UlRate"),
            UlBucketSize=json_data.get("UlBucketSize"),
            UlRatePolicy=json_data.get("UlRatePolicy"),
            DlRate=json_data.get("DlRate"),
            DlBucketSize=json_data.get("DlBucketSize"),
            DlRatePolicy=json_data.get("DlRatePolicy"),
            AddGwMetadata=json_data.get("AddGwMetadata"),
            DevStatusReqFreq=json_data.get("DevStatusReqFreq"),
            ReportDevStatusBattery=json_data.get("ReportDevStatusBattery"),
            ReportDevStatusMargin=json_data.get("ReportDevStatusMargin"),
            DrMin=json_data.get("DrMin"),
            DrMax=json_data.get("DrMax"),
            ChannelMask=json_data.get("ChannelMask"),
            PrAllowed=json_data.get("PrAllowed"),
            HrAllowed=json_data.get("HrAllowed"),
            RaAllowed=json_data.get("RaAllowed"),
            NwkGeoLoc=json_data.get("NwkGeoLoc"),
            TargetPer=json_data.get("TargetPer"),
            MinGwDiversity=json_data.get("MinGwDiversity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoRaWANServiceProfile = LoRaWANServiceProfile


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


