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
class AwsAmplifyuibuilderTheme(BaseModel):
    AppId: Optional[str]
    EnvironmentName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Overrides: Optional[Sequence["_ThemeValues"]]
    Tags: Optional[Any]
    Values: Optional[Sequence["_ThemeValues"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAmplifyuibuilderTheme"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAmplifyuibuilderTheme"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AppId=json_data.get("AppId"),
            EnvironmentName=json_data.get("EnvironmentName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Overrides=deserialize_list(json_data.get("Overrides"), ThemeValues),
            Tags=json_data.get("Tags"),
            Values=deserialize_list(json_data.get("Values"), ThemeValues),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAmplifyuibuilderTheme = AwsAmplifyuibuilderTheme


@dataclass
class ThemeValues(BaseModel):
    Key: Optional[str]
    Value: Optional["_ThemeValue"]

    @classmethod
    def _deserialize(
        cls: Type["_ThemeValues"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThemeValues"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=ThemeValue._deserialize(json_data.get("Value")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThemeValues = ThemeValues


@dataclass
class ThemeValue(BaseModel):
    Value: Optional[str]
    Children: Optional[Sequence["_ThemeValues"]]

    @classmethod
    def _deserialize(
        cls: Type["_ThemeValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThemeValue"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Children=deserialize_list(json_data.get("Children"), ThemeValues),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThemeValue = ThemeValue


