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
class AwsAppintegrationsDataintegration(BaseModel):
    Description: Optional[str]
    Id: Optional[str]
    DataIntegrationArn: Optional[str]
    Name: Optional[str]
    KmsKey: Optional[str]
    ScheduleConfig: Optional["_ScheduleConfig"]
    SourceURI: Optional[str]
    Tags: Optional[Any]
    FileConfiguration: Optional["_FileConfiguration"]
    ObjectConfiguration: Optional[MutableMapping[str, MutableMapping[str, Sequence[str]]]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppintegrationsDataintegration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppintegrationsDataintegration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            DataIntegrationArn=json_data.get("DataIntegrationArn"),
            Name=json_data.get("Name"),
            KmsKey=json_data.get("KmsKey"),
            ScheduleConfig=ScheduleConfig._deserialize(json_data.get("ScheduleConfig")),
            SourceURI=json_data.get("SourceURI"),
            Tags=json_data.get("Tags"),
            FileConfiguration=FileConfiguration._deserialize(json_data.get("FileConfiguration")),
            ObjectConfiguration=json_data.get("ObjectConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppintegrationsDataintegration = AwsAppintegrationsDataintegration


@dataclass
class ScheduleConfig(BaseModel):
    FirstExecutionFrom: Optional[str]
    Object: Optional[str]
    ScheduleExpression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleConfig"]:
        if not json_data:
            return None
        return cls(
            FirstExecutionFrom=json_data.get("FirstExecutionFrom"),
            Object=json_data.get("Object"),
            ScheduleExpression=json_data.get("ScheduleExpression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleConfig = ScheduleConfig


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


@dataclass
class FileConfiguration(BaseModel):
    Folders: Optional[Sequence[str]]
    Filters: Optional[MutableMapping[str, Sequence[str]]]

    @classmethod
    def _deserialize(
        cls: Type["_FileConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileConfiguration"]:
        if not json_data:
            return None
        return cls(
            Folders=json_data.get("Folders"),
            Filters=json_data.get("Filters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileConfiguration = FileConfiguration


