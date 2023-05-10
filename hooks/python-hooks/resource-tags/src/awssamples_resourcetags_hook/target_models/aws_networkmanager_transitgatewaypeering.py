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
class AwsNetworkmanagerTransitgatewaypeering(BaseModel):
    CoreNetworkId: Optional[str]
    CoreNetworkArn: Optional[str]
    TransitGatewayArn: Optional[str]
    TransitGatewayPeeringAttachmentId: Optional[str]
    PeeringId: Optional[str]
    State: Optional[str]
    EdgeLocation: Optional[str]
    ResourceArn: Optional[str]
    OwnerAccountId: Optional[str]
    PeeringType: Optional[str]
    CreatedAt: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsNetworkmanagerTransitgatewaypeering"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsNetworkmanagerTransitgatewaypeering"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CoreNetworkId=json_data.get("CoreNetworkId"),
            CoreNetworkArn=json_data.get("CoreNetworkArn"),
            TransitGatewayArn=json_data.get("TransitGatewayArn"),
            TransitGatewayPeeringAttachmentId=json_data.get("TransitGatewayPeeringAttachmentId"),
            PeeringId=json_data.get("PeeringId"),
            State=json_data.get("State"),
            EdgeLocation=json_data.get("EdgeLocation"),
            ResourceArn=json_data.get("ResourceArn"),
            OwnerAccountId=json_data.get("OwnerAccountId"),
            PeeringType=json_data.get("PeeringType"),
            CreatedAt=json_data.get("CreatedAt"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsNetworkmanagerTransitgatewaypeering = AwsNetworkmanagerTransitgatewaypeering


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


