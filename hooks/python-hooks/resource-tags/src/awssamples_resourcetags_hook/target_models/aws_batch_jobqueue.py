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
class AwsBatchJobqueue(BaseModel):
    JobQueueName: Optional[str]
    JobQueueArn: Optional[str]
    ComputeEnvironmentOrder: Optional[Sequence["_ComputeEnvironmentOrder"]]
    Priority: Optional[int]
    State: Optional[str]
    SchedulingPolicyArn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsBatchJobqueue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsBatchJobqueue"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            JobQueueName=json_data.get("JobQueueName"),
            JobQueueArn=json_data.get("JobQueueArn"),
            ComputeEnvironmentOrder=deserialize_list(json_data.get("ComputeEnvironmentOrder"), ComputeEnvironmentOrder),
            Priority=json_data.get("Priority"),
            State=json_data.get("State"),
            SchedulingPolicyArn=json_data.get("SchedulingPolicyArn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsBatchJobqueue = AwsBatchJobqueue


@dataclass
class ComputeEnvironmentOrder(BaseModel):
    ComputeEnvironment: Optional[str]
    Order: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ComputeEnvironmentOrder"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComputeEnvironmentOrder"]:
        if not json_data:
            return None
        return cls(
            ComputeEnvironment=json_data.get("ComputeEnvironment"),
            Order=json_data.get("Order"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComputeEnvironmentOrder = ComputeEnvironmentOrder


