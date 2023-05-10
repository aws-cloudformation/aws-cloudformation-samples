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
class AwsRoute53Hostedzone(BaseModel):
    Id: Optional[str]
    HostedZoneConfig: Optional["_HostedZoneConfig"]
    HostedZoneTags: Optional[AbstractSet["_HostedZoneTag"]]
    Name: Optional[str]
    QueryLoggingConfig: Optional["_QueryLoggingConfig"]
    VPCs: Optional[AbstractSet["_VPC"]]
    NameServers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRoute53Hostedzone"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRoute53Hostedzone"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            HostedZoneConfig=HostedZoneConfig._deserialize(json_data.get("HostedZoneConfig")),
            HostedZoneTags=set_or_none(json_data.get("HostedZoneTags")),
            Name=json_data.get("Name"),
            QueryLoggingConfig=QueryLoggingConfig._deserialize(json_data.get("QueryLoggingConfig")),
            VPCs=set_or_none(json_data.get("VPCs")),
            NameServers=json_data.get("NameServers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRoute53Hostedzone = AwsRoute53Hostedzone


@dataclass
class HostedZoneConfig(BaseModel):
    Comment: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostedZoneConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostedZoneConfig"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostedZoneConfig = HostedZoneConfig


@dataclass
class HostedZoneTag(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostedZoneTag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostedZoneTag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostedZoneTag = HostedZoneTag


@dataclass
class QueryLoggingConfig(BaseModel):
    CloudWatchLogsLogGroupArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QueryLoggingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryLoggingConfig"]:
        if not json_data:
            return None
        return cls(
            CloudWatchLogsLogGroupArn=json_data.get("CloudWatchLogsLogGroupArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryLoggingConfig = QueryLoggingConfig


@dataclass
class VPC(BaseModel):
    VPCId: Optional[str]
    VPCRegion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VPC"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VPC"]:
        if not json_data:
            return None
        return cls(
            VPCId=json_data.get("VPCId"),
            VPCRegion=json_data.get("VPCRegion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VPC = VPC


