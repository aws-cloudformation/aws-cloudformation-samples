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
class AwsEcsTaskdefinition(BaseModel):
    TaskDefinitionArn: Optional[str]
    Family: Optional[str]
    ContainerDefinitions: Optional[AbstractSet["_ContainerDefinition"]]
    Cpu: Optional[str]
    ExecutionRoleArn: Optional[str]
    EphemeralStorage: Optional["_EphemeralStorage"]
    InferenceAccelerators: Optional[AbstractSet["_InferenceAccelerator"]]
    Memory: Optional[str]
    NetworkMode: Optional[str]
    PlacementConstraints: Optional[AbstractSet["_TaskDefinitionPlacementConstraint"]]
    ProxyConfiguration: Optional["_ProxyConfiguration"]
    RequiresCompatibilities: Optional[AbstractSet[str]]
    TaskRoleArn: Optional[str]
    Volumes: Optional[AbstractSet["_Volume"]]
    PidMode: Optional[str]
    RuntimePlatform: Optional["_RuntimePlatform"]
    IpcMode: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEcsTaskdefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEcsTaskdefinition"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            TaskDefinitionArn=json_data.get("TaskDefinitionArn"),
            Family=json_data.get("Family"),
            ContainerDefinitions=set_or_none(json_data.get("ContainerDefinitions")),
            Cpu=json_data.get("Cpu"),
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            EphemeralStorage=EphemeralStorage._deserialize(json_data.get("EphemeralStorage")),
            InferenceAccelerators=set_or_none(json_data.get("InferenceAccelerators")),
            Memory=json_data.get("Memory"),
            NetworkMode=json_data.get("NetworkMode"),
            PlacementConstraints=set_or_none(json_data.get("PlacementConstraints")),
            ProxyConfiguration=ProxyConfiguration._deserialize(json_data.get("ProxyConfiguration")),
            RequiresCompatibilities=set_or_none(json_data.get("RequiresCompatibilities")),
            TaskRoleArn=json_data.get("TaskRoleArn"),
            Volumes=set_or_none(json_data.get("Volumes")),
            PidMode=json_data.get("PidMode"),
            RuntimePlatform=RuntimePlatform._deserialize(json_data.get("RuntimePlatform")),
            IpcMode=json_data.get("IpcMode"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEcsTaskdefinition = AwsEcsTaskdefinition


@dataclass
class ContainerDefinition(BaseModel):
    Command: Optional[Sequence[str]]
    Cpu: Optional[int]
    DependsOn: Optional[Sequence["_ContainerDependency"]]
    DisableNetworking: Optional[bool]
    DnsSearchDomains: Optional[Sequence[str]]
    DnsServers: Optional[Sequence[str]]
    DockerLabels: Optional[MutableMapping[str, str]]
    DockerSecurityOptions: Optional[Sequence[str]]
    EntryPoint: Optional[Sequence[str]]
    Environment: Optional[Sequence["_KeyValuePair"]]
    EnvironmentFiles: Optional[Sequence["_EnvironmentFile"]]
    Essential: Optional[bool]
    ExtraHosts: Optional[Sequence["_HostEntry"]]
    FirelensConfiguration: Optional["_FirelensConfiguration"]
    HealthCheck: Optional["_HealthCheck"]
    Hostname: Optional[str]
    Image: Optional[str]
    Links: Optional[AbstractSet[str]]
    LinuxParameters: Optional["_LinuxParameters"]
    LogConfiguration: Optional["_LogConfiguration"]
    Memory: Optional[int]
    MemoryReservation: Optional[int]
    MountPoints: Optional[Sequence["_MountPoint"]]
    Name: Optional[str]
    PortMappings: Optional[AbstractSet["_PortMapping"]]
    Privileged: Optional[bool]
    ReadonlyRootFilesystem: Optional[bool]
    RepositoryCredentials: Optional["_RepositoryCredentials"]
    ResourceRequirements: Optional[Sequence["_ResourceRequirement"]]
    Secrets: Optional[Sequence["_Secret"]]
    StartTimeout: Optional[int]
    StopTimeout: Optional[int]
    Ulimits: Optional[Sequence["_Ulimit"]]
    User: Optional[str]
    VolumesFrom: Optional[AbstractSet["_VolumeFrom"]]
    WorkingDirectory: Optional[str]
    Interactive: Optional[bool]
    PseudoTerminal: Optional[bool]
    SystemControls: Optional[Sequence["_SystemControl"]]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerDefinition"]:
        if not json_data:
            return None
        return cls(
            Command=json_data.get("Command"),
            Cpu=json_data.get("Cpu"),
            DependsOn=deserialize_list(json_data.get("DependsOn"), ContainerDependency),
            DisableNetworking=json_data.get("DisableNetworking"),
            DnsSearchDomains=json_data.get("DnsSearchDomains"),
            DnsServers=json_data.get("DnsServers"),
            DockerLabels=json_data.get("DockerLabels"),
            DockerSecurityOptions=json_data.get("DockerSecurityOptions"),
            EntryPoint=json_data.get("EntryPoint"),
            Environment=deserialize_list(json_data.get("Environment"), KeyValuePair),
            EnvironmentFiles=deserialize_list(json_data.get("EnvironmentFiles"), EnvironmentFile),
            Essential=json_data.get("Essential"),
            ExtraHosts=deserialize_list(json_data.get("ExtraHosts"), HostEntry),
            FirelensConfiguration=FirelensConfiguration._deserialize(json_data.get("FirelensConfiguration")),
            HealthCheck=HealthCheck._deserialize(json_data.get("HealthCheck")),
            Hostname=json_data.get("Hostname"),
            Image=json_data.get("Image"),
            Links=set_or_none(json_data.get("Links")),
            LinuxParameters=LinuxParameters._deserialize(json_data.get("LinuxParameters")),
            LogConfiguration=LogConfiguration._deserialize(json_data.get("LogConfiguration")),
            Memory=json_data.get("Memory"),
            MemoryReservation=json_data.get("MemoryReservation"),
            MountPoints=deserialize_list(json_data.get("MountPoints"), MountPoint),
            Name=json_data.get("Name"),
            PortMappings=set_or_none(json_data.get("PortMappings")),
            Privileged=json_data.get("Privileged"),
            ReadonlyRootFilesystem=json_data.get("ReadonlyRootFilesystem"),
            RepositoryCredentials=RepositoryCredentials._deserialize(json_data.get("RepositoryCredentials")),
            ResourceRequirements=deserialize_list(json_data.get("ResourceRequirements"), ResourceRequirement),
            Secrets=deserialize_list(json_data.get("Secrets"), Secret),
            StartTimeout=json_data.get("StartTimeout"),
            StopTimeout=json_data.get("StopTimeout"),
            Ulimits=deserialize_list(json_data.get("Ulimits"), Ulimit),
            User=json_data.get("User"),
            VolumesFrom=set_or_none(json_data.get("VolumesFrom")),
            WorkingDirectory=json_data.get("WorkingDirectory"),
            Interactive=json_data.get("Interactive"),
            PseudoTerminal=json_data.get("PseudoTerminal"),
            SystemControls=deserialize_list(json_data.get("SystemControls"), SystemControl),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerDefinition = ContainerDefinition


@dataclass
class ContainerDependency(BaseModel):
    ContainerName: Optional[str]
    Condition: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerDependency"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerDependency"]:
        if not json_data:
            return None
        return cls(
            ContainerName=json_data.get("ContainerName"),
            Condition=json_data.get("Condition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerDependency = ContainerDependency


@dataclass
class KeyValuePair(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeyValuePair"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyValuePair"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyValuePair = KeyValuePair


@dataclass
class EnvironmentFile(BaseModel):
    Value: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentFile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentFile"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentFile = EnvironmentFile


@dataclass
class HostEntry(BaseModel):
    Hostname: Optional[str]
    IpAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostEntry"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostEntry"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
            IpAddress=json_data.get("IpAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostEntry = HostEntry


@dataclass
class FirelensConfiguration(BaseModel):
    Type: Optional[str]
    Options: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_FirelensConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FirelensConfiguration"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Options=json_data.get("Options"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FirelensConfiguration = FirelensConfiguration


@dataclass
class HealthCheck(BaseModel):
    Command: Optional[Sequence[str]]
    Interval: Optional[int]
    Timeout: Optional[int]
    Retries: Optional[int]
    StartPeriod: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheck"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheck"]:
        if not json_data:
            return None
        return cls(
            Command=json_data.get("Command"),
            Interval=json_data.get("Interval"),
            Timeout=json_data.get("Timeout"),
            Retries=json_data.get("Retries"),
            StartPeriod=json_data.get("StartPeriod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheck = HealthCheck


@dataclass
class LinuxParameters(BaseModel):
    Capabilities: Optional["_KernelCapabilities"]
    Devices: Optional[Sequence["_Device"]]
    InitProcessEnabled: Optional[bool]
    MaxSwap: Optional[int]
    SharedMemorySize: Optional[int]
    Swappiness: Optional[int]
    Tmpfs: Optional[Sequence["_Tmpfs"]]

    @classmethod
    def _deserialize(
        cls: Type["_LinuxParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinuxParameters"]:
        if not json_data:
            return None
        return cls(
            Capabilities=KernelCapabilities._deserialize(json_data.get("Capabilities")),
            Devices=deserialize_list(json_data.get("Devices"), Device),
            InitProcessEnabled=json_data.get("InitProcessEnabled"),
            MaxSwap=json_data.get("MaxSwap"),
            SharedMemorySize=json_data.get("SharedMemorySize"),
            Swappiness=json_data.get("Swappiness"),
            Tmpfs=deserialize_list(json_data.get("Tmpfs"), Tmpfs),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinuxParameters = LinuxParameters


@dataclass
class KernelCapabilities(BaseModel):
    Add: Optional[Sequence[str]]
    Drop: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_KernelCapabilities"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KernelCapabilities"]:
        if not json_data:
            return None
        return cls(
            Add=json_data.get("Add"),
            Drop=json_data.get("Drop"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KernelCapabilities = KernelCapabilities


@dataclass
class Device(BaseModel):
    ContainerPath: Optional[str]
    HostPath: Optional[str]
    Permissions: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Device"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Device"]:
        if not json_data:
            return None
        return cls(
            ContainerPath=json_data.get("ContainerPath"),
            HostPath=json_data.get("HostPath"),
            Permissions=set_or_none(json_data.get("Permissions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Device = Device


@dataclass
class Tmpfs(BaseModel):
    ContainerPath: Optional[str]
    MountOptions: Optional[Sequence[str]]
    Size: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Tmpfs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tmpfs"]:
        if not json_data:
            return None
        return cls(
            ContainerPath=json_data.get("ContainerPath"),
            MountOptions=json_data.get("MountOptions"),
            Size=json_data.get("Size"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tmpfs = Tmpfs


@dataclass
class LogConfiguration(BaseModel):
    LogDriver: Optional[str]
    Options: Optional[MutableMapping[str, str]]
    SecretOptions: Optional[Sequence["_Secret"]]

    @classmethod
    def _deserialize(
        cls: Type["_LogConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogConfiguration"]:
        if not json_data:
            return None
        return cls(
            LogDriver=json_data.get("LogDriver"),
            Options=json_data.get("Options"),
            SecretOptions=deserialize_list(json_data.get("SecretOptions"), Secret),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogConfiguration = LogConfiguration


@dataclass
class Secret(BaseModel):
    Name: Optional[str]
    ValueFrom: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Secret"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Secret"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            ValueFrom=json_data.get("ValueFrom"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Secret = Secret


@dataclass
class MountPoint(BaseModel):
    ContainerPath: Optional[str]
    ReadOnly: Optional[bool]
    SourceVolume: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MountPoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MountPoint"]:
        if not json_data:
            return None
        return cls(
            ContainerPath=json_data.get("ContainerPath"),
            ReadOnly=json_data.get("ReadOnly"),
            SourceVolume=json_data.get("SourceVolume"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MountPoint = MountPoint


@dataclass
class PortMapping(BaseModel):
    Name: Optional[str]
    ContainerPort: Optional[int]
    ContainerPortRange: Optional[str]
    HostPort: Optional[int]
    Protocol: Optional[str]
    AppProtocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PortMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortMapping"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            ContainerPort=json_data.get("ContainerPort"),
            ContainerPortRange=json_data.get("ContainerPortRange"),
            HostPort=json_data.get("HostPort"),
            Protocol=json_data.get("Protocol"),
            AppProtocol=json_data.get("AppProtocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortMapping = PortMapping


@dataclass
class RepositoryCredentials(BaseModel):
    CredentialsParameter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RepositoryCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RepositoryCredentials"]:
        if not json_data:
            return None
        return cls(
            CredentialsParameter=json_data.get("CredentialsParameter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RepositoryCredentials = RepositoryCredentials


@dataclass
class ResourceRequirement(BaseModel):
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceRequirement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceRequirement"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceRequirement = ResourceRequirement


@dataclass
class Ulimit(BaseModel):
    HardLimit: Optional[int]
    Name: Optional[str]
    SoftLimit: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Ulimit"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ulimit"]:
        if not json_data:
            return None
        return cls(
            HardLimit=json_data.get("HardLimit"),
            Name=json_data.get("Name"),
            SoftLimit=json_data.get("SoftLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ulimit = Ulimit


@dataclass
class VolumeFrom(BaseModel):
    ReadOnly: Optional[bool]
    SourceContainer: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VolumeFrom"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumeFrom"]:
        if not json_data:
            return None
        return cls(
            ReadOnly=json_data.get("ReadOnly"),
            SourceContainer=json_data.get("SourceContainer"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumeFrom = VolumeFrom


@dataclass
class SystemControl(BaseModel):
    Namespace: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SystemControl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemControl"]:
        if not json_data:
            return None
        return cls(
            Namespace=json_data.get("Namespace"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemControl = SystemControl


@dataclass
class EphemeralStorage(BaseModel):
    SizeInGiB: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_EphemeralStorage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EphemeralStorage"]:
        if not json_data:
            return None
        return cls(
            SizeInGiB=json_data.get("SizeInGiB"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EphemeralStorage = EphemeralStorage


@dataclass
class InferenceAccelerator(BaseModel):
    DeviceName: Optional[str]
    DeviceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InferenceAccelerator"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InferenceAccelerator"]:
        if not json_data:
            return None
        return cls(
            DeviceName=json_data.get("DeviceName"),
            DeviceType=json_data.get("DeviceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InferenceAccelerator = InferenceAccelerator


@dataclass
class TaskDefinitionPlacementConstraint(BaseModel):
    Type: Optional[str]
    Expression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaskDefinitionPlacementConstraint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskDefinitionPlacementConstraint"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Expression=json_data.get("Expression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskDefinitionPlacementConstraint = TaskDefinitionPlacementConstraint


@dataclass
class ProxyConfiguration(BaseModel):
    ContainerName: Optional[str]
    ProxyConfigurationProperties: Optional[AbstractSet["_KeyValuePair"]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProxyConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProxyConfiguration"]:
        if not json_data:
            return None
        return cls(
            ContainerName=json_data.get("ContainerName"),
            ProxyConfigurationProperties=set_or_none(json_data.get("ProxyConfigurationProperties")),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProxyConfiguration = ProxyConfiguration


@dataclass
class Volume(BaseModel):
    DockerVolumeConfiguration: Optional["_DockerVolumeConfiguration"]
    EFSVolumeConfiguration: Optional["_EFSVolumeConfiguration"]
    Host: Optional["_HostVolumeProperties"]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Volume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Volume"]:
        if not json_data:
            return None
        return cls(
            DockerVolumeConfiguration=DockerVolumeConfiguration._deserialize(json_data.get("DockerVolumeConfiguration")),
            EFSVolumeConfiguration=EFSVolumeConfiguration._deserialize(json_data.get("EFSVolumeConfiguration")),
            Host=HostVolumeProperties._deserialize(json_data.get("Host")),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Volume = Volume


@dataclass
class DockerVolumeConfiguration(BaseModel):
    Autoprovision: Optional[bool]
    Driver: Optional[str]
    DriverOpts: Optional[MutableMapping[str, str]]
    Labels: Optional[MutableMapping[str, str]]
    Scope: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DockerVolumeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DockerVolumeConfiguration"]:
        if not json_data:
            return None
        return cls(
            Autoprovision=json_data.get("Autoprovision"),
            Driver=json_data.get("Driver"),
            DriverOpts=json_data.get("DriverOpts"),
            Labels=json_data.get("Labels"),
            Scope=json_data.get("Scope"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DockerVolumeConfiguration = DockerVolumeConfiguration


@dataclass
class EFSVolumeConfiguration(BaseModel):
    FilesystemId: Optional[str]
    RootDirectory: Optional[str]
    TransitEncryption: Optional[str]
    TransitEncryptionPort: Optional[int]
    AuthorizationConfig: Optional["_AuthorizationConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_EFSVolumeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EFSVolumeConfiguration"]:
        if not json_data:
            return None
        return cls(
            FilesystemId=json_data.get("FilesystemId"),
            RootDirectory=json_data.get("RootDirectory"),
            TransitEncryption=json_data.get("TransitEncryption"),
            TransitEncryptionPort=json_data.get("TransitEncryptionPort"),
            AuthorizationConfig=AuthorizationConfig._deserialize(json_data.get("AuthorizationConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EFSVolumeConfiguration = EFSVolumeConfiguration


@dataclass
class AuthorizationConfig(BaseModel):
    IAM: Optional[str]
    AccessPointId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthorizationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthorizationConfig"]:
        if not json_data:
            return None
        return cls(
            IAM=json_data.get("IAM"),
            AccessPointId=json_data.get("AccessPointId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthorizationConfig = AuthorizationConfig


@dataclass
class HostVolumeProperties(BaseModel):
    SourcePath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostVolumeProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostVolumeProperties"]:
        if not json_data:
            return None
        return cls(
            SourcePath=json_data.get("SourcePath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostVolumeProperties = HostVolumeProperties


@dataclass
class RuntimePlatform(BaseModel):
    CpuArchitecture: Optional[str]
    OperatingSystemFamily: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RuntimePlatform"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuntimePlatform"]:
        if not json_data:
            return None
        return cls(
            CpuArchitecture=json_data.get("CpuArchitecture"),
            OperatingSystemFamily=json_data.get("OperatingSystemFamily"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuntimePlatform = RuntimePlatform


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


