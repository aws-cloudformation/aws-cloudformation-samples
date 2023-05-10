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
class AwsRdsOptiongroup(BaseModel):
    OptionGroupName: Optional[str]
    OptionGroupDescription: Optional[str]
    EngineName: Optional[str]
    MajorEngineVersion: Optional[str]
    OptionConfigurations: Optional[Sequence["_OptionConfiguration"]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRdsOptiongroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRdsOptiongroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            OptionGroupName=json_data.get("OptionGroupName"),
            OptionGroupDescription=json_data.get("OptionGroupDescription"),
            EngineName=json_data.get("EngineName"),
            MajorEngineVersion=json_data.get("MajorEngineVersion"),
            OptionConfigurations=deserialize_list(json_data.get("OptionConfigurations"), OptionConfiguration),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRdsOptiongroup = AwsRdsOptiongroup


@dataclass
class OptionConfiguration(BaseModel):
    DBSecurityGroupMemberships: Optional[AbstractSet[str]]
    OptionName: Optional[str]
    OptionSettings: Optional[Sequence["_OptionSetting"]]
    OptionVersion: Optional[str]
    Port: Optional[int]
    VpcSecurityGroupMemberships: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_OptionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionConfiguration"]:
        if not json_data:
            return None
        return cls(
            DBSecurityGroupMemberships=set_or_none(json_data.get("DBSecurityGroupMemberships")),
            OptionName=json_data.get("OptionName"),
            OptionSettings=deserialize_list(json_data.get("OptionSettings"), OptionSetting),
            OptionVersion=json_data.get("OptionVersion"),
            Port=json_data.get("Port"),
            VpcSecurityGroupMemberships=set_or_none(json_data.get("VpcSecurityGroupMemberships")),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionConfiguration = OptionConfiguration


@dataclass
class OptionSetting(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OptionSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionSetting"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionSetting = OptionSetting


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


