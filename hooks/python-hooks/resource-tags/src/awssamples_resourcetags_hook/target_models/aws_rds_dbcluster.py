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
class AwsRdsDbcluster(BaseModel):
    Endpoint: Optional["_Endpoint"]
    ReadEndpoint: Optional["_ReadEndpoint"]
    AllocatedStorage: Optional[int]
    AssociatedRoles: Optional[Sequence["_DBClusterRole"]]
    AvailabilityZones: Optional[Sequence[str]]
    AutoMinorVersionUpgrade: Optional[bool]
    BacktrackWindow: Optional[int]
    BackupRetentionPeriod: Optional[int]
    CopyTagsToSnapshot: Optional[bool]
    DatabaseName: Optional[str]
    DBClusterArn: Optional[str]
    DBClusterInstanceClass: Optional[str]
    DBClusterResourceId: Optional[str]
    DBInstanceParameterGroupName: Optional[str]
    DBSystemId: Optional[str]
    GlobalClusterIdentifier: Optional[str]
    DBClusterIdentifier: Optional[str]
    DBClusterParameterGroupName: Optional[str]
    DBSubnetGroupName: Optional[str]
    DeletionProtection: Optional[bool]
    Domain: Optional[str]
    DomainIAMRoleName: Optional[str]
    EnableCloudwatchLogsExports: Optional[Sequence[str]]
    EnableHttpEndpoint: Optional[bool]
    EnableIAMDatabaseAuthentication: Optional[bool]
    Engine: Optional[str]
    EngineMode: Optional[str]
    EngineVersion: Optional[str]
    ManageMasterUserPassword: Optional[bool]
    Iops: Optional[int]
    KmsKeyId: Optional[str]
    MasterUsername: Optional[str]
    MasterUserPassword: Optional[str]
    MasterUserSecret: Optional["_MasterUserSecret"]
    MonitoringInterval: Optional[int]
    MonitoringRoleArn: Optional[str]
    NetworkType: Optional[str]
    PerformanceInsightsEnabled: Optional[bool]
    PerformanceInsightsKmsKeyId: Optional[str]
    PerformanceInsightsRetentionPeriod: Optional[int]
    Port: Optional[int]
    PreferredBackupWindow: Optional[str]
    PreferredMaintenanceWindow: Optional[str]
    PubliclyAccessible: Optional[bool]
    ReplicationSourceIdentifier: Optional[str]
    RestoreToTime: Optional[str]
    RestoreType: Optional[str]
    ServerlessV2ScalingConfiguration: Optional["_ServerlessV2ScalingConfiguration"]
    ScalingConfiguration: Optional["_ScalingConfiguration"]
    SnapshotIdentifier: Optional[str]
    SourceDBClusterIdentifier: Optional[str]
    SourceRegion: Optional[str]
    StorageEncrypted: Optional[bool]
    StorageType: Optional[str]
    Tags: Optional[Any]
    UseLatestRestorableTime: Optional[bool]
    VpcSecurityGroupIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRdsDbcluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRdsDbcluster"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Endpoint=Endpoint._deserialize(json_data.get("Endpoint")),
            ReadEndpoint=ReadEndpoint._deserialize(json_data.get("ReadEndpoint")),
            AllocatedStorage=json_data.get("AllocatedStorage"),
            AssociatedRoles=deserialize_list(json_data.get("AssociatedRoles"), DBClusterRole),
            AvailabilityZones=json_data.get("AvailabilityZones"),
            AutoMinorVersionUpgrade=json_data.get("AutoMinorVersionUpgrade"),
            BacktrackWindow=json_data.get("BacktrackWindow"),
            BackupRetentionPeriod=json_data.get("BackupRetentionPeriod"),
            CopyTagsToSnapshot=json_data.get("CopyTagsToSnapshot"),
            DatabaseName=json_data.get("DatabaseName"),
            DBClusterArn=json_data.get("DBClusterArn"),
            DBClusterInstanceClass=json_data.get("DBClusterInstanceClass"),
            DBClusterResourceId=json_data.get("DBClusterResourceId"),
            DBInstanceParameterGroupName=json_data.get("DBInstanceParameterGroupName"),
            DBSystemId=json_data.get("DBSystemId"),
            GlobalClusterIdentifier=json_data.get("GlobalClusterIdentifier"),
            DBClusterIdentifier=json_data.get("DBClusterIdentifier"),
            DBClusterParameterGroupName=json_data.get("DBClusterParameterGroupName"),
            DBSubnetGroupName=json_data.get("DBSubnetGroupName"),
            DeletionProtection=json_data.get("DeletionProtection"),
            Domain=json_data.get("Domain"),
            DomainIAMRoleName=json_data.get("DomainIAMRoleName"),
            EnableCloudwatchLogsExports=json_data.get("EnableCloudwatchLogsExports"),
            EnableHttpEndpoint=json_data.get("EnableHttpEndpoint"),
            EnableIAMDatabaseAuthentication=json_data.get("EnableIAMDatabaseAuthentication"),
            Engine=json_data.get("Engine"),
            EngineMode=json_data.get("EngineMode"),
            EngineVersion=json_data.get("EngineVersion"),
            ManageMasterUserPassword=json_data.get("ManageMasterUserPassword"),
            Iops=json_data.get("Iops"),
            KmsKeyId=json_data.get("KmsKeyId"),
            MasterUsername=json_data.get("MasterUsername"),
            MasterUserPassword=json_data.get("MasterUserPassword"),
            MasterUserSecret=MasterUserSecret._deserialize(json_data.get("MasterUserSecret")),
            MonitoringInterval=json_data.get("MonitoringInterval"),
            MonitoringRoleArn=json_data.get("MonitoringRoleArn"),
            NetworkType=json_data.get("NetworkType"),
            PerformanceInsightsEnabled=json_data.get("PerformanceInsightsEnabled"),
            PerformanceInsightsKmsKeyId=json_data.get("PerformanceInsightsKmsKeyId"),
            PerformanceInsightsRetentionPeriod=json_data.get("PerformanceInsightsRetentionPeriod"),
            Port=json_data.get("Port"),
            PreferredBackupWindow=json_data.get("PreferredBackupWindow"),
            PreferredMaintenanceWindow=json_data.get("PreferredMaintenanceWindow"),
            PubliclyAccessible=json_data.get("PubliclyAccessible"),
            ReplicationSourceIdentifier=json_data.get("ReplicationSourceIdentifier"),
            RestoreToTime=json_data.get("RestoreToTime"),
            RestoreType=json_data.get("RestoreType"),
            ServerlessV2ScalingConfiguration=ServerlessV2ScalingConfiguration._deserialize(json_data.get("ServerlessV2ScalingConfiguration")),
            ScalingConfiguration=ScalingConfiguration._deserialize(json_data.get("ScalingConfiguration")),
            SnapshotIdentifier=json_data.get("SnapshotIdentifier"),
            SourceDBClusterIdentifier=json_data.get("SourceDBClusterIdentifier"),
            SourceRegion=json_data.get("SourceRegion"),
            StorageEncrypted=json_data.get("StorageEncrypted"),
            StorageType=json_data.get("StorageType"),
            Tags=json_data.get("Tags"),
            UseLatestRestorableTime=json_data.get("UseLatestRestorableTime"),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRdsDbcluster = AwsRdsDbcluster


