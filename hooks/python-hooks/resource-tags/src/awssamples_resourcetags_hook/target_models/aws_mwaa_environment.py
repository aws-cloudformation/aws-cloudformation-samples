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
class AwsMwaaEnvironment(BaseModel):
    Name: Optional[str]
    Arn: Optional[str]
    WebserverUrl: Optional[str]
    ExecutionRoleArn: Optional[str]
    KmsKey: Optional[str]
    AirflowVersion: Optional[str]
    SourceBucketArn: Optional[str]
    DagS3Path: Optional[str]
    PluginsS3Path: Optional[str]
    PluginsS3ObjectVersion: Optional[str]
    RequirementsS3Path: Optional[str]
    RequirementsS3ObjectVersion: Optional[str]
    StartupScriptS3Path: Optional[str]
    StartupScriptS3ObjectVersion: Optional[str]
    AirflowConfigurationOptions: Optional[MutableMapping[str, Any]]
    EnvironmentClass: Optional[str]
    MaxWorkers: Optional[int]
    MinWorkers: Optional[int]
    Schedulers: Optional[int]
    NetworkConfiguration: Optional["_NetworkConfiguration"]
    LoggingConfiguration: Optional["_LoggingConfiguration"]
    WeeklyMaintenanceWindowStart: Optional[str]
    Tags: Optional[Any]
    WebserverAccessMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMwaaEnvironment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMwaaEnvironment"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Arn=json_data.get("Arn"),
            WebserverUrl=json_data.get("WebserverUrl"),
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            KmsKey=json_data.get("KmsKey"),
            AirflowVersion=json_data.get("AirflowVersion"),
            SourceBucketArn=json_data.get("SourceBucketArn"),
            DagS3Path=json_data.get("DagS3Path"),
            PluginsS3Path=json_data.get("PluginsS3Path"),
            PluginsS3ObjectVersion=json_data.get("PluginsS3ObjectVersion"),
            RequirementsS3Path=json_data.get("RequirementsS3Path"),
            RequirementsS3ObjectVersion=json_data.get("RequirementsS3ObjectVersion"),
            StartupScriptS3Path=json_data.get("StartupScriptS3Path"),
            StartupScriptS3ObjectVersion=json_data.get("StartupScriptS3ObjectVersion"),
            AirflowConfigurationOptions=json_data.get("AirflowConfigurationOptions"),
            EnvironmentClass=json_data.get("EnvironmentClass"),
            MaxWorkers=json_data.get("MaxWorkers"),
            MinWorkers=json_data.get("MinWorkers"),
            Schedulers=json_data.get("Schedulers"),
            NetworkConfiguration=NetworkConfiguration._deserialize(json_data.get("NetworkConfiguration")),
            LoggingConfiguration=LoggingConfiguration._deserialize(json_data.get("LoggingConfiguration")),
            WeeklyMaintenanceWindowStart=json_data.get("WeeklyMaintenanceWindowStart"),
            Tags=json_data.get("Tags"),
            WebserverAccessMode=json_data.get("WebserverAccessMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMwaaEnvironment = AwsMwaaEnvironment


@dataclass
class NetworkConfiguration(BaseModel):
    SubnetIds: Optional[Sequence[str]]
    SecurityGroupIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkConfiguration"]:
        if not json_data:
            return None
        return cls(
            SubnetIds=json_data.get("SubnetIds"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkConfiguration = NetworkConfiguration


@dataclass
class LoggingConfiguration(BaseModel):
    DagProcessingLogs: Optional["_ModuleLoggingConfiguration"]
    SchedulerLogs: Optional["_ModuleLoggingConfiguration"]
    WebserverLogs: Optional["_ModuleLoggingConfiguration"]
    WorkerLogs: Optional["_ModuleLoggingConfiguration"]
    TaskLogs: Optional["_ModuleLoggingConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingConfiguration"]:
        if not json_data:
            return None
        return cls(
            DagProcessingLogs=ModuleLoggingConfiguration._deserialize(json_data.get("DagProcessingLogs")),
            SchedulerLogs=ModuleLoggingConfiguration._deserialize(json_data.get("SchedulerLogs")),
            WebserverLogs=ModuleLoggingConfiguration._deserialize(json_data.get("WebserverLogs")),
            WorkerLogs=ModuleLoggingConfiguration._deserialize(json_data.get("WorkerLogs")),
            TaskLogs=ModuleLoggingConfiguration._deserialize(json_data.get("TaskLogs")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingConfiguration = LoggingConfiguration


@dataclass
class ModuleLoggingConfiguration(BaseModel):
    Enabled: Optional[bool]
    LogLevel: Optional[str]
    CloudWatchLogGroupArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ModuleLoggingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ModuleLoggingConfiguration"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            LogLevel=json_data.get("LogLevel"),
            CloudWatchLogGroupArn=json_data.get("CloudWatchLogGroupArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ModuleLoggingConfiguration = ModuleLoggingConfiguration


