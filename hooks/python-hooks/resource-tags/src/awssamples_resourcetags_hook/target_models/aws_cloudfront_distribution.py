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
class AwsCloudfrontDistribution(BaseModel):
    DistributionConfig: Optional["_DistributionConfig"]
    DomainName: Optional[str]
    Id: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudfrontDistribution"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudfrontDistribution"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DistributionConfig=DistributionConfig._deserialize(json_data.get("DistributionConfig")),
            DomainName=json_data.get("DomainName"),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudfrontDistribution = AwsCloudfrontDistribution


@dataclass
class DistributionConfig(BaseModel):
    Aliases: Optional[Sequence[str]]
    CNAMEs: Optional[Sequence[str]]
    CacheBehaviors: Optional[Sequence["_CacheBehavior"]]
    Comment: Optional[str]
    ContinuousDeploymentPolicyId: Optional[str]
    CustomErrorResponses: Optional[Sequence["_CustomErrorResponse"]]
    CustomOrigin: Optional["_LegacyCustomOrigin"]
    DefaultCacheBehavior: Optional["_DefaultCacheBehavior"]
    DefaultRootObject: Optional[str]
    Enabled: Optional[bool]
    HttpVersion: Optional[str]
    IPV6Enabled: Optional[bool]
    Logging: Optional["_Logging"]
    OriginGroups: Optional["_OriginGroups"]
    Origins: Optional[Sequence["_Origin"]]
    PriceClass: Optional[str]
    Restrictions: Optional["_Restrictions"]
    S3Origin: Optional["_LegacyS3Origin"]
    Staging: Optional[bool]
    ViewerCertificate: Optional["_ViewerCertificate"]
    WebACLId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DistributionConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DistributionConfig"]:
        if not json_data:
            return None
        return cls(
            Aliases=json_data.get("Aliases"),
            CNAMEs=json_data.get("CNAMEs"),
            CacheBehaviors=deserialize_list(json_data.get("CacheBehaviors"), CacheBehavior),
            Comment=json_data.get("Comment"),
            ContinuousDeploymentPolicyId=json_data.get("ContinuousDeploymentPolicyId"),
            CustomErrorResponses=deserialize_list(json_data.get("CustomErrorResponses"), CustomErrorResponse),
            CustomOrigin=LegacyCustomOrigin._deserialize(json_data.get("CustomOrigin")),
            DefaultCacheBehavior=DefaultCacheBehavior._deserialize(json_data.get("DefaultCacheBehavior")),
            DefaultRootObject=json_data.get("DefaultRootObject"),
            Enabled=json_data.get("Enabled"),
            HttpVersion=json_data.get("HttpVersion"),
            IPV6Enabled=json_data.get("IPV6Enabled"),
            Logging=Logging._deserialize(json_data.get("Logging")),
            OriginGroups=OriginGroups._deserialize(json_data.get("OriginGroups")),
            Origins=deserialize_list(json_data.get("Origins"), Origin),
            PriceClass=json_data.get("PriceClass"),
            Restrictions=Restrictions._deserialize(json_data.get("Restrictions")),
            S3Origin=LegacyS3Origin._deserialize(json_data.get("S3Origin")),
            Staging=json_data.get("Staging"),
            ViewerCertificate=ViewerCertificate._deserialize(json_data.get("ViewerCertificate")),
            WebACLId=json_data.get("WebACLId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DistributionConfig = DistributionConfig


@dataclass
class CacheBehavior(BaseModel):
    AllowedMethods: Optional[Sequence[str]]
    CachePolicyId: Optional[str]
    CachedMethods: Optional[Sequence[str]]
    Compress: Optional[bool]
    DefaultTTL: Optional[float]
    FieldLevelEncryptionId: Optional[str]
    ForwardedValues: Optional["_ForwardedValues"]
    FunctionAssociations: Optional[Sequence["_FunctionAssociation"]]
    LambdaFunctionAssociations: Optional[Sequence["_LambdaFunctionAssociation"]]
    MaxTTL: Optional[float]
    MinTTL: Optional[float]
    OriginRequestPolicyId: Optional[str]
    PathPattern: Optional[str]
    RealtimeLogConfigArn: Optional[str]
    ResponseHeadersPolicyId: Optional[str]
    SmoothStreaming: Optional[bool]
    TargetOriginId: Optional[str]
    TrustedKeyGroups: Optional[Sequence[str]]
    TrustedSigners: Optional[Sequence[str]]
    ViewerProtocolPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CacheBehavior"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CacheBehavior"]:
        if not json_data:
            return None
        return cls(
            AllowedMethods=json_data.get("AllowedMethods"),
            CachePolicyId=json_data.get("CachePolicyId"),
            CachedMethods=json_data.get("CachedMethods"),
            Compress=json_data.get("Compress"),
            DefaultTTL=json_data.get("DefaultTTL"),
            FieldLevelEncryptionId=json_data.get("FieldLevelEncryptionId"),
            ForwardedValues=ForwardedValues._deserialize(json_data.get("ForwardedValues")),
            FunctionAssociations=deserialize_list(json_data.get("FunctionAssociations"), FunctionAssociation),
            LambdaFunctionAssociations=deserialize_list(json_data.get("LambdaFunctionAssociations"), LambdaFunctionAssociation),
            MaxTTL=json_data.get("MaxTTL"),
            MinTTL=json_data.get("MinTTL"),
            OriginRequestPolicyId=json_data.get("OriginRequestPolicyId"),
            PathPattern=json_data.get("PathPattern"),
            RealtimeLogConfigArn=json_data.get("RealtimeLogConfigArn"),
            ResponseHeadersPolicyId=json_data.get("ResponseHeadersPolicyId"),
            SmoothStreaming=json_data.get("SmoothStreaming"),
            TargetOriginId=json_data.get("TargetOriginId"),
            TrustedKeyGroups=json_data.get("TrustedKeyGroups"),
            TrustedSigners=json_data.get("TrustedSigners"),
            ViewerProtocolPolicy=json_data.get("ViewerProtocolPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CacheBehavior = CacheBehavior


@dataclass
class ForwardedValues(BaseModel):
    Cookies: Optional["_Cookies"]
    Headers: Optional[Sequence[str]]
    QueryString: Optional[bool]
    QueryStringCacheKeys: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardedValues"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardedValues"]:
        if not json_data:
            return None
        return cls(
            Cookies=Cookies._deserialize(json_data.get("Cookies")),
            Headers=json_data.get("Headers"),
            QueryString=json_data.get("QueryString"),
            QueryStringCacheKeys=json_data.get("QueryStringCacheKeys"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardedValues = ForwardedValues


@dataclass
class Cookies(BaseModel):
    Forward: Optional[str]
    WhitelistedNames: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Cookies"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Cookies"]:
        if not json_data:
            return None
        return cls(
            Forward=json_data.get("Forward"),
            WhitelistedNames=json_data.get("WhitelistedNames"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Cookies = Cookies


@dataclass
class FunctionAssociation(BaseModel):
    EventType: Optional[str]
    FunctionARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FunctionAssociation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FunctionAssociation"]:
        if not json_data:
            return None
        return cls(
            EventType=json_data.get("EventType"),
            FunctionARN=json_data.get("FunctionARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FunctionAssociation = FunctionAssociation


@dataclass
class LambdaFunctionAssociation(BaseModel):
    EventType: Optional[str]
    IncludeBody: Optional[bool]
    LambdaFunctionARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaFunctionAssociation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaFunctionAssociation"]:
        if not json_data:
            return None
        return cls(
            EventType=json_data.get("EventType"),
            IncludeBody=json_data.get("IncludeBody"),
            LambdaFunctionARN=json_data.get("LambdaFunctionARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaFunctionAssociation = LambdaFunctionAssociation


@dataclass
class CustomErrorResponse(BaseModel):
    ErrorCachingMinTTL: Optional[float]
    ErrorCode: Optional[int]
    ResponseCode: Optional[int]
    ResponsePagePath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomErrorResponse"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomErrorResponse"]:
        if not json_data:
            return None
        return cls(
            ErrorCachingMinTTL=json_data.get("ErrorCachingMinTTL"),
            ErrorCode=json_data.get("ErrorCode"),
            ResponseCode=json_data.get("ResponseCode"),
            ResponsePagePath=json_data.get("ResponsePagePath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomErrorResponse = CustomErrorResponse


@dataclass
class LegacyCustomOrigin(BaseModel):
    DNSName: Optional[str]
    HTTPPort: Optional[int]
    HTTPSPort: Optional[int]
    OriginProtocolPolicy: Optional[str]
    OriginSSLProtocols: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_LegacyCustomOrigin"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LegacyCustomOrigin"]:
        if not json_data:
            return None
        return cls(
            DNSName=json_data.get("DNSName"),
            HTTPPort=json_data.get("HTTPPort"),
            HTTPSPort=json_data.get("HTTPSPort"),
            OriginProtocolPolicy=json_data.get("OriginProtocolPolicy"),
            OriginSSLProtocols=json_data.get("OriginSSLProtocols"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LegacyCustomOrigin = LegacyCustomOrigin


@dataclass
class DefaultCacheBehavior(BaseModel):
    AllowedMethods: Optional[Sequence[str]]
    CachePolicyId: Optional[str]
    CachedMethods: Optional[Sequence[str]]
    Compress: Optional[bool]
    DefaultTTL: Optional[float]
    FieldLevelEncryptionId: Optional[str]
    ForwardedValues: Optional["_ForwardedValues"]
    FunctionAssociations: Optional[Sequence["_FunctionAssociation"]]
    LambdaFunctionAssociations: Optional[Sequence["_LambdaFunctionAssociation"]]
    MaxTTL: Optional[float]
    MinTTL: Optional[float]
    OriginRequestPolicyId: Optional[str]
    RealtimeLogConfigArn: Optional[str]
    ResponseHeadersPolicyId: Optional[str]
    SmoothStreaming: Optional[bool]
    TargetOriginId: Optional[str]
    TrustedKeyGroups: Optional[Sequence[str]]
    TrustedSigners: Optional[Sequence[str]]
    ViewerProtocolPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultCacheBehavior"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultCacheBehavior"]:
        if not json_data:
            return None
        return cls(
            AllowedMethods=json_data.get("AllowedMethods"),
            CachePolicyId=json_data.get("CachePolicyId"),
            CachedMethods=json_data.get("CachedMethods"),
            Compress=json_data.get("Compress"),
            DefaultTTL=json_data.get("DefaultTTL"),
            FieldLevelEncryptionId=json_data.get("FieldLevelEncryptionId"),
            ForwardedValues=ForwardedValues._deserialize(json_data.get("ForwardedValues")),
            FunctionAssociations=deserialize_list(json_data.get("FunctionAssociations"), FunctionAssociation),
            LambdaFunctionAssociations=deserialize_list(json_data.get("LambdaFunctionAssociations"), LambdaFunctionAssociation),
            MaxTTL=json_data.get("MaxTTL"),
            MinTTL=json_data.get("MinTTL"),
            OriginRequestPolicyId=json_data.get("OriginRequestPolicyId"),
            RealtimeLogConfigArn=json_data.get("RealtimeLogConfigArn"),
            ResponseHeadersPolicyId=json_data.get("ResponseHeadersPolicyId"),
            SmoothStreaming=json_data.get("SmoothStreaming"),
            TargetOriginId=json_data.get("TargetOriginId"),
            TrustedKeyGroups=json_data.get("TrustedKeyGroups"),
            TrustedSigners=json_data.get("TrustedSigners"),
            ViewerProtocolPolicy=json_data.get("ViewerProtocolPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultCacheBehavior = DefaultCacheBehavior


@dataclass
class Logging(BaseModel):
    Bucket: Optional[str]
    IncludeCookies: Optional[bool]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Logging"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Logging"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            IncludeCookies=json_data.get("IncludeCookies"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Logging = Logging


@dataclass
class OriginGroups(BaseModel):
    Items: Optional[Sequence["_OriginGroup"]]
    Quantity: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_OriginGroups"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginGroups"]:
        if not json_data:
            return None
        return cls(
            Items=deserialize_list(json_data.get("Items"), OriginGroup),
            Quantity=json_data.get("Quantity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginGroups = OriginGroups


@dataclass
class OriginGroup(BaseModel):
    FailoverCriteria: Optional["_OriginGroupFailoverCriteria"]
    Id: Optional[str]
    Members: Optional["_OriginGroupMembers"]

    @classmethod
    def _deserialize(
        cls: Type["_OriginGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginGroup"]:
        if not json_data:
            return None
        return cls(
            FailoverCriteria=OriginGroupFailoverCriteria._deserialize(json_data.get("FailoverCriteria")),
            Id=json_data.get("Id"),
            Members=OriginGroupMembers._deserialize(json_data.get("Members")),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginGroup = OriginGroup


@dataclass
class OriginGroupFailoverCriteria(BaseModel):
    StatusCodes: Optional["_StatusCodes"]

    @classmethod
    def _deserialize(
        cls: Type["_OriginGroupFailoverCriteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginGroupFailoverCriteria"]:
        if not json_data:
            return None
        return cls(
            StatusCodes=StatusCodes._deserialize(json_data.get("StatusCodes")),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginGroupFailoverCriteria = OriginGroupFailoverCriteria


@dataclass
class StatusCodes(BaseModel):
    Items: Optional[Sequence[int]]
    Quantity: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_StatusCodes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatusCodes"]:
        if not json_data:
            return None
        return cls(
            Items=json_data.get("Items"),
            Quantity=json_data.get("Quantity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatusCodes = StatusCodes


@dataclass
class OriginGroupMembers(BaseModel):
    Items: Optional[Sequence["_OriginGroupMember"]]
    Quantity: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_OriginGroupMembers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginGroupMembers"]:
        if not json_data:
            return None
        return cls(
            Items=deserialize_list(json_data.get("Items"), OriginGroupMember),
            Quantity=json_data.get("Quantity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginGroupMembers = OriginGroupMembers


@dataclass
class OriginGroupMember(BaseModel):
    OriginId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OriginGroupMember"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginGroupMember"]:
        if not json_data:
            return None
        return cls(
            OriginId=json_data.get("OriginId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginGroupMember = OriginGroupMember


@dataclass
class Origin(BaseModel):
    ConnectionAttempts: Optional[int]
    ConnectionTimeout: Optional[int]
    CustomOriginConfig: Optional["_CustomOriginConfig"]
    DomainName: Optional[str]
    Id: Optional[str]
    OriginAccessControlId: Optional[str]
    OriginCustomHeaders: Optional[Sequence["_OriginCustomHeader"]]
    OriginPath: Optional[str]
    OriginShield: Optional["_OriginShield"]
    S3OriginConfig: Optional["_S3OriginConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_Origin"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Origin"]:
        if not json_data:
            return None
        return cls(
            ConnectionAttempts=json_data.get("ConnectionAttempts"),
            ConnectionTimeout=json_data.get("ConnectionTimeout"),
            CustomOriginConfig=CustomOriginConfig._deserialize(json_data.get("CustomOriginConfig")),
            DomainName=json_data.get("DomainName"),
            Id=json_data.get("Id"),
            OriginAccessControlId=json_data.get("OriginAccessControlId"),
            OriginCustomHeaders=deserialize_list(json_data.get("OriginCustomHeaders"), OriginCustomHeader),
            OriginPath=json_data.get("OriginPath"),
            OriginShield=OriginShield._deserialize(json_data.get("OriginShield")),
            S3OriginConfig=S3OriginConfig._deserialize(json_data.get("S3OriginConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Origin = Origin


@dataclass
class CustomOriginConfig(BaseModel):
    HTTPPort: Optional[int]
    HTTPSPort: Optional[int]
    OriginKeepaliveTimeout: Optional[int]
    OriginProtocolPolicy: Optional[str]
    OriginReadTimeout: Optional[int]
    OriginSSLProtocols: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomOriginConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomOriginConfig"]:
        if not json_data:
            return None
        return cls(
            HTTPPort=json_data.get("HTTPPort"),
            HTTPSPort=json_data.get("HTTPSPort"),
            OriginKeepaliveTimeout=json_data.get("OriginKeepaliveTimeout"),
            OriginProtocolPolicy=json_data.get("OriginProtocolPolicy"),
            OriginReadTimeout=json_data.get("OriginReadTimeout"),
            OriginSSLProtocols=json_data.get("OriginSSLProtocols"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomOriginConfig = CustomOriginConfig


@dataclass
class OriginCustomHeader(BaseModel):
    HeaderName: Optional[str]
    HeaderValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OriginCustomHeader"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginCustomHeader"]:
        if not json_data:
            return None
        return cls(
            HeaderName=json_data.get("HeaderName"),
            HeaderValue=json_data.get("HeaderValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginCustomHeader = OriginCustomHeader


@dataclass
class OriginShield(BaseModel):
    Enabled: Optional[bool]
    OriginShieldRegion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OriginShield"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginShield"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            OriginShieldRegion=json_data.get("OriginShieldRegion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginShield = OriginShield


@dataclass
class S3OriginConfig(BaseModel):
    OriginAccessIdentity: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3OriginConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3OriginConfig"]:
        if not json_data:
            return None
        return cls(
            OriginAccessIdentity=json_data.get("OriginAccessIdentity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3OriginConfig = S3OriginConfig


@dataclass
class Restrictions(BaseModel):
    GeoRestriction: Optional["_GeoRestriction"]

    @classmethod
    def _deserialize(
        cls: Type["_Restrictions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Restrictions"]:
        if not json_data:
            return None
        return cls(
            GeoRestriction=GeoRestriction._deserialize(json_data.get("GeoRestriction")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Restrictions = Restrictions


@dataclass
class GeoRestriction(BaseModel):
    Locations: Optional[Sequence[str]]
    RestrictionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GeoRestriction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeoRestriction"]:
        if not json_data:
            return None
        return cls(
            Locations=json_data.get("Locations"),
            RestrictionType=json_data.get("RestrictionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeoRestriction = GeoRestriction


@dataclass
class LegacyS3Origin(BaseModel):
    DNSName: Optional[str]
    OriginAccessIdentity: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LegacyS3Origin"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LegacyS3Origin"]:
        if not json_data:
            return None
        return cls(
            DNSName=json_data.get("DNSName"),
            OriginAccessIdentity=json_data.get("OriginAccessIdentity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LegacyS3Origin = LegacyS3Origin


@dataclass
class ViewerCertificate(BaseModel):
    AcmCertificateArn: Optional[str]
    CloudFrontDefaultCertificate: Optional[bool]
    IamCertificateId: Optional[str]
    MinimumProtocolVersion: Optional[str]
    SslSupportMethod: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ViewerCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ViewerCertificate"]:
        if not json_data:
            return None
        return cls(
            AcmCertificateArn=json_data.get("AcmCertificateArn"),
            CloudFrontDefaultCertificate=json_data.get("CloudFrontDefaultCertificate"),
            IamCertificateId=json_data.get("IamCertificateId"),
            MinimumProtocolVersion=json_data.get("MinimumProtocolVersion"),
            SslSupportMethod=json_data.get("SslSupportMethod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ViewerCertificate = ViewerCertificate


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


