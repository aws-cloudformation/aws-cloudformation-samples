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
class AwsEksIdentityproviderconfig(BaseModel):
    ClusterName: Optional[str]
    Type: Optional[str]
    IdentityProviderConfigName: Optional[str]
    Oidc: Optional["_OidcIdentityProviderConfig"]
    Tags: Optional[Any]
    IdentityProviderConfigArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEksIdentityproviderconfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEksIdentityproviderconfig"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ClusterName=json_data.get("ClusterName"),
            Type=json_data.get("Type"),
            IdentityProviderConfigName=json_data.get("IdentityProviderConfigName"),
            Oidc=OidcIdentityProviderConfig._deserialize(json_data.get("Oidc")),
            Tags=json_data.get("Tags"),
            IdentityProviderConfigArn=json_data.get("IdentityProviderConfigArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEksIdentityproviderconfig = AwsEksIdentityproviderconfig


@dataclass
class OidcIdentityProviderConfig(BaseModel):
    ClientId: Optional[str]
    GroupsClaim: Optional[str]
    GroupsPrefix: Optional[str]
    IssuerUrl: Optional[str]
    RequiredClaims: Optional[AbstractSet["_RequiredClaim"]]
    UsernameClaim: Optional[str]
    UsernamePrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OidcIdentityProviderConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OidcIdentityProviderConfig"]:
        if not json_data:
            return None
        return cls(
            ClientId=json_data.get("ClientId"),
            GroupsClaim=json_data.get("GroupsClaim"),
            GroupsPrefix=json_data.get("GroupsPrefix"),
            IssuerUrl=json_data.get("IssuerUrl"),
            RequiredClaims=set_or_none(json_data.get("RequiredClaims")),
            UsernameClaim=json_data.get("UsernameClaim"),
            UsernamePrefix=json_data.get("UsernamePrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OidcIdentityProviderConfig = OidcIdentityProviderConfig


@dataclass
class RequiredClaim(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequiredClaim"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequiredClaim"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequiredClaim = RequiredClaim


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


