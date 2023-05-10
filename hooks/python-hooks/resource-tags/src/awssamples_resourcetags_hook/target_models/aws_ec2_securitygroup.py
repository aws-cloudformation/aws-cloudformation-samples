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
class AwsEc2Securitygroup(BaseModel):
    GroupDescription: Optional[str]
    GroupName: Optional[str]
    VpcId: Optional[str]
    Id: Optional[str]
    SecurityGroupIngress: Optional[Sequence["_Ingress"]]
    SecurityGroupEgress: Optional[Sequence["_Egress"]]
    Tags: Optional[Any]
    GroupId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Securitygroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Securitygroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            GroupDescription=json_data.get("GroupDescription"),
            GroupName=json_data.get("GroupName"),
            VpcId=json_data.get("VpcId"),
            Id=json_data.get("Id"),
            SecurityGroupIngress=deserialize_list(json_data.get("SecurityGroupIngress"), Ingress),
            SecurityGroupEgress=deserialize_list(json_data.get("SecurityGroupEgress"), Egress),
            Tags=json_data.get("Tags"),
            GroupId=json_data.get("GroupId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Securitygroup = AwsEc2Securitygroup


@dataclass
class Ingress(BaseModel):
    CidrIp: Optional[str]
    CidrIpv6: Optional[str]
    Description: Optional[str]
    FromPort: Optional[int]
    SourceSecurityGroupName: Optional[str]
    ToPort: Optional[int]
    SourceSecurityGroupOwnerId: Optional[str]
    IpProtocol: Optional[str]
    SourceSecurityGroupId: Optional[str]
    SourcePrefixListId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ingress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ingress"]:
        if not json_data:
            return None
        return cls(
            CidrIp=json_data.get("CidrIp"),
            CidrIpv6=json_data.get("CidrIpv6"),
            Description=json_data.get("Description"),
            FromPort=json_data.get("FromPort"),
            SourceSecurityGroupName=json_data.get("SourceSecurityGroupName"),
            ToPort=json_data.get("ToPort"),
            SourceSecurityGroupOwnerId=json_data.get("SourceSecurityGroupOwnerId"),
            IpProtocol=json_data.get("IpProtocol"),
            SourceSecurityGroupId=json_data.get("SourceSecurityGroupId"),
            SourcePrefixListId=json_data.get("SourcePrefixListId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ingress = Ingress


@dataclass
class Egress(BaseModel):
    CidrIp: Optional[str]
    CidrIpv6: Optional[str]
    Description: Optional[str]
    FromPort: Optional[int]
    ToPort: Optional[int]
    IpProtocol: Optional[str]
    DestinationSecurityGroupId: Optional[str]
    DestinationPrefixListId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Egress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Egress"]:
        if not json_data:
            return None
        return cls(
            CidrIp=json_data.get("CidrIp"),
            CidrIpv6=json_data.get("CidrIpv6"),
            Description=json_data.get("Description"),
            FromPort=json_data.get("FromPort"),
            ToPort=json_data.get("ToPort"),
            IpProtocol=json_data.get("IpProtocol"),
            DestinationSecurityGroupId=json_data.get("DestinationSecurityGroupId"),
            DestinationPrefixListId=json_data.get("DestinationPrefixListId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Egress = Egress


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


