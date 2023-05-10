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
class AwsRefactorspacesApplication(BaseModel):
    ApiGatewayProxy: Optional["_ApiGatewayProxyInput"]
    Arn: Optional[str]
    ApiGatewayId: Optional[str]
    VpcLinkId: Optional[str]
    NlbArn: Optional[str]
    NlbName: Optional[str]
    ApplicationIdentifier: Optional[str]
    EnvironmentIdentifier: Optional[str]
    Name: Optional[str]
    ProxyType: Optional[str]
    VpcId: Optional[str]
    StageName: Optional[str]
    ProxyUrl: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRefactorspacesApplication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRefactorspacesApplication"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ApiGatewayProxy=ApiGatewayProxyInput._deserialize(json_data.get("ApiGatewayProxy")),
            Arn=json_data.get("Arn"),
            ApiGatewayId=json_data.get("ApiGatewayId"),
            VpcLinkId=json_data.get("VpcLinkId"),
            NlbArn=json_data.get("NlbArn"),
            NlbName=json_data.get("NlbName"),
            ApplicationIdentifier=json_data.get("ApplicationIdentifier"),
            EnvironmentIdentifier=json_data.get("EnvironmentIdentifier"),
            Name=json_data.get("Name"),
            ProxyType=json_data.get("ProxyType"),
            VpcId=json_data.get("VpcId"),
            StageName=json_data.get("StageName"),
            ProxyUrl=json_data.get("ProxyUrl"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRefactorspacesApplication = AwsRefactorspacesApplication


@dataclass
class ApiGatewayProxyInput(BaseModel):
    StageName: Optional[str]
    EndpointType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApiGatewayProxyInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApiGatewayProxyInput"]:
        if not json_data:
            return None
        return cls(
            StageName=json_data.get("StageName"),
            EndpointType=json_data.get("EndpointType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApiGatewayProxyInput = ApiGatewayProxyInput


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


