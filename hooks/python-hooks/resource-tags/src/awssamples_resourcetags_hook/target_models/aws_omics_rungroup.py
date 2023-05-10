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
class AwsOmicsRungroup(BaseModel):
    Arn: Optional[str]
    CreationTime: Optional[str]
    Id: Optional[str]
    MaxCpus: Optional[float]
    MaxDuration: Optional[float]
    MaxRuns: Optional[float]
    Name: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsOmicsRungroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsOmicsRungroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            CreationTime=json_data.get("CreationTime"),
            Id=json_data.get("Id"),
            MaxCpus=json_data.get("MaxCpus"),
            MaxDuration=json_data.get("MaxDuration"),
            MaxRuns=json_data.get("MaxRuns"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsOmicsRungroup = AwsOmicsRungroup


