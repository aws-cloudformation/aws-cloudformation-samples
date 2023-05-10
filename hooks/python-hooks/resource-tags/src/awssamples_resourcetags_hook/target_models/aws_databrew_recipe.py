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
class AwsDatabrewRecipe(BaseModel):
    Description: Optional[str]
    Name: Optional[str]
    Steps: Optional[Sequence["_RecipeStep"]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDatabrewRecipe"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDatabrewRecipe"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Steps=deserialize_list(json_data.get("Steps"), RecipeStep),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDatabrewRecipe = AwsDatabrewRecipe


@dataclass
class RecipeStep(BaseModel):
    Action: Optional["_Action"]
    ConditionExpressions: Optional[Sequence["_ConditionExpression"]]

    @classmethod
    def _deserialize(
        cls: Type["_RecipeStep"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecipeStep"]:
        if not json_data:
            return None
        return cls(
            Action=Action._deserialize(json_data.get("Action")),
            ConditionExpressions=deserialize_list(json_data.get("ConditionExpressions"), ConditionExpression),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecipeStep = RecipeStep


@dataclass
class Action(BaseModel):
    Operation: Optional[str]
    Parameters: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            Operation=json_data.get("Operation"),
            Parameters=json_data.get("Parameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class RecipeParameters(BaseModel):
    AggregateFunction: Optional[str]
    Base: Optional[str]
    CaseStatement: Optional[str]
    CategoryMap: Optional[str]
    CharsToRemove: Optional[str]
    CollapseConsecutiveWhitespace: Optional[str]
    ColumnDataType: Optional[str]
    ColumnRange: Optional[str]
    Count: Optional[str]
    CustomCharacters: Optional[str]
    CustomStopWords: Optional[str]
    CustomValue: Optional[str]
    DatasetsColumns: Optional[str]
    DateAddValue: Optional[str]
    DateTimeFormat: Optional[str]
    DateTimeParameters: Optional[str]
    DeleteOtherRows: Optional[str]
    Delimiter: Optional[str]
    EndPattern: Optional[str]
    EndPosition: Optional[str]
    EndValue: Optional[str]
    ExpandContractions: Optional[str]
    Exponent: Optional[str]
    FalseString: Optional[str]
    GroupByAggFunctionOptions: Optional[str]
    GroupByColumns: Optional[str]
    HiddenColumns: Optional[str]
    IgnoreCase: Optional[str]
    IncludeInSplit: Optional[str]
    Interval: Optional[str]
    IsText: Optional[str]
    JoinKeys: Optional[str]
    JoinType: Optional[str]
    LeftColumns: Optional[str]
    Limit: Optional[str]
    LowerBound: Optional[str]
    MapType: Optional[str]
    ModeType: Optional[str]
    MultiLine: Optional[bool]
    NumRows: Optional[str]
    NumRowsAfter: Optional[str]
    NumRowsBefore: Optional[str]
    OrderByColumn: Optional[str]
    OrderByColumns: Optional[str]
    Other: Optional[str]
    Pattern: Optional[str]
    PatternOption1: Optional[str]
    PatternOption2: Optional[str]
    PatternOptions: Optional[str]
    Period: Optional[str]
    Position: Optional[str]
    RemoveAllPunctuation: Optional[str]
    RemoveAllQuotes: Optional[str]
    RemoveAllWhitespace: Optional[str]
    RemoveCustomCharacters: Optional[str]
    RemoveCustomValue: Optional[str]
    RemoveLeadingAndTrailingPunctuation: Optional[str]
    RemoveLeadingAndTrailingQuotes: Optional[str]
    RemoveLeadingAndTrailingWhitespace: Optional[str]
    RemoveLetters: Optional[str]
    RemoveNumbers: Optional[str]
    RemoveSourceColumn: Optional[str]
    RemoveSpecialCharacters: Optional[str]
    RightColumns: Optional[str]
    SampleSize: Optional[str]
    SampleType: Optional[str]
    SecondInput: Optional[str]
    SecondaryInputs: Optional[Sequence["_SecondaryInput"]]
    SourceColumn: Optional[str]
    SourceColumn1: Optional[str]
    SourceColumn2: Optional[str]
    SourceColumns: Optional[str]
    StartColumnIndex: Optional[str]
    StartPattern: Optional[str]
    StartPosition: Optional[str]
    StartValue: Optional[str]
    StemmingMode: Optional[str]
    StepCount: Optional[str]
    StepIndex: Optional[str]
    StopWordsMode: Optional[str]
    Strategy: Optional[str]
    SheetNames: Optional[Sequence[str]]
    SheetIndexes: Optional[Sequence[int]]
    TargetColumn: Optional[str]
    TargetColumnNames: Optional[str]
    TargetDateFormat: Optional[str]
    TargetIndex: Optional[str]
    TimeZone: Optional[str]
    TokenizerPattern: Optional[str]
    TrueString: Optional[str]
    UdfLang: Optional[str]
    Units: Optional[str]
    UnpivotColumn: Optional[str]
    UpperBound: Optional[str]
    UseNewDataFrame: Optional[str]
    Value: Optional[str]
    Value1: Optional[str]
    Value2: Optional[str]
    ValueColumn: Optional[str]
    ViewFrame: Optional[str]
    Input: Optional["_Input"]

    @classmethod
    def _deserialize(
        cls: Type["_RecipeParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecipeParameters"]:
        if not json_data:
            return None
        return cls(
            AggregateFunction=json_data.get("AggregateFunction"),
            Base=json_data.get("Base"),
            CaseStatement=json_data.get("CaseStatement"),
            CategoryMap=json_data.get("CategoryMap"),
            CharsToRemove=json_data.get("CharsToRemove"),
            CollapseConsecutiveWhitespace=json_data.get("CollapseConsecutiveWhitespace"),
            ColumnDataType=json_data.get("ColumnDataType"),
            ColumnRange=json_data.get("ColumnRange"),
            Count=json_data.get("Count"),
            CustomCharacters=json_data.get("CustomCharacters"),
            CustomStopWords=json_data.get("CustomStopWords"),
            CustomValue=json_data.get("CustomValue"),
            DatasetsColumns=json_data.get("DatasetsColumns"),
            DateAddValue=json_data.get("DateAddValue"),
            DateTimeFormat=json_data.get("DateTimeFormat"),
            DateTimeParameters=json_data.get("DateTimeParameters"),
            DeleteOtherRows=json_data.get("DeleteOtherRows"),
            Delimiter=json_data.get("Delimiter"),
            EndPattern=json_data.get("EndPattern"),
            EndPosition=json_data.get("EndPosition"),
            EndValue=json_data.get("EndValue"),
            ExpandContractions=json_data.get("ExpandContractions"),
            Exponent=json_data.get("Exponent"),
            FalseString=json_data.get("FalseString"),
            GroupByAggFunctionOptions=json_data.get("GroupByAggFunctionOptions"),
            GroupByColumns=json_data.get("GroupByColumns"),
            HiddenColumns=json_data.get("HiddenColumns"),
            IgnoreCase=json_data.get("IgnoreCase"),
            IncludeInSplit=json_data.get("IncludeInSplit"),
            Interval=json_data.get("Interval"),
            IsText=json_data.get("IsText"),
            JoinKeys=json_data.get("JoinKeys"),
            JoinType=json_data.get("JoinType"),
            LeftColumns=json_data.get("LeftColumns"),
            Limit=json_data.get("Limit"),
            LowerBound=json_data.get("LowerBound"),
            MapType=json_data.get("MapType"),
            ModeType=json_data.get("ModeType"),
            MultiLine=json_data.get("MultiLine"),
            NumRows=json_data.get("NumRows"),
            NumRowsAfter=json_data.get("NumRowsAfter"),
            NumRowsBefore=json_data.get("NumRowsBefore"),
            OrderByColumn=json_data.get("OrderByColumn"),
            OrderByColumns=json_data.get("OrderByColumns"),
            Other=json_data.get("Other"),
            Pattern=json_data.get("Pattern"),
            PatternOption1=json_data.get("PatternOption1"),
            PatternOption2=json_data.get("PatternOption2"),
            PatternOptions=json_data.get("PatternOptions"),
            Period=json_data.get("Period"),
            Position=json_data.get("Position"),
            RemoveAllPunctuation=json_data.get("RemoveAllPunctuation"),
            RemoveAllQuotes=json_data.get("RemoveAllQuotes"),
            RemoveAllWhitespace=json_data.get("RemoveAllWhitespace"),
            RemoveCustomCharacters=json_data.get("RemoveCustomCharacters"),
            RemoveCustomValue=json_data.get("RemoveCustomValue"),
            RemoveLeadingAndTrailingPunctuation=json_data.get("RemoveLeadingAndTrailingPunctuation"),
            RemoveLeadingAndTrailingQuotes=json_data.get("RemoveLeadingAndTrailingQuotes"),
            RemoveLeadingAndTrailingWhitespace=json_data.get("RemoveLeadingAndTrailingWhitespace"),
            RemoveLetters=json_data.get("RemoveLetters"),
            RemoveNumbers=json_data.get("RemoveNumbers"),
            RemoveSourceColumn=json_data.get("RemoveSourceColumn"),
            RemoveSpecialCharacters=json_data.get("RemoveSpecialCharacters"),
            RightColumns=json_data.get("RightColumns"),
            SampleSize=json_data.get("SampleSize"),
            SampleType=json_data.get("SampleType"),
            SecondInput=json_data.get("SecondInput"),
            SecondaryInputs=deserialize_list(json_data.get("SecondaryInputs"), SecondaryInput),
            SourceColumn=json_data.get("SourceColumn"),
            SourceColumn1=json_data.get("SourceColumn1"),
            SourceColumn2=json_data.get("SourceColumn2"),
            SourceColumns=json_data.get("SourceColumns"),
            StartColumnIndex=json_data.get("StartColumnIndex"),
            StartPattern=json_data.get("StartPattern"),
            StartPosition=json_data.get("StartPosition"),
            StartValue=json_data.get("StartValue"),
            StemmingMode=json_data.get("StemmingMode"),
            StepCount=json_data.get("StepCount"),
            StepIndex=json_data.get("StepIndex"),
            StopWordsMode=json_data.get("StopWordsMode"),
            Strategy=json_data.get("Strategy"),
            SheetNames=json_data.get("SheetNames"),
            SheetIndexes=json_data.get("SheetIndexes"),
            TargetColumn=json_data.get("TargetColumn"),
            TargetColumnNames=json_data.get("TargetColumnNames"),
            TargetDateFormat=json_data.get("TargetDateFormat"),
            TargetIndex=json_data.get("TargetIndex"),
            TimeZone=json_data.get("TimeZone"),
            TokenizerPattern=json_data.get("TokenizerPattern"),
            TrueString=json_data.get("TrueString"),
            UdfLang=json_data.get("UdfLang"),
            Units=json_data.get("Units"),
            UnpivotColumn=json_data.get("UnpivotColumn"),
            UpperBound=json_data.get("UpperBound"),
            UseNewDataFrame=json_data.get("UseNewDataFrame"),
            Value=json_data.get("Value"),
            Value1=json_data.get("Value1"),
            Value2=json_data.get("Value2"),
            ValueColumn=json_data.get("ValueColumn"),
            ViewFrame=json_data.get("ViewFrame"),
            Input=Input._deserialize(json_data.get("Input")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecipeParameters = RecipeParameters


@dataclass
class SecondaryInput(BaseModel):
    S3InputDefinition: Optional["_S3Location"]
    DataCatalogInputDefinition: Optional["_DataCatalogInputDefinition"]

    @classmethod
    def _deserialize(
        cls: Type["_SecondaryInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondaryInput"]:
        if not json_data:
            return None
        return cls(
            S3InputDefinition=S3Location._deserialize(json_data.get("S3InputDefinition")),
            DataCatalogInputDefinition=DataCatalogInputDefinition._deserialize(json_data.get("DataCatalogInputDefinition")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecondaryInput = SecondaryInput


@dataclass
class S3Location(BaseModel):
    Bucket: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Location"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Location"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Location = S3Location


@dataclass
class DataCatalogInputDefinition(BaseModel):
    CatalogId: Optional[str]
    DatabaseName: Optional[str]
    TableName: Optional[str]
    TempDirectory: Optional["_S3Location"]

    @classmethod
    def _deserialize(
        cls: Type["_DataCatalogInputDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataCatalogInputDefinition"]:
        if not json_data:
            return None
        return cls(
            CatalogId=json_data.get("CatalogId"),
            DatabaseName=json_data.get("DatabaseName"),
            TableName=json_data.get("TableName"),
            TempDirectory=S3Location._deserialize(json_data.get("TempDirectory")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataCatalogInputDefinition = DataCatalogInputDefinition


@dataclass
class Input(BaseModel):
    S3InputDefinition: Optional["_S3Location"]
    DataCatalogInputDefinition: Optional["_DataCatalogInputDefinition"]

    @classmethod
    def _deserialize(
        cls: Type["_Input"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Input"]:
        if not json_data:
            return None
        return cls(
            S3InputDefinition=S3Location._deserialize(json_data.get("S3InputDefinition")),
            DataCatalogInputDefinition=DataCatalogInputDefinition._deserialize(json_data.get("DataCatalogInputDefinition")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Input = Input


@dataclass
class ConditionExpression(BaseModel):
    Condition: Optional[str]
    Value: Optional[str]
    TargetColumn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConditionExpression"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConditionExpression"]:
        if not json_data:
            return None
        return cls(
            Condition=json_data.get("Condition"),
            Value=json_data.get("Value"),
            TargetColumn=json_data.get("TargetColumn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConditionExpression = ConditionExpression


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


