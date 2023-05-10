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
class AwsEc2Verifiedaccesstrustprovider(BaseModel):
    TrustProviderType: Optional[str]
    DeviceTrustProviderType: Optional[str]
    UserTrustProviderType: Optional[str]
    OidcOptions: Optional["_OidcOptions"]
    DeviceOptions: Optional["_DeviceOptions"]
    PolicyReferenceName: Optional[str]
    CreationTime: Optional[str]
    LastUpdatedTime: Optional[str]
    VerifiedAccessTrustProviderId: Optional[str]
    Description: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Verifiedaccesstrustprovider"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Verifiedaccesstrustprovider"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            TrustProviderType=json_data.get("TrustProviderType"),
            DeviceTrustProviderType=json_data.get("DeviceTrustProviderType"),
            UserTrustProviderType=json_data.get("UserTrustProviderType"),
            OidcOptions=OidcOptions._deserialize(json_data.get("OidcOptions")),
            DeviceOptions=DeviceOptions._deserialize(json_data.get("DeviceOptions")),
            PolicyReferenceName=json_data.get("PolicyReferenceName"),
            CreationTime=json_data.get("CreationTime"),
            LastUpdatedTime=json_data.get("LastUpdatedTime"),
            VerifiedAccessTrustProviderId=json_data.get("VerifiedAccessTrustProviderId"),
            Description=json_data.get("Description"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Verifiedaccesstrustprovider = AwsEc2Verifiedaccesstrustprovider


@dataclass
class OidcOptions(BaseModel):
    Issuer: Optional[str]
    AuthorizationEndpoint: Optional[str]
    TokenEndpoint: Optional[str]
    UserInfoEndpoint: Optional[str]
    ClientId: Optional[str]
    ClientSecret: Optional[str]
    Scope: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OidcOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OidcOptions"]:
        if not json_data:
            return None
        return cls(
            Issuer=json_data.get("Issuer"),
            AuthorizationEndpoint=json_data.get("AuthorizationEndpoint"),
            TokenEndpoint=json_data.get("TokenEndpoint"),
            UserInfoEndpoint=json_data.get("UserInfoEndpoint"),
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
            Scope=json_data.get("Scope"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OidcOptions = OidcOptions


@dataclass
class DeviceOptions(BaseModel):
    TenantId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeviceOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeviceOptions"]:
        if not json_data:
            return None
        return cls(
            TenantId=json_data.get("TenantId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeviceOptions = DeviceOptions


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


