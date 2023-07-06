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
class AwsAppstreamAppblockbuilder(BaseModel):
    Name: Optional[str]
    Arn: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    Platform: Optional[str]
    AccessEndpoints: Optional[AbstractSet["_AccessEndpoint"]]
    Tags: Optional[Any]
    VpcConfig: Optional["_VpcConfig"]
    EnableDefaultInternetAccess: Optional[bool]
    IamRoleArn: Optional[str]
    CreatedTime: Optional[str]
    InstanceType: Optional[str]
    AppBlockArns: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppstreamAppblockbuilder"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppstreamAppblockbuilder"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Platform=json_data.get("Platform"),
            AccessEndpoints=set_or_none(json_data.get("AccessEndpoints")),
            Tags=json_data.get("Tags"),
            VpcConfig=VpcConfig._deserialize(json_data.get("VpcConfig")),
            EnableDefaultInternetAccess=json_data.get("EnableDefaultInternetAccess"),
            IamRoleArn=json_data.get("IamRoleArn"),
            CreatedTime=json_data.get("CreatedTime"),
            InstanceType=json_data.get("InstanceType"),
            AppBlockArns=set_or_none(json_data.get("AppBlockArns")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppstreamAppblockbuilder = AwsAppstreamAppblockbuilder


@dataclass
class AccessEndpoint(BaseModel):
    EndpointType: Optional[str]
    VpceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessEndpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessEndpoint"]:
        if not json_data:
            return None
        return cls(
            EndpointType=json_data.get("EndpointType"),
            VpceId=json_data.get("VpceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessEndpoint = AccessEndpoint


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


@dataclass
class VpcConfig(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfig"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfig = VpcConfig


