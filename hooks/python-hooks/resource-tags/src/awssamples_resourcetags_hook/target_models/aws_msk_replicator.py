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
class AwsMskReplicator(BaseModel):
    ReplicatorArn: Optional[str]
    ReplicatorName: Optional[str]
    CurrentVersion: Optional[str]
    Description: Optional[str]
    KafkaClusters: Optional[AbstractSet["_KafkaCluster"]]
    ReplicationInfoList: Optional[AbstractSet["_ReplicationInfo"]]
    ServiceExecutionRoleArn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMskReplicator"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMskReplicator"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ReplicatorArn=json_data.get("ReplicatorArn"),
            ReplicatorName=json_data.get("ReplicatorName"),
            CurrentVersion=json_data.get("CurrentVersion"),
            Description=json_data.get("Description"),
            KafkaClusters=set_or_none(json_data.get("KafkaClusters")),
            ReplicationInfoList=set_or_none(json_data.get("ReplicationInfoList")),
            ServiceExecutionRoleArn=json_data.get("ServiceExecutionRoleArn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMskReplicator = AwsMskReplicator


@dataclass
class KafkaCluster(BaseModel):
    AmazonMskCluster: Optional["_AmazonMskCluster"]
    VpcConfig: Optional["_KafkaClusterClientVpcConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_KafkaCluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KafkaCluster"]:
        if not json_data:
            return None
        return cls(
            AmazonMskCluster=AmazonMskCluster._deserialize(json_data.get("AmazonMskCluster")),
            VpcConfig=KafkaClusterClientVpcConfig._deserialize(json_data.get("VpcConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_KafkaCluster = KafkaCluster


@dataclass
class AmazonMskCluster(BaseModel):
    MskClusterArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AmazonMskCluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AmazonMskCluster"]:
        if not json_data:
            return None
        return cls(
            MskClusterArn=json_data.get("MskClusterArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AmazonMskCluster = AmazonMskCluster


@dataclass
class KafkaClusterClientVpcConfig(BaseModel):
    SecurityGroupIds: Optional[AbstractSet[str]]
    SubnetIds: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_KafkaClusterClientVpcConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KafkaClusterClientVpcConfig"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=set_or_none(json_data.get("SecurityGroupIds")),
            SubnetIds=set_or_none(json_data.get("SubnetIds")),
        )


# work around possible type aliasing issues when variable has same name as a model
_KafkaClusterClientVpcConfig = KafkaClusterClientVpcConfig


@dataclass
class ReplicationInfo(BaseModel):
    SourceKafkaClusterArn: Optional[str]
    TargetKafkaClusterArn: Optional[str]
    TargetCompressionType: Optional[str]
    TopicReplication: Optional["_TopicReplication"]
    ConsumerGroupReplication: Optional["_ConsumerGroupReplication"]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationInfo"]:
        if not json_data:
            return None
        return cls(
            SourceKafkaClusterArn=json_data.get("SourceKafkaClusterArn"),
            TargetKafkaClusterArn=json_data.get("TargetKafkaClusterArn"),
            TargetCompressionType=json_data.get("TargetCompressionType"),
            TopicReplication=TopicReplication._deserialize(json_data.get("TopicReplication")),
            ConsumerGroupReplication=ConsumerGroupReplication._deserialize(json_data.get("ConsumerGroupReplication")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationInfo = ReplicationInfo


@dataclass
class TopicReplication(BaseModel):
    TopicsToReplicate: Optional[AbstractSet[str]]
    TopicsToExclude: Optional[AbstractSet[str]]
    CopyTopicConfigurations: Optional[bool]
    CopyAccessControlListsForTopics: Optional[bool]
    DetectAndCopyNewTopics: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TopicReplication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopicReplication"]:
        if not json_data:
            return None
        return cls(
            TopicsToReplicate=set_or_none(json_data.get("TopicsToReplicate")),
            TopicsToExclude=set_or_none(json_data.get("TopicsToExclude")),
            CopyTopicConfigurations=json_data.get("CopyTopicConfigurations"),
            CopyAccessControlListsForTopics=json_data.get("CopyAccessControlListsForTopics"),
            DetectAndCopyNewTopics=json_data.get("DetectAndCopyNewTopics"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopicReplication = TopicReplication


@dataclass
class ConsumerGroupReplication(BaseModel):
    ConsumerGroupsToReplicate: Optional[AbstractSet[str]]
    ConsumerGroupsToExclude: Optional[AbstractSet[str]]
    SynchroniseConsumerGroupOffsets: Optional[bool]
    DetectAndCopyNewConsumerGroups: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ConsumerGroupReplication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConsumerGroupReplication"]:
        if not json_data:
            return None
        return cls(
            ConsumerGroupsToReplicate=set_or_none(json_data.get("ConsumerGroupsToReplicate")),
            ConsumerGroupsToExclude=set_or_none(json_data.get("ConsumerGroupsToExclude")),
            SynchroniseConsumerGroupOffsets=json_data.get("SynchroniseConsumerGroupOffsets"),
            DetectAndCopyNewConsumerGroups=json_data.get("DetectAndCopyNewConsumerGroups"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConsumerGroupReplication = ConsumerGroupReplication


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


