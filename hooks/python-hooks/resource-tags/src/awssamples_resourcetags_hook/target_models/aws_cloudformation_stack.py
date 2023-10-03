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
class AwsCloudformationStack(BaseModel):
    Capabilities: Optional[Sequence[str]]
    RoleARN: Optional[str]
    Outputs: Optional[Sequence["_Output"]]
    Description: Optional[str]
    DisableRollback: Optional[bool]
    EnableTerminationProtection: Optional[bool]
    NotificationARNs: Optional[Sequence[str]]
    Parameters: Optional[MutableMapping[str, str]]
    ParentId: Optional[str]
    RootId: Optional[str]
    ChangeSetId: Optional[str]
    StackName: Optional[str]
    StackId: Optional[str]
    StackPolicyBody: Optional[MutableMapping[str, Any]]
    StackPolicyURL: Optional[str]
    StackStatus: Optional[str]
    StackStatusReason: Optional[str]
    Tags: Optional[Any]
    TemplateBody: Optional[MutableMapping[str, Any]]
    TemplateURL: Optional[str]
    TimeoutInMinutes: Optional[int]
    LastUpdateTime: Optional[str]
    CreationTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudformationStack"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudformationStack"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Capabilities=json_data.get("Capabilities"),
            RoleARN=json_data.get("RoleARN"),
            Outputs=deserialize_list(json_data.get("Outputs"), Output),
            Description=json_data.get("Description"),
            DisableRollback=json_data.get("DisableRollback"),
            EnableTerminationProtection=json_data.get("EnableTerminationProtection"),
            NotificationARNs=json_data.get("NotificationARNs"),
            Parameters=json_data.get("Parameters"),
            ParentId=json_data.get("ParentId"),
            RootId=json_data.get("RootId"),
            ChangeSetId=json_data.get("ChangeSetId"),
            StackName=json_data.get("StackName"),
            StackId=json_data.get("StackId"),
            StackPolicyBody=json_data.get("StackPolicyBody"),
            StackPolicyURL=json_data.get("StackPolicyURL"),
            StackStatus=json_data.get("StackStatus"),
            StackStatusReason=json_data.get("StackStatusReason"),
            Tags=json_data.get("Tags"),
            TemplateBody=json_data.get("TemplateBody"),
            TemplateURL=json_data.get("TemplateURL"),
            TimeoutInMinutes=json_data.get("TimeoutInMinutes"),
            LastUpdateTime=json_data.get("LastUpdateTime"),
            CreationTime=json_data.get("CreationTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudformationStack = AwsCloudformationStack


@dataclass
class Output(BaseModel):
    Description: Optional[str]
    ExportName: Optional[str]
    OutputKey: Optional[str]
    OutputValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Output"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Output"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            ExportName=json_data.get("ExportName"),
            OutputKey=json_data.get("OutputKey"),
            OutputValue=json_data.get("OutputValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Output = Output


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


