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
class AwsSnsTopic(BaseModel):
    DisplayName: Optional[str]
    KmsMasterKeyId: Optional[str]
    DataProtectionPolicy: Optional[MutableMapping[str, Any]]
    Subscription: Optional[Sequence["_Subscription"]]
    FifoTopic: Optional[bool]
    ContentBasedDeduplication: Optional[bool]
    Tags: Optional[Any]
    TopicName: Optional[str]
    TopicArn: Optional[str]
    SignatureVersion: Optional[str]
    TracingConfig: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSnsTopic"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSnsTopic"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DisplayName=json_data.get("DisplayName"),
            KmsMasterKeyId=json_data.get("KmsMasterKeyId"),
            DataProtectionPolicy=json_data.get("DataProtectionPolicy"),
            Subscription=deserialize_list(json_data.get("Subscription"), Subscription),
            FifoTopic=json_data.get("FifoTopic"),
            ContentBasedDeduplication=json_data.get("ContentBasedDeduplication"),
            Tags=json_data.get("Tags"),
            TopicName=json_data.get("TopicName"),
            TopicArn=json_data.get("TopicArn"),
            SignatureVersion=json_data.get("SignatureVersion"),
            TracingConfig=json_data.get("TracingConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSnsTopic = AwsSnsTopic


@dataclass
class Subscription(BaseModel):
    Endpoint: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Subscription"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Subscription"]:
        if not json_data:
            return None
        return cls(
            Endpoint=json_data.get("Endpoint"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Subscription = Subscription


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


