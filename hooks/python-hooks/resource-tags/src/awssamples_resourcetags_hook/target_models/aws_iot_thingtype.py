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
class AwsIotThingtype(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]
    ThingTypeName: Optional[str]
    DeprecateThingType: Optional[bool]
    ThingTypeProperties: Optional["_ThingTypeProperties"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotThingtype"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotThingtype"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            ThingTypeName=json_data.get("ThingTypeName"),
            DeprecateThingType=json_data.get("DeprecateThingType"),
            ThingTypeProperties=ThingTypeProperties._deserialize(json_data.get("ThingTypeProperties")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotThingtype = AwsIotThingtype


@dataclass
class ThingTypeProperties(BaseModel):
    SearchableAttributes: Optional[Sequence[str]]
    ThingTypeDescription: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThingTypeProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThingTypeProperties"]:
        if not json_data:
            return None
        return cls(
            SearchableAttributes=json_data.get("SearchableAttributes"),
            ThingTypeDescription=json_data.get("ThingTypeDescription"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThingTypeProperties = ThingTypeProperties


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