@dataclass
class Endpoint(BaseModel):
    Address: Optional[str]
    Port: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Endpoint = Endpoint


@dataclass
class ReadEndpoint(BaseModel):
    Address: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReadEndpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReadEndpoint"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReadEndpoint = ReadEndpoint


@dataclass
class DBClusterRole(BaseModel):
    FeatureName: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DBClusterRole"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DBClusterRole"]:
        if not json_data:
            return None
        return cls(
            FeatureName=json_data.get("FeatureName"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DBClusterRole = DBClusterRole


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
class ServerlessV2ScalingConfiguration(BaseModel):
    MinCapacity: Optional[float]
    MaxCapacity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ServerlessV2ScalingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerlessV2ScalingConfiguration"]:
        if not json_data:
            return None
        return cls(
            MinCapacity=json_data.get("MinCapacity"),
            MaxCapacity=json_data.get("MaxCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerlessV2ScalingConfiguration = ServerlessV2ScalingConfiguration


@dataclass
class ScalingConfiguration(BaseModel):
    AutoPause: Optional[bool]
    MaxCapacity: Optional[int]
    MinCapacity: Optional[int]
    SecondsBeforeTimeout: Optional[int]
    SecondsUntilAutoPause: Optional[int]
    TimeoutAction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingConfiguration"]:
        if not json_data:
            return None
        return cls(
            AutoPause=json_data.get("AutoPause"),
            MaxCapacity=json_data.get("MaxCapacity"),
            MinCapacity=json_data.get("MinCapacity"),
            SecondsBeforeTimeout=json_data.get("SecondsBeforeTimeout"),
            SecondsUntilAutoPause=json_data.get("SecondsUntilAutoPause"),
            TimeoutAction=json_data.get("TimeoutAction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingConfiguration = ScalingConfiguration


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


