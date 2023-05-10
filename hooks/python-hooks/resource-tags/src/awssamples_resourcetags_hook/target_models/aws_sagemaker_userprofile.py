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
class AwsSagemakerUserprofile(BaseModel):
    UserProfileArn: Optional[str]
    DomainId: Optional[str]
    SingleSignOnUserIdentifier: Optional[str]
    SingleSignOnUserValue: Optional[str]
    UserProfileName: Optional[str]
    UserSettings: Optional["_UserSettings"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSagemakerUserprofile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSagemakerUserprofile"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            UserProfileArn=json_data.get("UserProfileArn"),
            DomainId=json_data.get("DomainId"),
            SingleSignOnUserIdentifier=json_data.get("SingleSignOnUserIdentifier"),
            SingleSignOnUserValue=json_data.get("SingleSignOnUserValue"),
            UserProfileName=json_data.get("UserProfileName"),
            UserSettings=UserSettings._deserialize(json_data.get("UserSettings")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSagemakerUserprofile = AwsSagemakerUserprofile


@dataclass
class UserSettings(BaseModel):
    ExecutionRole: Optional[str]
    JupyterServerAppSettings: Optional["_JupyterServerAppSettings"]
    KernelGatewayAppSettings: Optional["_KernelGatewayAppSettings"]
    RStudioServerProAppSettings: Optional["_RStudioServerProAppSettings"]
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


