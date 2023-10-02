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
class AwsEntityresolutionMatchingworkflow(BaseModel):
    WorkflowName: Optional[str]
    Description: Optional[str]
    InputSourceConfig: Optional[Sequence["_InputSource"]]
    OutputSourceConfig: Optional[Sequence["_OutputSource"]]
    ResolutionTechniques: Optional["_ResolutionTechniques"]
    RoleArn: Optional[str]
    Tags: Optional[Any]
    WorkflowArn: Optional[str]
    CreatedAt: Optional[str]
    UpdatedAt: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEntityresolutionMatchingworkflow"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEntityresolutionMatchingworkflow"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            WorkflowName=json_data.get("WorkflowName"),
            Description=json_data.get("Description"),
            InputSourceConfig=deserialize_list(json_data.get("InputSourceConfig"), InputSource),
            OutputSourceConfig=deserialize_list(json_data.get("OutputSourceConfig"), OutputSource),
            ResolutionTechniques=ResolutionTechniques._deserialize(json_data.get("ResolutionTechniques")),
            RoleArn=json_data.get("RoleArn"),
            Tags=json_data.get("Tags"),
            WorkflowArn=json_data.get("WorkflowArn"),
            CreatedAt=json_data.get("CreatedAt"),
            UpdatedAt=json_data.get("UpdatedAt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEntityresolutionMatchingworkflow = AwsEntityresolutionMatchingworkflow


@dataclass
class InputSource(BaseModel):
    InputSourceARN: Optional[str]
    SchemaArn: Optional[str]
    ApplyNormalization: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_InputSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputSource"]:
        if not json_data:
            return None
        return cls(
            InputSourceARN=json_data.get("InputSourceARN"),
            SchemaArn=json_data.get("SchemaArn"),
            ApplyNormalization=json_data.get("ApplyNormalization"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputSource = InputSource


@dataclass
class OutputSource(BaseModel):
    OutputS3Path: Optional[str]
    Output: Optional[Sequence["_OutputAttribute"]]
    KMSArn: Optional[str]
    ApplyNormalization: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_OutputSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputSource"]:
        if not json_data:
            return None
        return cls(
            OutputS3Path=json_data.get("OutputS3Path"),
            Output=deserialize_list(json_data.get("Output"), OutputAttribute),
            KMSArn=json_data.get("KMSArn"),
            ApplyNormalization=json_data.get("ApplyNormalization"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputSource = OutputSource


@dataclass
class OutputAttribute(BaseModel):
    Name: Optional[str]
    Hashed: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_OutputAttribute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputAttribute"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Hashed=json_data.get("Hashed"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputAttribute = OutputAttribute


@dataclass
class ResolutionTechniques(BaseModel):
    ResolutionType: Optional[str]
    RuleBasedProperties: Optional["_RuleBasedProperties"]

    @classmethod
    def _deserialize(
        cls: Type["_ResolutionTechniques"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResolutionTechniques"]:
        if not json_data:
            return None
        return cls(
            ResolutionType=json_data.get("ResolutionType"),
            RuleBasedProperties=RuleBasedProperties._deserialize(json_data.get("RuleBasedProperties")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResolutionTechniques = ResolutionTechniques


@dataclass
class RuleBasedProperties(BaseModel):
    Rules: Optional[Sequence["_Rule"]]
    AttributeMatchingModel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RuleBasedProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleBasedProperties"]:
        if not json_data:
            return None
        return cls(
            Rules=deserialize_list(json_data.get("Rules"), Rule),
            AttributeMatchingModel=json_data.get("AttributeMatchingModel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleBasedProperties = RuleBasedProperties


@dataclass
class Rule(BaseModel):
    RuleName: Optional[str]
    MatchingKeys: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            RuleName=json_data.get("RuleName"),
            MatchingKeys=json_data.get("MatchingKeys"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


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


