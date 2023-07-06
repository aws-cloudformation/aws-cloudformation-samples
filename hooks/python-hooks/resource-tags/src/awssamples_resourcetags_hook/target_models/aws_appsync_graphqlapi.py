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
class AwsAppsyncGraphqlapi(BaseModel):
    OpenIDConnectConfig: Optional["_OpenIDConnectConfig"]
    MergedApiExecutionRoleArn: Optional[str]
    RealtimeDns: Optional[str]
    OwnerContact: Optional[str]
    Name: Optional[str]
    AdditionalAuthenticationProviders: Optional[Sequence["_AdditionalAuthenticationProvider"]]
    RealtimeUrl: Optional[str]
    GraphQLUrl: Optional[str]
    GraphQLDns: Optional[str]
    ApiType: Optional[str]
    LambdaAuthorizerConfig: Optional["_LambdaAuthorizerConfig"]
    XrayEnabled: Optional[bool]
    Visibility: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    UserPoolConfig: Optional["_UserPoolConfig"]
    ApiId: Optional[str]
    Tags: Optional[Any]
    AuthenticationType: Optional[str]
    LogConfig: Optional["_LogConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppsyncGraphqlapi"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppsyncGraphqlapi"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            OpenIDConnectConfig=OpenIDConnectConfig._deserialize(json_data.get("OpenIDConnectConfig")),
            MergedApiExecutionRoleArn=json_data.get("MergedApiExecutionRoleArn"),
            RealtimeDns=json_data.get("RealtimeDns"),
            OwnerContact=json_data.get("OwnerContact"),
            Name=json_data.get("Name"),
            AdditionalAuthenticationProviders=deserialize_list(json_data.get("AdditionalAuthenticationProviders"), AdditionalAuthenticationProvider),
            RealtimeUrl=json_data.get("RealtimeUrl"),
            GraphQLUrl=json_data.get("GraphQLUrl"),
            GraphQLDns=json_data.get("GraphQLDns"),
            ApiType=json_data.get("ApiType"),
            LambdaAuthorizerConfig=LambdaAuthorizerConfig._deserialize(json_data.get("LambdaAuthorizerConfig")),
            XrayEnabled=json_data.get("XrayEnabled"),
            Visibility=json_data.get("Visibility"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            UserPoolConfig=UserPoolConfig._deserialize(json_data.get("UserPoolConfig")),
            ApiId=json_data.get("ApiId"),
            Tags=json_data.get("Tags"),
            AuthenticationType=json_data.get("AuthenticationType"),
            LogConfig=LogConfig._deserialize(json_data.get("LogConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppsyncGraphqlapi = AwsAppsyncGraphqlapi


@dataclass
class OpenIDConnectConfig(BaseModel):
    ClientId: Optional[str]
    AuthTTL: Optional[float]
    Issuer: Optional[str]
    IatTTL: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OpenIDConnectConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenIDConnectConfig"]:
        if not json_data:
            return None
        return cls(
            ClientId=json_data.get("ClientId"),
            AuthTTL=json_data.get("AuthTTL"),
            Issuer=json_data.get("Issuer"),
            IatTTL=json_data.get("IatTTL"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenIDConnectConfig = OpenIDConnectConfig


@dataclass
class AdditionalAuthenticationProvider(BaseModel):
    LambdaAuthorizerConfig: Optional["_LambdaAuthorizerConfig"]
    OpenIDConnectConfig: Optional["_OpenIDConnectConfig"]
    UserPoolConfig: Optional["_CognitoUserPoolConfig"]
    AuthenticationType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalAuthenticationProvider"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalAuthenticationProvider"]:
        if not json_data:
            return None
        return cls(
            LambdaAuthorizerConfig=LambdaAuthorizerConfig._deserialize(json_data.get("LambdaAuthorizerConfig")),
            OpenIDConnectConfig=OpenIDConnectConfig._deserialize(json_data.get("OpenIDConnectConfig")),
            UserPoolConfig=CognitoUserPoolConfig._deserialize(json_data.get("UserPoolConfig")),
            AuthenticationType=json_data.get("AuthenticationType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalAuthenticationProvider = AdditionalAuthenticationProvider


@dataclass
class LambdaAuthorizerConfig(BaseModel):
    IdentityValidationExpression: Optional[str]
    AuthorizerUri: Optional[str]
    AuthorizerResultTtlInSeconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaAuthorizerConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaAuthorizerConfig"]:
        if not json_data:
            return None
        return cls(
            IdentityValidationExpression=json_data.get("IdentityValidationExpression"),
            AuthorizerUri=json_data.get("AuthorizerUri"),
            AuthorizerResultTtlInSeconds=json_data.get("AuthorizerResultTtlInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaAuthorizerConfig = LambdaAuthorizerConfig


@dataclass
class CognitoUserPoolConfig(BaseModel):
    AppIdClientRegex: Optional[str]
    UserPoolId: Optional[str]
    AwsRegion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CognitoUserPoolConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CognitoUserPoolConfig"]:
        if not json_data:
            return None
        return cls(
            AppIdClientRegex=json_data.get("AppIdClientRegex"),
            UserPoolId=json_data.get("UserPoolId"),
            AwsRegion=json_data.get("AwsRegion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CognitoUserPoolConfig = CognitoUserPoolConfig


@dataclass
class UserPoolConfig(BaseModel):
    AppIdClientRegex: Optional[str]
    UserPoolId: Optional[str]
    AwsRegion: Optional[str]
    DefaultAction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserPoolConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserPoolConfig"]:
        if not json_data:
            return None
        return cls(
            AppIdClientRegex=json_data.get("AppIdClientRegex"),
            UserPoolId=json_data.get("UserPoolId"),
            AwsRegion=json_data.get("AwsRegion"),
            DefaultAction=json_data.get("DefaultAction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserPoolConfig = UserPoolConfig


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
class LogConfig(BaseModel):
    ExcludeVerboseContent: Optional[bool]
    FieldLogLevel: Optional[str]
    CloudWatchLogsRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogConfig"]:
        if not json_data:
            return None
        return cls(
            ExcludeVerboseContent=json_data.get("ExcludeVerboseContent"),
            FieldLogLevel=json_data.get("FieldLogLevel"),
            CloudWatchLogsRoleArn=json_data.get("CloudWatchLogsRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogConfig = LogConfig


