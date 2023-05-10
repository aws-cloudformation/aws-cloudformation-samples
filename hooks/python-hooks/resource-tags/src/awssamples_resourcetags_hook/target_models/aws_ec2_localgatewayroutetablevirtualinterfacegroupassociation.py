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
class AwsEc2Localgatewayroutetablevirtualinterfacegroupassociation(BaseModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociationId: Optional[str]
    LocalGatewayId: Optional[str]
    LocalGatewayRouteTableId: Optional[str]
    LocalGatewayRouteTableArn: Optional[str]
    LocalGatewayVirtualInterfaceGroupId: Optional[str]
    OwnerId: Optional[str]
    State: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Localgatewayroutetablevirtualinterfacegroupassociation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Localgatewayroutetablevirtualinterfacegroupassociation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            LocalGatewayRouteTableVirtualInterfaceGroupAssociationId=json_data.get("LocalGatewayRouteTableVirtualInterfaceGroupAssociationId"),
            LocalGatewayId=json_data.get("LocalGatewayId"),
            LocalGatewayRouteTableId=json_data.get("LocalGatewayRouteTableId"),
            LocalGatewayRouteTableArn=json_data.get("LocalGatewayRouteTableArn"),
            LocalGatewayVirtualInterfaceGroupId=json_data.get("LocalGatewayVirtualInterfaceGroupId"),
            OwnerId=json_data.get("OwnerId"),
            State=json_data.get("State"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Localgatewayroutetablevirtualinterfacegroupassociation = AwsEc2Localgatewayroutetablevirtualinterfacegroupassociation


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


