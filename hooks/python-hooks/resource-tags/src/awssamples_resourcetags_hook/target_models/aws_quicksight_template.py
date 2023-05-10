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
class AwsQuicksightTemplate(BaseModel):
    Arn: Optional[str]
    AwsAccountId: Optional[str]
    CreatedTime: Optional[str]
    Definition: Optional["_TemplateVersionDefinition"]
    LastUpdatedTime: Optional[str]
    Name: Optional[str]
    Permissions: Optional[Sequence["_ResourcePermission"]]
    SourceEntity: Optional["_TemplateSourceEntity"]
    Tags: Optional[Any]
    TemplateId: Optional[str]
    Version: Optional["_TemplateVersion"]
    VersionDescription: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsQuicksightTemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsQuicksightTemplate"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            AwsAccountId=json_data.get("AwsAccountId"),
            CreatedTime=json_data.get("CreatedTime"),
            Definition=TemplateVersionDefinition._deserialize(json_data.get("Definition")),
            LastUpdatedTime=json_data.get("LastUpdatedTime"),
            Name=json_data.get("Name"),
            Permissions=deserialize_list(json_data.get("Permissions"), ResourcePermission),
            SourceEntity=TemplateSourceEntity._deserialize(json_data.get("SourceEntity")),
            Tags=json_data.get("Tags"),
            TemplateId=json_data.get("TemplateId"),
            Version=TemplateVersion._deserialize(json_data.get("Version")),
            VersionDescription=json_data.get("VersionDescription"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsQuicksightTemplate = AwsQuicksightTemplate


@dataclass
class TemplateVersionDefinition(BaseModel):
    DataSetConfigurations: Optional[Sequence["_DataSetConfiguration"]]
    Sheets: Optional[Sequence["_SheetDefinition"]]
    CalculatedFields: Optional[Sequence["_CalculatedField"]]
    ParameterDeclarations: Optional[Sequence["_ParameterDeclaration"]]
    FilterGroups: Optional[Sequence["_FilterGroup"]]
    ColumnConfigurations: Optional[Sequence["_ColumnConfiguration"]]
    AnalysisDefaults: Optional["_AnalysisDefaults"]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateVersionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateVersionDefinition"]:
        if not json_data:
            return None
        return cls(
            DataSetConfigurations=deserialize_list(json_data.get("DataSetConfigurations"), DataSetConfiguration),
            Sheets=deserialize_list(json_data.get("Sheets"), SheetDefinition),
            CalculatedFields=deserialize_list(json_data.get("CalculatedFields"), CalculatedField),
            ParameterDeclarations=deserialize_list(json_data.get("ParameterDeclarations"), ParameterDeclaration),
            FilterGroups=deserialize_list(json_data.get("FilterGroups"), FilterGroup),
            ColumnConfigurations=deserialize_list(json_data.get("ColumnConfigurations"), ColumnConfiguration),
            AnalysisDefaults=AnalysisDefaults._deserialize(json_data.get("AnalysisDefaults")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateVersionDefinition = TemplateVersionDefinition


@dataclass
class DataSetConfiguration(BaseModel):
    Placeholder: Optional[str]
    DataSetSchema: Optional["_DataSetSchema"]
    ColumnGroupSchemaList: Optional[Sequence["_ColumnGroupSchema"]]

    @classmethod
    def _deserialize(
        cls: Type["_DataSetConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataSetConfiguration"]:
        if not json_data:
            return None
        return cls(
            Placeholder=json_data.get("Placeholder"),
            DataSetSchema=DataSetSchema._deserialize(json_data.get("DataSetSchema")),
            ColumnGroupSchemaList=deserialize_list(json_data.get("ColumnGroupSchemaList"), ColumnGroupSchema),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataSetConfiguration = DataSetConfiguration


@dataclass
class DataSetSchema(BaseModel):
    ColumnSchemaList: Optional[Sequence["_ColumnSchema"]]

    @classmethod
    def _deserialize(
        cls: Type["_DataSetSchema"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataSetSchema"]:
        if not json_data:
            return None
        return cls(
            ColumnSchemaList=deserialize_list(json_data.get("ColumnSchemaList"), ColumnSchema),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataSetSchema = DataSetSchema


@dataclass
class ColumnSchema(BaseModel):
    Name: Optional[str]
    DataType: Optional[str]
    GeographicRole: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnSchema"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnSchema"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            DataType=json_data.get("DataType"),
            GeographicRole=json_data.get("GeographicRole"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnSchema = ColumnSchema


@dataclass
class ColumnGroupSchema(BaseModel):
    Name: Optional[str]
    ColumnGroupColumnSchemaList: Optional[Sequence["_ColumnGroupColumnSchema"]]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnGroupSchema"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnGroupSchema"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            ColumnGroupColumnSchemaList=deserialize_list(json_data.get("ColumnGroupColumnSchemaList"), ColumnGroupColumnSchema),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnGroupSchema = ColumnGroupSchema


@dataclass
class ColumnGroupColumnSchema(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnGroupColumnSchema"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnGroupColumnSchema"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnGroupColumnSchema = ColumnGroupColumnSchema


@dataclass
class SheetDefinition(BaseModel):
    SheetId: Optional[str]
    Title: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    ParameterControls: Optional[Sequence["_ParameterControl"]]
    FilterControls: Optional[Sequence["_FilterControl"]]
    Visuals: Optional[Sequence["_Visual"]]
    TextBoxes: Optional[Sequence["_SheetTextBox"]]
    Layouts: Optional[Sequence["_Layout"]]
    SheetControlLayouts: Optional[Sequence["_SheetControlLayout"]]
    ContentType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SheetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SheetDefinition"]:
        if not json_data:
            return None
        return cls(
            SheetId=json_data.get("SheetId"),
            Title=json_data.get("Title"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            ParameterControls=deserialize_list(json_data.get("ParameterControls"), ParameterControl),
            FilterControls=deserialize_list(json_data.get("FilterControls"), FilterControl),
            Visuals=deserialize_list(json_data.get("Visuals"), Visual),
            TextBoxes=deserialize_list(json_data.get("TextBoxes"), SheetTextBox),
            Layouts=deserialize_list(json_data.get("Layouts"), Layout),
            SheetControlLayouts=deserialize_list(json_data.get("SheetControlLayouts"), SheetControlLayout),
            ContentType=json_data.get("ContentType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SheetDefinition = SheetDefinition


@dataclass
class ParameterControl(BaseModel):
    DateTimePicker: Optional["_ParameterDateTimePickerControl"]
    List: Optional["_ParameterListControl"]
    Dropdown: Optional["_ParameterDropDownControl"]
    TextField: Optional["_ParameterTextFieldControl"]
    TextArea: Optional["_ParameterTextAreaControl"]
    Slider: Optional["_ParameterSliderControl"]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterControl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterControl"]:
        if not json_data:
            return None
        return cls(
            DateTimePicker=ParameterDateTimePickerControl._deserialize(json_data.get("DateTimePicker")),
            List=ParameterListControl._deserialize(json_data.get("List")),
            Dropdown=ParameterDropDownControl._deserialize(json_data.get("Dropdown")),
            TextField=ParameterTextFieldControl._deserialize(json_data.get("TextField")),
            TextArea=ParameterTextAreaControl._deserialize(json_data.get("TextArea")),
            Slider=ParameterSliderControl._deserialize(json_data.get("Slider")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterControl = ParameterControl


@dataclass
class ParameterDateTimePickerControl(BaseModel):
    ParameterControlId: Optional[str]
    Title: Optional[str]
    SourceParameterName: Optional[str]
    DisplayOptions: Optional["_DateTimePickerControlDisplayOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterDateTimePickerControl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterDateTimePickerControl"]:
        if not json_data:
            return None
        return cls(
            ParameterControlId=json_data.get("ParameterControlId"),
            Title=json_data.get("Title"),
            SourceParameterName=json_data.get("SourceParameterName"),
            DisplayOptions=DateTimePickerControlDisplayOptions._deserialize(json_data.get("DisplayOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterDateTimePickerControl = ParameterDateTimePickerControl


@dataclass
class DateTimePickerControlDisplayOptions(BaseModel):
    TitleOptions: Optional["_LabelOptions"]
    DateTimeFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DateTimePickerControlDisplayOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DateTimePickerControlDisplayOptions"]:
        if not json_data:
            return None
        return cls(
            TitleOptions=LabelOptions._deserialize(json_data.get("TitleOptions")),
            DateTimeFormat=json_data.get("DateTimeFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DateTimePickerControlDisplayOptions = DateTimePickerControlDisplayOptions


@dataclass
class LabelOptions(BaseModel):
    Visibility: Optional[str]
    FontConfiguration: Optional["_FontConfiguration"]
    CustomLabel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelOptions"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
            FontConfiguration=FontConfiguration._deserialize(json_data.get("FontConfiguration")),
            CustomLabel=json_data.get("CustomLabel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelOptions = LabelOptions


@dataclass
class FontConfiguration(BaseModel):
    FontSize: Optional["_FontSize"]
    FontDecoration: Optional[str]
    FontColor: Optional[str]
    FontWeight: Optional["_FontWeight"]
    FontStyle: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FontConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FontConfiguration"]:
        if not json_data:
            return None
        return cls(
            FontSize=FontSize._deserialize(json_data.get("FontSize")),
            FontDecoration=json_data.get("FontDecoration"),
            FontColor=json_data.get("FontColor"),
            FontWeight=FontWeight._deserialize(json_data.get("FontWeight")),
            FontStyle=json_data.get("FontStyle"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FontConfiguration = FontConfiguration


@dataclass
class FontSize(BaseModel):
    Relative: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FontSize"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FontSize"]:
        if not json_data:
            return None
        return cls(
            Relative=json_data.get("Relative"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FontSize = FontSize


@dataclass
class FontWeight(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FontWeight"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FontWeight"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FontWeight = FontWeight


@dataclass
class ParameterListControl(BaseModel):
    ParameterControlId: Optional[str]
    Title: Optional[str]
    SourceParameterName: Optional[str]
    DisplayOptions: Optional["_ListControlDisplayOptions"]
    Type: Optional[str]
    SelectableValues: Optional["_ParameterSelectableValues"]
    CascadingControlConfiguration: Optional["_CascadingControlConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterListControl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterListControl"]:
        if not json_data:
            return None
        return cls(
            ParameterControlId=json_data.get("ParameterControlId"),
            Title=json_data.get("Title"),
            SourceParameterName=json_data.get("SourceParameterName"),
            DisplayOptions=ListControlDisplayOptions._deserialize(json_data.get("DisplayOptions")),
            Type=json_data.get("Type"),
            SelectableValues=ParameterSelectableValues._deserialize(json_data.get("SelectableValues")),
            CascadingControlConfiguration=CascadingControlConfiguration._deserialize(json_data.get("CascadingControlConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterListControl = ParameterListControl


@dataclass
class ListControlDisplayOptions(BaseModel):
    SearchOptions: Optional["_ListControlSearchOptions"]
    SelectAllOptions: Optional["_ListControlSelectAllOptions"]
    TitleOptions: Optional["_LabelOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_ListControlDisplayOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListControlDisplayOptions"]:
        if not json_data:
            return None
        return cls(
            SearchOptions=ListControlSearchOptions._deserialize(json_data.get("SearchOptions")),
            SelectAllOptions=ListControlSelectAllOptions._deserialize(json_data.get("SelectAllOptions")),
            TitleOptions=LabelOptions._deserialize(json_data.get("TitleOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListControlDisplayOptions = ListControlDisplayOptions


@dataclass
class ListControlSearchOptions(BaseModel):
    Visibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ListControlSearchOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListControlSearchOptions"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListControlSearchOptions = ListControlSearchOptions


@dataclass
class ListControlSelectAllOptions(BaseModel):
    Visibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ListControlSelectAllOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListControlSelectAllOptions"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListControlSelectAllOptions = ListControlSelectAllOptions


@dataclass
class ParameterSelectableValues(BaseModel):
    Values: Optional[Sequence[str]]
    LinkToDataSetColumn: Optional["_ColumnIdentifier"]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterSelectableValues"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterSelectableValues"]:
        if not json_data:
            return None
        return cls(
            Values=json_data.get("Values"),
            LinkToDataSetColumn=ColumnIdentifier._deserialize(json_data.get("LinkToDataSetColumn")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterSelectableValues = ParameterSelectableValues


@dataclass
class ColumnIdentifier(BaseModel):
    DataSetIdentifier: Optional[str]
    ColumnName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnIdentifier"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnIdentifier"]:
        if not json_data:
            return None
        return cls(
            DataSetIdentifier=json_data.get("DataSetIdentifier"),
            ColumnName=json_data.get("ColumnName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnIdentifier = ColumnIdentifier


@dataclass
class CascadingControlConfiguration(BaseModel):
    SourceControls: Optional[Sequence["_CascadingControlSource"]]

    @classmethod
    def _deserialize(
        cls: Type["_CascadingControlConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CascadingControlConfiguration"]:
        if not json_data:
            return None
        return cls(
            SourceControls=deserialize_list(json_data.get("SourceControls"), CascadingControlSource),
        )


# work around possible type aliasing issues when variable has same name as a model
_CascadingControlConfiguration = CascadingControlConfiguration


@dataclass
class CascadingControlSource(BaseModel):
    SourceSheetControlId: Optional[str]
    ColumnToMatch: Optional["_ColumnIdentifier"]

    @classmethod
    def _deserialize(
        cls: Type["_CascadingControlSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CascadingControlSource"]:
        if not json_data:
            return None
        return cls(
            SourceSheetControlId=json_data.get("SourceSheetControlId"),
            ColumnToMatch=ColumnIdentifier._deserialize(json_data.get("ColumnToMatch")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CascadingControlSource = CascadingControlSource


@dataclass
class ParameterDropDownControl(BaseModel):
    ParameterControlId: Optional[str]
    Title: Optional[str]
    SourceParameterName: Optional[str]
    DisplayOptions: Optional["_DropDownControlDisplayOptions"]
    Type: Optional[str]
    SelectableValues: Optional["_ParameterSelectableValues"]
    CascadingControlConfiguration: Optional["_CascadingControlConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterDropDownControl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterDropDownControl"]:
        if not json_data:
            return None
        return cls(
            ParameterControlId=json_data.get("ParameterControlId"),
            Title=json_data.get("Title"),
            SourceParameterName=json_data.get("SourceParameterName"),
            DisplayOptions=DropDownControlDisplayOptions._deserialize(json_data.get("DisplayOptions")),
            Type=json_data.get("Type"),
            SelectableValues=ParameterSelectableValues._deserialize(json_data.get("SelectableValues")),
            CascadingControlConfiguration=CascadingControlConfiguration._deserialize(json_data.get("CascadingControlConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterDropDownControl = ParameterDropDownControl


@dataclass
class DropDownControlDisplayOptions(BaseModel):
    SelectAllOptions: Optional["_ListControlSelectAllOptions"]
    TitleOptions: Optional["_LabelOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_DropDownControlDisplayOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DropDownControlDisplayOptions"]:
        if not json_data:
            return None
        return cls(
            SelectAllOptions=ListControlSelectAllOptions._deserialize(json_data.get("SelectAllOptions")),
            TitleOptions=LabelOptions._deserialize(json_data.get("TitleOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DropDownControlDisplayOptions = DropDownControlDisplayOptions


@dataclass
class ParameterTextFieldControl(BaseModel):
    ParameterControlId: Optional[str]
    Title: Optional[str]
    SourceParameterName: Optional[str]
    DisplayOptions: Optional["_TextFieldControlDisplayOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterTextFieldControl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterTextFieldControl"]:
        if not json_data:
            return None
        return cls(
            ParameterControlId=json_data.get("ParameterControlId"),
            Title=json_data.get("Title"),
            SourceParameterName=json_data.get("SourceParameterName"),
            DisplayOptions=TextFieldControlDisplayOptions._deserialize(json_data.get("DisplayOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterTextFieldControl = ParameterTextFieldControl


@dataclass
class TextFieldControlDisplayOptions(BaseModel):
    TitleOptions: Optional["_LabelOptions"]
    PlaceholderOptions: Optional["_TextControlPlaceholderOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_TextFieldControlDisplayOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TextFieldControlDisplayOptions"]:
        if not json_data:
            return None
        return cls(
            TitleOptions=LabelOptions._deserialize(json_data.get("TitleOptions")),
            PlaceholderOptions=TextControlPlaceholderOptions._deserialize(json_data.get("PlaceholderOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TextFieldControlDisplayOptions = TextFieldControlDisplayOptions


@dataclass
class TextControlPlaceholderOptions(BaseModel):
    Visibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TextControlPlaceholderOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TextControlPlaceholderOptions"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TextControlPlaceholderOptions = TextControlPlaceholderOptions


@dataclass
class ParameterTextAreaControl(BaseModel):
    ParameterControlId: Optional[str]
    Title: Optional[str]
    SourceParameterName: Optional[str]
    Delimiter: Optional[str]
    DisplayOptions: Optional["_TextAreaControlDisplayOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterTextAreaControl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterTextAreaControl"]:
        if not json_data:
            return None
        return cls(
            ParameterControlId=json_data.get("ParameterControlId"),
            Title=json_data.get("Title"),
            SourceParameterName=json_data.get("SourceParameterName"),
            Delimiter=json_data.get("Delimiter"),
            DisplayOptions=TextAreaControlDisplayOptions._deserialize(json_data.get("DisplayOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterTextAreaControl = ParameterTextAreaControl


@dataclass
class TextAreaControlDisplayOptions(BaseModel):
    TitleOptions: Optional["_LabelOptions"]
    PlaceholderOptions: Optional["_TextControlPlaceholderOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_TextAreaControlDisplayOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TextAreaControlDisplayOptions"]:
        if not json_data:
            return None
        return cls(
            TitleOptions=LabelOptions._deserialize(json_data.get("TitleOptions")),
            PlaceholderOptions=TextControlPlaceholderOptions._deserialize(json_data.get("PlaceholderOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TextAreaControlDisplayOptions = TextAreaControlDisplayOptions


@dataclass
class ParameterSliderControl(BaseModel):
    ParameterControlId: Optional[str]
    Title: Optional[str]
    SourceParameterName: Optional[str]
    DisplayOptions: Optional["_SliderControlDisplayOptions"]
    MaximumValue: Optional[float]
    MinimumValue: Optional[float]
    StepSize: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterSliderControl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterSliderControl"]:
        if not json_data:
            return None
        return cls(
            ParameterControlId=json_data.get("ParameterControlId"),
            Title=json_data.get("Title"),
            SourceParameterName=json_data.get("SourceParameterName"),
            DisplayOptions=SliderControlDisplayOptions._deserialize(json_data.get("DisplayOptions")),
            MaximumValue=json_data.get("MaximumValue"),
            MinimumValue=json_data.get("MinimumValue"),
            StepSize=json_data.get("StepSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterSliderControl = ParameterSliderControl


@dataclass
class SliderControlDisplayOptions(BaseModel):
    TitleOptions: Optional["_LabelOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_SliderControlDisplayOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SliderControlDisplayOptions"]:
        if not json_data:
            return None
        return cls(
            TitleOptions=LabelOptions._deserialize(json_data.get("TitleOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SliderControlDisplayOptions = SliderControlDisplayOptions


@dataclass
class FilterControl(BaseModel):
    DateTimePicker: Optional["_FilterDateTimePickerControl"]
    List: Optional["_FilterListControl"]
    Dropdown: Optional["_FilterDropDownControl"]
    TextField: Optional["_FilterTextFieldControl"]
    TextArea: Optional["_FilterTextAreaControl"]
    Slider: Optional["_FilterSliderControl"]
    RelativeDateTime: Optional["_FilterRelativeDateTimeControl"]

    @classmethod
    def _deserialize(
        cls: Type["_FilterControl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterControl"]:
        if not json_data:
            return None
        return cls(
            DateTimePicker=FilterDateTimePickerControl._deserialize(json_data.get("DateTimePicker")),
            List=FilterListControl._deserialize(json_data.get("List")),
            Dropdown=FilterDropDownControl._deserialize(json_data.get("Dropdown")),
            TextField=FilterTextFieldControl._deserialize(json_data.get("TextField")),
            TextArea=FilterTextAreaControl._deserialize(json_data.get("TextArea")),
            Slider=FilterSliderControl._deserialize(json_data.get("Slider")),
            RelativeDateTime=FilterRelativeDateTimeControl._deserialize(json_data.get("RelativeDateTime")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterControl = FilterControl


@dataclass
class FilterDateTimePickerControl(BaseModel):
    FilterControlId: Optional[str]
    Title: Optional[str]
    SourceFilterId: Optional[str]
    DisplayOptions: Optional["_DateTimePickerControlDisplayOptions"]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDateTimePickerControl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDateTimePickerControl"]:
        if not json_data:
            return None
        return cls(
            FilterControlId=json_data.get("FilterControlId"),
            Title=json_data.get("Title"),
            SourceFilterId=json_data.get("SourceFilterId"),
            DisplayOptions=DateTimePickerControlDisplayOptions._deserialize(json_data.get("DisplayOptions")),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDateTimePickerControl = FilterDateTimePickerControl


@dataclass
class FilterListControl(BaseModel):
    FilterControlId: Optional[str]
    Title: Optional[str]
    SourceFilterId: Optional[str]
    DisplayOptions: Optional["_ListControlDisplayOptions"]
    Type: Optional[str]
    SelectableValues: Optional["_FilterSelectableValues"]
    CascadingControlConfiguration: Optional["_CascadingControlConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_FilterListControl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterListControl"]:
        if not json_data:
            return None
        return cls(
            FilterControlId=json_data.get("FilterControlId"),
            Title=json_data.get("Title"),
            SourceFilterId=json_data.get("SourceFilterId"),
            DisplayOptions=ListControlDisplayOptions._deserialize(json_data.get("DisplayOptions")),
            Type=json_data.get("Type"),
            SelectableValues=FilterSelectableValues._deserialize(json_data.get("SelectableValues")),
            CascadingControlConfiguration=CascadingControlConfiguration._deserialize(json_data.get("CascadingControlConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterListControl = FilterListControl


@dataclass
class FilterSelectableValues(BaseModel):
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterSelectableValues"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterSelectableValues"]:
        if not json_data:
            return None
        return cls(
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterSelectableValues = FilterSelectableValues


@dataclass
class FilterDropDownControl(BaseModel):
    FilterControlId: Optional[str]
    Title: Optional[str]
    SourceFilterId: Optional[str]
    DisplayOptions: Optional["_DropDownControlDisplayOptions"]
    Type: Optional[str]
    SelectableValues: Optional["_FilterSelectableValues"]
    CascadingControlConfiguration: Optional["_CascadingControlConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDropDownControl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDropDownControl"]:
        if not json_data:
            return None
        return cls(
            FilterControlId=json_data.get("FilterControlId"),
            Title=json_data.get("Title"),
            SourceFilterId=json_data.get("SourceFilterId"),
            DisplayOptions=DropDownControlDisplayOptions._deserialize(json_data.get("DisplayOptions")),
            Type=json_data.get("Type"),
            SelectableValues=FilterSelectableValues._deserialize(json_data.get("SelectableValues")),
            CascadingControlConfiguration=CascadingControlConfiguration._deserialize(json_data.get("CascadingControlConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDropDownControl = FilterDropDownControl


@dataclass
class FilterTextFieldControl(BaseModel):
    FilterControlId: Optional[str]
    Title: Optional[str]
    SourceFilterId: Optional[str]
    DisplayOptions: Optional["_TextFieldControlDisplayOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_FilterTextFieldControl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterTextFieldControl"]:
        if not json_data:
            return None
        return cls(
            FilterControlId=json_data.get("FilterControlId"),
            Title=json_data.get("Title"),
            SourceFilterId=json_data.get("SourceFilterId"),
            DisplayOptions=TextFieldControlDisplayOptions._deserialize(json_data.get("DisplayOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterTextFieldControl = FilterTextFieldControl


@dataclass
class FilterTextAreaControl(BaseModel):
    FilterControlId: Optional[str]
    Title: Optional[str]
    SourceFilterId: Optional[str]
    Delimiter: Optional[str]
    DisplayOptions: Optional["_TextAreaControlDisplayOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_FilterTextAreaControl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterTextAreaControl"]:
        if not json_data:
            return None
        return cls(
            FilterControlId=json_data.get("FilterControlId"),
            Title=json_data.get("Title"),
            SourceFilterId=json_data.get("SourceFilterId"),
            Delimiter=json_data.get("Delimiter"),
            DisplayOptions=TextAreaControlDisplayOptions._deserialize(json_data.get("DisplayOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterTextAreaControl = FilterTextAreaControl


@dataclass
class FilterSliderControl(BaseModel):
    FilterControlId: Optional[str]
    Title: Optional[str]
    SourceFilterId: Optional[str]
    DisplayOptions: Optional["_SliderControlDisplayOptions"]
    Type: Optional[str]
    MaximumValue: Optional[float]
    MinimumValue: Optional[float]
    StepSize: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FilterSliderControl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterSliderControl"]:
        if not json_data:
            return None
        return cls(
            FilterControlId=json_data.get("FilterControlId"),
            Title=json_data.get("Title"),
            SourceFilterId=json_data.get("SourceFilterId"),
            DisplayOptions=SliderControlDisplayOptions._deserialize(json_data.get("DisplayOptions")),
            Type=json_data.get("Type"),
            MaximumValue=json_data.get("MaximumValue"),
            MinimumValue=json_data.get("MinimumValue"),
            StepSize=json_data.get("StepSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterSliderControl = FilterSliderControl


@dataclass
class FilterRelativeDateTimeControl(BaseModel):
    FilterControlId: Optional[str]
    Title: Optional[str]
    SourceFilterId: Optional[str]
    DisplayOptions: Optional["_RelativeDateTimeControlDisplayOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_FilterRelativeDateTimeControl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterRelativeDateTimeControl"]:
        if not json_data:
            return None
        return cls(
            FilterControlId=json_data.get("FilterControlId"),
            Title=json_data.get("Title"),
            SourceFilterId=json_data.get("SourceFilterId"),
            DisplayOptions=RelativeDateTimeControlDisplayOptions._deserialize(json_data.get("DisplayOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterRelativeDateTimeControl = FilterRelativeDateTimeControl


@dataclass
class RelativeDateTimeControlDisplayOptions(BaseModel):
    TitleOptions: Optional["_LabelOptions"]
    DateTimeFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelativeDateTimeControlDisplayOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelativeDateTimeControlDisplayOptions"]:
        if not json_data:
            return None
        return cls(
            TitleOptions=LabelOptions._deserialize(json_data.get("TitleOptions")),
            DateTimeFormat=json_data.get("DateTimeFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelativeDateTimeControlDisplayOptions = RelativeDateTimeControlDisplayOptions


@dataclass
class Visual(BaseModel):
    TableVisual: Optional["_TableVisual"]
    PivotTableVisual: Optional["_PivotTableVisual"]
    BarChartVisual: Optional["_BarChartVisual"]
    KPIVisual: Optional["_KPIVisual"]
    PieChartVisual: Optional["_PieChartVisual"]
    GaugeChartVisual: Optional["_GaugeChartVisual"]
    LineChartVisual: Optional["_LineChartVisual"]
    HeatMapVisual: Optional["_HeatMapVisual"]
    TreeMapVisual: Optional["_TreeMapVisual"]
    GeospatialMapVisual: Optional["_GeospatialMapVisual"]
    FilledMapVisual: Optional["_FilledMapVisual"]
    FunnelChartVisual: Optional["_FunnelChartVisual"]
    ScatterPlotVisual: Optional["_ScatterPlotVisual"]
    ComboChartVisual: Optional["_ComboChartVisual"]
    BoxPlotVisual: Optional["_BoxPlotVisual"]
    WaterfallVisual: Optional["_WaterfallVisual"]
    HistogramVisual: Optional["_HistogramVisual"]
    WordCloudVisual: Optional["_WordCloudVisual"]
    InsightVisual: Optional["_InsightVisual"]
    SankeyDiagramVisual: Optional["_SankeyDiagramVisual"]
    CustomContentVisual: Optional["_CustomContentVisual"]
    EmptyVisual: Optional["_EmptyVisual"]
    RadarChartVisual: Optional["_RadarChartVisual"]

    @classmethod
    def _deserialize(
        cls: Type["_Visual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Visual"]:
        if not json_data:
            return None
        return cls(
            TableVisual=TableVisual._deserialize(json_data.get("TableVisual")),
            PivotTableVisual=PivotTableVisual._deserialize(json_data.get("PivotTableVisual")),
            BarChartVisual=BarChartVisual._deserialize(json_data.get("BarChartVisual")),
            KPIVisual=KPIVisual._deserialize(json_data.get("KPIVisual")),
            PieChartVisual=PieChartVisual._deserialize(json_data.get("PieChartVisual")),
            GaugeChartVisual=GaugeChartVisual._deserialize(json_data.get("GaugeChartVisual")),
            LineChartVisual=LineChartVisual._deserialize(json_data.get("LineChartVisual")),
            HeatMapVisual=HeatMapVisual._deserialize(json_data.get("HeatMapVisual")),
            TreeMapVisual=TreeMapVisual._deserialize(json_data.get("TreeMapVisual")),
            GeospatialMapVisual=GeospatialMapVisual._deserialize(json_data.get("GeospatialMapVisual")),
            FilledMapVisual=FilledMapVisual._deserialize(json_data.get("FilledMapVisual")),
            FunnelChartVisual=FunnelChartVisual._deserialize(json_data.get("FunnelChartVisual")),
            ScatterPlotVisual=ScatterPlotVisual._deserialize(json_data.get("ScatterPlotVisual")),
            ComboChartVisual=ComboChartVisual._deserialize(json_data.get("ComboChartVisual")),
            BoxPlotVisual=BoxPlotVisual._deserialize(json_data.get("BoxPlotVisual")),
            WaterfallVisual=WaterfallVisual._deserialize(json_data.get("WaterfallVisual")),
            HistogramVisual=HistogramVisual._deserialize(json_data.get("HistogramVisual")),
            WordCloudVisual=WordCloudVisual._deserialize(json_data.get("WordCloudVisual")),
            InsightVisual=InsightVisual._deserialize(json_data.get("InsightVisual")),
            SankeyDiagramVisual=SankeyDiagramVisual._deserialize(json_data.get("SankeyDiagramVisual")),
            CustomContentVisual=CustomContentVisual._deserialize(json_data.get("CustomContentVisual")),
            EmptyVisual=EmptyVisual._deserialize(json_data.get("EmptyVisual")),
            RadarChartVisual=RadarChartVisual._deserialize(json_data.get("RadarChartVisual")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Visual = Visual


@dataclass
class TableVisual(BaseModel):
    VisualId: Optional[str]
    Title: Optional["_VisualTitleLabelOptions"]
    Subtitle: Optional["_VisualSubtitleLabelOptions"]
    ChartConfiguration: Optional["_TableConfiguration"]
    ConditionalFormatting: Optional["_TableConditionalFormatting"]
    Actions: Optional[Sequence["_VisualCustomAction"]]

    @classmethod
    def _deserialize(
        cls: Type["_TableVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            Title=VisualTitleLabelOptions._deserialize(json_data.get("Title")),
            Subtitle=VisualSubtitleLabelOptions._deserialize(json_data.get("Subtitle")),
            ChartConfiguration=TableConfiguration._deserialize(json_data.get("ChartConfiguration")),
            ConditionalFormatting=TableConditionalFormatting._deserialize(json_data.get("ConditionalFormatting")),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableVisual = TableVisual


@dataclass
class VisualTitleLabelOptions(BaseModel):
    Visibility: Optional[str]
    FormatText: Optional["_ShortFormatText"]

    @classmethod
    def _deserialize(
        cls: Type["_VisualTitleLabelOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VisualTitleLabelOptions"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
            FormatText=ShortFormatText._deserialize(json_data.get("FormatText")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VisualTitleLabelOptions = VisualTitleLabelOptions


@dataclass
class ShortFormatText(BaseModel):
    PlainText: Optional[str]
    RichText: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ShortFormatText"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShortFormatText"]:
        if not json_data:
            return None
        return cls(
            PlainText=json_data.get("PlainText"),
            RichText=json_data.get("RichText"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShortFormatText = ShortFormatText


@dataclass
class VisualSubtitleLabelOptions(BaseModel):
    Visibility: Optional[str]
    FormatText: Optional["_LongFormatText"]

    @classmethod
    def _deserialize(
        cls: Type["_VisualSubtitleLabelOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VisualSubtitleLabelOptions"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
            FormatText=LongFormatText._deserialize(json_data.get("FormatText")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VisualSubtitleLabelOptions = VisualSubtitleLabelOptions


@dataclass
class LongFormatText(BaseModel):
    PlainText: Optional[str]
    RichText: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LongFormatText"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LongFormatText"]:
        if not json_data:
            return None
        return cls(
            PlainText=json_data.get("PlainText"),
            RichText=json_data.get("RichText"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LongFormatText = LongFormatText


@dataclass
class TableConfiguration(BaseModel):
    FieldWells: Optional["_TableFieldWells"]
    SortConfiguration: Optional["_TableSortConfiguration"]
    TableOptions: Optional["_TableOptions"]
    TotalOptions: Optional["_TotalOptions"]
    FieldOptions: Optional["_TableFieldOptions"]
    PaginatedReportOptions: Optional["_TablePaginatedReportOptions"]
    TableInlineVisualizations: Optional[Sequence["_TableInlineVisualization"]]

    @classmethod
    def _deserialize(
        cls: Type["_TableConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableConfiguration"]:
        if not json_data:
            return None
        return cls(
            FieldWells=TableFieldWells._deserialize(json_data.get("FieldWells")),
            SortConfiguration=TableSortConfiguration._deserialize(json_data.get("SortConfiguration")),
            TableOptions=TableOptions._deserialize(json_data.get("TableOptions")),
            TotalOptions=TotalOptions._deserialize(json_data.get("TotalOptions")),
            FieldOptions=TableFieldOptions._deserialize(json_data.get("FieldOptions")),
            PaginatedReportOptions=TablePaginatedReportOptions._deserialize(json_data.get("PaginatedReportOptions")),
            TableInlineVisualizations=deserialize_list(json_data.get("TableInlineVisualizations"), TableInlineVisualization),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableConfiguration = TableConfiguration


@dataclass
class TableFieldWells(BaseModel):
    TableAggregatedFieldWells: Optional["_TableAggregatedFieldWells"]
    TableUnaggregatedFieldWells: Optional["_TableUnaggregatedFieldWells"]

    @classmethod
    def _deserialize(
        cls: Type["_TableFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableFieldWells"]:
        if not json_data:
            return None
        return cls(
            TableAggregatedFieldWells=TableAggregatedFieldWells._deserialize(json_data.get("TableAggregatedFieldWells")),
            TableUnaggregatedFieldWells=TableUnaggregatedFieldWells._deserialize(json_data.get("TableUnaggregatedFieldWells")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableFieldWells = TableFieldWells


@dataclass
class TableAggregatedFieldWells(BaseModel):
    GroupBy: Optional[Sequence["_DimensionField"]]
    Values: Optional[Sequence["_MeasureField"]]

    @classmethod
    def _deserialize(
        cls: Type["_TableAggregatedFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableAggregatedFieldWells"]:
        if not json_data:
            return None
        return cls(
            GroupBy=deserialize_list(json_data.get("GroupBy"), DimensionField),
            Values=deserialize_list(json_data.get("Values"), MeasureField),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableAggregatedFieldWells = TableAggregatedFieldWells


@dataclass
class DimensionField(BaseModel):
    NumericalDimensionField: Optional["_NumericalDimensionField"]
    CategoricalDimensionField: Optional["_CategoricalDimensionField"]
    DateDimensionField: Optional["_DateDimensionField"]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionField"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionField"]:
        if not json_data:
            return None
        return cls(
            NumericalDimensionField=NumericalDimensionField._deserialize(json_data.get("NumericalDimensionField")),
            CategoricalDimensionField=CategoricalDimensionField._deserialize(json_data.get("CategoricalDimensionField")),
            DateDimensionField=DateDimensionField._deserialize(json_data.get("DateDimensionField")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionField = DimensionField


@dataclass
class NumericalDimensionField(BaseModel):
    FieldId: Optional[str]
    Column: Optional["_ColumnIdentifier"]
    HierarchyId: Optional[str]
    FormatConfiguration: Optional["_NumberFormatConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_NumericalDimensionField"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumericalDimensionField"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            Column=ColumnIdentifier._deserialize(json_data.get("Column")),
            HierarchyId=json_data.get("HierarchyId"),
            FormatConfiguration=NumberFormatConfiguration._deserialize(json_data.get("FormatConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumericalDimensionField = NumericalDimensionField


@dataclass
class NumberFormatConfiguration(BaseModel):
    FormatConfiguration: Optional["_NumericFormatConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_NumberFormatConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumberFormatConfiguration"]:
        if not json_data:
            return None
        return cls(
            FormatConfiguration=NumericFormatConfiguration._deserialize(json_data.get("FormatConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumberFormatConfiguration = NumberFormatConfiguration


@dataclass
class NumericFormatConfiguration(BaseModel):
    NumberDisplayFormatConfiguration: Optional["_NumberDisplayFormatConfiguration"]
    CurrencyDisplayFormatConfiguration: Optional["_CurrencyDisplayFormatConfiguration"]
    PercentageDisplayFormatConfiguration: Optional["_PercentageDisplayFormatConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_NumericFormatConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumericFormatConfiguration"]:
        if not json_data:
            return None
        return cls(
            NumberDisplayFormatConfiguration=NumberDisplayFormatConfiguration._deserialize(json_data.get("NumberDisplayFormatConfiguration")),
            CurrencyDisplayFormatConfiguration=CurrencyDisplayFormatConfiguration._deserialize(json_data.get("CurrencyDisplayFormatConfiguration")),
            PercentageDisplayFormatConfiguration=PercentageDisplayFormatConfiguration._deserialize(json_data.get("PercentageDisplayFormatConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumericFormatConfiguration = NumericFormatConfiguration


@dataclass
class NumberDisplayFormatConfiguration(BaseModel):
    Prefix: Optional[str]
    Suffix: Optional[str]
    SeparatorConfiguration: Optional["_NumericSeparatorConfiguration"]
    DecimalPlacesConfiguration: Optional["_DecimalPlacesConfiguration"]
    NumberScale: Optional[str]
    NegativeValueConfiguration: Optional["_NegativeValueConfiguration"]
    NullValueFormatConfiguration: Optional["_NullValueFormatConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_NumberDisplayFormatConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumberDisplayFormatConfiguration"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
            Suffix=json_data.get("Suffix"),
            SeparatorConfiguration=NumericSeparatorConfiguration._deserialize(json_data.get("SeparatorConfiguration")),
            DecimalPlacesConfiguration=DecimalPlacesConfiguration._deserialize(json_data.get("DecimalPlacesConfiguration")),
            NumberScale=json_data.get("NumberScale"),
            NegativeValueConfiguration=NegativeValueConfiguration._deserialize(json_data.get("NegativeValueConfiguration")),
            NullValueFormatConfiguration=NullValueFormatConfiguration._deserialize(json_data.get("NullValueFormatConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumberDisplayFormatConfiguration = NumberDisplayFormatConfiguration


@dataclass
class NumericSeparatorConfiguration(BaseModel):
    DecimalSeparator: Optional[str]
    ThousandsSeparator: Optional["_ThousandSeparatorOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_NumericSeparatorConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumericSeparatorConfiguration"]:
        if not json_data:
            return None
        return cls(
            DecimalSeparator=json_data.get("DecimalSeparator"),
            ThousandsSeparator=ThousandSeparatorOptions._deserialize(json_data.get("ThousandsSeparator")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumericSeparatorConfiguration = NumericSeparatorConfiguration


@dataclass
class ThousandSeparatorOptions(BaseModel):
    Symbol: Optional[str]
    Visibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ThousandSeparatorOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThousandSeparatorOptions"]:
        if not json_data:
            return None
        return cls(
            Symbol=json_data.get("Symbol"),
            Visibility=json_data.get("Visibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThousandSeparatorOptions = ThousandSeparatorOptions


@dataclass
class DecimalPlacesConfiguration(BaseModel):
    DecimalPlaces: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DecimalPlacesConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DecimalPlacesConfiguration"]:
        if not json_data:
            return None
        return cls(
            DecimalPlaces=json_data.get("DecimalPlaces"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DecimalPlacesConfiguration = DecimalPlacesConfiguration


@dataclass
class NegativeValueConfiguration(BaseModel):
    DisplayMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NegativeValueConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NegativeValueConfiguration"]:
        if not json_data:
            return None
        return cls(
            DisplayMode=json_data.get("DisplayMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NegativeValueConfiguration = NegativeValueConfiguration


@dataclass
class NullValueFormatConfiguration(BaseModel):
    NullString: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NullValueFormatConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NullValueFormatConfiguration"]:
        if not json_data:
            return None
        return cls(
            NullString=json_data.get("NullString"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NullValueFormatConfiguration = NullValueFormatConfiguration


@dataclass
class CurrencyDisplayFormatConfiguration(BaseModel):
    Prefix: Optional[str]
    Suffix: Optional[str]
    SeparatorConfiguration: Optional["_NumericSeparatorConfiguration"]
    Symbol: Optional[str]
    DecimalPlacesConfiguration: Optional["_DecimalPlacesConfiguration"]
    NumberScale: Optional[str]
    NegativeValueConfiguration: Optional["_NegativeValueConfiguration"]
    NullValueFormatConfiguration: Optional["_NullValueFormatConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_CurrencyDisplayFormatConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CurrencyDisplayFormatConfiguration"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
            Suffix=json_data.get("Suffix"),
            SeparatorConfiguration=NumericSeparatorConfiguration._deserialize(json_data.get("SeparatorConfiguration")),
            Symbol=json_data.get("Symbol"),
            DecimalPlacesConfiguration=DecimalPlacesConfiguration._deserialize(json_data.get("DecimalPlacesConfiguration")),
            NumberScale=json_data.get("NumberScale"),
            NegativeValueConfiguration=NegativeValueConfiguration._deserialize(json_data.get("NegativeValueConfiguration")),
            NullValueFormatConfiguration=NullValueFormatConfiguration._deserialize(json_data.get("NullValueFormatConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CurrencyDisplayFormatConfiguration = CurrencyDisplayFormatConfiguration


@dataclass
class PercentageDisplayFormatConfiguration(BaseModel):
    Prefix: Optional[str]
    Suffix: Optional[str]
    SeparatorConfiguration: Optional["_NumericSeparatorConfiguration"]
    DecimalPlacesConfiguration: Optional["_DecimalPlacesConfiguration"]
    NegativeValueConfiguration: Optional["_NegativeValueConfiguration"]
    NullValueFormatConfiguration: Optional["_NullValueFormatConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_PercentageDisplayFormatConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PercentageDisplayFormatConfiguration"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
            Suffix=json_data.get("Suffix"),
            SeparatorConfiguration=NumericSeparatorConfiguration._deserialize(json_data.get("SeparatorConfiguration")),
            DecimalPlacesConfiguration=DecimalPlacesConfiguration._deserialize(json_data.get("DecimalPlacesConfiguration")),
            NegativeValueConfiguration=NegativeValueConfiguration._deserialize(json_data.get("NegativeValueConfiguration")),
            NullValueFormatConfiguration=NullValueFormatConfiguration._deserialize(json_data.get("NullValueFormatConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PercentageDisplayFormatConfiguration = PercentageDisplayFormatConfiguration


@dataclass
class CategoricalDimensionField(BaseModel):
    FieldId: Optional[str]
    Column: Optional["_ColumnIdentifier"]
    HierarchyId: Optional[str]
    FormatConfiguration: Optional["_StringFormatConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_CategoricalDimensionField"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CategoricalDimensionField"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            Column=ColumnIdentifier._deserialize(json_data.get("Column")),
            HierarchyId=json_data.get("HierarchyId"),
            FormatConfiguration=StringFormatConfiguration._deserialize(json_data.get("FormatConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CategoricalDimensionField = CategoricalDimensionField


@dataclass
class StringFormatConfiguration(BaseModel):
    NullValueFormatConfiguration: Optional["_NullValueFormatConfiguration"]
    NumericFormatConfiguration: Optional["_NumericFormatConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_StringFormatConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringFormatConfiguration"]:
        if not json_data:
            return None
        return cls(
            NullValueFormatConfiguration=NullValueFormatConfiguration._deserialize(json_data.get("NullValueFormatConfiguration")),
            NumericFormatConfiguration=NumericFormatConfiguration._deserialize(json_data.get("NumericFormatConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringFormatConfiguration = StringFormatConfiguration


@dataclass
class DateDimensionField(BaseModel):
    FieldId: Optional[str]
    Column: Optional["_ColumnIdentifier"]
    DateGranularity: Optional[str]
    HierarchyId: Optional[str]
    FormatConfiguration: Optional["_DateTimeFormatConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_DateDimensionField"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DateDimensionField"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            Column=ColumnIdentifier._deserialize(json_data.get("Column")),
            DateGranularity=json_data.get("DateGranularity"),
            HierarchyId=json_data.get("HierarchyId"),
            FormatConfiguration=DateTimeFormatConfiguration._deserialize(json_data.get("FormatConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DateDimensionField = DateDimensionField


@dataclass
class DateTimeFormatConfiguration(BaseModel):
    DateTimeFormat: Optional[str]
    NullValueFormatConfiguration: Optional["_NullValueFormatConfiguration"]
    NumericFormatConfiguration: Optional["_NumericFormatConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_DateTimeFormatConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DateTimeFormatConfiguration"]:
        if not json_data:
            return None
        return cls(
            DateTimeFormat=json_data.get("DateTimeFormat"),
            NullValueFormatConfiguration=NullValueFormatConfiguration._deserialize(json_data.get("NullValueFormatConfiguration")),
            NumericFormatConfiguration=NumericFormatConfiguration._deserialize(json_data.get("NumericFormatConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DateTimeFormatConfiguration = DateTimeFormatConfiguration


@dataclass
class MeasureField(BaseModel):
    NumericalMeasureField: Optional["_NumericalMeasureField"]
    CategoricalMeasureField: Optional["_CategoricalMeasureField"]
    DateMeasureField: Optional["_DateMeasureField"]
    CalculatedMeasureField: Optional["_CalculatedMeasureField"]

    @classmethod
    def _deserialize(
        cls: Type["_MeasureField"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MeasureField"]:
        if not json_data:
            return None
        return cls(
            NumericalMeasureField=NumericalMeasureField._deserialize(json_data.get("NumericalMeasureField")),
            CategoricalMeasureField=CategoricalMeasureField._deserialize(json_data.get("CategoricalMeasureField")),
            DateMeasureField=DateMeasureField._deserialize(json_data.get("DateMeasureField")),
            CalculatedMeasureField=CalculatedMeasureField._deserialize(json_data.get("CalculatedMeasureField")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MeasureField = MeasureField


@dataclass
class NumericalMeasureField(BaseModel):
    FieldId: Optional[str]
    Column: Optional["_ColumnIdentifier"]
    AggregationFunction: Optional["_NumericalAggregationFunction"]
    FormatConfiguration: Optional["_NumberFormatConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_NumericalMeasureField"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumericalMeasureField"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            Column=ColumnIdentifier._deserialize(json_data.get("Column")),
            AggregationFunction=NumericalAggregationFunction._deserialize(json_data.get("AggregationFunction")),
            FormatConfiguration=NumberFormatConfiguration._deserialize(json_data.get("FormatConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumericalMeasureField = NumericalMeasureField


@dataclass
class NumericalAggregationFunction(BaseModel):
    SimpleNumericalAggregation: Optional[str]
    PercentileAggregation: Optional["_PercentileAggregation"]

    @classmethod
    def _deserialize(
        cls: Type["_NumericalAggregationFunction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumericalAggregationFunction"]:
        if not json_data:
            return None
        return cls(
            SimpleNumericalAggregation=json_data.get("SimpleNumericalAggregation"),
            PercentileAggregation=PercentileAggregation._deserialize(json_data.get("PercentileAggregation")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumericalAggregationFunction = NumericalAggregationFunction


@dataclass
class PercentileAggregation(BaseModel):
    PercentileValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PercentileAggregation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PercentileAggregation"]:
        if not json_data:
            return None
        return cls(
            PercentileValue=json_data.get("PercentileValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PercentileAggregation = PercentileAggregation


@dataclass
class CategoricalMeasureField(BaseModel):
    FieldId: Optional[str]
    Column: Optional["_ColumnIdentifier"]
    AggregationFunction: Optional[str]
    FormatConfiguration: Optional["_StringFormatConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_CategoricalMeasureField"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CategoricalMeasureField"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            Column=ColumnIdentifier._deserialize(json_data.get("Column")),
            AggregationFunction=json_data.get("AggregationFunction"),
            FormatConfiguration=StringFormatConfiguration._deserialize(json_data.get("FormatConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CategoricalMeasureField = CategoricalMeasureField


@dataclass
class DateMeasureField(BaseModel):
    FieldId: Optional[str]
    Column: Optional["_ColumnIdentifier"]
    AggregationFunction: Optional[str]
    FormatConfiguration: Optional["_DateTimeFormatConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_DateMeasureField"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DateMeasureField"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            Column=ColumnIdentifier._deserialize(json_data.get("Column")),
            AggregationFunction=json_data.get("AggregationFunction"),
            FormatConfiguration=DateTimeFormatConfiguration._deserialize(json_data.get("FormatConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DateMeasureField = DateMeasureField


@dataclass
class CalculatedMeasureField(BaseModel):
    FieldId: Optional[str]
    Expression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CalculatedMeasureField"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CalculatedMeasureField"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            Expression=json_data.get("Expression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CalculatedMeasureField = CalculatedMeasureField


@dataclass
class TableUnaggregatedFieldWells(BaseModel):
    Values: Optional[Sequence["_UnaggregatedField"]]

    @classmethod
    def _deserialize(
        cls: Type["_TableUnaggregatedFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableUnaggregatedFieldWells"]:
        if not json_data:
            return None
        return cls(
            Values=deserialize_list(json_data.get("Values"), UnaggregatedField),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableUnaggregatedFieldWells = TableUnaggregatedFieldWells


@dataclass
class UnaggregatedField(BaseModel):
    FieldId: Optional[str]
    Column: Optional["_ColumnIdentifier"]
    FormatConfiguration: Optional["_FormatConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_UnaggregatedField"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UnaggregatedField"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            Column=ColumnIdentifier._deserialize(json_data.get("Column")),
            FormatConfiguration=FormatConfiguration._deserialize(json_data.get("FormatConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_UnaggregatedField = UnaggregatedField


@dataclass
class FormatConfiguration(BaseModel):
    StringFormatConfiguration: Optional["_StringFormatConfiguration"]
    NumberFormatConfiguration: Optional["_NumberFormatConfiguration"]
    DateTimeFormatConfiguration: Optional["_DateTimeFormatConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_FormatConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FormatConfiguration"]:
        if not json_data:
            return None
        return cls(
            StringFormatConfiguration=StringFormatConfiguration._deserialize(json_data.get("StringFormatConfiguration")),
            NumberFormatConfiguration=NumberFormatConfiguration._deserialize(json_data.get("NumberFormatConfiguration")),
            DateTimeFormatConfiguration=DateTimeFormatConfiguration._deserialize(json_data.get("DateTimeFormatConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FormatConfiguration = FormatConfiguration


@dataclass
class TableSortConfiguration(BaseModel):
    RowSort: Optional[Sequence["_FieldSortOptions"]]
    PaginationConfiguration: Optional["_PaginationConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_TableSortConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableSortConfiguration"]:
        if not json_data:
            return None
        return cls(
            RowSort=deserialize_list(json_data.get("RowSort"), FieldSortOptions),
            PaginationConfiguration=PaginationConfiguration._deserialize(json_data.get("PaginationConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableSortConfiguration = TableSortConfiguration


@dataclass
class FieldSortOptions(BaseModel):
    FieldSort: Optional["_FieldSort"]
    ColumnSort: Optional["_ColumnSort"]

    @classmethod
    def _deserialize(
        cls: Type["_FieldSortOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldSortOptions"]:
        if not json_data:
            return None
        return cls(
            FieldSort=FieldSort._deserialize(json_data.get("FieldSort")),
            ColumnSort=ColumnSort._deserialize(json_data.get("ColumnSort")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldSortOptions = FieldSortOptions


@dataclass
class FieldSort(BaseModel):
    FieldId: Optional[str]
    Direction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FieldSort"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldSort"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            Direction=json_data.get("Direction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldSort = FieldSort


@dataclass
class ColumnSort(BaseModel):
    SortBy: Optional["_ColumnIdentifier"]
    Direction: Optional[str]
    AggregationFunction: Optional["_AggregationFunction"]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnSort"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnSort"]:
        if not json_data:
            return None
        return cls(
            SortBy=ColumnIdentifier._deserialize(json_data.get("SortBy")),
            Direction=json_data.get("Direction"),
            AggregationFunction=AggregationFunction._deserialize(json_data.get("AggregationFunction")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnSort = ColumnSort


@dataclass
class AggregationFunction(BaseModel):
    NumericalAggregationFunction: Optional["_NumericalAggregationFunction"]
    CategoricalAggregationFunction: Optional[str]
    DateAggregationFunction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AggregationFunction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AggregationFunction"]:
        if not json_data:
            return None
        return cls(
            NumericalAggregationFunction=NumericalAggregationFunction._deserialize(json_data.get("NumericalAggregationFunction")),
            CategoricalAggregationFunction=json_data.get("CategoricalAggregationFunction"),
            DateAggregationFunction=json_data.get("DateAggregationFunction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AggregationFunction = AggregationFunction


@dataclass
class PaginationConfiguration(BaseModel):
    PageSize: Optional[float]
    PageNumber: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PaginationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PaginationConfiguration"]:
        if not json_data:
            return None
        return cls(
            PageSize=json_data.get("PageSize"),
            PageNumber=json_data.get("PageNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PaginationConfiguration = PaginationConfiguration


@dataclass
class TableOptions(BaseModel):
    Orientation: Optional[str]
    HeaderStyle: Optional["_TableCellStyle"]
    CellStyle: Optional["_TableCellStyle"]
    RowAlternateColorOptions: Optional["_RowAlternateColorOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_TableOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableOptions"]:
        if not json_data:
            return None
        return cls(
            Orientation=json_data.get("Orientation"),
            HeaderStyle=TableCellStyle._deserialize(json_data.get("HeaderStyle")),
            CellStyle=TableCellStyle._deserialize(json_data.get("CellStyle")),
            RowAlternateColorOptions=RowAlternateColorOptions._deserialize(json_data.get("RowAlternateColorOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableOptions = TableOptions


@dataclass
class TableCellStyle(BaseModel):
    Visibility: Optional[str]
    FontConfiguration: Optional["_FontConfiguration"]
    TextWrap: Optional[str]
    HorizontalTextAlignment: Optional[str]
    VerticalTextAlignment: Optional[str]
    BackgroundColor: Optional[str]
    Height: Optional[float]
    Border: Optional["_GlobalTableBorderOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_TableCellStyle"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableCellStyle"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
            FontConfiguration=FontConfiguration._deserialize(json_data.get("FontConfiguration")),
            TextWrap=json_data.get("TextWrap"),
            HorizontalTextAlignment=json_data.get("HorizontalTextAlignment"),
            VerticalTextAlignment=json_data.get("VerticalTextAlignment"),
            BackgroundColor=json_data.get("BackgroundColor"),
            Height=json_data.get("Height"),
            Border=GlobalTableBorderOptions._deserialize(json_data.get("Border")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableCellStyle = TableCellStyle


@dataclass
class GlobalTableBorderOptions(BaseModel):
    UniformBorder: Optional["_TableBorderOptions"]
    SideSpecificBorder: Optional["_TableSideBorderOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalTableBorderOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalTableBorderOptions"]:
        if not json_data:
            return None
        return cls(
            UniformBorder=TableBorderOptions._deserialize(json_data.get("UniformBorder")),
            SideSpecificBorder=TableSideBorderOptions._deserialize(json_data.get("SideSpecificBorder")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalTableBorderOptions = GlobalTableBorderOptions


@dataclass
class TableBorderOptions(BaseModel):
    Color: Optional[str]
    Thickness: Optional[float]
    Style: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TableBorderOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableBorderOptions"]:
        if not json_data:
            return None
        return cls(
            Color=json_data.get("Color"),
            Thickness=json_data.get("Thickness"),
            Style=json_data.get("Style"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableBorderOptions = TableBorderOptions


@dataclass
class TableSideBorderOptions(BaseModel):
    InnerVertical: Optional["_TableBorderOptions"]
    InnerHorizontal: Optional["_TableBorderOptions"]
    Left: Optional["_TableBorderOptions"]
    Right: Optional["_TableBorderOptions"]
    Top: Optional["_TableBorderOptions"]
    Bottom: Optional["_TableBorderOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_TableSideBorderOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableSideBorderOptions"]:
        if not json_data:
            return None
        return cls(
            InnerVertical=TableBorderOptions._deserialize(json_data.get("InnerVertical")),
            InnerHorizontal=TableBorderOptions._deserialize(json_data.get("InnerHorizontal")),
            Left=TableBorderOptions._deserialize(json_data.get("Left")),
            Right=TableBorderOptions._deserialize(json_data.get("Right")),
            Top=TableBorderOptions._deserialize(json_data.get("Top")),
            Bottom=TableBorderOptions._deserialize(json_data.get("Bottom")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableSideBorderOptions = TableSideBorderOptions


@dataclass
class RowAlternateColorOptions(BaseModel):
    Status: Optional[str]
    RowAlternateColors: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RowAlternateColorOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RowAlternateColorOptions"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            RowAlternateColors=json_data.get("RowAlternateColors"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RowAlternateColorOptions = RowAlternateColorOptions


@dataclass
class TotalOptions(BaseModel):
    TotalsVisibility: Optional[str]
    Placement: Optional[str]
    ScrollStatus: Optional[str]
    CustomLabel: Optional[str]
    TotalCellStyle: Optional["_TableCellStyle"]

    @classmethod
    def _deserialize(
        cls: Type["_TotalOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TotalOptions"]:
        if not json_data:
            return None
        return cls(
            TotalsVisibility=json_data.get("TotalsVisibility"),
            Placement=json_data.get("Placement"),
            ScrollStatus=json_data.get("ScrollStatus"),
            CustomLabel=json_data.get("CustomLabel"),
            TotalCellStyle=TableCellStyle._deserialize(json_data.get("TotalCellStyle")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TotalOptions = TotalOptions


@dataclass
class TableFieldOptions(BaseModel):
    SelectedFieldOptions: Optional[Sequence["_TableFieldOption"]]
    Order: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TableFieldOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableFieldOptions"]:
        if not json_data:
            return None
        return cls(
            SelectedFieldOptions=deserialize_list(json_data.get("SelectedFieldOptions"), TableFieldOption),
            Order=json_data.get("Order"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableFieldOptions = TableFieldOptions


@dataclass
class TableFieldOption(BaseModel):
    FieldId: Optional[str]
    Width: Optional[str]
    CustomLabel: Optional[str]
    Visibility: Optional[str]
    URLStyling: Optional["_TableFieldURLConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_TableFieldOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableFieldOption"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            Width=json_data.get("Width"),
            CustomLabel=json_data.get("CustomLabel"),
            Visibility=json_data.get("Visibility"),
            URLStyling=TableFieldURLConfiguration._deserialize(json_data.get("URLStyling")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableFieldOption = TableFieldOption


@dataclass
class TableFieldURLConfiguration(BaseModel):
    LinkConfiguration: Optional["_TableFieldLinkConfiguration"]
    ImageConfiguration: Optional["_TableFieldImageConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_TableFieldURLConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableFieldURLConfiguration"]:
        if not json_data:
            return None
        return cls(
            LinkConfiguration=TableFieldLinkConfiguration._deserialize(json_data.get("LinkConfiguration")),
            ImageConfiguration=TableFieldImageConfiguration._deserialize(json_data.get("ImageConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableFieldURLConfiguration = TableFieldURLConfiguration


@dataclass
class TableFieldLinkConfiguration(BaseModel):
    Target: Optional[str]
    Content: Optional["_TableFieldLinkContentConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_TableFieldLinkConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableFieldLinkConfiguration"]:
        if not json_data:
            return None
        return cls(
            Target=json_data.get("Target"),
            Content=TableFieldLinkContentConfiguration._deserialize(json_data.get("Content")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableFieldLinkConfiguration = TableFieldLinkConfiguration


@dataclass
class TableFieldLinkContentConfiguration(BaseModel):
    CustomTextContent: Optional["_TableFieldCustomTextContent"]
    CustomIconContent: Optional["_TableFieldCustomIconContent"]

    @classmethod
    def _deserialize(
        cls: Type["_TableFieldLinkContentConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableFieldLinkContentConfiguration"]:
        if not json_data:
            return None
        return cls(
            CustomTextContent=TableFieldCustomTextContent._deserialize(json_data.get("CustomTextContent")),
            CustomIconContent=TableFieldCustomIconContent._deserialize(json_data.get("CustomIconContent")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableFieldLinkContentConfiguration = TableFieldLinkContentConfiguration


@dataclass
class TableFieldCustomTextContent(BaseModel):
    Value: Optional[str]
    FontConfiguration: Optional["_FontConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_TableFieldCustomTextContent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableFieldCustomTextContent"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            FontConfiguration=FontConfiguration._deserialize(json_data.get("FontConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableFieldCustomTextContent = TableFieldCustomTextContent


@dataclass
class TableFieldCustomIconContent(BaseModel):
    Icon: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TableFieldCustomIconContent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableFieldCustomIconContent"]:
        if not json_data:
            return None
        return cls(
            Icon=json_data.get("Icon"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableFieldCustomIconContent = TableFieldCustomIconContent


@dataclass
class TableFieldImageConfiguration(BaseModel):
    SizingOptions: Optional["_TableCellImageSizingConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_TableFieldImageConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableFieldImageConfiguration"]:
        if not json_data:
            return None
        return cls(
            SizingOptions=TableCellImageSizingConfiguration._deserialize(json_data.get("SizingOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableFieldImageConfiguration = TableFieldImageConfiguration


@dataclass
class TableCellImageSizingConfiguration(BaseModel):
    TableCellImageScalingConfiguration: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TableCellImageSizingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableCellImageSizingConfiguration"]:
        if not json_data:
            return None
        return cls(
            TableCellImageScalingConfiguration=json_data.get("TableCellImageScalingConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableCellImageSizingConfiguration = TableCellImageSizingConfiguration


@dataclass
class TablePaginatedReportOptions(BaseModel):
    VerticalOverflowVisibility: Optional[str]
    OverflowColumnHeaderVisibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TablePaginatedReportOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TablePaginatedReportOptions"]:
        if not json_data:
            return None
        return cls(
            VerticalOverflowVisibility=json_data.get("VerticalOverflowVisibility"),
            OverflowColumnHeaderVisibility=json_data.get("OverflowColumnHeaderVisibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TablePaginatedReportOptions = TablePaginatedReportOptions


@dataclass
class TableInlineVisualization(BaseModel):
    DataBars: Optional["_DataBarsOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_TableInlineVisualization"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableInlineVisualization"]:
        if not json_data:
            return None
        return cls(
            DataBars=DataBarsOptions._deserialize(json_data.get("DataBars")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableInlineVisualization = TableInlineVisualization


@dataclass
class DataBarsOptions(BaseModel):
    FieldId: Optional[str]
    PositiveColor: Optional[str]
    NegativeColor: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataBarsOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataBarsOptions"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            PositiveColor=json_data.get("PositiveColor"),
            NegativeColor=json_data.get("NegativeColor"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataBarsOptions = DataBarsOptions


@dataclass
class TableConditionalFormatting(BaseModel):
    ConditionalFormattingOptions: Optional[Sequence["_TableConditionalFormattingOption"]]

    @classmethod
    def _deserialize(
        cls: Type["_TableConditionalFormatting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableConditionalFormatting"]:
        if not json_data:
            return None
        return cls(
            ConditionalFormattingOptions=deserialize_list(json_data.get("ConditionalFormattingOptions"), TableConditionalFormattingOption),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableConditionalFormatting = TableConditionalFormatting


@dataclass
class TableConditionalFormattingOption(BaseModel):
    Cell: Optional["_TableCellConditionalFormatting"]
    Row: Optional["_TableRowConditionalFormatting"]

    @classmethod
    def _deserialize(
        cls: Type["_TableConditionalFormattingOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableConditionalFormattingOption"]:
        if not json_data:
            return None
        return cls(
            Cell=TableCellConditionalFormatting._deserialize(json_data.get("Cell")),
            Row=TableRowConditionalFormatting._deserialize(json_data.get("Row")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableConditionalFormattingOption = TableConditionalFormattingOption


@dataclass
class TableCellConditionalFormatting(BaseModel):
    FieldId: Optional[str]
    TextFormat: Optional["_TextConditionalFormat"]

    @classmethod
    def _deserialize(
        cls: Type["_TableCellConditionalFormatting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableCellConditionalFormatting"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            TextFormat=TextConditionalFormat._deserialize(json_data.get("TextFormat")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableCellConditionalFormatting = TableCellConditionalFormatting


@dataclass
class TextConditionalFormat(BaseModel):
    BackgroundColor: Optional["_ConditionalFormattingColor"]
    TextColor: Optional["_ConditionalFormattingColor"]
    Icon: Optional["_ConditionalFormattingIcon"]

    @classmethod
    def _deserialize(
        cls: Type["_TextConditionalFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TextConditionalFormat"]:
        if not json_data:
            return None
        return cls(
            BackgroundColor=ConditionalFormattingColor._deserialize(json_data.get("BackgroundColor")),
            TextColor=ConditionalFormattingColor._deserialize(json_data.get("TextColor")),
            Icon=ConditionalFormattingIcon._deserialize(json_data.get("Icon")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TextConditionalFormat = TextConditionalFormat


@dataclass
class ConditionalFormattingColor(BaseModel):
    Solid: Optional["_ConditionalFormattingSolidColor"]
    Gradient: Optional["_ConditionalFormattingGradientColor"]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionalFormattingColor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionalFormattingColor"]:
        if not json_data:
            return None
        return cls(
            Solid=ConditionalFormattingSolidColor._deserialize(json_data.get("Solid")),
            Gradient=ConditionalFormattingGradientColor._deserialize(json_data.get("Gradient")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionalFormattingColor = ConditionalFormattingColor


@dataclass
class ConditionalFormattingSolidColor(BaseModel):
    Expression: Optional[str]
    Color: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionalFormattingSolidColor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionalFormattingSolidColor"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            Color=json_data.get("Color"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionalFormattingSolidColor = ConditionalFormattingSolidColor


@dataclass
class ConditionalFormattingGradientColor(BaseModel):
    Expression: Optional[str]
    Color: Optional["_GradientColor"]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionalFormattingGradientColor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionalFormattingGradientColor"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            Color=GradientColor._deserialize(json_data.get("Color")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionalFormattingGradientColor = ConditionalFormattingGradientColor


@dataclass
class GradientColor(BaseModel):
    Stops: Optional[Sequence["_GradientStop"]]

    @classmethod
    def _deserialize(
        cls: Type["_GradientColor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GradientColor"]:
        if not json_data:
            return None
        return cls(
            Stops=deserialize_list(json_data.get("Stops"), GradientStop),
        )


# work around possible type aliasing issues when variable has same name as a model
_GradientColor = GradientColor


@dataclass
class GradientStop(BaseModel):
    GradientOffset: Optional[float]
    DataValue: Optional[float]
    Color: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GradientStop"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GradientStop"]:
        if not json_data:
            return None
        return cls(
            GradientOffset=json_data.get("GradientOffset"),
            DataValue=json_data.get("DataValue"),
            Color=json_data.get("Color"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GradientStop = GradientStop


@dataclass
class ConditionalFormattingIcon(BaseModel):
    IconSet: Optional["_ConditionalFormattingIconSet"]
    CustomCondition: Optional["_ConditionalFormattingCustomIconCondition"]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionalFormattingIcon"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionalFormattingIcon"]:
        if not json_data:
            return None
        return cls(
            IconSet=ConditionalFormattingIconSet._deserialize(json_data.get("IconSet")),
            CustomCondition=ConditionalFormattingCustomIconCondition._deserialize(json_data.get("CustomCondition")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionalFormattingIcon = ConditionalFormattingIcon


@dataclass
class ConditionalFormattingIconSet(BaseModel):
    Expression: Optional[str]
    IconSetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionalFormattingIconSet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionalFormattingIconSet"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            IconSetType=json_data.get("IconSetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionalFormattingIconSet = ConditionalFormattingIconSet


@dataclass
class ConditionalFormattingCustomIconCondition(BaseModel):
    Expression: Optional[str]
    IconOptions: Optional["_ConditionalFormattingCustomIconOptions"]
    Color: Optional[str]
    DisplayConfiguration: Optional["_ConditionalFormattingIconDisplayConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionalFormattingCustomIconCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionalFormattingCustomIconCondition"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            IconOptions=ConditionalFormattingCustomIconOptions._deserialize(json_data.get("IconOptions")),
            Color=json_data.get("Color"),
            DisplayConfiguration=ConditionalFormattingIconDisplayConfiguration._deserialize(json_data.get("DisplayConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionalFormattingCustomIconCondition = ConditionalFormattingCustomIconCondition


@dataclass
class ConditionalFormattingCustomIconOptions(BaseModel):
    Icon: Optional[str]
    UnicodeIcon: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionalFormattingCustomIconOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionalFormattingCustomIconOptions"]:
        if not json_data:
            return None
        return cls(
            Icon=json_data.get("Icon"),
            UnicodeIcon=json_data.get("UnicodeIcon"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionalFormattingCustomIconOptions = ConditionalFormattingCustomIconOptions


@dataclass
class ConditionalFormattingIconDisplayConfiguration(BaseModel):
    IconDisplayOption: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionalFormattingIconDisplayConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionalFormattingIconDisplayConfiguration"]:
        if not json_data:
            return None
        return cls(
            IconDisplayOption=json_data.get("IconDisplayOption"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionalFormattingIconDisplayConfiguration = ConditionalFormattingIconDisplayConfiguration


@dataclass
class TableRowConditionalFormatting(BaseModel):
    BackgroundColor: Optional["_ConditionalFormattingColor"]
    TextColor: Optional["_ConditionalFormattingColor"]

    @classmethod
    def _deserialize(
        cls: Type["_TableRowConditionalFormatting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableRowConditionalFormatting"]:
        if not json_data:
            return None
        return cls(
            BackgroundColor=ConditionalFormattingColor._deserialize(json_data.get("BackgroundColor")),
            TextColor=ConditionalFormattingColor._deserialize(json_data.get("TextColor")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableRowConditionalFormatting = TableRowConditionalFormatting


@dataclass
class VisualCustomAction(BaseModel):
    CustomActionId: Optional[str]
    Name: Optional[str]
    Status: Optional[str]
    Trigger: Optional[str]
    ActionOperations: Optional[Sequence["_VisualCustomActionOperation"]]

    @classmethod
    def _deserialize(
        cls: Type["_VisualCustomAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VisualCustomAction"]:
        if not json_data:
            return None
        return cls(
            CustomActionId=json_data.get("CustomActionId"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            Trigger=json_data.get("Trigger"),
            ActionOperations=deserialize_list(json_data.get("ActionOperations"), VisualCustomActionOperation),
        )


# work around possible type aliasing issues when variable has same name as a model
_VisualCustomAction = VisualCustomAction


@dataclass
class VisualCustomActionOperation(BaseModel):
    FilterOperation: Optional["_CustomActionFilterOperation"]
    NavigationOperation: Optional["_CustomActionNavigationOperation"]
    URLOperation: Optional["_CustomActionURLOperation"]
    SetParametersOperation: Optional["_CustomActionSetParametersOperation"]

    @classmethod
    def _deserialize(
        cls: Type["_VisualCustomActionOperation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VisualCustomActionOperation"]:
        if not json_data:
            return None
        return cls(
            FilterOperation=CustomActionFilterOperation._deserialize(json_data.get("FilterOperation")),
            NavigationOperation=CustomActionNavigationOperation._deserialize(json_data.get("NavigationOperation")),
            URLOperation=CustomActionURLOperation._deserialize(json_data.get("URLOperation")),
            SetParametersOperation=CustomActionSetParametersOperation._deserialize(json_data.get("SetParametersOperation")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VisualCustomActionOperation = VisualCustomActionOperation


@dataclass
class CustomActionFilterOperation(BaseModel):
    SelectedFieldsConfiguration: Optional["_FilterOperationSelectedFieldsConfiguration"]
    TargetVisualsConfiguration: Optional["_FilterOperationTargetVisualsConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_CustomActionFilterOperation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomActionFilterOperation"]:
        if not json_data:
            return None
        return cls(
            SelectedFieldsConfiguration=FilterOperationSelectedFieldsConfiguration._deserialize(json_data.get("SelectedFieldsConfiguration")),
            TargetVisualsConfiguration=FilterOperationTargetVisualsConfiguration._deserialize(json_data.get("TargetVisualsConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomActionFilterOperation = CustomActionFilterOperation


@dataclass
class FilterOperationSelectedFieldsConfiguration(BaseModel):
    SelectedFields: Optional[Sequence[str]]
    SelectedFieldOptions: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterOperationSelectedFieldsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterOperationSelectedFieldsConfiguration"]:
        if not json_data:
            return None
        return cls(
            SelectedFields=json_data.get("SelectedFields"),
            SelectedFieldOptions=json_data.get("SelectedFieldOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterOperationSelectedFieldsConfiguration = FilterOperationSelectedFieldsConfiguration


@dataclass
class FilterOperationTargetVisualsConfiguration(BaseModel):
    SameSheetTargetVisualConfiguration: Optional["_SameSheetTargetVisualConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_FilterOperationTargetVisualsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterOperationTargetVisualsConfiguration"]:
        if not json_data:
            return None
        return cls(
            SameSheetTargetVisualConfiguration=SameSheetTargetVisualConfiguration._deserialize(json_data.get("SameSheetTargetVisualConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterOperationTargetVisualsConfiguration = FilterOperationTargetVisualsConfiguration


@dataclass
class SameSheetTargetVisualConfiguration(BaseModel):
    TargetVisuals: Optional[Sequence[str]]
    TargetVisualOptions: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SameSheetTargetVisualConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SameSheetTargetVisualConfiguration"]:
        if not json_data:
            return None
        return cls(
            TargetVisuals=json_data.get("TargetVisuals"),
            TargetVisualOptions=json_data.get("TargetVisualOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SameSheetTargetVisualConfiguration = SameSheetTargetVisualConfiguration


@dataclass
class CustomActionNavigationOperation(BaseModel):
    LocalNavigationConfiguration: Optional["_LocalNavigationConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_CustomActionNavigationOperation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomActionNavigationOperation"]:
        if not json_data:
            return None
        return cls(
            LocalNavigationConfiguration=LocalNavigationConfiguration._deserialize(json_data.get("LocalNavigationConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomActionNavigationOperation = CustomActionNavigationOperation


@dataclass
class LocalNavigationConfiguration(BaseModel):
    TargetSheetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LocalNavigationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalNavigationConfiguration"]:
        if not json_data:
            return None
        return cls(
            TargetSheetId=json_data.get("TargetSheetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalNavigationConfiguration = LocalNavigationConfiguration


@dataclass
class CustomActionURLOperation(BaseModel):
    URLTemplate: Optional[str]
    URLTarget: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomActionURLOperation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomActionURLOperation"]:
        if not json_data:
            return None
        return cls(
            URLTemplate=json_data.get("URLTemplate"),
            URLTarget=json_data.get("URLTarget"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomActionURLOperation = CustomActionURLOperation


@dataclass
class CustomActionSetParametersOperation(BaseModel):
    ParameterValueConfigurations: Optional[Sequence["_SetParameterValueConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomActionSetParametersOperation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomActionSetParametersOperation"]:
        if not json_data:
            return None
        return cls(
            ParameterValueConfigurations=deserialize_list(json_data.get("ParameterValueConfigurations"), SetParameterValueConfiguration),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomActionSetParametersOperation = CustomActionSetParametersOperation


@dataclass
class SetParameterValueConfiguration(BaseModel):
    DestinationParameterName: Optional[str]
    Value: Optional["_DestinationParameterValueConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_SetParameterValueConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SetParameterValueConfiguration"]:
        if not json_data:
            return None
        return cls(
            DestinationParameterName=json_data.get("DestinationParameterName"),
            Value=DestinationParameterValueConfiguration._deserialize(json_data.get("Value")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SetParameterValueConfiguration = SetParameterValueConfiguration


@dataclass
class DestinationParameterValueConfiguration(BaseModel):
    CustomValuesConfiguration: Optional["_CustomValuesConfiguration"]
    SelectAllValueOptions: Optional[str]
    SourceParameterName: Optional[str]
    SourceField: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationParameterValueConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationParameterValueConfiguration"]:
        if not json_data:
            return None
        return cls(
            CustomValuesConfiguration=CustomValuesConfiguration._deserialize(json_data.get("CustomValuesConfiguration")),
            SelectAllValueOptions=json_data.get("SelectAllValueOptions"),
            SourceParameterName=json_data.get("SourceParameterName"),
            SourceField=json_data.get("SourceField"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationParameterValueConfiguration = DestinationParameterValueConfiguration


@dataclass
class CustomValuesConfiguration(BaseModel):
    IncludeNullValue: Optional[bool]
    CustomValues: Optional["_CustomParameterValues"]

    @classmethod
    def _deserialize(
        cls: Type["_CustomValuesConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomValuesConfiguration"]:
        if not json_data:
            return None
        return cls(
            IncludeNullValue=json_data.get("IncludeNullValue"),
            CustomValues=CustomParameterValues._deserialize(json_data.get("CustomValues")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomValuesConfiguration = CustomValuesConfiguration


@dataclass
class CustomParameterValues(BaseModel):
    StringValues: Optional[Sequence[str]]
    IntegerValues: Optional[Sequence[float]]
    DecimalValues: Optional[Sequence[float]]
    DateTimeValues: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomParameterValues"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomParameterValues"]:
        if not json_data:
            return None
        return cls(
            StringValues=json_data.get("StringValues"),
            IntegerValues=json_data.get("IntegerValues"),
            DecimalValues=json_data.get("DecimalValues"),
            DateTimeValues=json_data.get("DateTimeValues"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomParameterValues = CustomParameterValues


@dataclass
class PivotTableVisual(BaseModel):
    VisualId: Optional[str]
    Title: Optional["_VisualTitleLabelOptions"]
    Subtitle: Optional["_VisualSubtitleLabelOptions"]
    ChartConfiguration: Optional["_PivotTableConfiguration"]
    ConditionalFormatting: Optional["_PivotTableConditionalFormatting"]
    Actions: Optional[Sequence["_VisualCustomAction"]]

    @classmethod
    def _deserialize(
        cls: Type["_PivotTableVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PivotTableVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            Title=VisualTitleLabelOptions._deserialize(json_data.get("Title")),
            Subtitle=VisualSubtitleLabelOptions._deserialize(json_data.get("Subtitle")),
            ChartConfiguration=PivotTableConfiguration._deserialize(json_data.get("ChartConfiguration")),
            ConditionalFormatting=PivotTableConditionalFormatting._deserialize(json_data.get("ConditionalFormatting")),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
        )


# work around possible type aliasing issues when variable has same name as a model
_PivotTableVisual = PivotTableVisual


@dataclass
class PivotTableConfiguration(BaseModel):
    FieldWells: Optional["_PivotTableFieldWells"]
    SortConfiguration: Optional["_PivotTableSortConfiguration"]
    TableOptions: Optional["_PivotTableOptions"]
    TotalOptions: Optional["_PivotTableTotalOptions"]
    FieldOptions: Optional["_PivotTableFieldOptions"]
    PaginatedReportOptions: Optional["_PivotTablePaginatedReportOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_PivotTableConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PivotTableConfiguration"]:
        if not json_data:
            return None
        return cls(
            FieldWells=PivotTableFieldWells._deserialize(json_data.get("FieldWells")),
            SortConfiguration=PivotTableSortConfiguration._deserialize(json_data.get("SortConfiguration")),
            TableOptions=PivotTableOptions._deserialize(json_data.get("TableOptions")),
            TotalOptions=PivotTableTotalOptions._deserialize(json_data.get("TotalOptions")),
            FieldOptions=PivotTableFieldOptions._deserialize(json_data.get("FieldOptions")),
            PaginatedReportOptions=PivotTablePaginatedReportOptions._deserialize(json_data.get("PaginatedReportOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PivotTableConfiguration = PivotTableConfiguration


@dataclass
class PivotTableFieldWells(BaseModel):
    PivotTableAggregatedFieldWells: Optional["_PivotTableAggregatedFieldWells"]

    @classmethod
    def _deserialize(
        cls: Type["_PivotTableFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PivotTableFieldWells"]:
        if not json_data:
            return None
        return cls(
            PivotTableAggregatedFieldWells=PivotTableAggregatedFieldWells._deserialize(json_data.get("PivotTableAggregatedFieldWells")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PivotTableFieldWells = PivotTableFieldWells


@dataclass
class PivotTableAggregatedFieldWells(BaseModel):
    Rows: Optional[Sequence["_DimensionField"]]
    Columns: Optional[Sequence["_DimensionField"]]
    Values: Optional[Sequence["_MeasureField"]]

    @classmethod
    def _deserialize(
        cls: Type["_PivotTableAggregatedFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PivotTableAggregatedFieldWells"]:
        if not json_data:
            return None
        return cls(
            Rows=deserialize_list(json_data.get("Rows"), DimensionField),
            Columns=deserialize_list(json_data.get("Columns"), DimensionField),
            Values=deserialize_list(json_data.get("Values"), MeasureField),
        )


# work around possible type aliasing issues when variable has same name as a model
_PivotTableAggregatedFieldWells = PivotTableAggregatedFieldWells


@dataclass
class PivotTableSortConfiguration(BaseModel):
    FieldSortOptions: Optional[Sequence["_PivotFieldSortOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_PivotTableSortConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PivotTableSortConfiguration"]:
        if not json_data:
            return None
        return cls(
            FieldSortOptions=deserialize_list(json_data.get("FieldSortOptions"), PivotFieldSortOptions),
        )


# work around possible type aliasing issues when variable has same name as a model
_PivotTableSortConfiguration = PivotTableSortConfiguration


@dataclass
class PivotFieldSortOptions(BaseModel):
    FieldId: Optional[str]
    SortBy: Optional["_PivotTableSortBy"]

    @classmethod
    def _deserialize(
        cls: Type["_PivotFieldSortOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PivotFieldSortOptions"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            SortBy=PivotTableSortBy._deserialize(json_data.get("SortBy")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PivotFieldSortOptions = PivotFieldSortOptions


@dataclass
class PivotTableSortBy(BaseModel):
    Field: Optional["_FieldSort"]
    Column: Optional["_ColumnSort"]
    DataPath: Optional["_DataPathSort"]

    @classmethod
    def _deserialize(
        cls: Type["_PivotTableSortBy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PivotTableSortBy"]:
        if not json_data:
            return None
        return cls(
            Field=FieldSort._deserialize(json_data.get("Field")),
            Column=ColumnSort._deserialize(json_data.get("Column")),
            DataPath=DataPathSort._deserialize(json_data.get("DataPath")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PivotTableSortBy = PivotTableSortBy


@dataclass
class DataPathSort(BaseModel):
    Direction: Optional[str]
    SortPaths: Optional[Sequence["_DataPathValue"]]

    @classmethod
    def _deserialize(
        cls: Type["_DataPathSort"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataPathSort"]:
        if not json_data:
            return None
        return cls(
            Direction=json_data.get("Direction"),
            SortPaths=deserialize_list(json_data.get("SortPaths"), DataPathValue),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataPathSort = DataPathSort


@dataclass
class DataPathValue(BaseModel):
    FieldId: Optional[str]
    FieldValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataPathValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataPathValue"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            FieldValue=json_data.get("FieldValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataPathValue = DataPathValue


@dataclass
class PivotTableOptions(BaseModel):
    MetricPlacement: Optional[str]
    SingleMetricVisibility: Optional[str]
    ColumnNamesVisibility: Optional[str]
    ToggleButtonsVisibility: Optional[str]
    ColumnHeaderStyle: Optional["_TableCellStyle"]
    RowHeaderStyle: Optional["_TableCellStyle"]
    CellStyle: Optional["_TableCellStyle"]
    RowFieldNamesStyle: Optional["_TableCellStyle"]
    RowAlternateColorOptions: Optional["_RowAlternateColorOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_PivotTableOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PivotTableOptions"]:
        if not json_data:
            return None
        return cls(
            MetricPlacement=json_data.get("MetricPlacement"),
            SingleMetricVisibility=json_data.get("SingleMetricVisibility"),
            ColumnNamesVisibility=json_data.get("ColumnNamesVisibility"),
            ToggleButtonsVisibility=json_data.get("ToggleButtonsVisibility"),
            ColumnHeaderStyle=TableCellStyle._deserialize(json_data.get("ColumnHeaderStyle")),
            RowHeaderStyle=TableCellStyle._deserialize(json_data.get("RowHeaderStyle")),
            CellStyle=TableCellStyle._deserialize(json_data.get("CellStyle")),
            RowFieldNamesStyle=TableCellStyle._deserialize(json_data.get("RowFieldNamesStyle")),
            RowAlternateColorOptions=RowAlternateColorOptions._deserialize(json_data.get("RowAlternateColorOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PivotTableOptions = PivotTableOptions


@dataclass
class PivotTableTotalOptions(BaseModel):
    RowSubtotalOptions: Optional["_SubtotalOptions"]
    ColumnSubtotalOptions: Optional["_SubtotalOptions"]
    RowTotalOptions: Optional["_PivotTotalOptions"]
    ColumnTotalOptions: Optional["_PivotTotalOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_PivotTableTotalOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PivotTableTotalOptions"]:
        if not json_data:
            return None
        return cls(
            RowSubtotalOptions=SubtotalOptions._deserialize(json_data.get("RowSubtotalOptions")),
            ColumnSubtotalOptions=SubtotalOptions._deserialize(json_data.get("ColumnSubtotalOptions")),
            RowTotalOptions=PivotTotalOptions._deserialize(json_data.get("RowTotalOptions")),
            ColumnTotalOptions=PivotTotalOptions._deserialize(json_data.get("ColumnTotalOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PivotTableTotalOptions = PivotTableTotalOptions


@dataclass
class SubtotalOptions(BaseModel):
    TotalsVisibility: Optional[str]
    CustomLabel: Optional[str]
    FieldLevel: Optional[str]
    FieldLevelOptions: Optional[Sequence["_PivotTableFieldSubtotalOptions"]]
    TotalCellStyle: Optional["_TableCellStyle"]
    ValueCellStyle: Optional["_TableCellStyle"]
    MetricHeaderCellStyle: Optional["_TableCellStyle"]

    @classmethod
    def _deserialize(
        cls: Type["_SubtotalOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubtotalOptions"]:
        if not json_data:
            return None
        return cls(
            TotalsVisibility=json_data.get("TotalsVisibility"),
            CustomLabel=json_data.get("CustomLabel"),
            FieldLevel=json_data.get("FieldLevel"),
            FieldLevelOptions=deserialize_list(json_data.get("FieldLevelOptions"), PivotTableFieldSubtotalOptions),
            TotalCellStyle=TableCellStyle._deserialize(json_data.get("TotalCellStyle")),
            ValueCellStyle=TableCellStyle._deserialize(json_data.get("ValueCellStyle")),
            MetricHeaderCellStyle=TableCellStyle._deserialize(json_data.get("MetricHeaderCellStyle")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubtotalOptions = SubtotalOptions


@dataclass
class PivotTableFieldSubtotalOptions(BaseModel):
    FieldId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PivotTableFieldSubtotalOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PivotTableFieldSubtotalOptions"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PivotTableFieldSubtotalOptions = PivotTableFieldSubtotalOptions


@dataclass
class PivotTotalOptions(BaseModel):
    TotalsVisibility: Optional[str]
    Placement: Optional[str]
    ScrollStatus: Optional[str]
    CustomLabel: Optional[str]
    TotalCellStyle: Optional["_TableCellStyle"]
    ValueCellStyle: Optional["_TableCellStyle"]
    MetricHeaderCellStyle: Optional["_TableCellStyle"]

    @classmethod
    def _deserialize(
        cls: Type["_PivotTotalOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PivotTotalOptions"]:
        if not json_data:
            return None
        return cls(
            TotalsVisibility=json_data.get("TotalsVisibility"),
            Placement=json_data.get("Placement"),
            ScrollStatus=json_data.get("ScrollStatus"),
            CustomLabel=json_data.get("CustomLabel"),
            TotalCellStyle=TableCellStyle._deserialize(json_data.get("TotalCellStyle")),
            ValueCellStyle=TableCellStyle._deserialize(json_data.get("ValueCellStyle")),
            MetricHeaderCellStyle=TableCellStyle._deserialize(json_data.get("MetricHeaderCellStyle")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PivotTotalOptions = PivotTotalOptions


@dataclass
class PivotTableFieldOptions(BaseModel):
    SelectedFieldOptions: Optional[Sequence["_PivotTableFieldOption"]]
    DataPathOptions: Optional[Sequence["_PivotTableDataPathOption"]]

    @classmethod
    def _deserialize(
        cls: Type["_PivotTableFieldOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PivotTableFieldOptions"]:
        if not json_data:
            return None
        return cls(
            SelectedFieldOptions=deserialize_list(json_data.get("SelectedFieldOptions"), PivotTableFieldOption),
            DataPathOptions=deserialize_list(json_data.get("DataPathOptions"), PivotTableDataPathOption),
        )


# work around possible type aliasing issues when variable has same name as a model
_PivotTableFieldOptions = PivotTableFieldOptions


@dataclass
class PivotTableFieldOption(BaseModel):
    FieldId: Optional[str]
    CustomLabel: Optional[str]
    Visibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PivotTableFieldOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PivotTableFieldOption"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            CustomLabel=json_data.get("CustomLabel"),
            Visibility=json_data.get("Visibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PivotTableFieldOption = PivotTableFieldOption


@dataclass
class PivotTableDataPathOption(BaseModel):
    DataPathList: Optional[Sequence["_DataPathValue"]]
    Width: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PivotTableDataPathOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PivotTableDataPathOption"]:
        if not json_data:
            return None
        return cls(
            DataPathList=deserialize_list(json_data.get("DataPathList"), DataPathValue),
            Width=json_data.get("Width"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PivotTableDataPathOption = PivotTableDataPathOption


@dataclass
class PivotTablePaginatedReportOptions(BaseModel):
    VerticalOverflowVisibility: Optional[str]
    OverflowColumnHeaderVisibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PivotTablePaginatedReportOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PivotTablePaginatedReportOptions"]:
        if not json_data:
            return None
        return cls(
            VerticalOverflowVisibility=json_data.get("VerticalOverflowVisibility"),
            OverflowColumnHeaderVisibility=json_data.get("OverflowColumnHeaderVisibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PivotTablePaginatedReportOptions = PivotTablePaginatedReportOptions


@dataclass
class PivotTableConditionalFormatting(BaseModel):
    ConditionalFormattingOptions: Optional[Sequence["_PivotTableConditionalFormattingOption"]]

    @classmethod
    def _deserialize(
        cls: Type["_PivotTableConditionalFormatting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PivotTableConditionalFormatting"]:
        if not json_data:
            return None
        return cls(
            ConditionalFormattingOptions=deserialize_list(json_data.get("ConditionalFormattingOptions"), PivotTableConditionalFormattingOption),
        )


# work around possible type aliasing issues when variable has same name as a model
_PivotTableConditionalFormatting = PivotTableConditionalFormatting


@dataclass
class PivotTableConditionalFormattingOption(BaseModel):
    Cell: Optional["_PivotTableCellConditionalFormatting"]

    @classmethod
    def _deserialize(
        cls: Type["_PivotTableConditionalFormattingOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PivotTableConditionalFormattingOption"]:
        if not json_data:
            return None
        return cls(
            Cell=PivotTableCellConditionalFormatting._deserialize(json_data.get("Cell")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PivotTableConditionalFormattingOption = PivotTableConditionalFormattingOption


@dataclass
class PivotTableCellConditionalFormatting(BaseModel):
    FieldId: Optional[str]
    TextFormat: Optional["_TextConditionalFormat"]
    Scope: Optional["_PivotTableConditionalFormattingScope"]

    @classmethod
    def _deserialize(
        cls: Type["_PivotTableCellConditionalFormatting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PivotTableCellConditionalFormatting"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            TextFormat=TextConditionalFormat._deserialize(json_data.get("TextFormat")),
            Scope=PivotTableConditionalFormattingScope._deserialize(json_data.get("Scope")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PivotTableCellConditionalFormatting = PivotTableCellConditionalFormatting


@dataclass
class PivotTableConditionalFormattingScope(BaseModel):
    Role: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PivotTableConditionalFormattingScope"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PivotTableConditionalFormattingScope"]:
        if not json_data:
            return None
        return cls(
            Role=json_data.get("Role"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PivotTableConditionalFormattingScope = PivotTableConditionalFormattingScope


@dataclass
class BarChartVisual(BaseModel):
    VisualId: Optional[str]
    Title: Optional["_VisualTitleLabelOptions"]
    Subtitle: Optional["_VisualSubtitleLabelOptions"]
    ChartConfiguration: Optional["_BarChartConfiguration"]
    Actions: Optional[Sequence["_VisualCustomAction"]]
    ColumnHierarchies: Optional[Sequence["_ColumnHierarchy"]]

    @classmethod
    def _deserialize(
        cls: Type["_BarChartVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BarChartVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            Title=VisualTitleLabelOptions._deserialize(json_data.get("Title")),
            Subtitle=VisualSubtitleLabelOptions._deserialize(json_data.get("Subtitle")),
            ChartConfiguration=BarChartConfiguration._deserialize(json_data.get("ChartConfiguration")),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
            ColumnHierarchies=deserialize_list(json_data.get("ColumnHierarchies"), ColumnHierarchy),
        )


# work around possible type aliasing issues when variable has same name as a model
_BarChartVisual = BarChartVisual


@dataclass
class BarChartConfiguration(BaseModel):
    FieldWells: Optional["_BarChartFieldWells"]
    SortConfiguration: Optional["_BarChartSortConfiguration"]
    Orientation: Optional[str]
    BarsArrangement: Optional[str]
    VisualPalette: Optional["_VisualPalette"]
    SmallMultiplesOptions: Optional["_SmallMultiplesOptions"]
    CategoryAxis: Optional["_AxisDisplayOptions"]
    CategoryLabelOptions: Optional["_ChartAxisLabelOptions"]
    ValueAxis: Optional["_AxisDisplayOptions"]
    ValueLabelOptions: Optional["_ChartAxisLabelOptions"]
    ColorLabelOptions: Optional["_ChartAxisLabelOptions"]
    Legend: Optional["_LegendOptions"]
    DataLabels: Optional["_DataLabelOptions"]
    Tooltip: Optional["_TooltipOptions"]
    ReferenceLines: Optional[Sequence["_ReferenceLine"]]
    ContributionAnalysisDefaults: Optional[Sequence["_ContributionAnalysisDefault"]]

    @classmethod
    def _deserialize(
        cls: Type["_BarChartConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BarChartConfiguration"]:
        if not json_data:
            return None
        return cls(
            FieldWells=BarChartFieldWells._deserialize(json_data.get("FieldWells")),
            SortConfiguration=BarChartSortConfiguration._deserialize(json_data.get("SortConfiguration")),
            Orientation=json_data.get("Orientation"),
            BarsArrangement=json_data.get("BarsArrangement"),
            VisualPalette=VisualPalette._deserialize(json_data.get("VisualPalette")),
            SmallMultiplesOptions=SmallMultiplesOptions._deserialize(json_data.get("SmallMultiplesOptions")),
            CategoryAxis=AxisDisplayOptions._deserialize(json_data.get("CategoryAxis")),
            CategoryLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("CategoryLabelOptions")),
            ValueAxis=AxisDisplayOptions._deserialize(json_data.get("ValueAxis")),
            ValueLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("ValueLabelOptions")),
            ColorLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("ColorLabelOptions")),
            Legend=LegendOptions._deserialize(json_data.get("Legend")),
            DataLabels=DataLabelOptions._deserialize(json_data.get("DataLabels")),
            Tooltip=TooltipOptions._deserialize(json_data.get("Tooltip")),
            ReferenceLines=deserialize_list(json_data.get("ReferenceLines"), ReferenceLine),
            ContributionAnalysisDefaults=deserialize_list(json_data.get("ContributionAnalysisDefaults"), ContributionAnalysisDefault),
        )


# work around possible type aliasing issues when variable has same name as a model
_BarChartConfiguration = BarChartConfiguration


@dataclass
class BarChartFieldWells(BaseModel):
    BarChartAggregatedFieldWells: Optional["_BarChartAggregatedFieldWells"]

    @classmethod
    def _deserialize(
        cls: Type["_BarChartFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BarChartFieldWells"]:
        if not json_data:
            return None
        return cls(
            BarChartAggregatedFieldWells=BarChartAggregatedFieldWells._deserialize(json_data.get("BarChartAggregatedFieldWells")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BarChartFieldWells = BarChartFieldWells


@dataclass
class BarChartAggregatedFieldWells(BaseModel):
    Category: Optional[Sequence["_DimensionField"]]
    Values: Optional[Sequence["_MeasureField"]]
    Colors: Optional[Sequence["_DimensionField"]]
    SmallMultiples: Optional[Sequence["_DimensionField"]]

    @classmethod
    def _deserialize(
        cls: Type["_BarChartAggregatedFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BarChartAggregatedFieldWells"]:
        if not json_data:
            return None
        return cls(
            Category=deserialize_list(json_data.get("Category"), DimensionField),
            Values=deserialize_list(json_data.get("Values"), MeasureField),
            Colors=deserialize_list(json_data.get("Colors"), DimensionField),
            SmallMultiples=deserialize_list(json_data.get("SmallMultiples"), DimensionField),
        )


# work around possible type aliasing issues when variable has same name as a model
_BarChartAggregatedFieldWells = BarChartAggregatedFieldWells


@dataclass
class BarChartSortConfiguration(BaseModel):
    CategorySort: Optional[Sequence["_FieldSortOptions"]]
    CategoryItemsLimit: Optional["_ItemsLimitConfiguration"]
    ColorSort: Optional[Sequence["_FieldSortOptions"]]
    ColorItemsLimit: Optional["_ItemsLimitConfiguration"]
    SmallMultiplesSort: Optional[Sequence["_FieldSortOptions"]]
    SmallMultiplesLimitConfiguration: Optional["_ItemsLimitConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_BarChartSortConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BarChartSortConfiguration"]:
        if not json_data:
            return None
        return cls(
            CategorySort=deserialize_list(json_data.get("CategorySort"), FieldSortOptions),
            CategoryItemsLimit=ItemsLimitConfiguration._deserialize(json_data.get("CategoryItemsLimit")),
            ColorSort=deserialize_list(json_data.get("ColorSort"), FieldSortOptions),
            ColorItemsLimit=ItemsLimitConfiguration._deserialize(json_data.get("ColorItemsLimit")),
            SmallMultiplesSort=deserialize_list(json_data.get("SmallMultiplesSort"), FieldSortOptions),
            SmallMultiplesLimitConfiguration=ItemsLimitConfiguration._deserialize(json_data.get("SmallMultiplesLimitConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BarChartSortConfiguration = BarChartSortConfiguration


@dataclass
class ItemsLimitConfiguration(BaseModel):
    ItemsLimit: Optional[float]
    OtherCategories: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ItemsLimitConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ItemsLimitConfiguration"]:
        if not json_data:
            return None
        return cls(
            ItemsLimit=json_data.get("ItemsLimit"),
            OtherCategories=json_data.get("OtherCategories"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ItemsLimitConfiguration = ItemsLimitConfiguration


@dataclass
class VisualPalette(BaseModel):
    ChartColor: Optional[str]
    ColorMap: Optional[Sequence["_DataPathColor"]]

    @classmethod
    def _deserialize(
        cls: Type["_VisualPalette"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VisualPalette"]:
        if not json_data:
            return None
        return cls(
            ChartColor=json_data.get("ChartColor"),
            ColorMap=deserialize_list(json_data.get("ColorMap"), DataPathColor),
        )


# work around possible type aliasing issues when variable has same name as a model
_VisualPalette = VisualPalette


@dataclass
class DataPathColor(BaseModel):
    Element: Optional["_DataPathValue"]
    Color: Optional[str]
    TimeGranularity: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataPathColor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataPathColor"]:
        if not json_data:
            return None
        return cls(
            Element=DataPathValue._deserialize(json_data.get("Element")),
            Color=json_data.get("Color"),
            TimeGranularity=json_data.get("TimeGranularity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataPathColor = DataPathColor


@dataclass
class SmallMultiplesOptions(BaseModel):
    MaxVisibleRows: Optional[float]
    MaxVisibleColumns: Optional[float]
    PanelConfiguration: Optional["_PanelConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_SmallMultiplesOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmallMultiplesOptions"]:
        if not json_data:
            return None
        return cls(
            MaxVisibleRows=json_data.get("MaxVisibleRows"),
            MaxVisibleColumns=json_data.get("MaxVisibleColumns"),
            PanelConfiguration=PanelConfiguration._deserialize(json_data.get("PanelConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmallMultiplesOptions = SmallMultiplesOptions


@dataclass
class PanelConfiguration(BaseModel):
    Title: Optional["_PanelTitleOptions"]
    BorderVisibility: Optional[str]
    BorderThickness: Optional[str]
    BorderStyle: Optional[str]
    BorderColor: Optional[str]
    GutterVisibility: Optional[str]
    GutterSpacing: Optional[str]
    BackgroundVisibility: Optional[str]
    BackgroundColor: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PanelConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PanelConfiguration"]:
        if not json_data:
            return None
        return cls(
            Title=PanelTitleOptions._deserialize(json_data.get("Title")),
            BorderVisibility=json_data.get("BorderVisibility"),
            BorderThickness=json_data.get("BorderThickness"),
            BorderStyle=json_data.get("BorderStyle"),
            BorderColor=json_data.get("BorderColor"),
            GutterVisibility=json_data.get("GutterVisibility"),
            GutterSpacing=json_data.get("GutterSpacing"),
            BackgroundVisibility=json_data.get("BackgroundVisibility"),
            BackgroundColor=json_data.get("BackgroundColor"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PanelConfiguration = PanelConfiguration


@dataclass
class PanelTitleOptions(BaseModel):
    Visibility: Optional[str]
    FontConfiguration: Optional["_FontConfiguration"]
    HorizontalTextAlignment: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PanelTitleOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PanelTitleOptions"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
            FontConfiguration=FontConfiguration._deserialize(json_data.get("FontConfiguration")),
            HorizontalTextAlignment=json_data.get("HorizontalTextAlignment"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PanelTitleOptions = PanelTitleOptions


@dataclass
class AxisDisplayOptions(BaseModel):
    TickLabelOptions: Optional["_AxisTickLabelOptions"]
    AxisLineVisibility: Optional[str]
    GridLineVisibility: Optional[str]
    DataOptions: Optional["_AxisDataOptions"]
    ScrollbarOptions: Optional["_ScrollBarOptions"]
    AxisOffset: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AxisDisplayOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AxisDisplayOptions"]:
        if not json_data:
            return None
        return cls(
            TickLabelOptions=AxisTickLabelOptions._deserialize(json_data.get("TickLabelOptions")),
            AxisLineVisibility=json_data.get("AxisLineVisibility"),
            GridLineVisibility=json_data.get("GridLineVisibility"),
            DataOptions=AxisDataOptions._deserialize(json_data.get("DataOptions")),
            ScrollbarOptions=ScrollBarOptions._deserialize(json_data.get("ScrollbarOptions")),
            AxisOffset=json_data.get("AxisOffset"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AxisDisplayOptions = AxisDisplayOptions


@dataclass
class AxisTickLabelOptions(BaseModel):
    LabelOptions: Optional["_LabelOptions"]
    RotationAngle: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AxisTickLabelOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AxisTickLabelOptions"]:
        if not json_data:
            return None
        return cls(
            LabelOptions=LabelOptions._deserialize(json_data.get("LabelOptions")),
            RotationAngle=json_data.get("RotationAngle"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AxisTickLabelOptions = AxisTickLabelOptions


@dataclass
class AxisDataOptions(BaseModel):
    NumericAxisOptions: Optional["_NumericAxisOptions"]
    DateAxisOptions: Optional["_DateAxisOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_AxisDataOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AxisDataOptions"]:
        if not json_data:
            return None
        return cls(
            NumericAxisOptions=NumericAxisOptions._deserialize(json_data.get("NumericAxisOptions")),
            DateAxisOptions=DateAxisOptions._deserialize(json_data.get("DateAxisOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AxisDataOptions = AxisDataOptions


@dataclass
class NumericAxisOptions(BaseModel):
    Scale: Optional["_AxisScale"]
    Range: Optional["_AxisDisplayRange"]

    @classmethod
    def _deserialize(
        cls: Type["_NumericAxisOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumericAxisOptions"]:
        if not json_data:
            return None
        return cls(
            Scale=AxisScale._deserialize(json_data.get("Scale")),
            Range=AxisDisplayRange._deserialize(json_data.get("Range")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumericAxisOptions = NumericAxisOptions


@dataclass
class AxisScale(BaseModel):
    Linear: Optional["_AxisLinearScale"]
    Logarithmic: Optional["_AxisLogarithmicScale"]

    @classmethod
    def _deserialize(
        cls: Type["_AxisScale"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AxisScale"]:
        if not json_data:
            return None
        return cls(
            Linear=AxisLinearScale._deserialize(json_data.get("Linear")),
            Logarithmic=AxisLogarithmicScale._deserialize(json_data.get("Logarithmic")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AxisScale = AxisScale


@dataclass
class AxisLinearScale(BaseModel):
    StepCount: Optional[float]
    StepSize: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AxisLinearScale"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AxisLinearScale"]:
        if not json_data:
            return None
        return cls(
            StepCount=json_data.get("StepCount"),
            StepSize=json_data.get("StepSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AxisLinearScale = AxisLinearScale


@dataclass
class AxisLogarithmicScale(BaseModel):
    Base: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AxisLogarithmicScale"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AxisLogarithmicScale"]:
        if not json_data:
            return None
        return cls(
            Base=json_data.get("Base"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AxisLogarithmicScale = AxisLogarithmicScale


@dataclass
class AxisDisplayRange(BaseModel):
    MinMax: Optional["_AxisDisplayMinMaxRange"]
    DataDriven: Optional[MutableMapping[str, Any]]

    @classmethod
    def _deserialize(
        cls: Type["_AxisDisplayRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AxisDisplayRange"]:
        if not json_data:
            return None
        return cls(
            MinMax=AxisDisplayMinMaxRange._deserialize(json_data.get("MinMax")),
            DataDriven=json_data.get("DataDriven"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AxisDisplayRange = AxisDisplayRange


@dataclass
class AxisDisplayMinMaxRange(BaseModel):
    Minimum: Optional[float]
    Maximum: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AxisDisplayMinMaxRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AxisDisplayMinMaxRange"]:
        if not json_data:
            return None
        return cls(
            Minimum=json_data.get("Minimum"),
            Maximum=json_data.get("Maximum"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AxisDisplayMinMaxRange = AxisDisplayMinMaxRange


@dataclass
class DateAxisOptions(BaseModel):
    MissingDateVisibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DateAxisOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DateAxisOptions"]:
        if not json_data:
            return None
        return cls(
            MissingDateVisibility=json_data.get("MissingDateVisibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DateAxisOptions = DateAxisOptions


@dataclass
class ScrollBarOptions(BaseModel):
    Visibility: Optional[str]
    VisibleRange: Optional["_VisibleRangeOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_ScrollBarOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScrollBarOptions"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
            VisibleRange=VisibleRangeOptions._deserialize(json_data.get("VisibleRange")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScrollBarOptions = ScrollBarOptions


@dataclass
class VisibleRangeOptions(BaseModel):
    PercentRange: Optional["_PercentVisibleRange"]

    @classmethod
    def _deserialize(
        cls: Type["_VisibleRangeOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VisibleRangeOptions"]:
        if not json_data:
            return None
        return cls(
            PercentRange=PercentVisibleRange._deserialize(json_data.get("PercentRange")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VisibleRangeOptions = VisibleRangeOptions


@dataclass
class PercentVisibleRange(BaseModel):
    From: Optional[float]
    To: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PercentVisibleRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PercentVisibleRange"]:
        if not json_data:
            return None
        return cls(
            From=json_data.get("From"),
            To=json_data.get("To"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PercentVisibleRange = PercentVisibleRange


@dataclass
class ChartAxisLabelOptions(BaseModel):
    Visibility: Optional[str]
    SortIconVisibility: Optional[str]
    AxisLabelOptions: Optional[Sequence["_AxisLabelOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ChartAxisLabelOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChartAxisLabelOptions"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
            SortIconVisibility=json_data.get("SortIconVisibility"),
            AxisLabelOptions=deserialize_list(json_data.get("AxisLabelOptions"), AxisLabelOptions),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChartAxisLabelOptions = ChartAxisLabelOptions


@dataclass
class AxisLabelOptions(BaseModel):
    FontConfiguration: Optional["_FontConfiguration"]
    CustomLabel: Optional[str]
    ApplyTo: Optional["_AxisLabelReferenceOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_AxisLabelOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AxisLabelOptions"]:
        if not json_data:
            return None
        return cls(
            FontConfiguration=FontConfiguration._deserialize(json_data.get("FontConfiguration")),
            CustomLabel=json_data.get("CustomLabel"),
            ApplyTo=AxisLabelReferenceOptions._deserialize(json_data.get("ApplyTo")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AxisLabelOptions = AxisLabelOptions


@dataclass
class AxisLabelReferenceOptions(BaseModel):
    FieldId: Optional[str]
    Column: Optional["_ColumnIdentifier"]

    @classmethod
    def _deserialize(
        cls: Type["_AxisLabelReferenceOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AxisLabelReferenceOptions"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            Column=ColumnIdentifier._deserialize(json_data.get("Column")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AxisLabelReferenceOptions = AxisLabelReferenceOptions


@dataclass
class LegendOptions(BaseModel):
    Visibility: Optional[str]
    Title: Optional["_LabelOptions"]
    Position: Optional[str]
    Width: Optional[str]
    Height: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LegendOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LegendOptions"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
            Title=LabelOptions._deserialize(json_data.get("Title")),
            Position=json_data.get("Position"),
            Width=json_data.get("Width"),
            Height=json_data.get("Height"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LegendOptions = LegendOptions


@dataclass
class DataLabelOptions(BaseModel):
    Visibility: Optional[str]
    CategoryLabelVisibility: Optional[str]
    MeasureLabelVisibility: Optional[str]
    DataLabelTypes: Optional[Sequence["_DataLabelType"]]
    Position: Optional[str]
    LabelContent: Optional[str]
    LabelFontConfiguration: Optional["_FontConfiguration"]
    LabelColor: Optional[str]
    Overlap: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataLabelOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataLabelOptions"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
            CategoryLabelVisibility=json_data.get("CategoryLabelVisibility"),
            MeasureLabelVisibility=json_data.get("MeasureLabelVisibility"),
            DataLabelTypes=deserialize_list(json_data.get("DataLabelTypes"), DataLabelType),
            Position=json_data.get("Position"),
            LabelContent=json_data.get("LabelContent"),
            LabelFontConfiguration=FontConfiguration._deserialize(json_data.get("LabelFontConfiguration")),
            LabelColor=json_data.get("LabelColor"),
            Overlap=json_data.get("Overlap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataLabelOptions = DataLabelOptions


@dataclass
class DataLabelType(BaseModel):
    FieldLabelType: Optional["_FieldLabelType"]
    DataPathLabelType: Optional["_DataPathLabelType"]
    RangeEndsLabelType: Optional["_RangeEndsLabelType"]
    MinimumLabelType: Optional["_MinimumLabelType"]
    MaximumLabelType: Optional["_MaximumLabelType"]

    @classmethod
    def _deserialize(
        cls: Type["_DataLabelType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataLabelType"]:
        if not json_data:
            return None
        return cls(
            FieldLabelType=FieldLabelType._deserialize(json_data.get("FieldLabelType")),
            DataPathLabelType=DataPathLabelType._deserialize(json_data.get("DataPathLabelType")),
            RangeEndsLabelType=RangeEndsLabelType._deserialize(json_data.get("RangeEndsLabelType")),
            MinimumLabelType=MinimumLabelType._deserialize(json_data.get("MinimumLabelType")),
            MaximumLabelType=MaximumLabelType._deserialize(json_data.get("MaximumLabelType")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataLabelType = DataLabelType


@dataclass
class FieldLabelType(BaseModel):
    FieldId: Optional[str]
    Visibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FieldLabelType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldLabelType"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            Visibility=json_data.get("Visibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldLabelType = FieldLabelType


@dataclass
class DataPathLabelType(BaseModel):
    FieldId: Optional[str]
    FieldValue: Optional[str]
    Visibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataPathLabelType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataPathLabelType"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            FieldValue=json_data.get("FieldValue"),
            Visibility=json_data.get("Visibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataPathLabelType = DataPathLabelType


@dataclass
class RangeEndsLabelType(BaseModel):
    Visibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RangeEndsLabelType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangeEndsLabelType"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangeEndsLabelType = RangeEndsLabelType


@dataclass
class MinimumLabelType(BaseModel):
    Visibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MinimumLabelType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MinimumLabelType"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MinimumLabelType = MinimumLabelType


@dataclass
class MaximumLabelType(BaseModel):
    Visibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaximumLabelType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaximumLabelType"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaximumLabelType = MaximumLabelType


@dataclass
class TooltipOptions(BaseModel):
    TooltipVisibility: Optional[str]
    SelectedTooltipType: Optional[str]
    FieldBasedTooltip: Optional["_FieldBasedTooltip"]

    @classmethod
    def _deserialize(
        cls: Type["_TooltipOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TooltipOptions"]:
        if not json_data:
            return None
        return cls(
            TooltipVisibility=json_data.get("TooltipVisibility"),
            SelectedTooltipType=json_data.get("SelectedTooltipType"),
            FieldBasedTooltip=FieldBasedTooltip._deserialize(json_data.get("FieldBasedTooltip")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TooltipOptions = TooltipOptions


@dataclass
class FieldBasedTooltip(BaseModel):
    AggregationVisibility: Optional[str]
    TooltipTitleType: Optional[str]
    TooltipFields: Optional[Sequence["_TooltipItem"]]

    @classmethod
    def _deserialize(
        cls: Type["_FieldBasedTooltip"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldBasedTooltip"]:
        if not json_data:
            return None
        return cls(
            AggregationVisibility=json_data.get("AggregationVisibility"),
            TooltipTitleType=json_data.get("TooltipTitleType"),
            TooltipFields=deserialize_list(json_data.get("TooltipFields"), TooltipItem),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldBasedTooltip = FieldBasedTooltip


@dataclass
class TooltipItem(BaseModel):
    FieldTooltipItem: Optional["_FieldTooltipItem"]
    ColumnTooltipItem: Optional["_ColumnTooltipItem"]

    @classmethod
    def _deserialize(
        cls: Type["_TooltipItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TooltipItem"]:
        if not json_data:
            return None
        return cls(
            FieldTooltipItem=FieldTooltipItem._deserialize(json_data.get("FieldTooltipItem")),
            ColumnTooltipItem=ColumnTooltipItem._deserialize(json_data.get("ColumnTooltipItem")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TooltipItem = TooltipItem


@dataclass
class FieldTooltipItem(BaseModel):
    FieldId: Optional[str]
    Label: Optional[str]
    Visibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FieldTooltipItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldTooltipItem"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            Label=json_data.get("Label"),
            Visibility=json_data.get("Visibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldTooltipItem = FieldTooltipItem


@dataclass
class ColumnTooltipItem(BaseModel):
    Column: Optional["_ColumnIdentifier"]
    Label: Optional[str]
    Visibility: Optional[str]
    Aggregation: Optional["_AggregationFunction"]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnTooltipItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnTooltipItem"]:
        if not json_data:
            return None
        return cls(
            Column=ColumnIdentifier._deserialize(json_data.get("Column")),
            Label=json_data.get("Label"),
            Visibility=json_data.get("Visibility"),
            Aggregation=AggregationFunction._deserialize(json_data.get("Aggregation")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnTooltipItem = ColumnTooltipItem


@dataclass
class ReferenceLine(BaseModel):
    Status: Optional[str]
    DataConfiguration: Optional["_ReferenceLineDataConfiguration"]
    StyleConfiguration: Optional["_ReferenceLineStyleConfiguration"]
    LabelConfiguration: Optional["_ReferenceLineLabelConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ReferenceLine"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReferenceLine"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
            DataConfiguration=ReferenceLineDataConfiguration._deserialize(json_data.get("DataConfiguration")),
            StyleConfiguration=ReferenceLineStyleConfiguration._deserialize(json_data.get("StyleConfiguration")),
            LabelConfiguration=ReferenceLineLabelConfiguration._deserialize(json_data.get("LabelConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReferenceLine = ReferenceLine


@dataclass
class ReferenceLineDataConfiguration(BaseModel):
    StaticConfiguration: Optional["_ReferenceLineStaticDataConfiguration"]
    DynamicConfiguration: Optional["_ReferenceLineDynamicDataConfiguration"]
    AxisBinding: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReferenceLineDataConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReferenceLineDataConfiguration"]:
        if not json_data:
            return None
        return cls(
            StaticConfiguration=ReferenceLineStaticDataConfiguration._deserialize(json_data.get("StaticConfiguration")),
            DynamicConfiguration=ReferenceLineDynamicDataConfiguration._deserialize(json_data.get("DynamicConfiguration")),
            AxisBinding=json_data.get("AxisBinding"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReferenceLineDataConfiguration = ReferenceLineDataConfiguration


@dataclass
class ReferenceLineStaticDataConfiguration(BaseModel):
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ReferenceLineStaticDataConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReferenceLineStaticDataConfiguration"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReferenceLineStaticDataConfiguration = ReferenceLineStaticDataConfiguration


@dataclass
class ReferenceLineDynamicDataConfiguration(BaseModel):
    Column: Optional["_ColumnIdentifier"]
    MeasureAggregationFunction: Optional["_AggregationFunction"]
    Calculation: Optional["_NumericalAggregationFunction"]

    @classmethod
    def _deserialize(
        cls: Type["_ReferenceLineDynamicDataConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReferenceLineDynamicDataConfiguration"]:
        if not json_data:
            return None
        return cls(
            Column=ColumnIdentifier._deserialize(json_data.get("Column")),
            MeasureAggregationFunction=AggregationFunction._deserialize(json_data.get("MeasureAggregationFunction")),
            Calculation=NumericalAggregationFunction._deserialize(json_data.get("Calculation")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReferenceLineDynamicDataConfiguration = ReferenceLineDynamicDataConfiguration


@dataclass
class ReferenceLineStyleConfiguration(BaseModel):
    Pattern: Optional[str]
    Color: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReferenceLineStyleConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReferenceLineStyleConfiguration"]:
        if not json_data:
            return None
        return cls(
            Pattern=json_data.get("Pattern"),
            Color=json_data.get("Color"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReferenceLineStyleConfiguration = ReferenceLineStyleConfiguration


@dataclass
class ReferenceLineLabelConfiguration(BaseModel):
    ValueLabelConfiguration: Optional["_ReferenceLineValueLabelConfiguration"]
    CustomLabelConfiguration: Optional["_ReferenceLineCustomLabelConfiguration"]
    FontConfiguration: Optional["_FontConfiguration"]
    FontColor: Optional[str]
    HorizontalPosition: Optional[str]
    VerticalPosition: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReferenceLineLabelConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReferenceLineLabelConfiguration"]:
        if not json_data:
            return None
        return cls(
            ValueLabelConfiguration=ReferenceLineValueLabelConfiguration._deserialize(json_data.get("ValueLabelConfiguration")),
            CustomLabelConfiguration=ReferenceLineCustomLabelConfiguration._deserialize(json_data.get("CustomLabelConfiguration")),
            FontConfiguration=FontConfiguration._deserialize(json_data.get("FontConfiguration")),
            FontColor=json_data.get("FontColor"),
            HorizontalPosition=json_data.get("HorizontalPosition"),
            VerticalPosition=json_data.get("VerticalPosition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReferenceLineLabelConfiguration = ReferenceLineLabelConfiguration


@dataclass
class ReferenceLineValueLabelConfiguration(BaseModel):
    RelativePosition: Optional[str]
    FormatConfiguration: Optional["_NumericFormatConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ReferenceLineValueLabelConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReferenceLineValueLabelConfiguration"]:
        if not json_data:
            return None
        return cls(
            RelativePosition=json_data.get("RelativePosition"),
            FormatConfiguration=NumericFormatConfiguration._deserialize(json_data.get("FormatConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReferenceLineValueLabelConfiguration = ReferenceLineValueLabelConfiguration


@dataclass
class ReferenceLineCustomLabelConfiguration(BaseModel):
    CustomLabel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReferenceLineCustomLabelConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReferenceLineCustomLabelConfiguration"]:
        if not json_data:
            return None
        return cls(
            CustomLabel=json_data.get("CustomLabel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReferenceLineCustomLabelConfiguration = ReferenceLineCustomLabelConfiguration


@dataclass
class ContributionAnalysisDefault(BaseModel):
    MeasureFieldId: Optional[str]
    ContributorDimensions: Optional[Sequence["_ColumnIdentifier"]]

    @classmethod
    def _deserialize(
        cls: Type["_ContributionAnalysisDefault"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContributionAnalysisDefault"]:
        if not json_data:
            return None
        return cls(
            MeasureFieldId=json_data.get("MeasureFieldId"),
            ContributorDimensions=deserialize_list(json_data.get("ContributorDimensions"), ColumnIdentifier),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContributionAnalysisDefault = ContributionAnalysisDefault


@dataclass
class ColumnHierarchy(BaseModel):
    ExplicitHierarchy: Optional["_ExplicitHierarchy"]
    DateTimeHierarchy: Optional["_DateTimeHierarchy"]
    PredefinedHierarchy: Optional["_PredefinedHierarchy"]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnHierarchy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnHierarchy"]:
        if not json_data:
            return None
        return cls(
            ExplicitHierarchy=ExplicitHierarchy._deserialize(json_data.get("ExplicitHierarchy")),
            DateTimeHierarchy=DateTimeHierarchy._deserialize(json_data.get("DateTimeHierarchy")),
            PredefinedHierarchy=PredefinedHierarchy._deserialize(json_data.get("PredefinedHierarchy")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnHierarchy = ColumnHierarchy


@dataclass
class ExplicitHierarchy(BaseModel):
    HierarchyId: Optional[str]
    Columns: Optional[Sequence["_ColumnIdentifier"]]
    DrillDownFilters: Optional[Sequence["_DrillDownFilter"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExplicitHierarchy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExplicitHierarchy"]:
        if not json_data:
            return None
        return cls(
            HierarchyId=json_data.get("HierarchyId"),
            Columns=deserialize_list(json_data.get("Columns"), ColumnIdentifier),
            DrillDownFilters=deserialize_list(json_data.get("DrillDownFilters"), DrillDownFilter),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExplicitHierarchy = ExplicitHierarchy


@dataclass
class DrillDownFilter(BaseModel):
    NumericEqualityFilter: Optional["_NumericEqualityDrillDownFilter"]
    CategoryFilter: Optional["_CategoryDrillDownFilter"]
    TimeRangeFilter: Optional["_TimeRangeDrillDownFilter"]

    @classmethod
    def _deserialize(
        cls: Type["_DrillDownFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DrillDownFilter"]:
        if not json_data:
            return None
        return cls(
            NumericEqualityFilter=NumericEqualityDrillDownFilter._deserialize(json_data.get("NumericEqualityFilter")),
            CategoryFilter=CategoryDrillDownFilter._deserialize(json_data.get("CategoryFilter")),
            TimeRangeFilter=TimeRangeDrillDownFilter._deserialize(json_data.get("TimeRangeFilter")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DrillDownFilter = DrillDownFilter


@dataclass
class NumericEqualityDrillDownFilter(BaseModel):
    Column: Optional["_ColumnIdentifier"]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NumericEqualityDrillDownFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumericEqualityDrillDownFilter"]:
        if not json_data:
            return None
        return cls(
            Column=ColumnIdentifier._deserialize(json_data.get("Column")),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumericEqualityDrillDownFilter = NumericEqualityDrillDownFilter


@dataclass
class CategoryDrillDownFilter(BaseModel):
    Column: Optional["_ColumnIdentifier"]
    CategoryValues: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CategoryDrillDownFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CategoryDrillDownFilter"]:
        if not json_data:
            return None
        return cls(
            Column=ColumnIdentifier._deserialize(json_data.get("Column")),
            CategoryValues=json_data.get("CategoryValues"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CategoryDrillDownFilter = CategoryDrillDownFilter


@dataclass
class TimeRangeDrillDownFilter(BaseModel):
    Column: Optional["_ColumnIdentifier"]
    RangeMinimum: Optional[str]
    RangeMaximum: Optional[str]
    TimeGranularity: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeRangeDrillDownFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeRangeDrillDownFilter"]:
        if not json_data:
            return None
        return cls(
            Column=ColumnIdentifier._deserialize(json_data.get("Column")),
            RangeMinimum=json_data.get("RangeMinimum"),
            RangeMaximum=json_data.get("RangeMaximum"),
            TimeGranularity=json_data.get("TimeGranularity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeRangeDrillDownFilter = TimeRangeDrillDownFilter


@dataclass
class DateTimeHierarchy(BaseModel):
    HierarchyId: Optional[str]
    DrillDownFilters: Optional[Sequence["_DrillDownFilter"]]

    @classmethod
    def _deserialize(
        cls: Type["_DateTimeHierarchy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DateTimeHierarchy"]:
        if not json_data:
            return None
        return cls(
            HierarchyId=json_data.get("HierarchyId"),
            DrillDownFilters=deserialize_list(json_data.get("DrillDownFilters"), DrillDownFilter),
        )


# work around possible type aliasing issues when variable has same name as a model
_DateTimeHierarchy = DateTimeHierarchy


@dataclass
class PredefinedHierarchy(BaseModel):
    HierarchyId: Optional[str]
    Columns: Optional[Sequence["_ColumnIdentifier"]]
    DrillDownFilters: Optional[Sequence["_DrillDownFilter"]]

    @classmethod
    def _deserialize(
        cls: Type["_PredefinedHierarchy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PredefinedHierarchy"]:
        if not json_data:
            return None
        return cls(
            HierarchyId=json_data.get("HierarchyId"),
            Columns=deserialize_list(json_data.get("Columns"), ColumnIdentifier),
            DrillDownFilters=deserialize_list(json_data.get("DrillDownFilters"), DrillDownFilter),
        )


# work around possible type aliasing issues when variable has same name as a model
_PredefinedHierarchy = PredefinedHierarchy


@dataclass
class KPIVisual(BaseModel):
    VisualId: Optional[str]
    Title: Optional["_VisualTitleLabelOptions"]
    Subtitle: Optional["_VisualSubtitleLabelOptions"]
    ChartConfiguration: Optional["_KPIConfiguration"]
    ConditionalFormatting: Optional["_KPIConditionalFormatting"]
    Actions: Optional[Sequence["_VisualCustomAction"]]
    ColumnHierarchies: Optional[Sequence["_ColumnHierarchy"]]

    @classmethod
    def _deserialize(
        cls: Type["_KPIVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KPIVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            Title=VisualTitleLabelOptions._deserialize(json_data.get("Title")),
            Subtitle=VisualSubtitleLabelOptions._deserialize(json_data.get("Subtitle")),
            ChartConfiguration=KPIConfiguration._deserialize(json_data.get("ChartConfiguration")),
            ConditionalFormatting=KPIConditionalFormatting._deserialize(json_data.get("ConditionalFormatting")),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
            ColumnHierarchies=deserialize_list(json_data.get("ColumnHierarchies"), ColumnHierarchy),
        )


# work around possible type aliasing issues when variable has same name as a model
_KPIVisual = KPIVisual


@dataclass
class KPIConfiguration(BaseModel):
    FieldWells: Optional["_KPIFieldWells"]
    SortConfiguration: Optional["_KPISortConfiguration"]
    KPIOptions: Optional["_KPIOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_KPIConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KPIConfiguration"]:
        if not json_data:
            return None
        return cls(
            FieldWells=KPIFieldWells._deserialize(json_data.get("FieldWells")),
            SortConfiguration=KPISortConfiguration._deserialize(json_data.get("SortConfiguration")),
            KPIOptions=KPIOptions._deserialize(json_data.get("KPIOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_KPIConfiguration = KPIConfiguration


@dataclass
class KPIFieldWells(BaseModel):
    Values: Optional[Sequence["_MeasureField"]]
    TargetValues: Optional[Sequence["_MeasureField"]]
    TrendGroups: Optional[Sequence["_DimensionField"]]

    @classmethod
    def _deserialize(
        cls: Type["_KPIFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KPIFieldWells"]:
        if not json_data:
            return None
        return cls(
            Values=deserialize_list(json_data.get("Values"), MeasureField),
            TargetValues=deserialize_list(json_data.get("TargetValues"), MeasureField),
            TrendGroups=deserialize_list(json_data.get("TrendGroups"), DimensionField),
        )


# work around possible type aliasing issues when variable has same name as a model
_KPIFieldWells = KPIFieldWells


@dataclass
class KPISortConfiguration(BaseModel):
    TrendGroupSort: Optional[Sequence["_FieldSortOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_KPISortConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KPISortConfiguration"]:
        if not json_data:
            return None
        return cls(
            TrendGroupSort=deserialize_list(json_data.get("TrendGroupSort"), FieldSortOptions),
        )


# work around possible type aliasing issues when variable has same name as a model
_KPISortConfiguration = KPISortConfiguration


@dataclass
class KPIOptions(BaseModel):
    ProgressBar: Optional["_ProgressBarOptions"]
    TrendArrows: Optional["_TrendArrowOptions"]
    SecondaryValue: Optional["_SecondaryValueOptions"]
    Comparison: Optional["_ComparisonConfiguration"]
    PrimaryValueDisplayType: Optional[str]
    PrimaryValueFontConfiguration: Optional["_FontConfiguration"]
    SecondaryValueFontConfiguration: Optional["_FontConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_KPIOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KPIOptions"]:
        if not json_data:
            return None
        return cls(
            ProgressBar=ProgressBarOptions._deserialize(json_data.get("ProgressBar")),
            TrendArrows=TrendArrowOptions._deserialize(json_data.get("TrendArrows")),
            SecondaryValue=SecondaryValueOptions._deserialize(json_data.get("SecondaryValue")),
            Comparison=ComparisonConfiguration._deserialize(json_data.get("Comparison")),
            PrimaryValueDisplayType=json_data.get("PrimaryValueDisplayType"),
            PrimaryValueFontConfiguration=FontConfiguration._deserialize(json_data.get("PrimaryValueFontConfiguration")),
            SecondaryValueFontConfiguration=FontConfiguration._deserialize(json_data.get("SecondaryValueFontConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_KPIOptions = KPIOptions


@dataclass
class ProgressBarOptions(BaseModel):
    Visibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProgressBarOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProgressBarOptions"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProgressBarOptions = ProgressBarOptions


@dataclass
class TrendArrowOptions(BaseModel):
    Visibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrendArrowOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrendArrowOptions"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrendArrowOptions = TrendArrowOptions


@dataclass
class SecondaryValueOptions(BaseModel):
    Visibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecondaryValueOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondaryValueOptions"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecondaryValueOptions = SecondaryValueOptions


@dataclass
class ComparisonConfiguration(BaseModel):
    ComparisonMethod: Optional[str]
    ComparisonFormat: Optional["_ComparisonFormatConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ComparisonConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComparisonConfiguration"]:
        if not json_data:
            return None
        return cls(
            ComparisonMethod=json_data.get("ComparisonMethod"),
            ComparisonFormat=ComparisonFormatConfiguration._deserialize(json_data.get("ComparisonFormat")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComparisonConfiguration = ComparisonConfiguration


@dataclass
class ComparisonFormatConfiguration(BaseModel):
    NumberDisplayFormatConfiguration: Optional["_NumberDisplayFormatConfiguration"]
    PercentageDisplayFormatConfiguration: Optional["_PercentageDisplayFormatConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ComparisonFormatConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComparisonFormatConfiguration"]:
        if not json_data:
            return None
        return cls(
            NumberDisplayFormatConfiguration=NumberDisplayFormatConfiguration._deserialize(json_data.get("NumberDisplayFormatConfiguration")),
            PercentageDisplayFormatConfiguration=PercentageDisplayFormatConfiguration._deserialize(json_data.get("PercentageDisplayFormatConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComparisonFormatConfiguration = ComparisonFormatConfiguration


@dataclass
class KPIConditionalFormatting(BaseModel):
    ConditionalFormattingOptions: Optional[Sequence["_KPIConditionalFormattingOption"]]

    @classmethod
    def _deserialize(
        cls: Type["_KPIConditionalFormatting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KPIConditionalFormatting"]:
        if not json_data:
            return None
        return cls(
            ConditionalFormattingOptions=deserialize_list(json_data.get("ConditionalFormattingOptions"), KPIConditionalFormattingOption),
        )


# work around possible type aliasing issues when variable has same name as a model
_KPIConditionalFormatting = KPIConditionalFormatting


@dataclass
class KPIConditionalFormattingOption(BaseModel):
    PrimaryValue: Optional["_KPIPrimaryValueConditionalFormatting"]
    ProgressBar: Optional["_KPIProgressBarConditionalFormatting"]

    @classmethod
    def _deserialize(
        cls: Type["_KPIConditionalFormattingOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KPIConditionalFormattingOption"]:
        if not json_data:
            return None
        return cls(
            PrimaryValue=KPIPrimaryValueConditionalFormatting._deserialize(json_data.get("PrimaryValue")),
            ProgressBar=KPIProgressBarConditionalFormatting._deserialize(json_data.get("ProgressBar")),
        )


# work around possible type aliasing issues when variable has same name as a model
_KPIConditionalFormattingOption = KPIConditionalFormattingOption


@dataclass
class KPIPrimaryValueConditionalFormatting(BaseModel):
    TextColor: Optional["_ConditionalFormattingColor"]
    Icon: Optional["_ConditionalFormattingIcon"]

    @classmethod
    def _deserialize(
        cls: Type["_KPIPrimaryValueConditionalFormatting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KPIPrimaryValueConditionalFormatting"]:
        if not json_data:
            return None
        return cls(
            TextColor=ConditionalFormattingColor._deserialize(json_data.get("TextColor")),
            Icon=ConditionalFormattingIcon._deserialize(json_data.get("Icon")),
        )


# work around possible type aliasing issues when variable has same name as a model
_KPIPrimaryValueConditionalFormatting = KPIPrimaryValueConditionalFormatting


@dataclass
class KPIProgressBarConditionalFormatting(BaseModel):
    ForegroundColor: Optional["_ConditionalFormattingColor"]

    @classmethod
    def _deserialize(
        cls: Type["_KPIProgressBarConditionalFormatting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KPIProgressBarConditionalFormatting"]:
        if not json_data:
            return None
        return cls(
            ForegroundColor=ConditionalFormattingColor._deserialize(json_data.get("ForegroundColor")),
        )


# work around possible type aliasing issues when variable has same name as a model
_KPIProgressBarConditionalFormatting = KPIProgressBarConditionalFormatting


@dataclass
class PieChartVisual(BaseModel):
    VisualId: Optional[str]
    Title: Optional["_VisualTitleLabelOptions"]
    Subtitle: Optional["_VisualSubtitleLabelOptions"]
    ChartConfiguration: Optional["_PieChartConfiguration"]
    Actions: Optional[Sequence["_VisualCustomAction"]]
    ColumnHierarchies: Optional[Sequence["_ColumnHierarchy"]]

    @classmethod
    def _deserialize(
        cls: Type["_PieChartVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PieChartVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            Title=VisualTitleLabelOptions._deserialize(json_data.get("Title")),
            Subtitle=VisualSubtitleLabelOptions._deserialize(json_data.get("Subtitle")),
            ChartConfiguration=PieChartConfiguration._deserialize(json_data.get("ChartConfiguration")),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
            ColumnHierarchies=deserialize_list(json_data.get("ColumnHierarchies"), ColumnHierarchy),
        )


# work around possible type aliasing issues when variable has same name as a model
_PieChartVisual = PieChartVisual


@dataclass
class PieChartConfiguration(BaseModel):
    FieldWells: Optional["_PieChartFieldWells"]
    SortConfiguration: Optional["_PieChartSortConfiguration"]
    DonutOptions: Optional["_DonutOptions"]
    SmallMultiplesOptions: Optional["_SmallMultiplesOptions"]
    CategoryLabelOptions: Optional["_ChartAxisLabelOptions"]
    ValueLabelOptions: Optional["_ChartAxisLabelOptions"]
    Legend: Optional["_LegendOptions"]
    DataLabels: Optional["_DataLabelOptions"]
    Tooltip: Optional["_TooltipOptions"]
    VisualPalette: Optional["_VisualPalette"]
    ContributionAnalysisDefaults: Optional[Sequence["_ContributionAnalysisDefault"]]

    @classmethod
    def _deserialize(
        cls: Type["_PieChartConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PieChartConfiguration"]:
        if not json_data:
            return None
        return cls(
            FieldWells=PieChartFieldWells._deserialize(json_data.get("FieldWells")),
            SortConfiguration=PieChartSortConfiguration._deserialize(json_data.get("SortConfiguration")),
            DonutOptions=DonutOptions._deserialize(json_data.get("DonutOptions")),
            SmallMultiplesOptions=SmallMultiplesOptions._deserialize(json_data.get("SmallMultiplesOptions")),
            CategoryLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("CategoryLabelOptions")),
            ValueLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("ValueLabelOptions")),
            Legend=LegendOptions._deserialize(json_data.get("Legend")),
            DataLabels=DataLabelOptions._deserialize(json_data.get("DataLabels")),
            Tooltip=TooltipOptions._deserialize(json_data.get("Tooltip")),
            VisualPalette=VisualPalette._deserialize(json_data.get("VisualPalette")),
            ContributionAnalysisDefaults=deserialize_list(json_data.get("ContributionAnalysisDefaults"), ContributionAnalysisDefault),
        )


# work around possible type aliasing issues when variable has same name as a model
_PieChartConfiguration = PieChartConfiguration


@dataclass
class PieChartFieldWells(BaseModel):
    PieChartAggregatedFieldWells: Optional["_PieChartAggregatedFieldWells"]

    @classmethod
    def _deserialize(
        cls: Type["_PieChartFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PieChartFieldWells"]:
        if not json_data:
            return None
        return cls(
            PieChartAggregatedFieldWells=PieChartAggregatedFieldWells._deserialize(json_data.get("PieChartAggregatedFieldWells")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PieChartFieldWells = PieChartFieldWells


@dataclass
class PieChartAggregatedFieldWells(BaseModel):
    Category: Optional[Sequence["_DimensionField"]]
    Values: Optional[Sequence["_MeasureField"]]
    SmallMultiples: Optional[Sequence["_DimensionField"]]

    @classmethod
    def _deserialize(
        cls: Type["_PieChartAggregatedFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PieChartAggregatedFieldWells"]:
        if not json_data:
            return None
        return cls(
            Category=deserialize_list(json_data.get("Category"), DimensionField),
            Values=deserialize_list(json_data.get("Values"), MeasureField),
            SmallMultiples=deserialize_list(json_data.get("SmallMultiples"), DimensionField),
        )


# work around possible type aliasing issues when variable has same name as a model
_PieChartAggregatedFieldWells = PieChartAggregatedFieldWells


@dataclass
class PieChartSortConfiguration(BaseModel):
    CategorySort: Optional[Sequence["_FieldSortOptions"]]
    CategoryItemsLimit: Optional["_ItemsLimitConfiguration"]
    SmallMultiplesSort: Optional[Sequence["_FieldSortOptions"]]
    SmallMultiplesLimitConfiguration: Optional["_ItemsLimitConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_PieChartSortConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PieChartSortConfiguration"]:
        if not json_data:
            return None
        return cls(
            CategorySort=deserialize_list(json_data.get("CategorySort"), FieldSortOptions),
            CategoryItemsLimit=ItemsLimitConfiguration._deserialize(json_data.get("CategoryItemsLimit")),
            SmallMultiplesSort=deserialize_list(json_data.get("SmallMultiplesSort"), FieldSortOptions),
            SmallMultiplesLimitConfiguration=ItemsLimitConfiguration._deserialize(json_data.get("SmallMultiplesLimitConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PieChartSortConfiguration = PieChartSortConfiguration


@dataclass
class DonutOptions(BaseModel):
    ArcOptions: Optional["_ArcOptions"]
    DonutCenterOptions: Optional["_DonutCenterOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_DonutOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DonutOptions"]:
        if not json_data:
            return None
        return cls(
            ArcOptions=ArcOptions._deserialize(json_data.get("ArcOptions")),
            DonutCenterOptions=DonutCenterOptions._deserialize(json_data.get("DonutCenterOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DonutOptions = DonutOptions


@dataclass
class ArcOptions(BaseModel):
    ArcThickness: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ArcOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArcOptions"]:
        if not json_data:
            return None
        return cls(
            ArcThickness=json_data.get("ArcThickness"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArcOptions = ArcOptions


@dataclass
class DonutCenterOptions(BaseModel):
    LabelVisibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DonutCenterOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DonutCenterOptions"]:
        if not json_data:
            return None
        return cls(
            LabelVisibility=json_data.get("LabelVisibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DonutCenterOptions = DonutCenterOptions


@dataclass
class GaugeChartVisual(BaseModel):
    VisualId: Optional[str]
    Title: Optional["_VisualTitleLabelOptions"]
    Subtitle: Optional["_VisualSubtitleLabelOptions"]
    ChartConfiguration: Optional["_GaugeChartConfiguration"]
    ConditionalFormatting: Optional["_GaugeChartConditionalFormatting"]
    Actions: Optional[Sequence["_VisualCustomAction"]]

    @classmethod
    def _deserialize(
        cls: Type["_GaugeChartVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GaugeChartVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            Title=VisualTitleLabelOptions._deserialize(json_data.get("Title")),
            Subtitle=VisualSubtitleLabelOptions._deserialize(json_data.get("Subtitle")),
            ChartConfiguration=GaugeChartConfiguration._deserialize(json_data.get("ChartConfiguration")),
            ConditionalFormatting=GaugeChartConditionalFormatting._deserialize(json_data.get("ConditionalFormatting")),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
        )


# work around possible type aliasing issues when variable has same name as a model
_GaugeChartVisual = GaugeChartVisual


@dataclass
class GaugeChartConfiguration(BaseModel):
    FieldWells: Optional["_GaugeChartFieldWells"]
    GaugeChartOptions: Optional["_GaugeChartOptions"]
    DataLabels: Optional["_DataLabelOptions"]
    TooltipOptions: Optional["_TooltipOptions"]
    VisualPalette: Optional["_VisualPalette"]

    @classmethod
    def _deserialize(
        cls: Type["_GaugeChartConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GaugeChartConfiguration"]:
        if not json_data:
            return None
        return cls(
            FieldWells=GaugeChartFieldWells._deserialize(json_data.get("FieldWells")),
            GaugeChartOptions=GaugeChartOptions._deserialize(json_data.get("GaugeChartOptions")),
            DataLabels=DataLabelOptions._deserialize(json_data.get("DataLabels")),
            TooltipOptions=TooltipOptions._deserialize(json_data.get("TooltipOptions")),
            VisualPalette=VisualPalette._deserialize(json_data.get("VisualPalette")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GaugeChartConfiguration = GaugeChartConfiguration


@dataclass
class GaugeChartFieldWells(BaseModel):
    Values: Optional[Sequence["_MeasureField"]]
    TargetValues: Optional[Sequence["_MeasureField"]]

    @classmethod
    def _deserialize(
        cls: Type["_GaugeChartFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GaugeChartFieldWells"]:
        if not json_data:
            return None
        return cls(
            Values=deserialize_list(json_data.get("Values"), MeasureField),
            TargetValues=deserialize_list(json_data.get("TargetValues"), MeasureField),
        )


# work around possible type aliasing issues when variable has same name as a model
_GaugeChartFieldWells = GaugeChartFieldWells


@dataclass
class GaugeChartOptions(BaseModel):
    PrimaryValueDisplayType: Optional[str]
    Comparison: Optional["_ComparisonConfiguration"]
    ArcAxis: Optional["_ArcAxisConfiguration"]
    Arc: Optional["_ArcConfiguration"]
    PrimaryValueFontConfiguration: Optional["_FontConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_GaugeChartOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GaugeChartOptions"]:
        if not json_data:
            return None
        return cls(
            PrimaryValueDisplayType=json_data.get("PrimaryValueDisplayType"),
            Comparison=ComparisonConfiguration._deserialize(json_data.get("Comparison")),
            ArcAxis=ArcAxisConfiguration._deserialize(json_data.get("ArcAxis")),
            Arc=ArcConfiguration._deserialize(json_data.get("Arc")),
            PrimaryValueFontConfiguration=FontConfiguration._deserialize(json_data.get("PrimaryValueFontConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GaugeChartOptions = GaugeChartOptions


@dataclass
class ArcAxisConfiguration(BaseModel):
    Range: Optional["_ArcAxisDisplayRange"]
    ReserveRange: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ArcAxisConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArcAxisConfiguration"]:
        if not json_data:
            return None
        return cls(
            Range=ArcAxisDisplayRange._deserialize(json_data.get("Range")),
            ReserveRange=json_data.get("ReserveRange"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArcAxisConfiguration = ArcAxisConfiguration


@dataclass
class ArcAxisDisplayRange(BaseModel):
    Min: Optional[float]
    Max: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ArcAxisDisplayRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArcAxisDisplayRange"]:
        if not json_data:
            return None
        return cls(
            Min=json_data.get("Min"),
            Max=json_data.get("Max"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArcAxisDisplayRange = ArcAxisDisplayRange


@dataclass
class ArcConfiguration(BaseModel):
    ArcAngle: Optional[float]
    ArcThickness: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ArcConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArcConfiguration"]:
        if not json_data:
            return None
        return cls(
            ArcAngle=json_data.get("ArcAngle"),
            ArcThickness=json_data.get("ArcThickness"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArcConfiguration = ArcConfiguration


@dataclass
class GaugeChartConditionalFormatting(BaseModel):
    ConditionalFormattingOptions: Optional[Sequence["_GaugeChartConditionalFormattingOption"]]

    @classmethod
    def _deserialize(
        cls: Type["_GaugeChartConditionalFormatting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GaugeChartConditionalFormatting"]:
        if not json_data:
            return None
        return cls(
            ConditionalFormattingOptions=deserialize_list(json_data.get("ConditionalFormattingOptions"), GaugeChartConditionalFormattingOption),
        )


# work around possible type aliasing issues when variable has same name as a model
_GaugeChartConditionalFormatting = GaugeChartConditionalFormatting


@dataclass
class GaugeChartConditionalFormattingOption(BaseModel):
    PrimaryValue: Optional["_GaugeChartPrimaryValueConditionalFormatting"]
    Arc: Optional["_GaugeChartArcConditionalFormatting"]

    @classmethod
    def _deserialize(
        cls: Type["_GaugeChartConditionalFormattingOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GaugeChartConditionalFormattingOption"]:
        if not json_data:
            return None
        return cls(
            PrimaryValue=GaugeChartPrimaryValueConditionalFormatting._deserialize(json_data.get("PrimaryValue")),
            Arc=GaugeChartArcConditionalFormatting._deserialize(json_data.get("Arc")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GaugeChartConditionalFormattingOption = GaugeChartConditionalFormattingOption


@dataclass
class GaugeChartPrimaryValueConditionalFormatting(BaseModel):
    TextColor: Optional["_ConditionalFormattingColor"]
    Icon: Optional["_ConditionalFormattingIcon"]

    @classmethod
    def _deserialize(
        cls: Type["_GaugeChartPrimaryValueConditionalFormatting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GaugeChartPrimaryValueConditionalFormatting"]:
        if not json_data:
            return None
        return cls(
            TextColor=ConditionalFormattingColor._deserialize(json_data.get("TextColor")),
            Icon=ConditionalFormattingIcon._deserialize(json_data.get("Icon")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GaugeChartPrimaryValueConditionalFormatting = GaugeChartPrimaryValueConditionalFormatting


@dataclass
class GaugeChartArcConditionalFormatting(BaseModel):
    ForegroundColor: Optional["_ConditionalFormattingColor"]

    @classmethod
    def _deserialize(
        cls: Type["_GaugeChartArcConditionalFormatting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GaugeChartArcConditionalFormatting"]:
        if not json_data:
            return None
        return cls(
            ForegroundColor=ConditionalFormattingColor._deserialize(json_data.get("ForegroundColor")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GaugeChartArcConditionalFormatting = GaugeChartArcConditionalFormatting


@dataclass
class LineChartVisual(BaseModel):
    VisualId: Optional[str]
    Title: Optional["_VisualTitleLabelOptions"]
    Subtitle: Optional["_VisualSubtitleLabelOptions"]
    ChartConfiguration: Optional["_LineChartConfiguration"]
    Actions: Optional[Sequence["_VisualCustomAction"]]
    ColumnHierarchies: Optional[Sequence["_ColumnHierarchy"]]

    @classmethod
    def _deserialize(
        cls: Type["_LineChartVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LineChartVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            Title=VisualTitleLabelOptions._deserialize(json_data.get("Title")),
            Subtitle=VisualSubtitleLabelOptions._deserialize(json_data.get("Subtitle")),
            ChartConfiguration=LineChartConfiguration._deserialize(json_data.get("ChartConfiguration")),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
            ColumnHierarchies=deserialize_list(json_data.get("ColumnHierarchies"), ColumnHierarchy),
        )


# work around possible type aliasing issues when variable has same name as a model
_LineChartVisual = LineChartVisual


@dataclass
class LineChartConfiguration(BaseModel):
    FieldWells: Optional["_LineChartFieldWells"]
    SortConfiguration: Optional["_LineChartSortConfiguration"]
    ForecastConfigurations: Optional[Sequence["_ForecastConfiguration"]]
    Type: Optional[str]
    SmallMultiplesOptions: Optional["_SmallMultiplesOptions"]
    XAxisDisplayOptions: Optional["_AxisDisplayOptions"]
    XAxisLabelOptions: Optional["_ChartAxisLabelOptions"]
    PrimaryYAxisDisplayOptions: Optional["_LineSeriesAxisDisplayOptions"]
    PrimaryYAxisLabelOptions: Optional["_ChartAxisLabelOptions"]
    SecondaryYAxisDisplayOptions: Optional["_LineSeriesAxisDisplayOptions"]
    SecondaryYAxisLabelOptions: Optional["_ChartAxisLabelOptions"]
    DefaultSeriesSettings: Optional["_LineChartDefaultSeriesSettings"]
    Series: Optional[Sequence["_SeriesItem"]]
    Legend: Optional["_LegendOptions"]
    DataLabels: Optional["_DataLabelOptions"]
    ReferenceLines: Optional[Sequence["_ReferenceLine"]]
    Tooltip: Optional["_TooltipOptions"]
    ContributionAnalysisDefaults: Optional[Sequence["_ContributionAnalysisDefault"]]
    VisualPalette: Optional["_VisualPalette"]

    @classmethod
    def _deserialize(
        cls: Type["_LineChartConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LineChartConfiguration"]:
        if not json_data:
            return None
        return cls(
            FieldWells=LineChartFieldWells._deserialize(json_data.get("FieldWells")),
            SortConfiguration=LineChartSortConfiguration._deserialize(json_data.get("SortConfiguration")),
            ForecastConfigurations=deserialize_list(json_data.get("ForecastConfigurations"), ForecastConfiguration),
            Type=json_data.get("Type"),
            SmallMultiplesOptions=SmallMultiplesOptions._deserialize(json_data.get("SmallMultiplesOptions")),
            XAxisDisplayOptions=AxisDisplayOptions._deserialize(json_data.get("XAxisDisplayOptions")),
            XAxisLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("XAxisLabelOptions")),
            PrimaryYAxisDisplayOptions=LineSeriesAxisDisplayOptions._deserialize(json_data.get("PrimaryYAxisDisplayOptions")),
            PrimaryYAxisLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("PrimaryYAxisLabelOptions")),
            SecondaryYAxisDisplayOptions=LineSeriesAxisDisplayOptions._deserialize(json_data.get("SecondaryYAxisDisplayOptions")),
            SecondaryYAxisLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("SecondaryYAxisLabelOptions")),
            DefaultSeriesSettings=LineChartDefaultSeriesSettings._deserialize(json_data.get("DefaultSeriesSettings")),
            Series=deserialize_list(json_data.get("Series"), SeriesItem),
            Legend=LegendOptions._deserialize(json_data.get("Legend")),
            DataLabels=DataLabelOptions._deserialize(json_data.get("DataLabels")),
            ReferenceLines=deserialize_list(json_data.get("ReferenceLines"), ReferenceLine),
            Tooltip=TooltipOptions._deserialize(json_data.get("Tooltip")),
            ContributionAnalysisDefaults=deserialize_list(json_data.get("ContributionAnalysisDefaults"), ContributionAnalysisDefault),
            VisualPalette=VisualPalette._deserialize(json_data.get("VisualPalette")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LineChartConfiguration = LineChartConfiguration


@dataclass
class LineChartFieldWells(BaseModel):
    LineChartAggregatedFieldWells: Optional["_LineChartAggregatedFieldWells"]

    @classmethod
    def _deserialize(
        cls: Type["_LineChartFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LineChartFieldWells"]:
        if not json_data:
            return None
        return cls(
            LineChartAggregatedFieldWells=LineChartAggregatedFieldWells._deserialize(json_data.get("LineChartAggregatedFieldWells")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LineChartFieldWells = LineChartFieldWells


@dataclass
class LineChartAggregatedFieldWells(BaseModel):
    Category: Optional[Sequence["_DimensionField"]]
    Values: Optional[Sequence["_MeasureField"]]
    Colors: Optional[Sequence["_DimensionField"]]
    SmallMultiples: Optional[Sequence["_DimensionField"]]

    @classmethod
    def _deserialize(
        cls: Type["_LineChartAggregatedFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LineChartAggregatedFieldWells"]:
        if not json_data:
            return None
        return cls(
            Category=deserialize_list(json_data.get("Category"), DimensionField),
            Values=deserialize_list(json_data.get("Values"), MeasureField),
            Colors=deserialize_list(json_data.get("Colors"), DimensionField),
            SmallMultiples=deserialize_list(json_data.get("SmallMultiples"), DimensionField),
        )


# work around possible type aliasing issues when variable has same name as a model
_LineChartAggregatedFieldWells = LineChartAggregatedFieldWells


@dataclass
class LineChartSortConfiguration(BaseModel):
    CategorySort: Optional[Sequence["_FieldSortOptions"]]
    CategoryItemsLimitConfiguration: Optional["_ItemsLimitConfiguration"]
    ColorItemsLimitConfiguration: Optional["_ItemsLimitConfiguration"]
    SmallMultiplesSort: Optional[Sequence["_FieldSortOptions"]]
    SmallMultiplesLimitConfiguration: Optional["_ItemsLimitConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_LineChartSortConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LineChartSortConfiguration"]:
        if not json_data:
            return None
        return cls(
            CategorySort=deserialize_list(json_data.get("CategorySort"), FieldSortOptions),
            CategoryItemsLimitConfiguration=ItemsLimitConfiguration._deserialize(json_data.get("CategoryItemsLimitConfiguration")),
            ColorItemsLimitConfiguration=ItemsLimitConfiguration._deserialize(json_data.get("ColorItemsLimitConfiguration")),
            SmallMultiplesSort=deserialize_list(json_data.get("SmallMultiplesSort"), FieldSortOptions),
            SmallMultiplesLimitConfiguration=ItemsLimitConfiguration._deserialize(json_data.get("SmallMultiplesLimitConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LineChartSortConfiguration = LineChartSortConfiguration


@dataclass
class ForecastConfiguration(BaseModel):
    ForecastProperties: Optional["_TimeBasedForecastProperties"]
    Scenario: Optional["_ForecastScenario"]

    @classmethod
    def _deserialize(
        cls: Type["_ForecastConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForecastConfiguration"]:
        if not json_data:
            return None
        return cls(
            ForecastProperties=TimeBasedForecastProperties._deserialize(json_data.get("ForecastProperties")),
            Scenario=ForecastScenario._deserialize(json_data.get("Scenario")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForecastConfiguration = ForecastConfiguration


@dataclass
class TimeBasedForecastProperties(BaseModel):
    PeriodsForward: Optional[float]
    PeriodsBackward: Optional[float]
    UpperBoundary: Optional[float]
    LowerBoundary: Optional[float]
    PredictionInterval: Optional[float]
    Seasonality: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TimeBasedForecastProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeBasedForecastProperties"]:
        if not json_data:
            return None
        return cls(
            PeriodsForward=json_data.get("PeriodsForward"),
            PeriodsBackward=json_data.get("PeriodsBackward"),
            UpperBoundary=json_data.get("UpperBoundary"),
            LowerBoundary=json_data.get("LowerBoundary"),
            PredictionInterval=json_data.get("PredictionInterval"),
            Seasonality=json_data.get("Seasonality"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeBasedForecastProperties = TimeBasedForecastProperties


@dataclass
class ForecastScenario(BaseModel):
    WhatIfPointScenario: Optional["_WhatIfPointScenario"]
    WhatIfRangeScenario: Optional["_WhatIfRangeScenario"]

    @classmethod
    def _deserialize(
        cls: Type["_ForecastScenario"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForecastScenario"]:
        if not json_data:
            return None
        return cls(
            WhatIfPointScenario=WhatIfPointScenario._deserialize(json_data.get("WhatIfPointScenario")),
            WhatIfRangeScenario=WhatIfRangeScenario._deserialize(json_data.get("WhatIfRangeScenario")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForecastScenario = ForecastScenario


@dataclass
class WhatIfPointScenario(BaseModel):
    Date: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_WhatIfPointScenario"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WhatIfPointScenario"]:
        if not json_data:
            return None
        return cls(
            Date=json_data.get("Date"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WhatIfPointScenario = WhatIfPointScenario


@dataclass
class WhatIfRangeScenario(BaseModel):
    StartDate: Optional[str]
    EndDate: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_WhatIfRangeScenario"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WhatIfRangeScenario"]:
        if not json_data:
            return None
        return cls(
            StartDate=json_data.get("StartDate"),
            EndDate=json_data.get("EndDate"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WhatIfRangeScenario = WhatIfRangeScenario


@dataclass
class LineSeriesAxisDisplayOptions(BaseModel):
    AxisOptions: Optional["_AxisDisplayOptions"]
    MissingDataConfigurations: Optional[Sequence["_MissingDataConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_LineSeriesAxisDisplayOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LineSeriesAxisDisplayOptions"]:
        if not json_data:
            return None
        return cls(
            AxisOptions=AxisDisplayOptions._deserialize(json_data.get("AxisOptions")),
            MissingDataConfigurations=deserialize_list(json_data.get("MissingDataConfigurations"), MissingDataConfiguration),
        )


# work around possible type aliasing issues when variable has same name as a model
_LineSeriesAxisDisplayOptions = LineSeriesAxisDisplayOptions


@dataclass
class MissingDataConfiguration(BaseModel):
    TreatmentOption: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MissingDataConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MissingDataConfiguration"]:
        if not json_data:
            return None
        return cls(
            TreatmentOption=json_data.get("TreatmentOption"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MissingDataConfiguration = MissingDataConfiguration


@dataclass
class LineChartDefaultSeriesSettings(BaseModel):
    AxisBinding: Optional[str]
    LineStyleSettings: Optional["_LineChartLineStyleSettings"]
    MarkerStyleSettings: Optional["_LineChartMarkerStyleSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_LineChartDefaultSeriesSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LineChartDefaultSeriesSettings"]:
        if not json_data:
            return None
        return cls(
            AxisBinding=json_data.get("AxisBinding"),
            LineStyleSettings=LineChartLineStyleSettings._deserialize(json_data.get("LineStyleSettings")),
            MarkerStyleSettings=LineChartMarkerStyleSettings._deserialize(json_data.get("MarkerStyleSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LineChartDefaultSeriesSettings = LineChartDefaultSeriesSettings


@dataclass
class LineChartLineStyleSettings(BaseModel):
    LineVisibility: Optional[str]
    LineInterpolation: Optional[str]
    LineStyle: Optional[str]
    LineWidth: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LineChartLineStyleSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LineChartLineStyleSettings"]:
        if not json_data:
            return None
        return cls(
            LineVisibility=json_data.get("LineVisibility"),
            LineInterpolation=json_data.get("LineInterpolation"),
            LineStyle=json_data.get("LineStyle"),
            LineWidth=json_data.get("LineWidth"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LineChartLineStyleSettings = LineChartLineStyleSettings


@dataclass
class LineChartMarkerStyleSettings(BaseModel):
    MarkerVisibility: Optional[str]
    MarkerShape: Optional[str]
    MarkerSize: Optional[str]
    MarkerColor: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LineChartMarkerStyleSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LineChartMarkerStyleSettings"]:
        if not json_data:
            return None
        return cls(
            MarkerVisibility=json_data.get("MarkerVisibility"),
            MarkerShape=json_data.get("MarkerShape"),
            MarkerSize=json_data.get("MarkerSize"),
            MarkerColor=json_data.get("MarkerColor"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LineChartMarkerStyleSettings = LineChartMarkerStyleSettings


@dataclass
class SeriesItem(BaseModel):
    FieldSeriesItem: Optional["_FieldSeriesItem"]
    DataFieldSeriesItem: Optional["_DataFieldSeriesItem"]

    @classmethod
    def _deserialize(
        cls: Type["_SeriesItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeriesItem"]:
        if not json_data:
            return None
        return cls(
            FieldSeriesItem=FieldSeriesItem._deserialize(json_data.get("FieldSeriesItem")),
            DataFieldSeriesItem=DataFieldSeriesItem._deserialize(json_data.get("DataFieldSeriesItem")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeriesItem = SeriesItem


@dataclass
class FieldSeriesItem(BaseModel):
    FieldId: Optional[str]
    AxisBinding: Optional[str]
    Settings: Optional["_LineChartSeriesSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_FieldSeriesItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldSeriesItem"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            AxisBinding=json_data.get("AxisBinding"),
            Settings=LineChartSeriesSettings._deserialize(json_data.get("Settings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldSeriesItem = FieldSeriesItem


@dataclass
class LineChartSeriesSettings(BaseModel):
    LineStyleSettings: Optional["_LineChartLineStyleSettings"]
    MarkerStyleSettings: Optional["_LineChartMarkerStyleSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_LineChartSeriesSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LineChartSeriesSettings"]:
        if not json_data:
            return None
        return cls(
            LineStyleSettings=LineChartLineStyleSettings._deserialize(json_data.get("LineStyleSettings")),
            MarkerStyleSettings=LineChartMarkerStyleSettings._deserialize(json_data.get("MarkerStyleSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LineChartSeriesSettings = LineChartSeriesSettings


@dataclass
class DataFieldSeriesItem(BaseModel):
    FieldId: Optional[str]
    FieldValue: Optional[str]
    AxisBinding: Optional[str]
    Settings: Optional["_LineChartSeriesSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_DataFieldSeriesItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataFieldSeriesItem"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            FieldValue=json_data.get("FieldValue"),
            AxisBinding=json_data.get("AxisBinding"),
            Settings=LineChartSeriesSettings._deserialize(json_data.get("Settings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataFieldSeriesItem = DataFieldSeriesItem


@dataclass
class HeatMapVisual(BaseModel):
    VisualId: Optional[str]
    Title: Optional["_VisualTitleLabelOptions"]
    Subtitle: Optional["_VisualSubtitleLabelOptions"]
    ChartConfiguration: Optional["_HeatMapConfiguration"]
    ColumnHierarchies: Optional[Sequence["_ColumnHierarchy"]]
    Actions: Optional[Sequence["_VisualCustomAction"]]

    @classmethod
    def _deserialize(
        cls: Type["_HeatMapVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeatMapVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            Title=VisualTitleLabelOptions._deserialize(json_data.get("Title")),
            Subtitle=VisualSubtitleLabelOptions._deserialize(json_data.get("Subtitle")),
            ChartConfiguration=HeatMapConfiguration._deserialize(json_data.get("ChartConfiguration")),
            ColumnHierarchies=deserialize_list(json_data.get("ColumnHierarchies"), ColumnHierarchy),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeatMapVisual = HeatMapVisual


@dataclass
class HeatMapConfiguration(BaseModel):
    FieldWells: Optional["_HeatMapFieldWells"]
    SortConfiguration: Optional["_HeatMapSortConfiguration"]
    RowLabelOptions: Optional["_ChartAxisLabelOptions"]
    ColumnLabelOptions: Optional["_ChartAxisLabelOptions"]
    ColorScale: Optional["_ColorScale"]
    Legend: Optional["_LegendOptions"]
    DataLabels: Optional["_DataLabelOptions"]
    Tooltip: Optional["_TooltipOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_HeatMapConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeatMapConfiguration"]:
        if not json_data:
            return None
        return cls(
            FieldWells=HeatMapFieldWells._deserialize(json_data.get("FieldWells")),
            SortConfiguration=HeatMapSortConfiguration._deserialize(json_data.get("SortConfiguration")),
            RowLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("RowLabelOptions")),
            ColumnLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("ColumnLabelOptions")),
            ColorScale=ColorScale._deserialize(json_data.get("ColorScale")),
            Legend=LegendOptions._deserialize(json_data.get("Legend")),
            DataLabels=DataLabelOptions._deserialize(json_data.get("DataLabels")),
            Tooltip=TooltipOptions._deserialize(json_data.get("Tooltip")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeatMapConfiguration = HeatMapConfiguration


@dataclass
class HeatMapFieldWells(BaseModel):
    HeatMapAggregatedFieldWells: Optional["_HeatMapAggregatedFieldWells"]

    @classmethod
    def _deserialize(
        cls: Type["_HeatMapFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeatMapFieldWells"]:
        if not json_data:
            return None
        return cls(
            HeatMapAggregatedFieldWells=HeatMapAggregatedFieldWells._deserialize(json_data.get("HeatMapAggregatedFieldWells")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeatMapFieldWells = HeatMapFieldWells


@dataclass
class HeatMapAggregatedFieldWells(BaseModel):
    Rows: Optional[Sequence["_DimensionField"]]
    Columns: Optional[Sequence["_DimensionField"]]
    Values: Optional[Sequence["_MeasureField"]]

    @classmethod
    def _deserialize(
        cls: Type["_HeatMapAggregatedFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeatMapAggregatedFieldWells"]:
        if not json_data:
            return None
        return cls(
            Rows=deserialize_list(json_data.get("Rows"), DimensionField),
            Columns=deserialize_list(json_data.get("Columns"), DimensionField),
            Values=deserialize_list(json_data.get("Values"), MeasureField),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeatMapAggregatedFieldWells = HeatMapAggregatedFieldWells


@dataclass
class HeatMapSortConfiguration(BaseModel):
    HeatMapRowSort: Optional[Sequence["_FieldSortOptions"]]
    HeatMapColumnSort: Optional[Sequence["_FieldSortOptions"]]
    HeatMapRowItemsLimitConfiguration: Optional["_ItemsLimitConfiguration"]
    HeatMapColumnItemsLimitConfiguration: Optional["_ItemsLimitConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_HeatMapSortConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeatMapSortConfiguration"]:
        if not json_data:
            return None
        return cls(
            HeatMapRowSort=deserialize_list(json_data.get("HeatMapRowSort"), FieldSortOptions),
            HeatMapColumnSort=deserialize_list(json_data.get("HeatMapColumnSort"), FieldSortOptions),
            HeatMapRowItemsLimitConfiguration=ItemsLimitConfiguration._deserialize(json_data.get("HeatMapRowItemsLimitConfiguration")),
            HeatMapColumnItemsLimitConfiguration=ItemsLimitConfiguration._deserialize(json_data.get("HeatMapColumnItemsLimitConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeatMapSortConfiguration = HeatMapSortConfiguration


@dataclass
class ColorScale(BaseModel):
    Colors: Optional[Sequence["_DataColor"]]
    ColorFillType: Optional[str]
    NullValueColor: Optional["_DataColor"]

    @classmethod
    def _deserialize(
        cls: Type["_ColorScale"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColorScale"]:
        if not json_data:
            return None
        return cls(
            Colors=deserialize_list(json_data.get("Colors"), DataColor),
            ColorFillType=json_data.get("ColorFillType"),
            NullValueColor=DataColor._deserialize(json_data.get("NullValueColor")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColorScale = ColorScale


@dataclass
class DataColor(BaseModel):
    Color: Optional[str]
    DataValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DataColor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataColor"]:
        if not json_data:
            return None
        return cls(
            Color=json_data.get("Color"),
            DataValue=json_data.get("DataValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataColor = DataColor


@dataclass
class TreeMapVisual(BaseModel):
    VisualId: Optional[str]
    Title: Optional["_VisualTitleLabelOptions"]
    Subtitle: Optional["_VisualSubtitleLabelOptions"]
    ChartConfiguration: Optional["_TreeMapConfiguration"]
    Actions: Optional[Sequence["_VisualCustomAction"]]
    ColumnHierarchies: Optional[Sequence["_ColumnHierarchy"]]

    @classmethod
    def _deserialize(
        cls: Type["_TreeMapVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TreeMapVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            Title=VisualTitleLabelOptions._deserialize(json_data.get("Title")),
            Subtitle=VisualSubtitleLabelOptions._deserialize(json_data.get("Subtitle")),
            ChartConfiguration=TreeMapConfiguration._deserialize(json_data.get("ChartConfiguration")),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
            ColumnHierarchies=deserialize_list(json_data.get("ColumnHierarchies"), ColumnHierarchy),
        )


# work around possible type aliasing issues when variable has same name as a model
_TreeMapVisual = TreeMapVisual


@dataclass
class TreeMapConfiguration(BaseModel):
    FieldWells: Optional["_TreeMapFieldWells"]
    SortConfiguration: Optional["_TreeMapSortConfiguration"]
    GroupLabelOptions: Optional["_ChartAxisLabelOptions"]
    SizeLabelOptions: Optional["_ChartAxisLabelOptions"]
    ColorLabelOptions: Optional["_ChartAxisLabelOptions"]
    ColorScale: Optional["_ColorScale"]
    Legend: Optional["_LegendOptions"]
    DataLabels: Optional["_DataLabelOptions"]
    Tooltip: Optional["_TooltipOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_TreeMapConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TreeMapConfiguration"]:
        if not json_data:
            return None
        return cls(
            FieldWells=TreeMapFieldWells._deserialize(json_data.get("FieldWells")),
            SortConfiguration=TreeMapSortConfiguration._deserialize(json_data.get("SortConfiguration")),
            GroupLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("GroupLabelOptions")),
            SizeLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("SizeLabelOptions")),
            ColorLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("ColorLabelOptions")),
            ColorScale=ColorScale._deserialize(json_data.get("ColorScale")),
            Legend=LegendOptions._deserialize(json_data.get("Legend")),
            DataLabels=DataLabelOptions._deserialize(json_data.get("DataLabels")),
            Tooltip=TooltipOptions._deserialize(json_data.get("Tooltip")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TreeMapConfiguration = TreeMapConfiguration


@dataclass
class TreeMapFieldWells(BaseModel):
    TreeMapAggregatedFieldWells: Optional["_TreeMapAggregatedFieldWells"]

    @classmethod
    def _deserialize(
        cls: Type["_TreeMapFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TreeMapFieldWells"]:
        if not json_data:
            return None
        return cls(
            TreeMapAggregatedFieldWells=TreeMapAggregatedFieldWells._deserialize(json_data.get("TreeMapAggregatedFieldWells")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TreeMapFieldWells = TreeMapFieldWells


@dataclass
class TreeMapAggregatedFieldWells(BaseModel):
    Groups: Optional[Sequence["_DimensionField"]]
    Sizes: Optional[Sequence["_MeasureField"]]
    Colors: Optional[Sequence["_MeasureField"]]

    @classmethod
    def _deserialize(
        cls: Type["_TreeMapAggregatedFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TreeMapAggregatedFieldWells"]:
        if not json_data:
            return None
        return cls(
            Groups=deserialize_list(json_data.get("Groups"), DimensionField),
            Sizes=deserialize_list(json_data.get("Sizes"), MeasureField),
            Colors=deserialize_list(json_data.get("Colors"), MeasureField),
        )


# work around possible type aliasing issues when variable has same name as a model
_TreeMapAggregatedFieldWells = TreeMapAggregatedFieldWells


@dataclass
class TreeMapSortConfiguration(BaseModel):
    TreeMapSort: Optional[Sequence["_FieldSortOptions"]]
    TreeMapGroupItemsLimitConfiguration: Optional["_ItemsLimitConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_TreeMapSortConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TreeMapSortConfiguration"]:
        if not json_data:
            return None
        return cls(
            TreeMapSort=deserialize_list(json_data.get("TreeMapSort"), FieldSortOptions),
            TreeMapGroupItemsLimitConfiguration=ItemsLimitConfiguration._deserialize(json_data.get("TreeMapGroupItemsLimitConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TreeMapSortConfiguration = TreeMapSortConfiguration


@dataclass
class GeospatialMapVisual(BaseModel):
    VisualId: Optional[str]
    Title: Optional["_VisualTitleLabelOptions"]
    Subtitle: Optional["_VisualSubtitleLabelOptions"]
    ChartConfiguration: Optional["_GeospatialMapConfiguration"]
    ColumnHierarchies: Optional[Sequence["_ColumnHierarchy"]]
    Actions: Optional[Sequence["_VisualCustomAction"]]

    @classmethod
    def _deserialize(
        cls: Type["_GeospatialMapVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeospatialMapVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            Title=VisualTitleLabelOptions._deserialize(json_data.get("Title")),
            Subtitle=VisualSubtitleLabelOptions._deserialize(json_data.get("Subtitle")),
            ChartConfiguration=GeospatialMapConfiguration._deserialize(json_data.get("ChartConfiguration")),
            ColumnHierarchies=deserialize_list(json_data.get("ColumnHierarchies"), ColumnHierarchy),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeospatialMapVisual = GeospatialMapVisual


@dataclass
class GeospatialMapConfiguration(BaseModel):
    FieldWells: Optional["_GeospatialMapFieldWells"]
    Legend: Optional["_LegendOptions"]
    Tooltip: Optional["_TooltipOptions"]
    WindowOptions: Optional["_GeospatialWindowOptions"]
    MapStyleOptions: Optional["_GeospatialMapStyleOptions"]
    PointStyleOptions: Optional["_GeospatialPointStyleOptions"]
    VisualPalette: Optional["_VisualPalette"]

    @classmethod
    def _deserialize(
        cls: Type["_GeospatialMapConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeospatialMapConfiguration"]:
        if not json_data:
            return None
        return cls(
            FieldWells=GeospatialMapFieldWells._deserialize(json_data.get("FieldWells")),
            Legend=LegendOptions._deserialize(json_data.get("Legend")),
            Tooltip=TooltipOptions._deserialize(json_data.get("Tooltip")),
            WindowOptions=GeospatialWindowOptions._deserialize(json_data.get("WindowOptions")),
            MapStyleOptions=GeospatialMapStyleOptions._deserialize(json_data.get("MapStyleOptions")),
            PointStyleOptions=GeospatialPointStyleOptions._deserialize(json_data.get("PointStyleOptions")),
            VisualPalette=VisualPalette._deserialize(json_data.get("VisualPalette")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeospatialMapConfiguration = GeospatialMapConfiguration


@dataclass
class GeospatialMapFieldWells(BaseModel):
    GeospatialMapAggregatedFieldWells: Optional["_GeospatialMapAggregatedFieldWells"]

    @classmethod
    def _deserialize(
        cls: Type["_GeospatialMapFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeospatialMapFieldWells"]:
        if not json_data:
            return None
        return cls(
            GeospatialMapAggregatedFieldWells=GeospatialMapAggregatedFieldWells._deserialize(json_data.get("GeospatialMapAggregatedFieldWells")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeospatialMapFieldWells = GeospatialMapFieldWells


@dataclass
class GeospatialMapAggregatedFieldWells(BaseModel):
    Geospatial: Optional[Sequence["_DimensionField"]]
    Values: Optional[Sequence["_MeasureField"]]
    Colors: Optional[Sequence["_DimensionField"]]

    @classmethod
    def _deserialize(
        cls: Type["_GeospatialMapAggregatedFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeospatialMapAggregatedFieldWells"]:
        if not json_data:
            return None
        return cls(
            Geospatial=deserialize_list(json_data.get("Geospatial"), DimensionField),
            Values=deserialize_list(json_data.get("Values"), MeasureField),
            Colors=deserialize_list(json_data.get("Colors"), DimensionField),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeospatialMapAggregatedFieldWells = GeospatialMapAggregatedFieldWells


@dataclass
class GeospatialWindowOptions(BaseModel):
    Bounds: Optional["_GeospatialCoordinateBounds"]
    MapZoomMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GeospatialWindowOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeospatialWindowOptions"]:
        if not json_data:
            return None
        return cls(
            Bounds=GeospatialCoordinateBounds._deserialize(json_data.get("Bounds")),
            MapZoomMode=json_data.get("MapZoomMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeospatialWindowOptions = GeospatialWindowOptions


@dataclass
class GeospatialCoordinateBounds(BaseModel):
    North: Optional[float]
    South: Optional[float]
    West: Optional[float]
    East: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_GeospatialCoordinateBounds"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeospatialCoordinateBounds"]:
        if not json_data:
            return None
        return cls(
            North=json_data.get("North"),
            South=json_data.get("South"),
            West=json_data.get("West"),
            East=json_data.get("East"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeospatialCoordinateBounds = GeospatialCoordinateBounds


@dataclass
class GeospatialMapStyleOptions(BaseModel):
    BaseMapStyle: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GeospatialMapStyleOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeospatialMapStyleOptions"]:
        if not json_data:
            return None
        return cls(
            BaseMapStyle=json_data.get("BaseMapStyle"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeospatialMapStyleOptions = GeospatialMapStyleOptions


@dataclass
class GeospatialPointStyleOptions(BaseModel):
    SelectedPointStyle: Optional[str]
    ClusterMarkerConfiguration: Optional["_ClusterMarkerConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_GeospatialPointStyleOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeospatialPointStyleOptions"]:
        if not json_data:
            return None
        return cls(
            SelectedPointStyle=json_data.get("SelectedPointStyle"),
            ClusterMarkerConfiguration=ClusterMarkerConfiguration._deserialize(json_data.get("ClusterMarkerConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeospatialPointStyleOptions = GeospatialPointStyleOptions


@dataclass
class ClusterMarkerConfiguration(BaseModel):
    ClusterMarker: Optional["_ClusterMarker"]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterMarkerConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterMarkerConfiguration"]:
        if not json_data:
            return None
        return cls(
            ClusterMarker=ClusterMarker._deserialize(json_data.get("ClusterMarker")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterMarkerConfiguration = ClusterMarkerConfiguration


@dataclass
class ClusterMarker(BaseModel):
    SimpleClusterMarker: Optional["_SimpleClusterMarker"]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterMarker"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterMarker"]:
        if not json_data:
            return None
        return cls(
            SimpleClusterMarker=SimpleClusterMarker._deserialize(json_data.get("SimpleClusterMarker")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterMarker = ClusterMarker


@dataclass
class SimpleClusterMarker(BaseModel):
    Color: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SimpleClusterMarker"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SimpleClusterMarker"]:
        if not json_data:
            return None
        return cls(
            Color=json_data.get("Color"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SimpleClusterMarker = SimpleClusterMarker


@dataclass
class FilledMapVisual(BaseModel):
    VisualId: Optional[str]
    Title: Optional["_VisualTitleLabelOptions"]
    Subtitle: Optional["_VisualSubtitleLabelOptions"]
    ChartConfiguration: Optional["_FilledMapConfiguration"]
    ConditionalFormatting: Optional["_FilledMapConditionalFormatting"]
    ColumnHierarchies: Optional[Sequence["_ColumnHierarchy"]]
    Actions: Optional[Sequence["_VisualCustomAction"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilledMapVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilledMapVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            Title=VisualTitleLabelOptions._deserialize(json_data.get("Title")),
            Subtitle=VisualSubtitleLabelOptions._deserialize(json_data.get("Subtitle")),
            ChartConfiguration=FilledMapConfiguration._deserialize(json_data.get("ChartConfiguration")),
            ConditionalFormatting=FilledMapConditionalFormatting._deserialize(json_data.get("ConditionalFormatting")),
            ColumnHierarchies=deserialize_list(json_data.get("ColumnHierarchies"), ColumnHierarchy),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilledMapVisual = FilledMapVisual


@dataclass
class FilledMapConfiguration(BaseModel):
    FieldWells: Optional["_FilledMapFieldWells"]
    SortConfiguration: Optional["_FilledMapSortConfiguration"]
    Legend: Optional["_LegendOptions"]
    Tooltip: Optional["_TooltipOptions"]
    WindowOptions: Optional["_GeospatialWindowOptions"]
    MapStyleOptions: Optional["_GeospatialMapStyleOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_FilledMapConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilledMapConfiguration"]:
        if not json_data:
            return None
        return cls(
            FieldWells=FilledMapFieldWells._deserialize(json_data.get("FieldWells")),
            SortConfiguration=FilledMapSortConfiguration._deserialize(json_data.get("SortConfiguration")),
            Legend=LegendOptions._deserialize(json_data.get("Legend")),
            Tooltip=TooltipOptions._deserialize(json_data.get("Tooltip")),
            WindowOptions=GeospatialWindowOptions._deserialize(json_data.get("WindowOptions")),
            MapStyleOptions=GeospatialMapStyleOptions._deserialize(json_data.get("MapStyleOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilledMapConfiguration = FilledMapConfiguration


@dataclass
class FilledMapFieldWells(BaseModel):
    FilledMapAggregatedFieldWells: Optional["_FilledMapAggregatedFieldWells"]

    @classmethod
    def _deserialize(
        cls: Type["_FilledMapFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilledMapFieldWells"]:
        if not json_data:
            return None
        return cls(
            FilledMapAggregatedFieldWells=FilledMapAggregatedFieldWells._deserialize(json_data.get("FilledMapAggregatedFieldWells")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilledMapFieldWells = FilledMapFieldWells


@dataclass
class FilledMapAggregatedFieldWells(BaseModel):
    Geospatial: Optional[Sequence["_DimensionField"]]
    Values: Optional[Sequence["_MeasureField"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilledMapAggregatedFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilledMapAggregatedFieldWells"]:
        if not json_data:
            return None
        return cls(
            Geospatial=deserialize_list(json_data.get("Geospatial"), DimensionField),
            Values=deserialize_list(json_data.get("Values"), MeasureField),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilledMapAggregatedFieldWells = FilledMapAggregatedFieldWells


@dataclass
class FilledMapSortConfiguration(BaseModel):
    CategorySort: Optional[Sequence["_FieldSortOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilledMapSortConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilledMapSortConfiguration"]:
        if not json_data:
            return None
        return cls(
            CategorySort=deserialize_list(json_data.get("CategorySort"), FieldSortOptions),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilledMapSortConfiguration = FilledMapSortConfiguration


@dataclass
class FilledMapConditionalFormatting(BaseModel):
    ConditionalFormattingOptions: Optional[Sequence["_FilledMapConditionalFormattingOption"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilledMapConditionalFormatting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilledMapConditionalFormatting"]:
        if not json_data:
            return None
        return cls(
            ConditionalFormattingOptions=deserialize_list(json_data.get("ConditionalFormattingOptions"), FilledMapConditionalFormattingOption),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilledMapConditionalFormatting = FilledMapConditionalFormatting


@dataclass
class FilledMapConditionalFormattingOption(BaseModel):
    Shape: Optional["_FilledMapShapeConditionalFormatting"]

    @classmethod
    def _deserialize(
        cls: Type["_FilledMapConditionalFormattingOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilledMapConditionalFormattingOption"]:
        if not json_data:
            return None
        return cls(
            Shape=FilledMapShapeConditionalFormatting._deserialize(json_data.get("Shape")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilledMapConditionalFormattingOption = FilledMapConditionalFormattingOption


@dataclass
class FilledMapShapeConditionalFormatting(BaseModel):
    FieldId: Optional[str]
    Format: Optional["_ShapeConditionalFormat"]

    @classmethod
    def _deserialize(
        cls: Type["_FilledMapShapeConditionalFormatting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilledMapShapeConditionalFormatting"]:
        if not json_data:
            return None
        return cls(
            FieldId=json_data.get("FieldId"),
            Format=ShapeConditionalFormat._deserialize(json_data.get("Format")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilledMapShapeConditionalFormatting = FilledMapShapeConditionalFormatting


@dataclass
class ShapeConditionalFormat(BaseModel):
    BackgroundColor: Optional["_ConditionalFormattingColor"]

    @classmethod
    def _deserialize(
        cls: Type["_ShapeConditionalFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShapeConditionalFormat"]:
        if not json_data:
            return None
        return cls(
            BackgroundColor=ConditionalFormattingColor._deserialize(json_data.get("BackgroundColor")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShapeConditionalFormat = ShapeConditionalFormat


@dataclass
class FunnelChartVisual(BaseModel):
    VisualId: Optional[str]
    Title: Optional["_VisualTitleLabelOptions"]
    Subtitle: Optional["_VisualSubtitleLabelOptions"]
    ChartConfiguration: Optional["_FunnelChartConfiguration"]
    Actions: Optional[Sequence["_VisualCustomAction"]]
    ColumnHierarchies: Optional[Sequence["_ColumnHierarchy"]]

    @classmethod
    def _deserialize(
        cls: Type["_FunnelChartVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FunnelChartVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            Title=VisualTitleLabelOptions._deserialize(json_data.get("Title")),
            Subtitle=VisualSubtitleLabelOptions._deserialize(json_data.get("Subtitle")),
            ChartConfiguration=FunnelChartConfiguration._deserialize(json_data.get("ChartConfiguration")),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
            ColumnHierarchies=deserialize_list(json_data.get("ColumnHierarchies"), ColumnHierarchy),
        )


# work around possible type aliasing issues when variable has same name as a model
_FunnelChartVisual = FunnelChartVisual


@dataclass
class FunnelChartConfiguration(BaseModel):
    FieldWells: Optional["_FunnelChartFieldWells"]
    SortConfiguration: Optional["_FunnelChartSortConfiguration"]
    CategoryLabelOptions: Optional["_ChartAxisLabelOptions"]
    ValueLabelOptions: Optional["_ChartAxisLabelOptions"]
    Tooltip: Optional["_TooltipOptions"]
    DataLabelOptions: Optional["_FunnelChartDataLabelOptions"]
    VisualPalette: Optional["_VisualPalette"]

    @classmethod
    def _deserialize(
        cls: Type["_FunnelChartConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FunnelChartConfiguration"]:
        if not json_data:
            return None
        return cls(
            FieldWells=FunnelChartFieldWells._deserialize(json_data.get("FieldWells")),
            SortConfiguration=FunnelChartSortConfiguration._deserialize(json_data.get("SortConfiguration")),
            CategoryLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("CategoryLabelOptions")),
            ValueLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("ValueLabelOptions")),
            Tooltip=TooltipOptions._deserialize(json_data.get("Tooltip")),
            DataLabelOptions=FunnelChartDataLabelOptions._deserialize(json_data.get("DataLabelOptions")),
            VisualPalette=VisualPalette._deserialize(json_data.get("VisualPalette")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FunnelChartConfiguration = FunnelChartConfiguration


@dataclass
class FunnelChartFieldWells(BaseModel):
    FunnelChartAggregatedFieldWells: Optional["_FunnelChartAggregatedFieldWells"]

    @classmethod
    def _deserialize(
        cls: Type["_FunnelChartFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FunnelChartFieldWells"]:
        if not json_data:
            return None
        return cls(
            FunnelChartAggregatedFieldWells=FunnelChartAggregatedFieldWells._deserialize(json_data.get("FunnelChartAggregatedFieldWells")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FunnelChartFieldWells = FunnelChartFieldWells


@dataclass
class FunnelChartAggregatedFieldWells(BaseModel):
    Category: Optional[Sequence["_DimensionField"]]
    Values: Optional[Sequence["_MeasureField"]]

    @classmethod
    def _deserialize(
        cls: Type["_FunnelChartAggregatedFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FunnelChartAggregatedFieldWells"]:
        if not json_data:
            return None
        return cls(
            Category=deserialize_list(json_data.get("Category"), DimensionField),
            Values=deserialize_list(json_data.get("Values"), MeasureField),
        )


# work around possible type aliasing issues when variable has same name as a model
_FunnelChartAggregatedFieldWells = FunnelChartAggregatedFieldWells


@dataclass
class FunnelChartSortConfiguration(BaseModel):
    CategorySort: Optional[Sequence["_FieldSortOptions"]]
    CategoryItemsLimit: Optional["_ItemsLimitConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_FunnelChartSortConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FunnelChartSortConfiguration"]:
        if not json_data:
            return None
        return cls(
            CategorySort=deserialize_list(json_data.get("CategorySort"), FieldSortOptions),
            CategoryItemsLimit=ItemsLimitConfiguration._deserialize(json_data.get("CategoryItemsLimit")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FunnelChartSortConfiguration = FunnelChartSortConfiguration


@dataclass
class FunnelChartDataLabelOptions(BaseModel):
    Visibility: Optional[str]
    CategoryLabelVisibility: Optional[str]
    MeasureLabelVisibility: Optional[str]
    Position: Optional[str]
    LabelFontConfiguration: Optional["_FontConfiguration"]
    LabelColor: Optional[str]
    MeasureDataLabelStyle: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FunnelChartDataLabelOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FunnelChartDataLabelOptions"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
            CategoryLabelVisibility=json_data.get("CategoryLabelVisibility"),
            MeasureLabelVisibility=json_data.get("MeasureLabelVisibility"),
            Position=json_data.get("Position"),
            LabelFontConfiguration=FontConfiguration._deserialize(json_data.get("LabelFontConfiguration")),
            LabelColor=json_data.get("LabelColor"),
            MeasureDataLabelStyle=json_data.get("MeasureDataLabelStyle"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FunnelChartDataLabelOptions = FunnelChartDataLabelOptions


@dataclass
class ScatterPlotVisual(BaseModel):
    VisualId: Optional[str]
    Title: Optional["_VisualTitleLabelOptions"]
    Subtitle: Optional["_VisualSubtitleLabelOptions"]
    ChartConfiguration: Optional["_ScatterPlotConfiguration"]
    Actions: Optional[Sequence["_VisualCustomAction"]]
    ColumnHierarchies: Optional[Sequence["_ColumnHierarchy"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScatterPlotVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScatterPlotVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            Title=VisualTitleLabelOptions._deserialize(json_data.get("Title")),
            Subtitle=VisualSubtitleLabelOptions._deserialize(json_data.get("Subtitle")),
            ChartConfiguration=ScatterPlotConfiguration._deserialize(json_data.get("ChartConfiguration")),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
            ColumnHierarchies=deserialize_list(json_data.get("ColumnHierarchies"), ColumnHierarchy),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScatterPlotVisual = ScatterPlotVisual


@dataclass
class ScatterPlotConfiguration(BaseModel):
    FieldWells: Optional["_ScatterPlotFieldWells"]
    XAxisLabelOptions: Optional["_ChartAxisLabelOptions"]
    XAxisDisplayOptions: Optional["_AxisDisplayOptions"]
    YAxisLabelOptions: Optional["_ChartAxisLabelOptions"]
    YAxisDisplayOptions: Optional["_AxisDisplayOptions"]
    Legend: Optional["_LegendOptions"]
    DataLabels: Optional["_DataLabelOptions"]
    Tooltip: Optional["_TooltipOptions"]
    VisualPalette: Optional["_VisualPalette"]

    @classmethod
    def _deserialize(
        cls: Type["_ScatterPlotConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScatterPlotConfiguration"]:
        if not json_data:
            return None
        return cls(
            FieldWells=ScatterPlotFieldWells._deserialize(json_data.get("FieldWells")),
            XAxisLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("XAxisLabelOptions")),
            XAxisDisplayOptions=AxisDisplayOptions._deserialize(json_data.get("XAxisDisplayOptions")),
            YAxisLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("YAxisLabelOptions")),
            YAxisDisplayOptions=AxisDisplayOptions._deserialize(json_data.get("YAxisDisplayOptions")),
            Legend=LegendOptions._deserialize(json_data.get("Legend")),
            DataLabels=DataLabelOptions._deserialize(json_data.get("DataLabels")),
            Tooltip=TooltipOptions._deserialize(json_data.get("Tooltip")),
            VisualPalette=VisualPalette._deserialize(json_data.get("VisualPalette")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScatterPlotConfiguration = ScatterPlotConfiguration


@dataclass
class ScatterPlotFieldWells(BaseModel):
    ScatterPlotCategoricallyAggregatedFieldWells: Optional["_ScatterPlotCategoricallyAggregatedFieldWells"]
    ScatterPlotUnaggregatedFieldWells: Optional["_ScatterPlotUnaggregatedFieldWells"]

    @classmethod
    def _deserialize(
        cls: Type["_ScatterPlotFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScatterPlotFieldWells"]:
        if not json_data:
            return None
        return cls(
            ScatterPlotCategoricallyAggregatedFieldWells=ScatterPlotCategoricallyAggregatedFieldWells._deserialize(json_data.get("ScatterPlotCategoricallyAggregatedFieldWells")),
            ScatterPlotUnaggregatedFieldWells=ScatterPlotUnaggregatedFieldWells._deserialize(json_data.get("ScatterPlotUnaggregatedFieldWells")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScatterPlotFieldWells = ScatterPlotFieldWells


@dataclass
class ScatterPlotCategoricallyAggregatedFieldWells(BaseModel):
    XAxis: Optional[Sequence["_MeasureField"]]
    YAxis: Optional[Sequence["_MeasureField"]]
    Category: Optional[Sequence["_DimensionField"]]
    Size: Optional[Sequence["_MeasureField"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScatterPlotCategoricallyAggregatedFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScatterPlotCategoricallyAggregatedFieldWells"]:
        if not json_data:
            return None
        return cls(
            XAxis=deserialize_list(json_data.get("XAxis"), MeasureField),
            YAxis=deserialize_list(json_data.get("YAxis"), MeasureField),
            Category=deserialize_list(json_data.get("Category"), DimensionField),
            Size=deserialize_list(json_data.get("Size"), MeasureField),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScatterPlotCategoricallyAggregatedFieldWells = ScatterPlotCategoricallyAggregatedFieldWells


@dataclass
class ScatterPlotUnaggregatedFieldWells(BaseModel):
    XAxis: Optional[Sequence["_DimensionField"]]
    YAxis: Optional[Sequence["_DimensionField"]]
    Size: Optional[Sequence["_MeasureField"]]

    @classmethod
    def _deserialize(
        cls: Type["_ScatterPlotUnaggregatedFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScatterPlotUnaggregatedFieldWells"]:
        if not json_data:
            return None
        return cls(
            XAxis=deserialize_list(json_data.get("XAxis"), DimensionField),
            YAxis=deserialize_list(json_data.get("YAxis"), DimensionField),
            Size=deserialize_list(json_data.get("Size"), MeasureField),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScatterPlotUnaggregatedFieldWells = ScatterPlotUnaggregatedFieldWells


@dataclass
class ComboChartVisual(BaseModel):
    VisualId: Optional[str]
    Title: Optional["_VisualTitleLabelOptions"]
    Subtitle: Optional["_VisualSubtitleLabelOptions"]
    ChartConfiguration: Optional["_ComboChartConfiguration"]
    Actions: Optional[Sequence["_VisualCustomAction"]]
    ColumnHierarchies: Optional[Sequence["_ColumnHierarchy"]]

    @classmethod
    def _deserialize(
        cls: Type["_ComboChartVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComboChartVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            Title=VisualTitleLabelOptions._deserialize(json_data.get("Title")),
            Subtitle=VisualSubtitleLabelOptions._deserialize(json_data.get("Subtitle")),
            ChartConfiguration=ComboChartConfiguration._deserialize(json_data.get("ChartConfiguration")),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
            ColumnHierarchies=deserialize_list(json_data.get("ColumnHierarchies"), ColumnHierarchy),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComboChartVisual = ComboChartVisual


@dataclass
class ComboChartConfiguration(BaseModel):
    FieldWells: Optional["_ComboChartFieldWells"]
    SortConfiguration: Optional["_ComboChartSortConfiguration"]
    BarsArrangement: Optional[str]
    CategoryAxis: Optional["_AxisDisplayOptions"]
    CategoryLabelOptions: Optional["_ChartAxisLabelOptions"]
    PrimaryYAxisDisplayOptions: Optional["_AxisDisplayOptions"]
    PrimaryYAxisLabelOptions: Optional["_ChartAxisLabelOptions"]
    SecondaryYAxisDisplayOptions: Optional["_AxisDisplayOptions"]
    SecondaryYAxisLabelOptions: Optional["_ChartAxisLabelOptions"]
    ColorLabelOptions: Optional["_ChartAxisLabelOptions"]
    Legend: Optional["_LegendOptions"]
    BarDataLabels: Optional["_DataLabelOptions"]
    LineDataLabels: Optional["_DataLabelOptions"]
    Tooltip: Optional["_TooltipOptions"]
    ReferenceLines: Optional[Sequence["_ReferenceLine"]]
    VisualPalette: Optional["_VisualPalette"]

    @classmethod
    def _deserialize(
        cls: Type["_ComboChartConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComboChartConfiguration"]:
        if not json_data:
            return None
        return cls(
            FieldWells=ComboChartFieldWells._deserialize(json_data.get("FieldWells")),
            SortConfiguration=ComboChartSortConfiguration._deserialize(json_data.get("SortConfiguration")),
            BarsArrangement=json_data.get("BarsArrangement"),
            CategoryAxis=AxisDisplayOptions._deserialize(json_data.get("CategoryAxis")),
            CategoryLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("CategoryLabelOptions")),
            PrimaryYAxisDisplayOptions=AxisDisplayOptions._deserialize(json_data.get("PrimaryYAxisDisplayOptions")),
            PrimaryYAxisLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("PrimaryYAxisLabelOptions")),
            SecondaryYAxisDisplayOptions=AxisDisplayOptions._deserialize(json_data.get("SecondaryYAxisDisplayOptions")),
            SecondaryYAxisLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("SecondaryYAxisLabelOptions")),
            ColorLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("ColorLabelOptions")),
            Legend=LegendOptions._deserialize(json_data.get("Legend")),
            BarDataLabels=DataLabelOptions._deserialize(json_data.get("BarDataLabels")),
            LineDataLabels=DataLabelOptions._deserialize(json_data.get("LineDataLabels")),
            Tooltip=TooltipOptions._deserialize(json_data.get("Tooltip")),
            ReferenceLines=deserialize_list(json_data.get("ReferenceLines"), ReferenceLine),
            VisualPalette=VisualPalette._deserialize(json_data.get("VisualPalette")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComboChartConfiguration = ComboChartConfiguration


@dataclass
class ComboChartFieldWells(BaseModel):
    ComboChartAggregatedFieldWells: Optional["_ComboChartAggregatedFieldWells"]

    @classmethod
    def _deserialize(
        cls: Type["_ComboChartFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComboChartFieldWells"]:
        if not json_data:
            return None
        return cls(
            ComboChartAggregatedFieldWells=ComboChartAggregatedFieldWells._deserialize(json_data.get("ComboChartAggregatedFieldWells")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComboChartFieldWells = ComboChartFieldWells


@dataclass
class ComboChartAggregatedFieldWells(BaseModel):
    Category: Optional[Sequence["_DimensionField"]]
    BarValues: Optional[Sequence["_MeasureField"]]
    Colors: Optional[Sequence["_DimensionField"]]
    LineValues: Optional[Sequence["_MeasureField"]]

    @classmethod
    def _deserialize(
        cls: Type["_ComboChartAggregatedFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComboChartAggregatedFieldWells"]:
        if not json_data:
            return None
        return cls(
            Category=deserialize_list(json_data.get("Category"), DimensionField),
            BarValues=deserialize_list(json_data.get("BarValues"), MeasureField),
            Colors=deserialize_list(json_data.get("Colors"), DimensionField),
            LineValues=deserialize_list(json_data.get("LineValues"), MeasureField),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComboChartAggregatedFieldWells = ComboChartAggregatedFieldWells


@dataclass
class ComboChartSortConfiguration(BaseModel):
    CategorySort: Optional[Sequence["_FieldSortOptions"]]
    CategoryItemsLimit: Optional["_ItemsLimitConfiguration"]
    ColorSort: Optional[Sequence["_FieldSortOptions"]]
    ColorItemsLimit: Optional["_ItemsLimitConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ComboChartSortConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComboChartSortConfiguration"]:
        if not json_data:
            return None
        return cls(
            CategorySort=deserialize_list(json_data.get("CategorySort"), FieldSortOptions),
            CategoryItemsLimit=ItemsLimitConfiguration._deserialize(json_data.get("CategoryItemsLimit")),
            ColorSort=deserialize_list(json_data.get("ColorSort"), FieldSortOptions),
            ColorItemsLimit=ItemsLimitConfiguration._deserialize(json_data.get("ColorItemsLimit")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComboChartSortConfiguration = ComboChartSortConfiguration


@dataclass
class BoxPlotVisual(BaseModel):
    VisualId: Optional[str]
    Title: Optional["_VisualTitleLabelOptions"]
    Subtitle: Optional["_VisualSubtitleLabelOptions"]
    ChartConfiguration: Optional["_BoxPlotChartConfiguration"]
    Actions: Optional[Sequence["_VisualCustomAction"]]
    ColumnHierarchies: Optional[Sequence["_ColumnHierarchy"]]

    @classmethod
    def _deserialize(
        cls: Type["_BoxPlotVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BoxPlotVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            Title=VisualTitleLabelOptions._deserialize(json_data.get("Title")),
            Subtitle=VisualSubtitleLabelOptions._deserialize(json_data.get("Subtitle")),
            ChartConfiguration=BoxPlotChartConfiguration._deserialize(json_data.get("ChartConfiguration")),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
            ColumnHierarchies=deserialize_list(json_data.get("ColumnHierarchies"), ColumnHierarchy),
        )


# work around possible type aliasing issues when variable has same name as a model
_BoxPlotVisual = BoxPlotVisual


@dataclass
class BoxPlotChartConfiguration(BaseModel):
    FieldWells: Optional["_BoxPlotFieldWells"]
    SortConfiguration: Optional["_BoxPlotSortConfiguration"]
    BoxPlotOptions: Optional["_BoxPlotOptions"]
    CategoryAxis: Optional["_AxisDisplayOptions"]
    CategoryLabelOptions: Optional["_ChartAxisLabelOptions"]
    PrimaryYAxisDisplayOptions: Optional["_AxisDisplayOptions"]
    PrimaryYAxisLabelOptions: Optional["_ChartAxisLabelOptions"]
    Legend: Optional["_LegendOptions"]
    Tooltip: Optional["_TooltipOptions"]
    ReferenceLines: Optional[Sequence["_ReferenceLine"]]
    VisualPalette: Optional["_VisualPalette"]

    @classmethod
    def _deserialize(
        cls: Type["_BoxPlotChartConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BoxPlotChartConfiguration"]:
        if not json_data:
            return None
        return cls(
            FieldWells=BoxPlotFieldWells._deserialize(json_data.get("FieldWells")),
            SortConfiguration=BoxPlotSortConfiguration._deserialize(json_data.get("SortConfiguration")),
            BoxPlotOptions=BoxPlotOptions._deserialize(json_data.get("BoxPlotOptions")),
            CategoryAxis=AxisDisplayOptions._deserialize(json_data.get("CategoryAxis")),
            CategoryLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("CategoryLabelOptions")),
            PrimaryYAxisDisplayOptions=AxisDisplayOptions._deserialize(json_data.get("PrimaryYAxisDisplayOptions")),
            PrimaryYAxisLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("PrimaryYAxisLabelOptions")),
            Legend=LegendOptions._deserialize(json_data.get("Legend")),
            Tooltip=TooltipOptions._deserialize(json_data.get("Tooltip")),
            ReferenceLines=deserialize_list(json_data.get("ReferenceLines"), ReferenceLine),
            VisualPalette=VisualPalette._deserialize(json_data.get("VisualPalette")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BoxPlotChartConfiguration = BoxPlotChartConfiguration


@dataclass
class BoxPlotFieldWells(BaseModel):
    BoxPlotAggregatedFieldWells: Optional["_BoxPlotAggregatedFieldWells"]

    @classmethod
    def _deserialize(
        cls: Type["_BoxPlotFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BoxPlotFieldWells"]:
        if not json_data:
            return None
        return cls(
            BoxPlotAggregatedFieldWells=BoxPlotAggregatedFieldWells._deserialize(json_data.get("BoxPlotAggregatedFieldWells")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BoxPlotFieldWells = BoxPlotFieldWells


@dataclass
class BoxPlotAggregatedFieldWells(BaseModel):
    GroupBy: Optional[Sequence["_DimensionField"]]
    Values: Optional[Sequence["_MeasureField"]]

    @classmethod
    def _deserialize(
        cls: Type["_BoxPlotAggregatedFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BoxPlotAggregatedFieldWells"]:
        if not json_data:
            return None
        return cls(
            GroupBy=deserialize_list(json_data.get("GroupBy"), DimensionField),
            Values=deserialize_list(json_data.get("Values"), MeasureField),
        )


# work around possible type aliasing issues when variable has same name as a model
_BoxPlotAggregatedFieldWells = BoxPlotAggregatedFieldWells


@dataclass
class BoxPlotSortConfiguration(BaseModel):
    CategorySort: Optional[Sequence["_FieldSortOptions"]]
    PaginationConfiguration: Optional["_PaginationConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_BoxPlotSortConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BoxPlotSortConfiguration"]:
        if not json_data:
            return None
        return cls(
            CategorySort=deserialize_list(json_data.get("CategorySort"), FieldSortOptions),
            PaginationConfiguration=PaginationConfiguration._deserialize(json_data.get("PaginationConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BoxPlotSortConfiguration = BoxPlotSortConfiguration


@dataclass
class BoxPlotOptions(BaseModel):
    StyleOptions: Optional["_BoxPlotStyleOptions"]
    OutlierVisibility: Optional[str]
    AllDataPointsVisibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BoxPlotOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BoxPlotOptions"]:
        if not json_data:
            return None
        return cls(
            StyleOptions=BoxPlotStyleOptions._deserialize(json_data.get("StyleOptions")),
            OutlierVisibility=json_data.get("OutlierVisibility"),
            AllDataPointsVisibility=json_data.get("AllDataPointsVisibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BoxPlotOptions = BoxPlotOptions


@dataclass
class BoxPlotStyleOptions(BaseModel):
    FillStyle: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BoxPlotStyleOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BoxPlotStyleOptions"]:
        if not json_data:
            return None
        return cls(
            FillStyle=json_data.get("FillStyle"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BoxPlotStyleOptions = BoxPlotStyleOptions


@dataclass
class WaterfallVisual(BaseModel):
    VisualId: Optional[str]
    Title: Optional["_VisualTitleLabelOptions"]
    Subtitle: Optional["_VisualSubtitleLabelOptions"]
    ChartConfiguration: Optional["_WaterfallChartConfiguration"]
    Actions: Optional[Sequence["_VisualCustomAction"]]
    ColumnHierarchies: Optional[Sequence["_ColumnHierarchy"]]

    @classmethod
    def _deserialize(
        cls: Type["_WaterfallVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WaterfallVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            Title=VisualTitleLabelOptions._deserialize(json_data.get("Title")),
            Subtitle=VisualSubtitleLabelOptions._deserialize(json_data.get("Subtitle")),
            ChartConfiguration=WaterfallChartConfiguration._deserialize(json_data.get("ChartConfiguration")),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
            ColumnHierarchies=deserialize_list(json_data.get("ColumnHierarchies"), ColumnHierarchy),
        )


# work around possible type aliasing issues when variable has same name as a model
_WaterfallVisual = WaterfallVisual


@dataclass
class WaterfallChartConfiguration(BaseModel):
    FieldWells: Optional["_WaterfallChartFieldWells"]
    SortConfiguration: Optional["_WaterfallChartSortConfiguration"]
    WaterfallChartOptions: Optional["_WaterfallChartOptions"]
    CategoryAxisLabelOptions: Optional["_ChartAxisLabelOptions"]
    CategoryAxisDisplayOptions: Optional["_AxisDisplayOptions"]
    PrimaryYAxisLabelOptions: Optional["_ChartAxisLabelOptions"]
    PrimaryYAxisDisplayOptions: Optional["_AxisDisplayOptions"]
    Legend: Optional["_LegendOptions"]
    DataLabels: Optional["_DataLabelOptions"]
    VisualPalette: Optional["_VisualPalette"]

    @classmethod
    def _deserialize(
        cls: Type["_WaterfallChartConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WaterfallChartConfiguration"]:
        if not json_data:
            return None
        return cls(
            FieldWells=WaterfallChartFieldWells._deserialize(json_data.get("FieldWells")),
            SortConfiguration=WaterfallChartSortConfiguration._deserialize(json_data.get("SortConfiguration")),
            WaterfallChartOptions=WaterfallChartOptions._deserialize(json_data.get("WaterfallChartOptions")),
            CategoryAxisLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("CategoryAxisLabelOptions")),
            CategoryAxisDisplayOptions=AxisDisplayOptions._deserialize(json_data.get("CategoryAxisDisplayOptions")),
            PrimaryYAxisLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("PrimaryYAxisLabelOptions")),
            PrimaryYAxisDisplayOptions=AxisDisplayOptions._deserialize(json_data.get("PrimaryYAxisDisplayOptions")),
            Legend=LegendOptions._deserialize(json_data.get("Legend")),
            DataLabels=DataLabelOptions._deserialize(json_data.get("DataLabels")),
            VisualPalette=VisualPalette._deserialize(json_data.get("VisualPalette")),
        )


# work around possible type aliasing issues when variable has same name as a model
_WaterfallChartConfiguration = WaterfallChartConfiguration


@dataclass
class WaterfallChartFieldWells(BaseModel):
    WaterfallChartAggregatedFieldWells: Optional["_WaterfallChartAggregatedFieldWells"]

    @classmethod
    def _deserialize(
        cls: Type["_WaterfallChartFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WaterfallChartFieldWells"]:
        if not json_data:
            return None
        return cls(
            WaterfallChartAggregatedFieldWells=WaterfallChartAggregatedFieldWells._deserialize(json_data.get("WaterfallChartAggregatedFieldWells")),
        )


# work around possible type aliasing issues when variable has same name as a model
_WaterfallChartFieldWells = WaterfallChartFieldWells


@dataclass
class WaterfallChartAggregatedFieldWells(BaseModel):
    Categories: Optional[Sequence["_DimensionField"]]
    Values: Optional[Sequence["_MeasureField"]]
    Breakdowns: Optional[Sequence["_DimensionField"]]

    @classmethod
    def _deserialize(
        cls: Type["_WaterfallChartAggregatedFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WaterfallChartAggregatedFieldWells"]:
        if not json_data:
            return None
        return cls(
            Categories=deserialize_list(json_data.get("Categories"), DimensionField),
            Values=deserialize_list(json_data.get("Values"), MeasureField),
            Breakdowns=deserialize_list(json_data.get("Breakdowns"), DimensionField),
        )


# work around possible type aliasing issues when variable has same name as a model
_WaterfallChartAggregatedFieldWells = WaterfallChartAggregatedFieldWells


@dataclass
class WaterfallChartSortConfiguration(BaseModel):
    CategorySort: Optional[Sequence["_FieldSortOptions"]]
    BreakdownItemsLimit: Optional["_ItemsLimitConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_WaterfallChartSortConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WaterfallChartSortConfiguration"]:
        if not json_data:
            return None
        return cls(
            CategorySort=deserialize_list(json_data.get("CategorySort"), FieldSortOptions),
            BreakdownItemsLimit=ItemsLimitConfiguration._deserialize(json_data.get("BreakdownItemsLimit")),
        )


# work around possible type aliasing issues when variable has same name as a model
_WaterfallChartSortConfiguration = WaterfallChartSortConfiguration


@dataclass
class WaterfallChartOptions(BaseModel):
    TotalBarLabel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WaterfallChartOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WaterfallChartOptions"]:
        if not json_data:
            return None
        return cls(
            TotalBarLabel=json_data.get("TotalBarLabel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WaterfallChartOptions = WaterfallChartOptions


@dataclass
class HistogramVisual(BaseModel):
    VisualId: Optional[str]
    Title: Optional["_VisualTitleLabelOptions"]
    Subtitle: Optional["_VisualSubtitleLabelOptions"]
    ChartConfiguration: Optional["_HistogramConfiguration"]
    Actions: Optional[Sequence["_VisualCustomAction"]]

    @classmethod
    def _deserialize(
        cls: Type["_HistogramVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HistogramVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            Title=VisualTitleLabelOptions._deserialize(json_data.get("Title")),
            Subtitle=VisualSubtitleLabelOptions._deserialize(json_data.get("Subtitle")),
            ChartConfiguration=HistogramConfiguration._deserialize(json_data.get("ChartConfiguration")),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
        )


# work around possible type aliasing issues when variable has same name as a model
_HistogramVisual = HistogramVisual


@dataclass
class HistogramConfiguration(BaseModel):
    FieldWells: Optional["_HistogramFieldWells"]
    XAxisDisplayOptions: Optional["_AxisDisplayOptions"]
    XAxisLabelOptions: Optional["_ChartAxisLabelOptions"]
    YAxisDisplayOptions: Optional["_AxisDisplayOptions"]
    BinOptions: Optional["_HistogramBinOptions"]
    DataLabels: Optional["_DataLabelOptions"]
    Tooltip: Optional["_TooltipOptions"]
    VisualPalette: Optional["_VisualPalette"]

    @classmethod
    def _deserialize(
        cls: Type["_HistogramConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HistogramConfiguration"]:
        if not json_data:
            return None
        return cls(
            FieldWells=HistogramFieldWells._deserialize(json_data.get("FieldWells")),
            XAxisDisplayOptions=AxisDisplayOptions._deserialize(json_data.get("XAxisDisplayOptions")),
            XAxisLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("XAxisLabelOptions")),
            YAxisDisplayOptions=AxisDisplayOptions._deserialize(json_data.get("YAxisDisplayOptions")),
            BinOptions=HistogramBinOptions._deserialize(json_data.get("BinOptions")),
            DataLabels=DataLabelOptions._deserialize(json_data.get("DataLabels")),
            Tooltip=TooltipOptions._deserialize(json_data.get("Tooltip")),
            VisualPalette=VisualPalette._deserialize(json_data.get("VisualPalette")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HistogramConfiguration = HistogramConfiguration


@dataclass
class HistogramFieldWells(BaseModel):
    HistogramAggregatedFieldWells: Optional["_HistogramAggregatedFieldWells"]

    @classmethod
    def _deserialize(
        cls: Type["_HistogramFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HistogramFieldWells"]:
        if not json_data:
            return None
        return cls(
            HistogramAggregatedFieldWells=HistogramAggregatedFieldWells._deserialize(json_data.get("HistogramAggregatedFieldWells")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HistogramFieldWells = HistogramFieldWells


@dataclass
class HistogramAggregatedFieldWells(BaseModel):
    Values: Optional[Sequence["_MeasureField"]]

    @classmethod
    def _deserialize(
        cls: Type["_HistogramAggregatedFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HistogramAggregatedFieldWells"]:
        if not json_data:
            return None
        return cls(
            Values=deserialize_list(json_data.get("Values"), MeasureField),
        )


# work around possible type aliasing issues when variable has same name as a model
_HistogramAggregatedFieldWells = HistogramAggregatedFieldWells


@dataclass
class HistogramBinOptions(BaseModel):
    SelectedBinType: Optional[str]
    BinCount: Optional["_BinCountOptions"]
    BinWidth: Optional["_BinWidthOptions"]
    StartValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HistogramBinOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HistogramBinOptions"]:
        if not json_data:
            return None
        return cls(
            SelectedBinType=json_data.get("SelectedBinType"),
            BinCount=BinCountOptions._deserialize(json_data.get("BinCount")),
            BinWidth=BinWidthOptions._deserialize(json_data.get("BinWidth")),
            StartValue=json_data.get("StartValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HistogramBinOptions = HistogramBinOptions


@dataclass
class BinCountOptions(BaseModel):
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BinCountOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BinCountOptions"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BinCountOptions = BinCountOptions


@dataclass
class BinWidthOptions(BaseModel):
    Value: Optional[float]
    BinCountLimit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BinWidthOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BinWidthOptions"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            BinCountLimit=json_data.get("BinCountLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BinWidthOptions = BinWidthOptions


@dataclass
class WordCloudVisual(BaseModel):
    VisualId: Optional[str]
    Title: Optional["_VisualTitleLabelOptions"]
    Subtitle: Optional["_VisualSubtitleLabelOptions"]
    ChartConfiguration: Optional["_WordCloudChartConfiguration"]
    Actions: Optional[Sequence["_VisualCustomAction"]]
    ColumnHierarchies: Optional[Sequence["_ColumnHierarchy"]]

    @classmethod
    def _deserialize(
        cls: Type["_WordCloudVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WordCloudVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            Title=VisualTitleLabelOptions._deserialize(json_data.get("Title")),
            Subtitle=VisualSubtitleLabelOptions._deserialize(json_data.get("Subtitle")),
            ChartConfiguration=WordCloudChartConfiguration._deserialize(json_data.get("ChartConfiguration")),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
            ColumnHierarchies=deserialize_list(json_data.get("ColumnHierarchies"), ColumnHierarchy),
        )


# work around possible type aliasing issues when variable has same name as a model
_WordCloudVisual = WordCloudVisual


@dataclass
class WordCloudChartConfiguration(BaseModel):
    FieldWells: Optional["_WordCloudFieldWells"]
    SortConfiguration: Optional["_WordCloudSortConfiguration"]
    CategoryLabelOptions: Optional["_ChartAxisLabelOptions"]
    WordCloudOptions: Optional["_WordCloudOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_WordCloudChartConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WordCloudChartConfiguration"]:
        if not json_data:
            return None
        return cls(
            FieldWells=WordCloudFieldWells._deserialize(json_data.get("FieldWells")),
            SortConfiguration=WordCloudSortConfiguration._deserialize(json_data.get("SortConfiguration")),
            CategoryLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("CategoryLabelOptions")),
            WordCloudOptions=WordCloudOptions._deserialize(json_data.get("WordCloudOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_WordCloudChartConfiguration = WordCloudChartConfiguration


@dataclass
class WordCloudFieldWells(BaseModel):
    WordCloudAggregatedFieldWells: Optional["_WordCloudAggregatedFieldWells"]

    @classmethod
    def _deserialize(
        cls: Type["_WordCloudFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WordCloudFieldWells"]:
        if not json_data:
            return None
        return cls(
            WordCloudAggregatedFieldWells=WordCloudAggregatedFieldWells._deserialize(json_data.get("WordCloudAggregatedFieldWells")),
        )


# work around possible type aliasing issues when variable has same name as a model
_WordCloudFieldWells = WordCloudFieldWells


@dataclass
class WordCloudAggregatedFieldWells(BaseModel):
    GroupBy: Optional[Sequence["_DimensionField"]]
    Size: Optional[Sequence["_MeasureField"]]

    @classmethod
    def _deserialize(
        cls: Type["_WordCloudAggregatedFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WordCloudAggregatedFieldWells"]:
        if not json_data:
            return None
        return cls(
            GroupBy=deserialize_list(json_data.get("GroupBy"), DimensionField),
            Size=deserialize_list(json_data.get("Size"), MeasureField),
        )


# work around possible type aliasing issues when variable has same name as a model
_WordCloudAggregatedFieldWells = WordCloudAggregatedFieldWells


@dataclass
class WordCloudSortConfiguration(BaseModel):
    CategoryItemsLimit: Optional["_ItemsLimitConfiguration"]
    CategorySort: Optional[Sequence["_FieldSortOptions"]]

    @classmethod
    def _deserialize(
        cls: Type["_WordCloudSortConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WordCloudSortConfiguration"]:
        if not json_data:
            return None
        return cls(
            CategoryItemsLimit=ItemsLimitConfiguration._deserialize(json_data.get("CategoryItemsLimit")),
            CategorySort=deserialize_list(json_data.get("CategorySort"), FieldSortOptions),
        )


# work around possible type aliasing issues when variable has same name as a model
_WordCloudSortConfiguration = WordCloudSortConfiguration


@dataclass
class WordCloudOptions(BaseModel):
    WordOrientation: Optional[str]
    WordScaling: Optional[str]
    CloudLayout: Optional[str]
    WordCasing: Optional[str]
    WordPadding: Optional[str]
    MaximumStringLength: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_WordCloudOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WordCloudOptions"]:
        if not json_data:
            return None
        return cls(
            WordOrientation=json_data.get("WordOrientation"),
            WordScaling=json_data.get("WordScaling"),
            CloudLayout=json_data.get("CloudLayout"),
            WordCasing=json_data.get("WordCasing"),
            WordPadding=json_data.get("WordPadding"),
            MaximumStringLength=json_data.get("MaximumStringLength"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WordCloudOptions = WordCloudOptions


@dataclass
class InsightVisual(BaseModel):
    VisualId: Optional[str]
    Title: Optional["_VisualTitleLabelOptions"]
    Subtitle: Optional["_VisualSubtitleLabelOptions"]
    InsightConfiguration: Optional["_InsightConfiguration"]
    Actions: Optional[Sequence["_VisualCustomAction"]]
    DataSetIdentifier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InsightVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InsightVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            Title=VisualTitleLabelOptions._deserialize(json_data.get("Title")),
            Subtitle=VisualSubtitleLabelOptions._deserialize(json_data.get("Subtitle")),
            InsightConfiguration=InsightConfiguration._deserialize(json_data.get("InsightConfiguration")),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
            DataSetIdentifier=json_data.get("DataSetIdentifier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InsightVisual = InsightVisual


@dataclass
class InsightConfiguration(BaseModel):
    Computations: Optional[Sequence["_Computation"]]
    CustomNarrative: Optional["_CustomNarrativeOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_InsightConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InsightConfiguration"]:
        if not json_data:
            return None
        return cls(
            Computations=deserialize_list(json_data.get("Computations"), Computation),
            CustomNarrative=CustomNarrativeOptions._deserialize(json_data.get("CustomNarrative")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InsightConfiguration = InsightConfiguration


@dataclass
class Computation(BaseModel):
    TopBottomRanked: Optional["_TopBottomRankedComputation"]
    TopBottomMovers: Optional["_TopBottomMoversComputation"]
    TotalAggregation: Optional["_TotalAggregationComputation"]
    MaximumMinimum: Optional["_MaximumMinimumComputation"]
    MetricComparison: Optional["_MetricComparisonComputation"]
    PeriodOverPeriod: Optional["_PeriodOverPeriodComputation"]
    PeriodToDate: Optional["_PeriodToDateComputation"]
    GrowthRate: Optional["_GrowthRateComputation"]
    UniqueValues: Optional["_UniqueValuesComputation"]
    Forecast: Optional["_ForecastComputation"]

    @classmethod
    def _deserialize(
        cls: Type["_Computation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Computation"]:
        if not json_data:
            return None
        return cls(
            TopBottomRanked=TopBottomRankedComputation._deserialize(json_data.get("TopBottomRanked")),
            TopBottomMovers=TopBottomMoversComputation._deserialize(json_data.get("TopBottomMovers")),
            TotalAggregation=TotalAggregationComputation._deserialize(json_data.get("TotalAggregation")),
            MaximumMinimum=MaximumMinimumComputation._deserialize(json_data.get("MaximumMinimum")),
            MetricComparison=MetricComparisonComputation._deserialize(json_data.get("MetricComparison")),
            PeriodOverPeriod=PeriodOverPeriodComputation._deserialize(json_data.get("PeriodOverPeriod")),
            PeriodToDate=PeriodToDateComputation._deserialize(json_data.get("PeriodToDate")),
            GrowthRate=GrowthRateComputation._deserialize(json_data.get("GrowthRate")),
            UniqueValues=UniqueValuesComputation._deserialize(json_data.get("UniqueValues")),
            Forecast=ForecastComputation._deserialize(json_data.get("Forecast")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Computation = Computation


@dataclass
class TopBottomRankedComputation(BaseModel):
    ComputationId: Optional[str]
    Name: Optional[str]
    Category: Optional["_DimensionField"]
    Value: Optional["_MeasureField"]
    ResultSize: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TopBottomRankedComputation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopBottomRankedComputation"]:
        if not json_data:
            return None
        return cls(
            ComputationId=json_data.get("ComputationId"),
            Name=json_data.get("Name"),
            Category=DimensionField._deserialize(json_data.get("Category")),
            Value=MeasureField._deserialize(json_data.get("Value")),
            ResultSize=json_data.get("ResultSize"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopBottomRankedComputation = TopBottomRankedComputation


@dataclass
class TopBottomMoversComputation(BaseModel):
    ComputationId: Optional[str]
    Name: Optional[str]
    Time: Optional["_DimensionField"]
    Category: Optional["_DimensionField"]
    Value: Optional["_MeasureField"]
    MoverSize: Optional[float]
    SortOrder: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TopBottomMoversComputation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopBottomMoversComputation"]:
        if not json_data:
            return None
        return cls(
            ComputationId=json_data.get("ComputationId"),
            Name=json_data.get("Name"),
            Time=DimensionField._deserialize(json_data.get("Time")),
            Category=DimensionField._deserialize(json_data.get("Category")),
            Value=MeasureField._deserialize(json_data.get("Value")),
            MoverSize=json_data.get("MoverSize"),
            SortOrder=json_data.get("SortOrder"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopBottomMoversComputation = TopBottomMoversComputation


@dataclass
class TotalAggregationComputation(BaseModel):
    ComputationId: Optional[str]
    Name: Optional[str]
    Value: Optional["_MeasureField"]

    @classmethod
    def _deserialize(
        cls: Type["_TotalAggregationComputation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TotalAggregationComputation"]:
        if not json_data:
            return None
        return cls(
            ComputationId=json_data.get("ComputationId"),
            Name=json_data.get("Name"),
            Value=MeasureField._deserialize(json_data.get("Value")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TotalAggregationComputation = TotalAggregationComputation


@dataclass
class MaximumMinimumComputation(BaseModel):
    ComputationId: Optional[str]
    Name: Optional[str]
    Time: Optional["_DimensionField"]
    Value: Optional["_MeasureField"]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaximumMinimumComputation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaximumMinimumComputation"]:
        if not json_data:
            return None
        return cls(
            ComputationId=json_data.get("ComputationId"),
            Name=json_data.get("Name"),
            Time=DimensionField._deserialize(json_data.get("Time")),
            Value=MeasureField._deserialize(json_data.get("Value")),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaximumMinimumComputation = MaximumMinimumComputation


@dataclass
class MetricComparisonComputation(BaseModel):
    ComputationId: Optional[str]
    Name: Optional[str]
    Time: Optional["_DimensionField"]
    FromValue: Optional["_MeasureField"]
    TargetValue: Optional["_MeasureField"]

    @classmethod
    def _deserialize(
        cls: Type["_MetricComparisonComputation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricComparisonComputation"]:
        if not json_data:
            return None
        return cls(
            ComputationId=json_data.get("ComputationId"),
            Name=json_data.get("Name"),
            Time=DimensionField._deserialize(json_data.get("Time")),
            FromValue=MeasureField._deserialize(json_data.get("FromValue")),
            TargetValue=MeasureField._deserialize(json_data.get("TargetValue")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricComparisonComputation = MetricComparisonComputation


@dataclass
class PeriodOverPeriodComputation(BaseModel):
    ComputationId: Optional[str]
    Name: Optional[str]
    Time: Optional["_DimensionField"]
    Value: Optional["_MeasureField"]

    @classmethod
    def _deserialize(
        cls: Type["_PeriodOverPeriodComputation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PeriodOverPeriodComputation"]:
        if not json_data:
            return None
        return cls(
            ComputationId=json_data.get("ComputationId"),
            Name=json_data.get("Name"),
            Time=DimensionField._deserialize(json_data.get("Time")),
            Value=MeasureField._deserialize(json_data.get("Value")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PeriodOverPeriodComputation = PeriodOverPeriodComputation


@dataclass
class PeriodToDateComputation(BaseModel):
    ComputationId: Optional[str]
    Name: Optional[str]
    Time: Optional["_DimensionField"]
    Value: Optional["_MeasureField"]
    PeriodTimeGranularity: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PeriodToDateComputation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PeriodToDateComputation"]:
        if not json_data:
            return None
        return cls(
            ComputationId=json_data.get("ComputationId"),
            Name=json_data.get("Name"),
            Time=DimensionField._deserialize(json_data.get("Time")),
            Value=MeasureField._deserialize(json_data.get("Value")),
            PeriodTimeGranularity=json_data.get("PeriodTimeGranularity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PeriodToDateComputation = PeriodToDateComputation


@dataclass
class GrowthRateComputation(BaseModel):
    ComputationId: Optional[str]
    Name: Optional[str]
    Time: Optional["_DimensionField"]
    Value: Optional["_MeasureField"]
    PeriodSize: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_GrowthRateComputation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrowthRateComputation"]:
        if not json_data:
            return None
        return cls(
            ComputationId=json_data.get("ComputationId"),
            Name=json_data.get("Name"),
            Time=DimensionField._deserialize(json_data.get("Time")),
            Value=MeasureField._deserialize(json_data.get("Value")),
            PeriodSize=json_data.get("PeriodSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrowthRateComputation = GrowthRateComputation


@dataclass
class UniqueValuesComputation(BaseModel):
    ComputationId: Optional[str]
    Name: Optional[str]
    Category: Optional["_DimensionField"]

    @classmethod
    def _deserialize(
        cls: Type["_UniqueValuesComputation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UniqueValuesComputation"]:
        if not json_data:
            return None
        return cls(
            ComputationId=json_data.get("ComputationId"),
            Name=json_data.get("Name"),
            Category=DimensionField._deserialize(json_data.get("Category")),
        )


# work around possible type aliasing issues when variable has same name as a model
_UniqueValuesComputation = UniqueValuesComputation


@dataclass
class ForecastComputation(BaseModel):
    ComputationId: Optional[str]
    Name: Optional[str]
    Time: Optional["_DimensionField"]
    Value: Optional["_MeasureField"]
    PeriodsForward: Optional[float]
    PeriodsBackward: Optional[float]
    UpperBoundary: Optional[float]
    LowerBoundary: Optional[float]
    PredictionInterval: Optional[float]
    Seasonality: Optional[str]
    CustomSeasonalityValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ForecastComputation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForecastComputation"]:
        if not json_data:
            return None
        return cls(
            ComputationId=json_data.get("ComputationId"),
            Name=json_data.get("Name"),
            Time=DimensionField._deserialize(json_data.get("Time")),
            Value=MeasureField._deserialize(json_data.get("Value")),
            PeriodsForward=json_data.get("PeriodsForward"),
            PeriodsBackward=json_data.get("PeriodsBackward"),
            UpperBoundary=json_data.get("UpperBoundary"),
            LowerBoundary=json_data.get("LowerBoundary"),
            PredictionInterval=json_data.get("PredictionInterval"),
            Seasonality=json_data.get("Seasonality"),
            CustomSeasonalityValue=json_data.get("CustomSeasonalityValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForecastComputation = ForecastComputation


@dataclass
class CustomNarrativeOptions(BaseModel):
    Narrative: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomNarrativeOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomNarrativeOptions"]:
        if not json_data:
            return None
        return cls(
            Narrative=json_data.get("Narrative"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomNarrativeOptions = CustomNarrativeOptions


@dataclass
class SankeyDiagramVisual(BaseModel):
    VisualId: Optional[str]
    Title: Optional["_VisualTitleLabelOptions"]
    Subtitle: Optional["_VisualSubtitleLabelOptions"]
    ChartConfiguration: Optional["_SankeyDiagramChartConfiguration"]
    Actions: Optional[Sequence["_VisualCustomAction"]]

    @classmethod
    def _deserialize(
        cls: Type["_SankeyDiagramVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SankeyDiagramVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            Title=VisualTitleLabelOptions._deserialize(json_data.get("Title")),
            Subtitle=VisualSubtitleLabelOptions._deserialize(json_data.get("Subtitle")),
            ChartConfiguration=SankeyDiagramChartConfiguration._deserialize(json_data.get("ChartConfiguration")),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
        )


# work around possible type aliasing issues when variable has same name as a model
_SankeyDiagramVisual = SankeyDiagramVisual


@dataclass
class SankeyDiagramChartConfiguration(BaseModel):
    FieldWells: Optional["_SankeyDiagramFieldWells"]
    SortConfiguration: Optional["_SankeyDiagramSortConfiguration"]
    DataLabels: Optional["_DataLabelOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_SankeyDiagramChartConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SankeyDiagramChartConfiguration"]:
        if not json_data:
            return None
        return cls(
            FieldWells=SankeyDiagramFieldWells._deserialize(json_data.get("FieldWells")),
            SortConfiguration=SankeyDiagramSortConfiguration._deserialize(json_data.get("SortConfiguration")),
            DataLabels=DataLabelOptions._deserialize(json_data.get("DataLabels")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SankeyDiagramChartConfiguration = SankeyDiagramChartConfiguration


@dataclass
class SankeyDiagramFieldWells(BaseModel):
    SankeyDiagramAggregatedFieldWells: Optional["_SankeyDiagramAggregatedFieldWells"]

    @classmethod
    def _deserialize(
        cls: Type["_SankeyDiagramFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SankeyDiagramFieldWells"]:
        if not json_data:
            return None
        return cls(
            SankeyDiagramAggregatedFieldWells=SankeyDiagramAggregatedFieldWells._deserialize(json_data.get("SankeyDiagramAggregatedFieldWells")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SankeyDiagramFieldWells = SankeyDiagramFieldWells


@dataclass
class SankeyDiagramAggregatedFieldWells(BaseModel):
    Source: Optional[Sequence["_DimensionField"]]
    Destination: Optional[Sequence["_DimensionField"]]
    Weight: Optional[Sequence["_MeasureField"]]

    @classmethod
    def _deserialize(
        cls: Type["_SankeyDiagramAggregatedFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SankeyDiagramAggregatedFieldWells"]:
        if not json_data:
            return None
        return cls(
            Source=deserialize_list(json_data.get("Source"), DimensionField),
            Destination=deserialize_list(json_data.get("Destination"), DimensionField),
            Weight=deserialize_list(json_data.get("Weight"), MeasureField),
        )


# work around possible type aliasing issues when variable has same name as a model
_SankeyDiagramAggregatedFieldWells = SankeyDiagramAggregatedFieldWells


@dataclass
class SankeyDiagramSortConfiguration(BaseModel):
    WeightSort: Optional[Sequence["_FieldSortOptions"]]
    SourceItemsLimit: Optional["_ItemsLimitConfiguration"]
    DestinationItemsLimit: Optional["_ItemsLimitConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_SankeyDiagramSortConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SankeyDiagramSortConfiguration"]:
        if not json_data:
            return None
        return cls(
            WeightSort=deserialize_list(json_data.get("WeightSort"), FieldSortOptions),
            SourceItemsLimit=ItemsLimitConfiguration._deserialize(json_data.get("SourceItemsLimit")),
            DestinationItemsLimit=ItemsLimitConfiguration._deserialize(json_data.get("DestinationItemsLimit")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SankeyDiagramSortConfiguration = SankeyDiagramSortConfiguration


@dataclass
class CustomContentVisual(BaseModel):
    VisualId: Optional[str]
    Title: Optional["_VisualTitleLabelOptions"]
    Subtitle: Optional["_VisualSubtitleLabelOptions"]
    ChartConfiguration: Optional["_CustomContentConfiguration"]
    Actions: Optional[Sequence["_VisualCustomAction"]]
    DataSetIdentifier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomContentVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomContentVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            Title=VisualTitleLabelOptions._deserialize(json_data.get("Title")),
            Subtitle=VisualSubtitleLabelOptions._deserialize(json_data.get("Subtitle")),
            ChartConfiguration=CustomContentConfiguration._deserialize(json_data.get("ChartConfiguration")),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
            DataSetIdentifier=json_data.get("DataSetIdentifier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomContentVisual = CustomContentVisual


@dataclass
class CustomContentConfiguration(BaseModel):
    ContentUrl: Optional[str]
    ContentType: Optional[str]
    ImageScaling: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomContentConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomContentConfiguration"]:
        if not json_data:
            return None
        return cls(
            ContentUrl=json_data.get("ContentUrl"),
            ContentType=json_data.get("ContentType"),
            ImageScaling=json_data.get("ImageScaling"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomContentConfiguration = CustomContentConfiguration


@dataclass
class EmptyVisual(BaseModel):
    VisualId: Optional[str]
    DataSetIdentifier: Optional[str]
    Actions: Optional[Sequence["_VisualCustomAction"]]

    @classmethod
    def _deserialize(
        cls: Type["_EmptyVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmptyVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            DataSetIdentifier=json_data.get("DataSetIdentifier"),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmptyVisual = EmptyVisual


@dataclass
class RadarChartVisual(BaseModel):
    VisualId: Optional[str]
    Title: Optional["_VisualTitleLabelOptions"]
    Subtitle: Optional["_VisualSubtitleLabelOptions"]
    ChartConfiguration: Optional["_RadarChartConfiguration"]
    Actions: Optional[Sequence["_VisualCustomAction"]]
    ColumnHierarchies: Optional[Sequence["_ColumnHierarchy"]]

    @classmethod
    def _deserialize(
        cls: Type["_RadarChartVisual"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RadarChartVisual"]:
        if not json_data:
            return None
        return cls(
            VisualId=json_data.get("VisualId"),
            Title=VisualTitleLabelOptions._deserialize(json_data.get("Title")),
            Subtitle=VisualSubtitleLabelOptions._deserialize(json_data.get("Subtitle")),
            ChartConfiguration=RadarChartConfiguration._deserialize(json_data.get("ChartConfiguration")),
            Actions=deserialize_list(json_data.get("Actions"), VisualCustomAction),
            ColumnHierarchies=deserialize_list(json_data.get("ColumnHierarchies"), ColumnHierarchy),
        )


# work around possible type aliasing issues when variable has same name as a model
_RadarChartVisual = RadarChartVisual


@dataclass
class RadarChartConfiguration(BaseModel):
    FieldWells: Optional["_RadarChartFieldWells"]
    SortConfiguration: Optional["_RadarChartSortConfiguration"]
    Shape: Optional[str]
    BaseSeriesSettings: Optional["_RadarChartSeriesSettings"]
    StartAngle: Optional[float]
    VisualPalette: Optional["_VisualPalette"]
    AlternateBandColorsVisibility: Optional[str]
    AlternateBandEvenColor: Optional[str]
    AlternateBandOddColor: Optional[str]
    CategoryAxis: Optional["_AxisDisplayOptions"]
    CategoryLabelOptions: Optional["_ChartAxisLabelOptions"]
    ColorAxis: Optional["_AxisDisplayOptions"]
    ColorLabelOptions: Optional["_ChartAxisLabelOptions"]
    Legend: Optional["_LegendOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_RadarChartConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RadarChartConfiguration"]:
        if not json_data:
            return None
        return cls(
            FieldWells=RadarChartFieldWells._deserialize(json_data.get("FieldWells")),
            SortConfiguration=RadarChartSortConfiguration._deserialize(json_data.get("SortConfiguration")),
            Shape=json_data.get("Shape"),
            BaseSeriesSettings=RadarChartSeriesSettings._deserialize(json_data.get("BaseSeriesSettings")),
            StartAngle=json_data.get("StartAngle"),
            VisualPalette=VisualPalette._deserialize(json_data.get("VisualPalette")),
            AlternateBandColorsVisibility=json_data.get("AlternateBandColorsVisibility"),
            AlternateBandEvenColor=json_data.get("AlternateBandEvenColor"),
            AlternateBandOddColor=json_data.get("AlternateBandOddColor"),
            CategoryAxis=AxisDisplayOptions._deserialize(json_data.get("CategoryAxis")),
            CategoryLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("CategoryLabelOptions")),
            ColorAxis=AxisDisplayOptions._deserialize(json_data.get("ColorAxis")),
            ColorLabelOptions=ChartAxisLabelOptions._deserialize(json_data.get("ColorLabelOptions")),
            Legend=LegendOptions._deserialize(json_data.get("Legend")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RadarChartConfiguration = RadarChartConfiguration


@dataclass
class RadarChartFieldWells(BaseModel):
    RadarChartAggregatedFieldWells: Optional["_RadarChartAggregatedFieldWells"]

    @classmethod
    def _deserialize(
        cls: Type["_RadarChartFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RadarChartFieldWells"]:
        if not json_data:
            return None
        return cls(
            RadarChartAggregatedFieldWells=RadarChartAggregatedFieldWells._deserialize(json_data.get("RadarChartAggregatedFieldWells")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RadarChartFieldWells = RadarChartFieldWells


@dataclass
class RadarChartAggregatedFieldWells(BaseModel):
    Category: Optional[Sequence["_DimensionField"]]
    Color: Optional[Sequence["_DimensionField"]]
    Values: Optional[Sequence["_MeasureField"]]

    @classmethod
    def _deserialize(
        cls: Type["_RadarChartAggregatedFieldWells"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RadarChartAggregatedFieldWells"]:
        if not json_data:
            return None
        return cls(
            Category=deserialize_list(json_data.get("Category"), DimensionField),
            Color=deserialize_list(json_data.get("Color"), DimensionField),
            Values=deserialize_list(json_data.get("Values"), MeasureField),
        )


# work around possible type aliasing issues when variable has same name as a model
_RadarChartAggregatedFieldWells = RadarChartAggregatedFieldWells


@dataclass
class RadarChartSortConfiguration(BaseModel):
    CategorySort: Optional[Sequence["_FieldSortOptions"]]
    CategoryItemsLimit: Optional["_ItemsLimitConfiguration"]
    ColorSort: Optional[Sequence["_FieldSortOptions"]]
    ColorItemsLimit: Optional["_ItemsLimitConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_RadarChartSortConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RadarChartSortConfiguration"]:
        if not json_data:
            return None
        return cls(
            CategorySort=deserialize_list(json_data.get("CategorySort"), FieldSortOptions),
            CategoryItemsLimit=ItemsLimitConfiguration._deserialize(json_data.get("CategoryItemsLimit")),
            ColorSort=deserialize_list(json_data.get("ColorSort"), FieldSortOptions),
            ColorItemsLimit=ItemsLimitConfiguration._deserialize(json_data.get("ColorItemsLimit")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RadarChartSortConfiguration = RadarChartSortConfiguration


@dataclass
class RadarChartSeriesSettings(BaseModel):
    AreaStyleSettings: Optional["_RadarChartAreaStyleSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_RadarChartSeriesSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RadarChartSeriesSettings"]:
        if not json_data:
            return None
        return cls(
            AreaStyleSettings=RadarChartAreaStyleSettings._deserialize(json_data.get("AreaStyleSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RadarChartSeriesSettings = RadarChartSeriesSettings


@dataclass
class RadarChartAreaStyleSettings(BaseModel):
    Visibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RadarChartAreaStyleSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RadarChartAreaStyleSettings"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RadarChartAreaStyleSettings = RadarChartAreaStyleSettings


@dataclass
class SheetTextBox(BaseModel):
    SheetTextBoxId: Optional[str]
    Content: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SheetTextBox"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SheetTextBox"]:
        if not json_data:
            return None
        return cls(
            SheetTextBoxId=json_data.get("SheetTextBoxId"),
            Content=json_data.get("Content"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SheetTextBox = SheetTextBox


@dataclass
class Layout(BaseModel):
    Configuration: Optional["_LayoutConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_Layout"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Layout"]:
        if not json_data:
            return None
        return cls(
            Configuration=LayoutConfiguration._deserialize(json_data.get("Configuration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Layout = Layout


@dataclass
class LayoutConfiguration(BaseModel):
    GridLayout: Optional["_GridLayoutConfiguration"]
    FreeFormLayout: Optional["_FreeFormLayoutConfiguration"]
    SectionBasedLayout: Optional["_SectionBasedLayoutConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_LayoutConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LayoutConfiguration"]:
        if not json_data:
            return None
        return cls(
            GridLayout=GridLayoutConfiguration._deserialize(json_data.get("GridLayout")),
            FreeFormLayout=FreeFormLayoutConfiguration._deserialize(json_data.get("FreeFormLayout")),
            SectionBasedLayout=SectionBasedLayoutConfiguration._deserialize(json_data.get("SectionBasedLayout")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LayoutConfiguration = LayoutConfiguration


@dataclass
class GridLayoutConfiguration(BaseModel):
    Elements: Optional[Sequence["_GridLayoutElement"]]
    CanvasSizeOptions: Optional["_GridLayoutCanvasSizeOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_GridLayoutConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GridLayoutConfiguration"]:
        if not json_data:
            return None
        return cls(
            Elements=deserialize_list(json_data.get("Elements"), GridLayoutElement),
            CanvasSizeOptions=GridLayoutCanvasSizeOptions._deserialize(json_data.get("CanvasSizeOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GridLayoutConfiguration = GridLayoutConfiguration


@dataclass
class GridLayoutElement(BaseModel):
    ElementId: Optional[str]
    ElementType: Optional[str]
    ColumnIndex: Optional[float]
    ColumnSpan: Optional[float]
    RowIndex: Optional[float]
    RowSpan: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_GridLayoutElement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GridLayoutElement"]:
        if not json_data:
            return None
        return cls(
            ElementId=json_data.get("ElementId"),
            ElementType=json_data.get("ElementType"),
            ColumnIndex=json_data.get("ColumnIndex"),
            ColumnSpan=json_data.get("ColumnSpan"),
            RowIndex=json_data.get("RowIndex"),
            RowSpan=json_data.get("RowSpan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GridLayoutElement = GridLayoutElement


@dataclass
class GridLayoutCanvasSizeOptions(BaseModel):
    ScreenCanvasSizeOptions: Optional["_GridLayoutScreenCanvasSizeOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_GridLayoutCanvasSizeOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GridLayoutCanvasSizeOptions"]:
        if not json_data:
            return None
        return cls(
            ScreenCanvasSizeOptions=GridLayoutScreenCanvasSizeOptions._deserialize(json_data.get("ScreenCanvasSizeOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GridLayoutCanvasSizeOptions = GridLayoutCanvasSizeOptions


@dataclass
class GridLayoutScreenCanvasSizeOptions(BaseModel):
    ResizeOption: Optional[str]
    OptimizedViewPortWidth: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GridLayoutScreenCanvasSizeOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GridLayoutScreenCanvasSizeOptions"]:
        if not json_data:
            return None
        return cls(
            ResizeOption=json_data.get("ResizeOption"),
            OptimizedViewPortWidth=json_data.get("OptimizedViewPortWidth"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GridLayoutScreenCanvasSizeOptions = GridLayoutScreenCanvasSizeOptions


@dataclass
class FreeFormLayoutConfiguration(BaseModel):
    Elements: Optional[Sequence["_FreeFormLayoutElement"]]
    CanvasSizeOptions: Optional["_FreeFormLayoutCanvasSizeOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_FreeFormLayoutConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeFormLayoutConfiguration"]:
        if not json_data:
            return None
        return cls(
            Elements=deserialize_list(json_data.get("Elements"), FreeFormLayoutElement),
            CanvasSizeOptions=FreeFormLayoutCanvasSizeOptions._deserialize(json_data.get("CanvasSizeOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeFormLayoutConfiguration = FreeFormLayoutConfiguration


@dataclass
class FreeFormLayoutElement(BaseModel):
    ElementId: Optional[str]
    ElementType: Optional[str]
    XAxisLocation: Optional[str]
    YAxisLocation: Optional[str]
    Width: Optional[str]
    Height: Optional[str]
    Visibility: Optional[str]
    RenderingRules: Optional[Sequence["_SheetElementRenderingRule"]]
    BorderStyle: Optional["_FreeFormLayoutElementBorderStyle"]
    SelectedBorderStyle: Optional["_FreeFormLayoutElementBorderStyle"]
    BackgroundStyle: Optional["_FreeFormLayoutElementBackgroundStyle"]
    LoadingAnimation: Optional["_LoadingAnimation"]

    @classmethod
    def _deserialize(
        cls: Type["_FreeFormLayoutElement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeFormLayoutElement"]:
        if not json_data:
            return None
        return cls(
            ElementId=json_data.get("ElementId"),
            ElementType=json_data.get("ElementType"),
            XAxisLocation=json_data.get("XAxisLocation"),
            YAxisLocation=json_data.get("YAxisLocation"),
            Width=json_data.get("Width"),
            Height=json_data.get("Height"),
            Visibility=json_data.get("Visibility"),
            RenderingRules=deserialize_list(json_data.get("RenderingRules"), SheetElementRenderingRule),
            BorderStyle=FreeFormLayoutElementBorderStyle._deserialize(json_data.get("BorderStyle")),
            SelectedBorderStyle=FreeFormLayoutElementBorderStyle._deserialize(json_data.get("SelectedBorderStyle")),
            BackgroundStyle=FreeFormLayoutElementBackgroundStyle._deserialize(json_data.get("BackgroundStyle")),
            LoadingAnimation=LoadingAnimation._deserialize(json_data.get("LoadingAnimation")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeFormLayoutElement = FreeFormLayoutElement


@dataclass
class SheetElementRenderingRule(BaseModel):
    Expression: Optional[str]
    ConfigurationOverrides: Optional["_SheetElementConfigurationOverrides"]

    @classmethod
    def _deserialize(
        cls: Type["_SheetElementRenderingRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SheetElementRenderingRule"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            ConfigurationOverrides=SheetElementConfigurationOverrides._deserialize(json_data.get("ConfigurationOverrides")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SheetElementRenderingRule = SheetElementRenderingRule


@dataclass
class SheetElementConfigurationOverrides(BaseModel):
    Visibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SheetElementConfigurationOverrides"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SheetElementConfigurationOverrides"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SheetElementConfigurationOverrides = SheetElementConfigurationOverrides


@dataclass
class FreeFormLayoutElementBorderStyle(BaseModel):
    Visibility: Optional[str]
    Color: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeFormLayoutElementBorderStyle"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeFormLayoutElementBorderStyle"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
            Color=json_data.get("Color"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeFormLayoutElementBorderStyle = FreeFormLayoutElementBorderStyle


@dataclass
class FreeFormLayoutElementBackgroundStyle(BaseModel):
    Visibility: Optional[str]
    Color: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeFormLayoutElementBackgroundStyle"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeFormLayoutElementBackgroundStyle"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
            Color=json_data.get("Color"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeFormLayoutElementBackgroundStyle = FreeFormLayoutElementBackgroundStyle


@dataclass
class LoadingAnimation(BaseModel):
    Visibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoadingAnimation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadingAnimation"]:
        if not json_data:
            return None
        return cls(
            Visibility=json_data.get("Visibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadingAnimation = LoadingAnimation


@dataclass
class FreeFormLayoutCanvasSizeOptions(BaseModel):
    ScreenCanvasSizeOptions: Optional["_FreeFormLayoutScreenCanvasSizeOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_FreeFormLayoutCanvasSizeOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeFormLayoutCanvasSizeOptions"]:
        if not json_data:
            return None
        return cls(
            ScreenCanvasSizeOptions=FreeFormLayoutScreenCanvasSizeOptions._deserialize(json_data.get("ScreenCanvasSizeOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeFormLayoutCanvasSizeOptions = FreeFormLayoutCanvasSizeOptions


@dataclass
class FreeFormLayoutScreenCanvasSizeOptions(BaseModel):
    OptimizedViewPortWidth: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeFormLayoutScreenCanvasSizeOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeFormLayoutScreenCanvasSizeOptions"]:
        if not json_data:
            return None
        return cls(
            OptimizedViewPortWidth=json_data.get("OptimizedViewPortWidth"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeFormLayoutScreenCanvasSizeOptions = FreeFormLayoutScreenCanvasSizeOptions


@dataclass
class SectionBasedLayoutConfiguration(BaseModel):
    HeaderSections: Optional[Sequence["_HeaderFooterSectionConfiguration"]]
    BodySections: Optional[Sequence["_BodySectionConfiguration"]]
    FooterSections: Optional[Sequence["_HeaderFooterSectionConfiguration"]]
    CanvasSizeOptions: Optional["_SectionBasedLayoutCanvasSizeOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_SectionBasedLayoutConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SectionBasedLayoutConfiguration"]:
        if not json_data:
            return None
        return cls(
            HeaderSections=deserialize_list(json_data.get("HeaderSections"), HeaderFooterSectionConfiguration),
            BodySections=deserialize_list(json_data.get("BodySections"), BodySectionConfiguration),
            FooterSections=deserialize_list(json_data.get("FooterSections"), HeaderFooterSectionConfiguration),
            CanvasSizeOptions=SectionBasedLayoutCanvasSizeOptions._deserialize(json_data.get("CanvasSizeOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SectionBasedLayoutConfiguration = SectionBasedLayoutConfiguration


@dataclass
class HeaderFooterSectionConfiguration(BaseModel):
    SectionId: Optional[str]
    Layout: Optional["_SectionLayoutConfiguration"]
    Style: Optional["_SectionStyle"]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderFooterSectionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderFooterSectionConfiguration"]:
        if not json_data:
            return None
        return cls(
            SectionId=json_data.get("SectionId"),
            Layout=SectionLayoutConfiguration._deserialize(json_data.get("Layout")),
            Style=SectionStyle._deserialize(json_data.get("Style")),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderFooterSectionConfiguration = HeaderFooterSectionConfiguration


@dataclass
class SectionLayoutConfiguration(BaseModel):
    FreeFormLayout: Optional["_FreeFormSectionLayoutConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_SectionLayoutConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SectionLayoutConfiguration"]:
        if not json_data:
            return None
        return cls(
            FreeFormLayout=FreeFormSectionLayoutConfiguration._deserialize(json_data.get("FreeFormLayout")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SectionLayoutConfiguration = SectionLayoutConfiguration


@dataclass
class FreeFormSectionLayoutConfiguration(BaseModel):
    Elements: Optional[Sequence["_FreeFormLayoutElement"]]

    @classmethod
    def _deserialize(
        cls: Type["_FreeFormSectionLayoutConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeFormSectionLayoutConfiguration"]:
        if not json_data:
            return None
        return cls(
            Elements=deserialize_list(json_data.get("Elements"), FreeFormLayoutElement),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeFormSectionLayoutConfiguration = FreeFormSectionLayoutConfiguration


@dataclass
class SectionStyle(BaseModel):
    Height: Optional[str]
    Padding: Optional["_Spacing"]

    @classmethod
    def _deserialize(
        cls: Type["_SectionStyle"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SectionStyle"]:
        if not json_data:
            return None
        return cls(
            Height=json_data.get("Height"),
            Padding=Spacing._deserialize(json_data.get("Padding")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SectionStyle = SectionStyle


@dataclass
class Spacing(BaseModel):
    Top: Optional[str]
    Bottom: Optional[str]
    Left: Optional[str]
    Right: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Spacing"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Spacing"]:
        if not json_data:
            return None
        return cls(
            Top=json_data.get("Top"),
            Bottom=json_data.get("Bottom"),
            Left=json_data.get("Left"),
            Right=json_data.get("Right"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Spacing = Spacing


@dataclass
class BodySectionConfiguration(BaseModel):
    SectionId: Optional[str]
    Content: Optional["_BodySectionContent"]
    Style: Optional["_SectionStyle"]
    PageBreakConfiguration: Optional["_SectionPageBreakConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_BodySectionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BodySectionConfiguration"]:
        if not json_data:
            return None
        return cls(
            SectionId=json_data.get("SectionId"),
            Content=BodySectionContent._deserialize(json_data.get("Content")),
            Style=SectionStyle._deserialize(json_data.get("Style")),
            PageBreakConfiguration=SectionPageBreakConfiguration._deserialize(json_data.get("PageBreakConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BodySectionConfiguration = BodySectionConfiguration


@dataclass
class BodySectionContent(BaseModel):
    Layout: Optional["_SectionLayoutConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_BodySectionContent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BodySectionContent"]:
        if not json_data:
            return None
        return cls(
            Layout=SectionLayoutConfiguration._deserialize(json_data.get("Layout")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BodySectionContent = BodySectionContent


@dataclass
class SectionPageBreakConfiguration(BaseModel):
    After: Optional["_SectionAfterPageBreak"]

    @classmethod
    def _deserialize(
        cls: Type["_SectionPageBreakConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SectionPageBreakConfiguration"]:
        if not json_data:
            return None
        return cls(
            After=SectionAfterPageBreak._deserialize(json_data.get("After")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SectionPageBreakConfiguration = SectionPageBreakConfiguration


@dataclass
class SectionAfterPageBreak(BaseModel):
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SectionAfterPageBreak"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SectionAfterPageBreak"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SectionAfterPageBreak = SectionAfterPageBreak


@dataclass
class SectionBasedLayoutCanvasSizeOptions(BaseModel):
    PaperCanvasSizeOptions: Optional["_SectionBasedLayoutPaperCanvasSizeOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_SectionBasedLayoutCanvasSizeOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SectionBasedLayoutCanvasSizeOptions"]:
        if not json_data:
            return None
        return cls(
            PaperCanvasSizeOptions=SectionBasedLayoutPaperCanvasSizeOptions._deserialize(json_data.get("PaperCanvasSizeOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SectionBasedLayoutCanvasSizeOptions = SectionBasedLayoutCanvasSizeOptions


@dataclass
class SectionBasedLayoutPaperCanvasSizeOptions(BaseModel):
    PaperSize: Optional[str]
    PaperOrientation: Optional[str]
    PaperMargin: Optional["_Spacing"]

    @classmethod
    def _deserialize(
        cls: Type["_SectionBasedLayoutPaperCanvasSizeOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SectionBasedLayoutPaperCanvasSizeOptions"]:
        if not json_data:
            return None
        return cls(
            PaperSize=json_data.get("PaperSize"),
            PaperOrientation=json_data.get("PaperOrientation"),
            PaperMargin=Spacing._deserialize(json_data.get("PaperMargin")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SectionBasedLayoutPaperCanvasSizeOptions = SectionBasedLayoutPaperCanvasSizeOptions


@dataclass
class SheetControlLayout(BaseModel):
    Configuration: Optional["_SheetControlLayoutConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_SheetControlLayout"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SheetControlLayout"]:
        if not json_data:
            return None
        return cls(
            Configuration=SheetControlLayoutConfiguration._deserialize(json_data.get("Configuration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SheetControlLayout = SheetControlLayout


@dataclass
class SheetControlLayoutConfiguration(BaseModel):
    GridLayout: Optional["_GridLayoutConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_SheetControlLayoutConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SheetControlLayoutConfiguration"]:
        if not json_data:
            return None
        return cls(
            GridLayout=GridLayoutConfiguration._deserialize(json_data.get("GridLayout")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SheetControlLayoutConfiguration = SheetControlLayoutConfiguration


@dataclass
class CalculatedField(BaseModel):
    DataSetIdentifier: Optional[str]
    Name: Optional[str]
    Expression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CalculatedField"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CalculatedField"]:
        if not json_data:
            return None
        return cls(
            DataSetIdentifier=json_data.get("DataSetIdentifier"),
            Name=json_data.get("Name"),
            Expression=json_data.get("Expression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CalculatedField = CalculatedField


@dataclass
class ParameterDeclaration(BaseModel):
    StringParameterDeclaration: Optional["_StringParameterDeclaration"]
    DecimalParameterDeclaration: Optional["_DecimalParameterDeclaration"]
    IntegerParameterDeclaration: Optional["_IntegerParameterDeclaration"]
    DateTimeParameterDeclaration: Optional["_DateTimeParameterDeclaration"]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterDeclaration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterDeclaration"]:
        if not json_data:
            return None
        return cls(
            StringParameterDeclaration=StringParameterDeclaration._deserialize(json_data.get("StringParameterDeclaration")),
            DecimalParameterDeclaration=DecimalParameterDeclaration._deserialize(json_data.get("DecimalParameterDeclaration")),
            IntegerParameterDeclaration=IntegerParameterDeclaration._deserialize(json_data.get("IntegerParameterDeclaration")),
            DateTimeParameterDeclaration=DateTimeParameterDeclaration._deserialize(json_data.get("DateTimeParameterDeclaration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterDeclaration = ParameterDeclaration


@dataclass
class StringParameterDeclaration(BaseModel):
    ParameterValueType: Optional[str]
    Name: Optional[str]
    DefaultValues: Optional["_StringDefaultValues"]
    ValueWhenUnset: Optional["_StringValueWhenUnsetConfiguration"]
    MappedDataSetParameters: Optional[Sequence["_MappedDataSetParameter"]]

    @classmethod
    def _deserialize(
        cls: Type["_StringParameterDeclaration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringParameterDeclaration"]:
        if not json_data:
            return None
        return cls(
            ParameterValueType=json_data.get("ParameterValueType"),
            Name=json_data.get("Name"),
            DefaultValues=StringDefaultValues._deserialize(json_data.get("DefaultValues")),
            ValueWhenUnset=StringValueWhenUnsetConfiguration._deserialize(json_data.get("ValueWhenUnset")),
            MappedDataSetParameters=deserialize_list(json_data.get("MappedDataSetParameters"), MappedDataSetParameter),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringParameterDeclaration = StringParameterDeclaration


@dataclass
class StringDefaultValues(BaseModel):
    DynamicValue: Optional["_DynamicDefaultValue"]
    StaticValues: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_StringDefaultValues"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringDefaultValues"]:
        if not json_data:
            return None
        return cls(
            DynamicValue=DynamicDefaultValue._deserialize(json_data.get("DynamicValue")),
            StaticValues=json_data.get("StaticValues"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringDefaultValues = StringDefaultValues


@dataclass
class DynamicDefaultValue(BaseModel):
    UserNameColumn: Optional["_ColumnIdentifier"]
    GroupNameColumn: Optional["_ColumnIdentifier"]
    DefaultValueColumn: Optional["_ColumnIdentifier"]

    @classmethod
    def _deserialize(
        cls: Type["_DynamicDefaultValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamicDefaultValue"]:
        if not json_data:
            return None
        return cls(
            UserNameColumn=ColumnIdentifier._deserialize(json_data.get("UserNameColumn")),
            GroupNameColumn=ColumnIdentifier._deserialize(json_data.get("GroupNameColumn")),
            DefaultValueColumn=ColumnIdentifier._deserialize(json_data.get("DefaultValueColumn")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamicDefaultValue = DynamicDefaultValue


@dataclass
class StringValueWhenUnsetConfiguration(BaseModel):
    ValueWhenUnsetOption: Optional[str]
    CustomValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StringValueWhenUnsetConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringValueWhenUnsetConfiguration"]:
        if not json_data:
            return None
        return cls(
            ValueWhenUnsetOption=json_data.get("ValueWhenUnsetOption"),
            CustomValue=json_data.get("CustomValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringValueWhenUnsetConfiguration = StringValueWhenUnsetConfiguration


@dataclass
class MappedDataSetParameter(BaseModel):
    DataSetIdentifier: Optional[str]
    DataSetParameterName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MappedDataSetParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MappedDataSetParameter"]:
        if not json_data:
            return None
        return cls(
            DataSetIdentifier=json_data.get("DataSetIdentifier"),
            DataSetParameterName=json_data.get("DataSetParameterName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MappedDataSetParameter = MappedDataSetParameter


@dataclass
class DecimalParameterDeclaration(BaseModel):
    ParameterValueType: Optional[str]
    Name: Optional[str]
    DefaultValues: Optional["_DecimalDefaultValues"]
    ValueWhenUnset: Optional["_DecimalValueWhenUnsetConfiguration"]
    MappedDataSetParameters: Optional[Sequence["_MappedDataSetParameter"]]

    @classmethod
    def _deserialize(
        cls: Type["_DecimalParameterDeclaration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DecimalParameterDeclaration"]:
        if not json_data:
            return None
        return cls(
            ParameterValueType=json_data.get("ParameterValueType"),
            Name=json_data.get("Name"),
            DefaultValues=DecimalDefaultValues._deserialize(json_data.get("DefaultValues")),
            ValueWhenUnset=DecimalValueWhenUnsetConfiguration._deserialize(json_data.get("ValueWhenUnset")),
            MappedDataSetParameters=deserialize_list(json_data.get("MappedDataSetParameters"), MappedDataSetParameter),
        )


# work around possible type aliasing issues when variable has same name as a model
_DecimalParameterDeclaration = DecimalParameterDeclaration


@dataclass
class DecimalDefaultValues(BaseModel):
    DynamicValue: Optional["_DynamicDefaultValue"]
    StaticValues: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_DecimalDefaultValues"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DecimalDefaultValues"]:
        if not json_data:
            return None
        return cls(
            DynamicValue=DynamicDefaultValue._deserialize(json_data.get("DynamicValue")),
            StaticValues=json_data.get("StaticValues"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DecimalDefaultValues = DecimalDefaultValues


@dataclass
class DecimalValueWhenUnsetConfiguration(BaseModel):
    ValueWhenUnsetOption: Optional[str]
    CustomValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DecimalValueWhenUnsetConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DecimalValueWhenUnsetConfiguration"]:
        if not json_data:
            return None
        return cls(
            ValueWhenUnsetOption=json_data.get("ValueWhenUnsetOption"),
            CustomValue=json_data.get("CustomValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DecimalValueWhenUnsetConfiguration = DecimalValueWhenUnsetConfiguration


@dataclass
class IntegerParameterDeclaration(BaseModel):
    ParameterValueType: Optional[str]
    Name: Optional[str]
    DefaultValues: Optional["_IntegerDefaultValues"]
    ValueWhenUnset: Optional["_IntegerValueWhenUnsetConfiguration"]
    MappedDataSetParameters: Optional[Sequence["_MappedDataSetParameter"]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegerParameterDeclaration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegerParameterDeclaration"]:
        if not json_data:
            return None
        return cls(
            ParameterValueType=json_data.get("ParameterValueType"),
            Name=json_data.get("Name"),
            DefaultValues=IntegerDefaultValues._deserialize(json_data.get("DefaultValues")),
            ValueWhenUnset=IntegerValueWhenUnsetConfiguration._deserialize(json_data.get("ValueWhenUnset")),
            MappedDataSetParameters=deserialize_list(json_data.get("MappedDataSetParameters"), MappedDataSetParameter),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegerParameterDeclaration = IntegerParameterDeclaration


@dataclass
class IntegerDefaultValues(BaseModel):
    DynamicValue: Optional["_DynamicDefaultValue"]
    StaticValues: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_IntegerDefaultValues"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegerDefaultValues"]:
        if not json_data:
            return None
        return cls(
            DynamicValue=DynamicDefaultValue._deserialize(json_data.get("DynamicValue")),
            StaticValues=json_data.get("StaticValues"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegerDefaultValues = IntegerDefaultValues


@dataclass
class IntegerValueWhenUnsetConfiguration(BaseModel):
    ValueWhenUnsetOption: Optional[str]
    CustomValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IntegerValueWhenUnsetConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegerValueWhenUnsetConfiguration"]:
        if not json_data:
            return None
        return cls(
            ValueWhenUnsetOption=json_data.get("ValueWhenUnsetOption"),
            CustomValue=json_data.get("CustomValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegerValueWhenUnsetConfiguration = IntegerValueWhenUnsetConfiguration


@dataclass
class DateTimeParameterDeclaration(BaseModel):
    Name: Optional[str]
    DefaultValues: Optional["_DateTimeDefaultValues"]
    TimeGranularity: Optional[str]
    ValueWhenUnset: Optional["_DateTimeValueWhenUnsetConfiguration"]
    MappedDataSetParameters: Optional[Sequence["_MappedDataSetParameter"]]

    @classmethod
    def _deserialize(
        cls: Type["_DateTimeParameterDeclaration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DateTimeParameterDeclaration"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            DefaultValues=DateTimeDefaultValues._deserialize(json_data.get("DefaultValues")),
            TimeGranularity=json_data.get("TimeGranularity"),
            ValueWhenUnset=DateTimeValueWhenUnsetConfiguration._deserialize(json_data.get("ValueWhenUnset")),
            MappedDataSetParameters=deserialize_list(json_data.get("MappedDataSetParameters"), MappedDataSetParameter),
        )


# work around possible type aliasing issues when variable has same name as a model
_DateTimeParameterDeclaration = DateTimeParameterDeclaration


@dataclass
class DateTimeDefaultValues(BaseModel):
    DynamicValue: Optional["_DynamicDefaultValue"]
    StaticValues: Optional[Sequence[str]]
    RollingDate: Optional["_RollingDateConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_DateTimeDefaultValues"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DateTimeDefaultValues"]:
        if not json_data:
            return None
        return cls(
            DynamicValue=DynamicDefaultValue._deserialize(json_data.get("DynamicValue")),
            StaticValues=json_data.get("StaticValues"),
            RollingDate=RollingDateConfiguration._deserialize(json_data.get("RollingDate")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DateTimeDefaultValues = DateTimeDefaultValues


@dataclass
class RollingDateConfiguration(BaseModel):
    DataSetIdentifier: Optional[str]
    Expression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RollingDateConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RollingDateConfiguration"]:
        if not json_data:
            return None
        return cls(
            DataSetIdentifier=json_data.get("DataSetIdentifier"),
            Expression=json_data.get("Expression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RollingDateConfiguration = RollingDateConfiguration


@dataclass
class DateTimeValueWhenUnsetConfiguration(BaseModel):
    ValueWhenUnsetOption: Optional[str]
    CustomValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DateTimeValueWhenUnsetConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DateTimeValueWhenUnsetConfiguration"]:
        if not json_data:
            return None
        return cls(
            ValueWhenUnsetOption=json_data.get("ValueWhenUnsetOption"),
            CustomValue=json_data.get("CustomValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DateTimeValueWhenUnsetConfiguration = DateTimeValueWhenUnsetConfiguration


@dataclass
class FilterGroup(BaseModel):
    FilterGroupId: Optional[str]
    Filters: Optional[Sequence["_Filter"]]
    ScopeConfiguration: Optional["_FilterScopeConfiguration"]
    Status: Optional[str]
    CrossDataset: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterGroup"]:
        if not json_data:
            return None
        return cls(
            FilterGroupId=json_data.get("FilterGroupId"),
            Filters=deserialize_list(json_data.get("Filters"), Filter),
            ScopeConfiguration=FilterScopeConfiguration._deserialize(json_data.get("ScopeConfiguration")),
            Status=json_data.get("Status"),
            CrossDataset=json_data.get("CrossDataset"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterGroup = FilterGroup


@dataclass
class Filter(BaseModel):
    CategoryFilter: Optional["_CategoryFilter"]
    NumericRangeFilter: Optional["_NumericRangeFilter"]
    NumericEqualityFilter: Optional["_NumericEqualityFilter"]
    TimeEqualityFilter: Optional["_TimeEqualityFilter"]
    TimeRangeFilter: Optional["_TimeRangeFilter"]
    RelativeDatesFilter: Optional["_RelativeDatesFilter"]
    TopBottomFilter: Optional["_TopBottomFilter"]

    @classmethod
    def _deserialize(
        cls: Type["_Filter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filter"]:
        if not json_data:
            return None
        return cls(
            CategoryFilter=CategoryFilter._deserialize(json_data.get("CategoryFilter")),
            NumericRangeFilter=NumericRangeFilter._deserialize(json_data.get("NumericRangeFilter")),
            NumericEqualityFilter=NumericEqualityFilter._deserialize(json_data.get("NumericEqualityFilter")),
            TimeEqualityFilter=TimeEqualityFilter._deserialize(json_data.get("TimeEqualityFilter")),
            TimeRangeFilter=TimeRangeFilter._deserialize(json_data.get("TimeRangeFilter")),
            RelativeDatesFilter=RelativeDatesFilter._deserialize(json_data.get("RelativeDatesFilter")),
            TopBottomFilter=TopBottomFilter._deserialize(json_data.get("TopBottomFilter")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Filter = Filter


@dataclass
class CategoryFilter(BaseModel):
    FilterId: Optional[str]
    Column: Optional["_ColumnIdentifier"]
    Configuration: Optional["_CategoryFilterConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_CategoryFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CategoryFilter"]:
        if not json_data:
            return None
        return cls(
            FilterId=json_data.get("FilterId"),
            Column=ColumnIdentifier._deserialize(json_data.get("Column")),
            Configuration=CategoryFilterConfiguration._deserialize(json_data.get("Configuration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CategoryFilter = CategoryFilter


@dataclass
class CategoryFilterConfiguration(BaseModel):
    FilterListConfiguration: Optional["_FilterListConfiguration"]
    CustomFilterListConfiguration: Optional["_CustomFilterListConfiguration"]
    CustomFilterConfiguration: Optional["_CustomFilterConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_CategoryFilterConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CategoryFilterConfiguration"]:
        if not json_data:
            return None
        return cls(
            FilterListConfiguration=FilterListConfiguration._deserialize(json_data.get("FilterListConfiguration")),
            CustomFilterListConfiguration=CustomFilterListConfiguration._deserialize(json_data.get("CustomFilterListConfiguration")),
            CustomFilterConfiguration=CustomFilterConfiguration._deserialize(json_data.get("CustomFilterConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CategoryFilterConfiguration = CategoryFilterConfiguration


@dataclass
class FilterListConfiguration(BaseModel):
    MatchOperator: Optional[str]
    CategoryValues: Optional[Sequence[str]]
    SelectAllOptions: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterListConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterListConfiguration"]:
        if not json_data:
            return None
        return cls(
            MatchOperator=json_data.get("MatchOperator"),
            CategoryValues=json_data.get("CategoryValues"),
            SelectAllOptions=json_data.get("SelectAllOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterListConfiguration = FilterListConfiguration


@dataclass
class CustomFilterListConfiguration(BaseModel):
    MatchOperator: Optional[str]
    CategoryValues: Optional[Sequence[str]]
    SelectAllOptions: Optional[str]
    NullOption: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomFilterListConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomFilterListConfiguration"]:
        if not json_data:
            return None
        return cls(
            MatchOperator=json_data.get("MatchOperator"),
            CategoryValues=json_data.get("CategoryValues"),
            SelectAllOptions=json_data.get("SelectAllOptions"),
            NullOption=json_data.get("NullOption"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomFilterListConfiguration = CustomFilterListConfiguration


@dataclass
class CustomFilterConfiguration(BaseModel):
    MatchOperator: Optional[str]
    CategoryValue: Optional[str]
    SelectAllOptions: Optional[str]
    ParameterName: Optional[str]
    NullOption: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomFilterConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomFilterConfiguration"]:
        if not json_data:
            return None
        return cls(
            MatchOperator=json_data.get("MatchOperator"),
            CategoryValue=json_data.get("CategoryValue"),
            SelectAllOptions=json_data.get("SelectAllOptions"),
            ParameterName=json_data.get("ParameterName"),
            NullOption=json_data.get("NullOption"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomFilterConfiguration = CustomFilterConfiguration


@dataclass
class NumericRangeFilter(BaseModel):
    FilterId: Optional[str]
    Column: Optional["_ColumnIdentifier"]
    IncludeMinimum: Optional[bool]
    IncludeMaximum: Optional[bool]
    RangeMinimum: Optional["_NumericRangeFilterValue"]
    RangeMaximum: Optional["_NumericRangeFilterValue"]
    SelectAllOptions: Optional[str]
    AggregationFunction: Optional["_AggregationFunction"]
    NullOption: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NumericRangeFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumericRangeFilter"]:
        if not json_data:
            return None
        return cls(
            FilterId=json_data.get("FilterId"),
            Column=ColumnIdentifier._deserialize(json_data.get("Column")),
            IncludeMinimum=json_data.get("IncludeMinimum"),
            IncludeMaximum=json_data.get("IncludeMaximum"),
            RangeMinimum=NumericRangeFilterValue._deserialize(json_data.get("RangeMinimum")),
            RangeMaximum=NumericRangeFilterValue._deserialize(json_data.get("RangeMaximum")),
            SelectAllOptions=json_data.get("SelectAllOptions"),
            AggregationFunction=AggregationFunction._deserialize(json_data.get("AggregationFunction")),
            NullOption=json_data.get("NullOption"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumericRangeFilter = NumericRangeFilter


@dataclass
class NumericRangeFilterValue(BaseModel):
    StaticValue: Optional[float]
    Parameter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NumericRangeFilterValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumericRangeFilterValue"]:
        if not json_data:
            return None
        return cls(
            StaticValue=json_data.get("StaticValue"),
            Parameter=json_data.get("Parameter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumericRangeFilterValue = NumericRangeFilterValue


@dataclass
class NumericEqualityFilter(BaseModel):
    FilterId: Optional[str]
    Column: Optional["_ColumnIdentifier"]
    Value: Optional[float]
    SelectAllOptions: Optional[str]
    MatchOperator: Optional[str]
    AggregationFunction: Optional["_AggregationFunction"]
    ParameterName: Optional[str]
    NullOption: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NumericEqualityFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumericEqualityFilter"]:
        if not json_data:
            return None
        return cls(
            FilterId=json_data.get("FilterId"),
            Column=ColumnIdentifier._deserialize(json_data.get("Column")),
            Value=json_data.get("Value"),
            SelectAllOptions=json_data.get("SelectAllOptions"),
            MatchOperator=json_data.get("MatchOperator"),
            AggregationFunction=AggregationFunction._deserialize(json_data.get("AggregationFunction")),
            ParameterName=json_data.get("ParameterName"),
            NullOption=json_data.get("NullOption"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumericEqualityFilter = NumericEqualityFilter


@dataclass
class TimeEqualityFilter(BaseModel):
    FilterId: Optional[str]
    Column: Optional["_ColumnIdentifier"]
    Value: Optional[str]
    ParameterName: Optional[str]
    TimeGranularity: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeEqualityFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeEqualityFilter"]:
        if not json_data:
            return None
        return cls(
            FilterId=json_data.get("FilterId"),
            Column=ColumnIdentifier._deserialize(json_data.get("Column")),
            Value=json_data.get("Value"),
            ParameterName=json_data.get("ParameterName"),
            TimeGranularity=json_data.get("TimeGranularity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeEqualityFilter = TimeEqualityFilter


@dataclass
class TimeRangeFilter(BaseModel):
    FilterId: Optional[str]
    Column: Optional["_ColumnIdentifier"]
    IncludeMinimum: Optional[bool]
    IncludeMaximum: Optional[bool]
    RangeMinimumValue: Optional["_TimeRangeFilterValue"]
    RangeMaximumValue: Optional["_TimeRangeFilterValue"]
    NullOption: Optional[str]
    ExcludePeriodConfiguration: Optional["_ExcludePeriodConfiguration"]
    TimeGranularity: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeRangeFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeRangeFilter"]:
        if not json_data:
            return None
        return cls(
            FilterId=json_data.get("FilterId"),
            Column=ColumnIdentifier._deserialize(json_data.get("Column")),
            IncludeMinimum=json_data.get("IncludeMinimum"),
            IncludeMaximum=json_data.get("IncludeMaximum"),
            RangeMinimumValue=TimeRangeFilterValue._deserialize(json_data.get("RangeMinimumValue")),
            RangeMaximumValue=TimeRangeFilterValue._deserialize(json_data.get("RangeMaximumValue")),
            NullOption=json_data.get("NullOption"),
            ExcludePeriodConfiguration=ExcludePeriodConfiguration._deserialize(json_data.get("ExcludePeriodConfiguration")),
            TimeGranularity=json_data.get("TimeGranularity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeRangeFilter = TimeRangeFilter


@dataclass
class TimeRangeFilterValue(BaseModel):
    StaticValue: Optional[str]
    RollingDate: Optional["_RollingDateConfiguration"]
    Parameter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeRangeFilterValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeRangeFilterValue"]:
        if not json_data:
            return None
        return cls(
            StaticValue=json_data.get("StaticValue"),
            RollingDate=RollingDateConfiguration._deserialize(json_data.get("RollingDate")),
            Parameter=json_data.get("Parameter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeRangeFilterValue = TimeRangeFilterValue


@dataclass
class ExcludePeriodConfiguration(BaseModel):
    Amount: Optional[float]
    Granularity: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExcludePeriodConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExcludePeriodConfiguration"]:
        if not json_data:
            return None
        return cls(
            Amount=json_data.get("Amount"),
            Granularity=json_data.get("Granularity"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExcludePeriodConfiguration = ExcludePeriodConfiguration


@dataclass
class RelativeDatesFilter(BaseModel):
    FilterId: Optional[str]
    Column: Optional["_ColumnIdentifier"]
    AnchorDateConfiguration: Optional["_AnchorDateConfiguration"]
    MinimumGranularity: Optional[str]
    TimeGranularity: Optional[str]
    RelativeDateType: Optional[str]
    RelativeDateValue: Optional[float]
    ParameterName: Optional[str]
    NullOption: Optional[str]
    ExcludePeriodConfiguration: Optional["_ExcludePeriodConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_RelativeDatesFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelativeDatesFilter"]:
        if not json_data:
            return None
        return cls(
            FilterId=json_data.get("FilterId"),
            Column=ColumnIdentifier._deserialize(json_data.get("Column")),
            AnchorDateConfiguration=AnchorDateConfiguration._deserialize(json_data.get("AnchorDateConfiguration")),
            MinimumGranularity=json_data.get("MinimumGranularity"),
            TimeGranularity=json_data.get("TimeGranularity"),
            RelativeDateType=json_data.get("RelativeDateType"),
            RelativeDateValue=json_data.get("RelativeDateValue"),
            ParameterName=json_data.get("ParameterName"),
            NullOption=json_data.get("NullOption"),
            ExcludePeriodConfiguration=ExcludePeriodConfiguration._deserialize(json_data.get("ExcludePeriodConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelativeDatesFilter = RelativeDatesFilter


@dataclass
class AnchorDateConfiguration(BaseModel):
    AnchorOption: Optional[str]
    ParameterName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnchorDateConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnchorDateConfiguration"]:
        if not json_data:
            return None
        return cls(
            AnchorOption=json_data.get("AnchorOption"),
            ParameterName=json_data.get("ParameterName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnchorDateConfiguration = AnchorDateConfiguration


@dataclass
class TopBottomFilter(BaseModel):
    FilterId: Optional[str]
    Column: Optional["_ColumnIdentifier"]
    Limit: Optional[float]
    AggregationSortConfigurations: Optional[Sequence["_AggregationSortConfiguration"]]
    TimeGranularity: Optional[str]
    ParameterName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TopBottomFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TopBottomFilter"]:
        if not json_data:
            return None
        return cls(
            FilterId=json_data.get("FilterId"),
            Column=ColumnIdentifier._deserialize(json_data.get("Column")),
            Limit=json_data.get("Limit"),
            AggregationSortConfigurations=deserialize_list(json_data.get("AggregationSortConfigurations"), AggregationSortConfiguration),
            TimeGranularity=json_data.get("TimeGranularity"),
            ParameterName=json_data.get("ParameterName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TopBottomFilter = TopBottomFilter


@dataclass
class AggregationSortConfiguration(BaseModel):
    Column: Optional["_ColumnIdentifier"]
    SortDirection: Optional[str]
    AggregationFunction: Optional["_AggregationFunction"]

    @classmethod
    def _deserialize(
        cls: Type["_AggregationSortConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AggregationSortConfiguration"]:
        if not json_data:
            return None
        return cls(
            Column=ColumnIdentifier._deserialize(json_data.get("Column")),
            SortDirection=json_data.get("SortDirection"),
            AggregationFunction=AggregationFunction._deserialize(json_data.get("AggregationFunction")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AggregationSortConfiguration = AggregationSortConfiguration


@dataclass
class FilterScopeConfiguration(BaseModel):
    SelectedSheets: Optional["_SelectedSheetsFilterScopeConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_FilterScopeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterScopeConfiguration"]:
        if not json_data:
            return None
        return cls(
            SelectedSheets=SelectedSheetsFilterScopeConfiguration._deserialize(json_data.get("SelectedSheets")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterScopeConfiguration = FilterScopeConfiguration


@dataclass
class SelectedSheetsFilterScopeConfiguration(BaseModel):
    SheetVisualScopingConfigurations: Optional[Sequence["_SheetVisualScopingConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_SelectedSheetsFilterScopeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelectedSheetsFilterScopeConfiguration"]:
        if not json_data:
            return None
        return cls(
            SheetVisualScopingConfigurations=deserialize_list(json_data.get("SheetVisualScopingConfigurations"), SheetVisualScopingConfiguration),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelectedSheetsFilterScopeConfiguration = SelectedSheetsFilterScopeConfiguration


@dataclass
class SheetVisualScopingConfiguration(BaseModel):
    SheetId: Optional[str]
    Scope: Optional[str]
    VisualIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SheetVisualScopingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SheetVisualScopingConfiguration"]:
        if not json_data:
            return None
        return cls(
            SheetId=json_data.get("SheetId"),
            Scope=json_data.get("Scope"),
            VisualIds=json_data.get("VisualIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SheetVisualScopingConfiguration = SheetVisualScopingConfiguration


@dataclass
class ColumnConfiguration(BaseModel):
    Column: Optional["_ColumnIdentifier"]
    FormatConfiguration: Optional["_FormatConfiguration"]
    Role: Optional[str]
    ColorsConfiguration: Optional["_ColorsConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnConfiguration"]:
        if not json_data:
            return None
        return cls(
            Column=ColumnIdentifier._deserialize(json_data.get("Column")),
            FormatConfiguration=FormatConfiguration._deserialize(json_data.get("FormatConfiguration")),
            Role=json_data.get("Role"),
            ColorsConfiguration=ColorsConfiguration._deserialize(json_data.get("ColorsConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnConfiguration = ColumnConfiguration


@dataclass
class ColorsConfiguration(BaseModel):
    CustomColors: Optional[Sequence["_CustomColor"]]

    @classmethod
    def _deserialize(
        cls: Type["_ColorsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColorsConfiguration"]:
        if not json_data:
            return None
        return cls(
            CustomColors=deserialize_list(json_data.get("CustomColors"), CustomColor),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColorsConfiguration = ColorsConfiguration


@dataclass
class CustomColor(BaseModel):
    FieldValue: Optional[str]
    Color: Optional[str]
    SpecialValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomColor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomColor"]:
        if not json_data:
            return None
        return cls(
            FieldValue=json_data.get("FieldValue"),
            Color=json_data.get("Color"),
            SpecialValue=json_data.get("SpecialValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomColor = CustomColor


@dataclass
class AnalysisDefaults(BaseModel):
    DefaultNewSheetConfiguration: Optional["_DefaultNewSheetConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AnalysisDefaults"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnalysisDefaults"]:
        if not json_data:
            return None
        return cls(
            DefaultNewSheetConfiguration=DefaultNewSheetConfiguration._deserialize(json_data.get("DefaultNewSheetConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnalysisDefaults = AnalysisDefaults


@dataclass
class DefaultNewSheetConfiguration(BaseModel):
    InteractiveLayoutConfiguration: Optional["_DefaultInteractiveLayoutConfiguration"]
    PaginatedLayoutConfiguration: Optional["_DefaultPaginatedLayoutConfiguration"]
    SheetContentType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultNewSheetConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultNewSheetConfiguration"]:
        if not json_data:
            return None
        return cls(
            InteractiveLayoutConfiguration=DefaultInteractiveLayoutConfiguration._deserialize(json_data.get("InteractiveLayoutConfiguration")),
            PaginatedLayoutConfiguration=DefaultPaginatedLayoutConfiguration._deserialize(json_data.get("PaginatedLayoutConfiguration")),
            SheetContentType=json_data.get("SheetContentType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultNewSheetConfiguration = DefaultNewSheetConfiguration


@dataclass
class DefaultInteractiveLayoutConfiguration(BaseModel):
    Grid: Optional["_DefaultGridLayoutConfiguration"]
    FreeForm: Optional["_DefaultFreeFormLayoutConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultInteractiveLayoutConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultInteractiveLayoutConfiguration"]:
        if not json_data:
            return None
        return cls(
            Grid=DefaultGridLayoutConfiguration._deserialize(json_data.get("Grid")),
            FreeForm=DefaultFreeFormLayoutConfiguration._deserialize(json_data.get("FreeForm")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultInteractiveLayoutConfiguration = DefaultInteractiveLayoutConfiguration


@dataclass
class DefaultGridLayoutConfiguration(BaseModel):
    CanvasSizeOptions: Optional["_GridLayoutCanvasSizeOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultGridLayoutConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultGridLayoutConfiguration"]:
        if not json_data:
            return None
        return cls(
            CanvasSizeOptions=GridLayoutCanvasSizeOptions._deserialize(json_data.get("CanvasSizeOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultGridLayoutConfiguration = DefaultGridLayoutConfiguration


@dataclass
class DefaultFreeFormLayoutConfiguration(BaseModel):
    CanvasSizeOptions: Optional["_FreeFormLayoutCanvasSizeOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultFreeFormLayoutConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultFreeFormLayoutConfiguration"]:
        if not json_data:
            return None
        return cls(
            CanvasSizeOptions=FreeFormLayoutCanvasSizeOptions._deserialize(json_data.get("CanvasSizeOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultFreeFormLayoutConfiguration = DefaultFreeFormLayoutConfiguration


@dataclass
class DefaultPaginatedLayoutConfiguration(BaseModel):
    SectionBased: Optional["_DefaultSectionBasedLayoutConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultPaginatedLayoutConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultPaginatedLayoutConfiguration"]:
        if not json_data:
            return None
        return cls(
            SectionBased=DefaultSectionBasedLayoutConfiguration._deserialize(json_data.get("SectionBased")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultPaginatedLayoutConfiguration = DefaultPaginatedLayoutConfiguration


@dataclass
class DefaultSectionBasedLayoutConfiguration(BaseModel):
    CanvasSizeOptions: Optional["_SectionBasedLayoutCanvasSizeOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultSectionBasedLayoutConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultSectionBasedLayoutConfiguration"]:
        if not json_data:
            return None
        return cls(
            CanvasSizeOptions=SectionBasedLayoutCanvasSizeOptions._deserialize(json_data.get("CanvasSizeOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultSectionBasedLayoutConfiguration = DefaultSectionBasedLayoutConfiguration


@dataclass
class ResourcePermission(BaseModel):
    Principal: Optional[str]
    Resource: Optional[str]
    Actions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourcePermission"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourcePermission"]:
        if not json_data:
            return None
        return cls(
            Principal=json_data.get("Principal"),
            Resource=json_data.get("Resource"),
            Actions=json_data.get("Actions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourcePermission = ResourcePermission


@dataclass
class TemplateSourceEntity(BaseModel):
    SourceAnalysis: Optional["_TemplateSourceAnalysis"]
    SourceTemplate: Optional["_TemplateSourceTemplate"]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateSourceEntity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateSourceEntity"]:
        if not json_data:
            return None
        return cls(
            SourceAnalysis=TemplateSourceAnalysis._deserialize(json_data.get("SourceAnalysis")),
            SourceTemplate=TemplateSourceTemplate._deserialize(json_data.get("SourceTemplate")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateSourceEntity = TemplateSourceEntity


@dataclass
class TemplateSourceAnalysis(BaseModel):
    Arn: Optional[str]
    DataSetReferences: Optional[Sequence["_DataSetReference"]]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateSourceAnalysis"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateSourceAnalysis"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            DataSetReferences=deserialize_list(json_data.get("DataSetReferences"), DataSetReference),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateSourceAnalysis = TemplateSourceAnalysis


@dataclass
class DataSetReference(BaseModel):
    DataSetPlaceholder: Optional[str]
    DataSetArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataSetReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataSetReference"]:
        if not json_data:
            return None
        return cls(
            DataSetPlaceholder=json_data.get("DataSetPlaceholder"),
            DataSetArn=json_data.get("DataSetArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataSetReference = DataSetReference


@dataclass
class TemplateSourceTemplate(BaseModel):
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateSourceTemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateSourceTemplate"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateSourceTemplate = TemplateSourceTemplate


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


@dataclass
class TemplateVersion(BaseModel):
    CreatedTime: Optional[str]
    Errors: Optional[Sequence["_TemplateError"]]
    VersionNumber: Optional[float]
    Status: Optional[str]
    DataSetConfigurations: Optional[Sequence["_DataSetConfiguration"]]
    Description: Optional[str]
    SourceEntityArn: Optional[str]
    ThemeArn: Optional[str]
    Sheets: Optional[Sequence["_Sheet"]]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateVersion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateVersion"]:
        if not json_data:
            return None
        return cls(
            CreatedTime=json_data.get("CreatedTime"),
            Errors=deserialize_list(json_data.get("Errors"), TemplateError),
            VersionNumber=json_data.get("VersionNumber"),
            Status=json_data.get("Status"),
            DataSetConfigurations=deserialize_list(json_data.get("DataSetConfigurations"), DataSetConfiguration),
            Description=json_data.get("Description"),
            SourceEntityArn=json_data.get("SourceEntityArn"),
            ThemeArn=json_data.get("ThemeArn"),
            Sheets=deserialize_list(json_data.get("Sheets"), Sheet),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateVersion = TemplateVersion


@dataclass
class TemplateError(BaseModel):
    Type: Optional[str]
    Message: Optional[str]
    ViolatedEntities: Optional[Sequence["_Entity"]]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateError"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateError"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Message=json_data.get("Message"),
            ViolatedEntities=deserialize_list(json_data.get("ViolatedEntities"), Entity),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateError = TemplateError


@dataclass
class Entity(BaseModel):
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Entity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Entity"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Entity = Entity


@dataclass
class Sheet(BaseModel):
    SheetId: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Sheet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sheet"]:
        if not json_data:
            return None
        return cls(
            SheetId=json_data.get("SheetId"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sheet = Sheet


