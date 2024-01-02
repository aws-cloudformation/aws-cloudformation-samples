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
class AwsDmsDataprovider(BaseModel):
    DataProviderName: Optional[str]
    DataProviderIdentifier: Optional[str]
    DataProviderArn: Optional[str]
    DataProviderCreationTime: Optional[str]
    Description: Optional[str]
    Engine: Optional[str]
    ExactSettings: Optional[bool]
    Settings: Optional["_Settings"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDmsDataprovider"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDmsDataprovider"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DataProviderName=json_data.get("DataProviderName"),
            DataProviderIdentifier=json_data.get("DataProviderIdentifier"),
            DataProviderArn=json_data.get("DataProviderArn"),
            DataProviderCreationTime=json_data.get("DataProviderCreationTime"),
            Description=json_data.get("Description"),
            Engine=json_data.get("Engine"),
            ExactSettings=json_data.get("ExactSettings"),
            Settings=Settings._deserialize(json_data.get("Settings")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDmsDataprovider = AwsDmsDataprovider


@dataclass
class Settings(BaseModel):
    PostgreSqlSettings: Optional["_PostgreSqlSettings"]
    MySqlSettings: Optional["_MySqlSettings"]
    OracleSettings: Optional["_OracleSettings"]
    MicrosoftSqlServerSettings: Optional["_MicrosoftSqlServerSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_Settings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Settings"]:
        if not json_data:
            return None
        return cls(
            PostgreSqlSettings=PostgreSqlSettings._deserialize(json_data.get("PostgreSqlSettings")),
            MySqlSettings=MySqlSettings._deserialize(json_data.get("MySqlSettings")),
            OracleSettings=OracleSettings._deserialize(json_data.get("OracleSettings")),
            MicrosoftSqlServerSettings=MicrosoftSqlServerSettings._deserialize(json_data.get("MicrosoftSqlServerSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Settings = Settings


@dataclass
class PostgreSqlSettings(BaseModel):
    ServerName: Optional[str]
    Port: Optional[int]
    DatabaseName: Optional[str]
    SslMode: Optional[str]
    CertificateArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PostgreSqlSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PostgreSqlSettings"]:
        if not json_data:
            return None
        return cls(
            ServerName=json_data.get("ServerName"),
            Port=json_data.get("Port"),
            DatabaseName=json_data.get("DatabaseName"),
            SslMode=json_data.get("SslMode"),
            CertificateArn=json_data.get("CertificateArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PostgreSqlSettings = PostgreSqlSettings


@dataclass
class MySqlSettings(BaseModel):
    ServerName: Optional[str]
    Port: Optional[int]
    SslMode: Optional[str]
    CertificateArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MySqlSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MySqlSettings"]:
        if not json_data:
            return None
        return cls(
            ServerName=json_data.get("ServerName"),
            Port=json_data.get("Port"),
            SslMode=json_data.get("SslMode"),
            CertificateArn=json_data.get("CertificateArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MySqlSettings = MySqlSettings


@dataclass
class OracleSettings(BaseModel):
    ServerName: Optional[str]
    Port: Optional[int]
    DatabaseName: Optional[str]
    SslMode: Optional[str]
    CertificateArn: Optional[str]
    AsmServer: Optional[str]
    SecretsManagerOracleAsmSecretId: Optional[str]
    SecretsManagerOracleAsmAccessRoleArn: Optional[str]
    SecretsManagerSecurityDbEncryptionSecretId: Optional[str]
    SecretsManagerSecurityDbEncryptionAccessRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OracleSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OracleSettings"]:
        if not json_data:
            return None
        return cls(
            ServerName=json_data.get("ServerName"),
            Port=json_data.get("Port"),
            DatabaseName=json_data.get("DatabaseName"),
            SslMode=json_data.get("SslMode"),
            CertificateArn=json_data.get("CertificateArn"),
            AsmServer=json_data.get("AsmServer"),
            SecretsManagerOracleAsmSecretId=json_data.get("SecretsManagerOracleAsmSecretId"),
            SecretsManagerOracleAsmAccessRoleArn=json_data.get("SecretsManagerOracleAsmAccessRoleArn"),
            SecretsManagerSecurityDbEncryptionSecretId=json_data.get("SecretsManagerSecurityDbEncryptionSecretId"),
            SecretsManagerSecurityDbEncryptionAccessRoleArn=json_data.get("SecretsManagerSecurityDbEncryptionAccessRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OracleSettings = OracleSettings


@dataclass
class MicrosoftSqlServerSettings(BaseModel):
    ServerName: Optional[str]
    Port: Optional[int]
    DatabaseName: Optional[str]
    SslMode: Optional[str]
    CertificateArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MicrosoftSqlServerSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MicrosoftSqlServerSettings"]:
        if not json_data:
            return None
        return cls(
            ServerName=json_data.get("ServerName"),
            Port=json_data.get("Port"),
            DatabaseName=json_data.get("DatabaseName"),
            SslMode=json_data.get("SslMode"),
            CertificateArn=json_data.get("CertificateArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MicrosoftSqlServerSettings = MicrosoftSqlServerSettings


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


