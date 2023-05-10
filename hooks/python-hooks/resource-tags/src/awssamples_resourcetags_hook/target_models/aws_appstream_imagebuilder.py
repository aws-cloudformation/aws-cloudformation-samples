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
class AwsAppstreamImagebuilder(BaseModel):
    Description: Optional[str]
    VpcConfig: Optional["_VpcConfig"]
    EnableDefaultInternetAccess: Optional[bool]
    DomainJoinInfo: Optional["_DomainJoinInfo"]
    AppstreamAgentVersion: Optional[str]
    Name: Optional[str]
    ImageName: Optional[str]
    DisplayName: Optional[str]
    IamRoleArn: Optional[str]
    InstanceType: Optional[str]
    Tags: Optional[Any]
    StreamingUrl: Optional[str]
    ImageArn: Optional[str]
    AccessEndpoints: Optional[Sequence["_AccessEndpoint"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppstreamImagebuilder"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppstreamImagebuilder"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            VpcConfig=VpcConfig._deserialize(json_data.get("VpcConfig")),
            EnableDefaultInternetAccess=json_data.get("EnableDefaultInternetAccess"),
            DomainJoinInfo=DomainJoinInfo._deserialize(json_data.get("DomainJoinInfo")),
            AppstreamAgentVersion=json_data.get("AppstreamAgentVersion"),
            Name=json_data.get("Name"),
            ImageName=json_data.get("ImageName"),
            DisplayName=json_data.get("DisplayName"),
            IamRoleArn=json_data.get("IamRoleArn"),
            InstanceType=json_data.get("InstanceType"),
            Tags=json_data.get("Tags"),
            StreamingUrl=json_data.get("StreamingUrl"),
            ImageArn=json_data.get("ImageArn"),
            AccessEndpoints=deserialize_list(json_data.get("AccessEndpoints"), AccessEndpoint),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppstreamImagebuilder = AwsAppstreamImagebuilder


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


@dataclass
class DomainJoinInfo(BaseModel):
    OrganizationalUnitDistinguishedName: Optional[str]
    DirectoryName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DomainJoinInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainJoinInfo"]:
        if not json_data:
            return None
        return cls(
            OrganizationalUnitDistinguishedName=json_data.get("OrganizationalUnitDistinguishedName"),
            DirectoryName=json_data.get("DirectoryName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainJoinInfo = DomainJoinInfo


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


