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
class AwsGreengrassFunctiondefinition(BaseModel):
    LatestVersionArn: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    Name: Optional[str]
    InitialVersion: Optional["_FunctionDefinitionVersion"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGreengrassFunctiondefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGreengrassFunctiondefinition"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            LatestVersionArn=json_data.get("LatestVersionArn"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            InitialVersion=FunctionDefinitionVersion._deserialize(json_data.get("InitialVersion")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGreengrassFunctiondefinition = AwsGreengrassFunctiondefinition


@dataclass
class FunctionDefinitionVersion(BaseModel):
    DefaultConfig: Optional["_DefaultConfig"]
    Functions: Optional[Sequence["_Function"]]

    @classmethod
    def _deserialize(
        cls: Type["_FunctionDefinitionVersion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FunctionDefinitionVersion"]:
        if not json_data:
            return None
        return cls(
            DefaultConfig=DefaultConfig._deserialize(json_data.get("DefaultConfig")),
            Functions=deserialize_list(json_data.get("Functions"), Function),
        )


# work around possible type aliasing issues when variable has same name as a model
_FunctionDefinitionVersion = FunctionDefinitionVersion


@dataclass
class DefaultConfig(BaseModel):
    Execution: Optional["_Execution"]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultConfig"]:
        if not json_data:
            return None
        return cls(
            Execution=Execution._deserialize(json_data.get("Execution")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultConfig = DefaultConfig


@dataclass
class Execution(BaseModel):
    IsolationMode: Optional[str]
    RunAs: Optional["_RunAs"]

    @classmethod
    def _deserialize(
        cls: Type["_Execution"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Execution"]:
        if not json_data:
            return None
        return cls(
            IsolationMode=json_data.get("IsolationMode"),
            RunAs=RunAs._deserialize(json_data.get("RunAs")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Execution = Execution


@dataclass
class RunAs(BaseModel):
    Uid: Optional[int]
    Gid: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_RunAs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RunAs"]:
        if not json_data:
            return None
        return cls(
            Uid=json_data.get("Uid"),
            Gid=json_data.get("Gid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RunAs = RunAs


@dataclass
class Function(BaseModel):
    FunctionArn: Optional[str]
    FunctionConfiguration: Optional["_FunctionConfiguration"]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Function"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Function"]:
        if not json_data:
            return None
        return cls(
            FunctionArn=json_data.get("FunctionArn"),
            FunctionConfiguration=FunctionConfiguration._deserialize(json_data.get("FunctionConfiguration")),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Function = Function


@dataclass
class FunctionConfiguration(BaseModel):
    MemorySize: Optional[int]
    Pinned: Optional[bool]
    ExecArgs: Optional[str]
    Timeout: Optional[int]
    EncodingType: Optional[str]
    Environment: Optional["_Environment"]
    Executable: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FunctionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FunctionConfiguration"]:
        if not json_data:
            return None
        return cls(
            MemorySize=json_data.get("MemorySize"),
            Pinned=json_data.get("Pinned"),
            ExecArgs=json_data.get("ExecArgs"),
            Timeout=json_data.get("Timeout"),
            EncodingType=json_data.get("EncodingType"),
            Environment=Environment._deserialize(json_data.get("Environment")),
            Executable=json_data.get("Executable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FunctionConfiguration = FunctionConfiguration


@dataclass
class Environment(BaseModel):
    Variables: Optional[MutableMapping[str, Any]]
    Execution: Optional["_Execution"]
    ResourceAccessPolicies: Optional[Sequence["_ResourceAccessPolicy"]]
    AccessSysfs: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Environment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Environment"]:
        if not json_data:
            return None
        return cls(
            Variables=json_data.get("Variables"),
            Execution=Execution._deserialize(json_data.get("Execution")),
            ResourceAccessPolicies=deserialize_list(json_data.get("ResourceAccessPolicies"), ResourceAccessPolicy),
            AccessSysfs=json_data.get("AccessSysfs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Environment = Environment


@dataclass
class ResourceAccessPolicy(BaseModel):
    ResourceId: Optional[str]
    Permission: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceAccessPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceAccessPolicy"]:
        if not json_data:
            return None
        return cls(
            ResourceId=json_data.get("ResourceId"),
            Permission=json_data.get("Permission"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceAccessPolicy = ResourceAccessPolicy


