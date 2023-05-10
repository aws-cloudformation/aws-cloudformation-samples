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
class AwsEc2Vpnconnection(BaseModel):
    VpnConnectionId: Optional[str]
    CustomerGatewayId: Optional[str]
    StaticRoutesOnly: Optional[bool]
    Tags: Optional[Any]
    TransitGatewayId: Optional[str]
    Type: Optional[str]
    VpnGatewayId: Optional[str]
    VpnTunnelOptionsSpecifications: Optional[Sequence["_VpnTunnelOptionsSpecification"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Vpnconnection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Vpnconnection"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            VpnConnectionId=json_data.get("VpnConnectionId"),
            CustomerGatewayId=json_data.get("CustomerGatewayId"),
            StaticRoutesOnly=json_data.get("StaticRoutesOnly"),
            Tags=json_data.get("Tags"),
            TransitGatewayId=json_data.get("TransitGatewayId"),
            Type=json_data.get("Type"),
            VpnGatewayId=json_data.get("VpnGatewayId"),
            VpnTunnelOptionsSpecifications=deserialize_list(json_data.get("VpnTunnelOptionsSpecifications"), VpnTunnelOptionsSpecification),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Vpnconnection = AwsEc2Vpnconnection


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
class VpnTunnelOptionsSpecification(BaseModel):
    PreSharedKey: Optional[str]
    TunnelInsideCidr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VpnTunnelOptionsSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpnTunnelOptionsSpecification"]:
        if not json_data:
            return None
        return cls(
            PreSharedKey=json_data.get("PreSharedKey"),
            TunnelInsideCidr=json_data.get("TunnelInsideCidr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpnTunnelOptionsSpecification = VpnTunnelOptionsSpecification


