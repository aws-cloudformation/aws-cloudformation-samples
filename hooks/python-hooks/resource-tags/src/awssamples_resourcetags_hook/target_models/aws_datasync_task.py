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
class AwsDatasyncTask(BaseModel):
    Excludes: Optional[Sequence["_FilterRule"]]
    Includes: Optional[Sequence["_FilterRule"]]
    Tags: Optional[Any]
    CloudWatchLogGroupArn: Optional[str]
    DestinationLocationArn: Optional[str]
    Name: Optional[str]
    Options: Optional["_Options"]
    Schedule: Optional["_TaskSchedule"]
    SourceLocationArn: Optional[str]
    TaskArn: Optional[str]
    Status: Optional[str]
    SourceNetworkInterfaceArns: Optional[Sequence[str]]
    DestinationNetworkInterfaceArns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDatasyncTask"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDatasyncTask"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Excludes=deserialize_list(json_data.get("Excludes"), FilterRule),
            Includes=deserialize_list(json_data.get("Includes"), FilterRule),
            Tags=json_data.get("Tags"),
            CloudWatchLogGroupArn=json_data.get("CloudWatchLogGroupArn"),
            DestinationLocationArn=json_data.get("DestinationLocationArn"),
            Name=json_data.get("Name"),
            Options=Options._deserialize(json_data.get("Options")),
            Schedule=TaskSchedule._deserialize(json_data.get("Schedule")),
            SourceLocationArn=json_data.get("SourceLocationArn"),
            TaskArn=json_data.get("TaskArn"),
            Status=json_data.get("Status"),
            SourceNetworkInterfaceArns=json_data.get("SourceNetworkInterfaceArns"),
            DestinationNetworkInterfaceArns=json_data.get("DestinationNetworkInterfaceArns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDatasyncTask = AwsDatasyncTask


@dataclass
class FilterRule(BaseModel):
    FilterType: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterRule"]:
        if not json_data:
            return None
        return cls(
            FilterType=json_data.get("FilterType"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterRule = FilterRule


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
class Options(BaseModel):
    Atime: Optional[str]
    BytesPerSecond: Optional[int]
    Gid: Optional[str]
    LogLevel: Optional[str]
    Mtime: Optional[str]
    OverwriteMode: Optional[str]
    PosixPermissions: Optional[str]
    PreserveDeletedFiles: Optional[str]
    PreserveDevices: Optional[str]
    SecurityDescriptorCopyFlags: Optional[str]
    TaskQueueing: Optional[str]
    TransferMode: Optional[str]
    Uid: Optional[str]
    VerifyMode: Optional[str]
    ObjectTags: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Options"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Options"]:
        if not json_data:
            return None
        return cls(
            Atime=json_data.get("Atime"),
            BytesPerSecond=json_data.get("BytesPerSecond"),
            Gid=json_data.get("Gid"),
            LogLevel=json_data.get("LogLevel"),
            Mtime=json_data.get("Mtime"),
            OverwriteMode=json_data.get("OverwriteMode"),
            PosixPermissions=json_data.get("PosixPermissions"),
            PreserveDeletedFiles=json_data.get("PreserveDeletedFiles"),
            PreserveDevices=json_data.get("PreserveDevices"),
            SecurityDescriptorCopyFlags=json_data.get("SecurityDescriptorCopyFlags"),
            TaskQueueing=json_data.get("TaskQueueing"),
            TransferMode=json_data.get("TransferMode"),
            Uid=json_data.get("Uid"),
            VerifyMode=json_data.get("VerifyMode"),
            ObjectTags=json_data.get("ObjectTags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Options = Options


@dataclass
class TaskSchedule(BaseModel):
    ScheduleExpression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaskSchedule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskSchedule"]:
        if not json_data:
            return None
        return cls(
            ScheduleExpression=json_data.get("ScheduleExpression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskSchedule = TaskSchedule


