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
class AwsSagemakerDomain(BaseModel):
    DomainArn: Optional[str]
    Url: Optional[str]
    AppNetworkAccessType: Optional[str]
    AuthMode: Optional[str]
    DefaultUserSettings: Optional["_UserSettings"]
    DefaultSpaceSettings: Optional["_DefaultSpaceSettings"]
    DomainName: Optional[str]
    KmsKeyId: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Tags: Optional[Any]
    VpcId: Optional[str]
    DomainId: Optional[str]
    HomeEfsFileSystemId: Optional[str]
    SingleSignOnManagedApplicationInstanceId: Optional[str]
    DomainSettings: Optional["_DomainSettings"]
    AppSecurityGroupManagement: Optional[str]
    SecurityGroupIdForDomainBoundary: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSagemakerDomain"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSagemakerDomain"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DomainArn=json_data.get("DomainArn"),
            Url=json_data.get("Url"),
            AppNetworkAccessType=json_data.get("AppNetworkAccessType"),
            AuthMode=json_data.get("AuthMode"),
            DefaultUserSettings=UserSettings._deserialize(json_data.get("DefaultUserSettings")),
            DefaultSpaceSettings=DefaultSpaceSettings._deserialize(json_data.get("DefaultSpaceSettings")),
            DomainName=json_data.get("DomainName"),
            KmsKeyId=json_data.get("KmsKeyId"),
            SubnetIds=json_data.get("SubnetIds"),
            Tags=json_data.get("Tags"),
            VpcId=json_data.get("VpcId"),
            DomainId=json_data.get("DomainId"),
            HomeEfsFileSystemId=json_data.get("HomeEfsFileSystemId"),
            SingleSignOnManagedApplicationInstanceId=json_data.get("SingleSignOnManagedApplicationInstanceId"),
            DomainSettings=DomainSettings._deserialize(json_data.get("DomainSettings")),
            AppSecurityGroupManagement=json_data.get("AppSecurityGroupManagement"),
            SecurityGroupIdForDomainBoundary=json_data.get("SecurityGroupIdForDomainBoundary"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSagemakerDomain = AwsSagemakerDomain


@dataclass
class UserSettings(BaseModel):
    ExecutionRole: Optional[str]
    JupyterServerAppSettings: Optional["_JupyterServerAppSettings"]
    KernelGatewayAppSettings: Optional["_KernelGatewayAppSettings"]
    RStudioServerProAppSettings: Optional["_RStudioServerProAppSettings"]
    RSessionAppSettings: Optional["_RSessionAppSettings"]
    SecurityGroups: Optional[Sequence[str]]
    SharingSettings: Optional["_SharingSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_UserSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserSettings"]:
        if not json_data:
            return None
        return cls(
            ExecutionRole=json_data.get("ExecutionRole"),
            JupyterServerAppSettings=JupyterServerAppSettings._deserialize(json_data.get("JupyterServerAppSettings")),
            KernelGatewayAppSettings=KernelGatewayAppSettings._deserialize(json_data.get("KernelGatewayAppSettings")),
            RStudioServerProAppSettings=RStudioServerProAppSettings._deserialize(json_data.get("RStudioServerProAppSettings")),
            RSessionAppSettings=RSessionAppSettings._deserialize(json_data.get("RSessionAppSettings")),
            SecurityGroups=json_data.get("SecurityGroups"),
            SharingSettings=SharingSettings._deserialize(json_data.get("SharingSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserSettings = UserSettings


@dataclass
class JupyterServerAppSettings(BaseModel):
    DefaultResourceSpec: Optional["_ResourceSpec"]

    @classmethod
    def _deserialize(
        cls: Type["_JupyterServerAppSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JupyterServerAppSettings"]:
        if not json_data:
            return None
        return cls(
            DefaultResourceSpec=ResourceSpec._deserialize(json_data.get("DefaultResourceSpec")),
        )


# work around possible type aliasing issues when variable has same name as a model
_JupyterServerAppSettings = JupyterServerAppSettings


@dataclass
class ResourceSpec(BaseModel):
    InstanceType: Optional[str]
    SageMakerImageArn: Optional[str]
    SageMakerImageVersionArn: Optional[str]
    LifecycleConfigArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceSpec"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceSpec"]:
        if not json_data:
            return None
        return cls(
            InstanceType=json_data.get("InstanceType"),
            SageMakerImageArn=json_data.get("SageMakerImageArn"),
            SageMakerImageVersionArn=json_data.get("SageMakerImageVersionArn"),
            LifecycleConfigArn=json_data.get("LifecycleConfigArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceSpec = ResourceSpec


@dataclass
class KernelGatewayAppSettings(BaseModel):
    CustomImages: Optional[Sequence["_CustomImage"]]
    DefaultResourceSpec: Optional["_ResourceSpec"]

    @classmethod
    def _deserialize(
        cls: Type["_KernelGatewayAppSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KernelGatewayAppSettings"]:
        if not json_data:
            return None
        return cls(
            CustomImages=deserialize_list(json_data.get("CustomImages"), CustomImage),
            DefaultResourceSpec=ResourceSpec._deserialize(json_data.get("DefaultResourceSpec")),
        )


# work around possible type aliasing issues when variable has same name as a model
_KernelGatewayAppSettings = KernelGatewayAppSettings


@dataclass
class CustomImage(BaseModel):
    AppImageConfigName: Optional[str]
    ImageName: Optional[str]
    ImageVersionNumber: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_CustomImage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomImage"]:
        if not json_data:
            return None
        return cls(
            AppImageConfigName=json_data.get("AppImageConfigName"),
            ImageName=json_data.get("ImageName"),
            ImageVersionNumber=json_data.get("ImageVersionNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomImage = CustomImage


@dataclass
class RStudioServerProAppSettings(BaseModel):
    AccessStatus: Optional[str]
    UserGroup: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RStudioServerProAppSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RStudioServerProAppSettings"]:
        if not json_data:
            return None
        return cls(
            AccessStatus=json_data.get("AccessStatus"),
            UserGroup=json_data.get("UserGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RStudioServerProAppSettings = RStudioServerProAppSettings


@dataclass
class RSessionAppSettings(BaseModel):
    CustomImages: Optional[Sequence["_CustomImage"]]
    DefaultResourceSpec: Optional["_ResourceSpec"]

    @classmethod
    def _deserialize(
        cls: Type["_RSessionAppSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RSessionAppSettings"]:
        if not json_data:
            return None
        return cls(
            CustomImages=deserialize_list(json_data.get("CustomImages"), CustomImage),
            DefaultResourceSpec=ResourceSpec._deserialize(json_data.get("DefaultResourceSpec")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RSessionAppSettings = RSessionAppSettings


@dataclass
class SharingSettings(BaseModel):
    NotebookOutputOption: Optional[str]
    S3KmsKeyId: Optional[str]
    S3OutputPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SharingSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SharingSettings"]:
        if not json_data:
            return None
        return cls(
            NotebookOutputOption=json_data.get("NotebookOutputOption"),
            S3KmsKeyId=json_data.get("S3KmsKeyId"),
            S3OutputPath=json_data.get("S3OutputPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SharingSettings = SharingSettings


@dataclass
class DefaultSpaceSettings(BaseModel):
    ExecutionRole: Optional[str]
    JupyterServerAppSettings: Optional["_JupyterServerAppSettings"]
    KernelGatewayAppSettings: Optional["_KernelGatewayAppSettings"]
    SecurityGroups: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultSpaceSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultSpaceSettings"]:
        if not json_data:
            return None
        return cls(
            ExecutionRole=json_data.get("ExecutionRole"),
            JupyterServerAppSettings=JupyterServerAppSettings._deserialize(json_data.get("JupyterServerAppSettings")),
            KernelGatewayAppSettings=KernelGatewayAppSettings._deserialize(json_data.get("KernelGatewayAppSettings")),
            SecurityGroups=json_data.get("SecurityGroups"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultSpaceSettings = DefaultSpaceSettings


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
class DomainSettings(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]]
    RStudioServerProDomainSettings: Optional["_RStudioServerProDomainSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_DomainSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainSettings"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            RStudioServerProDomainSettings=RStudioServerProDomainSettings._deserialize(json_data.get("RStudioServerProDomainSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainSettings = DomainSettings


@dataclass
class RStudioServerProDomainSettings(BaseModel):
    DomainExecutionRoleArn: Optional[str]
    RStudioConnectUrl: Optional[str]
    RStudioPackageManagerUrl: Optional[str]
    DefaultResourceSpec: Optional["_ResourceSpec"]

    @classmethod
    def _deserialize(
        cls: Type["_RStudioServerProDomainSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RStudioServerProDomainSettings"]:
        if not json_data:
            return None
        return cls(
            DomainExecutionRoleArn=json_data.get("DomainExecutionRoleArn"),
            RStudioConnectUrl=json_data.get("RStudioConnectUrl"),
            RStudioPackageManagerUrl=json_data.get("RStudioPackageManagerUrl"),
            DefaultResourceSpec=ResourceSpec._deserialize(json_data.get("DefaultResourceSpec")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RStudioServerProDomainSettings = RStudioServerProDomainSettings


