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
class AwsEc2Transitgatewayconnect(BaseModel):
    TransitGatewayAttachmentId: Optional[str]
    TransportTransitGatewayAttachmentId: Optional[str]
    TransitGatewayId: Optional[str]
    State: Optional[str]
    CreationTime: Optional[str]
    Tags: Optional[Any]
    Options: Optional["_TransitGatewayConnectOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Transitgatewayconnect"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Transitgatewayconnect"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            TransitGatewayAttachmentId=json_data.get("TransitGatewayAttachmentId"),
            TransportTransitGatewayAttachmentId=json_data.get("TransportTransitGatewayAttachmentId"),
            TransitGatewayId=json_data.get("TransitGatewayId"),
            State=json_data.get("State"),
            CreationTime=json_data.get("CreationTime"),
            Tags=json_data.get("Tags"),
            Options=TransitGatewayConnectOptions._deserialize(json_data.get("Options")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Transitgatewayconnect = AwsEc2Transitgatewayconnect


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
class TransitGatewayConnectOptions(BaseModel):
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TransitGatewayConnectOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransitGatewayConnectOptions"]:
        if not json_data:
            return None
        return cls(
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransitGatewayConnectOptions = TransitGatewayConnectOptions


