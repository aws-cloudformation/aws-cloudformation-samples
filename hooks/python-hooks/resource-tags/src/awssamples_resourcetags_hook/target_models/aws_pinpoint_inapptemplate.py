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
class AwsPinpointInapptemplate(BaseModel):
    Arn: Optional[str]
    Content: Optional[Sequence["_InAppMessageContent"]]
    CustomConfig: Optional[MutableMapping[str, Any]]
    Layout: Optional[str]
    Tags: Optional[Any]
    TemplateDescription: Optional[str]
    TemplateName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsPinpointInapptemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsPinpointInapptemplate"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Content=deserialize_list(json_data.get("Content"), InAppMessageContent),
            CustomConfig=json_data.get("CustomConfig"),
            Layout=json_data.get("Layout"),
            Tags=json_data.get("Tags"),
            TemplateDescription=json_data.get("TemplateDescription"),
            TemplateName=json_data.get("TemplateName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsPinpointInapptemplate = AwsPinpointInapptemplate


@dataclass
class InAppMessageContent(BaseModel):
    BackgroundColor: Optional[str]
    BodyConfig: Optional["_BodyConfig"]
    HeaderConfig: Optional["_HeaderConfig"]
    ImageUrl: Optional[str]
    PrimaryBtn: Optional["_ButtonConfig"]
    SecondaryBtn: Optional["_ButtonConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_InAppMessageContent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InAppMessageContent"]:
        if not json_data:
            return None
        return cls(
            BackgroundColor=json_data.get("BackgroundColor"),
            BodyConfig=BodyConfig._deserialize(json_data.get("BodyConfig")),
            HeaderConfig=HeaderConfig._deserialize(json_data.get("HeaderConfig")),
            ImageUrl=json_data.get("ImageUrl"),
            PrimaryBtn=ButtonConfig._deserialize(json_data.get("PrimaryBtn")),
            SecondaryBtn=ButtonConfig._deserialize(json_data.get("SecondaryBtn")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InAppMessageContent = InAppMessageContent


@dataclass
class BodyConfig(BaseModel):
    Alignment: Optional[str]
    Body: Optional[str]
    TextColor: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BodyConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BodyConfig"]:
        if not json_data:
            return None
        return cls(
            Alignment=json_data.get("Alignment"),
            Body=json_data.get("Body"),
            TextColor=json_data.get("TextColor"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BodyConfig = BodyConfig


@dataclass
class HeaderConfig(BaseModel):
    Alignment: Optional[str]
    Header: Optional[str]
    TextColor: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderConfig"]:
        if not json_data:
            return None
        return cls(
            Alignment=json_data.get("Alignment"),
            Header=json_data.get("Header"),
            TextColor=json_data.get("TextColor"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderConfig = HeaderConfig


@dataclass
class ButtonConfig(BaseModel):
    Android: Optional["_OverrideButtonConfiguration"]
    DefaultConfig: Optional["_DefaultButtonConfiguration"]
    IOS: Optional["_OverrideButtonConfiguration"]
    Web: Optional["_OverrideButtonConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ButtonConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ButtonConfig"]:
        if not json_data:
            return None
        return cls(
            Android=OverrideButtonConfiguration._deserialize(json_data.get("Android")),
            DefaultConfig=DefaultButtonConfiguration._deserialize(json_data.get("DefaultConfig")),
            IOS=OverrideButtonConfiguration._deserialize(json_data.get("IOS")),
            Web=OverrideButtonConfiguration._deserialize(json_data.get("Web")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ButtonConfig = ButtonConfig


@dataclass
class OverrideButtonConfiguration(BaseModel):
    ButtonAction: Optional[str]
    Link: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OverrideButtonConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverrideButtonConfiguration"]:
        if not json_data:
            return None
        return cls(
            ButtonAction=json_data.get("ButtonAction"),
            Link=json_data.get("Link"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverrideButtonConfiguration = OverrideButtonConfiguration


@dataclass
class DefaultButtonConfiguration(BaseModel):
    BackgroundColor: Optional[str]
    BorderRadius: Optional[int]
    ButtonAction: Optional[str]
    Link: Optional[str]
    Text: Optional[str]
    TextColor: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultButtonConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultButtonConfiguration"]:
        if not json_data:
            return None
        return cls(
            BackgroundColor=json_data.get("BackgroundColor"),
            BorderRadius=json_data.get("BorderRadius"),
            ButtonAction=json_data.get("ButtonAction"),
            Link=json_data.get("Link"),
            Text=json_data.get("Text"),
            TextColor=json_data.get("TextColor"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultButtonConfiguration = DefaultButtonConfiguration


