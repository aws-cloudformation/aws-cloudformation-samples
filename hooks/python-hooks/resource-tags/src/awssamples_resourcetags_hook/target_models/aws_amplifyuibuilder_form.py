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
class AwsAmplifyuibuilderForm(BaseModel):
    AppId: Optional[str]
    Cta: Optional["_FormCTA"]
    DataType: Optional["_FormDataTypeConfig"]
    EnvironmentName: Optional[str]
    Fields: Optional[MutableMapping[str, "_FieldConfig"]]
    FormActionType: Optional[str]
    Id: Optional[str]
    LabelDecorator: Optional[str]
    Name: Optional[str]
    SchemaVersion: Optional[str]
    SectionalElements: Optional[MutableMapping[str, "_SectionalElement"]]
    Style: Optional["_FormStyle"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAmplifyuibuilderForm"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAmplifyuibuilderForm"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AppId=json_data.get("AppId"),
            Cta=FormCTA._deserialize(json_data.get("Cta")),
            DataType=FormDataTypeConfig._deserialize(json_data.get("DataType")),
            EnvironmentName=json_data.get("EnvironmentName"),
            Fields=json_data.get("Fields"),
            FormActionType=json_data.get("FormActionType"),
            Id=json_data.get("Id"),
            LabelDecorator=json_data.get("LabelDecorator"),
            Name=json_data.get("Name"),
            SchemaVersion=json_data.get("SchemaVersion"),
            SectionalElements=json_data.get("SectionalElements"),
            Style=FormStyle._deserialize(json_data.get("Style")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAmplifyuibuilderForm = AwsAmplifyuibuilderForm


@dataclass
class FormCTA(BaseModel):
    Position: Optional[str]
    Clear: Optional["_FormButton"]
    Cancel: Optional["_FormButton"]
    Submit: Optional["_FormButton"]

    @classmethod
    def _deserialize(
        cls: Type["_FormCTA"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FormCTA"]:
        if not json_data:
            return None
        return cls(
            Position=json_data.get("Position"),
            Clear=FormButton._deserialize(json_data.get("Clear")),
            Cancel=FormButton._deserialize(json_data.get("Cancel")),
            Submit=FormButton._deserialize(json_data.get("Submit")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FormCTA = FormCTA


@dataclass
class FormButton(BaseModel):
    Excluded: Optional[bool]
    Children: Optional[str]
    Position: Optional["_FieldPosition"]

    @classmethod
    def _deserialize(
        cls: Type["_FormButton"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FormButton"]:
        if not json_data:
            return None
        return cls(
            Excluded=json_data.get("Excluded"),
            Children=json_data.get("Children"),
            Position=FieldPosition._deserialize(json_data.get("Position")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FormButton = FormButton


@dataclass
class FieldPosition(BaseModel):
    Fixed: Optional[str]
    RightOf: Optional[str]
    Below: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FieldPosition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldPosition"]:
        if not json_data:
            return None
        return cls(
            Fixed=json_data.get("Fixed"),
            RightOf=json_data.get("RightOf"),
            Below=json_data.get("Below"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldPosition = FieldPosition


@dataclass
class FormDataTypeConfig(BaseModel):
    DataSourceType: Optional[str]
    DataTypeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FormDataTypeConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FormDataTypeConfig"]:
        if not json_data:
            return None
        return cls(
            DataSourceType=json_data.get("DataSourceType"),
            DataTypeName=json_data.get("DataTypeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FormDataTypeConfig = FormDataTypeConfig


@dataclass
class FieldConfig(BaseModel):
    Label: Optional[str]
    Position: Optional["_FieldPosition"]
    Excluded: Optional[bool]
    InputType: Optional["_FieldInputConfig"]
    Validations: Optional[Sequence["_FieldValidationConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_FieldConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldConfig"]:
        if not json_data:
            return None
        return cls(
            Label=json_data.get("Label"),
            Position=FieldPosition._deserialize(json_data.get("Position")),
            Excluded=json_data.get("Excluded"),
            InputType=FieldInputConfig._deserialize(json_data.get("InputType")),
            Validations=deserialize_list(json_data.get("Validations"), FieldValidationConfiguration),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldConfig = FieldConfig


@dataclass
class FieldInputConfig(BaseModel):
    Type: Optional[str]
    Required: Optional[bool]
    ReadOnly: Optional[bool]
    Placeholder: Optional[str]
    DefaultValue: Optional[str]
    DescriptiveText: Optional[str]
    DefaultChecked: Optional[bool]
    DefaultCountryCode: Optional[str]
    ValueMappings: Optional["_ValueMappings"]
    Name: Optional[str]
    MinValue: Optional[float]
    MaxValue: Optional[float]
    Step: Optional[float]
    Value: Optional[str]
    IsArray: Optional[bool]
    FileUploaderConfig: Optional["_FileUploaderFieldConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_FieldInputConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldInputConfig"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Required=json_data.get("Required"),
            ReadOnly=json_data.get("ReadOnly"),
            Placeholder=json_data.get("Placeholder"),
            DefaultValue=json_data.get("DefaultValue"),
            DescriptiveText=json_data.get("DescriptiveText"),
            DefaultChecked=json_data.get("DefaultChecked"),
            DefaultCountryCode=json_data.get("DefaultCountryCode"),
            ValueMappings=ValueMappings._deserialize(json_data.get("ValueMappings")),
            Name=json_data.get("Name"),
            MinValue=json_data.get("MinValue"),
            MaxValue=json_data.get("MaxValue"),
            Step=json_data.get("Step"),
            Value=json_data.get("Value"),
            IsArray=json_data.get("IsArray"),
            FileUploaderConfig=FileUploaderFieldConfig._deserialize(json_data.get("FileUploaderConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldInputConfig = FieldInputConfig


@dataclass
class ValueMappings(BaseModel):
    Values: Optional[Sequence["_ValueMapping"]]

    @classmethod
    def _deserialize(
        cls: Type["_ValueMappings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValueMappings"]:
        if not json_data:
            return None
        return cls(
            Values=deserialize_list(json_data.get("Values"), ValueMapping),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValueMappings = ValueMappings


@dataclass
class ValueMapping(BaseModel):
    DisplayValue: Optional["_FormInputValueProperty"]
    Value: Optional["_FormInputValueProperty"]

    @classmethod
    def _deserialize(
        cls: Type["_ValueMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValueMapping"]:
        if not json_data:
            return None
        return cls(
            DisplayValue=FormInputValueProperty._deserialize(json_data.get("DisplayValue")),
            Value=FormInputValueProperty._deserialize(json_data.get("Value")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValueMapping = ValueMapping


@dataclass
class FormInputValueProperty(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FormInputValueProperty"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FormInputValueProperty"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FormInputValueProperty = FormInputValueProperty


@dataclass
class FileUploaderFieldConfig(BaseModel):
    AccessLevel: Optional[str]
    AcceptedFileTypes: Optional[Sequence[str]]
    ShowThumbnails: Optional[bool]
    IsResumable: Optional[bool]
    MaxFileCount: Optional[float]
    MaxSize: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FileUploaderFieldConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileUploaderFieldConfig"]:
        if not json_data:
            return None
        return cls(
            AccessLevel=json_data.get("AccessLevel"),
            AcceptedFileTypes=json_data.get("AcceptedFileTypes"),
            ShowThumbnails=json_data.get("ShowThumbnails"),
            IsResumable=json_data.get("IsResumable"),
            MaxFileCount=json_data.get("MaxFileCount"),
            MaxSize=json_data.get("MaxSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileUploaderFieldConfig = FileUploaderFieldConfig


@dataclass
class FieldValidationConfiguration(BaseModel):
    Type: Optional[str]
    StrValues: Optional[Sequence[str]]
    NumValues: Optional[Sequence[float]]
    ValidationMessage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FieldValidationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldValidationConfiguration"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            StrValues=json_data.get("StrValues"),
            NumValues=json_data.get("NumValues"),
            ValidationMessage=json_data.get("ValidationMessage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldValidationConfiguration = FieldValidationConfiguration


@dataclass
class SectionalElement(BaseModel):
    Type: Optional[str]
    Position: Optional["_FieldPosition"]
    Text: Optional[str]
    Level: Optional[float]
    Orientation: Optional[str]
    Excluded: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SectionalElement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SectionalElement"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Position=FieldPosition._deserialize(json_data.get("Position")),
            Text=json_data.get("Text"),
            Level=json_data.get("Level"),
            Orientation=json_data.get("Orientation"),
            Excluded=json_data.get("Excluded"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SectionalElement = SectionalElement


@dataclass
class FormStyle(BaseModel):
    HorizontalGap: Optional["_FormStyleConfig"]
    VerticalGap: Optional["_FormStyleConfig"]
    OuterPadding: Optional["_FormStyleConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_FormStyle"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FormStyle"]:
        if not json_data:
            return None
        return cls(
            HorizontalGap=FormStyleConfig._deserialize(json_data.get("HorizontalGap")),
            VerticalGap=FormStyleConfig._deserialize(json_data.get("VerticalGap")),
            OuterPadding=FormStyleConfig._deserialize(json_data.get("OuterPadding")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FormStyle = FormStyle


@dataclass
class FormStyleConfig(BaseModel):
    TokenReference: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FormStyleConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FormStyleConfig"]:
        if not json_data:
            return None
        return cls(
            TokenReference=json_data.get("TokenReference"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FormStyleConfig = FormStyleConfig


