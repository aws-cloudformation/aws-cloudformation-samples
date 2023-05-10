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
class AwsApprunnerService(BaseModel):
    ServiceName: Optional[str]
    ServiceId: Optional[str]
    ServiceArn: Optional[str]
    ServiceUrl: Optional[str]
    Status: Optional[str]
    SourceConfiguration: Optional["_SourceConfiguration"]
    InstanceConfiguration: Optional["_InstanceConfiguration"]
    Tags: Optional[Any]
    EncryptionConfiguration: Optional["_EncryptionConfiguration"]
    HealthCheckConfiguration: Optional["_HealthCheckConfiguration"]
    ObservabilityConfiguration: Optional["_ServiceObservabilityConfiguration"]
    AutoScalingConfigurationArn: Optional[str]
    NetworkConfiguration: Optional["_NetworkConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApprunnerService"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApprunnerService"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ServiceName=json_data.get("ServiceName"),
            ServiceId=json_data.get("ServiceId"),
            ServiceArn=json_data.get("ServiceArn"),
            ServiceUrl=json_data.get("ServiceUrl"),
            Status=json_data.get("Status"),
            SourceConfiguration=SourceConfiguration._deserialize(json_data.get("SourceConfiguration")),
            InstanceConfiguration=InstanceConfiguration._deserialize(json_data.get("InstanceConfiguration")),
            Tags=json_data.get("Tags"),
            EncryptionConfiguration=EncryptionConfiguration._deserialize(json_data.get("EncryptionConfiguration")),
            HealthCheckConfiguration=HealthCheckConfiguration._deserialize(json_data.get("HealthCheckConfiguration")),
            ObservabilityConfiguration=ServiceObservabilityConfiguration._deserialize(json_data.get("ObservabilityConfiguration")),
            AutoScalingConfigurationArn=json_data.get("AutoScalingConfigurationArn"),
            NetworkConfiguration=NetworkConfiguration._deserialize(json_data.get("NetworkConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApprunnerService = AwsApprunnerService


@dataclass
class SourceConfiguration(BaseModel):
    CodeRepository: Optional["_CodeRepository"]
    ImageRepository: Optional["_ImageRepository"]
    AutoDeploymentsEnabled: Optional[bool]
    AuthenticationConfiguration: Optional["_AuthenticationConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_SourceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceConfiguration"]:
        if not json_data:
            return None
        return cls(
            CodeRepository=CodeRepository._deserialize(json_data.get("CodeRepository")),
            ImageRepository=ImageRepository._deserialize(json_data.get("ImageRepository")),
            AutoDeploymentsEnabled=json_data.get("AutoDeploymentsEnabled"),
            AuthenticationConfiguration=AuthenticationConfiguration._deserialize(json_data.get("AuthenticationConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceConfiguration = SourceConfiguration


@dataclass
class CodeRepository(BaseModel):
    RepositoryUrl: Optional[str]
    SourceCodeVersion: Optional["_SourceCodeVersion"]
    CodeConfiguration: Optional["_CodeConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_CodeRepository"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CodeRepository"]:
        if not json_data:
            return None
        return cls(
            RepositoryUrl=json_data.get("RepositoryUrl"),
            SourceCodeVersion=SourceCodeVersion._deserialize(json_data.get("SourceCodeVersion")),
            CodeConfiguration=CodeConfiguration._deserialize(json_data.get("CodeConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CodeRepository = CodeRepository


@dataclass
class SourceCodeVersion(BaseModel):
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceCodeVersion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceCodeVersion"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceCodeVersion = SourceCodeVersion


@dataclass
class CodeConfiguration(BaseModel):
    ConfigurationSource: Optional[str]
    CodeConfigurationValues: Optional["_CodeConfigurationValues"]

    @classmethod
    def _deserialize(
        cls: Type["_CodeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CodeConfiguration"]:
        if not json_data:
            return None
        return cls(
            ConfigurationSource=json_data.get("ConfigurationSource"),
            CodeConfigurationValues=CodeConfigurationValues._deserialize(json_data.get("CodeConfigurationValues")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CodeConfiguration = CodeConfiguration


@dataclass
class CodeConfigurationValues(BaseModel):
    Runtime: Optional[str]
    BuildCommand: Optional[str]
    StartCommand: Optional[str]
    Port: Optional[str]
    RuntimeEnvironmentVariables: Optional[Sequence["_KeyValuePair"]]
    RuntimeEnvironmentSecrets: Optional[Sequence["_KeyValuePair"]]

    @classmethod
    def _deserialize(
        cls: Type["_CodeConfigurationValues"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CodeConfigurationValues"]:
        if not json_data:
            return None
        return cls(
            Runtime=json_data.get("Runtime"),
            BuildCommand=json_data.get("BuildCommand"),
            StartCommand=json_data.get("StartCommand"),
            Port=json_data.get("Port"),
            RuntimeEnvironmentVariables=deserialize_list(json_data.get("RuntimeEnvironmentVariables"), KeyValuePair),
            RuntimeEnvironmentSecrets=deserialize_list(json_data.get("RuntimeEnvironmentSecrets"), KeyValuePair),
        )


# work around possible type aliasing issues when variable has same name as a model
_CodeConfigurationValues = CodeConfigurationValues


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
class ImageRepository(BaseModel):
    ImageIdentifier: Optional[str]
    ImageConfiguration: Optional["_ImageConfiguration"]
    ImageRepositoryType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImageRepository"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageRepository"]:
        if not json_data:
            return None
        return cls(
            ImageIdentifier=json_data.get("ImageIdentifier"),
            ImageConfiguration=ImageConfiguration._deserialize(json_data.get("ImageConfiguration")),
            ImageRepositoryType=json_data.get("ImageRepositoryType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageRepository = ImageRepository


@dataclass
class ImageConfiguration(BaseModel):
    StartCommand: Optional[str]
    Port: Optional[str]
    RuntimeEnvironmentVariables: Optional[Sequence["_KeyValuePair"]]
    RuntimeEnvironmentSecrets: Optional[Sequence["_KeyValuePair"]]

    @classmethod
    def _deserialize(
        cls: Type["_ImageConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageConfiguration"]:
        if not json_data:
            return None
        return cls(
            StartCommand=json_data.get("StartCommand"),
            Port=json_data.get("Port"),
            RuntimeEnvironmentVariables=deserialize_list(json_data.get("RuntimeEnvironmentVariables"), KeyValuePair),
            RuntimeEnvironmentSecrets=deserialize_list(json_data.get("RuntimeEnvironmentSecrets"), KeyValuePair),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageConfiguration = ImageConfiguration


@dataclass
class AuthenticationConfiguration(BaseModel):
    ConnectionArn: Optional[str]
    AccessRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticationConfiguration"]:
        if not json_data:
            return None
        return cls(
            ConnectionArn=json_data.get("ConnectionArn"),
            AccessRoleArn=json_data.get("AccessRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticationConfiguration = AuthenticationConfiguration


@dataclass
class InstanceConfiguration(BaseModel):
    Cpu: Optional[str]
    Memory: Optional[str]
    InstanceRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceConfiguration"]:
        if not json_data:
            return None
        return cls(
            Cpu=json_data.get("Cpu"),
            Memory=json_data.get("Memory"),
            InstanceRoleArn=json_data.get("InstanceRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceConfiguration = InstanceConfiguration


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
class EncryptionConfiguration(BaseModel):
    KmsKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfiguration"]:
        if not json_data:
            return None
        return cls(
            KmsKey=json_data.get("KmsKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfiguration = EncryptionConfiguration


@dataclass
class HealthCheckConfiguration(BaseModel):
    Protocol: Optional[str]
    Path: Optional[str]
    Interval: Optional[int]
    Timeout: Optional[int]
    HealthyThreshold: Optional[int]
    UnhealthyThreshold: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckConfiguration"]:
        if not json_data:
            return None
        return cls(
            Protocol=json_data.get("Protocol"),
            Path=json_data.get("Path"),
            Interval=json_data.get("Interval"),
            Timeout=json_data.get("Timeout"),
            HealthyThreshold=json_data.get("HealthyThreshold"),
            UnhealthyThreshold=json_data.get("UnhealthyThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckConfiguration = HealthCheckConfiguration


@dataclass
class ServiceObservabilityConfiguration(BaseModel):
    ObservabilityEnabled: Optional[bool]
    ObservabilityConfigurationArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceObservabilityConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceObservabilityConfiguration"]:
        if not json_data:
            return None
        return cls(
            ObservabilityEnabled=json_data.get("ObservabilityEnabled"),
            ObservabilityConfigurationArn=json_data.get("ObservabilityConfigurationArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceObservabilityConfiguration = ServiceObservabilityConfiguration


@dataclass
class NetworkConfiguration(BaseModel):
    EgressConfiguration: Optional["_EgressConfiguration"]
    IngressConfiguration: Optional["_IngressConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkConfiguration"]:
        if not json_data:
            return None
        return cls(
            EgressConfiguration=EgressConfiguration._deserialize(json_data.get("EgressConfiguration")),
            IngressConfiguration=IngressConfiguration._deserialize(json_data.get("IngressConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkConfiguration = NetworkConfiguration


@dataclass
class EgressConfiguration(BaseModel):
    EgressType: Optional[str]
    VpcConnectorArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EgressConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EgressConfiguration"]:
        if not json_data:
            return None
        return cls(
            EgressType=json_data.get("EgressType"),
            VpcConnectorArn=json_data.get("VpcConnectorArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EgressConfiguration = EgressConfiguration


@dataclass
class IngressConfiguration(BaseModel):
    IsPubliclyAccessible: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_IngressConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressConfiguration"]:
        if not json_data:
            return None
        return cls(
            IsPubliclyAccessible=json_data.get("IsPubliclyAccessible"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngressConfiguration = IngressConfiguration


