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
class AwsQuicksightDatasource(BaseModel):
    AlternateDataSourceParameters: Optional[Sequence["_DataSourceParameters"]]
    Arn: Optional[str]
    AwsAccountId: Optional[str]
    CreatedTime: Optional[str]
    Credentials: Optional["_DataSourceCredentials"]
    DataSourceId: Optional[str]
    DataSourceParameters: Optional["_DataSourceParameters"]
    ErrorInfo: Optional["_DataSourceErrorInfo"]
    LastUpdatedTime: Optional[str]
    Name: Optional[str]
    Permissions: Optional[Sequence["_ResourcePermission"]]
    SslProperties: Optional["_SslProperties"]
    Status: Optional[str]
    Tags: Optional[Any]
    Type: Optional[str]
    VpcConnectionProperties: Optional["_VpcConnectionProperties"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsQuicksightDatasource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsQuicksightDatasource"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AlternateDataSourceParameters=deserialize_list(json_data.get("AlternateDataSourceParameters"), DataSourceParameters),
            Arn=json_data.get("Arn"),
            AwsAccountId=json_data.get("AwsAccountId"),
            CreatedTime=json_data.get("CreatedTime"),
            Credentials=DataSourceCredentials._deserialize(json_data.get("Credentials")),
            DataSourceId=json_data.get("DataSourceId"),
            DataSourceParameters=DataSourceParameters._deserialize(json_data.get("DataSourceParameters")),
            ErrorInfo=DataSourceErrorInfo._deserialize(json_data.get("ErrorInfo")),
            LastUpdatedTime=json_data.get("LastUpdatedTime"),
            Name=json_data.get("Name"),
            Permissions=deserialize_list(json_data.get("Permissions"), ResourcePermission),
            SslProperties=SslProperties._deserialize(json_data.get("SslProperties")),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            VpcConnectionProperties=VpcConnectionProperties._deserialize(json_data.get("VpcConnectionProperties")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsQuicksightDatasource = AwsQuicksightDatasource


@dataclass
class DataSourceParameters(BaseModel):
    AuroraPostgreSqlParameters: Optional["_AuroraPostgreSqlParameters"]
    TeradataParameters: Optional["_TeradataParameters"]
    RdsParameters: Optional["_RdsParameters"]
    AthenaParameters: Optional["_AthenaParameters"]
    SparkParameters: Optional["_SparkParameters"]
    MariaDbParameters: Optional["_MariaDbParameters"]
    OracleParameters: Optional["_OracleParameters"]
    PrestoParameters: Optional["_PrestoParameters"]
    RedshiftParameters: Optional["_RedshiftParameters"]
    MySqlParameters: Optional["_MySqlParameters"]
    SqlServerParameters: Optional["_SqlServerParameters"]
    SnowflakeParameters: Optional["_SnowflakeParameters"]
    AmazonElasticsearchParameters: Optional["_AmazonElasticsearchParameters"]
    AmazonOpenSearchParameters: Optional["_AmazonOpenSearchParameters"]
    PostgreSqlParameters: Optional["_PostgreSqlParameters"]
    AuroraParameters: Optional["_AuroraParameters"]
    S3Parameters: Optional["_S3Parameters"]
    DatabricksParameters: Optional["_DatabricksParameters"]

    @classmethod
    def _deserialize(
        cls: Type["_DataSourceParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataSourceParameters"]:
        if not json_data:
            return None
        return cls(
            AuroraPostgreSqlParameters=AuroraPostgreSqlParameters._deserialize(json_data.get("AuroraPostgreSqlParameters")),
            TeradataParameters=TeradataParameters._deserialize(json_data.get("TeradataParameters")),
            RdsParameters=RdsParameters._deserialize(json_data.get("RdsParameters")),
            AthenaParameters=AthenaParameters._deserialize(json_data.get("AthenaParameters")),
            SparkParameters=SparkParameters._deserialize(json_data.get("SparkParameters")),
            MariaDbParameters=MariaDbParameters._deserialize(json_data.get("MariaDbParameters")),
            OracleParameters=OracleParameters._deserialize(json_data.get("OracleParameters")),
            PrestoParameters=PrestoParameters._deserialize(json_data.get("PrestoParameters")),
            RedshiftParameters=RedshiftParameters._deserialize(json_data.get("RedshiftParameters")),
            MySqlParameters=MySqlParameters._deserialize(json_data.get("MySqlParameters")),
            SqlServerParameters=SqlServerParameters._deserialize(json_data.get("SqlServerParameters")),
            SnowflakeParameters=SnowflakeParameters._deserialize(json_data.get("SnowflakeParameters")),
            AmazonElasticsearchParameters=AmazonElasticsearchParameters._deserialize(json_data.get("AmazonElasticsearchParameters")),
            AmazonOpenSearchParameters=AmazonOpenSearchParameters._deserialize(json_data.get("AmazonOpenSearchParameters")),
            PostgreSqlParameters=PostgreSqlParameters._deserialize(json_data.get("PostgreSqlParameters")),
            AuroraParameters=AuroraParameters._deserialize(json_data.get("AuroraParameters")),
            S3Parameters=S3Parameters._deserialize(json_data.get("S3Parameters")),
            DatabricksParameters=DatabricksParameters._deserialize(json_data.get("DatabricksParameters")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataSourceParameters = DataSourceParameters


@dataclass
class AuroraPostgreSqlParameters(BaseModel):
    Port: Optional[float]
    Database: Optional[str]
    Host: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuroraPostgreSqlParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuroraPostgreSqlParameters"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Database=json_data.get("Database"),
            Host=json_data.get("Host"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuroraPostgreSqlParameters = AuroraPostgreSqlParameters


@dataclass
class TeradataParameters(BaseModel):
    Port: Optional[float]
    Database: Optional[str]
    Host: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TeradataParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TeradataParameters"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Database=json_data.get("Database"),
            Host=json_data.get("Host"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TeradataParameters = TeradataParameters


@dataclass
class RdsParameters(BaseModel):
    InstanceId: Optional[str]
    Database: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RdsParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RdsParameters"]:
        if not json_data:
            return None
        return cls(
            InstanceId=json_data.get("InstanceId"),
            Database=json_data.get("Database"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RdsParameters = RdsParameters


@dataclass
class AthenaParameters(BaseModel):
    WorkGroup: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AthenaParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AthenaParameters"]:
        if not json_data:
            return None
        return cls(
            WorkGroup=json_data.get("WorkGroup"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AthenaParameters = AthenaParameters


@dataclass
class SparkParameters(BaseModel):
    Port: Optional[float]
    Host: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SparkParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SparkParameters"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Host=json_data.get("Host"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SparkParameters = SparkParameters


@dataclass
class MariaDbParameters(BaseModel):
    Port: Optional[float]
    Database: Optional[str]
    Host: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MariaDbParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MariaDbParameters"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Database=json_data.get("Database"),
            Host=json_data.get("Host"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MariaDbParameters = MariaDbParameters


@dataclass
class OracleParameters(BaseModel):
    Port: Optional[float]
    Database: Optional[str]
    Host: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OracleParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OracleParameters"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Database=json_data.get("Database"),
            Host=json_data.get("Host"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OracleParameters = OracleParameters


@dataclass
class PrestoParameters(BaseModel):
    Port: Optional[float]
    Host: Optional[str]
    Catalog: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrestoParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrestoParameters"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Host=json_data.get("Host"),
            Catalog=json_data.get("Catalog"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrestoParameters = PrestoParameters


@dataclass
class RedshiftParameters(BaseModel):
    ClusterId: Optional[str]
    Port: Optional[float]
    Database: Optional[str]
    Host: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedshiftParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedshiftParameters"]:
        if not json_data:
            return None
        return cls(
            ClusterId=json_data.get("ClusterId"),
            Port=json_data.get("Port"),
            Database=json_data.get("Database"),
            Host=json_data.get("Host"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedshiftParameters = RedshiftParameters


@dataclass
class MySqlParameters(BaseModel):
    Port: Optional[float]
    Database: Optional[str]
    Host: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MySqlParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MySqlParameters"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Database=json_data.get("Database"),
            Host=json_data.get("Host"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MySqlParameters = MySqlParameters


@dataclass
class SqlServerParameters(BaseModel):
    Port: Optional[float]
    Database: Optional[str]
    Host: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SqlServerParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SqlServerParameters"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Database=json_data.get("Database"),
            Host=json_data.get("Host"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SqlServerParameters = SqlServerParameters


@dataclass
class SnowflakeParameters(BaseModel):
    Warehouse: Optional[str]
    Database: Optional[str]
    Host: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnowflakeParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnowflakeParameters"]:
        if not json_data:
            return None
        return cls(
            Warehouse=json_data.get("Warehouse"),
            Database=json_data.get("Database"),
            Host=json_data.get("Host"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnowflakeParameters = SnowflakeParameters


@dataclass
class AmazonElasticsearchParameters(BaseModel):
    Domain: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AmazonElasticsearchParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AmazonElasticsearchParameters"]:
        if not json_data:
            return None
        return cls(
            Domain=json_data.get("Domain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AmazonElasticsearchParameters = AmazonElasticsearchParameters


@dataclass
class AmazonOpenSearchParameters(BaseModel):
    Domain: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AmazonOpenSearchParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AmazonOpenSearchParameters"]:
        if not json_data:
            return None
        return cls(
            Domain=json_data.get("Domain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AmazonOpenSearchParameters = AmazonOpenSearchParameters


@dataclass
class PostgreSqlParameters(BaseModel):
    Port: Optional[float]
    Database: Optional[str]
    Host: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PostgreSqlParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PostgreSqlParameters"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Database=json_data.get("Database"),
            Host=json_data.get("Host"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PostgreSqlParameters = PostgreSqlParameters


@dataclass
class AuroraParameters(BaseModel):
    Port: Optional[float]
    Database: Optional[str]
    Host: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuroraParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuroraParameters"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Database=json_data.get("Database"),
            Host=json_data.get("Host"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuroraParameters = AuroraParameters


@dataclass
class S3Parameters(BaseModel):
    ManifestFileLocation: Optional["_ManifestFileLocation"]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Parameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Parameters"]:
        if not json_data:
            return None
        return cls(
            ManifestFileLocation=ManifestFileLocation._deserialize(json_data.get("ManifestFileLocation")),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Parameters = S3Parameters


@dataclass
class ManifestFileLocation(BaseModel):
    Bucket: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ManifestFileLocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManifestFileLocation"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManifestFileLocation = ManifestFileLocation


@dataclass
class DatabricksParameters(BaseModel):
    Host: Optional[str]
    Port: Optional[float]
    SqlEndpointPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatabricksParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatabricksParameters"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Port=json_data.get("Port"),
            SqlEndpointPath=json_data.get("SqlEndpointPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatabricksParameters = DatabricksParameters


@dataclass
class DataSourceCredentials(BaseModel):
    CopySourceArn: Optional[str]
    CredentialPair: Optional["_CredentialPair"]
    SecretArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataSourceCredentials"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataSourceCredentials"]:
        if not json_data:
            return None
        return cls(
            CopySourceArn=json_data.get("CopySourceArn"),
            CredentialPair=CredentialPair._deserialize(json_data.get("CredentialPair")),
            SecretArn=json_data.get("SecretArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataSourceCredentials = DataSourceCredentials


@dataclass
class CredentialPair(BaseModel):
    AlternateDataSourceParameters: Optional[Sequence["_DataSourceParameters"]]
    Username: Optional[str]
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CredentialPair"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CredentialPair"]:
        if not json_data:
            return None
        return cls(
            AlternateDataSourceParameters=deserialize_list(json_data.get("AlternateDataSourceParameters"), DataSourceParameters),
            Username=json_data.get("Username"),
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CredentialPair = CredentialPair


@dataclass
class DataSourceErrorInfo(BaseModel):
    Type: Optional[str]
    Message: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataSourceErrorInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataSourceErrorInfo"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Message=json_data.get("Message"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataSourceErrorInfo = DataSourceErrorInfo


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
class SslProperties(BaseModel):
    DisableSsl: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SslProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslProperties"]:
        if not json_data:
            return None
        return cls(
            DisableSsl=json_data.get("DisableSsl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslProperties = SslProperties


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
class VpcConnectionProperties(BaseModel):
    VpcConnectionArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConnectionProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConnectionProperties"]:
        if not json_data:
            return None
        return cls(
            VpcConnectionArn=json_data.get("VpcConnectionArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConnectionProperties = VpcConnectionProperties


