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
class AwsStepfunctionsStatemachine(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    DefinitionString: Optional[str]
    RoleArn: Optional[str]
    StateMachineName: Optional[str]
    StateMachineType: Optional[str]
    StateMachineRevisionId: Optional[str]
    LoggingConfiguration: Optional["_LoggingConfiguration"]
    TracingConfiguration: Optional["_TracingConfiguration"]
    DefinitionS3Location: Optional["_S3Location"]
    DefinitionSubstitutions: Optional[MutableMapping[str, Any]]
    Definition: Optional[MutableMapping[str, Any]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsStepfunctionsStatemachine"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsStepfunctionsStatemachine"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            DefinitionString=json_data.get("DefinitionString"),
            RoleArn=json_data.get("RoleArn"),
            StateMachineName=json_data.get("StateMachineName"),
            StateMachineType=json_data.get("StateMachineType"),
            StateMachineRevisionId=json_data.get("StateMachineRevisionId"),
            LoggingConfiguration=LoggingConfiguration._deserialize(json_data.get("LoggingConfiguration")),
            TracingConfiguration=TracingConfiguration._deserialize(json_data.get("TracingConfiguration")),
            DefinitionS3Location=S3Location._deserialize(json_data.get("DefinitionS3Location")),
            DefinitionSubstitutions=json_data.get("DefinitionSubstitutions"),
            Definition=json_data.get("Definition"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsStepfunctionsStatemachine = AwsStepfunctionsStatemachine


@dataclass
class LoggingConfiguration(BaseModel):
    Level: Optional[str]
    IncludeExecutionData: Optional[bool]
    Destinations: Optional[Sequence["_LogDestination"]]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingConfiguration"]:
        if not json_data:
            return None
        return cls(
            Level=json_data.get("Level"),
            IncludeExecutionData=json_data.get("IncludeExecutionData"),
            Destinations=deserialize_list(json_data.get("Destinations"), LogDestination),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingConfiguration = LoggingConfiguration


@dataclass
class LogDestination(BaseModel):
    CloudWatchLogsLogGroup: Optional["_CloudWatchLogsLogGroup"]

    @classmethod
    def _deserialize(
        cls: Type["_LogDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogDestination"]:
        if not json_data:
            return None
        return cls(
            CloudWatchLogsLogGroup=CloudWatchLogsLogGroup._deserialize(json_data.get("CloudWatchLogsLogGroup")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogDestination = LogDestination


@dataclass
class CloudWatchLogsLogGroup(BaseModel):
    LogGroupArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudWatchLogsLogGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudWatchLogsLogGroup"]:
        if not json_data:
            return None
        return cls(
            LogGroupArn=json_data.get("LogGroupArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudWatchLogsLogGroup = CloudWatchLogsLogGroup


@dataclass
class TracingConfiguration(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TracingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TracingConfiguration"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TracingConfiguration = TracingConfiguration


@dataclass
class S3Location(BaseModel):
    Bucket: Optional[str]
    Key: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Location"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Location"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Key=json_data.get("Key"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Location = S3Location


@dataclass
class TagsEntry(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsEntry"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsEntry"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsEntry = TagsEntry


