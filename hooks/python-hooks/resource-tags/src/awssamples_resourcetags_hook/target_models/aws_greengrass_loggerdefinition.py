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
class AwsGreengrassLoggerdefinition(BaseModel):
    LatestVersionArn: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    Name: Optional[str]
    InitialVersion: Optional["_LoggerDefinitionVersion"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGreengrassLoggerdefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGreengrassLoggerdefinition"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            LatestVersionArn=json_data.get("LatestVersionArn"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            InitialVersion=LoggerDefinitionVersion._deserialize(json_data.get("InitialVersion")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGreengrassLoggerdefinition = AwsGreengrassLoggerdefinition


@dataclass
class LoggerDefinitionVersion(BaseModel):
    Loggers: Optional[Sequence["_Logger"]]

    @classmethod
    def _deserialize(
        cls: Type["_LoggerDefinitionVersion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggerDefinitionVersion"]:
        if not json_data:
            return None
        return cls(
            Loggers=deserialize_list(json_data.get("Loggers"), Logger),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggerDefinitionVersion = LoggerDefinitionVersion


@dataclass
class Logger(BaseModel):
    Space: Optional[int]
    Type: Optional[str]
    Level: Optional[str]
    Id: Optional[str]
    Component: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Logger"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Logger"]:
        if not json_data:
            return None
        return cls(
            Space=json_data.get("Space"),
            Type=json_data.get("Type"),
            Level=json_data.get("Level"),
            Id=json_data.get("Id"),
            Component=json_data.get("Component"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Logger = Logger


