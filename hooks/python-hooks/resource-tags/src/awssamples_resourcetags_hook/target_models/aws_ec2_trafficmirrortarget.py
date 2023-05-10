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
class AwsEc2Trafficmirrortarget(BaseModel):
    NetworkLoadBalancerArn: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    NetworkInterfaceId: Optional[str]
    GatewayLoadBalancerEndpointId: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Trafficmirrortarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Trafficmirrortarget"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            NetworkLoadBalancerArn=json_data.get("NetworkLoadBalancerArn"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            GatewayLoadBalancerEndpointId=json_data.get("GatewayLoadBalancerEndpointId"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Trafficmirrortarget = AwsEc2Trafficmirrortarget


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


