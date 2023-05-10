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
class AwsEmrserverlessApplication(BaseModel):
    Architecture: Optional[str]
    Name: Optional[str]
    ReleaseLabel: Optional[str]
    Type: Optional[str]
    InitialCapacity: Optional[AbstractSet["_InitialCapacityConfigKeyValuePair"]]
    MaximumCapacity: Optional["_MaximumAllowedResources"]
    Tags: Optional[Any]
    AutoStartConfiguration: Optional["_AutoStartConfiguration"]
    AutoStopConfiguration: Optional["_AutoStopConfiguration"]
    ImageConfiguration: Optional["_ImageConfigurationInput"]
    NetworkConfiguration: Optional["_NetworkConfiguration"]
    Arn: Optional[str]
    ApplicationId: Optional[str]
    WorkerTypeSpecifications: Optional[MutableMapping[str, "_WorkerTypeSpecificationInput"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEmrserverlessApplication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEmrserverlessApplication"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Architecture=json_data.get("Architecture"),
            Name=json_data.get("Name"),
            ReleaseLabel=json_data.get("ReleaseLabel"),
            Type=json_data.get("Type"),
            InitialCapacity=set_or_none(json_data.get("InitialCapacity")),
            MaximumCapacity=MaximumAllowedResources._deserialize(json_data.get("MaximumCapacity")),
            Tags=json_data.get("Tags"),
            AutoStartConfiguration=AutoStartConfiguration._deserialize(json_data.get("AutoStartConfiguration")),
            AutoStopConfiguration=AutoStopConfiguration._deserialize(json_data.get("AutoStopConfiguration")),
            ImageConfiguration=ImageConfigurationInput._deserialize(json_data.get("ImageConfiguration")),
            NetworkConfiguration=NetworkConfiguration._deserialize(json_data.get("NetworkConfiguration")),
            Arn=json_data.get("Arn"),
            ApplicationId=json_data.get("ApplicationId"),
            WorkerTypeSpecifications=json_data.get("WorkerTypeSpecifications"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEmrserverlessApplication = AwsEmrserverlessApplication


@dataclass
class InitialCapacityConfigKeyValuePair(BaseModel):
    Key: Optional[str]
    Value: Optional["_InitialCapacityConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_InitialCapacityConfigKeyValuePair"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitialCapacityConfigKeyValuePair"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=InitialCapacityConfig._deserialize(json_data.get("Value")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitialCapacityConfigKeyValuePair = InitialCapacityConfigKeyValuePair


@dataclass
class InitialCapacityConfig(BaseModel):
    WorkerCount: Optional[int]
    WorkerConfiguration: Optional["_WorkerConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_InitialCapacityConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitialCapacityConfig"]:
        if not json_data:
            return None
        return cls(
            WorkerCount=json_data.get("WorkerCount"),
            WorkerConfiguration=WorkerConfiguration._deserialize(json_data.get("WorkerConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitialCapacityConfig = InitialCapacityConfig


@dataclass
class WorkerConfiguration(BaseModel):
    Cpu: Optional[str]
    Memory: Optional[str]
    Disk: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerConfiguration"]:
        if not json_data:
            return None
        return cls(
            Cpu=json_data.get("Cpu"),
            Memory=json_data.get("Memory"),
            Disk=json_data.get("Disk"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerConfiguration = WorkerConfiguration


@dataclass
class MaximumAllowedResources(BaseModel):
    Cpu: Optional[str]
    Memory: Optional[str]
    Disk: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaximumAllowedResources"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaximumAllowedResources"]:
        if not json_data:
            return None
        return cls(
            Cpu=json_data.get("Cpu"),
            Memory=json_data.get("Memory"),
            Disk=json_data.get("Disk"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaximumAllowedResources = MaximumAllowedResources


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
class AutoStartConfiguration(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AutoStartConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoStartConfiguration"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoStartConfiguration = AutoStartConfiguration


@dataclass
class AutoStopConfiguration(BaseModel):
    Enabled: Optional[bool]
    IdleTimeoutMinutes: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AutoStopConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoStopConfiguration"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            IdleTimeoutMinutes=json_data.get("IdleTimeoutMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoStopConfiguration = AutoStopConfiguration


@dataclass
class ImageConfigurationInput(BaseModel):
    ImageUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImageConfigurationInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageConfigurationInput"]:
        if not json_data:
            return None
        return cls(
            ImageUri=json_data.get("ImageUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageConfigurationInput = ImageConfigurationInput


@dataclass
class NetworkConfiguration(BaseModel):
    SubnetIds: Optional[AbstractSet[str]]
    SecurityGroupIds: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkConfiguration"]:
        if not json_data:
            return None
        return cls(
            SubnetIds=set_or_none(json_data.get("SubnetIds")),
            SecurityGroupIds=set_or_none(json_data.get("SecurityGroupIds")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkConfiguration = NetworkConfiguration


@dataclass
class WorkerTypeSpecificationInput(BaseModel):
    ImageConfiguration: Optional["_ImageConfigurationInput"]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerTypeSpecificationInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerTypeSpecificationInput"]:
        if not json_data:
            return None
        return cls(
            ImageConfiguration=ImageConfigurationInput._deserialize(json_data.get("ImageConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerTypeSpecificationInput = WorkerTypeSpecificationInput


