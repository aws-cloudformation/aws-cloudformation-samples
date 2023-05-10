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
class AwsConnectPhonenumber(BaseModel):
    TargetArn: Optional[str]
    PhoneNumberArn: Optional[str]
    Description: Optional[str]
    Type: Optional[str]
    CountryCode: Optional[str]
    Prefix: Optional[str]
    Address: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConnectPhonenumber"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConnectPhonenumber"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            TargetArn=json_data.get("TargetArn"),
            PhoneNumberArn=json_data.get("PhoneNumberArn"),
            Description=json_data.get("Description"),
            Type=json_data.get("Type"),
            CountryCode=json_data.get("CountryCode"),
            Prefix=json_data.get("Prefix"),
            Address=json_data.get("Address"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConnectPhonenumber = AwsConnectPhonenumber


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


