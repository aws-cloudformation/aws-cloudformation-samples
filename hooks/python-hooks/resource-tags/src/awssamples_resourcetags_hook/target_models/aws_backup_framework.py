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
class AwsBackupFramework(BaseModel):
    FrameworkName: Optional[str]
    FrameworkDescription: Optional[str]
    FrameworkArn: Optional[str]
    DeploymentStatus: Optional[str]
    CreationTime: Optional[str]
    FrameworkControls: Optional[AbstractSet["_FrameworkControl"]]
    FrameworkStatus: Optional[str]
    FrameworkTags: Optional[Sequence["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsBackupFramework"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsBackupFramework"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            FrameworkName=json_data.get("FrameworkName"),
            FrameworkDescription=json_data.get("FrameworkDescription"),
            FrameworkArn=json_data.get("FrameworkArn"),
            DeploymentStatus=json_data.get("DeploymentStatus"),
            CreationTime=json_data.get("CreationTime"),
            FrameworkControls=set_or_none(json_data.get("FrameworkControls")),
            FrameworkStatus=json_data.get("FrameworkStatus"),
            FrameworkTags=deserialize_list(json_data.get("FrameworkTags"), Tag),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsBackupFramework = AwsBackupFramework


@dataclass
class FrameworkControl(BaseModel):
    ControlName: Optional[str]
    ControlInputParameters: Optional[AbstractSet["_ControlInputParameter"]]
    ControlScope: Optional["_ControlScope"]

    @classmethod
    def _deserialize(
        cls: Type["_FrameworkControl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FrameworkControl"]:
        if not json_data:
            return None
        return cls(
            ControlName=json_data.get("ControlName"),
            ControlInputParameters=set_or_none(json_data.get("ControlInputParameters")),
            ControlScope=ControlScope._deserialize(json_data.get("ControlScope")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FrameworkControl = FrameworkControl


@dataclass
class ControlInputParameter(BaseModel):
    ParameterName: Optional[str]
    ParameterValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ControlInputParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ControlInputParameter"]:
        if not json_data:
            return None
        return cls(
            ParameterName=json_data.get("ParameterName"),
            ParameterValue=json_data.get("ParameterValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ControlInputParameter = ControlInputParameter


@dataclass
class ControlScope(BaseModel):
    ComplianceResourceIds: Optional[Sequence[str]]
    ComplianceResourceTypes: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_ControlScope"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ControlScope"]:
        if not json_data:
            return None
        return cls(
            ComplianceResourceIds=json_data.get("ComplianceResourceIds"),
            ComplianceResourceTypes=json_data.get("ComplianceResourceTypes"),
            Tags=deserialize_list(json_data.get("Tags"), Tag),
        )


# work around possible type aliasing issues when variable has same name as a model
_ControlScope = ControlScope


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


