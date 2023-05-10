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
class AwsIotwirelessTaskdefinition(BaseModel):
    Name: Optional[str]
    AutoCreateTasks: Optional[bool]
    Update: Optional["_UpdateWirelessGatewayTaskCreate"]
    LoRaWANUpdateGatewayTaskEntry: Optional["_LoRaWANUpdateGatewayTaskEntry"]
    Id: Optional[str]
    TaskDefinitionType: Optional[str]
    Arn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotwirelessTaskdefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotwirelessTaskdefinition"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            AutoCreateTasks=json_data.get("AutoCreateTasks"),
            Update=UpdateWirelessGatewayTaskCreate._deserialize(json_data.get("Update")),
            LoRaWANUpdateGatewayTaskEntry=LoRaWANUpdateGatewayTaskEntry._deserialize(json_data.get("LoRaWANUpdateGatewayTaskEntry")),
            Id=json_data.get("Id"),
            TaskDefinitionType=json_data.get("TaskDefinitionType"),
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotwirelessTaskdefinition = AwsIotwirelessTaskdefinition


@dataclass
class UpdateWirelessGatewayTaskCreate(BaseModel):
    UpdateDataSource: Optional[str]
    UpdateDataRole: Optional[str]
    LoRaWAN: Optional["_LoRaWANUpdateGatewayTaskCreate"]

    @classmethod
    def _deserialize(
        cls: Type["_UpdateWirelessGatewayTaskCreate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpdateWirelessGatewayTaskCreate"]:
        if not json_data:
            return None
        return cls(
            UpdateDataSource=json_data.get("UpdateDataSource"),
            UpdateDataRole=json_data.get("UpdateDataRole"),
            LoRaWAN=LoRaWANUpdateGatewayTaskCreate._deserialize(json_data.get("LoRaWAN")),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpdateWirelessGatewayTaskCreate = UpdateWirelessGatewayTaskCreate


@dataclass
class LoRaWANUpdateGatewayTaskCreate(BaseModel):
    UpdateSignature: Optional[str]
    SigKeyCrc: Optional[int]
    CurrentVersion: Optional["_LoRaWANGatewayVersion"]
    UpdateVersion: Optional["_LoRaWANGatewayVersion"]

    @classmethod
    def _deserialize(
        cls: Type["_LoRaWANUpdateGatewayTaskCreate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoRaWANUpdateGatewayTaskCreate"]:
        if not json_data:
            return None
        return cls(
            UpdateSignature=json_data.get("UpdateSignature"),
            SigKeyCrc=json_data.get("SigKeyCrc"),
            CurrentVersion=LoRaWANGatewayVersion._deserialize(json_data.get("CurrentVersion")),
            UpdateVersion=LoRaWANGatewayVersion._deserialize(json_data.get("UpdateVersion")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoRaWANUpdateGatewayTaskCreate = LoRaWANUpdateGatewayTaskCreate


@dataclass
class LoRaWANGatewayVersion(BaseModel):
    PackageVersion: Optional[str]
    Model: Optional[str]
    Station: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoRaWANGatewayVersion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoRaWANGatewayVersion"]:
        if not json_data:
            return None
        return cls(
            PackageVersion=json_data.get("PackageVersion"),
            Model=json_data.get("Model"),
            Station=json_data.get("Station"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoRaWANGatewayVersion = LoRaWANGatewayVersion


@dataclass
class LoRaWANUpdateGatewayTaskEntry(BaseModel):
    CurrentVersion: Optional["_LoRaWANGatewayVersion"]
    UpdateVersion: Optional["_LoRaWANGatewayVersion"]

    @classmethod
    def _deserialize(
        cls: Type["_LoRaWANUpdateGatewayTaskEntry"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoRaWANUpdateGatewayTaskEntry"]:
        if not json_data:
            return None
        return cls(
            CurrentVersion=LoRaWANGatewayVersion._deserialize(json_data.get("CurrentVersion")),
            UpdateVersion=LoRaWANGatewayVersion._deserialize(json_data.get("UpdateVersion")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoRaWANUpdateGatewayTaskEntry = LoRaWANUpdateGatewayTaskEntry


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


