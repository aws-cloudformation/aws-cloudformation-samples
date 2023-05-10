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
class AwsCodebuildProject(BaseModel):
    Description: Optional[str]
    ResourceAccessRole: Optional[str]
    VpcConfig: Optional["_VpcConfig"]
    SecondarySources: Optional[Sequence["_Source"]]
    EncryptionKey: Optional[str]
    SecondaryArtifacts: Optional[Sequence["_Artifacts"]]
    Source: Optional["_Source"]
    Name: Optional[str]
    LogsConfig: Optional["_LogsConfig"]
    ServiceRole: Optional[str]
    QueuedTimeoutInMinutes: Optional[int]
    SecondarySourceVersions: Optional[Sequence["_ProjectSourceVersion"]]
    Tags: Optional[Any]
    SourceVersion: Optional[str]
    Triggers: Optional["_ProjectTriggers"]
    Artifacts: Optional["_Artifacts"]
    BadgeEnabled: Optional[bool]
    FileSystemLocations: Optional[Sequence["_ProjectFileSystemLocation"]]
    Environment: Optional["_Environment"]
    ConcurrentBuildLimit: Optional[int]
    Visibility: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    BuildBatchConfig: Optional["_ProjectBuildBatchConfig"]
    TimeoutInMinutes: Optional[int]
    Cache: Optional["_ProjectCache"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCodebuildProject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCodebuildProject"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            ResourceAccessRole=json_data.get("ResourceAccessRole"),
            VpcConfig=VpcConfig._deserialize(json_data.get("VpcConfig")),
            SecondarySources=deserialize_list(json_data.get("SecondarySources"), Source),
            EncryptionKey=json_data.get("EncryptionKey"),
            SecondaryArtifacts=deserialize_list(json_data.get("SecondaryArtifacts"), Artifacts),
            Source=Source._deserialize(json_data.get("Source")),
            Name=json_data.get("Name"),
            LogsConfig=LogsConfig._deserialize(json_data.get("LogsConfig")),
            ServiceRole=json_data.get("ServiceRole"),
            QueuedTimeoutInMinutes=json_data.get("QueuedTimeoutInMinutes"),
            SecondarySourceVersions=deserialize_list(json_data.get("SecondarySourceVersions"), ProjectSourceVersion),
            Tags=json_data.get("Tags"),
            SourceVersion=json_data.get("SourceVersion"),
            Triggers=ProjectTriggers._deserialize(json_data.get("Triggers")),
            Artifacts=Artifacts._deserialize(json_data.get("Artifacts")),
            BadgeEnabled=json_data.get("BadgeEnabled"),
            FileSystemLocations=deserialize_list(json_data.get("FileSystemLocations"), ProjectFileSystemLocation),
            Environment=Environment._deserialize(json_data.get("Environment")),
            ConcurrentBuildLimit=json_data.get("ConcurrentBuildLimit"),
            Visibility=json_data.get("Visibility"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            BuildBatchConfig=ProjectBuildBatchConfig._deserialize(json_data.get("BuildBatchConfig")),
            TimeoutInMinutes=json_data.get("TimeoutInMinutes"),
            Cache=ProjectCache._deserialize(json_data.get("Cache")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCodebuildProject = AwsCodebuildProject


@dataclass
class VpcConfig(BaseModel):
    Subnets: Optional[Sequence[str]]
    VpcId: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfig"]:
        if not json_data:
            return None
        return cls(
            Subnets=json_data.get("Subnets"),
            VpcId=json_data.get("VpcId"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfig = VpcConfig


@dataclass
class Source(BaseModel):
    Type: Optional[str]
    ReportBuildStatus: Optional[bool]
    Auth: Optional["_SourceAuth"]
    SourceIdentifier: Optional[str]
    BuildSpec: Optional[str]
    GitCloneDepth: Optional[int]
    BuildStatusConfig: Optional["_BuildStatusConfig"]
    GitSubmodulesConfig: Optional["_GitSubmodulesConfig"]
    InsecureSsl: Optional[bool]
    Location: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Source"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Source"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            ReportBuildStatus=json_data.get("ReportBuildStatus"),
            Auth=SourceAuth._deserialize(json_data.get("Auth")),
            SourceIdentifier=json_data.get("SourceIdentifier"),
            BuildSpec=json_data.get("BuildSpec"),
            GitCloneDepth=json_data.get("GitCloneDepth"),
            BuildStatusConfig=BuildStatusConfig._deserialize(json_data.get("BuildStatusConfig")),
            GitSubmodulesConfig=GitSubmodulesConfig._deserialize(json_data.get("GitSubmodulesConfig")),
            InsecureSsl=json_data.get("InsecureSsl"),
            Location=json_data.get("Location"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Source = Source


@dataclass
class SourceAuth(BaseModel):
    Resource: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceAuth"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceAuth"]:
        if not json_data:
            return None
        return cls(
            Resource=json_data.get("Resource"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceAuth = SourceAuth


@dataclass
class BuildStatusConfig(BaseModel):
    Context: Optional[str]
    TargetUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BuildStatusConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BuildStatusConfig"]:
        if not json_data:
            return None
        return cls(
            Context=json_data.get("Context"),
            TargetUrl=json_data.get("TargetUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BuildStatusConfig = BuildStatusConfig


@dataclass
class GitSubmodulesConfig(BaseModel):
    FetchSubmodules: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GitSubmodulesConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GitSubmodulesConfig"]:
        if not json_data:
            return None
        return cls(
            FetchSubmodules=json_data.get("FetchSubmodules"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GitSubmodulesConfig = GitSubmodulesConfig


@dataclass
class Artifacts(BaseModel):
    Path: Optional[str]
    Type: Optional[str]
    ArtifactIdentifier: Optional[str]
    OverrideArtifactName: Optional[bool]
    Packaging: Optional[str]
    EncryptionDisabled: Optional[bool]
    Location: Optional[str]
    Name: Optional[str]
    NamespaceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Artifacts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Artifacts"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Type=json_data.get("Type"),
            ArtifactIdentifier=json_data.get("ArtifactIdentifier"),
            OverrideArtifactName=json_data.get("OverrideArtifactName"),
            Packaging=json_data.get("Packaging"),
            EncryptionDisabled=json_data.get("EncryptionDisabled"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            NamespaceType=json_data.get("NamespaceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Artifacts = Artifacts


@dataclass
class LogsConfig(BaseModel):
    CloudWatchLogs: Optional["_CloudWatchLogsConfig"]
    S3Logs: Optional["_S3LogsConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_LogsConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogsConfig"]:
        if not json_data:
            return None
        return cls(
            CloudWatchLogs=CloudWatchLogsConfig._deserialize(json_data.get("CloudWatchLogs")),
            S3Logs=S3LogsConfig._deserialize(json_data.get("S3Logs")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogsConfig = LogsConfig


@dataclass
class CloudWatchLogsConfig(BaseModel):
    Status: Optional[str]
    GroupName: Optional[str]
    StreamName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudWatchLogsConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudWatchLogsConfig"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            GroupName=json_data.get("GroupName"),
            StreamName=json_data.get("StreamName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudWatchLogsConfig = CloudWatchLogsConfig


@dataclass
class S3LogsConfig(BaseModel):
    Status: Optional[str]
    EncryptionDisabled: Optional[bool]
    Location: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3LogsConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3LogsConfig"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            EncryptionDisabled=json_data.get("EncryptionDisabled"),
            Location=json_data.get("Location"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3LogsConfig = S3LogsConfig


@dataclass
class ProjectSourceVersion(BaseModel):
    SourceIdentifier: Optional[str]
    SourceVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectSourceVersion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectSourceVersion"]:
        if not json_data:
            return None
        return cls(
            SourceIdentifier=json_data.get("SourceIdentifier"),
            SourceVersion=json_data.get("SourceVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectSourceVersion = ProjectSourceVersion


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


@dataclass
class ProjectTriggers(BaseModel):
    BuildType: Optional[str]
    FilterGroups: Optional[Sequence[MutableMapping[str, Any]]]
    Webhook: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectTriggers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectTriggers"]:
        if not json_data:
            return None
        return cls(
            BuildType=json_data.get("BuildType"),
            FilterGroups=json_data.get("FilterGroups"),
            Webhook=json_data.get("Webhook"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectTriggers = ProjectTriggers


@dataclass
class ProjectFileSystemLocation(BaseModel):
    MountPoint: Optional[str]
    Type: Optional[str]
    Identifier: Optional[str]
    MountOptions: Optional[str]
    Location: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectFileSystemLocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectFileSystemLocation"]:
        if not json_data:
            return None
        return cls(
            MountPoint=json_data.get("MountPoint"),
            Type=json_data.get("Type"),
            Identifier=json_data.get("Identifier"),
            MountOptions=json_data.get("MountOptions"),
            Location=json_data.get("Location"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectFileSystemLocation = ProjectFileSystemLocation


@dataclass
class Environment(BaseModel):
    Type: Optional[str]
    EnvironmentVariables: Optional[Sequence["_EnvironmentVariable"]]
    PrivilegedMode: Optional[bool]
    ImagePullCredentialsType: Optional[str]
    Image: Optional[str]
    RegistryCredential: Optional["_RegistryCredential"]
    ComputeType: Optional[str]
    Certificate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Environment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Environment"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            EnvironmentVariables=deserialize_list(json_data.get("EnvironmentVariables"), EnvironmentVariable),
            PrivilegedMode=json_data.get("PrivilegedMode"),
            ImagePullCredentialsType=json_data.get("ImagePullCredentialsType"),
            Image=json_data.get("Image"),
            RegistryCredential=RegistryCredential._deserialize(json_data.get("RegistryCredential")),
            ComputeType=json_data.get("ComputeType"),
            Certificate=json_data.get("Certificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Environment = Environment


@dataclass
class EnvironmentVariable(BaseModel):
    Value: Optional[str]
    Type: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentVariable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentVariable"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Type=json_data.get("Type"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentVariable = EnvironmentVariable


@dataclass
class RegistryCredential(BaseModel):
    Credential: Optional[str]
    CredentialProvider: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RegistryCredential"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RegistryCredential"]:
        if not json_data:
            return None
        return cls(
            Credential=json_data.get("Credential"),
            CredentialProvider=json_data.get("CredentialProvider"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RegistryCredential = RegistryCredential


@dataclass
class ProjectBuildBatchConfig(BaseModel):
    CombineArtifacts: Optional[bool]
    ServiceRole: Optional[str]
    BatchReportMode: Optional[str]
    TimeoutInMins: Optional[int]
    Restrictions: Optional["_BatchRestrictions"]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectBuildBatchConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectBuildBatchConfig"]:
        if not json_data:
            return None
        return cls(
            CombineArtifacts=json_data.get("CombineArtifacts"),
            ServiceRole=json_data.get("ServiceRole"),
            BatchReportMode=json_data.get("BatchReportMode"),
            TimeoutInMins=json_data.get("TimeoutInMins"),
            Restrictions=BatchRestrictions._deserialize(json_data.get("Restrictions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectBuildBatchConfig = ProjectBuildBatchConfig


@dataclass
class BatchRestrictions(BaseModel):
    ComputeTypesAllowed: Optional[Sequence[str]]
    MaximumBuildsAllowed: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_BatchRestrictions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BatchRestrictions"]:
        if not json_data:
            return None
        return cls(
            ComputeTypesAllowed=json_data.get("ComputeTypesAllowed"),
            MaximumBuildsAllowed=json_data.get("MaximumBuildsAllowed"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BatchRestrictions = BatchRestrictions


@dataclass
class ProjectCache(BaseModel):
    Modes: Optional[Sequence[str]]
    Type: Optional[str]
    Location: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectCache"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectCache"]:
        if not json_data:
            return None
        return cls(
            Modes=json_data.get("Modes"),
            Type=json_data.get("Type"),
            Location=json_data.get("Location"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectCache = ProjectCache


