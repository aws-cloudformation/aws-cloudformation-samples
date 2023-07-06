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
class AwsAthenaCapacityreservation(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    Status: Optional[str]
    TargetDpus: Optional[int]
    AllocatedDpus: Optional[int]
    CapacityAssignmentConfiguration: Optional["_CapacityAssignmentConfiguration"]
    CreationTime: Optional[str]
    LastSuccessfulAllocationTime: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAthenaCapacityreservation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAthenaCapacityreservation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            TargetDpus=json_data.get("TargetDpus"),
            AllocatedDpus=json_data.get("AllocatedDpus"),
            CapacityAssignmentConfiguration=CapacityAssignmentConfiguration._deserialize(json_data.get("CapacityAssignmentConfiguration")),
            CreationTime=json_data.get("CreationTime"),
            LastSuccessfulAllocationTime=json_data.get("LastSuccessfulAllocationTime"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAthenaCapacityreservation = AwsAthenaCapacityreservation


@dataclass
class CapacityAssignmentConfiguration(BaseModel):
    CapacityAssignments: Optional[Sequence["_CapacityAssignment"]]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityAssignmentConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityAssignmentConfiguration"]:
        if not json_data:
            return None
        return cls(
            CapacityAssignments=deserialize_list(json_data.get("CapacityAssignments"), CapacityAssignment),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityAssignmentConfiguration = CapacityAssignmentConfiguration


@dataclass
class CapacityAssignment(BaseModel):
    WorkgroupNames: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityAssignment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityAssignment"]:
        if not json_data:
            return None
        return cls(
            WorkgroupNames=json_data.get("WorkgroupNames"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityAssignment = CapacityAssignment


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


