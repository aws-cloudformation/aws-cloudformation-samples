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
class AwsEc2Vpngateway(BaseModel):
    VPNGatewayId: Optional[str]
    AmazonSideAsn: Optional[int]
    Tags: Optional[Any]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Vpngateway"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Vpngateway"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            VPNGatewayId=json_data.get("VPNGatewayId"),
            AmazonSideAsn=json_data.get("AmazonSideAsn"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Vpngateway = AwsEc2Vpngateway


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


