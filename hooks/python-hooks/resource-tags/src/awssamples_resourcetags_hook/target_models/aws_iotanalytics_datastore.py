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
class AwsIotanalyticsDatastore(BaseModel):
    DatastoreStorage: Optional["_DatastoreStorage"]
    DatastoreName: Optional[str]
    DatastorePartitions: Optional["_DatastorePartitions"]
    Id: Optional[str]
    FileFormatConfiguration: Optional["_FileFormatConfiguration"]
    RetentionPeriod: Optional["_RetentionPeriod"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotanalyticsDatastore"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotanalyticsDatastore"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DatastoreStorage=DatastoreStorage._deserialize(json_data.get("DatastoreStorage")),
            DatastoreName=json_data.get("DatastoreName"),
            DatastorePartitions=DatastorePartitions._deserialize(json_data.get("DatastorePartitions")),
            Id=json_data.get("Id"),
            FileFormatConfiguration=FileFormatConfiguration._deserialize(json_data.get("FileFormatConfiguration")),
            RetentionPeriod=RetentionPeriod._deserialize(json_data.get("RetentionPeriod")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotanalyticsDatastore = AwsIotanalyticsDatastore


@dataclass
class DatastoreStorage(BaseModel):
    ServiceManagedS3: Optional[MutableMapping[str, Any]]
    CustomerManagedS3: Optional["_CustomerManagedS3"]
    IotSiteWiseMultiLayerStorage: Optional["_IotSiteWiseMultiLayerStorage"]

    @classmethod
    def _deserialize(
        cls: Type["_DatastoreStorage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatastoreStorage"]:
        if not json_data:
            return None
        return cls(
            ServiceManagedS3=json_data.get("ServiceManagedS3"),
            CustomerManagedS3=CustomerManagedS3._deserialize(json_data.get("CustomerManagedS3")),
            IotSiteWiseMultiLayerStorage=IotSiteWiseMultiLayerStorage._deserialize(json_data.get("IotSiteWiseMultiLayerStorage")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatastoreStorage = DatastoreStorage


@dataclass
class CustomerManagedS3(BaseModel):
    Bucket: Optional[str]
    RoleArn: Optional[str]
    KeyPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomerManagedS3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomerManagedS3"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            RoleArn=json_data.get("RoleArn"),
            KeyPrefix=json_data.get("KeyPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomerManagedS3 = CustomerManagedS3


@dataclass
class IotSiteWiseMultiLayerStorage(BaseModel):
    CustomerManagedS3Storage: Optional["_CustomerManagedS3Storage"]

    @classmethod
    def _deserialize(
        cls: Type["_IotSiteWiseMultiLayerStorage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IotSiteWiseMultiLayerStorage"]:
        if not json_data:
            return None
        return cls(
            CustomerManagedS3Storage=CustomerManagedS3Storage._deserialize(json_data.get("CustomerManagedS3Storage")),
        )


# work around possible type aliasing issues when variable has same name as a model
_IotSiteWiseMultiLayerStorage = IotSiteWiseMultiLayerStorage


@dataclass
class CustomerManagedS3Storage(BaseModel):
    Bucket: Optional[str]
    KeyPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomerManagedS3Storage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomerManagedS3Storage"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            KeyPrefix=json_data.get("KeyPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomerManagedS3Storage = CustomerManagedS3Storage


@dataclass
class DatastorePartitions(BaseModel):
    Partitions: Optional[Sequence["_DatastorePartition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DatastorePartitions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatastorePartitions"]:
        if not json_data:
            return None
        return cls(
            Partitions=deserialize_list(json_data.get("Partitions"), DatastorePartition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatastorePartitions = DatastorePartitions


@dataclass
class DatastorePartition(BaseModel):
    Partition: Optional["_Partition"]
    TimestampPartition: Optional["_TimestampPartition"]

    @classmethod
    def _deserialize(
        cls: Type["_DatastorePartition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatastorePartition"]:
        if not json_data:
            return None
        return cls(
            Partition=Partition._deserialize(json_data.get("Partition")),
            TimestampPartition=TimestampPartition._deserialize(json_data.get("TimestampPartition")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatastorePartition = DatastorePartition


@dataclass
class Partition(BaseModel):
    AttributeName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Partition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Partition"]:
        if not json_data:
            return None
        return cls(
            AttributeName=json_data.get("AttributeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Partition = Partition


@dataclass
class TimestampPartition(BaseModel):
    AttributeName: Optional[str]
    TimestampFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimestampPartition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimestampPartition"]:
        if not json_data:
            return None
        return cls(
            AttributeName=json_data.get("AttributeName"),
            TimestampFormat=json_data.get("TimestampFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimestampPartition = TimestampPartition


@dataclass
class FileFormatConfiguration(BaseModel):
    JsonConfiguration: Optional[MutableMapping[str, Any]]
    ParquetConfiguration: Optional["_ParquetConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_FileFormatConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileFormatConfiguration"]:
        if not json_data:
            return None
        return cls(
            JsonConfiguration=json_data.get("JsonConfiguration"),
            ParquetConfiguration=ParquetConfiguration._deserialize(json_data.get("ParquetConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileFormatConfiguration = FileFormatConfiguration


@dataclass
class ParquetConfiguration(BaseModel):
    SchemaDefinition: Optional["_SchemaDefinition"]

    @classmethod
    def _deserialize(
        cls: Type["_ParquetConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParquetConfiguration"]:
        if not json_data:
            return None
        return cls(
            SchemaDefinition=SchemaDefinition._deserialize(json_data.get("SchemaDefinition")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParquetConfiguration = ParquetConfiguration


@dataclass
class SchemaDefinition(BaseModel):
    Columns: Optional[Sequence["_Column"]]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaDefinition"]:
        if not json_data:
            return None
        return cls(
            Columns=deserialize_list(json_data.get("Columns"), Column),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaDefinition = SchemaDefinition


@dataclass
class Column(BaseModel):
    Type: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Column"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Column"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Column = Column


@dataclass
class RetentionPeriod(BaseModel):
    NumberOfDays: Optional[int]
    Unlimited: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionPeriod"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionPeriod"]:
        if not json_data:
            return None
        return cls(
            NumberOfDays=json_data.get("NumberOfDays"),
            Unlimited=json_data.get("Unlimited"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionPeriod = RetentionPeriod


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


