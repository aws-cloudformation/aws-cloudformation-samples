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
class AwsSqsQueue(BaseModel):
    QueueUrl: Optional[str]
    Arn: Optional[str]
    ContentBasedDeduplication: Optional[bool]
    DeduplicationScope: Optional[str]
    DelaySeconds: Optional[int]
    FifoQueue: Optional[bool]
    FifoThroughputLimit: Optional[str]
    KmsDataKeyReusePeriodSeconds: Optional[int]
    KmsMasterKeyId: Optional[str]
    SqsManagedSseEnabled: Optional[bool]
    MaximumMessageSize: Optional[int]
    MessageRetentionPeriod: Optional[int]
    QueueName: Optional[str]
    ReceiveMessageWaitTimeSeconds: Optional[int]
    RedriveAllowPolicy: Optional[Any]
    RedrivePolicy: Optional[Any]
    Tags: Optional[Any]
    VisibilityTimeout: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSqsQueue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSqsQueue"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            QueueUrl=json_data.get("QueueUrl"),
            Arn=json_data.get("Arn"),
            ContentBasedDeduplication=json_data.get("ContentBasedDeduplication"),
            DeduplicationScope=json_data.get("DeduplicationScope"),
            DelaySeconds=json_data.get("DelaySeconds"),
            FifoQueue=json_data.get("FifoQueue"),
            FifoThroughputLimit=json_data.get("FifoThroughputLimit"),
            KmsDataKeyReusePeriodSeconds=json_data.get("KmsDataKeyReusePeriodSeconds"),
            KmsMasterKeyId=json_data.get("KmsMasterKeyId"),
            SqsManagedSseEnabled=json_data.get("SqsManagedSseEnabled"),
            MaximumMessageSize=json_data.get("MaximumMessageSize"),
            MessageRetentionPeriod=json_data.get("MessageRetentionPeriod"),
            QueueName=json_data.get("QueueName"),
            ReceiveMessageWaitTimeSeconds=json_data.get("ReceiveMessageWaitTimeSeconds"),
            RedriveAllowPolicy=json_data.get("RedriveAllowPolicy"),
            RedrivePolicy=json_data.get("RedrivePolicy"),
            Tags=json_data.get("Tags"),
            VisibilityTimeout=json_data.get("VisibilityTimeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSqsQueue = AwsSqsQueue


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


