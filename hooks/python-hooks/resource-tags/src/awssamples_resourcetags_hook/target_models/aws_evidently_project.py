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
class AwsEvidentlyProject(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    Description: Optional[str]
    DataDelivery: Optional["_DataDeliveryObject"]
    AppConfigResource: Optional["_AppConfigResourceObject"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEvidentlyProject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEvidentlyProject"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            DataDelivery=DataDeliveryObject._deserialize(json_data.get("DataDelivery")),
            AppConfigResource=AppConfigResourceObject._deserialize(json_data.get("AppConfigResource")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEvidentlyProject = AwsEvidentlyProject


@dataclass
class DataDeliveryObject(BaseModel):
    S3: Optional["_S3Destination"]
    LogGroup: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataDeliveryObject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDeliveryObject"]:
        if not json_data:
            return None
        return cls(
            S3=S3Destination._deserialize(json_data.get("S3")),
            LogGroup=json_data.get("LogGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDeliveryObject = DataDeliveryObject


@dataclass
class S3Destination(BaseModel):
    BucketName: Optional[str]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Destination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Destination"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Destination = S3Destination


@dataclass
class AppConfigResourceObject(BaseModel):
    ApplicationId: Optional[str]
    EnvironmentId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AppConfigResourceObject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppConfigResourceObject"]:
        if not json_data:
            return None
        return cls(
            ApplicationId=json_data.get("ApplicationId"),
            EnvironmentId=json_data.get("EnvironmentId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppConfigResourceObject = AppConfigResourceObject


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


