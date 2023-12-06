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
class AwsS3Accessgrantslocation(BaseModel):
    AccessGrantsLocationArn: Optional[str]
    AccessGrantsLocationId: Optional[str]
    IamRoleArn: Optional[str]
    LocationScope: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsS3Accessgrantslocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsS3Accessgrantslocation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AccessGrantsLocationArn=json_data.get("AccessGrantsLocationArn"),
            AccessGrantsLocationId=json_data.get("AccessGrantsLocationId"),
            IamRoleArn=json_data.get("IamRoleArn"),
            LocationScope=json_data.get("LocationScope"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsS3Accessgrantslocation = AwsS3Accessgrantslocation


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


