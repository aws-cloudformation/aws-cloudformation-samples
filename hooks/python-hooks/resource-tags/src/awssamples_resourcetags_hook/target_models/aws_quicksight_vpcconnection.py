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
class AwsQuicksightVpcconnection(BaseModel):
    Arn: Optional[str]
    AwsAccountId: Optional[str]
    Name: Optional[str]
    VPCConnectionId: Optional[str]
    VPCId: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]
    DnsResolvers: Optional[Sequence[str]]
    Status: Optional[str]
    AvailabilityStatus: Optional[str]
    NetworkInterfaces: Optional[Sequence["_NetworkInterface"]]
    RoleArn: Optional[str]
    CreatedTime: Optional[str]
    LastUpdatedTime: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsQuicksightVpcconnection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsQuicksightVpcconnection"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            AwsAccountId=json_data.get("AwsAccountId"),
            Name=json_data.get("Name"),
            VPCConnectionId=json_data.get("VPCConnectionId"),
            VPCId=json_data.get("VPCId"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
            DnsResolvers=json_data.get("DnsResolvers"),
            Status=json_data.get("Status"),
            AvailabilityStatus=json_data.get("AvailabilityStatus"),
            NetworkInterfaces=deserialize_list(json_data.get("NetworkInterfaces"), NetworkInterface),
            RoleArn=json_data.get("RoleArn"),
            CreatedTime=json_data.get("CreatedTime"),
            LastUpdatedTime=json_data.get("LastUpdatedTime"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsQuicksightVpcconnection = AwsQuicksightVpcconnection


@dataclass
class NetworkInterface(BaseModel):
    SubnetId: Optional[str]
    AvailabilityZone: Optional[str]
    ErrorMessage: Optional[str]
    Status: Optional[str]
    NetworkInterfaceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterface"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterface"]:
        if not json_data:
            return None
        return cls(
            SubnetId=json_data.get("SubnetId"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            ErrorMessage=json_data.get("ErrorMessage"),
            Status=json_data.get("Status"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterface = NetworkInterface


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


