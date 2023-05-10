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
class AwsPinpointemailIdentity(BaseModel):
    Id: Optional[str]
    IdentityDNSRecordName3: Optional[str]
    IdentityDNSRecordName1: Optional[str]
    IdentityDNSRecordName2: Optional[str]
    IdentityDNSRecordValue3: Optional[str]
    IdentityDNSRecordValue2: Optional[str]
    IdentityDNSRecordValue1: Optional[str]
    FeedbackForwardingEnabled: Optional[bool]
    DkimSigningEnabled: Optional[bool]
    Tags: Optional[Any]
    Name: Optional[str]
    MailFromAttributes: Optional["_MailFromAttributes"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsPinpointemailIdentity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsPinpointemailIdentity"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            IdentityDNSRecordName3=json_data.get("IdentityDNSRecordName3"),
            IdentityDNSRecordName1=json_data.get("IdentityDNSRecordName1"),
            IdentityDNSRecordName2=json_data.get("IdentityDNSRecordName2"),
            IdentityDNSRecordValue3=json_data.get("IdentityDNSRecordValue3"),
            IdentityDNSRecordValue2=json_data.get("IdentityDNSRecordValue2"),
            IdentityDNSRecordValue1=json_data.get("IdentityDNSRecordValue1"),
            FeedbackForwardingEnabled=json_data.get("FeedbackForwardingEnabled"),
            DkimSigningEnabled=json_data.get("DkimSigningEnabled"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
            MailFromAttributes=MailFromAttributes._deserialize(json_data.get("MailFromAttributes")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsPinpointemailIdentity = AwsPinpointemailIdentity


@dataclass
class Tags(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class MailFromAttributes(BaseModel):
    MailFromDomain: Optional[str]
    BehaviorOnMxFailure: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MailFromAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MailFromAttributes"]:
        if not json_data:
            return None
        return cls(
            MailFromDomain=json_data.get("MailFromDomain"),
            BehaviorOnMxFailure=json_data.get("BehaviorOnMxFailure"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MailFromAttributes = MailFromAttributes


