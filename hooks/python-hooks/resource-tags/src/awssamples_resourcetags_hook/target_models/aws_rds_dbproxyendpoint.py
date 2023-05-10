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
class AwsRdsDbproxyendpoint(BaseModel):
    DBProxyEndpointName: Optional[str]
    DBProxyEndpointArn: Optional[str]
    DBProxyName: Optional[str]
    VpcId: Optional[str]
    VpcSecurityGroupIds: Optional[Sequence[str]]
    VpcSubnetIds: Optional[Sequence[str]]
    Endpoint: Optional[str]
    TargetRole: Optional[str]
    IsDefault: Optional[bool]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRdsDbproxyendpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRdsDbproxyendpoint"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DBProxyEndpointName=json_data.get("DBProxyEndpointName"),
            DBProxyEndpointArn=json_data.get("DBProxyEndpointArn"),
            DBProxyName=json_data.get("DBProxyName"),
            VpcId=json_data.get("VpcId"),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
            VpcSubnetIds=json_data.get("VpcSubnetIds"),
            Endpoint=json_data.get("Endpoint"),
            TargetRole=json_data.get("TargetRole"),
            IsDefault=json_data.get("IsDefault"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRdsDbproxyendpoint = AwsRdsDbproxyendpoint


@dataclass
class TagFormat(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagFormat"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagFormat = TagFormat


