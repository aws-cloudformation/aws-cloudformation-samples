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
    TaskRoleArn: Optional[str]
    IpcMode: Optional[str]
    InferenceAccelerators: Optional[AbstractSet["_InferenceAccelerator"]]
    Memory: Optional[str]
    PlacementConstraints: Optional[AbstractSet["_TaskDefinitionPlacementConstraint"]]
    Cpu: Optional[str]
    RequiresCompatibilities: Optional[AbstractSet[str]]
    NetworkMode: Optional[str]
    PidMode: Optional[str]
    ExecutionRoleArn: Optional[str]
    RuntimePlatform: Optional["_RuntimePlatform"]
    ProxyConfiguration: Optional["_ProxyConfiguration"]
    Volumes: Optional[AbstractSet["_Volume"]]
    ContainerDefinitions: Optional[AbstractSet["_ContainerDefinition"]]
    Family: Optional[str]
    EphemeralStorage: Optional["_EphemeralStorage"]
    Tags: Optional[Any]
    TaskDefinitionArn: Optional[str]

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
            TaskRoleArn=json_data.get("TaskRoleArn"),
            IpcMode=json_data.get("IpcMode"),
            InferenceAccelerators=set_or_none(json_data.get("InferenceAccelerators")),
            Memory=json_data.get("Memory"),
            PlacementConstraints=set_or_none(json_data.get("PlacementConstraints")),
            Cpu=json_data.get("Cpu"),
            RequiresCompatibilities=set_or_none(json_data.get("RequiresCompatibilities")),
            NetworkMode=json_data.get("NetworkMode"),
            PidMode=json_data.get("PidMode"),
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            RuntimePlatform=RuntimePlatform._deserialize(json_data.get("RuntimePlatform")),
            ProxyConfiguration=ProxyConfiguration._deserialize(json_data.get("ProxyConfiguration")),
            Volumes=set_or_none(json_data.get("Volumes")),
            ContainerDefinitions=set_or_none(json_data.get("ContainerDefinitions")),
            Family=json_data.get("Family"),
            EphemeralStorage=EphemeralStorage._deserialize(json_data.get("EphemeralStorage")),
            Tags=json_data.get("Tags"),
            TaskDefinitionArn=json_data.get("TaskDefinitionArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEcsTaskdefinition = AwsEcsTaskdefinition


@dataclass
class InferenceAccelerator(BaseModel):
    DeviceType: Optional[str]
    DeviceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InferenceAccelerator"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InferenceAccelerator"]:
        if not json_data:
            return None
        return cls(
            DeviceType=json_data.get("DeviceType"),
            DeviceName=json_data.get("DeviceName"),
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
class RuntimePlatform(BaseModel):
    OperatingSystemFamily: Optional[str]
    CpuArchitecture: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RuntimePlatform"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuntimePlatform"]:
        if not json_data:
            return None
        return cls(
            OperatingSystemFamily=json_data.get("OperatingSystemFamily"),
            CpuArchitecture=json_data.get("CpuArchitecture"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuntimePlatform = RuntimePlatform


@dataclass
class ProxyConfiguration(BaseModel):
    ProxyConfigurationProperties: Optional[AbstractSet["_KeyValuePair"]]
    Type: Optional[str]
    ContainerName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProxyConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProxyConfiguration"]:
        if not json_data:
            return None
        return cls(
            ProxyConfigurationProperties=set_or_none(json_data.get("ProxyConfigurationProperties")),
            Type=json_data.get("Type"),
            ContainerName=json_data.get("ContainerName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProxyConfiguration = ProxyConfiguration


@dataclass
class KeyValuePair(BaseModel):
    Value: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeyValuePair"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyValuePair"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyValuePair = KeyValuePair


@dataclass
class Volume(BaseModel):
    EFSVolumeConfiguration: Optional["_EFSVolumeConfiguration"]
    Host: Optional["_HostVolumeProperties"]
    DockerVolumeConfiguration: Optional["_DockerVolumeConfiguration"]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Volume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Volume"]:
        if not json_data:
            return None
        return cls(
            EFSVolumeConfiguration=EFSVolumeConfiguration._deserialize(json_data.get("EFSVolumeConfiguration")),
            Host=HostVolumeProperties._deserialize(json_data.get("Host")),
            DockerVolumeConfiguration=DockerVolumeConfiguration._deserialize(json_data.get("DockerVolumeConfiguration")),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Volume = Volume


@dataclass
class EFSVolumeConfiguration(BaseModel):
    FilesystemId: Optional[str]
    TransitEncryption: Optional[str]
    AuthorizationConfig: Optional["_AuthorizationConfig"]
    RootDirectory: Optional[str]
    TransitEncryptionPort: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_EFSVolumeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EFSVolumeConfiguration"]:
        if not json_data:
            return None
        return cls(
            FilesystemId=json_data.get("FilesystemId"),
            TransitEncryption=json_data.get("TransitEncryption"),
            AuthorizationConfig=AuthorizationConfig._deserialize(json_data.get("AuthorizationConfig")),
            RootDirectory=json_data.get("RootDirectory"),
            TransitEncryptionPort=json_data.get("TransitEncryptionPort"),
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
class DockerVolumeConfiguration(BaseModel):
    DriverOpts: Optional[MutableMapping[str, str]]
    Scope: Optional[str]
    Autoprovision: Optional[bool]
    Driver: Optional[str]
    Labels: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_DockerVolumeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DockerVolumeConfiguration"]:
        if not json_data:
            return None
        return cls(
            DriverOpts=json_data.get("DriverOpts"),
            Scope=json_data.get("Scope"),
            Autoprovision=json_data.get("Autoprovision"),
            Driver=json_data.get("Driver"),
            Labels=json_data.get("Labels"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DockerVolumeConfiguration = DockerVolumeConfiguration


@dataclass
class ContainerDefinition(BaseModel):
    User: Optional[str]
    Secrets: Optional[Sequence["_Secret"]]
    Memory: Optional[int]
    Privileged: Optional[bool]
    HealthCheck: Optional["_HealthCheck"]
    StartTimeout: Optional[int]
    VolumesFrom: Optional[AbstractSet["_VolumeFrom"]]
    Cpu: Optional[int]
    EntryPoint: Optional[Sequence[str]]
    DnsServers: Optional[Sequence[str]]
    ReadonlyRootFilesystem: Optional[bool]
    Image: Optional[str]
    Essential: Optional[bool]
    LogConfiguration: Optional["_LogConfiguration"]
    ResourceRequirements: Optional[Sequence["_ResourceRequirement"]]
    EnvironmentFiles: Optional[Sequence["_EnvironmentFile"]]
    Name: Optional[str]
    FirelensConfiguration: Optional["_FirelensConfiguration"]
    DockerSecurityOptions: Optional[Sequence[str]]
    SystemControls: Optional[Sequence["_SystemControl"]]
    Interactive: Optional[bool]
    DnsSearchDomains: Optional[Sequence[str]]
    Ulimits: Optional[Sequence["_Ulimit"]]
    StopTimeout: Optional[int]
    WorkingDirectory: Optional[str]
    MemoryReservation: Optional[int]
    RepositoryCredentials: Optional["_RepositoryCredentials"]
    ExtraHosts: Optional[Sequence["_HostEntry"]]
    Hostname: Optional[str]
    LinuxParameters: Optional["_LinuxParameters"]
    DisableNetworking: Optional[bool]
    PseudoTerminal: Optional[bool]
    MountPoints: Optional[Sequence["_MountPoint"]]
    DependsOn: Optional[Sequence["_ContainerDependency"]]
    DockerLabels: Optional[MutableMapping[str, str]]
    PortMappings: Optional[AbstractSet["_PortMapping"]]
    Command: Optional[Sequence[str]]
    Environment: Optional[AbstractSet["_KeyValuePair"]]
    Links: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerDefinition"]:
        if not json_data:
            return None
        return cls(
            User=json_data.get("User"),
            Secrets=deserialize_list(json_data.get("Secrets"), Secret),
            Memory=json_data.get("Memory"),
            Privileged=json_data.get("Privileged"),
            HealthCheck=HealthCheck._deserialize(json_data.get("HealthCheck")),
            StartTimeout=json_data.get("StartTimeout"),
            VolumesFrom=set_or_none(json_data.get("VolumesFrom")),
            Cpu=json_data.get("Cpu"),
            EntryPoint=json_data.get("EntryPoint"),
            DnsServers=json_data.get("DnsServers"),
            ReadonlyRootFilesystem=json_data.get("ReadonlyRootFilesystem"),
            Image=json_data.get("Image"),
            Essential=json_data.get("Essential"),
            LogConfiguration=LogConfiguration._deserialize(json_data.get("LogConfiguration")),
            ResourceRequirements=deserialize_list(json_data.get("ResourceRequirements"), ResourceRequirement),
            EnvironmentFiles=deserialize_list(json_data.get("EnvironmentFiles"), EnvironmentFile),
            Name=json_data.get("Name"),
            FirelensConfiguration=FirelensConfiguration._deserialize(json_data.get("FirelensConfiguration")),
            DockerSecurityOptions=json_data.get("DockerSecurityOptions"),
            SystemControls=deserialize_list(json_data.get("SystemControls"), SystemControl),
            Interactive=json_data.get("Interactive"),
            DnsSearchDomains=json_data.get("DnsSearchDomains"),
            Ulimits=deserialize_list(json_data.get("Ulimits"), Ulimit),
            StopTimeout=json_data.get("StopTimeout"),
            WorkingDirectory=json_data.get("WorkingDirectory"),
            MemoryReservation=json_data.get("MemoryReservation"),
            RepositoryCredentials=RepositoryCredentials._deserialize(json_data.get("RepositoryCredentials")),
            ExtraHosts=deserialize_list(json_data.get("ExtraHosts"), HostEntry),
            Hostname=json_data.get("Hostname"),
            LinuxParameters=LinuxParameters._deserialize(json_data.get("LinuxParameters")),
            DisableNetworking=json_data.get("DisableNetworking"),
            PseudoTerminal=json_data.get("PseudoTerminal"),
            MountPoints=deserialize_list(json_data.get("MountPoints"), MountPoint),
            DependsOn=deserialize_list(json_data.get("DependsOn"), ContainerDependency),
            DockerLabels=json_data.get("DockerLabels"),
            PortMappings=set_or_none(json_data.get("PortMappings")),
            Command=json_data.get("Command"),
            Environment=set_or_none(json_data.get("Environment")),
            Links=set_or_none(json_data.get("Links")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerDefinition = ContainerDefinition


@dataclass
class Secret(BaseModel):
    ValueFrom: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Secret"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Secret"]:
        if not json_data:
            return None
        return cls(
            ValueFrom=json_data.get("ValueFrom"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Secret = Secret


@dataclass
class HealthCheck(BaseModel):
    Command: Optional[Sequence[str]]
    Timeout: Optional[int]
    Retries: Optional[int]
    Interval: Optional[int]
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
            Timeout=json_data.get("Timeout"),
            Retries=json_data.get("Retries"),
            Interval=json_data.get("Interval"),
            StartPeriod=json_data.get("StartPeriod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheck = HealthCheck


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
class LogConfiguration(BaseModel):
    SecretOptions: Optional[Sequence["_Secret"]]
    Options: Optional[MutableMapping[str, str]]
    LogDriver: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogConfiguration"]:
        if not json_data:
            return None
        return cls(
            SecretOptions=deserialize_list(json_data.get("SecretOptions"), Secret),
            Options=json_data.get("Options"),
            LogDriver=json_data.get("LogDriver"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogConfiguration = LogConfiguration


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
class EnvironmentFile(BaseModel):
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentFile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentFile"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentFile = EnvironmentFile


@dataclass
class FirelensConfiguration(BaseModel):
    Options: Optional[MutableMapping[str, str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FirelensConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FirelensConfiguration"]:
        if not json_data:
            return None
        return cls(
            Options=json_data.get("Options"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FirelensConfiguration = FirelensConfiguration


@dataclass
class SystemControl(BaseModel):
    Value: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SystemControl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemControl"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemControl = SystemControl


@dataclass
class Ulimit(BaseModel):
    SoftLimit: Optional[int]
    HardLimit: Optional[int]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ulimit"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ulimit"]:
        if not json_data:
            return None
        return cls(
            SoftLimit=json_data.get("SoftLimit"),
            HardLimit=json_data.get("HardLimit"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ulimit = Ulimit


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
class LinuxParameters(BaseModel):
    Capabilities: Optional["_KernelCapabilities"]
    Swappiness: Optional[int]
    Tmpfs: Optional[Sequence["_Tmpfs"]]
    SharedMemorySize: Optional[int]
    Devices: Optional[Sequence["_Device"]]
    InitProcessEnabled: Optional[bool]
    MaxSwap: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_LinuxParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinuxParameters"]:
        if not json_data:
            return None
        return cls(
            Capabilities=KernelCapabilities._deserialize(json_data.get("Capabilities")),
            Swappiness=json_data.get("Swappiness"),
            Tmpfs=deserialize_list(json_data.get("Tmpfs"), Tmpfs),
            SharedMemorySize=json_data.get("SharedMemorySize"),
            Devices=deserialize_list(json_data.get("Devices"), Device),
            InitProcessEnabled=json_data.get("InitProcessEnabled"),
            MaxSwap=json_data.get("MaxSwap"),
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
class Tmpfs(BaseModel):
    Size: Optional[int]
    ContainerPath: Optional[str]
    MountOptions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Tmpfs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tmpfs"]:
        if not json_data:
            return None
        return cls(
            Size=json_data.get("Size"),
            ContainerPath=json_data.get("ContainerPath"),
            MountOptions=json_data.get("MountOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tmpfs = Tmpfs


@dataclass
class Device(BaseModel):
    HostPath: Optional[str]
    Permissions: Optional[AbstractSet[str]]
    ContainerPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Device"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Device"]:
        if not json_data:
            return None
        return cls(
            HostPath=json_data.get("HostPath"),
            Permissions=set_or_none(json_data.get("Permissions")),
            ContainerPath=json_data.get("ContainerPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Device = Device


@dataclass
class MountPoint(BaseModel):
    ReadOnly: Optional[bool]
    SourceVolume: Optional[str]
    ContainerPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MountPoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MountPoint"]:
        if not json_data:
            return None
        return cls(
            ReadOnly=json_data.get("ReadOnly"),
            SourceVolume=json_data.get("SourceVolume"),
            ContainerPath=json_data.get("ContainerPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MountPoint = MountPoint


@dataclass
class ContainerDependency(BaseModel):
    Condition: Optional[str]
    ContainerName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerDependency"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerDependency"]:
        if not json_data:
            return None
        return cls(
            Condition=json_data.get("Condition"),
            ContainerName=json_data.get("ContainerName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerDependency = ContainerDependency


@dataclass
class PortMapping(BaseModel):
    AppProtocol: Optional[str]
    ContainerPortRange: Optional[str]
    HostPort: Optional[int]
    ContainerPort: Optional[int]
    Protocol: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PortMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortMapping"]:
        if not json_data:
            return None
        return cls(
            AppProtocol=json_data.get("AppProtocol"),
            ContainerPortRange=json_data.get("ContainerPortRange"),
            HostPort=json_data.get("HostPort"),
            ContainerPort=json_data.get("ContainerPort"),
            Protocol=json_data.get("Protocol"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortMapping = PortMapping


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
class Tag(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


