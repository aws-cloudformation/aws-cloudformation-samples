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
class AwsNeptuneDbcluster(BaseModel):
    Endpoint: Optional[str]
    ReadEndpoint: Optional[str]
    ClusterResourceId: Optional[str]
    AssociatedRoles: Optional[Sequence["_DBClusterRole"]]
    AvailabilityZones: Optional[Sequence[str]]
    BackupRetentionPeriod: Optional[int]
    CopyTagsToSnapshot: Optional[bool]
    DBClusterIdentifier: Optional[str]
    DBClusterParameterGroupName: Optional[str]
    DBInstanceParameterGroupName: Optional[str]
    DBSubnetGroupName: Optional[str]
    DeletionProtection: Optional[bool]
    EnableCloudwatchLogsExports: Optional[Sequence[str]]
    EngineVersion: Optional[str]
    IamAuthEnabled: Optional[bool]
    KmsKeyId: Optional[str]
    Port: Optional[str]
    PreferredBackupWindow: Optional[str]
    PreferredMaintenanceWindow: Optional[str]
    RestoreToTime: Optional[str]
    RestoreType: Optional[str]
    ServerlessScalingConfiguration: Optional["_ServerlessScalingConfiguration"]
    SnapshotIdentifier: Optional[str]
    SourceDBClusterIdentifier: Optional[str]
    StorageEncrypted: Optional[bool]
    Tags: Optional[Any]
    UseLatestRestorableTime: Optional[bool]
    VpcSecurityGroupIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsNeptuneDbcluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsNeptuneDbcluster"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Endpoint=json_data.get("Endpoint"),
            ReadEndpoint=json_data.get("ReadEndpoint"),
            ClusterResourceId=json_data.get("ClusterResourceId"),
            AssociatedRoles=deserialize_list(json_data.get("AssociatedRoles"), DBClusterRole),
            AvailabilityZones=json_data.get("AvailabilityZones"),
            BackupRetentionPeriod=json_data.get("BackupRetentionPeriod"),
            CopyTagsToSnapshot=json_data.get("CopyTagsToSnapshot"),
            DBClusterIdentifier=json_data.get("DBClusterIdentifier"),
            DBClusterParameterGroupName=json_data.get("DBClusterParameterGroupName"),
            DBInstanceParameterGroupName=json_data.get("DBInstanceParameterGroupName"),
            DBSubnetGroupName=json_data.get("DBSubnetGroupName"),
            DeletionProtection=json_data.get("DeletionProtection"),
            EnableCloudwatchLogsExports=json_data.get("EnableCloudwatchLogsExports"),
            EngineVersion=json_data.get("EngineVersion"),
            IamAuthEnabled=json_data.get("IamAuthEnabled"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Port=json_data.get("Port"),
            PreferredBackupWindow=json_data.get("PreferredBackupWindow"),
            PreferredMaintenanceWindow=json_data.get("PreferredMaintenanceWindow"),
            RestoreToTime=json_data.get("RestoreToTime"),
            RestoreType=json_data.get("RestoreType"),
            ServerlessScalingConfiguration=ServerlessScalingConfiguration._deserialize(json_data.get("ServerlessScalingConfiguration")),
            SnapshotIdentifier=json_data.get("SnapshotIdentifier"),
            SourceDBClusterIdentifier=json_data.get("SourceDBClusterIdentifier"),
            StorageEncrypted=json_data.get("StorageEncrypted"),
            Tags=json_data.get("Tags"),
            UseLatestRestorableTime=json_data.get("UseLatestRestorableTime"),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsNeptuneDbcluster = AwsNeptuneDbcluster


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
class ServerlessScalingConfiguration(BaseModel):
    MinCapacity: Optional[float]
    MaxCapacity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ServerlessScalingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerlessScalingConfiguration"]:
        if not json_data:
            return None
        return cls(
            MinCapacity=json_data.get("MinCapacity"),
            MaxCapacity=json_data.get("MaxCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerlessScalingConfiguration = ServerlessScalingConfiguration


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


