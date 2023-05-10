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
class AwsDocdbDbcluster(BaseModel):
    StorageEncrypted: Optional[bool]
    RestoreToTime: Optional[str]
    SnapshotIdentifier: Optional[str]
    Port: Optional[int]
    DBClusterIdentifier: Optional[str]
    PreferredBackupWindow: Optional[str]
    ClusterResourceId: Optional[str]
    Endpoint: Optional[str]
    VpcSecurityGroupIds: Optional[Sequence[str]]
    CopyTagsToSnapshot: Optional[bool]
    RestoreType: Optional[str]
    Tags: Optional[Any]
    EngineVersion: Optional[str]
    KmsKeyId: Optional[str]
    AvailabilityZones: Optional[Sequence[str]]
    PreferredMaintenanceWindow: Optional[str]
    DBSubnetGroupName: Optional[str]
    DeletionProtection: Optional[bool]
    UseLatestRestorableTime: Optional[bool]
    MasterUserPassword: Optional[str]
    SourceDBClusterIdentifier: Optional[str]
    MasterUsername: Optional[str]
    ReadEndpoint: Optional[str]
    DBClusterParameterGroupName: Optional[str]
    BackupRetentionPeriod: Optional[int]
    Id: Optional[str]
    EnableCloudwatchLogsExports: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDocdbDbcluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDocdbDbcluster"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            StorageEncrypted=json_data.get("StorageEncrypted"),
            RestoreToTime=json_data.get("RestoreToTime"),
            SnapshotIdentifier=json_data.get("SnapshotIdentifier"),
            Port=json_data.get("Port"),
            DBClusterIdentifier=json_data.get("DBClusterIdentifier"),
            PreferredBackupWindow=json_data.get("PreferredBackupWindow"),
            ClusterResourceId=json_data.get("ClusterResourceId"),
            Endpoint=json_data.get("Endpoint"),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
            CopyTagsToSnapshot=json_data.get("CopyTagsToSnapshot"),
            RestoreType=json_data.get("RestoreType"),
            Tags=json_data.get("Tags"),
            EngineVersion=json_data.get("EngineVersion"),
            KmsKeyId=json_data.get("KmsKeyId"),
            AvailabilityZones=json_data.get("AvailabilityZones"),
            PreferredMaintenanceWindow=json_data.get("PreferredMaintenanceWindow"),
            DBSubnetGroupName=json_data.get("DBSubnetGroupName"),
            DeletionProtection=json_data.get("DeletionProtection"),
            UseLatestRestorableTime=json_data.get("UseLatestRestorableTime"),
            MasterUserPassword=json_data.get("MasterUserPassword"),
            SourceDBClusterIdentifier=json_data.get("SourceDBClusterIdentifier"),
            MasterUsername=json_data.get("MasterUsername"),
            ReadEndpoint=json_data.get("ReadEndpoint"),
            DBClusterParameterGroupName=json_data.get("DBClusterParameterGroupName"),
            BackupRetentionPeriod=json_data.get("BackupRetentionPeriod"),
            Id=json_data.get("Id"),
            EnableCloudwatchLogsExports=json_data.get("EnableCloudwatchLogsExports"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDocdbDbcluster = AwsDocdbDbcluster


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


