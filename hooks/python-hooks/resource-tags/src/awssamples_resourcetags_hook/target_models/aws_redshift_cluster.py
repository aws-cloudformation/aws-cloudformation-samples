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
class AwsRedshiftCluster(BaseModel):
    ClusterIdentifier: Optional[str]
    MasterUsername: Optional[str]
    MasterUserPassword: Optional[str]
    NodeType: Optional[str]
    AllowVersionUpgrade: Optional[bool]
    AutomatedSnapshotRetentionPeriod: Optional[int]
    AvailabilityZone: Optional[str]
    ClusterParameterGroupName: Optional[str]
    ClusterType: Optional[str]
    ClusterVersion: Optional[str]
    ClusterSubnetGroupName: Optional[str]
    DBName: Optional[str]
    ElasticIp: Optional[str]
    Encrypted: Optional[bool]
    HsmClientCertificateIdentifier: Optional[str]
    HsmConfigurationIdentifier: Optional[str]
    KmsKeyId: Optional[str]
    NumberOfNodes: Optional[int]
    Port: Optional[int]
    PreferredMaintenanceWindow: Optional[str]
    PubliclyAccessible: Optional[bool]
    ClusterSecurityGroups: Optional[Sequence[str]]
    IamRoles: Optional[Sequence[str]]
    Tags: Optional[Any]
    VpcSecurityGroupIds: Optional[Sequence[str]]
    SnapshotClusterIdentifier: Optional[str]
    SnapshotIdentifier: Optional[str]
    Id: Optional[str]
    OwnerAccount: Optional[str]
    LoggingProperties: Optional["_LoggingProperties"]
    Endpoint: Optional["_Endpoint"]
    DestinationRegion: Optional[str]
    SnapshotCopyRetentionPeriod: Optional[int]
    SnapshotCopyGrantName: Optional[str]
    ManualSnapshotRetentionPeriod: Optional[int]
    SnapshotCopyManual: Optional[bool]
    AvailabilityZoneRelocation: Optional[bool]
    AvailabilityZoneRelocationStatus: Optional[str]
    AquaConfigurationStatus: Optional[str]
    Classic: Optional[bool]
    EnhancedVpcRouting: Optional[bool]
    MaintenanceTrackName: Optional[str]
    DeferMaintenance: Optional[bool]
    DeferMaintenanceIdentifier: Optional[str]
    DeferMaintenanceStartTime: Optional[str]
    DeferMaintenanceEndTime: Optional[str]
    DeferMaintenanceDuration: Optional[int]
    RevisionTarget: Optional[str]
    ResourceAction: Optional[str]
    RotateEncryptionKey: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRedshiftCluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRedshiftCluster"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ClusterIdentifier=json_data.get("ClusterIdentifier"),
            MasterUsername=json_data.get("MasterUsername"),
            MasterUserPassword=json_data.get("MasterUserPassword"),
            NodeType=json_data.get("NodeType"),
            AllowVersionUpgrade=json_data.get("AllowVersionUpgrade"),
            AutomatedSnapshotRetentionPeriod=json_data.get("AutomatedSnapshotRetentionPeriod"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            ClusterParameterGroupName=json_data.get("ClusterParameterGroupName"),
            ClusterType=json_data.get("ClusterType"),
            ClusterVersion=json_data.get("ClusterVersion"),
            ClusterSubnetGroupName=json_data.get("ClusterSubnetGroupName"),
            DBName=json_data.get("DBName"),
            ElasticIp=json_data.get("ElasticIp"),
            Encrypted=json_data.get("Encrypted"),
            HsmClientCertificateIdentifier=json_data.get("HsmClientCertificateIdentifier"),
            HsmConfigurationIdentifier=json_data.get("HsmConfigurationIdentifier"),
            KmsKeyId=json_data.get("KmsKeyId"),
            NumberOfNodes=json_data.get("NumberOfNodes"),
            Port=json_data.get("Port"),
            PreferredMaintenanceWindow=json_data.get("PreferredMaintenanceWindow"),
            PubliclyAccessible=json_data.get("PubliclyAccessible"),
            ClusterSecurityGroups=json_data.get("ClusterSecurityGroups"),
            IamRoles=json_data.get("IamRoles"),
            Tags=json_data.get("Tags"),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
            SnapshotClusterIdentifier=json_data.get("SnapshotClusterIdentifier"),
            SnapshotIdentifier=json_data.get("SnapshotIdentifier"),
            Id=json_data.get("Id"),
            OwnerAccount=json_data.get("OwnerAccount"),
            LoggingProperties=LoggingProperties._deserialize(json_data.get("LoggingProperties")),
            Endpoint=Endpoint._deserialize(json_data.get("Endpoint")),
            DestinationRegion=json_data.get("DestinationRegion"),
            SnapshotCopyRetentionPeriod=json_data.get("SnapshotCopyRetentionPeriod"),
            SnapshotCopyGrantName=json_data.get("SnapshotCopyGrantName"),
            ManualSnapshotRetentionPeriod=json_data.get("ManualSnapshotRetentionPeriod"),
            SnapshotCopyManual=json_data.get("SnapshotCopyManual"),
            AvailabilityZoneRelocation=json_data.get("AvailabilityZoneRelocation"),
            AvailabilityZoneRelocationStatus=json_data.get("AvailabilityZoneRelocationStatus"),
            AquaConfigurationStatus=json_data.get("AquaConfigurationStatus"),
            Classic=json_data.get("Classic"),
            EnhancedVpcRouting=json_data.get("EnhancedVpcRouting"),
            MaintenanceTrackName=json_data.get("MaintenanceTrackName"),
            DeferMaintenance=json_data.get("DeferMaintenance"),
            DeferMaintenanceIdentifier=json_data.get("DeferMaintenanceIdentifier"),
            DeferMaintenanceStartTime=json_data.get("DeferMaintenanceStartTime"),
            DeferMaintenanceEndTime=json_data.get("DeferMaintenanceEndTime"),
            DeferMaintenanceDuration=json_data.get("DeferMaintenanceDuration"),
            RevisionTarget=json_data.get("RevisionTarget"),
            ResourceAction=json_data.get("ResourceAction"),
            RotateEncryptionKey=json_data.get("RotateEncryptionKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRedshiftCluster = AwsRedshiftCluster


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
class LoggingProperties(BaseModel):
    BucketName: Optional[str]
    S3KeyPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingProperties"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            S3KeyPrefix=json_data.get("S3KeyPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingProperties = LoggingProperties


@dataclass
class Endpoint(BaseModel):
    Port: Optional[str]
    Address: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Endpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Endpoint"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Address=json_data.get("Address"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Endpoint = Endpoint


