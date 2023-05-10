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
class AwsMediastoreContainer(BaseModel):
    Policy: Optional[str]
    MetricPolicy: Optional["_MetricPolicy"]
    Endpoint: Optional[str]
    ContainerName: Optional[str]
    CorsPolicy: Optional[Sequence["_CorsRule"]]
    LifecyclePolicy: Optional[str]
    AccessLoggingEnabled: Optional[bool]
    Id: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMediastoreContainer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMediastoreContainer"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Policy=json_data.get("Policy"),
            MetricPolicy=MetricPolicy._deserialize(json_data.get("MetricPolicy")),
            Endpoint=json_data.get("Endpoint"),
            ContainerName=json_data.get("ContainerName"),
            CorsPolicy=deserialize_list(json_data.get("CorsPolicy"), CorsRule),
            LifecyclePolicy=json_data.get("LifecyclePolicy"),
            AccessLoggingEnabled=json_data.get("AccessLoggingEnabled"),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMediastoreContainer = AwsMediastoreContainer


@dataclass
class MetricPolicy(BaseModel):
    ContainerLevelMetrics: Optional[str]
    MetricPolicyRules: Optional[Sequence["_MetricPolicyRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricPolicy"]:
        if not json_data:
            return None
        return cls(
            ContainerLevelMetrics=json_data.get("ContainerLevelMetrics"),
            MetricPolicyRules=deserialize_list(json_data.get("MetricPolicyRules"), MetricPolicyRule),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricPolicy = MetricPolicy


@dataclass
class MetricPolicyRule(BaseModel):
    ObjectGroupName: Optional[str]
    ObjectGroup: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricPolicyRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricPolicyRule"]:
        if not json_data:
            return None
        return cls(
            ObjectGroupName=json_data.get("ObjectGroupName"),
            ObjectGroup=json_data.get("ObjectGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricPolicyRule = MetricPolicyRule


@dataclass
class CorsRule(BaseModel):
    AllowedMethods: Optional[Sequence[str]]
    AllowedOrigins: Optional[Sequence[str]]
    ExposeHeaders: Optional[Sequence[str]]
    MaxAgeSeconds: Optional[int]
    AllowedHeaders: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CorsRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsRule"]:
        if not json_data:
            return None
        return cls(
            AllowedMethods=json_data.get("AllowedMethods"),
            AllowedOrigins=json_data.get("AllowedOrigins"),
            ExposeHeaders=json_data.get("ExposeHeaders"),
            MaxAgeSeconds=json_data.get("MaxAgeSeconds"),
            AllowedHeaders=json_data.get("AllowedHeaders"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsRule = CorsRule


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


