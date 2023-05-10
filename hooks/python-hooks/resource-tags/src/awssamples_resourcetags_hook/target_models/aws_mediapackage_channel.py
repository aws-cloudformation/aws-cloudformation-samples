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
class AwsMediapackageChannel(BaseModel):
    Arn: Optional[str]
    Id: Optional[str]
    Description: Optional[str]
    HlsIngest: Optional["_HlsIngest"]
    Tags: Optional[Any]
    EgressAccessLogs: Optional["_LogConfiguration"]
    IngressAccessLogs: Optional["_LogConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMediapackageChannel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMediapackageChannel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            Description=json_data.get("Description"),
            HlsIngest=HlsIngest._deserialize(json_data.get("HlsIngest")),
            Tags=json_data.get("Tags"),
            EgressAccessLogs=LogConfiguration._deserialize(json_data.get("EgressAccessLogs")),
            IngressAccessLogs=LogConfiguration._deserialize(json_data.get("IngressAccessLogs")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMediapackageChannel = AwsMediapackageChannel


@dataclass
class HlsIngest(BaseModel):
    ingestEndpoints: Optional[Sequence["_IngestEndpoint"]]

    @classmethod
    def _deserialize(
        cls: Type["_HlsIngest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HlsIngest"]:
        if not json_data:
            return None
        return cls(
            ingestEndpoints=deserialize_list(json_data.get("ingestEndpoints"), IngestEndpoint),
        )


# work around possible type aliasing issues when variable has same name as a model
_HlsIngest = HlsIngest


@dataclass
class IngestEndpoint(BaseModel):
    Id: Optional[str]
    Username: Optional[str]
    Password: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IngestEndpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngestEndpoint"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Username=json_data.get("Username"),
            Password=json_data.get("Password"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngestEndpoint = IngestEndpoint


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


@dataclass
class LogConfiguration(BaseModel):
    LogGroupName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogConfiguration"]:
        if not json_data:
            return None
        return cls(
            LogGroupName=json_data.get("LogGroupName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogConfiguration = LogConfiguration


