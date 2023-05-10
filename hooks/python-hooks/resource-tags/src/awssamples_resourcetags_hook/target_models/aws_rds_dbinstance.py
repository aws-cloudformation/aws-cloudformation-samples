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
class AwsRdsDbinstance(BaseModel):
    AllocatedStorage: Optional[str]
    AllowMajorVersionUpgrade: Optional[bool]
    AssociatedRoles: Optional[Sequence["_DBInstanceRole"]]
    AutoMinorVersionUpgrade: Optional[bool]
    AvailabilityZone: Optional[str]
    BackupRetentionPeriod: Optional[int]
    CACertificateIdentifier: Optional[str]
    CertificateDetails: Optional["_CertificateDetails"]
    CertificateRotationRestart: Optional[bool]
    CharacterSetName: Optional[str]
    CopyTagsToSnapshot: Optional[bool]
    CustomIAMInstanceProfile: Optional[str]
    DBClusterIdentifier: Optional[str]
    DBClusterSnapshotIdentifier: Optional[str]
    DBInstanceArn: Optional[str]
    DBInstanceClass: Optional[str]
    DBInstanceIdentifier: Optional[str]
    DbiResourceId: Optional[str]
    DBName: Optional[str]
    DBParameterGroupName: Optional[str]
    DBSecurityGroups: Optional[Sequence[str]]
    DBSnapshotIdentifier: Optional[str]
    DBSubnetGroupName: Optional[str]
    DBSystemId: Optional[str]
    DeleteAutomatedBackups: Optional[bool]
    DeletionProtection: Optional[bool]
    Domain: Optional[str]
    DomainIAMRoleName: Optional[str]
    EnableCloudwatchLogsExports: Optional[Sequence[str]]
    EnableIAMDatabaseAuthentication: Optional[bool]
    EnablePerformanceInsights: Optional[bool]
    Endpoint: Optional["_Endpoint"]
    Engine: Optional[str]
    EngineVersion: Optional[str]
    ManageMasterUserPassword: Optional[bool]
    Iops: Optional[int]
    KmsKeyId: Optional[str]
    LicenseModel: Optional[str]
    MasterUsername: Optional[str]
    MasterUserPassword: Optional[str]
    MasterUserSecret: Optional["_MasterUserSecret"]
    MaxAllocatedStorage: Optional[int]
    MonitoringInterval: Optional[int]
    MonitoringRoleArn: Optional[str]
    MultiAZ: Optional[bool]
    NcharCharacterSetName: Optional[str]
    NetworkType: Optional[str]
    OptionGroupName: Optional[str]
    PerformanceInsightsKMSKeyId: Optional[str]
    PerformanceInsightsRetentionPeriod: Optional[int]
    Port: Optional[str]
    PreferredBackupWindow: Optional[str]
    PreferredMaintenanceWindow: Optional[str]
    ProcessorFeatures: Optional[Sequence["_ProcessorFeature"]]
    PromotionTier: Optional[int]
    PubliclyAccessible: Optional[bool]
    ReplicaMode: Optional[str]
    RestoreTime: Optional[str]
    SourceDBClusterIdentifier: Optional[str]
    SourceDbiResourceId: Optional[str]
    SourceDBInstanceAutomatedBackupsArn: Optional[str]
    SourceDBInstanceIdentifier: Optional[str]
    SourceRegion: Optional[str]
    StorageEncrypted: Optional[bool]
    StorageType: Optional[str]
    StorageThroughput: Optional[int]
    Tags: Optional[Any]
    TdeCredentialArn: Optional[str]
    TdeCredentialPassword: Optional[str]
    Timezone: Optional[str]
    UseDefaultProcessorFeatures: Optional[bool]
    UseLatestRestorableTime: Optional[bool]
    VPCSecurityGroups: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRdsDbinstance"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRdsDbinstance"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AllocatedStorage=json_data.get("AllocatedStorage"),
            AllowMajorVersionUpgrade=json_data.get("AllowMajorVersionUpgrade"),
            AssociatedRoles=deserialize_list(json_data.get("AssociatedRoles"), DBInstanceRole),
            AutoMinorVersionUpgrade=json_data.get("AutoMinorVersionUpgrade"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            BackupRetentionPeriod=json_data.get("BackupRetentionPeriod"),
            CACertificateIdentifier=json_data.get("CACertificateIdentifier"),
            CertificateDetails=CertificateDetails._deserialize(json_data.get("CertificateDetails")),
            CertificateRotationRestart=json_data.get("CertificateRotationRestart"),
            CharacterSetName=json_data.get("CharacterSetName"),
            CopyTagsToSnapshot=json_data.get("CopyTagsToSnapshot"),
            CustomIAMInstanceProfile=json_data.get("CustomIAMInstanceProfile"),
            DBClusterIdentifier=json_data.get("DBClusterIdentifier"),
            DBClusterSnapshotIdentifier=json_data.get("DBClusterSnapshotIdentifier"),
            DBInstanceArn=json_data.get("DBInstanceArn"),
            DBInstanceClass=json_data.get("DBInstanceClass"),
            DBInstanceIdentifier=json_data.get("DBInstanceIdentifier"),
            DbiResourceId=json_data.get("DbiResourceId"),
            DBName=json_data.get("DBName"),
            DBParameterGroupName=json_data.get("DBParameterGroupName"),
            DBSecurityGroups=json_data.get("DBSecurityGroups"),
            DBSnapshotIdentifier=json_data.get("DBSnapshotIdentifier"),
            DBSubnetGroupName=json_data.get("DBSubnetGroupName"),
            DBSystemId=json_data.get("DBSystemId"),
            DeleteAutomatedBackups=json_data.get("DeleteAutomatedBackups"),
            DeletionProtection=json_data.get("DeletionProtection"),
            Domain=json_data.get("Domain"),
            DomainIAMRoleName=json_data.get("DomainIAMRoleName"),
            EnableCloudwatchLogsExports=json_data.get("EnableCloudwatchLogsExports"),
            EnableIAMDatabaseAuthentication=json_data.get("EnableIAMDatabaseAuthentication"),
            EnablePerformanceInsights=json_data.get("EnablePerformanceInsights"),
            Endpoint=Endpoint._deserialize(json_data.get("Endpoint")),
            Engine=json_data.get("Engine"),
            EngineVersion=json_data.get("EngineVersion"),
            ManageMasterUserPassword=json_data.get("ManageMasterUserPassword"),
            Iops=json_data.get("Iops"),
            KmsKeyId=json_data.get("KmsKeyId"),
            LicenseModel=json_data.get("LicenseModel"),
            MasterUsername=json_data.get("MasterUsername"),
            MasterUserPassword=json_data.get("MasterUserPassword"),
            MasterUserSecret=MasterUserSecret._deserialize(json_data.get("MasterUserSecret")),
            MaxAllocatedStorage=json_data.get("MaxAllocatedStorage"),
            MonitoringInterval=json_data.get("MonitoringInterval"),
            MonitoringRoleArn=json_data.get("MonitoringRoleArn"),
            MultiAZ=json_data.get("MultiAZ"),
            NcharCharacterSetName=json_data.get("NcharCharacterSetName"),
            NetworkType=json_data.get("NetworkType"),
            OptionGroupName=json_data.get("OptionGroupName"),
            PerformanceInsightsKMSKeyId=json_data.get("PerformanceInsightsKMSKeyId"),
            PerformanceInsightsRetentionPeriod=json_data.get("PerformanceInsightsRetentionPeriod"),
            Port=json_data.get("Port"),
            PreferredBackupWindow=json_data.get("PreferredBackupWindow"),
            PreferredMaintenanceWindow=json_data.get("PreferredMaintenanceWindow"),
            ProcessorFeatures=deserialize_list(json_data.get("ProcessorFeatures"), ProcessorFeature),
            PromotionTier=json_data.get("PromotionTier"),
            PubliclyAccessible=json_data.get("PubliclyAccessible"),
            ReplicaMode=json_data.get("ReplicaMode"),
            RestoreTime=json_data.get("RestoreTime"),
            SourceDBClusterIdentifier=json_data.get("SourceDBClusterIdentifier"),
            SourceDbiResourceId=json_data.get("SourceDbiResourceId"),
            SourceDBInstanceAutomatedBackupsArn=json_data.get("SourceDBInstanceAutomatedBackupsArn"),
            SourceDBInstanceIdentifier=json_data.get("SourceDBInstanceIdentifier"),
            SourceRegion=json_data.get("SourceRegion"),
            StorageEncrypted=json_data.get("StorageEncrypted"),
            StorageType=json_data.get("StorageType"),
            StorageThroughput=json_data.get("StorageThroughput"),
            Tags=json_data.get("Tags"),
            TdeCredentialArn=json_data.get("TdeCredentialArn"),
            TdeCredentialPassword=json_data.get("TdeCredentialPassword"),
            Timezone=json_data.get("Timezone"),
            UseDefaultProcessorFeatures=json_data.get("UseDefaultProcessorFeatures"),
            UseLatestRestorableTime=json_data.get("UseLatestRestorableTime"),
            VPCSecurityGroups=json_data.get("VPCSecurityGroups"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRdsDbinstance = AwsRdsDbinstance


@dataclass
class DBInstanceRole(BaseModel):
    FeatureName: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DBInstanceRole"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DBInstanceRole"]:
        if not json_data:
            return None
        return cls(
            FeatureName=json_data.get("FeatureName"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DBInstanceRole = DBInstanceRole


@dataclass
class CertificateDetails(BaseModel):
    CAIdentifier: Optional[str]
    ValidTill: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDetails"]:
        if not json_data:
            return None
        return cls(
            CAIdentifier=json_data.get("CAIdentifier"),
            ValidTill=json_data.get("ValidTill"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDetails = CertificateDetails


@dataclass
class Endpoint(BaseModel):
    Address: Optional[str]
    Port: Optional[str]
    HostedZoneId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Endpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Endpoint"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Port=json_data.get("Port"),
            HostedZoneId=json_data.get("HostedZoneId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Endpoint = Endpoint


@dataclass
class MasterUserSecret(BaseModel):
    SecretArn: Optional[str]
    KmsKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MasterUserSecret"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MasterUserSecret"]:
        if not json_data:
            return None
        return cls(
            SecretArn=json_data.get("SecretArn"),
            KmsKeyId=json_data.get("KmsKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MasterUserSecret = MasterUserSecret


@dataclass
class ProcessorFeature(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProcessorFeature"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProcessorFeature"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProcessorFeature = ProcessorFeature


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


