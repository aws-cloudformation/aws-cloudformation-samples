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
class AwsApsWorkspace(BaseModel):
    WorkspaceId: Optional[str]
    Alias: Optional[str]
    Arn: Optional[str]
    AlertManagerDefinition: Optional[str]
    PrometheusEndpoint: Optional[str]
    LoggingConfiguration: Optional["_LoggingConfiguration"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApsWorkspace"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApsWorkspace"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            WorkspaceId=json_data.get("WorkspaceId"),
            Alias=json_data.get("Alias"),
            Arn=json_data.get("Arn"),
            AlertManagerDefinition=json_data.get("AlertManagerDefinition"),
            PrometheusEndpoint=json_data.get("PrometheusEndpoint"),
            LoggingConfiguration=LoggingConfiguration._deserialize(json_data.get("LoggingConfiguration")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApsWorkspace = AwsApsWorkspace


@dataclass
class LoggingConfiguration(BaseModel):
    LogGroupArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingConfiguration"]:
        if not json_data:
            return None
        return cls(
            LogGroupArn=json_data.get("LogGroupArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingConfiguration = LoggingConfiguration


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


