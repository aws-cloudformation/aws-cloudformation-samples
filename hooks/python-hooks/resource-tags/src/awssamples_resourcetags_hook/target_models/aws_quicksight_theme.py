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
class AwsQuicksightTheme(BaseModel):
    Arn: Optional[str]
    AwsAccountId: Optional[str]
    BaseThemeId: Optional[str]
    Configuration: Optional["_ThemeConfiguration"]
    CreatedTime: Optional[str]
    LastUpdatedTime: Optional[str]
    Name: Optional[str]
    Permissions: Optional[Sequence["_ResourcePermission"]]
    Tags: Optional[Any]
    ThemeId: Optional[str]
    Type: Optional[str]
    Version: Optional["_ThemeVersion"]
    VersionDescription: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsQuicksightTheme"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsQuicksightTheme"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            AwsAccountId=json_data.get("AwsAccountId"),
            BaseThemeId=json_data.get("BaseThemeId"),
            Configuration=ThemeConfiguration._deserialize(json_data.get("Configuration")),
            CreatedTime=json_data.get("CreatedTime"),
            LastUpdatedTime=json_data.get("LastUpdatedTime"),
            Name=json_data.get("Name"),
            Permissions=deserialize_list(json_data.get("Permissions"), ResourcePermission),
            Tags=json_data.get("Tags"),
            ThemeId=json_data.get("ThemeId"),
            Type=json_data.get("Type"),
            Version=ThemeVersion._deserialize(json_data.get("Version")),
            VersionDescription=json_data.get("VersionDescription"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsQuicksightTheme = AwsQuicksightTheme


@dataclass
class ThemeConfiguration(BaseModel):
    DataColorPalette: Optional["_DataColorPalette"]
    UIColorPalette: Optional["_UIColorPalette"]
    Sheet: Optional["_SheetStyle"]
    Typography: Optional["_Typography"]

    @classmethod
    def _deserialize(
        cls: Type["_ThemeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThemeConfiguration"]:
        if not json_data:
            return None
        return cls(
            DataColorPalette=DataColorPalette._deserialize(json_data.get("DataColorPalette")),
            UIColorPalette=UIColorPalette._deserialize(json_data.get("UIColorPalette")),
            Sheet=SheetStyle._deserialize(json_data.get("Sheet")),
            Typography=Typography._deserialize(json_data.get("Typography")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThemeConfiguration = ThemeConfiguration


@dataclass
class DataColorPalette(BaseModel):
    EmptyFillColor: Optional[str]
    Colors: Optional[Sequence[str]]
    MinMaxGradient: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DataColorPalette"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataColorPalette"]:
        if not json_data:
            return None
        return cls(
            EmptyFillColor=json_data.get("EmptyFillColor"),
            Colors=json_data.get("Colors"),
            MinMaxGradient=json_data.get("MinMaxGradient"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataColorPalette = DataColorPalette


@dataclass
class UIColorPalette(BaseModel):
    Warning: Optional[str]
    Accent: Optional[str]
    AccentForeground: Optional[str]
    SecondaryBackground: Optional[str]
    DangerForeground: Optional[str]
    PrimaryBackground: Optional[str]
    Dimension: Optional[str]
    SecondaryForeground: Optional[str]
    WarningForeground: Optional[str]
    DimensionForeground: Optional[str]
    PrimaryForeground: Optional[str]
    Success: Optional[str]
    Danger: Optional[str]
    SuccessForeground: Optional[str]
    Measure: Optional[str]
    MeasureForeground: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UIColorPalette"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UIColorPalette"]:
        if not json_data:
            return None
        return cls(
            Warning=json_data.get("Warning"),
            Accent=json_data.get("Accent"),
            AccentForeground=json_data.get("AccentForeground"),
            SecondaryBackground=json_data.get("SecondaryBackground"),
            DangerForeground=json_data.get("DangerForeground"),
            PrimaryBackground=json_data.get("PrimaryBackground"),
            Dimension=json_data.get("Dimension"),
            SecondaryForeground=json_data.get("SecondaryForeground"),
            WarningForeground=json_data.get("WarningForeground"),
            DimensionForeground=json_data.get("DimensionForeground"),
            PrimaryForeground=json_data.get("PrimaryForeground"),
            Success=json_data.get("Success"),
            Danger=json_data.get("Danger"),
            SuccessForeground=json_data.get("SuccessForeground"),
            Measure=json_data.get("Measure"),
            MeasureForeground=json_data.get("MeasureForeground"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UIColorPalette = UIColorPalette


@dataclass
class SheetStyle(BaseModel):
    TileLayout: Optional["_TileLayoutStyle"]
    Tile: Optional["_TileStyle"]

    @classmethod
    def _deserialize(
        cls: Type["_SheetStyle"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SheetStyle"]:
        if not json_data:
            return None
        return cls(
            TileLayout=TileLayoutStyle._deserialize(json_data.get("TileLayout")),
            Tile=TileStyle._deserialize(json_data.get("Tile")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SheetStyle = SheetStyle


@dataclass
class TileLayoutStyle(BaseModel):
    Gutter: Optional["_GutterStyle"]
    Margin: Optional["_MarginStyle"]

    @classmethod
    def _deserialize(
        cls: Type["_TileLayoutStyle"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TileLayoutStyle"]:
        if not json_data:
            return None
        return cls(
            Gutter=GutterStyle._deserialize(json_data.get("Gutter")),
            Margin=MarginStyle._deserialize(json_data.get("Margin")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TileLayoutStyle = TileLayoutStyle


@dataclass
class GutterStyle(BaseModel):
    Show: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GutterStyle"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GutterStyle"]:
        if not json_data:
            return None
        return cls(
            Show=json_data.get("Show"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GutterStyle = GutterStyle


@dataclass
class MarginStyle(BaseModel):
    Show: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_MarginStyle"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarginStyle"]:
        if not json_data:
            return None
        return cls(
            Show=json_data.get("Show"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarginStyle = MarginStyle


@dataclass
class TileStyle(BaseModel):
    Border: Optional["_BorderStyle"]

    @classmethod
    def _deserialize(
        cls: Type["_TileStyle"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TileStyle"]:
        if not json_data:
            return None
        return cls(
            Border=BorderStyle._deserialize(json_data.get("Border")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TileStyle = TileStyle


@dataclass
class BorderStyle(BaseModel):
    Show: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_BorderStyle"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BorderStyle"]:
        if not json_data:
            return None
        return cls(
            Show=json_data.get("Show"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BorderStyle = BorderStyle


@dataclass
class Typography(BaseModel):
    FontFamilies: Optional[Sequence["_Font"]]

    @classmethod
    def _deserialize(
        cls: Type["_Typography"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Typography"]:
        if not json_data:
            return None
        return cls(
            FontFamilies=deserialize_list(json_data.get("FontFamilies"), Font),
        )


# work around possible type aliasing issues when variable has same name as a model
_Typography = Typography


@dataclass
class Font(BaseModel):
    FontFamily: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Font"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Font"]:
        if not json_data:
            return None
        return cls(
            FontFamily=json_data.get("FontFamily"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Font = Font


@dataclass
class ResourcePermission(BaseModel):
    Actions: Optional[Sequence[str]]
    Principal: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourcePermission"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourcePermission"]:
        if not json_data:
            return None
        return cls(
            Actions=json_data.get("Actions"),
            Principal=json_data.get("Principal"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourcePermission = ResourcePermission


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


@dataclass
class ThemeVersion(BaseModel):
    Status: Optional[str]
    Errors: Optional[Sequence["_ThemeError"]]
    Description: Optional[str]
    CreatedTime: Optional[str]
    Configuration: Optional["_ThemeConfiguration"]
    BaseThemeId: Optional[str]
    Arn: Optional[str]
    VersionNumber: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ThemeVersion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThemeVersion"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            Errors=deserialize_list(json_data.get("Errors"), ThemeError),
            Description=json_data.get("Description"),
            CreatedTime=json_data.get("CreatedTime"),
            Configuration=ThemeConfiguration._deserialize(json_data.get("Configuration")),
            BaseThemeId=json_data.get("BaseThemeId"),
            Arn=json_data.get("Arn"),
            VersionNumber=json_data.get("VersionNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThemeVersion = ThemeVersion


@dataclass
class ThemeError(BaseModel):
    Type: Optional[str]
    Message: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThemeError"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThemeError"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Message=json_data.get("Message"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThemeError = ThemeError


