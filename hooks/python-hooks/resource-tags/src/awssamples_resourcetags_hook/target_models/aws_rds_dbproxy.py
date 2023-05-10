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
class AwsRdsDbproxy(BaseModel):
    Auth: Optional[Sequence["_AuthFormat"]]
    DBProxyArn: Optional[str]
    DBProxyName: Optional[str]
    DebugLogging: Optional[bool]
    Endpoint: Optional[str]
    EngineFamily: Optional[str]
    IdleClientTimeout: Optional[int]
    RequireTLS: Optional[bool]
    RoleArn: Optional[str]
    Tags: Optional[Any]
    VpcId: Optional[str]
    VpcSecurityGroupIds: Optional[Sequence[str]]
    VpcSubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRdsDbproxy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRdsDbproxy"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Auth=deserialize_list(json_data.get("Auth"), AuthFormat),
            DBProxyArn=json_data.get("DBProxyArn"),
            DBProxyName=json_data.get("DBProxyName"),
            DebugLogging=json_data.get("DebugLogging"),
            Endpoint=json_data.get("Endpoint"),
            EngineFamily=json_data.get("EngineFamily"),
            IdleClientTimeout=json_data.get("IdleClientTimeout"),
            RequireTLS=json_data.get("RequireTLS"),
            RoleArn=json_data.get("RoleArn"),
            Tags=json_data.get("Tags"),
            VpcId=json_data.get("VpcId"),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
            VpcSubnetIds=json_data.get("VpcSubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRdsDbproxy = AwsRdsDbproxy


@dataclass
class AuthFormat(BaseModel):
    AuthScheme: Optional[str]
    Description: Optional[str]
    IAMAuth: Optional[str]
    SecretArn: Optional[str]
    ClientPasswordAuthType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthFormat"]:
        if not json_data:
            return None
        return cls(
            AuthScheme=json_data.get("AuthScheme"),
            Description=json_data.get("Description"),
            IAMAuth=json_data.get("IAMAuth"),
            SecretArn=json_data.get("SecretArn"),
            ClientPasswordAuthType=json_data.get("ClientPasswordAuthType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthFormat = AuthFormat


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


