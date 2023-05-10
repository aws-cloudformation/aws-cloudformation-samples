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
class AwsEc2Localgatewayroutetablevpcassociation(BaseModel):
    LocalGatewayId: Optional[str]
    LocalGatewayRouteTableId: Optional[str]
    LocalGatewayRouteTableVpcAssociationId: Optional[str]
    State: Optional[str]
    VpcId: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Localgatewayroutetablevpcassociation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Localgatewayroutetablevpcassociation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            LocalGatewayId=json_data.get("LocalGatewayId"),
            LocalGatewayRouteTableId=json_data.get("LocalGatewayRouteTableId"),
            LocalGatewayRouteTableVpcAssociationId=json_data.get("LocalGatewayRouteTableVpcAssociationId"),
            State=json_data.get("State"),
            VpcId=json_data.get("VpcId"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Localgatewayroutetablevpcassociation = AwsEc2Localgatewayroutetablevpcassociation


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


