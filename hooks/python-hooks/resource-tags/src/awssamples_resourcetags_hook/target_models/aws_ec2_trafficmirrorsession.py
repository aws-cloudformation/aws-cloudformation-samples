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
class AwsEc2Trafficmirrorsession(BaseModel):
    Id: Optional[str]
    TrafficMirrorTargetId: Optional[str]
    Description: Optional[str]
    SessionNumber: Optional[int]
    VirtualNetworkId: Optional[int]
    PacketLength: Optional[int]
    NetworkInterfaceId: Optional[str]
    TrafficMirrorFilterId: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Trafficmirrorsession"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Trafficmirrorsession"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            TrafficMirrorTargetId=json_data.get("TrafficMirrorTargetId"),
            Description=json_data.get("Description"),
            SessionNumber=json_data.get("SessionNumber"),
            VirtualNetworkId=json_data.get("VirtualNetworkId"),
            PacketLength=json_data.get("PacketLength"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            TrafficMirrorFilterId=json_data.get("TrafficMirrorFilterId"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Trafficmirrorsession = AwsEc2Trafficmirrorsession


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


