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
class AwsCassandraTable(BaseModel):
    KeyspaceName: Optional[str]
    TableName: Optional[str]
    RegularColumns: Optional[AbstractSet["_Column"]]
    PartitionKeyColumns: Optional[Sequence["_Column"]]
    ClusteringKeyColumns: Optional[Sequence["_ClusteringKeyColumn"]]
    BillingMode: Optional["_BillingMode"]
    PointInTimeRecoveryEnabled: Optional[bool]
    ClientSideTimestampsEnabled: Optional[bool]
    Tags: Optional[Any]
    DefaultTimeToLive: Optional[int]
    EncryptionSpecification: Optional["_EncryptionSpecification"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCassandraTable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCassandraTable"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            KeyspaceName=json_data.get("KeyspaceName"),
            TableName=json_data.get("TableName"),
            RegularColumns=set_or_none(json_data.get("RegularColumns")),
            PartitionKeyColumns=deserialize_list(json_data.get("PartitionKeyColumns"), Column),
            ClusteringKeyColumns=deserialize_list(json_data.get("ClusteringKeyColumns"), ClusteringKeyColumn),
            BillingMode=BillingMode._deserialize(json_data.get("BillingMode")),
            PointInTimeRecoveryEnabled=json_data.get("PointInTimeRecoveryEnabled"),
            ClientSideTimestampsEnabled=json_data.get("ClientSideTimestampsEnabled"),
            Tags=json_data.get("Tags"),
            DefaultTimeToLive=json_data.get("DefaultTimeToLive"),
            EncryptionSpecification=EncryptionSpecification._deserialize(json_data.get("EncryptionSpecification")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCassandraTable = AwsCassandraTable


@dataclass
class Column(BaseModel):
    ColumnName: Optional[str]
    ColumnType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Column"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Column"]:
        if not json_data:
            return None
        return cls(
            ColumnName=json_data.get("ColumnName"),
            ColumnType=json_data.get("ColumnType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Column = Column


@dataclass
class ClusteringKeyColumn(BaseModel):
    Column: Optional["_Column"]
    OrderBy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusteringKeyColumn"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusteringKeyColumn"]:
        if not json_data:
            return None
        return cls(
            Column=Column._deserialize(json_data.get("Column")),
            OrderBy=json_data.get("OrderBy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusteringKeyColumn = ClusteringKeyColumn


@dataclass
class BillingMode(BaseModel):
    Mode: Optional[str]
    ProvisionedThroughput: Optional["_ProvisionedThroughput"]

    @classmethod
    def _deserialize(
        cls: Type["_BillingMode"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BillingMode"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
            ProvisionedThroughput=ProvisionedThroughput._deserialize(json_data.get("ProvisionedThroughput")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BillingMode = BillingMode


@dataclass
class ProvisionedThroughput(BaseModel):
    ReadCapacityUnits: Optional[int]
    WriteCapacityUnits: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ProvisionedThroughput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProvisionedThroughput"]:
        if not json_data:
            return None
        return cls(
            ReadCapacityUnits=json_data.get("ReadCapacityUnits"),
            WriteCapacityUnits=json_data.get("WriteCapacityUnits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProvisionedThroughput = ProvisionedThroughput


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
class EncryptionSpecification(BaseModel):
    EncryptionType: Optional[str]
    KmsKeyIdentifier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionSpecification"]:
        if not json_data:
            return None
        return cls(
            EncryptionType=json_data.get("EncryptionType"),
            KmsKeyIdentifier=json_data.get("KmsKeyIdentifier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionSpecification = EncryptionSpecification


