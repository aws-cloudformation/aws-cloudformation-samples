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
class AwsGreengrassResourcedefinition(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]
    LatestVersionArn: Optional[str]
    Tags: Optional[Any]
    Name: Optional[str]
    InitialVersion: Optional["_ResourceDefinitionVersion"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGreengrassResourcedefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGreengrassResourcedefinition"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            LatestVersionArn=json_data.get("LatestVersionArn"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
            InitialVersion=ResourceDefinitionVersion._deserialize(json_data.get("InitialVersion")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGreengrassResourcedefinition = AwsGreengrassResourcedefinition


@dataclass
class ResourceDefinitionVersion(BaseModel):
    Resources: Optional[Sequence["_ResourceInstance"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceDefinitionVersion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceDefinitionVersion"]:
        if not json_data:
            return None
        return cls(
            Resources=deserialize_list(json_data.get("Resources"), ResourceInstance),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceDefinitionVersion = ResourceDefinitionVersion


@dataclass
class ResourceInstance(BaseModel):
    ResourceDataContainer: Optional["_ResourceDataContainer"]
    Id: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceInstance"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceInstance"]:
        if not json_data:
            return None
        return cls(
            ResourceDataContainer=ResourceDataContainer._deserialize(json_data.get("ResourceDataContainer")),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceInstance = ResourceInstance


@dataclass
class ResourceDataContainer(BaseModel):
    LocalVolumeResourceData: Optional["_LocalVolumeResourceData"]
    LocalDeviceResourceData: Optional["_LocalDeviceResourceData"]
    S3MachineLearningModelResourceData: Optional["_S3MachineLearningModelResourceData"]
    SecretsManagerSecretResourceData: Optional["_SecretsManagerSecretResourceData"]
    SageMakerMachineLearningModelResourceData: Optional["_SageMakerMachineLearningModelResourceData"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceDataContainer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceDataContainer"]:
        if not json_data:
            return None
        return cls(
            LocalVolumeResourceData=LocalVolumeResourceData._deserialize(json_data.get("LocalVolumeResourceData")),
            LocalDeviceResourceData=LocalDeviceResourceData._deserialize(json_data.get("LocalDeviceResourceData")),
            S3MachineLearningModelResourceData=S3MachineLearningModelResourceData._deserialize(json_data.get("S3MachineLearningModelResourceData")),
            SecretsManagerSecretResourceData=SecretsManagerSecretResourceData._deserialize(json_data.get("SecretsManagerSecretResourceData")),
            SageMakerMachineLearningModelResourceData=SageMakerMachineLearningModelResourceData._deserialize(json_data.get("SageMakerMachineLearningModelResourceData")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceDataContainer = ResourceDataContainer


@dataclass
class LocalVolumeResourceData(BaseModel):
    SourcePath: Optional[str]
    DestinationPath: Optional[str]
    GroupOwnerSetting: Optional["_GroupOwnerSetting"]

    @classmethod
    def _deserialize(
        cls: Type["_LocalVolumeResourceData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalVolumeResourceData"]:
        if not json_data:
            return None
        return cls(
            SourcePath=json_data.get("SourcePath"),
            DestinationPath=json_data.get("DestinationPath"),
            GroupOwnerSetting=GroupOwnerSetting._deserialize(json_data.get("GroupOwnerSetting")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalVolumeResourceData = LocalVolumeResourceData


@dataclass
class GroupOwnerSetting(BaseModel):
    AutoAddGroupOwner: Optional[bool]
    GroupOwner: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GroupOwnerSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupOwnerSetting"]:
        if not json_data:
            return None
        return cls(
            AutoAddGroupOwner=json_data.get("AutoAddGroupOwner"),
            GroupOwner=json_data.get("GroupOwner"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupOwnerSetting = GroupOwnerSetting


@dataclass
class LocalDeviceResourceData(BaseModel):
    SourcePath: Optional[str]
    GroupOwnerSetting: Optional["_GroupOwnerSetting"]

    @classmethod
    def _deserialize(
        cls: Type["_LocalDeviceResourceData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalDeviceResourceData"]:
        if not json_data:
            return None
        return cls(
            SourcePath=json_data.get("SourcePath"),
            GroupOwnerSetting=GroupOwnerSetting._deserialize(json_data.get("GroupOwnerSetting")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalDeviceResourceData = LocalDeviceResourceData


@dataclass
class S3MachineLearningModelResourceData(BaseModel):
    OwnerSetting: Optional["_ResourceDownloadOwnerSetting"]
    DestinationPath: Optional[str]
    S3Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3MachineLearningModelResourceData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3MachineLearningModelResourceData"]:
        if not json_data:
            return None
        return cls(
            OwnerSetting=ResourceDownloadOwnerSetting._deserialize(json_data.get("OwnerSetting")),
            DestinationPath=json_data.get("DestinationPath"),
            S3Uri=json_data.get("S3Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3MachineLearningModelResourceData = S3MachineLearningModelResourceData


@dataclass
class ResourceDownloadOwnerSetting(BaseModel):
    GroupPermission: Optional[str]
    GroupOwner: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceDownloadOwnerSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceDownloadOwnerSetting"]:
        if not json_data:
            return None
        return cls(
            GroupPermission=json_data.get("GroupPermission"),
            GroupOwner=json_data.get("GroupOwner"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceDownloadOwnerSetting = ResourceDownloadOwnerSetting


@dataclass
class SecretsManagerSecretResourceData(BaseModel):
    ARN: Optional[str]
    AdditionalStagingLabelsToDownload: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SecretsManagerSecretResourceData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecretsManagerSecretResourceData"]:
        if not json_data:
            return None
        return cls(
            ARN=json_data.get("ARN"),
            AdditionalStagingLabelsToDownload=json_data.get("AdditionalStagingLabelsToDownload"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecretsManagerSecretResourceData = SecretsManagerSecretResourceData


@dataclass
class SageMakerMachineLearningModelResourceData(BaseModel):
    OwnerSetting: Optional["_ResourceDownloadOwnerSetting"]
    SageMakerJobArn: Optional[str]
    DestinationPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SageMakerMachineLearningModelResourceData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SageMakerMachineLearningModelResourceData"]:
        if not json_data:
            return None
        return cls(
            OwnerSetting=ResourceDownloadOwnerSetting._deserialize(json_data.get("OwnerSetting")),
            SageMakerJobArn=json_data.get("SageMakerJobArn"),
            DestinationPath=json_data.get("DestinationPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SageMakerMachineLearningModelResourceData = SageMakerMachineLearningModelResourceData


