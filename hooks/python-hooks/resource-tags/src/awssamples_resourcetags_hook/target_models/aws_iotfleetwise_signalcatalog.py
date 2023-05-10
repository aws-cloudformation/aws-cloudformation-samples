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
class AwsIotfleetwiseSignalcatalog(BaseModel):
    Arn: Optional[str]
    CreationTime: Optional[str]
    Description: Optional[str]
    LastModificationTime: Optional[str]
    Name: Optional[str]
    NodeCounts: Optional["_NodeCounts"]
    Nodes: Optional[AbstractSet["_Node"]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotfleetwiseSignalcatalog"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotfleetwiseSignalcatalog"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            CreationTime=json_data.get("CreationTime"),
            Description=json_data.get("Description"),
            LastModificationTime=json_data.get("LastModificationTime"),
            Name=json_data.get("Name"),
            NodeCounts=NodeCounts._deserialize(json_data.get("NodeCounts")),
            Nodes=set_or_none(json_data.get("Nodes")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotfleetwiseSignalcatalog = AwsIotfleetwiseSignalcatalog


@dataclass
class NodeCounts(BaseModel):
    TotalNodes: Optional[float]
    TotalBranches: Optional[float]
    TotalSensors: Optional[float]
    TotalAttributes: Optional[float]
    TotalActuators: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NodeCounts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeCounts"]:
        if not json_data:
            return None
        return cls(
            TotalNodes=json_data.get("TotalNodes"),
            TotalBranches=json_data.get("TotalBranches"),
            TotalSensors=json_data.get("TotalSensors"),
            TotalAttributes=json_data.get("TotalAttributes"),
            TotalActuators=json_data.get("TotalActuators"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeCounts = NodeCounts


@dataclass
class Node(BaseModel):
    Branch: Optional["_Branch"]
    Sensor: Optional["_Sensor"]
    Actuator: Optional["_Actuator"]
    Attribute: Optional["_Attribute"]

    @classmethod
    def _deserialize(
        cls: Type["_Node"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Node"]:
        if not json_data:
            return None
        return cls(
            Branch=Branch._deserialize(json_data.get("Branch")),
            Sensor=Sensor._deserialize(json_data.get("Sensor")),
            Actuator=Actuator._deserialize(json_data.get("Actuator")),
            Attribute=Attribute._deserialize(json_data.get("Attribute")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Node = Node


@dataclass
class Branch(BaseModel):
    FullyQualifiedName: Optional[str]
    Description: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Branch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Branch"]:
        if not json_data:
            return None
        return cls(
            FullyQualifiedName=json_data.get("FullyQualifiedName"),
            Description=json_data.get("Description"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Branch = Branch


@dataclass
class Sensor(BaseModel):
    FullyQualifiedName: Optional[str]
    DataType: Optional[str]
    Description: Optional[str]
    Unit: Optional[str]
    AllowedValues: Optional[Sequence[str]]
    Min: Optional[float]
    Max: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Sensor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sensor"]:
        if not json_data:
            return None
        return cls(
            FullyQualifiedName=json_data.get("FullyQualifiedName"),
            DataType=json_data.get("DataType"),
            Description=json_data.get("Description"),
            Unit=json_data.get("Unit"),
            AllowedValues=json_data.get("AllowedValues"),
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sensor = Sensor


@dataclass
class Actuator(BaseModel):
    FullyQualifiedName: Optional[str]
    DataType: Optional[str]
    Description: Optional[str]
    Unit: Optional[str]
    AllowedValues: Optional[Sequence[str]]
    Min: Optional[float]
    Max: Optional[float]
    AssignedValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Actuator"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Actuator"]:
        if not json_data:
            return None
        return cls(
            FullyQualifiedName=json_data.get("FullyQualifiedName"),
            DataType=json_data.get("DataType"),
            Description=json_data.get("Description"),
            Unit=json_data.get("Unit"),
            AllowedValues=json_data.get("AllowedValues"),
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
            AssignedValue=json_data.get("AssignedValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Actuator = Actuator


@dataclass
class Attribute(BaseModel):
    FullyQualifiedName: Optional[str]
    DataType: Optional[str]
    Description: Optional[str]
    Unit: Optional[str]
    AllowedValues: Optional[Sequence[str]]
    Min: Optional[float]
    Max: Optional[float]
    AssignedValue: Optional[str]
    DefaultValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Attribute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Attribute"]:
        if not json_data:
            return None
        return cls(
            FullyQualifiedName=json_data.get("FullyQualifiedName"),
            DataType=json_data.get("DataType"),
            Description=json_data.get("Description"),
            Unit=json_data.get("Unit"),
            AllowedValues=json_data.get("AllowedValues"),
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
            AssignedValue=json_data.get("AssignedValue"),
            DefaultValue=json_data.get("DefaultValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Attribute = Attribute


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


