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
class AwsEc2Eip(BaseModel):
    PublicIp: Optional[str]
    AllocationId: Optional[str]
    Domain: Optional[str]
    NetworkBorderGroup: Optional[str]
    TransferAddress: Optional[str]
    InstanceId: Optional[str]
    PublicIpv4Pool: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Eip"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Eip"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            PublicIp=json_data.get("PublicIp"),
            AllocationId=json_data.get("AllocationId"),
            Domain=json_data.get("Domain"),
            NetworkBorderGroup=json_data.get("NetworkBorderGroup"),
            TransferAddress=json_data.get("TransferAddress"),
            InstanceId=json_data.get("InstanceId"),
            PublicIpv4Pool=json_data.get("PublicIpv4Pool"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Eip = AwsEc2Eip


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


