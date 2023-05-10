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
class AwsDmsEndpoint(BaseModel):
    SybaseSettings: Optional["_SybaseSettings"]
    RedisSettings: Optional["_RedisSettings"]
    OracleSettings: Optional["_OracleSettings"]
    KafkaSettings: Optional["_KafkaSettings"]
    Port: Optional[int]
    MySqlSettings: Optional["_MySqlSettings"]
    S3Settings: Optional["_S3Settings"]
    ResourceIdentifier: Optional[str]
    KinesisSettings: Optional["_KinesisSettings"]
    SslMode: Optional[str]
    RedshiftSettings: Optional["_RedshiftSettings"]
    EndpointType: Optional[str]
    Tags: Optional[Any]
    Password: Optional[str]
    MongoDbSettings: Optional["_MongoDbSettings"]
    IbmDb2Settings: Optional["_IbmDb2Settings"]
    KmsKeyId: Optional[str]
    ExternalId: Optional[str]
    DatabaseName: Optional[str]
    NeptuneSettings: Optional["_NeptuneSettings"]
    ElasticsearchSettings: Optional["_ElasticsearchSettings"]
    EngineName: Optional[str]
    DocDbSettings: Optional["_DocDbSettings"]
    DynamoDbSettings: Optional["_DynamoDbSettings"]
    Username: Optional[str]
    MicrosoftSqlServerSettings: Optional["_MicrosoftSqlServerSettings"]
    GcpMySQLSettings: Optional["_GcpMySQLSettings"]
    ServerName: Optional[str]
    ExtraConnectionAttributes: Optional[str]
    Id: Optional[str]
    EndpointIdentifier: Optional[str]
    CertificateArn: Optional[str]
    PostgreSqlSettings: Optional["_PostgreSqlSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDmsEndpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDmsEndpoint"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            SybaseSettings=SybaseSettings._deserialize(json_data.get("SybaseSettings")),
            RedisSettings=RedisSettings._deserialize(json_data.get("RedisSettings")),
            OracleSettings=OracleSettings._deserialize(json_data.get("OracleSettings")),
            KafkaSettings=KafkaSettings._deserialize(json_data.get("KafkaSettings")),
            Port=json_data.get("Port"),
            MySqlSettings=MySqlSettings._deserialize(json_data.get("MySqlSettings")),
            S3Settings=S3Settings._deserialize(json_data.get("S3Settings")),
            ResourceIdentifier=json_data.get("ResourceIdentifier"),
            KinesisSettings=KinesisSettings._deserialize(json_data.get("KinesisSettings")),
            SslMode=json_data.get("SslMode"),
            RedshiftSettings=RedshiftSettings._deserialize(json_data.get("RedshiftSettings")),
            EndpointType=json_data.get("EndpointType"),
            Tags=json_data.get("Tags"),
            Password=json_data.get("Password"),
            MongoDbSettings=MongoDbSettings._deserialize(json_data.get("MongoDbSettings")),
            IbmDb2Settings=IbmDb2Settings._deserialize(json_data.get("IbmDb2Settings")),
            KmsKeyId=json_data.get("KmsKeyId"),
            ExternalId=json_data.get("ExternalId"),
            DatabaseName=json_data.get("DatabaseName"),
            NeptuneSettings=NeptuneSettings._deserialize(json_data.get("NeptuneSettings")),
            ElasticsearchSettings=ElasticsearchSettings._deserialize(json_data.get("ElasticsearchSettings")),
            EngineName=json_data.get("EngineName"),
            DocDbSettings=DocDbSettings._deserialize(json_data.get("DocDbSettings")),
            DynamoDbSettings=DynamoDbSettings._deserialize(json_data.get("DynamoDbSettings")),
            Username=json_data.get("Username"),
            MicrosoftSqlServerSettings=MicrosoftSqlServerSettings._deserialize(json_data.get("MicrosoftSqlServerSettings")),
            GcpMySQLSettings=GcpMySQLSettings._deserialize(json_data.get("GcpMySQLSettings")),
            ServerName=json_data.get("ServerName"),
            ExtraConnectionAttributes=json_data.get("ExtraConnectionAttributes"),
            Id=json_data.get("Id"),
            EndpointIdentifier=json_data.get("EndpointIdentifier"),
            CertificateArn=json_data.get("CertificateArn"),
            PostgreSqlSettings=PostgreSqlSettings._deserialize(json_data.get("PostgreSqlSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDmsEndpoint = AwsDmsEndpoint


@dataclass
class SybaseSettings(BaseModel):
    SecretsManagerAccessRoleArn: Optional[str]
    SecretsManagerSecretId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SybaseSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SybaseSettings"]:
        if not json_data:
            return None
        return cls(
            SecretsManagerAccessRoleArn=json_data.get("SecretsManagerAccessRoleArn"),
            SecretsManagerSecretId=json_data.get("SecretsManagerSecretId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SybaseSettings = SybaseSettings


@dataclass
class RedisSettings(BaseModel):
    SslSecurityProtocol: Optional[str]
    AuthUserName: Optional[str]
    ServerName: Optional[str]
    Port: Optional[float]
    SslCaCertificateArn: Optional[str]
    AuthPassword: Optional[str]
    AuthType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedisSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedisSettings"]:
        if not json_data:
            return None
        return cls(
            SslSecurityProtocol=json_data.get("SslSecurityProtocol"),
            AuthUserName=json_data.get("AuthUserName"),
            ServerName=json_data.get("ServerName"),
            Port=json_data.get("Port"),
            SslCaCertificateArn=json_data.get("SslCaCertificateArn"),
            AuthPassword=json_data.get("AuthPassword"),
            AuthType=json_data.get("AuthType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedisSettings = RedisSettings


@dataclass
class OracleSettings(BaseModel):
    AsmPassword: Optional[str]
    DirectPathParallelLoad: Optional[bool]
    AdditionalArchivedLogDestId: Optional[int]
    SpatialDataOptionToGeoJsonFunctionName: Optional[str]
    ReplacePathPrefix: Optional[bool]
    FailTasksOnLobTruncation: Optional[bool]
    AsmServer: Optional[str]
    SecretsManagerOracleAsmAccessRoleArn: Optional[str]
    OraclePathPrefix: Optional[str]
    ReadAheadBlocks: Optional[int]
    StandbyDelayTime: Optional[int]
    AllowSelectNestedTables: Optional[bool]
    AddSupplementalLogging: Optional[bool]
    SecretsManagerSecretId: Optional[str]
    UseBFile: Optional[bool]
    EnableHomogenousTablespace: Optional[bool]
    AsmUser: Optional[str]
    UseDirectPathFullLoad: Optional[bool]
    SecurityDbEncryption: Optional[str]
    ParallelAsmReadThreads: Optional[int]
    ArchivedLogDestId: Optional[int]
    UsePathPrefix: Optional[str]
    UseLogminerReader: Optional[bool]
    SecurityDbEncryptionName: Optional[str]
    DirectPathNoLog: Optional[bool]
    SecretsManagerOracleAsmSecretId: Optional[str]
    CharLengthSemantics: Optional[str]
    NumberDatatypeScale: Optional[int]
    ReadTableSpaceName: Optional[bool]
    AccessAlternateDirectly: Optional[bool]
    UseAlternateFolderForOnline: Optional[bool]
    ArchivedLogsOnly: Optional[bool]
    ExtraArchivedLogDestIds: Optional[Sequence[int]]
    RetryInterval: Optional[int]
    SecretsManagerAccessRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OracleSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OracleSettings"]:
        if not json_data:
            return None
        return cls(
            AsmPassword=json_data.get("AsmPassword"),
            DirectPathParallelLoad=json_data.get("DirectPathParallelLoad"),
            AdditionalArchivedLogDestId=json_data.get("AdditionalArchivedLogDestId"),
            SpatialDataOptionToGeoJsonFunctionName=json_data.get("SpatialDataOptionToGeoJsonFunctionName"),
            ReplacePathPrefix=json_data.get("ReplacePathPrefix"),
            FailTasksOnLobTruncation=json_data.get("FailTasksOnLobTruncation"),
            AsmServer=json_data.get("AsmServer"),
            SecretsManagerOracleAsmAccessRoleArn=json_data.get("SecretsManagerOracleAsmAccessRoleArn"),
            OraclePathPrefix=json_data.get("OraclePathPrefix"),
            ReadAheadBlocks=json_data.get("ReadAheadBlocks"),
            StandbyDelayTime=json_data.get("StandbyDelayTime"),
            AllowSelectNestedTables=json_data.get("AllowSelectNestedTables"),
            AddSupplementalLogging=json_data.get("AddSupplementalLogging"),
            SecretsManagerSecretId=json_data.get("SecretsManagerSecretId"),
            UseBFile=json_data.get("UseBFile"),
            EnableHomogenousTablespace=json_data.get("EnableHomogenousTablespace"),
            AsmUser=json_data.get("AsmUser"),
            UseDirectPathFullLoad=json_data.get("UseDirectPathFullLoad"),
            SecurityDbEncryption=json_data.get("SecurityDbEncryption"),
            ParallelAsmReadThreads=json_data.get("ParallelAsmReadThreads"),
            ArchivedLogDestId=json_data.get("ArchivedLogDestId"),
            UsePathPrefix=json_data.get("UsePathPrefix"),
            UseLogminerReader=json_data.get("UseLogminerReader"),
            SecurityDbEncryptionName=json_data.get("SecurityDbEncryptionName"),
            DirectPathNoLog=json_data.get("DirectPathNoLog"),
            SecretsManagerOracleAsmSecretId=json_data.get("SecretsManagerOracleAsmSecretId"),
            CharLengthSemantics=json_data.get("CharLengthSemantics"),
            NumberDatatypeScale=json_data.get("NumberDatatypeScale"),
            ReadTableSpaceName=json_data.get("ReadTableSpaceName"),
            AccessAlternateDirectly=json_data.get("AccessAlternateDirectly"),
            UseAlternateFolderForOnline=json_data.get("UseAlternateFolderForOnline"),
            ArchivedLogsOnly=json_data.get("ArchivedLogsOnly"),
            ExtraArchivedLogDestIds=json_data.get("ExtraArchivedLogDestIds"),
            RetryInterval=json_data.get("RetryInterval"),
            SecretsManagerAccessRoleArn=json_data.get("SecretsManagerAccessRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OracleSettings = OracleSettings


@dataclass
class KafkaSettings(BaseModel):
    Broker: Optional[str]
    SaslPassword: Optional[str]
    MessageFormat: Optional[str]
    SslClientCertificateArn: Optional[str]
    IncludeTransactionDetails: Optional[bool]
    SecurityProtocol: Optional[str]
    IncludeTableAlterOperations: Optional[bool]
    SslCaCertificateArn: Optional[str]
    IncludeControlDetails: Optional[bool]
    IncludePartitionValue: Optional[bool]
    NoHexPrefix: Optional[bool]
    SslClientKeyArn: Optional[str]
    SslClientKeyPassword: Optional[str]
    SaslUserName: Optional[str]
    MessageMaxBytes: Optional[int]
    Topic: Optional[str]
    PartitionIncludeSchemaTable: Optional[bool]
    IncludeNullAndEmpty: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_KafkaSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KafkaSettings"]:
        if not json_data:
            return None
        return cls(
            Broker=json_data.get("Broker"),
            SaslPassword=json_data.get("SaslPassword"),
            MessageFormat=json_data.get("MessageFormat"),
            SslClientCertificateArn=json_data.get("SslClientCertificateArn"),
            IncludeTransactionDetails=json_data.get("IncludeTransactionDetails"),
            SecurityProtocol=json_data.get("SecurityProtocol"),
            IncludeTableAlterOperations=json_data.get("IncludeTableAlterOperations"),
            SslCaCertificateArn=json_data.get("SslCaCertificateArn"),
            IncludeControlDetails=json_data.get("IncludeControlDetails"),
            IncludePartitionValue=json_data.get("IncludePartitionValue"),
            NoHexPrefix=json_data.get("NoHexPrefix"),
            SslClientKeyArn=json_data.get("SslClientKeyArn"),
            SslClientKeyPassword=json_data.get("SslClientKeyPassword"),
            SaslUserName=json_data.get("SaslUserName"),
            MessageMaxBytes=json_data.get("MessageMaxBytes"),
            Topic=json_data.get("Topic"),
            PartitionIncludeSchemaTable=json_data.get("PartitionIncludeSchemaTable"),
            IncludeNullAndEmpty=json_data.get("IncludeNullAndEmpty"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KafkaSettings = KafkaSettings


@dataclass
class MySqlSettings(BaseModel):
    ServerTimezone: Optional[str]
    EventsPollInterval: Optional[int]
    ParallelLoadThreads: Optional[int]
    AfterConnectScript: Optional[str]
    MaxFileSize: Optional[int]
    TargetDbType: Optional[str]
    SecretsManagerSecretId: Optional[str]
    SecretsManagerAccessRoleArn: Optional[str]
    CleanSourceMetadataOnMismatch: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_MySqlSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MySqlSettings"]:
        if not json_data:
            return None
        return cls(
            ServerTimezone=json_data.get("ServerTimezone"),
            EventsPollInterval=json_data.get("EventsPollInterval"),
            ParallelLoadThreads=json_data.get("ParallelLoadThreads"),
            AfterConnectScript=json_data.get("AfterConnectScript"),
            MaxFileSize=json_data.get("MaxFileSize"),
            TargetDbType=json_data.get("TargetDbType"),
            SecretsManagerSecretId=json_data.get("SecretsManagerSecretId"),
            SecretsManagerAccessRoleArn=json_data.get("SecretsManagerAccessRoleArn"),
            CleanSourceMetadataOnMismatch=json_data.get("CleanSourceMetadataOnMismatch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MySqlSettings = MySqlSettings


@dataclass
class S3Settings(BaseModel):
    TimestampColumnName: Optional[str]
    EnableStatistics: Optional[bool]
    DatePartitionSequence: Optional[str]
    IncludeOpForFullLoad: Optional[bool]
    CsvNullValue: Optional[str]
    CdcInsertsAndUpdates: Optional[bool]
    BucketName: Optional[str]
    ServerSideEncryptionKmsKeyId: Optional[str]
    UseTaskStartTimeForFullLoadTimestamp: Optional[bool]
    DataFormat: Optional[str]
    CsvDelimiter: Optional[str]
    IgnoreHeaderRows: Optional[int]
    CannedAclForObjects: Optional[str]
    Rfc4180: Optional[bool]
    ServiceAccessRoleArn: Optional[str]
    ParquetTimestampInMillisecond: Optional[bool]
    PreserveTransactions: Optional[bool]
    BucketFolder: Optional[str]
    DatePartitionDelimiter: Optional[str]
    EncodingType: Optional[str]
    ParquetVersion: Optional[str]
    AddColumnName: Optional[bool]
    CdcMinFileSize: Optional[int]
    ExternalTableDefinition: Optional[str]
    UseCsvNoSupValue: Optional[bool]
    MaxFileSize: Optional[int]
    CsvNoSupValue: Optional[str]
    CdcPath: Optional[str]
    CsvRowDelimiter: Optional[str]
    RowGroupLength: Optional[int]
    CdcMaxBatchInterval: Optional[int]
    DataPageSize: Optional[int]
    DictPageSizeLimit: Optional[int]
    DatePartitionEnabled: Optional[bool]
    CompressionType: Optional[str]
    DatePartitionTimezone: Optional[str]
    CdcInsertsOnly: Optional[bool]
    EncryptionMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Settings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Settings"]:
        if not json_data:
            return None
        return cls(
            TimestampColumnName=json_data.get("TimestampColumnName"),
            EnableStatistics=json_data.get("EnableStatistics"),
            DatePartitionSequence=json_data.get("DatePartitionSequence"),
            IncludeOpForFullLoad=json_data.get("IncludeOpForFullLoad"),
            CsvNullValue=json_data.get("CsvNullValue"),
            CdcInsertsAndUpdates=json_data.get("CdcInsertsAndUpdates"),
            BucketName=json_data.get("BucketName"),
            ServerSideEncryptionKmsKeyId=json_data.get("ServerSideEncryptionKmsKeyId"),
            UseTaskStartTimeForFullLoadTimestamp=json_data.get("UseTaskStartTimeForFullLoadTimestamp"),
            DataFormat=json_data.get("DataFormat"),
            CsvDelimiter=json_data.get("CsvDelimiter"),
            IgnoreHeaderRows=json_data.get("IgnoreHeaderRows"),
            CannedAclForObjects=json_data.get("CannedAclForObjects"),
            Rfc4180=json_data.get("Rfc4180"),
            ServiceAccessRoleArn=json_data.get("ServiceAccessRoleArn"),
            ParquetTimestampInMillisecond=json_data.get("ParquetTimestampInMillisecond"),
            PreserveTransactions=json_data.get("PreserveTransactions"),
            BucketFolder=json_data.get("BucketFolder"),
            DatePartitionDelimiter=json_data.get("DatePartitionDelimiter"),
            EncodingType=json_data.get("EncodingType"),
            ParquetVersion=json_data.get("ParquetVersion"),
            AddColumnName=json_data.get("AddColumnName"),
            CdcMinFileSize=json_data.get("CdcMinFileSize"),
            ExternalTableDefinition=json_data.get("ExternalTableDefinition"),
            UseCsvNoSupValue=json_data.get("UseCsvNoSupValue"),
            MaxFileSize=json_data.get("MaxFileSize"),
            CsvNoSupValue=json_data.get("CsvNoSupValue"),
            CdcPath=json_data.get("CdcPath"),
            CsvRowDelimiter=json_data.get("CsvRowDelimiter"),
            RowGroupLength=json_data.get("RowGroupLength"),
            CdcMaxBatchInterval=json_data.get("CdcMaxBatchInterval"),
            DataPageSize=json_data.get("DataPageSize"),
            DictPageSizeLimit=json_data.get("DictPageSizeLimit"),
            DatePartitionEnabled=json_data.get("DatePartitionEnabled"),
            CompressionType=json_data.get("CompressionType"),
            DatePartitionTimezone=json_data.get("DatePartitionTimezone"),
            CdcInsertsOnly=json_data.get("CdcInsertsOnly"),
            EncryptionMode=json_data.get("EncryptionMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Settings = S3Settings


@dataclass
class KinesisSettings(BaseModel):
    MessageFormat: Optional[str]
    IncludeTransactionDetails: Optional[bool]
    IncludeTableAlterOperations: Optional[bool]
    IncludeControlDetails: Optional[bool]
    IncludePartitionValue: Optional[bool]
    StreamArn: Optional[str]
    ServiceAccessRoleArn: Optional[str]
    NoHexPrefix: Optional[bool]
    PartitionIncludeSchemaTable: Optional[bool]
    IncludeNullAndEmpty: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisSettings"]:
        if not json_data:
            return None
        return cls(
            MessageFormat=json_data.get("MessageFormat"),
            IncludeTransactionDetails=json_data.get("IncludeTransactionDetails"),
            IncludeTableAlterOperations=json_data.get("IncludeTableAlterOperations"),
            IncludeControlDetails=json_data.get("IncludeControlDetails"),
            IncludePartitionValue=json_data.get("IncludePartitionValue"),
            StreamArn=json_data.get("StreamArn"),
            ServiceAccessRoleArn=json_data.get("ServiceAccessRoleArn"),
            NoHexPrefix=json_data.get("NoHexPrefix"),
            PartitionIncludeSchemaTable=json_data.get("PartitionIncludeSchemaTable"),
            IncludeNullAndEmpty=json_data.get("IncludeNullAndEmpty"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisSettings = KinesisSettings


@dataclass
class RedshiftSettings(BaseModel):
    ConnectionTimeout: Optional[int]
    MapBooleanAsBoolean: Optional[bool]
    AfterConnectScript: Optional[str]
    FileTransferUploadStreams: Optional[int]
    BucketName: Optional[str]
    ServerSideEncryptionKmsKeyId: Optional[str]
    ExplicitIds: Optional[bool]
    SecretsManagerSecretId: Optional[str]
    TruncateColumns: Optional[bool]
    ServiceAccessRoleArn: Optional[str]
    ReplaceChars: Optional[str]
    TimeFormat: Optional[str]
    BucketFolder: Optional[str]
    ReplaceInvalidChars: Optional[str]
    RemoveQuotes: Optional[bool]
    LoadTimeout: Optional[int]
    MaxFileSize: Optional[int]
    TrimBlanks: Optional[bool]
    DateFormat: Optional[str]
    CompUpdate: Optional[bool]
    AcceptAnyDate: Optional[bool]
    WriteBufferSize: Optional[int]
    SecretsManagerAccessRoleArn: Optional[str]
    CaseSensitiveNames: Optional[bool]
    EmptyAsNull: Optional[bool]
    EncryptionMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedshiftSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedshiftSettings"]:
        if not json_data:
            return None
        return cls(
            ConnectionTimeout=json_data.get("ConnectionTimeout"),
            MapBooleanAsBoolean=json_data.get("MapBooleanAsBoolean"),
            AfterConnectScript=json_data.get("AfterConnectScript"),
            FileTransferUploadStreams=json_data.get("FileTransferUploadStreams"),
            BucketName=json_data.get("BucketName"),
            ServerSideEncryptionKmsKeyId=json_data.get("ServerSideEncryptionKmsKeyId"),
            ExplicitIds=json_data.get("ExplicitIds"),
            SecretsManagerSecretId=json_data.get("SecretsManagerSecretId"),
            TruncateColumns=json_data.get("TruncateColumns"),
            ServiceAccessRoleArn=json_data.get("ServiceAccessRoleArn"),
            ReplaceChars=json_data.get("ReplaceChars"),
            TimeFormat=json_data.get("TimeFormat"),
            BucketFolder=json_data.get("BucketFolder"),
            ReplaceInvalidChars=json_data.get("ReplaceInvalidChars"),
            RemoveQuotes=json_data.get("RemoveQuotes"),
            LoadTimeout=json_data.get("LoadTimeout"),
            MaxFileSize=json_data.get("MaxFileSize"),
            TrimBlanks=json_data.get("TrimBlanks"),
            DateFormat=json_data.get("DateFormat"),
            CompUpdate=json_data.get("CompUpdate"),
            AcceptAnyDate=json_data.get("AcceptAnyDate"),
            WriteBufferSize=json_data.get("WriteBufferSize"),
            SecretsManagerAccessRoleArn=json_data.get("SecretsManagerAccessRoleArn"),
            CaseSensitiveNames=json_data.get("CaseSensitiveNames"),
            EmptyAsNull=json_data.get("EmptyAsNull"),
            EncryptionMode=json_data.get("EncryptionMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedshiftSettings = RedshiftSettings


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
class MongoDbSettings(BaseModel):
    Port: Optional[int]
    ExtractDocId: Optional[str]
    DatabaseName: Optional[str]
    AuthSource: Optional[str]
    AuthMechanism: Optional[str]
    Username: Optional[str]
    DocsToInvestigate: Optional[str]
    ServerName: Optional[str]
    SecretsManagerSecretId: Optional[str]
    AuthType: Optional[str]
    SecretsManagerAccessRoleArn: Optional[str]
    Password: Optional[str]
    NestingLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MongoDbSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MongoDbSettings"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            ExtractDocId=json_data.get("ExtractDocId"),
            DatabaseName=json_data.get("DatabaseName"),
            AuthSource=json_data.get("AuthSource"),
            AuthMechanism=json_data.get("AuthMechanism"),
            Username=json_data.get("Username"),
            DocsToInvestigate=json_data.get("DocsToInvestigate"),
            ServerName=json_data.get("ServerName"),
            SecretsManagerSecretId=json_data.get("SecretsManagerSecretId"),
            AuthType=json_data.get("AuthType"),
            SecretsManagerAccessRoleArn=json_data.get("SecretsManagerAccessRoleArn"),
            Password=json_data.get("Password"),
            NestingLevel=json_data.get("NestingLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MongoDbSettings = MongoDbSettings


@dataclass
class IbmDb2Settings(BaseModel):
    SecretsManagerSecretId: Optional[str]
    SetDataCaptureChanges: Optional[bool]
    SecretsManagerAccessRoleArn: Optional[str]
    CurrentLsn: Optional[str]
    MaxKBytesPerRead: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_IbmDb2Settings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IbmDb2Settings"]:
        if not json_data:
            return None
        return cls(
            SecretsManagerSecretId=json_data.get("SecretsManagerSecretId"),
            SetDataCaptureChanges=json_data.get("SetDataCaptureChanges"),
            SecretsManagerAccessRoleArn=json_data.get("SecretsManagerAccessRoleArn"),
            CurrentLsn=json_data.get("CurrentLsn"),
            MaxKBytesPerRead=json_data.get("MaxKBytesPerRead"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IbmDb2Settings = IbmDb2Settings


@dataclass
class NeptuneSettings(BaseModel):
    MaxRetryCount: Optional[int]
    MaxFileSize: Optional[int]
    S3BucketFolder: Optional[str]
    ErrorRetryDuration: Optional[int]
    IamAuthEnabled: Optional[bool]
    S3BucketName: Optional[str]
    ServiceAccessRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NeptuneSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NeptuneSettings"]:
        if not json_data:
            return None
        return cls(
            MaxRetryCount=json_data.get("MaxRetryCount"),
            MaxFileSize=json_data.get("MaxFileSize"),
            S3BucketFolder=json_data.get("S3BucketFolder"),
            ErrorRetryDuration=json_data.get("ErrorRetryDuration"),
            IamAuthEnabled=json_data.get("IamAuthEnabled"),
            S3BucketName=json_data.get("S3BucketName"),
            ServiceAccessRoleArn=json_data.get("ServiceAccessRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NeptuneSettings = NeptuneSettings


@dataclass
class ElasticsearchSettings(BaseModel):
    EndpointUri: Optional[str]
    ErrorRetryDuration: Optional[int]
    FullLoadErrorPercentage: Optional[int]
    ServiceAccessRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticsearchSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticsearchSettings"]:
        if not json_data:
            return None
        return cls(
            EndpointUri=json_data.get("EndpointUri"),
            ErrorRetryDuration=json_data.get("ErrorRetryDuration"),
            FullLoadErrorPercentage=json_data.get("FullLoadErrorPercentage"),
            ServiceAccessRoleArn=json_data.get("ServiceAccessRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticsearchSettings = ElasticsearchSettings


@dataclass
class DocDbSettings(BaseModel):
    SecretsManagerSecretId: Optional[str]
    DocsToInvestigate: Optional[int]
    SecretsManagerAccessRoleArn: Optional[str]
    ExtractDocId: Optional[bool]
    NestingLevel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DocDbSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DocDbSettings"]:
        if not json_data:
            return None
        return cls(
            SecretsManagerSecretId=json_data.get("SecretsManagerSecretId"),
            DocsToInvestigate=json_data.get("DocsToInvestigate"),
            SecretsManagerAccessRoleArn=json_data.get("SecretsManagerAccessRoleArn"),
            ExtractDocId=json_data.get("ExtractDocId"),
            NestingLevel=json_data.get("NestingLevel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DocDbSettings = DocDbSettings


@dataclass
class DynamoDbSettings(BaseModel):
    ServiceAccessRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DynamoDbSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamoDbSettings"]:
        if not json_data:
            return None
        return cls(
            ServiceAccessRoleArn=json_data.get("ServiceAccessRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamoDbSettings = DynamoDbSettings


@dataclass
class MicrosoftSqlServerSettings(BaseModel):
    ReadBackupOnly: Optional[bool]
    BcpPacketSize: Optional[int]
    QuerySingleAlwaysOnNode: Optional[bool]
    SafeguardPolicy: Optional[str]
    UseThirdPartyBackupDevice: Optional[bool]
    SecretsManagerSecretId: Optional[str]
    ControlTablesFileGroup: Optional[str]
    SecretsManagerAccessRoleArn: Optional[str]
    UseBcpFullLoad: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_MicrosoftSqlServerSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MicrosoftSqlServerSettings"]:
        if not json_data:
            return None
        return cls(
            ReadBackupOnly=json_data.get("ReadBackupOnly"),
            BcpPacketSize=json_data.get("BcpPacketSize"),
            QuerySingleAlwaysOnNode=json_data.get("QuerySingleAlwaysOnNode"),
            SafeguardPolicy=json_data.get("SafeguardPolicy"),
            UseThirdPartyBackupDevice=json_data.get("UseThirdPartyBackupDevice"),
            SecretsManagerSecretId=json_data.get("SecretsManagerSecretId"),
            ControlTablesFileGroup=json_data.get("ControlTablesFileGroup"),
            SecretsManagerAccessRoleArn=json_data.get("SecretsManagerAccessRoleArn"),
            UseBcpFullLoad=json_data.get("UseBcpFullLoad"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MicrosoftSqlServerSettings = MicrosoftSqlServerSettings


@dataclass
class GcpMySQLSettings(BaseModel):
    AfterConnectScript: Optional[str]
    Port: Optional[int]
    DatabaseName: Optional[str]
    CleanSourceMetadataOnMismatch: Optional[bool]
    ServerTimezone: Optional[str]
    EventsPollInterval: Optional[int]
    ParallelLoadThreads: Optional[int]
    Username: Optional[str]
    MaxFileSize: Optional[int]
    ServerName: Optional[str]
    SecretsManagerSecretId: Optional[str]
    SecretsManagerAccessRoleArn: Optional[str]
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GcpMySQLSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GcpMySQLSettings"]:
        if not json_data:
            return None
        return cls(
            AfterConnectScript=json_data.get("AfterConnectScript"),
            Port=json_data.get("Port"),
            DatabaseName=json_data.get("DatabaseName"),
            CleanSourceMetadataOnMismatch=json_data.get("CleanSourceMetadataOnMismatch"),
            ServerTimezone=json_data.get("ServerTimezone"),
            EventsPollInterval=json_data.get("EventsPollInterval"),
            ParallelLoadThreads=json_data.get("ParallelLoadThreads"),
            Username=json_data.get("Username"),
            MaxFileSize=json_data.get("MaxFileSize"),
            ServerName=json_data.get("ServerName"),
            SecretsManagerSecretId=json_data.get("SecretsManagerSecretId"),
            SecretsManagerAccessRoleArn=json_data.get("SecretsManagerAccessRoleArn"),
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GcpMySQLSettings = GcpMySQLSettings


@dataclass
class PostgreSqlSettings(BaseModel):
    PluginName: Optional[str]
    MapBooleanAsBoolean: Optional[bool]
    AfterConnectScript: Optional[str]
    ExecuteTimeout: Optional[int]
    DdlArtifactsSchema: Optional[str]
    FailTasksOnLobTruncation: Optional[bool]
    HeartbeatEnable: Optional[bool]
    CaptureDdls: Optional[bool]
    MaxFileSize: Optional[int]
    HeartbeatFrequency: Optional[int]
    SecretsManagerSecretId: Optional[str]
    SecretsManagerAccessRoleArn: Optional[str]
    HeartbeatSchema: Optional[str]
    SlotName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PostgreSqlSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PostgreSqlSettings"]:
        if not json_data:
            return None
        return cls(
            PluginName=json_data.get("PluginName"),
            MapBooleanAsBoolean=json_data.get("MapBooleanAsBoolean"),
            AfterConnectScript=json_data.get("AfterConnectScript"),
            ExecuteTimeout=json_data.get("ExecuteTimeout"),
            DdlArtifactsSchema=json_data.get("DdlArtifactsSchema"),
            FailTasksOnLobTruncation=json_data.get("FailTasksOnLobTruncation"),
            HeartbeatEnable=json_data.get("HeartbeatEnable"),
            CaptureDdls=json_data.get("CaptureDdls"),
            MaxFileSize=json_data.get("MaxFileSize"),
            HeartbeatFrequency=json_data.get("HeartbeatFrequency"),
            SecretsManagerSecretId=json_data.get("SecretsManagerSecretId"),
            SecretsManagerAccessRoleArn=json_data.get("SecretsManagerAccessRoleArn"),
            HeartbeatSchema=json_data.get("HeartbeatSchema"),
            SlotName=json_data.get("SlotName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PostgreSqlSettings = PostgreSqlSettings


