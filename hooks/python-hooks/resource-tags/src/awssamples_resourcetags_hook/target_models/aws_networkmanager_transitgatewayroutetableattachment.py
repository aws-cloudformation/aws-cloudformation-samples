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
class AwsNetworkmanagerTransitgatewayroutetableattachment(BaseModel):
    PeeringId: Optional[str]
    TransitGatewayRouteTableArn: Optional[str]
    CoreNetworkId: Optional[str]
    CoreNetworkArn: Optional[str]
    AttachmentId: Optional[str]
    OwnerAccountId: Optional[str]
    AttachmentType: Optional[str]
    State: Optional[str]
    EdgeLocation: Optional[str]
    ResourceArn: Optional[str]
    AttachmentPolicyRuleNumber: Optional[int]
    SegmentName: Optional[str]
    ProposedSegmentChange: Optional["_ProposedSegmentChange"]
    CreatedAt: Optional[str]
    UpdatedAt: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsNetworkmanagerTransitgatewayroutetableattachment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsNetworkmanagerTransitgatewayroutetableattachment"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            PeeringId=json_data.get("PeeringId"),
            TransitGatewayRouteTableArn=json_data.get("TransitGatewayRouteTableArn"),
            CoreNetworkId=json_data.get("CoreNetworkId"),
            CoreNetworkArn=json_data.get("CoreNetworkArn"),
            AttachmentId=json_data.get("AttachmentId"),
            OwnerAccountId=json_data.get("OwnerAccountId"),
            AttachmentType=json_data.get("AttachmentType"),
            State=json_data.get("State"),
            EdgeLocation=json_data.get("EdgeLocation"),
            ResourceArn=json_data.get("ResourceArn"),
            AttachmentPolicyRuleNumber=json_data.get("AttachmentPolicyRuleNumber"),
            SegmentName=json_data.get("SegmentName"),
            ProposedSegmentChange=ProposedSegmentChange._deserialize(json_data.get("ProposedSegmentChange")),
            CreatedAt=json_data.get("CreatedAt"),
            UpdatedAt=json_data.get("UpdatedAt"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsNetworkmanagerTransitgatewayroutetableattachment = AwsNetworkmanagerTransitgatewayroutetableattachment


@dataclass
class ProposedSegmentChange(BaseModel):
    Tags: Optional[AbstractSet["_Tag"]]
    AttachmentPolicyRuleNumber: Optional[int]
    SegmentName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProposedSegmentChange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProposedSegmentChange"]:
        if not json_data:
            return None
        return cls(
            Tags=set_or_none(json_data.get("Tags")),
            AttachmentPolicyRuleNumber=json_data.get("AttachmentPolicyRuleNumber"),
            SegmentName=json_data.get("SegmentName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProposedSegmentChange = ProposedSegmentChange


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


