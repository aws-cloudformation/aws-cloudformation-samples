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
class AwsMemorydbCluster(BaseModel):
    ClusterName: Optional[str]
    Description: Optional[str]
    Status: Optional[str]
    NodeType: Optional[str]
    NumShards: Optional[int]
    NumReplicasPerShard: Optional[int]
    SubnetGroupName: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    MaintenanceWindow: Optional[str]
    ParameterGroupName: Optional[str]
    ParameterGroupStatus: Optional[str]
    Port: Optional[int]
    SnapshotRetentionLimit: Optional[int]
    SnapshotWindow: Optional[str]
    ACLName: Optional[str]
    SnsTopicArn: Optional[str]
    SnsTopicStatus: Optional[str]
    TLSEnabled: Optional[bool]
    DataTiering: Optional[str]
    KmsKeyId: Optional[str]
    SnapshotArns: Optional[Sequence[str]]
    SnapshotName: Optional[str]
    FinalSnapshotName: Optional[str]
    ARN: Optional[str]
    EngineVersion: Optional[str]
    ClusterEndpoint: Optional["_Endpoint"]
    AutoMinorVersionUpgrade: Optional[bool]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMemorydbCluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMemorydbCluster"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ClusterName=json_data.get("ClusterName"),
            Description=json_data.get("Description"),
            Status=json_data.get("Status"),
            NodeType=json_data.get("NodeType"),
            NumShards=json_data.get("NumShards"),
            NumReplicasPerShard=json_data.get("NumReplicasPerShard"),
            SubnetGroupName=json_data.get("SubnetGroupName"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            MaintenanceWindow=json_data.get("MaintenanceWindow"),
            ParameterGroupName=json_data.get("ParameterGroupName"),
            ParameterGroupStatus=json_data.get("ParameterGroupStatus"),
            Port=json_data.get("Port"),
            SnapshotRetentionLimit=json_data.get("SnapshotRetentionLimit"),
            SnapshotWindow=json_data.get("SnapshotWindow"),
            ACLName=json_data.get("ACLName"),
            SnsTopicArn=json_data.get("SnsTopicArn"),
            SnsTopicStatus=json_data.get("SnsTopicStatus"),
            TLSEnabled=json_data.get("TLSEnabled"),
            DataTiering=json_data.get("DataTiering"),
            KmsKeyId=json_data.get("KmsKeyId"),
            SnapshotArns=json_data.get("SnapshotArns"),
            SnapshotName=json_data.get("SnapshotName"),
            FinalSnapshotName=json_data.get("FinalSnapshotName"),
            ARN=json_data.get("ARN"),
            EngineVersion=json_data.get("EngineVersion"),
            ClusterEndpoint=Endpoint._deserialize(json_data.get("ClusterEndpoint")),
            AutoMinorVersionUpgrade=json_data.get("AutoMinorVersionUpgrade"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMemorydbCluster = AwsMemorydbCluster


@dataclass
class Endpoint(BaseModel):
    Address: Optional[str]
    Port: Optional[int]

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


