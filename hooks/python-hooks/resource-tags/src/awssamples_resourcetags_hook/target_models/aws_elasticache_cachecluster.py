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
class AwsElasticacheCachecluster(BaseModel):
    CacheSecurityGroupNames: Optional[Sequence[str]]
    SnapshotArns: Optional[Sequence[str]]
    Port: Optional[int]
    ConfigurationEndpointAddress: Optional[str]
    NotificationTopicArn: Optional[str]
    NumCacheNodes: Optional[int]
    SnapshotName: Optional[str]
    TransitEncryptionEnabled: Optional[bool]
    NetworkType: Optional[str]
    PreferredAvailabilityZones: Optional[Sequence[str]]
    VpcSecurityGroupIds: Optional[Sequence[str]]
    ClusterName: Optional[str]
    RedisEndpointAddress: Optional[str]
    Engine: Optional[str]
    Tags: Optional[Any]
    EngineVersion: Optional[str]
    RedisEndpointPort: Optional[str]
    CacheSubnetGroupName: Optional[str]
    CacheParameterGroupName: Optional[str]
    PreferredMaintenanceWindow: Optional[str]
    AutoMinorVersionUpgrade: Optional[bool]
    PreferredAvailabilityZone: Optional[str]
    SnapshotWindow: Optional[str]
    CacheNodeType: Optional[str]
    SnapshotRetentionLimit: Optional[int]
    ConfigurationEndpointPort: Optional[str]
    IpDiscovery: Optional[str]
    LogDeliveryConfigurations: Optional[Sequence["_LogDeliveryConfigurationRequest"]]
    Id: Optional[str]
    AZMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsElasticacheCachecluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsElasticacheCachecluster"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CacheSecurityGroupNames=json_data.get("CacheSecurityGroupNames"),
            SnapshotArns=json_data.get("SnapshotArns"),
            Port=json_data.get("Port"),
            ConfigurationEndpointAddress=json_data.get("ConfigurationEndpointAddress"),
            NotificationTopicArn=json_data.get("NotificationTopicArn"),
            NumCacheNodes=json_data.get("NumCacheNodes"),
            SnapshotName=json_data.get("SnapshotName"),
            TransitEncryptionEnabled=json_data.get("TransitEncryptionEnabled"),
            NetworkType=json_data.get("NetworkType"),
            PreferredAvailabilityZones=json_data.get("PreferredAvailabilityZones"),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
            ClusterName=json_data.get("ClusterName"),
            RedisEndpointAddress=json_data.get("RedisEndpointAddress"),
            Engine=json_data.get("Engine"),
            Tags=json_data.get("Tags"),
            EngineVersion=json_data.get("EngineVersion"),
            RedisEndpointPort=json_data.get("RedisEndpointPort"),
            CacheSubnetGroupName=json_data.get("CacheSubnetGroupName"),
            CacheParameterGroupName=json_data.get("CacheParameterGroupName"),
            PreferredMaintenanceWindow=json_data.get("PreferredMaintenanceWindow"),
            AutoMinorVersionUpgrade=json_data.get("AutoMinorVersionUpgrade"),
            PreferredAvailabilityZone=json_data.get("PreferredAvailabilityZone"),
            SnapshotWindow=json_data.get("SnapshotWindow"),
            CacheNodeType=json_data.get("CacheNodeType"),
            SnapshotRetentionLimit=json_data.get("SnapshotRetentionLimit"),
            ConfigurationEndpointPort=json_data.get("ConfigurationEndpointPort"),
            IpDiscovery=json_data.get("IpDiscovery"),
            LogDeliveryConfigurations=deserialize_list(json_data.get("LogDeliveryConfigurations"), LogDeliveryConfigurationRequest),
            Id=json_data.get("Id"),
            AZMode=json_data.get("AZMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsElasticacheCachecluster = AwsElasticacheCachecluster


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


