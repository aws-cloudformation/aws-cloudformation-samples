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
class AwsDatabrewDataset(BaseModel):
    Name: Optional[str]
    Format: Optional[str]
    FormatOptions: Optional["_FormatOptions"]
    Input: Optional["_Input"]
    PathOptions: Optional["_PathOptions"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDatabrewDataset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDatabrewDataset"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Format=json_data.get("Format"),
            FormatOptions=FormatOptions._deserialize(json_data.get("FormatOptions")),
            Input=Input._deserialize(json_data.get("Input")),
            PathOptions=PathOptions._deserialize(json_data.get("PathOptions")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDatabrewDataset = AwsDatabrewDataset


@dataclass
class FormatOptions(BaseModel):
    Json: Optional["_JsonOptions"]
    Excel: Optional["_ExcelOptions"]
    Csv: Optional["_CsvOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_FormatOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FormatOptions"]:
        if not json_data:
            return None
        return cls(
            Json=JsonOptions._deserialize(json_data.get("Json")),
            Excel=ExcelOptions._deserialize(json_data.get("Excel")),
            Csv=CsvOptions._deserialize(json_data.get("Csv")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FormatOptions = FormatOptions


@dataclass
class JsonOptions(BaseModel):
    MultiLine: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_JsonOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JsonOptions"]:
        if not json_data:
            return None
        return cls(
            MultiLine=json_data.get("MultiLine"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JsonOptions = JsonOptions


@dataclass
class ExcelOptions(BaseModel):
    SheetNames: Optional[Sequence[str]]
    SheetIndexes: Optional[Sequence[int]]
    HeaderRow: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ExcelOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExcelOptions"]:
        if not json_data:
            return None
        return cls(
            SheetNames=json_data.get("SheetNames"),
            SheetIndexes=json_data.get("SheetIndexes"),
            HeaderRow=json_data.get("HeaderRow"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExcelOptions = ExcelOptions


@dataclass
class CsvOptions(BaseModel):
    Delimiter: Optional[str]
    HeaderRow: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CsvOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CsvOptions"]:
        if not json_data:
            return None
        return cls(
            Delimiter=json_data.get("Delimiter"),
            HeaderRow=json_data.get("HeaderRow"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CsvOptions = CsvOptions


@dataclass
class Input(BaseModel):
    S3InputDefinition: Optional["_S3Location"]
    DataCatalogInputDefinition: Optional["_DataCatalogInputDefinition"]
    DatabaseInputDefinition: Optional["_DatabaseInputDefinition"]
    Metadata: Optional["_Metadata"]

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
            DatabaseInputDefinition=DatabaseInputDefinition._deserialize(json_data.get("DatabaseInputDefinition")),
            Metadata=Metadata._deserialize(json_data.get("Metadata")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Input = Input


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
class DatabaseInputDefinition(BaseModel):
    GlueConnectionName: Optional[str]
    DatabaseTableName: Optional[str]
    TempDirectory: Optional["_S3Location"]
    QueryString: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseInputDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseInputDefinition"]:
        if not json_data:
            return None
        return cls(
            GlueConnectionName=json_data.get("GlueConnectionName"),
            DatabaseTableName=json_data.get("DatabaseTableName"),
            TempDirectory=S3Location._deserialize(json_data.get("TempDirectory")),
            QueryString=json_data.get("QueryString"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseInputDefinition = DatabaseInputDefinition


@dataclass
class Metadata(BaseModel):
    SourceArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            SourceArn=json_data.get("SourceArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class PathOptions(BaseModel):
    FilesLimit: Optional["_FilesLimit"]
    LastModifiedDateCondition: Optional["_FilterExpression"]
    Parameters: Optional[Sequence["_PathParameter"]]

    @classmethod
    def _deserialize(
        cls: Type["_PathOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathOptions"]:
        if not json_data:
            return None
        return cls(
            FilesLimit=FilesLimit._deserialize(json_data.get("FilesLimit")),
            LastModifiedDateCondition=FilterExpression._deserialize(json_data.get("LastModifiedDateCondition")),
            Parameters=deserialize_list(json_data.get("Parameters"), PathParameter),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathOptions = PathOptions


@dataclass
class FilesLimit(BaseModel):
    MaxFiles: Optional[int]
    OrderedBy: Optional[str]
    Order: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilesLimit"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilesLimit"]:
        if not json_data:
            return None
        return cls(
            MaxFiles=json_data.get("MaxFiles"),
            OrderedBy=json_data.get("OrderedBy"),
            Order=json_data.get("Order"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilesLimit = FilesLimit


@dataclass
class FilterExpression(BaseModel):
    Expression: Optional[str]
    ValuesMap: Optional[Sequence["_FilterValue"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterExpression"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterExpression"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            ValuesMap=deserialize_list(json_data.get("ValuesMap"), FilterValue),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterExpression = FilterExpression


@dataclass
class FilterValue(BaseModel):
    ValueReference: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterValue"]:
        if not json_data:
            return None
        return cls(
            ValueReference=json_data.get("ValueReference"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterValue = FilterValue


@dataclass
class PathParameter(BaseModel):
    PathParameterName: Optional[str]
    DatasetParameter: Optional["_DatasetParameter"]

    @classmethod
    def _deserialize(
        cls: Type["_PathParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathParameter"]:
        if not json_data:
            return None
        return cls(
            PathParameterName=json_data.get("PathParameterName"),
            DatasetParameter=DatasetParameter._deserialize(json_data.get("DatasetParameter")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathParameter = PathParameter


@dataclass
class DatasetParameter(BaseModel):
    Name: Optional[str]
    Type: Optional[str]
    DatetimeOptions: Optional["_DatetimeOptions"]
    CreateColumn: Optional[bool]
    Filter: Optional["_FilterExpression"]

    @classmethod
    def _deserialize(
        cls: Type["_DatasetParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatasetParameter"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            DatetimeOptions=DatetimeOptions._deserialize(json_data.get("DatetimeOptions")),
            CreateColumn=json_data.get("CreateColumn"),
            Filter=FilterExpression._deserialize(json_data.get("Filter")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatasetParameter = DatasetParameter


@dataclass
class DatetimeOptions(BaseModel):
    Format: Optional[str]
    TimezoneOffset: Optional[str]
    LocaleCode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatetimeOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatetimeOptions"]:
        if not json_data:
            return None
        return cls(
            Format=json_data.get("Format"),
            TimezoneOffset=json_data.get("TimezoneOffset"),
            LocaleCode=json_data.get("LocaleCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatetimeOptions = DatetimeOptions


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


