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
class AwsNimblestudioLaunchprofile(BaseModel):
    Description: Optional[str]
    Ec2SubnetIds: Optional[Sequence[str]]
    LaunchProfileId: Optional[str]
    LaunchProfileProtocolVersions: Optional[Sequence[str]]
    Name: Optional[str]
    StreamConfiguration: Optional["_StreamConfiguration"]
    StudioComponentIds: Optional[Sequence[str]]
    StudioId: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsNimblestudioLaunchprofile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsNimblestudioLaunchprofile"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            Ec2SubnetIds=json_data.get("Ec2SubnetIds"),
            LaunchProfileId=json_data.get("LaunchProfileId"),
            LaunchProfileProtocolVersions=json_data.get("LaunchProfileProtocolVersions"),
            Name=json_data.get("Name"),
            StreamConfiguration=StreamConfiguration._deserialize(json_data.get("StreamConfiguration")),
            StudioComponentIds=json_data.get("StudioComponentIds"),
            StudioId=json_data.get("StudioId"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsNimblestudioLaunchprofile = AwsNimblestudioLaunchprofile


@dataclass
class StreamConfiguration(BaseModel):
    ClipboardMode: Optional[str]
    Ec2InstanceTypes: Optional[Sequence[str]]
    MaxSessionLengthInMinutes: Optional[float]
    StreamingImageIds: Optional[Sequence[str]]
    MaxStoppedSessionLengthInMinutes: Optional[float]
    SessionStorage: Optional["_StreamConfigurationSessionStorage"]
    SessionBackup: Optional["_StreamConfigurationSessionBackup"]
    SessionPersistenceMode: Optional[str]
    VolumeConfiguration: Optional["_VolumeConfiguration"]
    AutomaticTerminationMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StreamConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StreamConfiguration"]:
        if not json_data:
            return None
        return cls(
            ClipboardMode=json_data.get("ClipboardMode"),
            Ec2InstanceTypes=json_data.get("Ec2InstanceTypes"),
            MaxSessionLengthInMinutes=json_data.get("MaxSessionLengthInMinutes"),
            StreamingImageIds=json_data.get("StreamingImageIds"),
            MaxStoppedSessionLengthInMinutes=json_data.get("MaxStoppedSessionLengthInMinutes"),
            SessionStorage=StreamConfigurationSessionStorage._deserialize(json_data.get("SessionStorage")),
            SessionBackup=StreamConfigurationSessionBackup._deserialize(json_data.get("SessionBackup")),
            SessionPersistenceMode=json_data.get("SessionPersistenceMode"),
            VolumeConfiguration=VolumeConfiguration._deserialize(json_data.get("VolumeConfiguration")),
            AutomaticTerminationMode=json_data.get("AutomaticTerminationMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StreamConfiguration = StreamConfiguration


@dataclass
class StreamConfigurationSessionStorage(BaseModel):
    Root: Optional["_StreamingSessionStorageRoot"]
    Mode: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_StreamConfigurationSessionStorage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StreamConfigurationSessionStorage"]:
        if not json_data:
            return None
        return cls(
            Root=StreamingSessionStorageRoot._deserialize(json_data.get("Root")),
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StreamConfigurationSessionStorage = StreamConfigurationSessionStorage


@dataclass
class StreamingSessionStorageRoot(BaseModel):
    Linux: Optional[str]
    Windows: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StreamingSessionStorageRoot"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StreamingSessionStorageRoot"]:
        if not json_data:
            return None
        return cls(
            Linux=json_data.get("Linux"),
            Windows=json_data.get("Windows"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StreamingSessionStorageRoot = StreamingSessionStorageRoot


@dataclass
class StreamConfigurationSessionBackup(BaseModel):
    Mode: Optional[str]
    MaxBackupsToRetain: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StreamConfigurationSessionBackup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StreamConfigurationSessionBackup"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
            MaxBackupsToRetain=json_data.get("MaxBackupsToRetain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StreamConfigurationSessionBackup = StreamConfigurationSessionBackup


@dataclass
class VolumeConfiguration(BaseModel):
    Size: Optional[float]
    Throughput: Optional[float]
    Iops: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeConfiguration"]:
        if not json_data:
            return None
        return cls(
            Size=json_data.get("Size"),
            Throughput=json_data.get("Throughput"),
            Iops=json_data.get("Iops"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeConfiguration = VolumeConfiguration


