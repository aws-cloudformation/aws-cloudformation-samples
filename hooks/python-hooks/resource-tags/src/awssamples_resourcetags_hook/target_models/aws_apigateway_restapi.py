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
class AwsApigatewayRestapi(BaseModel):
    RestApiId: Optional[str]
    RootResourceId: Optional[str]
    ApiKeySourceType: Optional[str]
    BinaryMediaTypes: Optional[Sequence[str]]
    Body: Optional[Any]
    BodyS3Location: Optional["_S3Location"]
    CloneFrom: Optional[str]
    EndpointConfiguration: Optional["_EndpointConfiguration"]
    Description: Optional[str]
    DisableExecuteApiEndpoint: Optional[bool]
    FailOnWarnings: Optional[bool]
    Name: Optional[str]
    MinimumCompressionSize: Optional[int]
    Mode: Optional[str]
    Policy: Optional[Any]
    Parameters: Optional[Any]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayRestapi"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayRestapi"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            RestApiId=json_data.get("RestApiId"),
            RootResourceId=json_data.get("RootResourceId"),
            ApiKeySourceType=json_data.get("ApiKeySourceType"),
            BinaryMediaTypes=json_data.get("BinaryMediaTypes"),
            Body=json_data.get("Body"),
            BodyS3Location=S3Location._deserialize(json_data.get("BodyS3Location")),
            CloneFrom=json_data.get("CloneFrom"),
            EndpointConfiguration=EndpointConfiguration._deserialize(json_data.get("EndpointConfiguration")),
            Description=json_data.get("Description"),
            DisableExecuteApiEndpoint=json_data.get("DisableExecuteApiEndpoint"),
            FailOnWarnings=json_data.get("FailOnWarnings"),
            Name=json_data.get("Name"),
            MinimumCompressionSize=json_data.get("MinimumCompressionSize"),
            Mode=json_data.get("Mode"),
            Policy=json_data.get("Policy"),
            Parameters=json_data.get("Parameters"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayRestapi = AwsApigatewayRestapi


@dataclass
class S3Location(BaseModel):
    Bucket: Optional[str]
    ETag: Optional[str]
    Version: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Location"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Location"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            ETag=json_data.get("ETag"),
            Version=json_data.get("Version"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Location = S3Location


@dataclass
class EndpointConfiguration(BaseModel):
    Types: Optional[Sequence[str]]
    VpcEndpointIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointConfiguration"]:
        if not json_data:
            return None
        return cls(
            Types=json_data.get("Types"),
            VpcEndpointIds=json_data.get("VpcEndpointIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointConfiguration = EndpointConfiguration


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


