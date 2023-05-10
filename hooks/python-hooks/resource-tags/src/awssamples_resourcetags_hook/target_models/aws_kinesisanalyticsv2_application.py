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
class AwsKinesisanalyticsv2Application(BaseModel):
    ApplicationConfiguration: Optional["_ApplicationConfiguration"]
    ApplicationDescription: Optional[str]
    ApplicationMode: Optional[str]
    ApplicationName: Optional[str]
    RuntimeEnvironment: Optional[str]
    ServiceExecutionRole: Optional[str]
    RunConfiguration: Optional["_RunConfiguration"]
    ApplicationMaintenanceConfiguration: Optional["_ApplicationMaintenanceConfiguration"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsKinesisanalyticsv2Application"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsKinesisanalyticsv2Application"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ApplicationConfiguration=ApplicationConfiguration._deserialize(json_data.get("ApplicationConfiguration")),
            ApplicationDescription=json_data.get("ApplicationDescription"),
            ApplicationMode=json_data.get("ApplicationMode"),
            ApplicationName=json_data.get("ApplicationName"),
            RuntimeEnvironment=json_data.get("RuntimeEnvironment"),
            ServiceExecutionRole=json_data.get("ServiceExecutionRole"),
            RunConfiguration=RunConfiguration._deserialize(json_data.get("RunConfiguration")),
            ApplicationMaintenanceConfiguration=ApplicationMaintenanceConfiguration._deserialize(json_data.get("ApplicationMaintenanceConfiguration")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsKinesisanalyticsv2Application = AwsKinesisanalyticsv2Application


@dataclass
class ApplicationConfiguration(BaseModel):
    ApplicationCodeConfiguration: Optional["_ApplicationCodeConfiguration"]
    ApplicationSnapshotConfiguration: Optional["_ApplicationSnapshotConfiguration"]
    EnvironmentProperties: Optional["_EnvironmentProperties"]
    FlinkApplicationConfiguration: Optional["_FlinkApplicationConfiguration"]
    SqlApplicationConfiguration: Optional["_SqlApplicationConfiguration"]
    ZeppelinApplicationConfiguration: Optional["_ZeppelinApplicationConfiguration"]
    VpcConfigurations: Optional[Sequence["_VpcConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationConfiguration"]:
        if not json_data:
            return None
        return cls(
            ApplicationCodeConfiguration=ApplicationCodeConfiguration._deserialize(json_data.get("ApplicationCodeConfiguration")),
            ApplicationSnapshotConfiguration=ApplicationSnapshotConfiguration._deserialize(json_data.get("ApplicationSnapshotConfiguration")),
            EnvironmentProperties=EnvironmentProperties._deserialize(json_data.get("EnvironmentProperties")),
            FlinkApplicationConfiguration=FlinkApplicationConfiguration._deserialize(json_data.get("FlinkApplicationConfiguration")),
            SqlApplicationConfiguration=SqlApplicationConfiguration._deserialize(json_data.get("SqlApplicationConfiguration")),
            ZeppelinApplicationConfiguration=ZeppelinApplicationConfiguration._deserialize(json_data.get("ZeppelinApplicationConfiguration")),
            VpcConfigurations=deserialize_list(json_data.get("VpcConfigurations"), VpcConfiguration),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationConfiguration = ApplicationConfiguration


@dataclass
class ApplicationCodeConfiguration(BaseModel):
    CodeContent: Optional["_CodeContent"]
    CodeContentType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationCodeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationCodeConfiguration"]:
        if not json_data:
            return None
        return cls(
            CodeContent=CodeContent._deserialize(json_data.get("CodeContent")),
            CodeContentType=json_data.get("CodeContentType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationCodeConfiguration = ApplicationCodeConfiguration


@dataclass
class CodeContent(BaseModel):
    ZipFileContent: Optional[str]
    S3ContentLocation: Optional["_S3ContentLocation"]
    TextContent: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CodeContent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CodeContent"]:
        if not json_data:
            return None
        return cls(
            ZipFileContent=json_data.get("ZipFileContent"),
            S3ContentLocation=S3ContentLocation._deserialize(json_data.get("S3ContentLocation")),
            TextContent=json_data.get("TextContent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CodeContent = CodeContent


@dataclass
class S3ContentLocation(BaseModel):
    BucketARN: Optional[str]
    FileKey: Optional[str]
    ObjectVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3ContentLocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3ContentLocation"]:
        if not json_data:
            return None
        return cls(
            BucketARN=json_data.get("BucketARN"),
            FileKey=json_data.get("FileKey"),
            ObjectVersion=json_data.get("ObjectVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3ContentLocation = S3ContentLocation


@dataclass
class ApplicationSnapshotConfiguration(BaseModel):
    SnapshotsEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationSnapshotConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationSnapshotConfiguration"]:
        if not json_data:
            return None
        return cls(
            SnapshotsEnabled=json_data.get("SnapshotsEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationSnapshotConfiguration = ApplicationSnapshotConfiguration


@dataclass
class EnvironmentProperties(BaseModel):
    PropertyGroups: Optional[Sequence["_PropertyGroup"]]

    @classmethod
    def _deserialize(
        cls: Type["_EnvironmentProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnvironmentProperties"]:
        if not json_data:
            return None
        return cls(
            PropertyGroups=deserialize_list(json_data.get("PropertyGroups"), PropertyGroup),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnvironmentProperties = EnvironmentProperties


@dataclass
class PropertyGroup(BaseModel):
    PropertyGroupId: Optional[str]
    PropertyMap: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_PropertyGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertyGroup"]:
        if not json_data:
            return None
        return cls(
            PropertyGroupId=json_data.get("PropertyGroupId"),
            PropertyMap=json_data.get("PropertyMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertyGroup = PropertyGroup


@dataclass
class FlinkApplicationConfiguration(BaseModel):
    CheckpointConfiguration: Optional["_CheckpointConfiguration"]
    MonitoringConfiguration: Optional["_MonitoringConfiguration"]
    ParallelismConfiguration: Optional["_ParallelismConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_FlinkApplicationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FlinkApplicationConfiguration"]:
        if not json_data:
            return None
        return cls(
            CheckpointConfiguration=CheckpointConfiguration._deserialize(json_data.get("CheckpointConfiguration")),
            MonitoringConfiguration=MonitoringConfiguration._deserialize(json_data.get("MonitoringConfiguration")),
            ParallelismConfiguration=ParallelismConfiguration._deserialize(json_data.get("ParallelismConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FlinkApplicationConfiguration = FlinkApplicationConfiguration


@dataclass
class CheckpointConfiguration(BaseModel):
    ConfigurationType: Optional[str]
    CheckpointingEnabled: Optional[bool]
    CheckpointInterval: Optional[int]
    MinPauseBetweenCheckpoints: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_CheckpointConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CheckpointConfiguration"]:
        if not json_data:
            return None
        return cls(
            ConfigurationType=json_data.get("ConfigurationType"),
            CheckpointingEnabled=json_data.get("CheckpointingEnabled"),
            CheckpointInterval=json_data.get("CheckpointInterval"),
            MinPauseBetweenCheckpoints=json_data.get("MinPauseBetweenCheckpoints"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CheckpointConfiguration = CheckpointConfiguration


@dataclass
class MonitoringConfiguration(BaseModel):
    ConfigurationType: Optional[str]
    MetricsLevel: Optional[str]
    LogLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MonitoringConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitoringConfiguration"]:
        if not json_data:
            return None
        return cls(
            ConfigurationType=json_data.get("ConfigurationType"),
            MetricsLevel=json_data.get("MetricsLevel"),
            LogLevel=json_data.get("LogLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitoringConfiguration = MonitoringConfiguration


@dataclass
class ParallelismConfiguration(BaseModel):
    ConfigurationType: Optional[str]
    ParallelismPerKPU: Optional[int]
    Parallelism: Optional[int]
    AutoScalingEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ParallelismConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParallelismConfiguration"]:
        if not json_data:
            return None
        return cls(
            ConfigurationType=json_data.get("ConfigurationType"),
            ParallelismPerKPU=json_data.get("ParallelismPerKPU"),
            Parallelism=json_data.get("Parallelism"),
            AutoScalingEnabled=json_data.get("AutoScalingEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParallelismConfiguration = ParallelismConfiguration


@dataclass
class SqlApplicationConfiguration(BaseModel):
    Inputs: Optional[Sequence["_Input"]]

    @classmethod
    def _deserialize(
        cls: Type["_SqlApplicationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SqlApplicationConfiguration"]:
        if not json_data:
            return None
        return cls(
            Inputs=deserialize_list(json_data.get("Inputs"), Input),
        )


# work around possible type aliasing issues when variable has same name as a model
_SqlApplicationConfiguration = SqlApplicationConfiguration


@dataclass
class Input(BaseModel):
    NamePrefix: Optional[str]
    InputSchema: Optional["_InputSchema"]
    KinesisStreamsInput: Optional["_KinesisStreamsInput"]
    KinesisFirehoseInput: Optional["_KinesisFirehoseInput"]
    InputProcessingConfiguration: Optional["_InputProcessingConfiguration"]
    InputParallelism: Optional["_InputParallelism"]

    @classmethod
    def _deserialize(
        cls: Type["_Input"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Input"]:
        if not json_data:
            return None
        return cls(
            NamePrefix=json_data.get("NamePrefix"),
            InputSchema=InputSchema._deserialize(json_data.get("InputSchema")),
            KinesisStreamsInput=KinesisStreamsInput._deserialize(json_data.get("KinesisStreamsInput")),
            KinesisFirehoseInput=KinesisFirehoseInput._deserialize(json_data.get("KinesisFirehoseInput")),
            InputProcessingConfiguration=InputProcessingConfiguration._deserialize(json_data.get("InputProcessingConfiguration")),
            InputParallelism=InputParallelism._deserialize(json_data.get("InputParallelism")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Input = Input


@dataclass
class InputSchema(BaseModel):
    RecordEncoding: Optional[str]
    RecordColumns: Optional[Sequence["_RecordColumn"]]
    RecordFormat: Optional["_RecordFormat"]

    @classmethod
    def _deserialize(
        cls: Type["_InputSchema"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputSchema"]:
        if not json_data:
            return None
        return cls(
            RecordEncoding=json_data.get("RecordEncoding"),
            RecordColumns=deserialize_list(json_data.get("RecordColumns"), RecordColumn),
            RecordFormat=RecordFormat._deserialize(json_data.get("RecordFormat")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputSchema = InputSchema


@dataclass
class RecordColumn(BaseModel):
    Mapping: Optional[str]
    Name: Optional[str]
    SqlType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecordColumn"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordColumn"]:
        if not json_data:
            return None
        return cls(
            Mapping=json_data.get("Mapping"),
            Name=json_data.get("Name"),
            SqlType=json_data.get("SqlType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordColumn = RecordColumn


@dataclass
class RecordFormat(BaseModel):
    RecordFormatType: Optional[str]
    MappingParameters: Optional["_MappingParameters"]

    @classmethod
    def _deserialize(
        cls: Type["_RecordFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordFormat"]:
        if not json_data:
            return None
        return cls(
            RecordFormatType=json_data.get("RecordFormatType"),
            MappingParameters=MappingParameters._deserialize(json_data.get("MappingParameters")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordFormat = RecordFormat


@dataclass
class MappingParameters(BaseModel):
    CSVMappingParameters: Optional["_CSVMappingParameters"]
    JSONMappingParameters: Optional["_JSONMappingParameters"]

    @classmethod
    def _deserialize(
        cls: Type["_MappingParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MappingParameters"]:
        if not json_data:
            return None
        return cls(
            CSVMappingParameters=CSVMappingParameters._deserialize(json_data.get("CSVMappingParameters")),
            JSONMappingParameters=JSONMappingParameters._deserialize(json_data.get("JSONMappingParameters")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MappingParameters = MappingParameters


@dataclass
class CSVMappingParameters(BaseModel):
    RecordColumnDelimiter: Optional[str]
    RecordRowDelimiter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CSVMappingParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CSVMappingParameters"]:
        if not json_data:
            return None
        return cls(
            RecordColumnDelimiter=json_data.get("RecordColumnDelimiter"),
            RecordRowDelimiter=json_data.get("RecordRowDelimiter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CSVMappingParameters = CSVMappingParameters


@dataclass
class JSONMappingParameters(BaseModel):
    RecordRowPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JSONMappingParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JSONMappingParameters"]:
        if not json_data:
            return None
        return cls(
            RecordRowPath=json_data.get("RecordRowPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JSONMappingParameters = JSONMappingParameters


@dataclass
class KinesisStreamsInput(BaseModel):
    ResourceARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisStreamsInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisStreamsInput"]:
        if not json_data:
            return None
        return cls(
            ResourceARN=json_data.get("ResourceARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisStreamsInput = KinesisStreamsInput


@dataclass
class KinesisFirehoseInput(BaseModel):
    ResourceARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisFirehoseInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisFirehoseInput"]:
        if not json_data:
            return None
        return cls(
            ResourceARN=json_data.get("ResourceARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisFirehoseInput = KinesisFirehoseInput


@dataclass
class InputProcessingConfiguration(BaseModel):
    InputLambdaProcessor: Optional["_InputLambdaProcessor"]

    @classmethod
    def _deserialize(
        cls: Type["_InputProcessingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputProcessingConfiguration"]:
        if not json_data:
            return None
        return cls(
            InputLambdaProcessor=InputLambdaProcessor._deserialize(json_data.get("InputLambdaProcessor")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputProcessingConfiguration = InputProcessingConfiguration


@dataclass
class InputLambdaProcessor(BaseModel):
    ResourceARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputLambdaProcessor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputLambdaProcessor"]:
        if not json_data:
            return None
        return cls(
            ResourceARN=json_data.get("ResourceARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputLambdaProcessor = InputLambdaProcessor


@dataclass
class InputParallelism(BaseModel):
    Count: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_InputParallelism"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputParallelism"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputParallelism = InputParallelism


@dataclass
class ZeppelinApplicationConfiguration(BaseModel):
    CatalogConfiguration: Optional["_CatalogConfiguration"]
    MonitoringConfiguration: Optional["_ZeppelinMonitoringConfiguration"]
    DeployAsApplicationConfiguration: Optional["_DeployAsApplicationConfiguration"]
    CustomArtifactsConfiguration: Optional[Sequence["_CustomArtifactConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_ZeppelinApplicationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZeppelinApplicationConfiguration"]:
        if not json_data:
            return None
        return cls(
            CatalogConfiguration=CatalogConfiguration._deserialize(json_data.get("CatalogConfiguration")),
            MonitoringConfiguration=ZeppelinMonitoringConfiguration._deserialize(json_data.get("MonitoringConfiguration")),
            DeployAsApplicationConfiguration=DeployAsApplicationConfiguration._deserialize(json_data.get("DeployAsApplicationConfiguration")),
            CustomArtifactsConfiguration=deserialize_list(json_data.get("CustomArtifactsConfiguration"), CustomArtifactConfiguration),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZeppelinApplicationConfiguration = ZeppelinApplicationConfiguration


@dataclass
class CatalogConfiguration(BaseModel):
    GlueDataCatalogConfiguration: Optional["_GlueDataCatalogConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_CatalogConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CatalogConfiguration"]:
        if not json_data:
            return None
        return cls(
            GlueDataCatalogConfiguration=GlueDataCatalogConfiguration._deserialize(json_data.get("GlueDataCatalogConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CatalogConfiguration = CatalogConfiguration


@dataclass
class GlueDataCatalogConfiguration(BaseModel):
    DatabaseARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GlueDataCatalogConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlueDataCatalogConfiguration"]:
        if not json_data:
            return None
        return cls(
            DatabaseARN=json_data.get("DatabaseARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlueDataCatalogConfiguration = GlueDataCatalogConfiguration


@dataclass
class ZeppelinMonitoringConfiguration(BaseModel):
    LogLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ZeppelinMonitoringConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZeppelinMonitoringConfiguration"]:
        if not json_data:
            return None
        return cls(
            LogLevel=json_data.get("LogLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZeppelinMonitoringConfiguration = ZeppelinMonitoringConfiguration


@dataclass
class DeployAsApplicationConfiguration(BaseModel):
    S3ContentLocation: Optional["_S3ContentBaseLocation"]

    @classmethod
    def _deserialize(
        cls: Type["_DeployAsApplicationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeployAsApplicationConfiguration"]:
        if not json_data:
            return None
        return cls(
            S3ContentLocation=S3ContentBaseLocation._deserialize(json_data.get("S3ContentLocation")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeployAsApplicationConfiguration = DeployAsApplicationConfiguration


@dataclass
class S3ContentBaseLocation(BaseModel):
    BucketARN: Optional[str]
    BasePath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3ContentBaseLocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3ContentBaseLocation"]:
        if not json_data:
            return None
        return cls(
            BucketARN=json_data.get("BucketARN"),
            BasePath=json_data.get("BasePath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3ContentBaseLocation = S3ContentBaseLocation


@dataclass
class CustomArtifactConfiguration(BaseModel):
    ArtifactType: Optional[str]
    MavenReference: Optional["_MavenReference"]
    S3ContentLocation: Optional["_S3ContentLocation"]

    @classmethod
    def _deserialize(
        cls: Type["_CustomArtifactConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomArtifactConfiguration"]:
        if not json_data:
            return None
        return cls(
            ArtifactType=json_data.get("ArtifactType"),
            MavenReference=MavenReference._deserialize(json_data.get("MavenReference")),
            S3ContentLocation=S3ContentLocation._deserialize(json_data.get("S3ContentLocation")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomArtifactConfiguration = CustomArtifactConfiguration


@dataclass
class MavenReference(BaseModel):
    ArtifactId: Optional[str]
    GroupId: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MavenReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MavenReference"]:
        if not json_data:
            return None
        return cls(
            ArtifactId=json_data.get("ArtifactId"),
            GroupId=json_data.get("GroupId"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MavenReference = MavenReference


@dataclass
class VpcConfiguration(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfiguration"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfiguration = VpcConfiguration


@dataclass
class RunConfiguration(BaseModel):
    ApplicationRestoreConfiguration: Optional["_ApplicationRestoreConfiguration"]
    FlinkRunConfiguration: Optional["_FlinkRunConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_RunConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RunConfiguration"]:
        if not json_data:
            return None
        return cls(
            ApplicationRestoreConfiguration=ApplicationRestoreConfiguration._deserialize(json_data.get("ApplicationRestoreConfiguration")),
            FlinkRunConfiguration=FlinkRunConfiguration._deserialize(json_data.get("FlinkRunConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RunConfiguration = RunConfiguration


@dataclass
class ApplicationRestoreConfiguration(BaseModel):
    ApplicationRestoreType: Optional[str]
    SnapshotName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationRestoreConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationRestoreConfiguration"]:
        if not json_data:
            return None
        return cls(
            ApplicationRestoreType=json_data.get("ApplicationRestoreType"),
            SnapshotName=json_data.get("SnapshotName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationRestoreConfiguration = ApplicationRestoreConfiguration


@dataclass
class FlinkRunConfiguration(BaseModel):
    AllowNonRestoredState: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_FlinkRunConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FlinkRunConfiguration"]:
        if not json_data:
            return None
        return cls(
            AllowNonRestoredState=json_data.get("AllowNonRestoredState"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FlinkRunConfiguration = FlinkRunConfiguration


@dataclass
class ApplicationMaintenanceConfiguration(BaseModel):
    ApplicationMaintenanceWindowStartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationMaintenanceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationMaintenanceConfiguration"]:
        if not json_data:
            return None
        return cls(
            ApplicationMaintenanceWindowStartTime=json_data.get("ApplicationMaintenanceWindowStartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationMaintenanceConfiguration = ApplicationMaintenanceConfiguration


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


