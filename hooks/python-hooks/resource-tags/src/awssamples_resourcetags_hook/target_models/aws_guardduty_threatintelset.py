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
    Format: Optional[str]
    Activate: Optional[bool]
    DetectorId: Optional[str]
    Id: Optional[str]
    Tags: Optional[Any]
    Name: Optional[str]
    Location: Optional[str]

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
            Format=json_data.get("Format"),
            Activate=json_data.get("Activate"),
            DetectorId=json_data.get("DetectorId"),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
            Location=json_data.get("Location"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGuarddutyThreatintelset = AwsGuarddutyThreatintelset


@dataclass
class Tag(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


