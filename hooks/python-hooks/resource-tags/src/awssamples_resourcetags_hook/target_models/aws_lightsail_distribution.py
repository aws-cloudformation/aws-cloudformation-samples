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
class AwsLightsailDistribution(BaseModel):
    DistributionName: Optional[str]
    DistributionArn: Optional[str]
    BundleId: Optional[str]
    IpAddressType: Optional[str]
    CacheBehaviors: Optional[AbstractSet["_CacheBehaviorPerPath"]]
    CacheBehaviorSettings: Optional["_CacheSettings"]
    DefaultCacheBehavior: Optional["_CacheBehavior"]
    Origin: Optional["_InputOrigin"]
    Status: Optional[str]
    AbleToUpdateBundle: Optional[bool]
    IsEnabled: Optional[bool]
    CertificateName: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLightsailDistribution"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLightsailDistribution"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DistributionName=json_data.get("DistributionName"),
            DistributionArn=json_data.get("DistributionArn"),
            BundleId=json_data.get("BundleId"),
            IpAddressType=json_data.get("IpAddressType"),
            CacheBehaviors=set_or_none(json_data.get("CacheBehaviors")),
            CacheBehaviorSettings=CacheSettings._deserialize(json_data.get("CacheBehaviorSettings")),
            DefaultCacheBehavior=CacheBehavior._deserialize(json_data.get("DefaultCacheBehavior")),
            Origin=InputOrigin._deserialize(json_data.get("Origin")),
            Status=json_data.get("Status"),
            AbleToUpdateBundle=json_data.get("AbleToUpdateBundle"),
            IsEnabled=json_data.get("IsEnabled"),
            CertificateName=json_data.get("CertificateName"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLightsailDistribution = AwsLightsailDistribution


@dataclass
class CacheBehaviorPerPath(BaseModel):
    Behavior: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CacheBehaviorPerPath"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CacheBehaviorPerPath"]:
        if not json_data:
            return None
        return cls(
            Behavior=json_data.get("Behavior"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CacheBehaviorPerPath = CacheBehaviorPerPath


@dataclass
class CacheSettings(BaseModel):
    AllowedHTTPMethods: Optional[str]
    CachedHTTPMethods: Optional[str]
    DefaultTTL: Optional[int]
    MaximumTTL: Optional[int]
    MinimumTTL: Optional[int]
    ForwardedCookies: Optional["_CookieObject"]
    ForwardedHeaders: Optional["_HeaderObject"]
    ForwardedQueryStrings: Optional["_QueryStringObject"]

    @classmethod
    def _deserialize(
        cls: Type["_CacheSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CacheSettings"]:
        if not json_data:
            return None
        return cls(
            AllowedHTTPMethods=json_data.get("AllowedHTTPMethods"),
            CachedHTTPMethods=json_data.get("CachedHTTPMethods"),
            DefaultTTL=json_data.get("DefaultTTL"),
            MaximumTTL=json_data.get("MaximumTTL"),
            MinimumTTL=json_data.get("MinimumTTL"),
            ForwardedCookies=CookieObject._deserialize(json_data.get("ForwardedCookies")),
            ForwardedHeaders=HeaderObject._deserialize(json_data.get("ForwardedHeaders")),
            ForwardedQueryStrings=QueryStringObject._deserialize(json_data.get("ForwardedQueryStrings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CacheSettings = CacheSettings


@dataclass
class CookieObject(BaseModel):
    CookiesAllowList: Optional[AbstractSet[str]]
    Option: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CookieObject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CookieObject"]:
        if not json_data:
            return None
        return cls(
            CookiesAllowList=set_or_none(json_data.get("CookiesAllowList")),
            Option=json_data.get("Option"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CookieObject = CookieObject


@dataclass
class HeaderObject(BaseModel):
    HeadersAllowList: Optional[AbstractSet[str]]
    Option: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderObject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderObject"]:
        if not json_data:
            return None
        return cls(
            HeadersAllowList=set_or_none(json_data.get("HeadersAllowList")),
            Option=json_data.get("Option"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderObject = HeaderObject


@dataclass
class QueryStringObject(BaseModel):
    QueryStringsAllowList: Optional[AbstractSet[str]]
    Option: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_QueryStringObject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryStringObject"]:
        if not json_data:
            return None
        return cls(
            QueryStringsAllowList=set_or_none(json_data.get("QueryStringsAllowList")),
            Option=json_data.get("Option"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryStringObject = QueryStringObject


@dataclass
class CacheBehavior(BaseModel):
    Behavior: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CacheBehavior"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CacheBehavior"]:
        if not json_data:
            return None
        return cls(
            Behavior=json_data.get("Behavior"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CacheBehavior = CacheBehavior


@dataclass
class InputOrigin(BaseModel):
    Name: Optional[str]
    ProtocolPolicy: Optional[str]
    RegionName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputOrigin"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputOrigin"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            ProtocolPolicy=json_data.get("ProtocolPolicy"),
            RegionName=json_data.get("RegionName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputOrigin = InputOrigin


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


