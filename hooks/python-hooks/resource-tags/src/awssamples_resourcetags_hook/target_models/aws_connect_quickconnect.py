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
class AwsConnectQuickconnect(BaseModel):
    InstanceArn: Optional[str]
    Name: Optional[str]
    Description: Optional[str]
    QuickConnectConfig: Optional["_QuickConnectConfig"]
    QuickConnectArn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConnectQuickconnect"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConnectQuickconnect"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            InstanceArn=json_data.get("InstanceArn"),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            QuickConnectConfig=QuickConnectConfig._deserialize(json_data.get("QuickConnectConfig")),
            QuickConnectArn=json_data.get("QuickConnectArn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConnectQuickconnect = AwsConnectQuickconnect


@dataclass
class QuickConnectConfig(BaseModel):
    QuickConnectType: Optional[str]
    PhoneConfig: Optional["_PhoneNumberQuickConnectConfig"]
    QueueConfig: Optional["_QueueQuickConnectConfig"]
    UserConfig: Optional["_UserQuickConnectConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_QuickConnectConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QuickConnectConfig"]:
        if not json_data:
            return None
        return cls(
            QuickConnectType=json_data.get("QuickConnectType"),
            PhoneConfig=PhoneNumberQuickConnectConfig._deserialize(json_data.get("PhoneConfig")),
            QueueConfig=QueueQuickConnectConfig._deserialize(json_data.get("QueueConfig")),
            UserConfig=UserQuickConnectConfig._deserialize(json_data.get("UserConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_QuickConnectConfig = QuickConnectConfig


@dataclass
class PhoneNumberQuickConnectConfig(BaseModel):
    PhoneNumber: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PhoneNumberQuickConnectConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PhoneNumberQuickConnectConfig"]:
        if not json_data:
            return None
        return cls(
            PhoneNumber=json_data.get("PhoneNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PhoneNumberQuickConnectConfig = PhoneNumberQuickConnectConfig


@dataclass
class QueueQuickConnectConfig(BaseModel):
    ContactFlowArn: Optional[str]
    QueueArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QueueQuickConnectConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueueQuickConnectConfig"]:
        if not json_data:
            return None
        return cls(
            ContactFlowArn=json_data.get("ContactFlowArn"),
            QueueArn=json_data.get("QueueArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueueQuickConnectConfig = QueueQuickConnectConfig


@dataclass
class UserQuickConnectConfig(BaseModel):
    ContactFlowArn: Optional[str]
    UserArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserQuickConnectConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserQuickConnectConfig"]:
        if not json_data:
            return None
        return cls(
            ContactFlowArn=json_data.get("ContactFlowArn"),
            UserArn=json_data.get("UserArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserQuickConnectConfig = UserQuickConnectConfig


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


