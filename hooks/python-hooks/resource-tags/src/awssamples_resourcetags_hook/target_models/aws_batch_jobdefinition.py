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
    Parameters: Optional[MutableMapping[str, Any]]
    Timeout: Optional["_Timeout"]
    JobDefinitionName: Optional[str]
    PropagateTags: Optional[bool]
    PlatformCapabilities: Optional[Sequence[str]]
    EksProperties: Optional["_EksProperties"]
    Type: Optional[str]
    NodeProperties: Optional["_NodeProperties"]
    SchedulingPriority: Optional[int]
    ContainerProperties: Optional["_ContainerProperties"]
    Id: Optional[str]
    RetryStrategy: Optional["_RetryStrategy"]
    Tags: Optional[Any]

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
            Parameters=json_data.get("Parameters"),
            Timeout=Timeout._deserialize(json_data.get("Timeout")),
            JobDefinitionName=json_data.get("JobDefinitionName"),
            PropagateTags=json_data.get("PropagateTags"),
            PlatformCapabilities=json_data.get("PlatformCapabilities"),
            EksProperties=EksProperties._deserialize(json_data.get("EksProperties")),
            Type=json_data.get("Type"),
            NodeProperties=NodeProperties._deserialize(json_data.get("NodeProperties")),
            SchedulingPriority=json_data.get("SchedulingPriority"),
            ContainerProperties=ContainerProperties._deserialize(json_data.get("ContainerProperties")),
            Id=json_data.get("Id"),
            RetryStrategy=RetryStrategy._deserialize(json_data.get("RetryStrategy")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsBatchJobdefinition = AwsBatchJobdefinition


@dataclass
class Timeout(BaseModel):
    AttemptDurationSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Timeout"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeout"]:
        if not json_data:
            return None
        return cls(
            AttemptDurationSeconds=json_data.get("AttemptDurationSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeout = Timeout


@dataclass
class EksProperties(BaseModel):
    PodProperties: Optional["_PodProperties"]

    @classmethod
    def _deserialize(
        cls: Type["_EksProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EksProperties"]:
        if not json_data:
            return None
        return cls(
            PodProperties=PodProperties._deserialize(json_data.get("PodProperties")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EksProperties = EksProperties


@dataclass
class PodProperties(BaseModel):
    Volumes: Optional[Sequence["_EksVolume"]]
    DnsPolicy: Optional[str]
    Containers: Optional[Sequence["_EksContainer"]]
    Metadata: Optional["_Metadata"]
    ServiceAccountName: Optional[str]
    HostNetwork: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PodProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PodProperties"]:
        if not json_data:
            return None
        return cls(
            Volumes=deserialize_list(json_data.get("Volumes"), EksVolume),
            DnsPolicy=json_data.get("DnsPolicy"),
            Containers=deserialize_list(json_data.get("Containers"), EksContainer),
            Metadata=Metadata._deserialize(json_data.get("Metadata")),
            ServiceAccountName=json_data.get("ServiceAccountName"),
            HostNetwork=json_data.get("HostNetwork"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PodProperties = PodProperties


@dataclass
class EksVolume(BaseModel):
    Secret: Optional["_EksSecret"]
    EmptyDir: Optional["_EksEmptyDir"]
    HostPath: Optional["_EksHostPath"]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EksVolume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EksVolume"]:
        if not json_data:
            return None
        return cls(
            Secret=EksSecret._deserialize(json_data.get("Secret")),
            EmptyDir=EksEmptyDir._deserialize(json_data.get("EmptyDir")),
            HostPath=EksHostPath._deserialize(json_data.get("HostPath")),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EksVolume = EksVolume


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
class EksContainer(BaseModel):
    Args: Optional[Sequence[str]]
    VolumeMounts: Optional[Sequence["_EksContainerVolumeMount"]]
    ImagePullPolicy: Optional[str]
    Command: Optional[Sequence[str]]
    SecurityContext: Optional["_EksContainerSecurityContext"]
    Resources: Optional["_EksContainerResourceRequirements"]
    Image: Optional[str]
    Env: Optional[Sequence["_EksContainerEnvironmentVariable"]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EksContainer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EksContainer"]:
        if not json_data:
            return None
        return cls(
            Args=json_data.get("Args"),
            VolumeMounts=deserialize_list(json_data.get("VolumeMounts"), EksContainerVolumeMount),
            ImagePullPolicy=json_data.get("ImagePullPolicy"),
            Command=json_data.get("Command"),
            SecurityContext=EksContainerSecurityContext._deserialize(json_data.get("SecurityContext")),
            Resources=EksContainerResourceRequirements._deserialize(json_data.get("Resources")),
            Image=json_data.get("Image"),
            Env=deserialize_list(json_data.get("Env"), EksContainerEnvironmentVariable),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EksContainer = EksContainer


@dataclass
class EksContainerVolumeMount(BaseModel):
    MountPath: Optional[str]
    ReadOnly: Optional[bool]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EksContainerVolumeMount"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EksContainerVolumeMount"]:
        if not json_data:
            return None
        return cls(
            MountPath=json_data.get("MountPath"),
            ReadOnly=json_data.get("ReadOnly"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EksContainerVolumeMount = EksContainerVolumeMount


@dataclass
class EksContainerSecurityContext(BaseModel):
    RunAsUser: Optional[int]
    RunAsGroup: Optional[int]
    RunAsNonRoot: Optional[bool]
    Privileged: Optional[bool]
    ReadOnlyRootFilesystem: Optional[bool]

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
            RunAsNonRoot=json_data.get("RunAsNonRoot"),
            Privileged=json_data.get("Privileged"),
            ReadOnlyRootFilesystem=json_data.get("ReadOnlyRootFilesystem"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EksContainerSecurityContext = EksContainerSecurityContext


@dataclass
class EksContainerResourceRequirements(BaseModel):
    Requests: Optional[MutableMapping[str, Any]]
    Limits: Optional[MutableMapping[str, Any]]

    @classmethod
    def _deserialize(
        cls: Type["_EksContainerResourceRequirements"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EksContainerResourceRequirements"]:
        if not json_data:
            return None
        return cls(
            Requests=json_data.get("Requests"),
            Limits=json_data.get("Limits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EksContainerResourceRequirements = EksContainerResourceRequirements


@dataclass
class EksContainerEnvironmentVariable(BaseModel):
    Value: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EksContainerEnvironmentVariable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EksContainerEnvironmentVariable"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EksContainerEnvironmentVariable = EksContainerEnvironmentVariable


@dataclass
class Metadata(BaseModel):
    Labels: Optional[MutableMapping[str, Any]]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            Labels=json_data.get("Labels"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class NodeProperties(BaseModel):
    MainNode: Optional[int]
    NodeRangeProperties: Optional[Sequence["_NodeRangeProperty"]]
    NumNodes: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_NodeProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeProperties"]:
        if not json_data:
            return None
        return cls(
            MainNode=json_data.get("MainNode"),
            NodeRangeProperties=deserialize_list(json_data.get("NodeRangeProperties"), NodeRangeProperty),
            NumNodes=json_data.get("NumNodes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeProperties = NodeProperties


@dataclass
class NodeRangeProperty(BaseModel):
    Container: Optional["_ContainerProperties"]
    TargetNodes: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeRangeProperty"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeRangeProperty"]:
        if not json_data:
            return None
        return cls(
            Container=ContainerProperties._deserialize(json_data.get("Container")),
            TargetNodes=json_data.get("TargetNodes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeRangeProperty = NodeRangeProperty


@dataclass
class ContainerProperties(BaseModel):
    User: Optional[str]
    Secrets: Optional[Sequence["_Secret"]]
    Memory: Optional[int]
    Privileged: Optional[bool]
    LinuxParameters: Optional["_LinuxParameters"]
    FargatePlatformConfiguration: Optional["_FargatePlatformConfiguration"]
    JobRoleArn: Optional[str]
    ReadonlyRootFilesystem: Optional[bool]
    Vcpus: Optional[int]
    Image: Optional[str]
    ResourceRequirements: Optional[Sequence["_ResourceRequirement"]]
    LogConfiguration: Optional["_LogConfiguration"]
    MountPoints: Optional[Sequence["_MountPoints"]]
    ExecutionRoleArn: Optional[str]
    Volumes: Optional[Sequence["_Volumes"]]
    Command: Optional[Sequence[str]]
    Environment: Optional[Sequence["_Environment"]]
    Ulimits: Optional[Sequence["_Ulimit"]]
    NetworkConfiguration: Optional["_NetworkConfiguration"]
    InstanceType: Optional[str]
    EphemeralStorage: Optional["_EphemeralStorage"]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerProperties"]:
        if not json_data:
            return None
        return cls(
            User=json_data.get("User"),
            Secrets=deserialize_list(json_data.get("Secrets"), Secret),
            Memory=json_data.get("Memory"),
            Privileged=json_data.get("Privileged"),
            LinuxParameters=LinuxParameters._deserialize(json_data.get("LinuxParameters")),
            FargatePlatformConfiguration=FargatePlatformConfiguration._deserialize(json_data.get("FargatePlatformConfiguration")),
            JobRoleArn=json_data.get("JobRoleArn"),
            ReadonlyRootFilesystem=json_data.get("ReadonlyRootFilesystem"),
            Vcpus=json_data.get("Vcpus"),
            Image=json_data.get("Image"),
            ResourceRequirements=deserialize_list(json_data.get("ResourceRequirements"), ResourceRequirement),
            LogConfiguration=LogConfiguration._deserialize(json_data.get("LogConfiguration")),
            MountPoints=deserialize_list(json_data.get("MountPoints"), MountPoints),
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            Volumes=deserialize_list(json_data.get("Volumes"), Volumes),
            Command=json_data.get("Command"),
            Environment=deserialize_list(json_data.get("Environment"), Environment),
            Ulimits=deserialize_list(json_data.get("Ulimits"), Ulimit),
            NetworkConfiguration=NetworkConfiguration._deserialize(json_data.get("NetworkConfiguration")),
            InstanceType=json_data.get("InstanceType"),
            EphemeralStorage=EphemeralStorage._deserialize(json_data.get("EphemeralStorage")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerProperties = ContainerProperties


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
class LinuxParameters(BaseModel):
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
class Device(BaseModel):
    Permissions: Optional[Sequence[str]]
    HostPath: Optional[str]
    ContainerPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Device"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Device"]:
        if not json_data:
            return None
        return cls(
            Permissions=json_data.get("Permissions"),
            HostPath=json_data.get("HostPath"),
            ContainerPath=json_data.get("ContainerPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Device = Device


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
class ResourceRequirement(BaseModel):
    Value: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceRequirement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceRequirement"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceRequirement = ResourceRequirement


@dataclass
class LogConfiguration(BaseModel):
    SecretOptions: Optional[Sequence["_Secret"]]
    Options: Optional[MutableMapping[str, Any]]
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
class MountPoints(BaseModel):
    ReadOnly: Optional[bool]
    SourceVolume: Optional[str]
    ContainerPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MountPoints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MountPoints"]:
        if not json_data:
            return None
        return cls(
            ReadOnly=json_data.get("ReadOnly"),
            SourceVolume=json_data.get("SourceVolume"),
            ContainerPath=json_data.get("ContainerPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MountPoints = MountPoints


@dataclass
class Volumes(BaseModel):
    Host: Optional["_VolumesHost"]
    EfsVolumeConfiguration: Optional["_EfsVolumeConfiguration"]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Volumes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Volumes"]:
        if not json_data:
            return None
        return cls(
            Host=VolumesHost._deserialize(json_data.get("Host")),
            EfsVolumeConfiguration=EfsVolumeConfiguration._deserialize(json_data.get("EfsVolumeConfiguration")),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Volumes = Volumes


@dataclass
class VolumesHost(BaseModel):
    SourcePath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VolumesHost"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VolumesHost"]:
        if not json_data:
            return None
        return cls(
            SourcePath=json_data.get("SourcePath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VolumesHost = VolumesHost


@dataclass
class EfsVolumeConfiguration(BaseModel):
    FileSystemId: Optional[str]
    TransitEncryption: Optional[str]
    RootDirectory: Optional[str]
    TransitEncryptionPort: Optional[int]
    AuthorizationConfig: Optional["_AuthorizationConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_EfsVolumeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EfsVolumeConfiguration"]:
        if not json_data:
            return None
        return cls(
            FileSystemId=json_data.get("FileSystemId"),
            TransitEncryption=json_data.get("TransitEncryption"),
            RootDirectory=json_data.get("RootDirectory"),
            TransitEncryptionPort=json_data.get("TransitEncryptionPort"),
            AuthorizationConfig=AuthorizationConfig._deserialize(json_data.get("AuthorizationConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EfsVolumeConfiguration = EfsVolumeConfiguration


@dataclass
class AuthorizationConfig(BaseModel):
    Iam: Optional[str]
    AccessPointId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthorizationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthorizationConfig"]:
        if not json_data:
            return None
        return cls(
            Iam=json_data.get("Iam"),
            AccessPointId=json_data.get("AccessPointId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthorizationConfig = AuthorizationConfig


@dataclass
class Environment(BaseModel):
    Value: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Environment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Environment"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Environment = Environment


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
class RetryStrategy(BaseModel):
    EvaluateOnExit: Optional[Sequence["_EvaluateOnExit"]]
    Attempts: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_RetryStrategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetryStrategy"]:
        if not json_data:
            return None
        return cls(
            EvaluateOnExit=deserialize_list(json_data.get("EvaluateOnExit"), EvaluateOnExit),
            Attempts=json_data.get("Attempts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetryStrategy = RetryStrategy


@dataclass
class EvaluateOnExit(BaseModel):
    Action: Optional[str]
    OnStatusReason: Optional[str]
    OnExitCode: Optional[str]
    OnReason: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EvaluateOnExit"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EvaluateOnExit"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            OnStatusReason=json_data.get("OnStatusReason"),
            OnExitCode=json_data.get("OnExitCode"),
            OnReason=json_data.get("OnReason"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EvaluateOnExit = EvaluateOnExit


