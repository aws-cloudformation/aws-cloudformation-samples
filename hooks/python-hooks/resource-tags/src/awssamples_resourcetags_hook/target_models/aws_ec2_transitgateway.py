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
class AwsEc2Transitgateway(BaseModel):
    DefaultRouteTablePropagation: Optional[str]
    Description: Optional[str]
    AutoAcceptSharedAttachments: Optional[str]
    DefaultRouteTableAssociation: Optional[str]
    Id: Optional[str]
    VpnEcmpSupport: Optional[str]
    DnsSupport: Optional[str]
    MulticastSupport: Optional[str]
    AmazonSideAsn: Optional[int]
    TransitGatewayCidrBlocks: Optional[Sequence[str]]
    Tags: Optional[Any]
    AssociationDefaultRouteTableId: Optional[str]
    PropagationDefaultRouteTableId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Transitgateway"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Transitgateway"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DefaultRouteTablePropagation=json_data.get("DefaultRouteTablePropagation"),
            Description=json_data.get("Description"),
            AutoAcceptSharedAttachments=json_data.get("AutoAcceptSharedAttachments"),
            DefaultRouteTableAssociation=json_data.get("DefaultRouteTableAssociation"),
            Id=json_data.get("Id"),
            VpnEcmpSupport=json_data.get("VpnEcmpSupport"),
            DnsSupport=json_data.get("DnsSupport"),
            MulticastSupport=json_data.get("MulticastSupport"),
            AmazonSideAsn=json_data.get("AmazonSideAsn"),
            TransitGatewayCidrBlocks=json_data.get("TransitGatewayCidrBlocks"),
            Tags=json_data.get("Tags"),
            AssociationDefaultRouteTableId=json_data.get("AssociationDefaultRouteTableId"),
            PropagationDefaultRouteTableId=json_data.get("PropagationDefaultRouteTableId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Transitgateway = AwsEc2Transitgateway


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


