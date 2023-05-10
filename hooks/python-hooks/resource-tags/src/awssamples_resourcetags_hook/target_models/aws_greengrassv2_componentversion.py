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
class AwsGreengrassv2Componentversion(BaseModel):
    Arn: Optional[str]
    ComponentName: Optional[str]
    ComponentVersion: Optional[str]
    InlineRecipe: Optional[str]
    LambdaFunction: Optional["_LambdaFunctionRecipeSource"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGreengrassv2Componentversion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGreengrassv2Componentversion"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            ComponentName=json_data.get("ComponentName"),
            ComponentVersion=json_data.get("ComponentVersion"),
            InlineRecipe=json_data.get("InlineRecipe"),
            LambdaFunction=LambdaFunctionRecipeSource._deserialize(json_data.get("LambdaFunction")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGreengrassv2Componentversion = AwsGreengrassv2Componentversion


@dataclass
class LambdaFunctionRecipeSource(BaseModel):
    LambdaArn: Optional[str]
    ComponentName: Optional[str]
    ComponentVersion: Optional[str]
    ComponentPlatforms: Optional[Sequence["_ComponentPlatform"]]
    ComponentDependencies: Optional[MutableMapping[str, "_ComponentDependencyRequirement"]]
    ComponentLambdaParameters: Optional["_LambdaExecutionParameters"]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaFunctionRecipeSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaFunctionRecipeSource"]:
        if not json_data:
            return None
        return cls(
            LambdaArn=json_data.get("LambdaArn"),
            ComponentName=json_data.get("ComponentName"),
            ComponentVersion=json_data.get("ComponentVersion"),
            ComponentPlatforms=deserialize_list(json_data.get("ComponentPlatforms"), ComponentPlatform),
            ComponentDependencies=json_data.get("ComponentDependencies"),
            ComponentLambdaParameters=LambdaExecutionParameters._deserialize(json_data.get("ComponentLambdaParameters")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaFunctionRecipeSource = LambdaFunctionRecipeSource


@dataclass
class ComponentPlatform(BaseModel):
    Name: Optional[str]
    Attributes: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentPlatform"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentPlatform"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Attributes=json_data.get("Attributes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentPlatform = ComponentPlatform


@dataclass
class ComponentDependencyRequirement(BaseModel):
    VersionRequirement: Optional[str]
    DependencyType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentDependencyRequirement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentDependencyRequirement"]:
        if not json_data:
            return None
        return cls(
            VersionRequirement=json_data.get("VersionRequirement"),
            DependencyType=json_data.get("DependencyType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentDependencyRequirement = ComponentDependencyRequirement


@dataclass
class LambdaExecutionParameters(BaseModel):
    EventSources: Optional[Sequence["_LambdaEventSource"]]
    MaxQueueSize: Optional[int]
    MaxInstancesCount: Optional[int]
    MaxIdleTimeInSeconds: Optional[int]
    TimeoutInSeconds: Optional[int]
    StatusTimeoutInSeconds: Optional[int]
    Pinned: Optional[bool]
    InputPayloadEncodingType: Optional[str]
    ExecArgs: Optional[Sequence[str]]
    EnvironmentVariables: Optional[MutableMapping[str, str]]
    LinuxProcessParams: Optional["_LambdaLinuxProcessParams"]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaExecutionParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaExecutionParameters"]:
        if not json_data:
            return None
        return cls(
            EventSources=deserialize_list(json_data.get("EventSources"), LambdaEventSource),
            MaxQueueSize=json_data.get("MaxQueueSize"),
            MaxInstancesCount=json_data.get("MaxInstancesCount"),
            MaxIdleTimeInSeconds=json_data.get("MaxIdleTimeInSeconds"),
            TimeoutInSeconds=json_data.get("TimeoutInSeconds"),
            StatusTimeoutInSeconds=json_data.get("StatusTimeoutInSeconds"),
            Pinned=json_data.get("Pinned"),
            InputPayloadEncodingType=json_data.get("InputPayloadEncodingType"),
            ExecArgs=json_data.get("ExecArgs"),
            EnvironmentVariables=json_data.get("EnvironmentVariables"),
            LinuxProcessParams=LambdaLinuxProcessParams._deserialize(json_data.get("LinuxProcessParams")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaExecutionParameters = LambdaExecutionParameters


@dataclass
class LambdaEventSource(BaseModel):
    Topic: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaEventSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaEventSource"]:
        if not json_data:
            return None
        return cls(
            Topic=json_data.get("Topic"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaEventSource = LambdaEventSource


@dataclass
class LambdaLinuxProcessParams(BaseModel):
    IsolationMode: Optional[str]
    ContainerParams: Optional["_LambdaContainerParams"]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaLinuxProcessParams"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaLinuxProcessParams"]:
        if not json_data:
            return None
        return cls(
            IsolationMode=json_data.get("IsolationMode"),
            ContainerParams=LambdaContainerParams._deserialize(json_data.get("ContainerParams")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaLinuxProcessParams = LambdaLinuxProcessParams


@dataclass
class LambdaContainerParams(BaseModel):
    MemorySizeInKB: Optional[int]
    MountROSysfs: Optional[bool]
    Volumes: Optional[Sequence["_LambdaVolumeMount"]]
    Devices: Optional[Sequence["_LambdaDeviceMount"]]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaContainerParams"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaContainerParams"]:
        if not json_data:
            return None
        return cls(
            MemorySizeInKB=json_data.get("MemorySizeInKB"),
            MountROSysfs=json_data.get("MountROSysfs"),
            Volumes=deserialize_list(json_data.get("Volumes"), LambdaVolumeMount),
            Devices=deserialize_list(json_data.get("Devices"), LambdaDeviceMount),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaContainerParams = LambdaContainerParams


@dataclass
class LambdaVolumeMount(BaseModel):
    SourcePath: Optional[str]
    DestinationPath: Optional[str]
    Permission: Optional[str]
    AddGroupOwner: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaVolumeMount"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaVolumeMount"]:
        if not json_data:
            return None
        return cls(
            SourcePath=json_data.get("SourcePath"),
            DestinationPath=json_data.get("DestinationPath"),
            Permission=json_data.get("Permission"),
            AddGroupOwner=json_data.get("AddGroupOwner"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaVolumeMount = LambdaVolumeMount


@dataclass
class LambdaDeviceMount(BaseModel):
    Path: Optional[str]
    Permission: Optional[str]
    AddGroupOwner: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaDeviceMount"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaDeviceMount"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Permission=json_data.get("Permission"),
            AddGroupOwner=json_data.get("AddGroupOwner"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaDeviceMount = LambdaDeviceMount


