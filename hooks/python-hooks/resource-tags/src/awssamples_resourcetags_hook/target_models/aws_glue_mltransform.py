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
class AwsGlueMltransform(BaseModel):
    MaxRetries: Optional[int]
    Description: Optional[str]
    TransformEncryption: Optional["_TransformEncryption"]
    Timeout: Optional[int]
    Name: Optional[str]
    Role: Optional[str]
    WorkerType: Optional[str]
    GlueVersion: Optional[str]
    TransformParameters: Optional["_TransformParameters"]
    Id: Optional[str]
    InputRecordTables: Optional["_InputRecordTables"]
    NumberOfWorkers: Optional[int]
    Tags: Optional[Any]
    MaxCapacity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGlueMltransform"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGlueMltransform"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            MaxRetries=json_data.get("MaxRetries"),
            Description=json_data.get("Description"),
            TransformEncryption=TransformEncryption._deserialize(json_data.get("TransformEncryption")),
            Timeout=json_data.get("Timeout"),
            Name=json_data.get("Name"),
            Role=json_data.get("Role"),
            WorkerType=json_data.get("WorkerType"),
            GlueVersion=json_data.get("GlueVersion"),
            TransformParameters=TransformParameters._deserialize(json_data.get("TransformParameters")),
            Id=json_data.get("Id"),
            InputRecordTables=InputRecordTables._deserialize(json_data.get("InputRecordTables")),
            NumberOfWorkers=json_data.get("NumberOfWorkers"),
            Tags=json_data.get("Tags"),
            MaxCapacity=json_data.get("MaxCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGlueMltransform = AwsGlueMltransform


@dataclass
class TransformEncryption(BaseModel):
    TaskRunSecurityConfigurationName: Optional[str]
    MLUserDataEncryption: Optional["_MLUserDataEncryption"]

    @classmethod
    def _deserialize(
        cls: Type["_TransformEncryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransformEncryption"]:
        if not json_data:
            return None
        return cls(
            TaskRunSecurityConfigurationName=json_data.get("TaskRunSecurityConfigurationName"),
            MLUserDataEncryption=MLUserDataEncryption._deserialize(json_data.get("MLUserDataEncryption")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransformEncryption = TransformEncryption


@dataclass
class MLUserDataEncryption(BaseModel):
    KmsKeyId: Optional[str]
    MLUserDataEncryptionMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MLUserDataEncryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MLUserDataEncryption"]:
        if not json_data:
            return None
        return cls(
            KmsKeyId=json_data.get("KmsKeyId"),
            MLUserDataEncryptionMode=json_data.get("MLUserDataEncryptionMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MLUserDataEncryption = MLUserDataEncryption


@dataclass
class TransformParameters(BaseModel):
    TransformType: Optional[str]
    FindMatchesParameters: Optional["_FindMatchesParameters"]

    @classmethod
    def _deserialize(
        cls: Type["_TransformParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TransformParameters"]:
        if not json_data:
            return None
        return cls(
            TransformType=json_data.get("TransformType"),
            FindMatchesParameters=FindMatchesParameters._deserialize(json_data.get("FindMatchesParameters")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TransformParameters = TransformParameters


@dataclass
class FindMatchesParameters(BaseModel):
    PrecisionRecallTradeoff: Optional[float]
    EnforceProvidedLabels: Optional[bool]
    PrimaryKeyColumnName: Optional[str]
    AccuracyCostTradeoff: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FindMatchesParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FindMatchesParameters"]:
        if not json_data:
            return None
        return cls(
            PrecisionRecallTradeoff=json_data.get("PrecisionRecallTradeoff"),
            EnforceProvidedLabels=json_data.get("EnforceProvidedLabels"),
            PrimaryKeyColumnName=json_data.get("PrimaryKeyColumnName"),
            AccuracyCostTradeoff=json_data.get("AccuracyCostTradeoff"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FindMatchesParameters = FindMatchesParameters


@dataclass
class InputRecordTables(BaseModel):
    GlueTables: Optional[Sequence["_GlueTables"]]

    @classmethod
    def _deserialize(
        cls: Type["_InputRecordTables"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputRecordTables"]:
        if not json_data:
            return None
        return cls(
            GlueTables=deserialize_list(json_data.get("GlueTables"), GlueTables),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputRecordTables = InputRecordTables


@dataclass
class GlueTables(BaseModel):
    ConnectionName: Optional[str]
    DatabaseName: Optional[str]
    TableName: Optional[str]
    CatalogId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GlueTables"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlueTables"]:
        if not json_data:
            return None
        return cls(
            ConnectionName=json_data.get("ConnectionName"),
            DatabaseName=json_data.get("DatabaseName"),
            TableName=json_data.get("TableName"),
            CatalogId=json_data.get("CatalogId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlueTables = GlueTables


