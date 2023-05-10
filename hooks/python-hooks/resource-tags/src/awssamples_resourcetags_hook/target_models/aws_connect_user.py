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
class AwsConnectUser(BaseModel):
    InstanceArn: Optional[str]
    DirectoryUserId: Optional[str]
    HierarchyGroupArn: Optional[str]
    Username: Optional[str]
    Password: Optional[str]
    RoutingProfileArn: Optional[str]
    IdentityInfo: Optional["_UserIdentityInfo"]
    PhoneConfig: Optional["_UserPhoneConfig"]
    SecurityProfileArns: Optional[AbstractSet[str]]
    UserArn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConnectUser"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConnectUser"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            InstanceArn=json_data.get("InstanceArn"),
            DirectoryUserId=json_data.get("DirectoryUserId"),
            HierarchyGroupArn=json_data.get("HierarchyGroupArn"),
            Username=json_data.get("Username"),
            Password=json_data.get("Password"),
            RoutingProfileArn=json_data.get("RoutingProfileArn"),
            IdentityInfo=UserIdentityInfo._deserialize(json_data.get("IdentityInfo")),
            PhoneConfig=UserPhoneConfig._deserialize(json_data.get("PhoneConfig")),
            SecurityProfileArns=set_or_none(json_data.get("SecurityProfileArns")),
            UserArn=json_data.get("UserArn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConnectUser = AwsConnectUser


@dataclass
class UserIdentityInfo(BaseModel):
    FirstName: Optional[str]
    LastName: Optional[str]
    Email: Optional[str]
    SecondaryEmail: Optional[str]
    Mobile: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserIdentityInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserIdentityInfo"]:
        if not json_data:
            return None
        return cls(
            FirstName=json_data.get("FirstName"),
            LastName=json_data.get("LastName"),
            Email=json_data.get("Email"),
            SecondaryEmail=json_data.get("SecondaryEmail"),
            Mobile=json_data.get("Mobile"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserIdentityInfo = UserIdentityInfo


@dataclass
class UserPhoneConfig(BaseModel):
    AfterContactWorkTimeLimit: Optional[int]
    AutoAccept: Optional[bool]
    DeskPhoneNumber: Optional[str]
    PhoneType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserPhoneConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserPhoneConfig"]:
        if not json_data:
            return None
        return cls(
            AfterContactWorkTimeLimit=json_data.get("AfterContactWorkTimeLimit"),
            AutoAccept=json_data.get("AutoAccept"),
            DeskPhoneNumber=json_data.get("DeskPhoneNumber"),
            PhoneType=json_data.get("PhoneType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserPhoneConfig = UserPhoneConfig


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


