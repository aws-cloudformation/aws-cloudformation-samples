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
class AwsGuarddutyDetector(BaseModel):
    FindingPublishingFrequency: Optional[str]
    Enable: Optional[bool]
    DataSources: Optional["_CFNDataSourceConfigurations"]
    Features: Optional[Sequence["_FeatureConfigurations"]]
    Id: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGuarddutyDetector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGuarddutyDetector"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            FindingPublishingFrequency=json_data.get("FindingPublishingFrequency"),
            Enable=json_data.get("Enable"),
            DataSources=CFNDataSourceConfigurations._deserialize(json_data.get("DataSources")),
            Features=deserialize_list(json_data.get("Features"), FeatureConfigurations),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGuarddutyDetector = AwsGuarddutyDetector


@dataclass
class CFNDataSourceConfigurations(BaseModel):
    MalwareProtection: Optional["_CFNMalwareProtectionConfiguration"]
    S3Logs: Optional["_CFNS3LogsConfiguration"]
    Kubernetes: Optional["_CFNKubernetesConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_CFNDataSourceConfigurations"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CFNDataSourceConfigurations"]:
        if not json_data:
            return None
        return cls(
            MalwareProtection=CFNMalwareProtectionConfiguration._deserialize(json_data.get("MalwareProtection")),
            S3Logs=CFNS3LogsConfiguration._deserialize(json_data.get("S3Logs")),
            Kubernetes=CFNKubernetesConfiguration._deserialize(json_data.get("Kubernetes")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CFNDataSourceConfigurations = CFNDataSourceConfigurations


@dataclass
class CFNMalwareProtectionConfiguration(BaseModel):
    ScanEc2InstanceWithFindings: Optional["_CFNScanEc2InstanceWithFindingsConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_CFNMalwareProtectionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CFNMalwareProtectionConfiguration"]:
        if not json_data:
            return None
        return cls(
            ScanEc2InstanceWithFindings=CFNScanEc2InstanceWithFindingsConfiguration._deserialize(json_data.get("ScanEc2InstanceWithFindings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CFNMalwareProtectionConfiguration = CFNMalwareProtectionConfiguration


@dataclass
class CFNScanEc2InstanceWithFindingsConfiguration(BaseModel):
    EbsVolumes: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CFNScanEc2InstanceWithFindingsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CFNScanEc2InstanceWithFindingsConfiguration"]:
        if not json_data:
            return None
        return cls(
            EbsVolumes=json_data.get("EbsVolumes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CFNScanEc2InstanceWithFindingsConfiguration = CFNScanEc2InstanceWithFindingsConfiguration


@dataclass
class CFNS3LogsConfiguration(BaseModel):
    Enable: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CFNS3LogsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CFNS3LogsConfiguration"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CFNS3LogsConfiguration = CFNS3LogsConfiguration


@dataclass
class CFNKubernetesConfiguration(BaseModel):
    AuditLogs: Optional["_CFNKubernetesAuditLogsConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_CFNKubernetesConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CFNKubernetesConfiguration"]:
        if not json_data:
            return None
        return cls(
            AuditLogs=CFNKubernetesAuditLogsConfiguration._deserialize(json_data.get("AuditLogs")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CFNKubernetesConfiguration = CFNKubernetesConfiguration


@dataclass
class CFNKubernetesAuditLogsConfiguration(BaseModel):
    Enable: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CFNKubernetesAuditLogsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CFNKubernetesAuditLogsConfiguration"]:
        if not json_data:
            return None
        return cls(
            Enable=json_data.get("Enable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CFNKubernetesAuditLogsConfiguration = CFNKubernetesAuditLogsConfiguration


@dataclass
class FeatureConfigurations(BaseModel):
    Status: Optional[str]
    AdditionalConfiguration: Optional[Sequence["_FeatureAdditionalConfiguration"]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FeatureConfigurations"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FeatureConfigurations"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            AdditionalConfiguration=deserialize_list(json_data.get("AdditionalConfiguration"), FeatureAdditionalConfiguration),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FeatureConfigurations = FeatureConfigurations


@dataclass
class FeatureAdditionalConfiguration(BaseModel):
    Status: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FeatureAdditionalConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FeatureAdditionalConfiguration"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FeatureAdditionalConfiguration = FeatureAdditionalConfiguration


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


