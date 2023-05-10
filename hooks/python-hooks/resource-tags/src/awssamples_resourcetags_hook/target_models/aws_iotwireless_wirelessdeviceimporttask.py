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
class AwsIotwirelessWirelessdeviceimporttask(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]
    DestinationName: Optional[str]
    CreationDate: Optional[str]
    Sidewalk: Optional["_Sidewalk"]
    Status: Optional[str]
    StatusReason: Optional[str]
    InitializedImportedDevicesCount: Optional[int]
    PendingImportedDevicesCount: Optional[int]
    OnboardedImportedDevicesCount: Optional[int]
    FailedImportedDevicesCount: Optional[int]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotwirelessWirelessdeviceimporttask"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotwirelessWirelessdeviceimporttask"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            DestinationName=json_data.get("DestinationName"),
            CreationDate=json_data.get("CreationDate"),
            Sidewalk=Sidewalk._deserialize(json_data.get("Sidewalk")),
            Status=json_data.get("Status"),
            StatusReason=json_data.get("StatusReason"),
            InitializedImportedDevicesCount=json_data.get("InitializedImportedDevicesCount"),
            PendingImportedDevicesCount=json_data.get("PendingImportedDevicesCount"),
            OnboardedImportedDevicesCount=json_data.get("OnboardedImportedDevicesCount"),
            FailedImportedDevicesCount=json_data.get("FailedImportedDevicesCount"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotwirelessWirelessdeviceimporttask = AwsIotwirelessWirelessdeviceimporttask


@dataclass
class Sidewalk(BaseModel):
    SidewalkManufacturingSn: Optional[str]
    DeviceCreationFile: Optional[str]
    DeviceCreationFileList: Optional[Sequence[str]]
    Role: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Sidewalk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sidewalk"]:
        if not json_data:
            return None
        return cls(
            SidewalkManufacturingSn=json_data.get("SidewalkManufacturingSn"),
            DeviceCreationFile=json_data.get("DeviceCreationFile"),
            DeviceCreationFileList=json_data.get("DeviceCreationFileList"),
            Role=json_data.get("Role"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sidewalk = Sidewalk


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


