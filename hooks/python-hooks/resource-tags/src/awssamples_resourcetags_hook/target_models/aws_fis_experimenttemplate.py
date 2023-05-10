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
class AwsFisExperimenttemplate(BaseModel):
    Id: Optional[str]
    Description: Optional[str]
    Targets: Optional[MutableMapping[str, "_ExperimentTemplateTarget"]]
    Actions: Optional[MutableMapping[str, "_ExperimentTemplateAction"]]
    StopConditions: Optional[Sequence["_ExperimentTemplateStopCondition"]]
    LogConfiguration: Optional["_ExperimentTemplateLogConfiguration"]
    RoleArn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsFisExperimenttemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsFisExperimenttemplate"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Description=json_data.get("Description"),
            Targets=json_data.get("Targets"),
            Actions=json_data.get("Actions"),
            StopConditions=deserialize_list(json_data.get("StopConditions"), ExperimentTemplateStopCondition),
            LogConfiguration=ExperimentTemplateLogConfiguration._deserialize(json_data.get("LogConfiguration")),
            RoleArn=json_data.get("RoleArn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsFisExperimenttemplate = AwsFisExperimenttemplate


@dataclass
class ExperimentTemplateTarget(BaseModel):
    ResourceType: Optional[str]
    ResourceArns: Optional[Sequence[str]]
    ResourceTags: Optional[MutableMapping[str, str]]
    Parameters: Optional[MutableMapping[str, str]]
    Filters: Optional[Sequence["_ExperimentTemplateTargetFilter"]]
    SelectionMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExperimentTemplateTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExperimentTemplateTarget"]:
        if not json_data:
            return None
        return cls(
            ResourceType=json_data.get("ResourceType"),
            ResourceArns=json_data.get("ResourceArns"),
            ResourceTags=json_data.get("ResourceTags"),
            Parameters=json_data.get("Parameters"),
            Filters=deserialize_list(json_data.get("Filters"), ExperimentTemplateTargetFilter),
            SelectionMode=json_data.get("SelectionMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExperimentTemplateTarget = ExperimentTemplateTarget


@dataclass
class ExperimentTemplateTargetFilter(BaseModel):
    Path: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ExperimentTemplateTargetFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExperimentTemplateTargetFilter"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExperimentTemplateTargetFilter = ExperimentTemplateTargetFilter


@dataclass
class ExperimentTemplateAction(BaseModel):
    ActionId: Optional[str]
    Description: Optional[str]
    Parameters: Optional[MutableMapping[str, str]]
    Targets: Optional[MutableMapping[str, str]]
    StartAfter: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ExperimentTemplateAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExperimentTemplateAction"]:
        if not json_data:
            return None
        return cls(
            ActionId=json_data.get("ActionId"),
            Description=json_data.get("Description"),
            Parameters=json_data.get("Parameters"),
            Targets=json_data.get("Targets"),
            StartAfter=json_data.get("StartAfter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExperimentTemplateAction = ExperimentTemplateAction


@dataclass
class ExperimentTemplateStopCondition(BaseModel):
    Source: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExperimentTemplateStopCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExperimentTemplateStopCondition"]:
        if not json_data:
            return None
        return cls(
            Source=json_data.get("Source"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExperimentTemplateStopCondition = ExperimentTemplateStopCondition


@dataclass
class ExperimentTemplateLogConfiguration(BaseModel):
    CloudWatchLogsConfiguration: Optional["_CloudWatchLogsConfiguration"]
    S3Configuration: Optional["_S3Configuration"]
    LogSchemaVersion: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ExperimentTemplateLogConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExperimentTemplateLogConfiguration"]:
        if not json_data:
            return None
        return cls(
            CloudWatchLogsConfiguration=CloudWatchLogsConfiguration._deserialize(json_data.get("CloudWatchLogsConfiguration")),
            S3Configuration=S3Configuration._deserialize(json_data.get("S3Configuration")),
            LogSchemaVersion=json_data.get("LogSchemaVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExperimentTemplateLogConfiguration = ExperimentTemplateLogConfiguration


@dataclass
class CloudWatchLogsConfiguration(BaseModel):
    LogGroupArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudWatchLogsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudWatchLogsConfiguration"]:
        if not json_data:
            return None
        return cls(
            LogGroupArn=json_data.get("LogGroupArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudWatchLogsConfiguration = CloudWatchLogsConfiguration


@dataclass
class S3Configuration(BaseModel):
    BucketName: Optional[str]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Configuration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Configuration"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Configuration = S3Configuration


