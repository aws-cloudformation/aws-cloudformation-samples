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
class AwsGlueJob(BaseModel):
    Connections: Optional["_ConnectionsList"]
    MaxRetries: Optional[float]
    Description: Optional[str]
    Timeout: Optional[int]
    AllocatedCapacity: Optional[float]
    Name: Optional[str]
    Role: Optional[str]
    DefaultArguments: Optional[MutableMapping[str, Any]]
    NotificationProperty: Optional["_NotificationProperty"]
    WorkerType: Optional[str]
    ExecutionClass: Optional[str]
    LogUri: Optional[str]
    Command: Optional["_JobCommand"]
    GlueVersion: Optional[str]
    ExecutionProperty: Optional["_ExecutionProperty"]
    SecurityConfiguration: Optional[str]
    Id: Optional[str]
    NumberOfWorkers: Optional[int]
    Tags: Optional[Any]
    MaxCapacity: Optional[float]
    NonOverridableArguments: Optional[MutableMapping[str, Any]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGlueJob"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGlueJob"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Connections=ConnectionsList._deserialize(json_data.get("Connections")),
            MaxRetries=json_data.get("MaxRetries"),
            Description=json_data.get("Description"),
            Timeout=json_data.get("Timeout"),
            AllocatedCapacity=json_data.get("AllocatedCapacity"),
            Name=json_data.get("Name"),
            Role=json_data.get("Role"),
            DefaultArguments=json_data.get("DefaultArguments"),
            NotificationProperty=NotificationProperty._deserialize(json_data.get("NotificationProperty")),
            WorkerType=json_data.get("WorkerType"),
            ExecutionClass=json_data.get("ExecutionClass"),
            LogUri=json_data.get("LogUri"),
            Command=JobCommand._deserialize(json_data.get("Command")),
            GlueVersion=json_data.get("GlueVersion"),
            ExecutionProperty=ExecutionProperty._deserialize(json_data.get("ExecutionProperty")),
            SecurityConfiguration=json_data.get("SecurityConfiguration"),
            Id=json_data.get("Id"),
            NumberOfWorkers=json_data.get("NumberOfWorkers"),
            Tags=json_data.get("Tags"),
            MaxCapacity=json_data.get("MaxCapacity"),
            NonOverridableArguments=json_data.get("NonOverridableArguments"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGlueJob = AwsGlueJob


@dataclass
class ConnectionsList(BaseModel):
    Connections: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionsList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionsList"]:
        if not json_data:
            return None
        return cls(
            Connections=json_data.get("Connections"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionsList = ConnectionsList


@dataclass
class NotificationProperty(BaseModel):
    NotifyDelayAfter: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationProperty"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationProperty"]:
        if not json_data:
            return None
        return cls(
            NotifyDelayAfter=json_data.get("NotifyDelayAfter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationProperty = NotificationProperty


@dataclass
class JobCommand(BaseModel):
    Runtime: Optional[str]
    ScriptLocation: Optional[str]
    PythonVersion: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JobCommand"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JobCommand"]:
        if not json_data:
            return None
        return cls(
            Runtime=json_data.get("Runtime"),
            ScriptLocation=json_data.get("ScriptLocation"),
            PythonVersion=json_data.get("PythonVersion"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JobCommand = JobCommand


@dataclass
class ExecutionProperty(BaseModel):
    MaxConcurrentRuns: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ExecutionProperty"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExecutionProperty"]:
        if not json_data:
            return None
        return cls(
            MaxConcurrentRuns=json_data.get("MaxConcurrentRuns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExecutionProperty = ExecutionProperty


