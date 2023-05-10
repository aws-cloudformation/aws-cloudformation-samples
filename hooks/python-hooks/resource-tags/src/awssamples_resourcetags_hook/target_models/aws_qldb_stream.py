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
class AwsQldbStream(BaseModel):
    LedgerName: Optional[str]
    StreamName: Optional[str]
    RoleArn: Optional[str]
    InclusiveStartTime: Optional[str]
    ExclusiveEndTime: Optional[str]
    KinesisConfiguration: Optional["_KinesisConfiguration"]
    Tags: Optional[Any]
    Arn: Optional[str]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsQldbStream"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsQldbStream"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            LedgerName=json_data.get("LedgerName"),
            StreamName=json_data.get("StreamName"),
            RoleArn=json_data.get("RoleArn"),
            InclusiveStartTime=json_data.get("InclusiveStartTime"),
            ExclusiveEndTime=json_data.get("ExclusiveEndTime"),
            KinesisConfiguration=KinesisConfiguration._deserialize(json_data.get("KinesisConfiguration")),
            Tags=json_data.get("Tags"),
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsQldbStream = AwsQldbStream


@dataclass
class KinesisConfiguration(BaseModel):
    StreamArn: Optional[str]
    AggregationEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisConfiguration"]:
        if not json_data:
            return None
        return cls(
            StreamArn=json_data.get("StreamArn"),
            AggregationEnabled=json_data.get("AggregationEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisConfiguration = KinesisConfiguration


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


