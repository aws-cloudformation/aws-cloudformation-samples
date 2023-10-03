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
class AwsConnectQueue(BaseModel):
    InstanceArn: Optional[str]
    Description: Optional[str]
    HoursOfOperationArn: Optional[str]
    MaxContacts: Optional[int]
    Name: Optional[str]
    OutboundCallerConfig: Optional["_OutboundCallerConfig"]
    QueueArn: Optional[str]
    Status: Optional[str]
    QuickConnectArns: Optional[Sequence[str]]
    Tags: Optional[Any]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConnectQueue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConnectQueue"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            InstanceArn=json_data.get("InstanceArn"),
            Description=json_data.get("Description"),
            HoursOfOperationArn=json_data.get("HoursOfOperationArn"),
            MaxContacts=json_data.get("MaxContacts"),
            Name=json_data.get("Name"),
            OutboundCallerConfig=OutboundCallerConfig._deserialize(json_data.get("OutboundCallerConfig")),
            QueueArn=json_data.get("QueueArn"),
            Status=json_data.get("Status"),
            QuickConnectArns=json_data.get("QuickConnectArns"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConnectQueue = AwsConnectQueue


@dataclass
class OutboundCallerConfig(BaseModel):
    OutboundCallerIdName: Optional[str]
    OutboundCallerIdNumberArn: Optional[str]
    OutboundFlowArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutboundCallerConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutboundCallerConfig"]:
        if not json_data:
            return None
        return cls(
            OutboundCallerIdName=json_data.get("OutboundCallerIdName"),
            OutboundCallerIdNumberArn=json_data.get("OutboundCallerIdNumberArn"),
            OutboundFlowArn=json_data.get("OutboundFlowArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutboundCallerConfig = OutboundCallerConfig


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


