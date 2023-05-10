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
class AwsRefactorspacesService(BaseModel):
    Arn: Optional[str]
    ApplicationIdentifier: Optional[str]
    Description: Optional[str]
    EndpointType: Optional[str]
    EnvironmentIdentifier: Optional[str]
    LambdaEndpoint: Optional["_LambdaEndpointInput"]
    Name: Optional[str]
    ServiceIdentifier: Optional[str]
    UrlEndpoint: Optional["_UrlEndpointInput"]
    VpcId: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRefactorspacesService"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRefactorspacesService"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            ApplicationIdentifier=json_data.get("ApplicationIdentifier"),
            Description=json_data.get("Description"),
            EndpointType=json_data.get("EndpointType"),
            EnvironmentIdentifier=json_data.get("EnvironmentIdentifier"),
            LambdaEndpoint=LambdaEndpointInput._deserialize(json_data.get("LambdaEndpoint")),
            Name=json_data.get("Name"),
            ServiceIdentifier=json_data.get("ServiceIdentifier"),
            UrlEndpoint=UrlEndpointInput._deserialize(json_data.get("UrlEndpoint")),
            VpcId=json_data.get("VpcId"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRefactorspacesService = AwsRefactorspacesService


@dataclass
class LambdaEndpointInput(BaseModel):
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaEndpointInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaEndpointInput"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaEndpointInput = LambdaEndpointInput


@dataclass
class UrlEndpointInput(BaseModel):
    HealthUrl: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UrlEndpointInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UrlEndpointInput"]:
        if not json_data:
            return None
        return cls(
            HealthUrl=json_data.get("HealthUrl"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UrlEndpointInput = UrlEndpointInput


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


