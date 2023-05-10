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
class AwsRdsDbsecuritygroup(BaseModel):
    Id: Optional[str]
    DBSecurityGroupIngress: Optional[Sequence["_Ingress"]]
    EC2VpcId: Optional[str]
    GroupDescription: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRdsDbsecuritygroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRdsDbsecuritygroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            DBSecurityGroupIngress=deserialize_list(json_data.get("DBSecurityGroupIngress"), Ingress),
            EC2VpcId=json_data.get("EC2VpcId"),
            GroupDescription=json_data.get("GroupDescription"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRdsDbsecuritygroup = AwsRdsDbsecuritygroup


@dataclass
class Ingress(BaseModel):
    CIDRIP: Optional[str]
    EC2SecurityGroupId: Optional[str]
    EC2SecurityGroupName: Optional[str]
    EC2SecurityGroupOwnerId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ingress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ingress"]:
        if not json_data:
            return None
        return cls(
            CIDRIP=json_data.get("CIDRIP"),
            EC2SecurityGroupId=json_data.get("EC2SecurityGroupId"),
            EC2SecurityGroupName=json_data.get("EC2SecurityGroupName"),
            EC2SecurityGroupOwnerId=json_data.get("EC2SecurityGroupOwnerId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ingress = Ingress


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


