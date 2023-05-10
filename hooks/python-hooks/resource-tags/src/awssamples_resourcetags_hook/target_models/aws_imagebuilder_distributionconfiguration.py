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
class AwsImagebuilderDistributionconfiguration(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    Description: Optional[str]
    Distributions: Optional[Sequence["_Distribution"]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsImagebuilderDistributionconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsImagebuilderDistributionconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            Distributions=deserialize_list(json_data.get("Distributions"), Distribution),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsImagebuilderDistributionconfiguration = AwsImagebuilderDistributionconfiguration


@dataclass
class Distribution(BaseModel):
    Region: Optional[str]
    AmiDistributionConfiguration: Optional["_AmiDistributionConfiguration"]
    ContainerDistributionConfiguration: Optional["_ContainerDistributionConfiguration"]
    LicenseConfigurationArns: Optional[Sequence[str]]
    LaunchTemplateConfigurations: Optional[Sequence["_LaunchTemplateConfiguration"]]
    FastLaunchConfigurations: Optional[Sequence["_FastLaunchConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_Distribution"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Distribution"]:
        if not json_data:
            return None
        return cls(
            Region=json_data.get("Region"),
            AmiDistributionConfiguration=AmiDistributionConfiguration._deserialize(json_data.get("AmiDistributionConfiguration")),
            ContainerDistributionConfiguration=ContainerDistributionConfiguration._deserialize(json_data.get("ContainerDistributionConfiguration")),
            LicenseConfigurationArns=json_data.get("LicenseConfigurationArns"),
            LaunchTemplateConfigurations=deserialize_list(json_data.get("LaunchTemplateConfigurations"), LaunchTemplateConfiguration),
            FastLaunchConfigurations=deserialize_list(json_data.get("FastLaunchConfigurations"), FastLaunchConfiguration),
        )


# work around possible type aliasing issues when variable has same name as a model
_Distribution = Distribution


@dataclass
class AmiDistributionConfiguration(BaseModel):
    Name: Optional[str]
    KmsKeyId: Optional[str]
    Description: Optional[str]
    AmiTags: Optional[MutableMapping[str, str]]
    TargetAccountIds: Optional[Sequence[str]]
    LaunchPermissionConfiguration: Optional["_LaunchPermissionConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AmiDistributionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AmiDistributionConfiguration"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Description=json_data.get("Description"),
            AmiTags=json_data.get("AmiTags"),
            TargetAccountIds=json_data.get("TargetAccountIds"),
            LaunchPermissionConfiguration=LaunchPermissionConfiguration._deserialize(json_data.get("LaunchPermissionConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AmiDistributionConfiguration = AmiDistributionConfiguration


@dataclass
class LaunchPermissionConfiguration(BaseModel):
    UserIds: Optional[Sequence[str]]
    UserGroups: Optional[Sequence[str]]
    OrganizationArns: Optional[Sequence[str]]
    OrganizationalUnitArns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchPermissionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchPermissionConfiguration"]:
        if not json_data:
            return None
        return cls(
            UserIds=json_data.get("UserIds"),
            UserGroups=json_data.get("UserGroups"),
            OrganizationArns=json_data.get("OrganizationArns"),
            OrganizationalUnitArns=json_data.get("OrganizationalUnitArns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchPermissionConfiguration = LaunchPermissionConfiguration


@dataclass
class ContainerDistributionConfiguration(BaseModel):
    Description: Optional[str]
    ContainerTags: Optional[Sequence[str]]
    TargetRepository: Optional["_TargetContainerRepository"]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerDistributionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerDistributionConfiguration"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            ContainerTags=json_data.get("ContainerTags"),
            TargetRepository=TargetContainerRepository._deserialize(json_data.get("TargetRepository")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerDistributionConfiguration = ContainerDistributionConfiguration


@dataclass
class TargetContainerRepository(BaseModel):
    Service: Optional[str]
    RepositoryName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetContainerRepository"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetContainerRepository"]:
        if not json_data:
            return None
        return cls(
            Service=json_data.get("Service"),
            RepositoryName=json_data.get("RepositoryName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetContainerRepository = TargetContainerRepository


@dataclass
class LaunchTemplateConfiguration(BaseModel):
    LaunchTemplateId: Optional[str]
    AccountId: Optional[str]
    SetDefaultVersion: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_LaunchTemplateConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LaunchTemplateConfiguration"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateId=json_data.get("LaunchTemplateId"),
            AccountId=json_data.get("AccountId"),
            SetDefaultVersion=json_data.get("SetDefaultVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LaunchTemplateConfiguration = LaunchTemplateConfiguration


@dataclass
class FastLaunchConfiguration(BaseModel):
    AccountId: Optional[str]
    Enabled: Optional[bool]
    LaunchTemplate: Optional["_FastLaunchLaunchTemplateSpecification"]
    MaxParallelLaunches: Optional[int]
    SnapshotConfiguration: Optional["_FastLaunchSnapshotConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_FastLaunchConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FastLaunchConfiguration"]:
        if not json_data:
            return None
        return cls(
            AccountId=json_data.get("AccountId"),
            Enabled=json_data.get("Enabled"),
            LaunchTemplate=FastLaunchLaunchTemplateSpecification._deserialize(json_data.get("LaunchTemplate")),
            MaxParallelLaunches=json_data.get("MaxParallelLaunches"),
            SnapshotConfiguration=FastLaunchSnapshotConfiguration._deserialize(json_data.get("SnapshotConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FastLaunchConfiguration = FastLaunchConfiguration


@dataclass
class FastLaunchLaunchTemplateSpecification(BaseModel):
    LaunchTemplateId: Optional[str]
    LaunchTemplateName: Optional[str]
    LaunchTemplateVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FastLaunchLaunchTemplateSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FastLaunchLaunchTemplateSpecification"]:
        if not json_data:
            return None
        return cls(
            LaunchTemplateId=json_data.get("LaunchTemplateId"),
            LaunchTemplateName=json_data.get("LaunchTemplateName"),
            LaunchTemplateVersion=json_data.get("LaunchTemplateVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FastLaunchLaunchTemplateSpecification = FastLaunchLaunchTemplateSpecification


@dataclass
class FastLaunchSnapshotConfiguration(BaseModel):
    TargetResourceCount: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_FastLaunchSnapshotConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FastLaunchSnapshotConfiguration"]:
        if not json_data:
            return None
        return cls(
            TargetResourceCount=json_data.get("TargetResourceCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FastLaunchSnapshotConfiguration = FastLaunchSnapshotConfiguration


