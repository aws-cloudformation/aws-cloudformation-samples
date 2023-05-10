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
class AwsDatasyncStoragesystem(BaseModel):
    ServerConfiguration: Optional["_ServerConfiguration"]
    ServerCredentials: Optional["_ServerCredentials"]
    SecretsManagerArn: Optional[str]
    SystemType: Optional[str]
    AgentArns: Optional[Sequence[str]]
    CloudWatchLogGroupArn: Optional[str]
    Name: Optional[str]
    Tags: Optional[Any]
    StorageSystemArn: Optional[str]
    ConnectivityStatus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDatasyncStoragesystem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDatasyncStoragesystem"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ServerConfiguration=ServerConfiguration._deserialize(json_data.get("ServerConfiguration")),
            ServerCredentials=ServerCredentials._deserialize(json_data.get("ServerCredentials")),
            SecretsManagerArn=json_data.get("SecretsManagerArn"),
            SystemType=json_data.get("SystemType"),
            AgentArns=json_data.get("AgentArns"),
            CloudWatchLogGroupArn=json_data.get("CloudWatchLogGroupArn"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            StorageSystemArn=json_data.get("StorageSystemArn"),
            ConnectivityStatus=json_data.get("ConnectivityStatus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDatasyncStoragesystem = AwsDatasyncStoragesystem


@dataclass
class ServerConfiguration(BaseModel):
    ServerHostname: Optional[str]
    ServerPort: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ServerConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerConfiguration"]:
        if not json_data:
            return None
        return cls(
            ServerHostname=json_data.get("ServerHostname"),
            ServerPort=json_data.get("ServerPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerConfiguration = ServerConfiguration


@dataclass
class ServerCredentials(BaseModel):
    Username: Optional[str]
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerCredentials"]:
        if not json_data:
            return None
        return cls(
            Username=json_data.get("Username"),
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerCredentials = ServerCredentials


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


