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
class AwsGreengrassDevicedefinition(BaseModel):
    LatestVersionArn: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    Name: Optional[str]
    InitialVersion: Optional["_DeviceDefinitionVersion"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGreengrassDevicedefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGreengrassDevicedefinition"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            LatestVersionArn=json_data.get("LatestVersionArn"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            InitialVersion=DeviceDefinitionVersion._deserialize(json_data.get("InitialVersion")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGreengrassDevicedefinition = AwsGreengrassDevicedefinition


@dataclass
class DeviceDefinitionVersion(BaseModel):
    Devices: Optional[Sequence["_Device"]]

    @classmethod
    def _deserialize(
        cls: Type["_DeviceDefinitionVersion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeviceDefinitionVersion"]:
        if not json_data:
            return None
        return cls(
            Devices=deserialize_list(json_data.get("Devices"), Device),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeviceDefinitionVersion = DeviceDefinitionVersion


@dataclass
class Device(BaseModel):
    SyncShadow: Optional[bool]
    ThingArn: Optional[str]
    Id: Optional[str]
    CertificateArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Device"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Device"]:
        if not json_data:
            return None
        return cls(
            SyncShadow=json_data.get("SyncShadow"),
            ThingArn=json_data.get("ThingArn"),
            Id=json_data.get("Id"),
            CertificateArn=json_data.get("CertificateArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Device = Device


