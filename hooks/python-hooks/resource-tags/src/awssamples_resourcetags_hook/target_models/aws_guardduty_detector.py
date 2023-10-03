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
    Features: Optional[Sequence["_CFNFeatureConfiguration"]]
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
            Features=deserialize_list(json_data.get("Features"), CFNFeatureConfiguration),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGuarddutyDetector = AwsGuarddutyDetector


@dataclass
class CFNDataSourceConfigurations(BaseModel):
    S3Logs: Optional["_CFNS3LogsConfiguration"]
    Kubernetes: Optional["_CFNKubernetesConfiguration"]
    MalwareProtection: Optional["_CFNMalwareProtectionConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_CFNDataSourceConfigurations"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CFNDataSourceConfigurations"]:
        if not json_data:
            return None
        return cls(
            S3Logs=CFNS3LogsConfiguration._deserialize(json_data.get("S3Logs")),
            Kubernetes=CFNKubernetesConfiguration._deserialize(json_data.get("Kubernetes")),
            MalwareProtection=CFNMalwareProtectionConfiguration._deserialize(json_data.get("MalwareProtection")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CFNDataSourceConfigurations = CFNDataSourceConfigurations


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
class CFNFeatureConfiguration(BaseModel):
    Name: Optional[str]
    Status: Optional[str]
    AdditionalConfiguration: Optional[Sequence["_CFNFeatureAdditionalConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_CFNFeatureConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CFNFeatureConfiguration"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            AdditionalConfiguration=deserialize_list(json_data.get("AdditionalConfiguration"), CFNFeatureAdditionalConfiguration),
        )


# work around possible type aliasing issues when variable has same name as a model
_CFNFeatureConfiguration = CFNFeatureConfiguration


@dataclass
class CFNFeatureAdditionalConfiguration(BaseModel):
    Name: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CFNFeatureAdditionalConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CFNFeatureAdditionalConfiguration"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CFNFeatureAdditionalConfiguration = CFNFeatureAdditionalConfiguration


@dataclass
class TagItem(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagItem"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagItem = TagItem


