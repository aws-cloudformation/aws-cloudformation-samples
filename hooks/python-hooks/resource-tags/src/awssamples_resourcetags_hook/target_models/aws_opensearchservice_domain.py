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
class AwsOpensearchserviceDomain(BaseModel):
    ClusterConfig: Optional["_ClusterConfig"]
    DomainName: Optional[str]
    AccessPolicies: Optional[MutableMapping[str, Any]]
    EngineVersion: Optional[str]
    AdvancedOptions: Optional[MutableMapping[str, str]]
    LogPublishingOptions: Optional[MutableMapping[str, "_LogPublishingOption"]]
    SnapshotOptions: Optional["_SnapshotOptions"]
    VPCOptions: Optional["_VPCOptions"]
    NodeToNodeEncryptionOptions: Optional["_NodeToNodeEncryptionOptions"]
    DomainEndpointOptions: Optional["_DomainEndpointOptions"]
    CognitoOptions: Optional["_CognitoOptions"]
    AdvancedSecurityOptions: Optional["_AdvancedSecurityOptionsInput"]
    DomainEndpoint: Optional[str]
    DomainEndpoints: Optional[MutableMapping[str, str]]
    EBSOptions: Optional["_EBSOptions"]
    Id: Optional[str]
    Arn: Optional[str]
    DomainArn: Optional[str]
    EncryptionAtRestOptions: Optional["_EncryptionAtRestOptions"]
    Tags: Optional[Any]
    ServiceSoftwareOptions: Optional["_ServiceSoftwareOptions"]
    OffPeakWindowOptions: Optional["_OffPeakWindowOptions"]
    SoftwareUpdateOptions: Optional["_SoftwareUpdateOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsOpensearchserviceDomain"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsOpensearchserviceDomain"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ClusterConfig=ClusterConfig._deserialize(json_data.get("ClusterConfig")),
            DomainName=json_data.get("DomainName"),
            AccessPolicies=json_data.get("AccessPolicies"),
            EngineVersion=json_data.get("EngineVersion"),
            AdvancedOptions=json_data.get("AdvancedOptions"),
            LogPublishingOptions=json_data.get("LogPublishingOptions"),
            SnapshotOptions=SnapshotOptions._deserialize(json_data.get("SnapshotOptions")),
            VPCOptions=VPCOptions._deserialize(json_data.get("VPCOptions")),
            NodeToNodeEncryptionOptions=NodeToNodeEncryptionOptions._deserialize(json_data.get("NodeToNodeEncryptionOptions")),
            DomainEndpointOptions=DomainEndpointOptions._deserialize(json_data.get("DomainEndpointOptions")),
            CognitoOptions=CognitoOptions._deserialize(json_data.get("CognitoOptions")),
            AdvancedSecurityOptions=AdvancedSecurityOptionsInput._deserialize(json_data.get("AdvancedSecurityOptions")),
            DomainEndpoint=json_data.get("DomainEndpoint"),
            DomainEndpoints=json_data.get("DomainEndpoints"),
            EBSOptions=EBSOptions._deserialize(json_data.get("EBSOptions")),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            DomainArn=json_data.get("DomainArn"),
            EncryptionAtRestOptions=EncryptionAtRestOptions._deserialize(json_data.get("EncryptionAtRestOptions")),
            Tags=json_data.get("Tags"),
            ServiceSoftwareOptions=ServiceSoftwareOptions._deserialize(json_data.get("ServiceSoftwareOptions")),
            OffPeakWindowOptions=OffPeakWindowOptions._deserialize(json_data.get("OffPeakWindowOptions")),
            SoftwareUpdateOptions=SoftwareUpdateOptions._deserialize(json_data.get("SoftwareUpdateOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsOpensearchserviceDomain = AwsOpensearchserviceDomain


@dataclass
class ClusterConfig(BaseModel):
    InstanceCount: Optional[int]
    WarmEnabled: Optional[bool]
    WarmCount: Optional[int]
    DedicatedMasterEnabled: Optional[bool]
    ZoneAwarenessConfig: Optional["_ZoneAwarenessConfig"]
    DedicatedMasterCount: Optional[int]
    InstanceType: Optional[str]
    WarmType: Optional[str]
    ZoneAwarenessEnabled: Optional[bool]
    DedicatedMasterType: Optional[str]
    MultiAZWithStandbyEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterConfig"]:
        if not json_data:
            return None
        return cls(
            InstanceCount=json_data.get("InstanceCount"),
            WarmEnabled=json_data.get("WarmEnabled"),
            WarmCount=json_data.get("WarmCount"),
            DedicatedMasterEnabled=json_data.get("DedicatedMasterEnabled"),
            ZoneAwarenessConfig=ZoneAwarenessConfig._deserialize(json_data.get("ZoneAwarenessConfig")),
            DedicatedMasterCount=json_data.get("DedicatedMasterCount"),
            InstanceType=json_data.get("InstanceType"),
            WarmType=json_data.get("WarmType"),
            ZoneAwarenessEnabled=json_data.get("ZoneAwarenessEnabled"),
            DedicatedMasterType=json_data.get("DedicatedMasterType"),
            MultiAZWithStandbyEnabled=json_data.get("MultiAZWithStandbyEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterConfig = ClusterConfig


@dataclass
class ZoneAwarenessConfig(BaseModel):
    AvailabilityZoneCount: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ZoneAwarenessConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZoneAwarenessConfig"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZoneCount=json_data.get("AvailabilityZoneCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZoneAwarenessConfig = ZoneAwarenessConfig


@dataclass
class LogPublishingOption(BaseModel):
    CloudWatchLogsLogGroupArn: Optional[str]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_LogPublishingOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogPublishingOption"]:
        if not json_data:
            return None
        return cls(
            CloudWatchLogsLogGroupArn=json_data.get("CloudWatchLogsLogGroupArn"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogPublishingOption = LogPublishingOption


@dataclass
class SnapshotOptions(BaseModel):
    AutomatedSnapshotStartHour: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotOptions"]:
        if not json_data:
            return None
        return cls(
            AutomatedSnapshotStartHour=json_data.get("AutomatedSnapshotStartHour"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotOptions = SnapshotOptions


@dataclass
class VPCOptions(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VPCOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VPCOptions"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VPCOptions = VPCOptions


@dataclass
class NodeToNodeEncryptionOptions(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NodeToNodeEncryptionOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeToNodeEncryptionOptions"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeToNodeEncryptionOptions = NodeToNodeEncryptionOptions


@dataclass
class DomainEndpointOptions(BaseModel):
    CustomEndpointCertificateArn: Optional[str]
    CustomEndpointEnabled: Optional[bool]
    EnforceHTTPS: Optional[bool]
    CustomEndpoint: Optional[str]
    TLSSecurityPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DomainEndpointOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainEndpointOptions"]:
        if not json_data:
            return None
        return cls(
            CustomEndpointCertificateArn=json_data.get("CustomEndpointCertificateArn"),
            CustomEndpointEnabled=json_data.get("CustomEndpointEnabled"),
            EnforceHTTPS=json_data.get("EnforceHTTPS"),
            CustomEndpoint=json_data.get("CustomEndpoint"),
            TLSSecurityPolicy=json_data.get("TLSSecurityPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainEndpointOptions = DomainEndpointOptions


@dataclass
class CognitoOptions(BaseModel):
    Enabled: Optional[bool]
    IdentityPoolId: Optional[str]
    UserPoolId: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CognitoOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CognitoOptions"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            IdentityPoolId=json_data.get("IdentityPoolId"),
            UserPoolId=json_data.get("UserPoolId"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CognitoOptions = CognitoOptions


@dataclass
class AdvancedSecurityOptionsInput(BaseModel):
    Enabled: Optional[bool]
    MasterUserOptions: Optional["_MasterUserOptions"]
    InternalUserDatabaseEnabled: Optional[bool]
    AnonymousAuthEnabled: Optional[bool]
    SAMLOptions: Optional["_SAMLOptions"]
    AnonymousAuthDisableDate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedSecurityOptionsInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedSecurityOptionsInput"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            MasterUserOptions=MasterUserOptions._deserialize(json_data.get("MasterUserOptions")),
            InternalUserDatabaseEnabled=json_data.get("InternalUserDatabaseEnabled"),
            AnonymousAuthEnabled=json_data.get("AnonymousAuthEnabled"),
            SAMLOptions=SAMLOptions._deserialize(json_data.get("SAMLOptions")),
            AnonymousAuthDisableDate=json_data.get("AnonymousAuthDisableDate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedSecurityOptionsInput = AdvancedSecurityOptionsInput


@dataclass
class MasterUserOptions(BaseModel):
    MasterUserPassword: Optional[str]
    MasterUserName: Optional[str]
    MasterUserARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MasterUserOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MasterUserOptions"]:
        if not json_data:
            return None
        return cls(
            MasterUserPassword=json_data.get("MasterUserPassword"),
            MasterUserName=json_data.get("MasterUserName"),
            MasterUserARN=json_data.get("MasterUserARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MasterUserOptions = MasterUserOptions


@dataclass
class SAMLOptions(BaseModel):
    Enabled: Optional[bool]
    Idp: Optional["_Idp"]
    MasterUserName: Optional[str]
    MasterBackendRole: Optional[str]
    SubjectKey: Optional[str]
    RolesKey: Optional[str]
    SessionTimeoutMinutes: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_SAMLOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SAMLOptions"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Idp=Idp._deserialize(json_data.get("Idp")),
            MasterUserName=json_data.get("MasterUserName"),
            MasterBackendRole=json_data.get("MasterBackendRole"),
            SubjectKey=json_data.get("SubjectKey"),
            RolesKey=json_data.get("RolesKey"),
            SessionTimeoutMinutes=json_data.get("SessionTimeoutMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SAMLOptions = SAMLOptions


@dataclass
class Idp(BaseModel):
    MetadataContent: Optional[str]
    EntityId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Idp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Idp"]:
        if not json_data:
            return None
        return cls(
            MetadataContent=json_data.get("MetadataContent"),
            EntityId=json_data.get("EntityId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Idp = Idp


@dataclass
class EBSOptions(BaseModel):
    EBSEnabled: Optional[bool]
    VolumeType: Optional[str]
    Iops: Optional[int]
    VolumeSize: Optional[int]
    Throughput: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_EBSOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EBSOptions"]:
        if not json_data:
            return None
        return cls(
            EBSEnabled=json_data.get("EBSEnabled"),
            VolumeType=json_data.get("VolumeType"),
            Iops=json_data.get("Iops"),
            VolumeSize=json_data.get("VolumeSize"),
            Throughput=json_data.get("Throughput"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EBSOptions = EBSOptions


@dataclass
class EncryptionAtRestOptions(BaseModel):
    KmsKeyId: Optional[str]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionAtRestOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionAtRestOptions"]:
        if not json_data:
            return None
        return cls(
            KmsKeyId=json_data.get("KmsKeyId"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionAtRestOptions = EncryptionAtRestOptions


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
class ServiceSoftwareOptions(BaseModel):
    CurrentVersion: Optional[str]
    NewVersion: Optional[str]
    UpdateAvailable: Optional[bool]
    Cancellable: Optional[bool]
    UpdateStatus: Optional[str]
    Description: Optional[str]
    AutomatedUpdateDate: Optional[str]
    OptionalDeployment: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceSoftwareOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceSoftwareOptions"]:
        if not json_data:
            return None
        return cls(
            CurrentVersion=json_data.get("CurrentVersion"),
            NewVersion=json_data.get("NewVersion"),
            UpdateAvailable=json_data.get("UpdateAvailable"),
            Cancellable=json_data.get("Cancellable"),
            UpdateStatus=json_data.get("UpdateStatus"),
            Description=json_data.get("Description"),
            AutomatedUpdateDate=json_data.get("AutomatedUpdateDate"),
            OptionalDeployment=json_data.get("OptionalDeployment"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceSoftwareOptions = ServiceSoftwareOptions


@dataclass
class OffPeakWindowOptions(BaseModel):
    Enabled: Optional[bool]
    OffPeakWindow: Optional["_OffPeakWindow"]

    @classmethod
    def _deserialize(
        cls: Type["_OffPeakWindowOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OffPeakWindowOptions"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            OffPeakWindow=OffPeakWindow._deserialize(json_data.get("OffPeakWindow")),
        )


# work around possible type aliasing issues when variable has same name as a model
_OffPeakWindowOptions = OffPeakWindowOptions


@dataclass
class OffPeakWindow(BaseModel):
    WindowStartTime: Optional["_WindowStartTime"]

    @classmethod
    def _deserialize(
        cls: Type["_OffPeakWindow"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OffPeakWindow"]:
        if not json_data:
            return None
        return cls(
            WindowStartTime=WindowStartTime._deserialize(json_data.get("WindowStartTime")),
        )


# work around possible type aliasing issues when variable has same name as a model
_OffPeakWindow = OffPeakWindow


@dataclass
class WindowStartTime(BaseModel):
    Hours: Optional[int]
    Minutes: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_WindowStartTime"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WindowStartTime"]:
        if not json_data:
            return None
        return cls(
            Hours=json_data.get("Hours"),
            Minutes=json_data.get("Minutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WindowStartTime = WindowStartTime


@dataclass
class SoftwareUpdateOptions(BaseModel):
    AutoSoftwareUpdateEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SoftwareUpdateOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SoftwareUpdateOptions"]:
        if not json_data:
            return None
        return cls(
            AutoSoftwareUpdateEnabled=json_data.get("AutoSoftwareUpdateEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SoftwareUpdateOptions = SoftwareUpdateOptions


