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
class AwsApigatewayv2Api(BaseModel):
    RouteSelectionExpression: Optional[str]
    BodyS3Location: Optional["_BodyS3Location"]
    Description: Optional[str]
    ApiEndpoint: Optional[str]
    BasePath: Optional[str]
    FailOnWarnings: Optional[bool]
    DisableExecuteApiEndpoint: Optional[bool]
    DisableSchemaValidation: Optional[bool]
    Name: Optional[str]
    Target: Optional[str]
    CredentialsArn: Optional[str]
    CorsConfiguration: Optional["_Cors"]
    Version: Optional[str]
    ProtocolType: Optional[str]
    RouteKey: Optional[str]
    ApiId: Optional[str]
    Body: Optional[MutableMapping[str, Any]]
    Tags: Optional[Any]
    ApiKeySelectionExpression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayv2Api"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayv2Api"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            RouteSelectionExpression=json_data.get("RouteSelectionExpression"),
            BodyS3Location=BodyS3Location._deserialize(json_data.get("BodyS3Location")),
            Description=json_data.get("Description"),
            ApiEndpoint=json_data.get("ApiEndpoint"),
            BasePath=json_data.get("BasePath"),
            FailOnWarnings=json_data.get("FailOnWarnings"),
            DisableExecuteApiEndpoint=json_data.get("DisableExecuteApiEndpoint"),
            DisableSchemaValidation=json_data.get("DisableSchemaValidation"),
            Name=json_data.get("Name"),
            Target=json_data.get("Target"),
            CredentialsArn=json_data.get("CredentialsArn"),
            CorsConfiguration=Cors._deserialize(json_data.get("CorsConfiguration")),
            Version=json_data.get("Version"),
            ProtocolType=json_data.get("ProtocolType"),
            RouteKey=json_data.get("RouteKey"),
            ApiId=json_data.get("ApiId"),
            Body=json_data.get("Body"),
            Tags=json_data.get("Tags"),
            ApiKeySelectionExpression=json_data.get("ApiKeySelectionExpression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayv2Api = AwsApigatewayv2Api


@dataclass
class BodyS3Location(BaseModel):
    Etag: Optional[str]
    Bucket: Optional[str]
    Version: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BodyS3Location"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BodyS3Location"]:
        if not json_data:
            return None
        return cls(
            Etag=json_data.get("Etag"),
            Bucket=json_data.get("Bucket"),
            Version=json_data.get("Version"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BodyS3Location = BodyS3Location


@dataclass
class Cors(BaseModel):
    AllowOrigins: Optional[Sequence[str]]
    AllowCredentials: Optional[bool]
    ExposeHeaders: Optional[Sequence[str]]
    AllowHeaders: Optional[Sequence[str]]
    MaxAge: Optional[int]
    AllowMethods: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Cors"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Cors"]:
        if not json_data:
            return None
        return cls(
            AllowOrigins=json_data.get("AllowOrigins"),
            AllowCredentials=json_data.get("AllowCredentials"),
            ExposeHeaders=json_data.get("ExposeHeaders"),
            AllowHeaders=json_data.get("AllowHeaders"),
            MaxAge=json_data.get("MaxAge"),
            AllowMethods=json_data.get("AllowMethods"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Cors = Cors


