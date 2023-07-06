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
class AwsCleanroomsConfiguredtable(BaseModel):
    Arn: Optional[str]
    Tags: Optional[Any]
    AllowedColumns: Optional[Sequence[str]]
    AnalysisMethod: Optional[str]
    ConfiguredTableIdentifier: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    AnalysisRules: Optional[Sequence["_AnalysisRule"]]
    TableReference: Optional["_TableReference"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCleanroomsConfiguredtable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCleanroomsConfiguredtable"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
            AllowedColumns=json_data.get("AllowedColumns"),
            AnalysisMethod=json_data.get("AnalysisMethod"),
            ConfiguredTableIdentifier=json_data.get("ConfiguredTableIdentifier"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            AnalysisRules=deserialize_list(json_data.get("AnalysisRules"), AnalysisRule),
            TableReference=TableReference._deserialize(json_data.get("TableReference")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCleanroomsConfiguredtable = AwsCleanroomsConfiguredtable


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
class AnalysisRule(BaseModel):
    Type: Optional[str]
    Policy: Optional["_ConfiguredTableAnalysisRulePolicy"]

    @classmethod
    def _deserialize(
        cls: Type["_AnalysisRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnalysisRule"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Policy=ConfiguredTableAnalysisRulePolicy._deserialize(json_data.get("Policy")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnalysisRule = AnalysisRule


@dataclass
class ConfiguredTableAnalysisRulePolicy(BaseModel):
    V1: Optional["_ConfiguredTableAnalysisRulePolicyV1"]

    @classmethod
    def _deserialize(
        cls: Type["_ConfiguredTableAnalysisRulePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfiguredTableAnalysisRulePolicy"]:
        if not json_data:
            return None
        return cls(
            V1=ConfiguredTableAnalysisRulePolicyV1._deserialize(json_data.get("V1")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfiguredTableAnalysisRulePolicy = ConfiguredTableAnalysisRulePolicy


@dataclass
class ConfiguredTableAnalysisRulePolicyV1(BaseModel):
    List: Optional["_AnalysisRuleList"]
    Aggregation: Optional["_AnalysisRuleAggregation"]

    @classmethod
    def _deserialize(
        cls: Type["_ConfiguredTableAnalysisRulePolicyV1"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfiguredTableAnalysisRulePolicyV1"]:
        if not json_data:
            return None
        return cls(
            List=AnalysisRuleList._deserialize(json_data.get("List")),
            Aggregation=AnalysisRuleAggregation._deserialize(json_data.get("Aggregation")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfiguredTableAnalysisRulePolicyV1 = ConfiguredTableAnalysisRulePolicyV1


@dataclass
class AnalysisRuleList(BaseModel):
    JoinColumns: Optional[Sequence[str]]
    ListColumns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AnalysisRuleList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnalysisRuleList"]:
        if not json_data:
            return None
        return cls(
            JoinColumns=json_data.get("JoinColumns"),
            ListColumns=json_data.get("ListColumns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnalysisRuleList = AnalysisRuleList


@dataclass
class AnalysisRuleAggregation(BaseModel):
    AggregateColumns: Optional[Sequence["_AggregateColumn"]]
    JoinColumns: Optional[Sequence[str]]
    JoinRequired: Optional[str]
    DimensionColumns: Optional[Sequence[str]]
    ScalarFunctions: Optional[Sequence[str]]
    OutputConstraints: Optional[Sequence["_AggregationConstraint"]]

    @classmethod
    def _deserialize(
        cls: Type["_AnalysisRuleAggregation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnalysisRuleAggregation"]:
        if not json_data:
            return None
        return cls(
            AggregateColumns=deserialize_list(json_data.get("AggregateColumns"), AggregateColumn),
            JoinColumns=json_data.get("JoinColumns"),
            JoinRequired=json_data.get("JoinRequired"),
            DimensionColumns=json_data.get("DimensionColumns"),
            ScalarFunctions=json_data.get("ScalarFunctions"),
            OutputConstraints=deserialize_list(json_data.get("OutputConstraints"), AggregationConstraint),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnalysisRuleAggregation = AnalysisRuleAggregation


@dataclass
class AggregateColumn(BaseModel):
    ColumnNames: Optional[Sequence[str]]
    Function: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AggregateColumn"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AggregateColumn"]:
        if not json_data:
            return None
        return cls(
            ColumnNames=json_data.get("ColumnNames"),
            Function=json_data.get("Function"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AggregateColumn = AggregateColumn


@dataclass
class AggregationConstraint(BaseModel):
    ColumnName: Optional[str]
    Minimum: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AggregationConstraint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AggregationConstraint"]:
        if not json_data:
            return None
        return cls(
            ColumnName=json_data.get("ColumnName"),
            Minimum=json_data.get("Minimum"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AggregationConstraint = AggregationConstraint


@dataclass
class TableReference(BaseModel):
    Glue: Optional["_GlueTableReference"]

    @classmethod
    def _deserialize(
        cls: Type["_TableReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableReference"]:
        if not json_data:
            return None
        return cls(
            Glue=GlueTableReference._deserialize(json_data.get("Glue")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableReference = TableReference


@dataclass
class GlueTableReference(BaseModel):
    TableName: Optional[str]
    DatabaseName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GlueTableReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlueTableReference"]:
        if not json_data:
            return None
        return cls(
            TableName=json_data.get("TableName"),
            DatabaseName=json_data.get("DatabaseName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlueTableReference = GlueTableReference


