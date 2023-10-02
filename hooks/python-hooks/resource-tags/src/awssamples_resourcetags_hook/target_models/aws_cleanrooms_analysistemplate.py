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
class AwsCleanroomsAnalysistemplate(BaseModel):
    Arn: Optional[str]
    CollaborationArn: Optional[str]
    CollaborationIdentifier: Optional[str]
    Tags: Optional[Any]
    AnalysisParameters: Optional[Sequence["_AnalysisParameter"]]
    AnalysisTemplateIdentifier: Optional[str]
    Description: Optional[str]
    MembershipArn: Optional[str]
    MembershipIdentifier: Optional[str]
    Name: Optional[str]
    Schema: Optional["_AnalysisSchema"]
    Source: Optional["_AnalysisSource"]
    Format: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCleanroomsAnalysistemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCleanroomsAnalysistemplate"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            CollaborationArn=json_data.get("CollaborationArn"),
            CollaborationIdentifier=json_data.get("CollaborationIdentifier"),
            Tags=json_data.get("Tags"),
            AnalysisParameters=deserialize_list(json_data.get("AnalysisParameters"), AnalysisParameter),
            AnalysisTemplateIdentifier=json_data.get("AnalysisTemplateIdentifier"),
            Description=json_data.get("Description"),
            MembershipArn=json_data.get("MembershipArn"),
            MembershipIdentifier=json_data.get("MembershipIdentifier"),
            Name=json_data.get("Name"),
            Schema=AnalysisSchema._deserialize(json_data.get("Schema")),
            Source=AnalysisSource._deserialize(json_data.get("Source")),
            Format=json_data.get("Format"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCleanroomsAnalysistemplate = AwsCleanroomsAnalysistemplate


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
class AnalysisParameter(BaseModel):
    DefaultValue: Optional[str]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnalysisParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnalysisParameter"]:
        if not json_data:
            return None
        return cls(
            DefaultValue=json_data.get("DefaultValue"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnalysisParameter = AnalysisParameter


@dataclass
class AnalysisSchema(BaseModel):
    ReferencedTables: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AnalysisSchema"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnalysisSchema"]:
        if not json_data:
            return None
        return cls(
            ReferencedTables=json_data.get("ReferencedTables"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnalysisSchema = AnalysisSchema


@dataclass
class AnalysisSource(BaseModel):
    Text: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnalysisSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnalysisSource"]:
        if not json_data:
            return None
        return cls(
            Text=json_data.get("Text"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnalysisSource = AnalysisSource


