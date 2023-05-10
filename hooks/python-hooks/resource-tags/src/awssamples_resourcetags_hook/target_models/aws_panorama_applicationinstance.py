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
class AwsPanoramaApplicationinstance(BaseModel):
    Name: Optional[str]
    Description: Optional[str]
    ManifestPayload: Optional["_ManifestPayload"]
    ManifestOverridesPayload: Optional["_ManifestOverridesPayload"]
    RuntimeRoleArn: Optional[str]
    DefaultRuntimeContextDevice: Optional[str]
    DefaultRuntimeContextDeviceName: Optional[str]
    ApplicationInstanceId: Optional[str]
    ApplicationInstanceIdToReplace: Optional[str]
    DeviceId: Optional[str]
    StatusFilter: Optional[str]
    Status: Optional[str]
    HealthStatus: Optional[str]
    StatusDescription: Optional[str]
    CreatedTime: Optional[int]
    LastUpdatedTime: Optional[int]
    Arn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsPanoramaApplicationinstance"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsPanoramaApplicationinstance"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            ManifestPayload=ManifestPayload._deserialize(json_data.get("ManifestPayload")),
            ManifestOverridesPayload=ManifestOverridesPayload._deserialize(json_data.get("ManifestOverridesPayload")),
            RuntimeRoleArn=json_data.get("RuntimeRoleArn"),
            DefaultRuntimeContextDevice=json_data.get("DefaultRuntimeContextDevice"),
            DefaultRuntimeContextDeviceName=json_data.get("DefaultRuntimeContextDeviceName"),
            ApplicationInstanceId=json_data.get("ApplicationInstanceId"),
            ApplicationInstanceIdToReplace=json_data.get("ApplicationInstanceIdToReplace"),
            DeviceId=json_data.get("DeviceId"),
            StatusFilter=json_data.get("StatusFilter"),
            Status=json_data.get("Status"),
            HealthStatus=json_data.get("HealthStatus"),
            StatusDescription=json_data.get("StatusDescription"),
            CreatedTime=json_data.get("CreatedTime"),
            LastUpdatedTime=json_data.get("LastUpdatedTime"),
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsPanoramaApplicationinstance = AwsPanoramaApplicationinstance


@dataclass
class ManifestPayload(BaseModel):
    PayloadData: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ManifestPayload"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManifestPayload"]:
        if not json_data:
            return None
        return cls(
            PayloadData=json_data.get("PayloadData"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManifestPayload = ManifestPayload


@dataclass
class ManifestOverridesPayload(BaseModel):
    PayloadData: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ManifestOverridesPayload"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManifestOverridesPayload"]:
        if not json_data:
            return None
        return cls(
            PayloadData=json_data.get("PayloadData"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManifestOverridesPayload = ManifestOverridesPayload


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


