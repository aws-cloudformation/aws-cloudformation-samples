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
class AwsQuicksightDataset(BaseModel):
    Arn: Optional[str]
    AwsAccountId: Optional[str]
    ColumnGroups: Optional[Sequence["_ColumnGroup"]]
    ColumnLevelPermissionRules: Optional[Sequence["_ColumnLevelPermissionRule"]]
    ConsumedSpiceCapacityInBytes: Optional[float]
    CreatedTime: Optional[str]
    DataSetId: Optional[str]
    FieldFolders: Optional[MutableMapping[str, "_FieldFolder"]]
    ImportMode: Optional[str]
    LastUpdatedTime: Optional[str]
    LogicalTableMap: Optional[MutableMapping[str, "_LogicalTable"]]
    Name: Optional[str]
    OutputColumns: Optional[Sequence["_OutputColumn"]]
    Permissions: Optional[Sequence["_ResourcePermission"]]
    PhysicalTableMap: Optional[MutableMapping[str, "_PhysicalTable"]]
    RowLevelPermissionDataSet: Optional["_RowLevelPermissionDataSet"]
    Tags: Optional[Any]
    IngestionWaitPolicy: Optional["_IngestionWaitPolicy"]
    DataSetUsageConfiguration: Optional["_DataSetUsageConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsQuicksightDataset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsQuicksightDataset"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            AwsAccountId=json_data.get("AwsAccountId"),
            ColumnGroups=deserialize_list(json_data.get("ColumnGroups"), ColumnGroup),
            ColumnLevelPermissionRules=deserialize_list(json_data.get("ColumnLevelPermissionRules"), ColumnLevelPermissionRule),
            ConsumedSpiceCapacityInBytes=json_data.get("ConsumedSpiceCapacityInBytes"),
            CreatedTime=json_data.get("CreatedTime"),
            DataSetId=json_data.get("DataSetId"),
            FieldFolders=json_data.get("FieldFolders"),
            ImportMode=json_data.get("ImportMode"),
            LastUpdatedTime=json_data.get("LastUpdatedTime"),
            LogicalTableMap=json_data.get("LogicalTableMap"),
            Name=json_data.get("Name"),
            OutputColumns=deserialize_list(json_data.get("OutputColumns"), OutputColumn),
            Permissions=deserialize_list(json_data.get("Permissions"), ResourcePermission),
            PhysicalTableMap=json_data.get("PhysicalTableMap"),
            RowLevelPermissionDataSet=RowLevelPermissionDataSet._deserialize(json_data.get("RowLevelPermissionDataSet")),
            Tags=json_data.get("Tags"),
            IngestionWaitPolicy=IngestionWaitPolicy._deserialize(json_data.get("IngestionWaitPolicy")),
            DataSetUsageConfiguration=DataSetUsageConfiguration._deserialize(json_data.get("DataSetUsageConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsQuicksightDataset = AwsQuicksightDataset


@dataclass
class ColumnGroup(BaseModel):
    GeoSpatialColumnGroup: Optional["_GeoSpatialColumnGroup"]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnGroup"]:
        if not json_data:
            return None
        return cls(
            GeoSpatialColumnGroup=GeoSpatialColumnGroup._deserialize(json_data.get("GeoSpatialColumnGroup")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnGroup = ColumnGroup


@dataclass
class GeoSpatialColumnGroup(BaseModel):
    Columns: Optional[Sequence[str]]
    CountryCode: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GeoSpatialColumnGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeoSpatialColumnGroup"]:
        if not json_data:
            return None
        return cls(
            Columns=json_data.get("Columns"),
            CountryCode=json_data.get("CountryCode"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeoSpatialColumnGroup = GeoSpatialColumnGroup


@dataclass
class ColumnLevelPermissionRule(BaseModel):
    ColumnNames: Optional[Sequence[str]]
    Principals: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnLevelPermissionRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnLevelPermissionRule"]:
        if not json_data:
            return None
        return cls(
            ColumnNames=json_data.get("ColumnNames"),
            Principals=json_data.get("Principals"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnLevelPermissionRule = ColumnLevelPermissionRule


@dataclass
class FieldFolder(BaseModel):
    Description: Optional[str]
    Columns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FieldFolder"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldFolder"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Columns=json_data.get("Columns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldFolder = FieldFolder


@dataclass
class LogicalTable(BaseModel):
    Alias: Optional[str]
    DataTransforms: Optional[Sequence["_TransformOperation"]]
    Source: Optional["_LogicalTableSource"]

    @classmethod
    def _deserialize(
        cls: Type["_LogicalTable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogicalTable"]:
        if not json_data:
            return None
        return cls(
            Alias=json_data.get("Alias"),
            DataTransforms=deserialize_list(json_data.get("DataTransforms"), TransformOperation),
            Source=LogicalTableSource._deserialize(json_data.get("Source")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogicalTable = LogicalTable


@dataclass
class TransformOperation(BaseModel):
    TagColumnOperation: Optional["_TagColumnOperation"]
    FilterOperation: Optional["_FilterOperation"]
    CastColumnTypeOperation: Optional["_CastColumnTypeOperation"]
    CreateColumnsOperation: Optional["_CreateColumnsOperation"]
    RenameColumnOperation: Optional["_RenameColumnOperation"]
    ProjectOperation: Optional["_ProjectOperation"]

    @classmethod
    def _deserialize(
        cls: Type["_TransformOperation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransformOperation"]:
        if not json_data:
            return None
        return cls(
            TagColumnOperation=TagColumnOperation._deserialize(json_data.get("TagColumnOperation")),
            FilterOperation=FilterOperation._deserialize(json_data.get("FilterOperation")),
            CastColumnTypeOperation=CastColumnTypeOperation._deserialize(json_data.get("CastColumnTypeOperation")),
            CreateColumnsOperation=CreateColumnsOperation._deserialize(json_data.get("CreateColumnsOperation")),
            RenameColumnOperation=RenameColumnOperation._deserialize(json_data.get("RenameColumnOperation")),
            ProjectOperation=ProjectOperation._deserialize(json_data.get("ProjectOperation")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransformOperation = TransformOperation


@dataclass
class TagColumnOperation(BaseModel):
    ColumnName: Optional[str]
    Tags: Optional[Sequence["_ColumnTag"]]

    @classmethod
    def _deserialize(
        cls: Type["_TagColumnOperation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagColumnOperation"]:
        if not json_data:
            return None
        return cls(
            ColumnName=json_data.get("ColumnName"),
            Tags=deserialize_list(json_data.get("Tags"), ColumnTag),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagColumnOperation = TagColumnOperation


@dataclass
class ColumnTag(BaseModel):
    ColumnGeographicRole: Optional[str]
    ColumnDescription: Optional["_ColumnDescription"]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnTag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnTag"]:
        if not json_data:
            return None
        return cls(
            ColumnGeographicRole=json_data.get("ColumnGeographicRole"),
            ColumnDescription=ColumnDescription._deserialize(json_data.get("ColumnDescription")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnTag = ColumnTag


@dataclass
class ColumnDescription(BaseModel):
    Text: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnDescription"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnDescription"]:
        if not json_data:
            return None
        return cls(
            Text=json_data.get("Text"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnDescription = ColumnDescription


@dataclass
class FilterOperation(BaseModel):
    ConditionExpression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterOperation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterOperation"]:
        if not json_data:
            return None
        return cls(
            ConditionExpression=json_data.get("ConditionExpression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterOperation = FilterOperation


@dataclass
class CastColumnTypeOperation(BaseModel):
    ColumnName: Optional[str]
    Format: Optional[str]
    NewColumnType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CastColumnTypeOperation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CastColumnTypeOperation"]:
        if not json_data:
            return None
        return cls(
            ColumnName=json_data.get("ColumnName"),
            Format=json_data.get("Format"),
            NewColumnType=json_data.get("NewColumnType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CastColumnTypeOperation = CastColumnTypeOperation


@dataclass
class CreateColumnsOperation(BaseModel):
    Columns: Optional[Sequence["_CalculatedColumn"]]

    @classmethod
    def _deserialize(
        cls: Type["_CreateColumnsOperation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreateColumnsOperation"]:
        if not json_data:
            return None
        return cls(
            Columns=deserialize_list(json_data.get("Columns"), CalculatedColumn),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreateColumnsOperation = CreateColumnsOperation


@dataclass
class CalculatedColumn(BaseModel):
    ColumnId: Optional[str]
    ColumnName: Optional[str]
    Expression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CalculatedColumn"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CalculatedColumn"]:
        if not json_data:
            return None
        return cls(
            ColumnId=json_data.get("ColumnId"),
            ColumnName=json_data.get("ColumnName"),
            Expression=json_data.get("Expression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CalculatedColumn = CalculatedColumn


@dataclass
class RenameColumnOperation(BaseModel):
    NewColumnName: Optional[str]
    ColumnName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RenameColumnOperation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RenameColumnOperation"]:
        if not json_data:
            return None
        return cls(
            NewColumnName=json_data.get("NewColumnName"),
            ColumnName=json_data.get("ColumnName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RenameColumnOperation = RenameColumnOperation


@dataclass
class ProjectOperation(BaseModel):
    ProjectedColumns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectOperation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectOperation"]:
        if not json_data:
            return None
        return cls(
            ProjectedColumns=json_data.get("ProjectedColumns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectOperation = ProjectOperation


@dataclass
class LogicalTableSource(BaseModel):
    PhysicalTableId: Optional[str]
    JoinInstruction: Optional["_JoinInstruction"]
    DataSetArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogicalTableSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogicalTableSource"]:
        if not json_data:
            return None
        return cls(
            PhysicalTableId=json_data.get("PhysicalTableId"),
            JoinInstruction=JoinInstruction._deserialize(json_data.get("JoinInstruction")),
            DataSetArn=json_data.get("DataSetArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogicalTableSource = LogicalTableSource


@dataclass
class JoinInstruction(BaseModel):
    OnClause: Optional[str]
    Type: Optional[str]
    LeftJoinKeyProperties: Optional["_JoinKeyProperties"]
    LeftOperand: Optional[str]
    RightOperand: Optional[str]
    RightJoinKeyProperties: Optional["_JoinKeyProperties"]

    @classmethod
    def _deserialize(
        cls: Type["_JoinInstruction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JoinInstruction"]:
        if not json_data:
            return None
        return cls(
            OnClause=json_data.get("OnClause"),
            Type=json_data.get("Type"),
            LeftJoinKeyProperties=JoinKeyProperties._deserialize(json_data.get("LeftJoinKeyProperties")),
            LeftOperand=json_data.get("LeftOperand"),
            RightOperand=json_data.get("RightOperand"),
            RightJoinKeyProperties=JoinKeyProperties._deserialize(json_data.get("RightJoinKeyProperties")),
        )


# work around possible type aliasing issues when variable has same name as a model
_JoinInstruction = JoinInstruction


@dataclass
class JoinKeyProperties(BaseModel):
    UniqueKey: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_JoinKeyProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JoinKeyProperties"]:
        if not json_data:
            return None
        return cls(
            UniqueKey=json_data.get("UniqueKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JoinKeyProperties = JoinKeyProperties


@dataclass
class OutputColumn(BaseModel):
    Type: Optional[str]
    Description: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutputColumn"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputColumn"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputColumn = OutputColumn


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
class PhysicalTable(BaseModel):
    RelationalTable: Optional["_RelationalTable"]
    CustomSql: Optional["_CustomSql"]
    S3Source: Optional["_S3Source"]

    @classmethod
    def _deserialize(
        cls: Type["_PhysicalTable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PhysicalTable"]:
        if not json_data:
            return None
        return cls(
            RelationalTable=RelationalTable._deserialize(json_data.get("RelationalTable")),
            CustomSql=CustomSql._deserialize(json_data.get("CustomSql")),
            S3Source=S3Source._deserialize(json_data.get("S3Source")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PhysicalTable = PhysicalTable


@dataclass
class RelationalTable(BaseModel):
    DataSourceArn: Optional[str]
    InputColumns: Optional[Sequence["_InputColumn"]]
    Schema: Optional[str]
    Catalog: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelationalTable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelationalTable"]:
        if not json_data:
            return None
        return cls(
            DataSourceArn=json_data.get("DataSourceArn"),
            InputColumns=deserialize_list(json_data.get("InputColumns"), InputColumn),
            Schema=json_data.get("Schema"),
            Catalog=json_data.get("Catalog"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelationalTable = RelationalTable


@dataclass
class InputColumn(BaseModel):
    Type: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputColumn"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputColumn"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputColumn = InputColumn


@dataclass
class CustomSql(BaseModel):
    DataSourceArn: Optional[str]
    SqlQuery: Optional[str]
    Columns: Optional[Sequence["_InputColumn"]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomSql"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomSql"]:
        if not json_data:
            return None
        return cls(
            DataSourceArn=json_data.get("DataSourceArn"),
            SqlQuery=json_data.get("SqlQuery"),
            Columns=deserialize_list(json_data.get("Columns"), InputColumn),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomSql = CustomSql


@dataclass
class S3Source(BaseModel):
    DataSourceArn: Optional[str]
    InputColumns: Optional[Sequence["_InputColumn"]]
    UploadSettings: Optional["_UploadSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_S3Source"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Source"]:
        if not json_data:
            return None
        return cls(
            DataSourceArn=json_data.get("DataSourceArn"),
            InputColumns=deserialize_list(json_data.get("InputColumns"), InputColumn),
            UploadSettings=UploadSettings._deserialize(json_data.get("UploadSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Source = S3Source


@dataclass
class UploadSettings(BaseModel):
    ContainsHeader: Optional[bool]
    TextQualifier: Optional[str]
    Format: Optional[str]
    StartFromRow: Optional[float]
    Delimiter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UploadSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UploadSettings"]:
        if not json_data:
            return None
        return cls(
            ContainsHeader=json_data.get("ContainsHeader"),
            TextQualifier=json_data.get("TextQualifier"),
            Format=json_data.get("Format"),
            StartFromRow=json_data.get("StartFromRow"),
            Delimiter=json_data.get("Delimiter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UploadSettings = UploadSettings


@dataclass
class RowLevelPermissionDataSet(BaseModel):
    Arn: Optional[str]
    Namespace: Optional[str]
    PermissionPolicy: Optional[str]
    FormatVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RowLevelPermissionDataSet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RowLevelPermissionDataSet"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            Namespace=json_data.get("Namespace"),
            PermissionPolicy=json_data.get("PermissionPolicy"),
            FormatVersion=json_data.get("FormatVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RowLevelPermissionDataSet = RowLevelPermissionDataSet


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
class IngestionWaitPolicy(BaseModel):
    WaitForSpiceIngestion: Optional[bool]
    IngestionWaitTimeInHours: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IngestionWaitPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngestionWaitPolicy"]:
        if not json_data:
            return None
        return cls(
            WaitForSpiceIngestion=json_data.get("WaitForSpiceIngestion"),
            IngestionWaitTimeInHours=json_data.get("IngestionWaitTimeInHours"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngestionWaitPolicy = IngestionWaitPolicy


@dataclass
class DataSetUsageConfiguration(BaseModel):
    DisableUseAsDirectQuerySource: Optional[bool]
    DisableUseAsImportedSource: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DataSetUsageConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataSetUsageConfiguration"]:
        if not json_data:
            return None
        return cls(
            DisableUseAsDirectQuerySource=json_data.get("DisableUseAsDirectQuerySource"),
            DisableUseAsImportedSource=json_data.get("DisableUseAsImportedSource"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataSetUsageConfiguration = DataSetUsageConfiguration


