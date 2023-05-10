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
class AwsMediaconvertQueue(BaseModel):
    Status: Optional[str]
    Description: Optional[str]
    PricingPlan: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMediaconvertQueue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMediaconvertQueue"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Status=json_data.get("Status"),
            Description=json_data.get("Description"),
            PricingPlan=json_data.get("PricingPlan"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMediaconvertQueue = AwsMediaconvertQueue


