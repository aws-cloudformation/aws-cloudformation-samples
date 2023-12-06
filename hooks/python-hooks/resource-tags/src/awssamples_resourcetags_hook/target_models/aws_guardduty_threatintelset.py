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
class AwsGuarddutyThreatintelset(BaseModel):
    Id: Optional[str]
    Format: Optional[str]
    Activate: Optional[bool]
    DetectorId: Optional[str]
    Name: Optional[str]
    Location: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGuarddutyThreatintelset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGuarddutyThreatintelset"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Format=json_data.get("Format"),
            Activate=json_data.get("Activate"),
            DetectorId=json_data.get("DetectorId"),
            Name=json_data.get("Name"),
            Location=json_data.get("Location"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGuarddutyThreatintelset = AwsGuarddutyThreatintelset


@dataclass
class TagItem(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagItem"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagItem = TagItem


