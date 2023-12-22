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
class AwsBatchJobdefinition(BaseModel):
    ContainerProperties: Optional["_ContainerProperties"]
    ContainerOrchestrationType: Optional[str]
    NodeProperties: Optional["_NodeProperties"]
    JobDefinitionName: Optional[str]
    JobDefinitionArn: Optional[str]
    Revision: Optional[int]
    Status: Optional[str]
    SchedulingPriority: Optional[int]
    Parameters: Optional[MutableMapping[str, str]]
    PlatformCapabilities: Optional[Sequence[str]]
    PropagateTags: Optional[bool]
    RetryStrategy: Optional["_RetryStrategy"]
    Timeout: Optional["_JobTimeout"]
    Type: Optional[str]
    Tags: Optional[Any]
    EksProperties: Optional["_EksProperties"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsBatchJobdefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsBatchJobdefinition"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ContainerProperties=ContainerProperties._deserialize(json_data.get("ContainerProperties")),
            ContainerOrchestrationType=json_data.get("ContainerOrchestrationType"),
            NodeProperties=NodeProperties._deserialize(json_data.get("NodeProperties")),
            JobDefinitionName=json_data.get("JobDefinitionName"),
            JobDefinitionArn=json_data.get("JobDefinitionArn"),
            Revision=json_data.get("Revision"),
            Status=json_data.get("Status"),
            SchedulingPriority=json_data.get("SchedulingPriority"),
            Parameters=json_data.get("Parameters"),
            PlatformCapabilities=json_data.get("PlatformCapabilities"),
            PropagateTags=json_data.get("PropagateTags"),
            RetryStrategy=RetryStrategy._deserialize(json_data.get("RetryStrategy")),
            Timeout=JobTimeout._deserialize(json_data.get("Timeout")),
            Type=json_data.get("Type"),
            Tags=json_data.get("Tags"),
            EksProperties=EksProperties._deserialize(json_data.get("EksProperties")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsBatchJobdefinition = AwsBatchJobdefinition


@dataclass
class ContainerProperties(BaseModel):
    Command: Optional[Sequence[str]]
    Environment: Optional[Sequence["_Environment"]]
    Image: Optional[str]
    JobRoleArn: Optional[str]
    Memory: Optional[int]
    MountPoints: Optional[Sequence["_MountPoint"]]
    Privileged: Optional[bool]
    ReadonlyRootFilesystem: Optional[bool]
    Ulimits: Optional[Sequence["_Ulimit"]]
    User: Optional[str]
    Vcpus: Optional[int]
    Volumes: Optional[Sequence["_Volume"]]
    InstanceType: Optional[str]
    ResourceRequirements: Optional[Sequence["_ResourceRequirement"]]
    LinuxParameters: Optional["_LinuxParameters"]
    LogConfiguration: Optional["_LogConfiguration"]
    ExecutionRoleArn: Optional[str]
    Secrets: Optional[Sequence["_Secret"]]
    NetworkConfiguration: Optional["_NetworkConfiguration"]
    FargatePlatformConfiguration: Optional["_FargatePlatformConfiguration"]
    EphemeralStorage: Optional["_EphemeralStorage"]
    RuntimePlatform: Optional["_RuntimePlatform"]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerProperties"]:
        if not json_data:
            return None
        return cls(
            Command=json_data.get("Command"),
            Environment=deserialize_list(json_data.get("Environment"), Environment),
            Image=json_data.get("Image"),
            JobRoleArn=json_data.get("JobRoleArn"),
            Memory=json_data.get("Memory"),
            MountPoints=deserialize_list(json_data.get("MountPoints"), MountPoint),
            Privileged=json_data.get("Privileged"),
            ReadonlyRootFilesystem=json_data.get("ReadonlyRootFilesystem"),
            Ulimits=deserialize_list(json_data.get("Ulimits"), Ulimit),
            User=json_data.get("User"),
            Vcpus=json_data.get("Vcpus"),
            Volumes=deserialize_list(json_data.get("Volumes"), Volume),
            InstanceType=json_data.get("InstanceType"),
            ResourceRequirements=deserialize_list(json_data.get("ResourceRequirements"), ResourceRequirement),
            LinuxParameters=LinuxParameters._deserialize(json_data.get("LinuxParameters")),
            LogConfiguration=LogConfiguration._deserialize(json_data.get("LogConfiguration")),
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            Secrets=deserialize_list(json_data.get("Secrets"), Secret),
            NetworkConfiguration=NetworkConfiguration._deserialize(json_data.get("NetworkConfiguration")),
            FargatePlatformConfiguration=FargatePlatformConfiguration._deserialize(json_data.get("FargatePlatformConfiguration")),
            EphemeralStorage=EphemeralStorage._deserialize(json_data.get("EphemeralStorage")),
            RuntimePlatform=RuntimePlatform._deserialize(json_data.get("RuntimePlatform")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerProperties = ContainerProperties


@dataclass
class Environment(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Environment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Environment"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Environment = Environment


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
class Volume(BaseModel):
    Host: Optional["_Host"]
    EfsVolumeConfiguration: Optional["_EFSVolumeConfiguration"]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Volume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Volume"]:
        if not json_data:
            return None
        return cls(
            Host=Host._deserialize(json_data.get("Host")),
            EfsVolumeConfiguration=EFSVolumeConfiguration._deserialize(json_data.get("EfsVolumeConfiguration")),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Volume = Volume


@dataclass
class Host(BaseModel):
    SourcePath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Host"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Host"]:
        if not json_data:
            return None
        return cls(
            SourcePath=json_data.get("SourcePath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Host = Host


@dataclass
class EFSVolumeConfiguration(BaseModel):
    FileSystemId: Optional[str]
    RootDirectory: Optional[str]
    TransitEncryption: Optional[str]
    TransitEncryptionPort: Optional[int]
    AuthorizationConfig: Optional["_EFSAuthorizationConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_EFSVolumeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EFSVolumeConfiguration"]:
        if not json_data:
            return None
        return cls(
            FileSystemId=json_data.get("FileSystemId"),
            RootDirectory=json_data.get("RootDirectory"),
            TransitEncryption=json_data.get("TransitEncryption"),
            TransitEncryptionPort=json_data.get("TransitEncryptionPort"),
            AuthorizationConfig=EFSAuthorizationConfig._deserialize(json_data.get("AuthorizationConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EFSVolumeConfiguration = EFSVolumeConfiguration


@dataclass
class EFSAuthorizationConfig(BaseModel):
    AccessPointId: Optional[str]
    Iam: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EFSAuthorizationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EFSAuthorizationConfig"]:
        if not json_data:
            return None
        return cls(
            AccessPointId=json_data.get("AccessPointId"),
            Iam=json_data.get("Iam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EFSAuthorizationConfig = EFSAuthorizationConfig


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
class LinuxParameters(BaseModel):
    Devices: Optional[Sequence["_Device"]]
    InitProcessEnabled: Optional[bool]
    MaxSwap: Optional[int]
    Swappiness: Optional[int]
    SharedMemorySize: Optional[int]
    Tmpfs: Optional[Sequence["_Tmpfs"]]

    @classmethod
    def _deserialize(
        cls: Type["_LinuxParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinuxParameters"]:
        if not json_data:
            return None
        return cls(
            Devices=deserialize_list(json_data.get("Devices"), Device),
            InitProcessEnabled=json_data.get("InitProcessEnabled"),
            MaxSwap=json_data.get("MaxSwap"),
            Swappiness=json_data.get("Swappiness"),
            SharedMemorySize=json_data.get("SharedMemorySize"),
            Tmpfs=deserialize_list(json_data.get("Tmpfs"), Tmpfs),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinuxParameters = LinuxParameters


@dataclass
class Device(BaseModel):
    HostPath: Optional[str]
    ContainerPath: Optional[str]
    Permissions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Device"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Device"]:
        if not json_data:
            return None
        return cls(
            HostPath=json_data.get("HostPath"),
            ContainerPath=json_data.get("ContainerPath"),
            Permissions=json_data.get("Permissions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Device = Device


@dataclass
class Tmpfs(BaseModel):
    ContainerPath: Optional[str]
    Size: Optional[int]
    MountOptions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Tmpfs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tmpfs"]:
        if not json_data:
            return None
        return cls(
            ContainerPath=json_data.get("ContainerPath"),
            Size=json_data.get("Size"),
            MountOptions=json_data.get("MountOptions"),
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
class NetworkConfiguration(BaseModel):
    AssignPublicIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkConfiguration"]:
        if not json_data:
            return None
        return cls(
            AssignPublicIp=json_data.get("AssignPublicIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkConfiguration = NetworkConfiguration


@dataclass
class FargatePlatformConfiguration(BaseModel):
    PlatformVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FargatePlatformConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FargatePlatformConfiguration"]:
        if not json_data:
            return None
        return cls(
            PlatformVersion=json_data.get("PlatformVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FargatePlatformConfiguration = FargatePlatformConfiguration


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
class NodeProperties(BaseModel):
    NumNodes: Optional[int]
    MainNode: Optional[int]
    NodeRangeProperties: Optional[Sequence["_NodeRangeProperty"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodeProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeProperties"]:
        if not json_data:
            return None
        return cls(
            NumNodes=json_data.get("NumNodes"),
            MainNode=json_data.get("MainNode"),
            NodeRangeProperties=deserialize_list(json_data.get("NodeRangeProperties"), NodeRangeProperty),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeProperties = NodeProperties


@dataclass
class NodeRangeProperty(BaseModel):
    TargetNodes: Optional[str]
    Container: Optional["_ContainerProperties"]

    @classmethod
    def _deserialize(
        cls: Type["_NodeRangeProperty"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeRangeProperty"]:
        if not json_data:
            return None
        return cls(
            TargetNodes=json_data.get("TargetNodes"),
            Container=ContainerProperties._deserialize(json_data.get("Container")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeRangeProperty = NodeRangeProperty


@dataclass
class RetryStrategy(BaseModel):
    Attempts: Optional[int]
    EvaluateOnExit: Optional[Sequence["_EvaluateOnExit"]]

    @classmethod
    def _deserialize(
        cls: Type["_RetryStrategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetryStrategy"]:
        if not json_data:
            return None
        return cls(
            Attempts=json_data.get("Attempts"),
            EvaluateOnExit=deserialize_list(json_data.get("EvaluateOnExit"), EvaluateOnExit),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetryStrategy = RetryStrategy


@dataclass
class EvaluateOnExit(BaseModel):
    OnExitCode: Optional[str]
    OnStatusReason: Optional[str]
    OnReason: Optional[str]
    Action: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EvaluateOnExit"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EvaluateOnExit"]:
        if not json_data:
            return None
        return cls(
            OnExitCode=json_data.get("OnExitCode"),
            OnStatusReason=json_data.get("OnStatusReason"),
            OnReason=json_data.get("OnReason"),
            Action=json_data.get("Action"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EvaluateOnExit = EvaluateOnExit


@dataclass
class JobTimeout(BaseModel):
    AttemptDurationSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_JobTimeout"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JobTimeout"]:
        if not json_data:
            return None
        return cls(
            AttemptDurationSeconds=json_data.get("AttemptDurationSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JobTimeout = JobTimeout


@dataclass
class EksProperties(BaseModel):
    PodProperties: Optional["_EksPodProperties"]

    @classmethod
    def _deserialize(
        cls: Type["_EksProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EksProperties"]:
        if not json_data:
            return None
        return cls(
            PodProperties=EksPodProperties._deserialize(json_data.get("PodProperties")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EksProperties = EksProperties


@dataclass
class EksPodProperties(BaseModel):
    ServiceAccountName: Optional[str]
    HostNetwork: Optional[bool]
    DnsPolicy: Optional[str]
    Containers: Optional[Sequence["_EksContainer"]]
    Volumes: Optional[Sequence["_EksVolume"]]
    Metadata: Optional["_EksMetadata"]

    @classmethod
    def _deserialize(
        cls: Type["_EksPodProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EksPodProperties"]:
        if not json_data:
            return None
        return cls(
            ServiceAccountName=json_data.get("ServiceAccountName"),
            HostNetwork=json_data.get("HostNetwork"),
            DnsPolicy=json_data.get("DnsPolicy"),
            Containers=deserialize_list(json_data.get("Containers"), EksContainer),
            Volumes=deserialize_list(json_data.get("Volumes"), EksVolume),
            Metadata=EksMetadata._deserialize(json_data.get("Metadata")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EksPodProperties = EksPodProperties


@dataclass
class EksContainer(BaseModel):
    Name: Optional[str]
    Image: Optional[str]
    ImagePullPolicy: Optional[str]
    Command: Optional[Sequence[str]]
    Args: Optional[Sequence[str]]
    Env: Optional[Sequence["_EksContainerEnvironmentVariable"]]
    Resources: Optional["_EksContainerResourceRequirements"]
    VolumeMounts: Optional[Sequence["_EksContainerVolumeMount"]]
    SecurityContext: Optional["_EksContainerSecurityContext"]

    @classmethod
    def _deserialize(
        cls: Type["_EksContainer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EksContainer"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Image=json_data.get("Image"),
            ImagePullPolicy=json_data.get("ImagePullPolicy"),
            Command=json_data.get("Command"),
            Args=json_data.get("Args"),
            Env=deserialize_list(json_data.get("Env"), EksContainerEnvironmentVariable),
            Resources=EksContainerResourceRequirements._deserialize(json_data.get("Resources")),
            VolumeMounts=deserialize_list(json_data.get("VolumeMounts"), EksContainerVolumeMount),
            SecurityContext=EksContainerSecurityContext._deserialize(json_data.get("SecurityContext")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EksContainer = EksContainer


@dataclass
class EksContainerEnvironmentVariable(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EksContainerEnvironmentVariable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EksContainerEnvironmentVariable"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EksContainerEnvironmentVariable = EksContainerEnvironmentVariable


@dataclass
class EksContainerResourceRequirements(BaseModel):
    Limits: Optional[MutableMapping[str, str]]
    Requests: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_EksContainerResourceRequirements"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EksContainerResourceRequirements"]:
        if not json_data:
            return None
        return cls(
            Limits=json_data.get("Limits"),
            Requests=json_data.get("Requests"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EksContainerResourceRequirements = EksContainerResourceRequirements


@dataclass
class EksContainerVolumeMount(BaseModel):
    Name: Optional[str]
    MountPath: Optional[str]
    ReadOnly: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EksContainerVolumeMount"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EksContainerVolumeMount"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            MountPath=json_data.get("MountPath"),
            ReadOnly=json_data.get("ReadOnly"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EksContainerVolumeMount = EksContainerVolumeMount


@dataclass
class EksContainerSecurityContext(BaseModel):
    RunAsUser: Optional[int]
    RunAsGroup: Optional[int]
    Privileged: Optional[bool]
    ReadOnlyRootFilesystem: Optional[bool]
    RunAsNonRoot: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EksContainerSecurityContext"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EksContainerSecurityContext"]:
        if not json_data:
            return None
        return cls(
            RunAsUser=json_data.get("RunAsUser"),
            RunAsGroup=json_data.get("RunAsGroup"),
            Privileged=json_data.get("Privileged"),
            ReadOnlyRootFilesystem=json_data.get("ReadOnlyRootFilesystem"),
            RunAsNonRoot=json_data.get("RunAsNonRoot"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EksContainerSecurityContext = EksContainerSecurityContext


@dataclass
class EksVolume(BaseModel):
    Name: Optional[str]
    HostPath: Optional["_EksHostPath"]
    EmptyDir: Optional["_EksEmptyDir"]
    Secret: Optional["_EksSecret"]

    @classmethod
    def _deserialize(
        cls: Type["_EksVolume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EksVolume"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            HostPath=EksHostPath._deserialize(json_data.get("HostPath")),
            EmptyDir=EksEmptyDir._deserialize(json_data.get("EmptyDir")),
            Secret=EksSecret._deserialize(json_data.get("Secret")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EksVolume = EksVolume


@dataclass
class EksHostPath(BaseModel):
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EksHostPath"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EksHostPath"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EksHostPath = EksHostPath


@dataclass
class EksEmptyDir(BaseModel):
    Medium: Optional[str]
    SizeLimit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EksEmptyDir"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EksEmptyDir"]:
        if not json_data:
            return None
        return cls(
            Medium=json_data.get("Medium"),
            SizeLimit=json_data.get("SizeLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EksEmptyDir = EksEmptyDir


@dataclass
class EksSecret(BaseModel):
    SecretName: Optional[str]
    Optional: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EksSecret"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EksSecret"]:
        if not json_data:
            return None
        return cls(
            SecretName=json_data.get("SecretName"),
            Optional=json_data.get("Optional"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EksSecret = EksSecret


@dataclass
class EksMetadata(BaseModel):
    Labels: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_EksMetadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EksMetadata"]:
        if not json_data:
            return None
        return cls(
            Labels=json_data.get("Labels"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EksMetadata = EksMetadata


