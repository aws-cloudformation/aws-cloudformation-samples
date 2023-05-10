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
class AwsDatabrewJob(BaseModel):
    DatasetName: Optional[str]
    EncryptionKeyArn: Optional[str]
    EncryptionMode: Optional[str]
    Name: Optional[str]
    Type: Optional[str]
    LogSubscription: Optional[str]
    MaxCapacity: Optional[int]
    MaxRetries: Optional[int]
    Outputs: Optional[Sequence["_Output"]]
    DataCatalogOutputs: Optional[Sequence["_DataCatalogOutput"]]
    DatabaseOutputs: Optional[Sequence["_DatabaseOutput"]]
    OutputLocation: Optional["_OutputLocation"]
    ProjectName: Optional[str]
    Recipe: Optional["_Recipe"]
    RoleArn: Optional[str]
    Tags: Optional[Any]
    Timeout: Optional[int]
    JobSample: Optional["_JobSample"]
    ProfileConfiguration: Optional["_ProfileConfiguration"]
    ValidationConfigurations: Optional[Sequence["_ValidationConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDatabrewJob"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDatabrewJob"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DatasetName=json_data.get("DatasetName"),
            EncryptionKeyArn=json_data.get("EncryptionKeyArn"),
            EncryptionMode=json_data.get("EncryptionMode"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            LogSubscription=json_data.get("LogSubscription"),
            MaxCapacity=json_data.get("MaxCapacity"),
            MaxRetries=json_data.get("MaxRetries"),
            Outputs=deserialize_list(json_data.get("Outputs"), Output),
            DataCatalogOutputs=deserialize_list(json_data.get("DataCatalogOutputs"), DataCatalogOutput),
            DatabaseOutputs=deserialize_list(json_data.get("DatabaseOutputs"), DatabaseOutput),
            OutputLocation=OutputLocation._deserialize(json_data.get("OutputLocation")),
            ProjectName=json_data.get("ProjectName"),
            Recipe=Recipe._deserialize(json_data.get("Recipe")),
            RoleArn=json_data.get("RoleArn"),
            Tags=json_data.get("Tags"),
            Timeout=json_data.get("Timeout"),
            JobSample=JobSample._deserialize(json_data.get("JobSample")),
            ProfileConfiguration=ProfileConfiguration._deserialize(json_data.get("ProfileConfiguration")),
            ValidationConfigurations=deserialize_list(json_data.get("ValidationConfigurations"), ValidationConfiguration),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDatabrewJob = AwsDatabrewJob


@dataclass
class Output(BaseModel):
    CompressionFormat: Optional[str]
    Format: Optional[str]
    FormatOptions: Optional["_OutputFormatOptions"]
    PartitionColumns: Optional[Sequence[str]]
    Location: Optional["_S3Location"]
    Overwrite: Optional[bool]
    MaxOutputFiles: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Output"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Output"]:
        if not json_data:
            return None
        return cls(
            CompressionFormat=json_data.get("CompressionFormat"),
            Format=json_data.get("Format"),
            FormatOptions=OutputFormatOptions._deserialize(json_data.get("FormatOptions")),
            PartitionColumns=json_data.get("PartitionColumns"),
            Location=S3Location._deserialize(json_data.get("Location")),
            Overwrite=json_data.get("Overwrite"),
            MaxOutputFiles=json_data.get("MaxOutputFiles"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Output = Output


@dataclass
class OutputFormatOptions(BaseModel):
    Csv: Optional["_CsvOutputOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_OutputFormatOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputFormatOptions"]:
        if not json_data:
            return None
        return cls(
            Csv=CsvOutputOptions._deserialize(json_data.get("Csv")),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputFormatOptions = OutputFormatOptions


@dataclass
class CsvOutputOptions(BaseModel):
    Delimiter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CsvOutputOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CsvOutputOptions"]:
        if not json_data:
            return None
        return cls(
            Delimiter=json_data.get("Delimiter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CsvOutputOptions = CsvOutputOptions


@dataclass
class S3Location(BaseModel):
    Bucket: Optional[str]
    Key: Optional[str]
    BucketOwner: Optional[str]

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
            BucketOwner=json_data.get("BucketOwner"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Location = S3Location


@dataclass
class DataCatalogOutput(BaseModel):
    CatalogId: Optional[str]
    DatabaseName: Optional[str]
    TableName: Optional[str]
    S3Options: Optional["_S3TableOutputOptions"]
    DatabaseOptions: Optional["_DatabaseTableOutputOptions"]
    Overwrite: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DataCatalogOutput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataCatalogOutput"]:
        if not json_data:
            return None
        return cls(
            CatalogId=json_data.get("CatalogId"),
            DatabaseName=json_data.get("DatabaseName"),
            TableName=json_data.get("TableName"),
            S3Options=S3TableOutputOptions._deserialize(json_data.get("S3Options")),
            DatabaseOptions=DatabaseTableOutputOptions._deserialize(json_data.get("DatabaseOptions")),
            Overwrite=json_data.get("Overwrite"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataCatalogOutput = DataCatalogOutput


@dataclass
class S3TableOutputOptions(BaseModel):
    Location: Optional["_S3Location"]

    @classmethod
    def _deserialize(
        cls: Type["_S3TableOutputOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3TableOutputOptions"]:
        if not json_data:
            return None
        return cls(
            Location=S3Location._deserialize(json_data.get("Location")),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3TableOutputOptions = S3TableOutputOptions


@dataclass
class DatabaseTableOutputOptions(BaseModel):
    TempDirectory: Optional["_S3Location"]
    TableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseTableOutputOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseTableOutputOptions"]:
        if not json_data:
            return None
        return cls(
            TempDirectory=S3Location._deserialize(json_data.get("TempDirectory")),
            TableName=json_data.get("TableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseTableOutputOptions = DatabaseTableOutputOptions


@dataclass
class DatabaseOutput(BaseModel):
    GlueConnectionName: Optional[str]
    DatabaseOutputMode: Optional[str]
    DatabaseOptions: Optional["_DatabaseTableOutputOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_DatabaseOutput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabaseOutput"]:
        if not json_data:
            return None
        return cls(
            GlueConnectionName=json_data.get("GlueConnectionName"),
            DatabaseOutputMode=json_data.get("DatabaseOutputMode"),
            DatabaseOptions=DatabaseTableOutputOptions._deserialize(json_data.get("DatabaseOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabaseOutput = DatabaseOutput


@dataclass
class OutputLocation(BaseModel):
    Bucket: Optional[str]
    Key: Optional[str]
    BucketOwner: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutputLocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputLocation"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Key=json_data.get("Key"),
            BucketOwner=json_data.get("BucketOwner"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputLocation = OutputLocation


@dataclass
class Recipe(BaseModel):
    Name: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Recipe"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Recipe"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Recipe = Recipe


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
class JobSample(BaseModel):
    Mode: Optional[str]
    Size: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_JobSample"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JobSample"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
            Size=json_data.get("Size"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JobSample = JobSample


@dataclass
class ProfileConfiguration(BaseModel):
    DatasetStatisticsConfiguration: Optional["_StatisticsConfiguration"]
    ProfileColumns: Optional[Sequence["_ColumnSelector"]]
    ColumnStatisticsConfigurations: Optional[Sequence["_ColumnStatisticsConfiguration"]]
    EntityDetectorConfiguration: Optional["_EntityDetectorConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ProfileConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProfileConfiguration"]:
        if not json_data:
            return None
        return cls(
            DatasetStatisticsConfiguration=StatisticsConfiguration._deserialize(json_data.get("DatasetStatisticsConfiguration")),
            ProfileColumns=deserialize_list(json_data.get("ProfileColumns"), ColumnSelector),
            ColumnStatisticsConfigurations=deserialize_list(json_data.get("ColumnStatisticsConfigurations"), ColumnStatisticsConfiguration),
            EntityDetectorConfiguration=EntityDetectorConfiguration._deserialize(json_data.get("EntityDetectorConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProfileConfiguration = ProfileConfiguration


@dataclass
class StatisticsConfiguration(BaseModel):
    IncludedStatistics: Optional[Sequence[str]]
    Overrides: Optional[Sequence["_StatisticOverride"]]

    @classmethod
    def _deserialize(
        cls: Type["_StatisticsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatisticsConfiguration"]:
        if not json_data:
            return None
        return cls(
            IncludedStatistics=json_data.get("IncludedStatistics"),
            Overrides=deserialize_list(json_data.get("Overrides"), StatisticOverride),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatisticsConfiguration = StatisticsConfiguration


@dataclass
class StatisticOverride(BaseModel):
    Statistic: Optional[str]
    Parameters: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_StatisticOverride"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatisticOverride"]:
        if not json_data:
            return None
        return cls(
            Statistic=json_data.get("Statistic"),
            Parameters=json_data.get("Parameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatisticOverride = StatisticOverride


@dataclass
class ColumnSelector(BaseModel):
    Regex: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnSelector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnSelector"]:
        if not json_data:
            return None
        return cls(
            Regex=json_data.get("Regex"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnSelector = ColumnSelector


@dataclass
class ColumnStatisticsConfiguration(BaseModel):
    Selectors: Optional[Sequence["_ColumnSelector"]]
    Statistics: Optional["_StatisticsConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ColumnStatisticsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColumnStatisticsConfiguration"]:
        if not json_data:
            return None
        return cls(
            Selectors=deserialize_list(json_data.get("Selectors"), ColumnSelector),
            Statistics=StatisticsConfiguration._deserialize(json_data.get("Statistics")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColumnStatisticsConfiguration = ColumnStatisticsConfiguration


@dataclass
class EntityDetectorConfiguration(BaseModel):
    EntityTypes: Optional[Sequence[str]]
    AllowedStatistics: Optional["_AllowedStatistics"]

    @classmethod
    def _deserialize(
        cls: Type["_EntityDetectorConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntityDetectorConfiguration"]:
        if not json_data:
            return None
        return cls(
            EntityTypes=json_data.get("EntityTypes"),
            AllowedStatistics=AllowedStatistics._deserialize(json_data.get("AllowedStatistics")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntityDetectorConfiguration = EntityDetectorConfiguration


@dataclass
class AllowedStatistics(BaseModel):
    Statistics: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AllowedStatistics"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllowedStatistics"]:
        if not json_data:
            return None
        return cls(
            Statistics=json_data.get("Statistics"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllowedStatistics = AllowedStatistics


@dataclass
class ValidationConfiguration(BaseModel):
    RulesetArn: Optional[str]
    ValidationMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValidationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValidationConfiguration"]:
        if not json_data:
            return None
        return cls(
            RulesetArn=json_data.get("RulesetArn"),
            ValidationMode=json_data.get("ValidationMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValidationConfiguration = ValidationConfiguration


