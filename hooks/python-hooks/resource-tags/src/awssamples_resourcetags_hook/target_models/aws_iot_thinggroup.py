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
class AwsIotThinggroup(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]
    ThingGroupName: Optional[str]
    ParentGroupName: Optional[str]
    QueryString: Optional[str]
    ThingGroupProperties: Optional["_ThingGroupProperties"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotThinggroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotThinggroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            ThingGroupName=json_data.get("ThingGroupName"),
            ParentGroupName=json_data.get("ParentGroupName"),
            QueryString=json_data.get("QueryString"),
            ThingGroupProperties=ThingGroupProperties._deserialize(json_data.get("ThingGroupProperties")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotThinggroup = AwsIotThinggroup


@dataclass
class ThingGroupProperties(BaseModel):
    AttributePayload: Optional["_AttributePayload"]
    ThingGroupDescription: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThingGroupProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThingGroupProperties"]:
        if not json_data:
            return None
        return cls(
            AttributePayload=AttributePayload._deserialize(json_data.get("AttributePayload")),
            ThingGroupDescription=json_data.get("ThingGroupDescription"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThingGroupProperties = ThingGroupProperties


@dataclass
class AttributePayload(BaseModel):
    Attributes: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_AttributePayload"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributePayload"]:
        if not json_data:
            return None
        return cls(
            Attributes=json_data.get("Attributes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributePayload = AttributePayload


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


