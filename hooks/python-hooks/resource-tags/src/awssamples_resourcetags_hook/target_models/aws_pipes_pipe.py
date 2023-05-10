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
class AwsPipesPipe(BaseModel):
    Arn: Optional[str]
    CreationTime: Optional[str]
    CurrentState: Optional[str]
    Description: Optional[str]
    DesiredState: Optional[str]
    Enrichment: Optional[str]
    EnrichmentParameters: Optional["_PipeEnrichmentParameters"]
    LastModifiedTime: Optional[str]
    Name: Optional[str]
    RoleArn: Optional[str]
    Source: Optional[str]
    SourceParameters: Optional["_PipeSourceParameters"]
    StateReason: Optional[str]
    Tags: Optional[Any]
    Target: Optional[str]
    TargetParameters: Optional["_PipeTargetParameters"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsPipesPipe"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsPipesPipe"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            CreationTime=json_data.get("CreationTime"),
            CurrentState=json_data.get("CurrentState"),
            Description=json_data.get("Description"),
            DesiredState=json_data.get("DesiredState"),
            Enrichment=json_data.get("Enrichment"),
            EnrichmentParameters=PipeEnrichmentParameters._deserialize(json_data.get("EnrichmentParameters")),
            LastModifiedTime=json_data.get("LastModifiedTime"),
            Name=json_data.get("Name"),
            RoleArn=json_data.get("RoleArn"),
            Source=json_data.get("Source"),
            SourceParameters=PipeSourceParameters._deserialize(json_data.get("SourceParameters")),
            StateReason=json_data.get("StateReason"),
            Tags=json_data.get("Tags"),
            Target=json_data.get("Target"),
            TargetParameters=PipeTargetParameters._deserialize(json_data.get("TargetParameters")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsPipesPipe = AwsPipesPipe


@dataclass
class PipeEnrichmentParameters(BaseModel):
    InputTemplate: Optional[str]
    HttpParameters: Optional["_PipeEnrichmentHttpParameters"]

    @classmethod
    def _deserialize(
        cls: Type["_PipeEnrichmentParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipeEnrichmentParameters"]:
        if not json_data:
            return None
        return cls(
            InputTemplate=json_data.get("InputTemplate"),
            HttpParameters=PipeEnrichmentHttpParameters._deserialize(json_data.get("HttpParameters")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipeEnrichmentParameters = PipeEnrichmentParameters


@dataclass
class PipeEnrichmentHttpParameters(BaseModel):
    PathParameterValues: Optional[Sequence[str]]
    HeaderParameters: Optional[MutableMapping[str, str]]
    QueryStringParameters: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_PipeEnrichmentHttpParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipeEnrichmentHttpParameters"]:
        if not json_data:
            return None
        return cls(
            PathParameterValues=json_data.get("PathParameterValues"),
            HeaderParameters=json_data.get("HeaderParameters"),
            QueryStringParameters=json_data.get("QueryStringParameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipeEnrichmentHttpParameters = PipeEnrichmentHttpParameters


@dataclass
class PipeSourceParameters(BaseModel):
    FilterCriteria: Optional["_FilterCriteria"]
    KinesisStreamParameters: Optional["_PipeSourceKinesisStreamParameters"]
    DynamoDBStreamParameters: Optional["_PipeSourceDynamoDBStreamParameters"]
    SqsQueueParameters: Optional["_PipeSourceSqsQueueParameters"]
    ActiveMQBrokerParameters: Optional["_PipeSourceActiveMQBrokerParameters"]
    RabbitMQBrokerParameters: Optional["_PipeSourceRabbitMQBrokerParameters"]
    ManagedStreamingKafkaParameters: Optional["_PipeSourceManagedStreamingKafkaParameters"]
    SelfManagedKafkaParameters: Optional["_PipeSourceSelfManagedKafkaParameters"]

    @classmethod
    def _deserialize(
        cls: Type["_PipeSourceParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipeSourceParameters"]:
        if not json_data:
            return None
        return cls(
            FilterCriteria=FilterCriteria._deserialize(json_data.get("FilterCriteria")),
            KinesisStreamParameters=PipeSourceKinesisStreamParameters._deserialize(json_data.get("KinesisStreamParameters")),
            DynamoDBStreamParameters=PipeSourceDynamoDBStreamParameters._deserialize(json_data.get("DynamoDBStreamParameters")),
            SqsQueueParameters=PipeSourceSqsQueueParameters._deserialize(json_data.get("SqsQueueParameters")),
            ActiveMQBrokerParameters=PipeSourceActiveMQBrokerParameters._deserialize(json_data.get("ActiveMQBrokerParameters")),
            RabbitMQBrokerParameters=PipeSourceRabbitMQBrokerParameters._deserialize(json_data.get("RabbitMQBrokerParameters")),
            ManagedStreamingKafkaParameters=PipeSourceManagedStreamingKafkaParameters._deserialize(json_data.get("ManagedStreamingKafkaParameters")),
            SelfManagedKafkaParameters=PipeSourceSelfManagedKafkaParameters._deserialize(json_data.get("SelfManagedKafkaParameters")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipeSourceParameters = PipeSourceParameters


@dataclass
class FilterCriteria(BaseModel):
    Filters: Optional[Sequence["_Filter"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterCriteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterCriteria"]:
        if not json_data:
            return None
        return cls(
            Filters=deserialize_list(json_data.get("Filters"), Filter),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterCriteria = FilterCriteria


@dataclass
class Filter(BaseModel):
    Pattern: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Filter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filter"]:
        if not json_data:
            return None
        return cls(
            Pattern=json_data.get("Pattern"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Filter = Filter


@dataclass
class PipeSourceKinesisStreamParameters(BaseModel):
    BatchSize: Optional[int]
    DeadLetterConfig: Optional["_DeadLetterConfig"]
    OnPartialBatchItemFailure: Optional[str]
    MaximumBatchingWindowInSeconds: Optional[int]
    MaximumRecordAgeInSeconds: Optional[int]
    MaximumRetryAttempts: Optional[int]
    ParallelizationFactor: Optional[int]
    StartingPosition: Optional[str]
    StartingPositionTimestamp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PipeSourceKinesisStreamParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipeSourceKinesisStreamParameters"]:
        if not json_data:
            return None
        return cls(
            BatchSize=json_data.get("BatchSize"),
            DeadLetterConfig=DeadLetterConfig._deserialize(json_data.get("DeadLetterConfig")),
            OnPartialBatchItemFailure=json_data.get("OnPartialBatchItemFailure"),
            MaximumBatchingWindowInSeconds=json_data.get("MaximumBatchingWindowInSeconds"),
            MaximumRecordAgeInSeconds=json_data.get("MaximumRecordAgeInSeconds"),
            MaximumRetryAttempts=json_data.get("MaximumRetryAttempts"),
            ParallelizationFactor=json_data.get("ParallelizationFactor"),
            StartingPosition=json_data.get("StartingPosition"),
            StartingPositionTimestamp=json_data.get("StartingPositionTimestamp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipeSourceKinesisStreamParameters = PipeSourceKinesisStreamParameters


@dataclass
class DeadLetterConfig(BaseModel):
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeadLetterConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeadLetterConfig"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeadLetterConfig = DeadLetterConfig


@dataclass
class PipeSourceDynamoDBStreamParameters(BaseModel):
    BatchSize: Optional[int]
    DeadLetterConfig: Optional["_DeadLetterConfig"]
    OnPartialBatchItemFailure: Optional[str]
    MaximumBatchingWindowInSeconds: Optional[int]
    MaximumRecordAgeInSeconds: Optional[int]
    MaximumRetryAttempts: Optional[int]
    ParallelizationFactor: Optional[int]
    StartingPosition: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PipeSourceDynamoDBStreamParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipeSourceDynamoDBStreamParameters"]:
        if not json_data:
            return None
        return cls(
            BatchSize=json_data.get("BatchSize"),
            DeadLetterConfig=DeadLetterConfig._deserialize(json_data.get("DeadLetterConfig")),
            OnPartialBatchItemFailure=json_data.get("OnPartialBatchItemFailure"),
            MaximumBatchingWindowInSeconds=json_data.get("MaximumBatchingWindowInSeconds"),
            MaximumRecordAgeInSeconds=json_data.get("MaximumRecordAgeInSeconds"),
            MaximumRetryAttempts=json_data.get("MaximumRetryAttempts"),
            ParallelizationFactor=json_data.get("ParallelizationFactor"),
            StartingPosition=json_data.get("StartingPosition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipeSourceDynamoDBStreamParameters = PipeSourceDynamoDBStreamParameters


@dataclass
class PipeSourceSqsQueueParameters(BaseModel):
    BatchSize: Optional[int]
    MaximumBatchingWindowInSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_PipeSourceSqsQueueParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipeSourceSqsQueueParameters"]:
        if not json_data:
            return None
        return cls(
            BatchSize=json_data.get("BatchSize"),
            MaximumBatchingWindowInSeconds=json_data.get("MaximumBatchingWindowInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipeSourceSqsQueueParameters = PipeSourceSqsQueueParameters


@dataclass
class PipeSourceActiveMQBrokerParameters(BaseModel):
    Credentials: Optional["_MQBrokerAccessCredentials"]
    QueueName: Optional[str]
    BatchSize: Optional[int]
    MaximumBatchingWindowInSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_PipeSourceActiveMQBrokerParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipeSourceActiveMQBrokerParameters"]:
        if not json_data:
            return None
        return cls(
            Credentials=MQBrokerAccessCredentials._deserialize(json_data.get("Credentials")),
            QueueName=json_data.get("QueueName"),
            BatchSize=json_data.get("BatchSize"),
            MaximumBatchingWindowInSeconds=json_data.get("MaximumBatchingWindowInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipeSourceActiveMQBrokerParameters = PipeSourceActiveMQBrokerParameters


@dataclass
class MQBrokerAccessCredentials(BaseModel):
    BasicAuth: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MQBrokerAccessCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MQBrokerAccessCredentials"]:
        if not json_data:
            return None
        return cls(
            BasicAuth=json_data.get("BasicAuth"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MQBrokerAccessCredentials = MQBrokerAccessCredentials


@dataclass
class PipeSourceRabbitMQBrokerParameters(BaseModel):
    Credentials: Optional["_MQBrokerAccessCredentials"]
    QueueName: Optional[str]
    VirtualHost: Optional[str]
    BatchSize: Optional[int]
    MaximumBatchingWindowInSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_PipeSourceRabbitMQBrokerParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipeSourceRabbitMQBrokerParameters"]:
        if not json_data:
            return None
        return cls(
            Credentials=MQBrokerAccessCredentials._deserialize(json_data.get("Credentials")),
            QueueName=json_data.get("QueueName"),
            VirtualHost=json_data.get("VirtualHost"),
            BatchSize=json_data.get("BatchSize"),
            MaximumBatchingWindowInSeconds=json_data.get("MaximumBatchingWindowInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipeSourceRabbitMQBrokerParameters = PipeSourceRabbitMQBrokerParameters


@dataclass
class PipeSourceManagedStreamingKafkaParameters(BaseModel):
    TopicName: Optional[str]
    StartingPosition: Optional[str]
    BatchSize: Optional[int]
    MaximumBatchingWindowInSeconds: Optional[int]
    ConsumerGroupID: Optional[str]
    Credentials: Optional["_MSKAccessCredentials"]

    @classmethod
    def _deserialize(
        cls: Type["_PipeSourceManagedStreamingKafkaParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipeSourceManagedStreamingKafkaParameters"]:
        if not json_data:
            return None
        return cls(
            TopicName=json_data.get("TopicName"),
            StartingPosition=json_data.get("StartingPosition"),
            BatchSize=json_data.get("BatchSize"),
            MaximumBatchingWindowInSeconds=json_data.get("MaximumBatchingWindowInSeconds"),
            ConsumerGroupID=json_data.get("ConsumerGroupID"),
            Credentials=MSKAccessCredentials._deserialize(json_data.get("Credentials")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipeSourceManagedStreamingKafkaParameters = PipeSourceManagedStreamingKafkaParameters


@dataclass
class MSKAccessCredentials(BaseModel):
    SaslScram512Auth: Optional[str]
    ClientCertificateTlsAuth: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MSKAccessCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MSKAccessCredentials"]:
        if not json_data:
            return None
        return cls(
            SaslScram512Auth=json_data.get("SaslScram512Auth"),
            ClientCertificateTlsAuth=json_data.get("ClientCertificateTlsAuth"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MSKAccessCredentials = MSKAccessCredentials


@dataclass
class PipeSourceSelfManagedKafkaParameters(BaseModel):
    TopicName: Optional[str]
    StartingPosition: Optional[str]
    AdditionalBootstrapServers: Optional[Sequence[str]]
    BatchSize: Optional[int]
    MaximumBatchingWindowInSeconds: Optional[int]
    ConsumerGroupID: Optional[str]
    Credentials: Optional["_SelfManagedKafkaAccessConfigurationCredentials"]
    ServerRootCaCertificate: Optional[str]
    Vpc: Optional["_SelfManagedKafkaAccessConfigurationVpc"]

    @classmethod
    def _deserialize(
        cls: Type["_PipeSourceSelfManagedKafkaParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipeSourceSelfManagedKafkaParameters"]:
        if not json_data:
            return None
        return cls(
            TopicName=json_data.get("TopicName"),
            StartingPosition=json_data.get("StartingPosition"),
            AdditionalBootstrapServers=json_data.get("AdditionalBootstrapServers"),
            BatchSize=json_data.get("BatchSize"),
            MaximumBatchingWindowInSeconds=json_data.get("MaximumBatchingWindowInSeconds"),
            ConsumerGroupID=json_data.get("ConsumerGroupID"),
            Credentials=SelfManagedKafkaAccessConfigurationCredentials._deserialize(json_data.get("Credentials")),
            ServerRootCaCertificate=json_data.get("ServerRootCaCertificate"),
            Vpc=SelfManagedKafkaAccessConfigurationVpc._deserialize(json_data.get("Vpc")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipeSourceSelfManagedKafkaParameters = PipeSourceSelfManagedKafkaParameters


@dataclass
class SelfManagedKafkaAccessConfigurationCredentials(BaseModel):
    BasicAuth: Optional[str]
    SaslScram512Auth: Optional[str]
    SaslScram256Auth: Optional[str]
    ClientCertificateTlsAuth: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SelfManagedKafkaAccessConfigurationCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelfManagedKafkaAccessConfigurationCredentials"]:
        if not json_data:
            return None
        return cls(
            BasicAuth=json_data.get("BasicAuth"),
            SaslScram512Auth=json_data.get("SaslScram512Auth"),
            SaslScram256Auth=json_data.get("SaslScram256Auth"),
            ClientCertificateTlsAuth=json_data.get("ClientCertificateTlsAuth"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelfManagedKafkaAccessConfigurationCredentials = SelfManagedKafkaAccessConfigurationCredentials


@dataclass
class SelfManagedKafkaAccessConfigurationVpc(BaseModel):
    Subnets: Optional[Sequence[str]]
    SecurityGroup: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SelfManagedKafkaAccessConfigurationVpc"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelfManagedKafkaAccessConfigurationVpc"]:
        if not json_data:
            return None
        return cls(
            Subnets=json_data.get("Subnets"),
            SecurityGroup=json_data.get("SecurityGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelfManagedKafkaAccessConfigurationVpc = SelfManagedKafkaAccessConfigurationVpc


@dataclass
class PipeTargetParameters(BaseModel):
    InputTemplate: Optional[str]
    LambdaFunctionParameters: Optional["_PipeTargetLambdaFunctionParameters"]
    StepFunctionStateMachineParameters: Optional["_PipeTargetStateMachineParameters"]
    KinesisStreamParameters: Optional["_PipeTargetKinesisStreamParameters"]
    EcsTaskParameters: Optional["_PipeTargetEcsTaskParameters"]
    BatchJobParameters: Optional["_PipeTargetBatchJobParameters"]
    SqsQueueParameters: Optional["_PipeTargetSqsQueueParameters"]
    HttpParameters: Optional["_PipeTargetHttpParameters"]
    RedshiftDataParameters: Optional["_PipeTargetRedshiftDataParameters"]
    SageMakerPipelineParameters: Optional["_PipeTargetSageMakerPipelineParameters"]
    EventBridgeEventBusParameters: Optional["_PipeTargetEventBridgeEventBusParameters"]
    CloudWatchLogsParameters: Optional["_PipeTargetCloudWatchLogsParameters"]

    @classmethod
    def _deserialize(
        cls: Type["_PipeTargetParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipeTargetParameters"]:
        if not json_data:
            return None
        return cls(
            InputTemplate=json_data.get("InputTemplate"),
            LambdaFunctionParameters=PipeTargetLambdaFunctionParameters._deserialize(json_data.get("LambdaFunctionParameters")),
            StepFunctionStateMachineParameters=PipeTargetStateMachineParameters._deserialize(json_data.get("StepFunctionStateMachineParameters")),
            KinesisStreamParameters=PipeTargetKinesisStreamParameters._deserialize(json_data.get("KinesisStreamParameters")),
            EcsTaskParameters=PipeTargetEcsTaskParameters._deserialize(json_data.get("EcsTaskParameters")),
            BatchJobParameters=PipeTargetBatchJobParameters._deserialize(json_data.get("BatchJobParameters")),
            SqsQueueParameters=PipeTargetSqsQueueParameters._deserialize(json_data.get("SqsQueueParameters")),
            HttpParameters=PipeTargetHttpParameters._deserialize(json_data.get("HttpParameters")),
            RedshiftDataParameters=PipeTargetRedshiftDataParameters._deserialize(json_data.get("RedshiftDataParameters")),
            SageMakerPipelineParameters=PipeTargetSageMakerPipelineParameters._deserialize(json_data.get("SageMakerPipelineParameters")),
            EventBridgeEventBusParameters=PipeTargetEventBridgeEventBusParameters._deserialize(json_data.get("EventBridgeEventBusParameters")),
            CloudWatchLogsParameters=PipeTargetCloudWatchLogsParameters._deserialize(json_data.get("CloudWatchLogsParameters")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipeTargetParameters = PipeTargetParameters


@dataclass
class PipeTargetLambdaFunctionParameters(BaseModel):
    InvocationType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PipeTargetLambdaFunctionParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipeTargetLambdaFunctionParameters"]:
        if not json_data:
            return None
        return cls(
            InvocationType=json_data.get("InvocationType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipeTargetLambdaFunctionParameters = PipeTargetLambdaFunctionParameters


@dataclass
class PipeTargetStateMachineParameters(BaseModel):
    InvocationType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PipeTargetStateMachineParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipeTargetStateMachineParameters"]:
        if not json_data:
            return None
        return cls(
            InvocationType=json_data.get("InvocationType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipeTargetStateMachineParameters = PipeTargetStateMachineParameters


@dataclass
class PipeTargetKinesisStreamParameters(BaseModel):
    PartitionKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PipeTargetKinesisStreamParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipeTargetKinesisStreamParameters"]:
        if not json_data:
            return None
        return cls(
            PartitionKey=json_data.get("PartitionKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipeTargetKinesisStreamParameters = PipeTargetKinesisStreamParameters


@dataclass
class PipeTargetEcsTaskParameters(BaseModel):
    TaskDefinitionArn: Optional[str]
    TaskCount: Optional[int]
    LaunchType: Optional[str]
    NetworkConfiguration: Optional["_NetworkConfiguration"]
    PlatformVersion: Optional[str]
    Group: Optional[str]
    CapacityProviderStrategy: Optional[Sequence["_CapacityProviderStrategyItem"]]
    EnableECSManagedTags: Optional[bool]
    EnableExecuteCommand: Optional[bool]
    PlacementConstraints: Optional[Sequence["_PlacementConstraint"]]
    PlacementStrategy: Optional[Sequence["_PlacementStrategy"]]
    PropagateTags: Optional[str]
    ReferenceId: Optional[str]
    Overrides: Optional["_EcsTaskOverride"]
    Tags: Optional[Sequence["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_PipeTargetEcsTaskParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipeTargetEcsTaskParameters"]:
        if not json_data:
            return None
        return cls(
            TaskDefinitionArn=json_data.get("TaskDefinitionArn"),
            TaskCount=json_data.get("TaskCount"),
            LaunchType=json_data.get("LaunchType"),
            NetworkConfiguration=NetworkConfiguration._deserialize(json_data.get("NetworkConfiguration")),
            PlatformVersion=json_data.get("PlatformVersion"),
            Group=json_data.get("Group"),
            CapacityProviderStrategy=deserialize_list(json_data.get("CapacityProviderStrategy"), CapacityProviderStrategyItem),
            EnableECSManagedTags=json_data.get("EnableECSManagedTags"),
            EnableExecuteCommand=json_data.get("EnableExecuteCommand"),
            PlacementConstraints=deserialize_list(json_data.get("PlacementConstraints"), PlacementConstraint),
            PlacementStrategy=deserialize_list(json_data.get("PlacementStrategy"), PlacementStrategy),
            PropagateTags=json_data.get("PropagateTags"),
            ReferenceId=json_data.get("ReferenceId"),
            Overrides=EcsTaskOverride._deserialize(json_data.get("Overrides")),
            Tags=deserialize_list(json_data.get("Tags"), Tag),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipeTargetEcsTaskParameters = PipeTargetEcsTaskParameters


@dataclass
class NetworkConfiguration(BaseModel):
    AwsvpcConfiguration: Optional["_AwsVpcConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkConfiguration"]:
        if not json_data:
            return None
        return cls(
            AwsvpcConfiguration=AwsVpcConfiguration._deserialize(json_data.get("AwsvpcConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkConfiguration = NetworkConfiguration


@dataclass
class AwsVpcConfiguration(BaseModel):
    Subnets: Optional[Sequence[str]]
    SecurityGroups: Optional[Sequence[str]]
    AssignPublicIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsVpcConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsVpcConfiguration"]:
        if not json_data:
            return None
        return cls(
            Subnets=json_data.get("Subnets"),
            SecurityGroups=json_data.get("SecurityGroups"),
            AssignPublicIp=json_data.get("AssignPublicIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsVpcConfiguration = AwsVpcConfiguration


@dataclass
class CapacityProviderStrategyItem(BaseModel):
    CapacityProvider: Optional[str]
    Weight: Optional[int]
    Base: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityProviderStrategyItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityProviderStrategyItem"]:
        if not json_data:
            return None
        return cls(
            CapacityProvider=json_data.get("CapacityProvider"),
            Weight=json_data.get("Weight"),
            Base=json_data.get("Base"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityProviderStrategyItem = CapacityProviderStrategyItem


@dataclass
class PlacementConstraint(BaseModel):
    Type: Optional[str]
    Expression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementConstraint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementConstraint"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Expression=json_data.get("Expression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementConstraint = PlacementConstraint


@dataclass
class PlacementStrategy(BaseModel):
    Type: Optional[str]
    Field: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementStrategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementStrategy"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Field=json_data.get("Field"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementStrategy = PlacementStrategy


@dataclass
class EcsTaskOverride(BaseModel):
    ContainerOverrides: Optional[Sequence["_EcsContainerOverride"]]
    Cpu: Optional[str]
    EphemeralStorage: Optional["_EcsEphemeralStorage"]
    ExecutionRoleArn: Optional[str]
    InferenceAcceleratorOverrides: Optional[Sequence["_EcsInferenceAcceleratorOverride"]]
    Memory: Optional[str]
    TaskRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EcsTaskOverride"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EcsTaskOverride"]:
        if not json_data:
            return None
        return cls(
            ContainerOverrides=deserialize_list(json_data.get("ContainerOverrides"), EcsContainerOverride),
            Cpu=json_data.get("Cpu"),
            EphemeralStorage=EcsEphemeralStorage._deserialize(json_data.get("EphemeralStorage")),
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            InferenceAcceleratorOverrides=deserialize_list(json_data.get("InferenceAcceleratorOverrides"), EcsInferenceAcceleratorOverride),
            Memory=json_data.get("Memory"),
            TaskRoleArn=json_data.get("TaskRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EcsTaskOverride = EcsTaskOverride


@dataclass
class EcsContainerOverride(BaseModel):
    Command: Optional[Sequence[str]]
    Cpu: Optional[int]
    Environment: Optional[Sequence["_EcsEnvironmentVariable"]]
    EnvironmentFiles: Optional[Sequence["_EcsEnvironmentFile"]]
    Memory: Optional[int]
    MemoryReservation: Optional[int]
    Name: Optional[str]
    ResourceRequirements: Optional[Sequence["_EcsResourceRequirement"]]

    @classmethod
    def _deserialize(
        cls: Type["_EcsContainerOverride"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EcsContainerOverride"]:
        if not json_data:
            return None
        return cls(
            Command=json_data.get("Command"),
            Cpu=json_data.get("Cpu"),
            Environment=deserialize_list(json_data.get("Environment"), EcsEnvironmentVariable),
            EnvironmentFiles=deserialize_list(json_data.get("EnvironmentFiles"), EcsEnvironmentFile),
            Memory=json_data.get("Memory"),
            MemoryReservation=json_data.get("MemoryReservation"),
            Name=json_data.get("Name"),
            ResourceRequirements=deserialize_list(json_data.get("ResourceRequirements"), EcsResourceRequirement),
        )


# work around possible type aliasing issues when variable has same name as a model
_EcsContainerOverride = EcsContainerOverride


@dataclass
class EcsEnvironmentVariable(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EcsEnvironmentVariable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EcsEnvironmentVariable"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EcsEnvironmentVariable = EcsEnvironmentVariable


@dataclass
class EcsEnvironmentFile(BaseModel):
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EcsEnvironmentFile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EcsEnvironmentFile"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EcsEnvironmentFile = EcsEnvironmentFile


@dataclass
class EcsResourceRequirement(BaseModel):
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EcsResourceRequirement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EcsResourceRequirement"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EcsResourceRequirement = EcsResourceRequirement


@dataclass
class EcsEphemeralStorage(BaseModel):
    SizeInGiB: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_EcsEphemeralStorage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EcsEphemeralStorage"]:
        if not json_data:
            return None
        return cls(
            SizeInGiB=json_data.get("SizeInGiB"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EcsEphemeralStorage = EcsEphemeralStorage


@dataclass
class EcsInferenceAcceleratorOverride(BaseModel):
    DeviceName: Optional[str]
    DeviceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EcsInferenceAcceleratorOverride"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EcsInferenceAcceleratorOverride"]:
        if not json_data:
            return None
        return cls(
            DeviceName=json_data.get("DeviceName"),
            DeviceType=json_data.get("DeviceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EcsInferenceAcceleratorOverride = EcsInferenceAcceleratorOverride


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
class PipeTargetBatchJobParameters(BaseModel):
    JobDefinition: Optional[str]
    JobName: Optional[str]
    ArrayProperties: Optional["_BatchArrayProperties"]
    RetryStrategy: Optional["_BatchRetryStrategy"]
    ContainerOverrides: Optional["_BatchContainerOverrides"]
    DependsOn: Optional[Sequence["_BatchJobDependency"]]
    Parameters: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_PipeTargetBatchJobParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipeTargetBatchJobParameters"]:
        if not json_data:
            return None
        return cls(
            JobDefinition=json_data.get("JobDefinition"),
            JobName=json_data.get("JobName"),
            ArrayProperties=BatchArrayProperties._deserialize(json_data.get("ArrayProperties")),
            RetryStrategy=BatchRetryStrategy._deserialize(json_data.get("RetryStrategy")),
            ContainerOverrides=BatchContainerOverrides._deserialize(json_data.get("ContainerOverrides")),
            DependsOn=deserialize_list(json_data.get("DependsOn"), BatchJobDependency),
            Parameters=json_data.get("Parameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipeTargetBatchJobParameters = PipeTargetBatchJobParameters


@dataclass
class BatchArrayProperties(BaseModel):
    Size: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_BatchArrayProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BatchArrayProperties"]:
        if not json_data:
            return None
        return cls(
            Size=json_data.get("Size"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BatchArrayProperties = BatchArrayProperties


@dataclass
class BatchRetryStrategy(BaseModel):
    Attempts: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_BatchRetryStrategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BatchRetryStrategy"]:
        if not json_data:
            return None
        return cls(
            Attempts=json_data.get("Attempts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BatchRetryStrategy = BatchRetryStrategy


@dataclass
class BatchContainerOverrides(BaseModel):
    Command: Optional[Sequence[str]]
    Environment: Optional[Sequence["_BatchEnvironmentVariable"]]
    InstanceType: Optional[str]
    ResourceRequirements: Optional[Sequence["_BatchResourceRequirement"]]

    @classmethod
    def _deserialize(
        cls: Type["_BatchContainerOverrides"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BatchContainerOverrides"]:
        if not json_data:
            return None
        return cls(
            Command=json_data.get("Command"),
            Environment=deserialize_list(json_data.get("Environment"), BatchEnvironmentVariable),
            InstanceType=json_data.get("InstanceType"),
            ResourceRequirements=deserialize_list(json_data.get("ResourceRequirements"), BatchResourceRequirement),
        )


# work around possible type aliasing issues when variable has same name as a model
_BatchContainerOverrides = BatchContainerOverrides


@dataclass
class BatchEnvironmentVariable(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BatchEnvironmentVariable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BatchEnvironmentVariable"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BatchEnvironmentVariable = BatchEnvironmentVariable


@dataclass
class BatchResourceRequirement(BaseModel):
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BatchResourceRequirement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BatchResourceRequirement"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BatchResourceRequirement = BatchResourceRequirement


@dataclass
class BatchJobDependency(BaseModel):
    JobId: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BatchJobDependency"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BatchJobDependency"]:
        if not json_data:
            return None
        return cls(
            JobId=json_data.get("JobId"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BatchJobDependency = BatchJobDependency


@dataclass
class PipeTargetSqsQueueParameters(BaseModel):
    MessageGroupId: Optional[str]
    MessageDeduplicationId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PipeTargetSqsQueueParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipeTargetSqsQueueParameters"]:
        if not json_data:
            return None
        return cls(
            MessageGroupId=json_data.get("MessageGroupId"),
            MessageDeduplicationId=json_data.get("MessageDeduplicationId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipeTargetSqsQueueParameters = PipeTargetSqsQueueParameters


@dataclass
class PipeTargetHttpParameters(BaseModel):
    PathParameterValues: Optional[Sequence[str]]
    HeaderParameters: Optional[MutableMapping[str, str]]
    QueryStringParameters: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_PipeTargetHttpParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipeTargetHttpParameters"]:
        if not json_data:
            return None
        return cls(
            PathParameterValues=json_data.get("PathParameterValues"),
            HeaderParameters=json_data.get("HeaderParameters"),
            QueryStringParameters=json_data.get("QueryStringParameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipeTargetHttpParameters = PipeTargetHttpParameters


@dataclass
class PipeTargetRedshiftDataParameters(BaseModel):
    SecretManagerArn: Optional[str]
    Database: Optional[str]
    DbUser: Optional[str]
    StatementName: Optional[str]
    WithEvent: Optional[bool]
    Sqls: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PipeTargetRedshiftDataParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipeTargetRedshiftDataParameters"]:
        if not json_data:
            return None
        return cls(
            SecretManagerArn=json_data.get("SecretManagerArn"),
            Database=json_data.get("Database"),
            DbUser=json_data.get("DbUser"),
            StatementName=json_data.get("StatementName"),
            WithEvent=json_data.get("WithEvent"),
            Sqls=json_data.get("Sqls"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipeTargetRedshiftDataParameters = PipeTargetRedshiftDataParameters


@dataclass
class PipeTargetSageMakerPipelineParameters(BaseModel):
    PipelineParameterList: Optional[Sequence["_SageMakerPipelineParameter"]]

    @classmethod
    def _deserialize(
        cls: Type["_PipeTargetSageMakerPipelineParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipeTargetSageMakerPipelineParameters"]:
        if not json_data:
            return None
        return cls(
            PipelineParameterList=deserialize_list(json_data.get("PipelineParameterList"), SageMakerPipelineParameter),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipeTargetSageMakerPipelineParameters = PipeTargetSageMakerPipelineParameters


@dataclass
class SageMakerPipelineParameter(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SageMakerPipelineParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SageMakerPipelineParameter"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SageMakerPipelineParameter = SageMakerPipelineParameter


@dataclass
class PipeTargetEventBridgeEventBusParameters(BaseModel):
    EndpointId: Optional[str]
    DetailType: Optional[str]
    Source: Optional[str]
    Resources: Optional[Sequence[str]]
    Time: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PipeTargetEventBridgeEventBusParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipeTargetEventBridgeEventBusParameters"]:
        if not json_data:
            return None
        return cls(
            EndpointId=json_data.get("EndpointId"),
            DetailType=json_data.get("DetailType"),
            Source=json_data.get("Source"),
            Resources=json_data.get("Resources"),
            Time=json_data.get("Time"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipeTargetEventBridgeEventBusParameters = PipeTargetEventBridgeEventBusParameters


@dataclass
class PipeTargetCloudWatchLogsParameters(BaseModel):
    LogStreamName: Optional[str]
    Timestamp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PipeTargetCloudWatchLogsParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipeTargetCloudWatchLogsParameters"]:
        if not json_data:
            return None
        return cls(
            LogStreamName=json_data.get("LogStreamName"),
            Timestamp=json_data.get("Timestamp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipeTargetCloudWatchLogsParameters = PipeTargetCloudWatchLogsParameters


