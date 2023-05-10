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
class AwsSsmParameter(BaseModel):
    Type: Optional[str]
    Description: Optional[str]
    Policies: Optional[str]
    AllowedPattern: Optional[str]
    Tier: Optional[str]
    Value: Optional[str]
    DataType: Optional[str]
    Id: Optional[str]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSsmParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSsmParameter"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Type=json_data.get("Type"),
            Description=json_data.get("Description"),
            Policies=json_data.get("Policies"),
            AllowedPattern=json_data.get("AllowedPattern"),
            Tier=json_data.get("Tier"),
            Value=json_data.get("Value"),
            DataType=json_data.get("DataType"),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSsmParameter = AwsSsmParameter


