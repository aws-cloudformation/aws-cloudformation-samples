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
class AwsEc2Transitgatewayvpcattachment(BaseModel):
    Options: Optional["_Options"]
    TransitGatewayId: Optional[str]
    VpcId: Optional[str]
    RemoveSubnetIds: Optional[Sequence[str]]
    Id: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    AddSubnetIds: Optional[Sequence[str]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Transitgatewayvpcattachment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Transitgatewayvpcattachment"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Options=Options._deserialize(json_data.get("Options")),
            TransitGatewayId=json_data.get("TransitGatewayId"),
            VpcId=json_data.get("VpcId"),
            RemoveSubnetIds=json_data.get("RemoveSubnetIds"),
            Id=json_data.get("Id"),
            SubnetIds=json_data.get("SubnetIds"),
            AddSubnetIds=json_data.get("AddSubnetIds"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Transitgatewayvpcattachment = AwsEc2Transitgatewayvpcattachment


@dataclass
class Options(BaseModel):
    Ipv6Support: Optional[str]
    ApplianceModeSupport: Optional[str]
    DnsSupport: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Options"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Options"]:
        if not json_data:
            return None
        return cls(
            Ipv6Support=json_data.get("Ipv6Support"),
            ApplianceModeSupport=json_data.get("ApplianceModeSupport"),
            DnsSupport=json_data.get("DnsSupport"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Options = Options


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


