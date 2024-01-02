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
class AwsB2biPartnership(BaseModel):
    Capabilities: Optional[Sequence[str]]
    CreatedAt: Optional[str]
    Email: Optional[str]
    ModifiedAt: Optional[str]
    Name: Optional[str]
    PartnershipArn: Optional[str]
    PartnershipId: Optional[str]
    Phone: Optional[str]
    ProfileId: Optional[str]
    Tags: Optional[Any]
    TradingPartnerId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsB2biPartnership"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsB2biPartnership"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Capabilities=json_data.get("Capabilities"),
            CreatedAt=json_data.get("CreatedAt"),
            Email=json_data.get("Email"),
            ModifiedAt=json_data.get("ModifiedAt"),
            Name=json_data.get("Name"),
            PartnershipArn=json_data.get("PartnershipArn"),
            PartnershipId=json_data.get("PartnershipId"),
            Phone=json_data.get("Phone"),
            ProfileId=json_data.get("ProfileId"),
            Tags=json_data.get("Tags"),
            TradingPartnerId=json_data.get("TradingPartnerId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsB2biPartnership = AwsB2biPartnership


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


