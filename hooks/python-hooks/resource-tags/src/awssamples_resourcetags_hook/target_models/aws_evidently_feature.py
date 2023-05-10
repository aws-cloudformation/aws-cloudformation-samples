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
class AwsEvidentlyFeature(BaseModel):
    Arn: Optional[str]
    Project: Optional[str]
    Name: Optional[str]
    Description: Optional[str]
    EvaluationStrategy: Optional[str]
    Variations: Optional[Sequence["_VariationObject"]]
    DefaultVariation: Optional[str]
    EntityOverrides: Optional[AbstractSet["_EntityOverride"]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEvidentlyFeature"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEvidentlyFeature"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Project=json_data.get("Project"),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            EvaluationStrategy=json_data.get("EvaluationStrategy"),
            Variations=deserialize_list(json_data.get("Variations"), VariationObject),
            DefaultVariation=json_data.get("DefaultVariation"),
            EntityOverrides=set_or_none(json_data.get("EntityOverrides")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEvidentlyFeature = AwsEvidentlyFeature


@dataclass
class VariationObject(BaseModel):
    VariationName: Optional[str]
    BooleanValue: Optional[bool]
    StringValue: Optional[str]
    LongValue: Optional[float]
    DoubleValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VariationObject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VariationObject"]:
        if not json_data:
            return None
        return cls(
            VariationName=json_data.get("VariationName"),
            BooleanValue=json_data.get("BooleanValue"),
            StringValue=json_data.get("StringValue"),
            LongValue=json_data.get("LongValue"),
            DoubleValue=json_data.get("DoubleValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VariationObject = VariationObject


@dataclass
class EntityOverride(BaseModel):
    EntityId: Optional[str]
    Variation: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EntityOverride"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntityOverride"]:
        if not json_data:
            return None
        return cls(
            EntityId=json_data.get("EntityId"),
            Variation=json_data.get("Variation"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntityOverride = EntityOverride


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


