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
class AwsPinpointPushtemplate(BaseModel):
    GCM: Optional["_AndroidPushNotificationTemplate"]
    Baidu: Optional["_AndroidPushNotificationTemplate"]
    TemplateName: Optional[str]
    ADM: Optional["_AndroidPushNotificationTemplate"]
    APNS: Optional["_APNSPushNotificationTemplate"]
    TemplateDescription: Optional[str]
    DefaultSubstitutions: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    Default: Optional["_DefaultPushNotificationTemplate"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsPinpointPushtemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsPinpointPushtemplate"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            GCM=AndroidPushNotificationTemplate._deserialize(json_data.get("GCM")),
            Baidu=AndroidPushNotificationTemplate._deserialize(json_data.get("Baidu")),
            TemplateName=json_data.get("TemplateName"),
            ADM=AndroidPushNotificationTemplate._deserialize(json_data.get("ADM")),
            APNS=APNSPushNotificationTemplate._deserialize(json_data.get("APNS")),
            TemplateDescription=json_data.get("TemplateDescription"),
            DefaultSubstitutions=json_data.get("DefaultSubstitutions"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Default=DefaultPushNotificationTemplate._deserialize(json_data.get("Default")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsPinpointPushtemplate = AwsPinpointPushtemplate


@dataclass
class AndroidPushNotificationTemplate(BaseModel):
    Action: Optional[str]
    ImageUrl: Optional[str]
    SmallImageIconUrl: Optional[str]
    Title: Optional[str]
    ImageIconUrl: Optional[str]
    Sound: Optional[str]
    Body: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AndroidPushNotificationTemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AndroidPushNotificationTemplate"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            ImageUrl=json_data.get("ImageUrl"),
            SmallImageIconUrl=json_data.get("SmallImageIconUrl"),
            Title=json_data.get("Title"),
            ImageIconUrl=json_data.get("ImageIconUrl"),
            Sound=json_data.get("Sound"),
            Body=json_data.get("Body"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AndroidPushNotificationTemplate = AndroidPushNotificationTemplate


@dataclass
class APNSPushNotificationTemplate(BaseModel):
    Action: Optional[str]
    MediaUrl: Optional[str]
    Title: Optional[str]
    Sound: Optional[str]
    Body: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_APNSPushNotificationTemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_APNSPushNotificationTemplate"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            MediaUrl=json_data.get("MediaUrl"),
            Title=json_data.get("Title"),
            Sound=json_data.get("Sound"),
            Body=json_data.get("Body"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_APNSPushNotificationTemplate = APNSPushNotificationTemplate


@dataclass
class DefaultPushNotificationTemplate(BaseModel):
    Title: Optional[str]
    Action: Optional[str]
    Sound: Optional[str]
    Body: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultPushNotificationTemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultPushNotificationTemplate"]:
        if not json_data:
            return None
        return cls(
            Title=json_data.get("Title"),
            Action=json_data.get("Action"),
            Sound=json_data.get("Sound"),
            Body=json_data.get("Body"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultPushNotificationTemplate = DefaultPushNotificationTemplate


