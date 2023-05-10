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
class AwsNimblestudioStudiocomponent(BaseModel):
    Configuration: Optional["_StudioComponentConfiguration"]
    Description: Optional[str]
    Ec2SecurityGroupIds: Optional[Sequence[str]]
    InitializationScripts: Optional[Sequence["_StudioComponentInitializationScript"]]
    Name: Optional[str]
    RuntimeRoleArn: Optional[str]
    ScriptParameters: Optional[Sequence["_ScriptParameterKeyValue"]]
    SecureInitializationRoleArn: Optional[str]
    StudioComponentId: Optional[str]
    StudioId: Optional[str]
    Subtype: Optional[str]
    Tags: Optional[Any]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsNimblestudioStudiocomponent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsNimblestudioStudiocomponent"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Configuration=StudioComponentConfiguration._deserialize(json_data.get("Configuration")),
            Description=json_data.get("Description"),
            Ec2SecurityGroupIds=json_data.get("Ec2SecurityGroupIds"),
            InitializationScripts=deserialize_list(json_data.get("InitializationScripts"), StudioComponentInitializationScript),
            Name=json_data.get("Name"),
            RuntimeRoleArn=json_data.get("RuntimeRoleArn"),
            ScriptParameters=deserialize_list(json_data.get("ScriptParameters"), ScriptParameterKeyValue),
            SecureInitializationRoleArn=json_data.get("SecureInitializationRoleArn"),
            StudioComponentId=json_data.get("StudioComponentId"),
            StudioId=json_data.get("StudioId"),
            Subtype=json_data.get("Subtype"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsNimblestudioStudiocomponent = AwsNimblestudioStudiocomponent


@dataclass
class StudioComponentConfiguration(BaseModel):
    ActiveDirectoryConfiguration: Optional["_ActiveDirectoryConfiguration"]
    ComputeFarmConfiguration: Optional["_ComputeFarmConfiguration"]
    LicenseServiceConfiguration: Optional["_LicenseServiceConfiguration"]
    SharedFileSystemConfiguration: Optional["_SharedFileSystemConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_StudioComponentConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StudioComponentConfiguration"]:
        if not json_data:
            return None
        return cls(
            ActiveDirectoryConfiguration=ActiveDirectoryConfiguration._deserialize(json_data.get("ActiveDirectoryConfiguration")),
            ComputeFarmConfiguration=ComputeFarmConfiguration._deserialize(json_data.get("ComputeFarmConfiguration")),
            LicenseServiceConfiguration=LicenseServiceConfiguration._deserialize(json_data.get("LicenseServiceConfiguration")),
            SharedFileSystemConfiguration=SharedFileSystemConfiguration._deserialize(json_data.get("SharedFileSystemConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_StudioComponentConfiguration = StudioComponentConfiguration


@dataclass
class ActiveDirectoryConfiguration(BaseModel):
    ComputerAttributes: Optional[Sequence["_ActiveDirectoryComputerAttribute"]]
    DirectoryId: Optional[str]
    OrganizationalUnitDistinguishedName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActiveDirectoryConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActiveDirectoryConfiguration"]:
        if not json_data:
            return None
        return cls(
            ComputerAttributes=deserialize_list(json_data.get("ComputerAttributes"), ActiveDirectoryComputerAttribute),
            DirectoryId=json_data.get("DirectoryId"),
            OrganizationalUnitDistinguishedName=json_data.get("OrganizationalUnitDistinguishedName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActiveDirectoryConfiguration = ActiveDirectoryConfiguration


@dataclass
class ActiveDirectoryComputerAttribute(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActiveDirectoryComputerAttribute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActiveDirectoryComputerAttribute"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActiveDirectoryComputerAttribute = ActiveDirectoryComputerAttribute


@dataclass
class ComputeFarmConfiguration(BaseModel):
    ActiveDirectoryUser: Optional[str]
    Endpoint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComputeFarmConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComputeFarmConfiguration"]:
        if not json_data:
            return None
        return cls(
            ActiveDirectoryUser=json_data.get("ActiveDirectoryUser"),
            Endpoint=json_data.get("Endpoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComputeFarmConfiguration = ComputeFarmConfiguration


@dataclass
class LicenseServiceConfiguration(BaseModel):
    Endpoint: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LicenseServiceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LicenseServiceConfiguration"]:
        if not json_data:
            return None
        return cls(
            Endpoint=json_data.get("Endpoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LicenseServiceConfiguration = LicenseServiceConfiguration


@dataclass
class SharedFileSystemConfiguration(BaseModel):
    Endpoint: Optional[str]
    FileSystemId: Optional[str]
    LinuxMountPoint: Optional[str]
    ShareName: Optional[str]
    WindowsMountDrive: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SharedFileSystemConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SharedFileSystemConfiguration"]:
        if not json_data:
            return None
        return cls(
            Endpoint=json_data.get("Endpoint"),
            FileSystemId=json_data.get("FileSystemId"),
            LinuxMountPoint=json_data.get("LinuxMountPoint"),
            ShareName=json_data.get("ShareName"),
            WindowsMountDrive=json_data.get("WindowsMountDrive"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SharedFileSystemConfiguration = SharedFileSystemConfiguration


@dataclass
class StudioComponentInitializationScript(BaseModel):
    LaunchProfileProtocolVersion: Optional[str]
    Platform: Optional[str]
    RunContext: Optional[str]
    Script: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StudioComponentInitializationScript"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StudioComponentInitializationScript"]:
        if not json_data:
            return None
        return cls(
            LaunchProfileProtocolVersion=json_data.get("LaunchProfileProtocolVersion"),
            Platform=json_data.get("Platform"),
            RunContext=json_data.get("RunContext"),
            Script=json_data.get("Script"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StudioComponentInitializationScript = StudioComponentInitializationScript


@dataclass
class ScriptParameterKeyValue(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScriptParameterKeyValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScriptParameterKeyValue"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScriptParameterKeyValue = ScriptParameterKeyValue


