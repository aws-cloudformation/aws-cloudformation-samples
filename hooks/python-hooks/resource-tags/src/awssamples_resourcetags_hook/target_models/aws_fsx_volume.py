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
class AwsFsxVolume(BaseModel):
    OpenZFSConfiguration: Optional["_OpenZFSConfiguration"]
    ResourceARN: Optional[str]
    VolumeId: Optional[str]
    VolumeType: Optional[str]
    BackupId: Optional[str]
    OntapConfiguration: Optional["_OntapConfiguration"]
    UUID: Optional[str]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsFsxVolume"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsFsxVolume"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            OpenZFSConfiguration=OpenZFSConfiguration._deserialize(json_data.get("OpenZFSConfiguration")),
            ResourceARN=json_data.get("ResourceARN"),
            VolumeId=json_data.get("VolumeId"),
            VolumeType=json_data.get("VolumeType"),
            BackupId=json_data.get("BackupId"),
            OntapConfiguration=OntapConfiguration._deserialize(json_data.get("OntapConfiguration")),
            UUID=json_data.get("UUID"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsFsxVolume = AwsFsxVolume


@dataclass
class OpenZFSConfiguration(BaseModel):
    ReadOnly: Optional[bool]
    Options: Optional[Sequence[str]]
    DataCompressionType: Optional[str]
    NfsExports: Optional[Sequence["_NfsExports"]]
    StorageCapacityQuotaGiB: Optional[int]
    CopyTagsToSnapshots: Optional[bool]
    ParentVolumeId: Optional[str]
    StorageCapacityReservationGiB: Optional[int]
    RecordSizeKiB: Optional[int]
    OriginSnapshot: Optional["_OriginSnapshot"]
    UserAndGroupQuotas: Optional[Sequence["_UserAndGroupQuotas"]]

    @classmethod
    def _deserialize(
        cls: Type["_OpenZFSConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenZFSConfiguration"]:
        if not json_data:
            return None
        return cls(
            ReadOnly=json_data.get("ReadOnly"),
            Options=json_data.get("Options"),
            DataCompressionType=json_data.get("DataCompressionType"),
            NfsExports=deserialize_list(json_data.get("NfsExports"), NfsExports),
            StorageCapacityQuotaGiB=json_data.get("StorageCapacityQuotaGiB"),
            CopyTagsToSnapshots=json_data.get("CopyTagsToSnapshots"),
            ParentVolumeId=json_data.get("ParentVolumeId"),
            StorageCapacityReservationGiB=json_data.get("StorageCapacityReservationGiB"),
            RecordSizeKiB=json_data.get("RecordSizeKiB"),
            OriginSnapshot=OriginSnapshot._deserialize(json_data.get("OriginSnapshot")),
            UserAndGroupQuotas=deserialize_list(json_data.get("UserAndGroupQuotas"), UserAndGroupQuotas),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenZFSConfiguration = OpenZFSConfiguration


@dataclass
class NfsExports(BaseModel):
    ClientConfigurations: Optional[Sequence["_ClientConfigurations"]]

    @classmethod
    def _deserialize(
        cls: Type["_NfsExports"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NfsExports"]:
        if not json_data:
            return None
        return cls(
            ClientConfigurations=deserialize_list(json_data.get("ClientConfigurations"), ClientConfigurations),
        )


# work around possible type aliasing issues when variable has same name as a model
_NfsExports = NfsExports


@dataclass
class ClientConfigurations(BaseModel):
    Clients: Optional[str]
    Options: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientConfigurations"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientConfigurations"]:
        if not json_data:
            return None
        return cls(
            Clients=json_data.get("Clients"),
            Options=json_data.get("Options"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientConfigurations = ClientConfigurations


@dataclass
class OriginSnapshot(BaseModel):
    SnapshotARN: Optional[str]
    CopyStrategy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OriginSnapshot"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginSnapshot"]:
        if not json_data:
            return None
        return cls(
            SnapshotARN=json_data.get("SnapshotARN"),
            CopyStrategy=json_data.get("CopyStrategy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginSnapshot = OriginSnapshot


@dataclass
class UserAndGroupQuotas(BaseModel):
    Type: Optional[str]
    Id: Optional[int]
    StorageCapacityQuotaGiB: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_UserAndGroupQuotas"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserAndGroupQuotas"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Id=json_data.get("Id"),
            StorageCapacityQuotaGiB=json_data.get("StorageCapacityQuotaGiB"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserAndGroupQuotas = UserAndGroupQuotas


@dataclass
class OntapConfiguration(BaseModel):
    JunctionPath: Optional[str]
    StorageVirtualMachineId: Optional[str]
    TieringPolicy: Optional["_TieringPolicy"]
    SizeInMegabytes: Optional[str]
    VolumeStyle: Optional[str]
    SizeInBytes: Optional[str]
    SecurityStyle: Optional[str]
    SnaplockConfiguration: Optional["_SnaplockConfiguration"]
    AggregateConfiguration: Optional["_AggregateConfiguration"]
    SnapshotPolicy: Optional[str]
    StorageEfficiencyEnabled: Optional[str]
    CopyTagsToBackups: Optional[str]
    OntapVolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OntapConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OntapConfiguration"]:
        if not json_data:
            return None
        return cls(
            JunctionPath=json_data.get("JunctionPath"),
            StorageVirtualMachineId=json_data.get("StorageVirtualMachineId"),
            TieringPolicy=TieringPolicy._deserialize(json_data.get("TieringPolicy")),
            SizeInMegabytes=json_data.get("SizeInMegabytes"),
            VolumeStyle=json_data.get("VolumeStyle"),
            SizeInBytes=json_data.get("SizeInBytes"),
            SecurityStyle=json_data.get("SecurityStyle"),
            SnaplockConfiguration=SnaplockConfiguration._deserialize(json_data.get("SnaplockConfiguration")),
            AggregateConfiguration=AggregateConfiguration._deserialize(json_data.get("AggregateConfiguration")),
            SnapshotPolicy=json_data.get("SnapshotPolicy"),
            StorageEfficiencyEnabled=json_data.get("StorageEfficiencyEnabled"),
            CopyTagsToBackups=json_data.get("CopyTagsToBackups"),
            OntapVolumeType=json_data.get("OntapVolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OntapConfiguration = OntapConfiguration


@dataclass
class TieringPolicy(BaseModel):
    CoolingPeriod: Optional[int]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TieringPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TieringPolicy"]:
        if not json_data:
            return None
        return cls(
            CoolingPeriod=json_data.get("CoolingPeriod"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TieringPolicy = TieringPolicy


@dataclass
class SnaplockConfiguration(BaseModel):
    AuditLogVolume: Optional[str]
    VolumeAppendModeEnabled: Optional[str]
    AutocommitPeriod: Optional["_AutocommitPeriod"]
    RetentionPeriod: Optional["_SnaplockRetentionPeriod"]
    PrivilegedDelete: Optional[str]
    SnaplockType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnaplockConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnaplockConfiguration"]:
        if not json_data:
            return None
        return cls(
            AuditLogVolume=json_data.get("AuditLogVolume"),
            VolumeAppendModeEnabled=json_data.get("VolumeAppendModeEnabled"),
            AutocommitPeriod=AutocommitPeriod._deserialize(json_data.get("AutocommitPeriod")),
            RetentionPeriod=SnaplockRetentionPeriod._deserialize(json_data.get("RetentionPeriod")),
            PrivilegedDelete=json_data.get("PrivilegedDelete"),
            SnaplockType=json_data.get("SnaplockType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnaplockConfiguration = SnaplockConfiguration


@dataclass
class AutocommitPeriod(BaseModel):
    Value: Optional[int]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AutocommitPeriod"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutocommitPeriod"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutocommitPeriod = AutocommitPeriod


@dataclass
class SnaplockRetentionPeriod(BaseModel):
    MinimumRetention: Optional["_RetentionPeriod"]
    DefaultRetention: Optional["_RetentionPeriod"]
    MaximumRetention: Optional["_RetentionPeriod"]

    @classmethod
    def _deserialize(
        cls: Type["_SnaplockRetentionPeriod"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnaplockRetentionPeriod"]:
        if not json_data:
            return None
        return cls(
            MinimumRetention=RetentionPeriod._deserialize(json_data.get("MinimumRetention")),
            DefaultRetention=RetentionPeriod._deserialize(json_data.get("DefaultRetention")),
            MaximumRetention=RetentionPeriod._deserialize(json_data.get("MaximumRetention")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnaplockRetentionPeriod = SnaplockRetentionPeriod


@dataclass
class RetentionPeriod(BaseModel):
    Value: Optional[int]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionPeriod"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionPeriod"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionPeriod = RetentionPeriod


@dataclass
class AggregateConfiguration(BaseModel):
    Aggregates: Optional[Sequence[str]]
    ConstituentsPerAggregate: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AggregateConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AggregateConfiguration"]:
        if not json_data:
            return None
        return cls(
            Aggregates=json_data.get("Aggregates"),
            ConstituentsPerAggregate=json_data.get("ConstituentsPerAggregate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AggregateConfiguration = AggregateConfiguration


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


