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
class AwsVpclatticeServicenetworkvpcassociation(BaseModel):
    Arn: Optional[str]
    CreatedAt: Optional[str]
    SecurityGroupIds: Optional[AbstractSet[str]]
    Id: Optional[str]
    ServiceNetworkArn: Optional[str]
    ServiceNetworkId: Optional[str]
    ServiceNetworkIdentifier: Optional[str]
    ServiceNetworkName: Optional[str]
    Status: Optional[str]
    VpcId: Optional[str]
    VpcIdentifier: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsVpclatticeServicenetworkvpcassociation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsVpclatticeServicenetworkvpcassociation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            CreatedAt=json_data.get("CreatedAt"),
            SecurityGroupIds=set_or_none(json_data.get("SecurityGroupIds")),
            Id=json_data.get("Id"),
            ServiceNetworkArn=json_data.get("ServiceNetworkArn"),
            ServiceNetworkId=json_data.get("ServiceNetworkId"),
            ServiceNetworkIdentifier=json_data.get("ServiceNetworkIdentifier"),
            ServiceNetworkName=json_data.get("ServiceNetworkName"),
            Status=json_data.get("Status"),
            VpcId=json_data.get("VpcId"),
            VpcIdentifier=json_data.get("VpcIdentifier"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsVpclatticeServicenetworkvpcassociation = AwsVpclatticeServicenetworkvpcassociation


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


