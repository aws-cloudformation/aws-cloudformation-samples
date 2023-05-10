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
class AwsEc2Transitgatewaypeeringattachment(BaseModel):
    Status: Optional["_PeeringAttachmentStatus"]
    TransitGatewayId: Optional[str]
    PeerTransitGatewayId: Optional[str]
    PeerAccountId: Optional[str]
    State: Optional[str]
    CreationTime: Optional[str]
    PeerRegion: Optional[str]
    Tags: Optional[Any]
    TransitGatewayAttachmentId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Transitgatewaypeeringattachment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Transitgatewaypeeringattachment"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Status=PeeringAttachmentStatus._deserialize(json_data.get("Status")),
            TransitGatewayId=json_data.get("TransitGatewayId"),
            PeerTransitGatewayId=json_data.get("PeerTransitGatewayId"),
            PeerAccountId=json_data.get("PeerAccountId"),
            State=json_data.get("State"),
            CreationTime=json_data.get("CreationTime"),
            PeerRegion=json_data.get("PeerRegion"),
            Tags=json_data.get("Tags"),
            TransitGatewayAttachmentId=json_data.get("TransitGatewayAttachmentId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Transitgatewaypeeringattachment = AwsEc2Transitgatewaypeeringattachment


@dataclass
class PeeringAttachmentStatus(BaseModel):
    Message: Optional[str]
    Code: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PeeringAttachmentStatus"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PeeringAttachmentStatus"]:
        if not json_data:
            return None
        return cls(
            Message=json_data.get("Message"),
            Code=json_data.get("Code"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PeeringAttachmentStatus = PeeringAttachmentStatus


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


