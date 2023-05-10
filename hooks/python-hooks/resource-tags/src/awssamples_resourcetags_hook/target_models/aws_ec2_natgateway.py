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
class AwsEc2Natgateway(BaseModel):
    SubnetId: Optional[str]
    NatGatewayId: Optional[str]
    ConnectivityType: Optional[str]
    PrivateIpAddress: Optional[str]
    Tags: Optional[Any]
    AllocationId: Optional[str]
    SecondaryAllocationIds: Optional[Sequence[str]]
    SecondaryPrivateIpAddresses: Optional[Sequence[str]]
    SecondaryPrivateIpAddressCount: Optional[int]
    MaxDrainDurationSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Natgateway"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Natgateway"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            SubnetId=json_data.get("SubnetId"),
            NatGatewayId=json_data.get("NatGatewayId"),
            ConnectivityType=json_data.get("ConnectivityType"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            Tags=json_data.get("Tags"),
            AllocationId=json_data.get("AllocationId"),
            SecondaryAllocationIds=json_data.get("SecondaryAllocationIds"),
            SecondaryPrivateIpAddresses=json_data.get("SecondaryPrivateIpAddresses"),
            SecondaryPrivateIpAddressCount=json_data.get("SecondaryPrivateIpAddressCount"),
            MaxDrainDurationSeconds=json_data.get("MaxDrainDurationSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Natgateway = AwsEc2Natgateway


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


