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
class AwsElasticacheReplicationgroup(BaseModel):
    PreferredCacheClusterAZs: Optional[Sequence[str]]
    PrimaryEndPointPort: Optional[str]
    CacheSecurityGroupNames: Optional[Sequence[str]]
    ReaderEndPointPort: Optional[str]
    NodeGroupConfiguration: Optional[Sequence["_NodeGroupConfiguration"]]
    SnapshotArns: Optional[Sequence[str]]
    ConfigurationEndPointPort: Optional[str]
    Port: Optional[int]
    ReadEndPointPortsList: Optional[Sequence[str]]
    NumNodeGroups: Optional[int]
    NotificationTopicArn: Optional[str]
    SnapshotName: Optional[str]
    AutomaticFailoverEnabled: Optional[bool]
    ReplicasPerNodeGroup: Optional[int]
    ReplicationGroupDescription: Optional[str]
    ReaderEndPointAddress: Optional[str]
    MultiAZEnabled: Optional[bool]
    TransitEncryptionEnabled: Optional[bool]
    NetworkType: Optional[str]
    ReplicationGroupId: Optional[str]
    Engine: Optional[str]
    Tags: Optional[Any]
    NumCacheClusters: Optional[int]
    PrimaryEndPointAddress: Optional[str]
    GlobalReplicationGroupId: Optional[str]
    ConfigurationEndPointAddress: Optional[str]
    EngineVersion: Optional[str]
    KmsKeyId: Optional[str]
    CacheSubnetGroupName: Optional[str]
    CacheParameterGroupName: Optional[str]
    PreferredMaintenanceWindow: Optional[str]
    PrimaryClusterId: Optional[str]
    ReadEndPointPorts: Optional[str]
    AtRestEncryptionEnabled: Optional[bool]
    AutoMinorVersionUpgrade: Optional[bool]
    SecurityGroupIds: Optional[Sequence[str]]
    SnapshotWindow: Optional[str]
    TransitEncryptionMode: Optional[str]
    CacheNodeType: Optional[str]
    SnapshotRetentionLimit: Optional[int]
    ReadEndPointAddressesList: Optional[Sequence[str]]
    SnapshottingClusterId: Optional[str]
    UserGroupIds: Optional[Sequence[str]]
    IpDiscovery: Optional[str]
    AuthToken: Optional[str]
    DataTieringEnabled: Optional[bool]
    LogDeliveryConfigurations: Optional[Sequence["_LogDeliveryConfigurationRequest"]]
    ReadEndPointAddresses: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsElasticacheReplicationgroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsElasticacheReplicationgroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            PreferredCacheClusterAZs=json_data.get("PreferredCacheClusterAZs"),
            PrimaryEndPointPort=json_data.get("PrimaryEndPointPort"),
            CacheSecurityGroupNames=json_data.get("CacheSecurityGroupNames"),
            ReaderEndPointPort=json_data.get("ReaderEndPointPort"),
            NodeGroupConfiguration=deserialize_list(json_data.get("NodeGroupConfiguration"), NodeGroupConfiguration),
            SnapshotArns=json_data.get("SnapshotArns"),
            ConfigurationEndPointPort=json_data.get("ConfigurationEndPointPort"),
            Port=json_data.get("Port"),
            ReadEndPointPortsList=json_data.get("ReadEndPointPortsList"),
            NumNodeGroups=json_data.get("NumNodeGroups"),
            NotificationTopicArn=json_data.get("NotificationTopicArn"),
            SnapshotName=json_data.get("SnapshotName"),
            AutomaticFailoverEnabled=json_data.get("AutomaticFailoverEnabled"),
            ReplicasPerNodeGroup=json_data.get("ReplicasPerNodeGroup"),
            ReplicationGroupDescription=json_data.get("ReplicationGroupDescription"),
            ReaderEndPointAddress=json_data.get("ReaderEndPointAddress"),
            MultiAZEnabled=json_data.get("MultiAZEnabled"),
            TransitEncryptionEnabled=json_data.get("TransitEncryptionEnabled"),
            NetworkType=json_data.get("NetworkType"),
            ReplicationGroupId=json_data.get("ReplicationGroupId"),
            Engine=json_data.get("Engine"),
            Tags=json_data.get("Tags"),
            NumCacheClusters=json_data.get("NumCacheClusters"),
            PrimaryEndPointAddress=json_data.get("PrimaryEndPointAddress"),
            GlobalReplicationGroupId=json_data.get("GlobalReplicationGroupId"),
            ConfigurationEndPointAddress=json_data.get("ConfigurationEndPointAddress"),
            EngineVersion=json_data.get("EngineVersion"),
            KmsKeyId=json_data.get("KmsKeyId"),
            CacheSubnetGroupName=json_data.get("CacheSubnetGroupName"),
            CacheParameterGroupName=json_data.get("CacheParameterGroupName"),
            PreferredMaintenanceWindow=json_data.get("PreferredMaintenanceWindow"),
            PrimaryClusterId=json_data.get("PrimaryClusterId"),
            ReadEndPointPorts=json_data.get("ReadEndPointPorts"),
            AtRestEncryptionEnabled=json_data.get("AtRestEncryptionEnabled"),
            AutoMinorVersionUpgrade=json_data.get("AutoMinorVersionUpgrade"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SnapshotWindow=json_data.get("SnapshotWindow"),
            TransitEncryptionMode=json_data.get("TransitEncryptionMode"),
            CacheNodeType=json_data.get("CacheNodeType"),
            SnapshotRetentionLimit=json_data.get("SnapshotRetentionLimit"),
            ReadEndPointAddressesList=json_data.get("ReadEndPointAddressesList"),
            SnapshottingClusterId=json_data.get("SnapshottingClusterId"),
            UserGroupIds=json_data.get("UserGroupIds"),
            IpDiscovery=json_data.get("IpDiscovery"),
            AuthToken=json_data.get("AuthToken"),
            DataTieringEnabled=json_data.get("DataTieringEnabled"),
            LogDeliveryConfigurations=deserialize_list(json_data.get("LogDeliveryConfigurations"), LogDeliveryConfigurationRequest),
            ReadEndPointAddresses=json_data.get("ReadEndPointAddresses"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsElasticacheReplicationgroup = AwsElasticacheReplicationgroup


@dataclass
class NodeGroupConfiguration(BaseModel):
    Slots: Optional[str]
    PrimaryAvailabilityZone: Optional[str]
    ReplicaAvailabilityZones: Optional[Sequence[str]]
    NodeGroupId: Optional[str]
    ReplicaCount: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_NodeGroupConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeGroupConfiguration"]:
        if not json_data:
            return None
        return cls(
            Slots=json_data.get("Slots"),
            PrimaryAvailabilityZone=json_data.get("PrimaryAvailabilityZone"),
            ReplicaAvailabilityZones=json_data.get("ReplicaAvailabilityZones"),
            NodeGroupId=json_data.get("NodeGroupId"),
            ReplicaCount=json_data.get("ReplicaCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeGroupConfiguration = NodeGroupConfiguration


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
class LogDeliveryConfigurationRequest(BaseModel):
    LogType: Optional[str]
    LogFormat: Optional[str]
    DestinationType: Optional[str]
    DestinationDetails: Optional["_DestinationDetails"]

    @classmethod
    def _deserialize(
        cls: Type["_LogDeliveryConfigurationRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogDeliveryConfigurationRequest"]:
        if not json_data:
            return None
        return cls(
            LogType=json_data.get("LogType"),
            LogFormat=json_data.get("LogFormat"),
            DestinationType=json_data.get("DestinationType"),
            DestinationDetails=DestinationDetails._deserialize(json_data.get("DestinationDetails")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogDeliveryConfigurationRequest = LogDeliveryConfigurationRequest


@dataclass
class DestinationDetails(BaseModel):
    CloudWatchLogsDetails: Optional["_CloudWatchLogsDestinationDetails"]
    KinesisFirehoseDetails: Optional["_KinesisFirehoseDestinationDetails"]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationDetails"]:
        if not json_data:
            return None
        return cls(
            CloudWatchLogsDetails=CloudWatchLogsDestinationDetails._deserialize(json_data.get("CloudWatchLogsDetails")),
            KinesisFirehoseDetails=KinesisFirehoseDestinationDetails._deserialize(json_data.get("KinesisFirehoseDetails")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationDetails = DestinationDetails


@dataclass
class CloudWatchLogsDestinationDetails(BaseModel):
    LogGroup: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudWatchLogsDestinationDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudWatchLogsDestinationDetails"]:
        if not json_data:
            return None
        return cls(
            LogGroup=json_data.get("LogGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudWatchLogsDestinationDetails = CloudWatchLogsDestinationDetails


@dataclass
class KinesisFirehoseDestinationDetails(BaseModel):
    DeliveryStream: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisFirehoseDestinationDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisFirehoseDestinationDetails"]:
        if not json_data:
            return None
        return cls(
            DeliveryStream=json_data.get("DeliveryStream"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisFirehoseDestinationDetails = KinesisFirehoseDestinationDetails


