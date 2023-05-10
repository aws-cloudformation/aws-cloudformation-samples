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
class AwsSagemakerWorkteam(BaseModel):
    Description: Optional[str]
    NotificationConfiguration: Optional["_NotificationConfiguration"]
    WorkteamName: Optional[str]
    MemberDefinitions: Optional[Sequence["_MemberDefinition"]]
    Id: Optional[str]
    WorkforceName: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSagemakerWorkteam"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSagemakerWorkteam"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            NotificationConfiguration=NotificationConfiguration._deserialize(json_data.get("NotificationConfiguration")),
            WorkteamName=json_data.get("WorkteamName"),
            MemberDefinitions=deserialize_list(json_data.get("MemberDefinitions"), MemberDefinition),
            Id=json_data.get("Id"),
            WorkforceName=json_data.get("WorkforceName"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSagemakerWorkteam = AwsSagemakerWorkteam


@dataclass
class NotificationConfiguration(BaseModel):
    NotificationTopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationConfiguration"]:
        if not json_data:
            return None
        return cls(
            NotificationTopicArn=json_data.get("NotificationTopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationConfiguration = NotificationConfiguration


@dataclass
class MemberDefinition(BaseModel):
    CognitoMemberDefinition: Optional["_CognitoMemberDefinition"]
    OidcMemberDefinition: Optional["_OidcMemberDefinition"]

    @classmethod
    def _deserialize(
        cls: Type["_MemberDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemberDefinition"]:
        if not json_data:
            return None
        return cls(
            CognitoMemberDefinition=CognitoMemberDefinition._deserialize(json_data.get("CognitoMemberDefinition")),
            OidcMemberDefinition=OidcMemberDefinition._deserialize(json_data.get("OidcMemberDefinition")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemberDefinition = MemberDefinition


@dataclass
class CognitoMemberDefinition(BaseModel):
    CognitoUserGroup: Optional[str]
    CognitoUserPool: Optional[str]
    CognitoClientId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CognitoMemberDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CognitoMemberDefinition"]:
        if not json_data:
            return None
        return cls(
            CognitoUserGroup=json_data.get("CognitoUserGroup"),
            CognitoUserPool=json_data.get("CognitoUserPool"),
            CognitoClientId=json_data.get("CognitoClientId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CognitoMemberDefinition = CognitoMemberDefinition


@dataclass
class OidcMemberDefinition(BaseModel):
    OidcGroups: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_OidcMemberDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OidcMemberDefinition"]:
        if not json_data:
            return None
        return cls(
            OidcGroups=json_data.get("OidcGroups"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OidcMemberDefinition = OidcMemberDefinition


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


