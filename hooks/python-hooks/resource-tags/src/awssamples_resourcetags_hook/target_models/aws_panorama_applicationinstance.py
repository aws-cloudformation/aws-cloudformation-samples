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
    DefaultRuntimeContextDeviceName: Optional[str]
    Status: Optional[str]
    DefaultRuntimeContextDevice: Optional[str]
    Description: Optional[str]
    ApplicationInstanceIdToReplace: Optional[str]
    CreatedTime: Optional[int]
    HealthStatus: Optional[str]
    ManifestOverridesPayload: Optional["_ManifestOverridesPayload"]
    LastUpdatedTime: Optional[int]
    RuntimeRoleArn: Optional[str]
    Name: Optional[str]
    ApplicationInstanceId: Optional[str]
    StatusDescription: Optional[str]
    ManifestPayload: Optional["_ManifestPayload"]
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
            DefaultRuntimeContextDeviceName=json_data.get("DefaultRuntimeContextDeviceName"),
            Status=json_data.get("Status"),
            DefaultRuntimeContextDevice=json_data.get("DefaultRuntimeContextDevice"),
            Description=json_data.get("Description"),
            ApplicationInstanceIdToReplace=json_data.get("ApplicationInstanceIdToReplace"),
            CreatedTime=json_data.get("CreatedTime"),
            HealthStatus=json_data.get("HealthStatus"),
            ManifestOverridesPayload=ManifestOverridesPayload._deserialize(json_data.get("ManifestOverridesPayload")),
            LastUpdatedTime=json_data.get("LastUpdatedTime"),
            RuntimeRoleArn=json_data.get("RuntimeRoleArn"),
            Name=json_data.get("Name"),
            ApplicationInstanceId=json_data.get("ApplicationInstanceId"),
            StatusDescription=json_data.get("StatusDescription"),
            ManifestPayload=ManifestPayload._deserialize(json_data.get("ManifestPayload")),
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsPanoramaApplicationinstance = AwsPanoramaApplicationinstance


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
class Tag(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


