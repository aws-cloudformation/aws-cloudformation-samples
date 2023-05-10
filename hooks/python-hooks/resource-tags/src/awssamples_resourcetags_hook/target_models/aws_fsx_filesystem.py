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
class AwsFsxFilesystem(BaseModel):
    StorageType: Optional[str]
    KmsKeyId: Optional[str]
    StorageCapacity: Optional[int]
    RootVolumeId: Optional[str]
    LustreConfiguration: Optional["_LustreConfiguration"]
    BackupId: Optional[str]
    OntapConfiguration: Optional["_OntapConfiguration"]
    DNSName: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    SecurityGroupIds: Optional[Sequence[str]]
    WindowsConfiguration: Optional["_WindowsConfiguration"]
    FileSystemTypeVersion: Optional[str]
    OpenZFSConfiguration: Optional["_OpenZFSConfiguration"]
    ResourceARN: Optional[str]
    FileSystemType: Optional[str]
    Id: Optional[str]
    LustreMountName: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsFsxFilesystem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsFsxFilesystem"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            StorageType=json_data.get("StorageType"),
            KmsKeyId=json_data.get("KmsKeyId"),
            StorageCapacity=json_data.get("StorageCapacity"),
            RootVolumeId=json_data.get("RootVolumeId"),
            LustreConfiguration=LustreConfiguration._deserialize(json_data.get("LustreConfiguration")),
            BackupId=json_data.get("BackupId"),
            OntapConfiguration=OntapConfiguration._deserialize(json_data.get("OntapConfiguration")),
            DNSName=json_data.get("DNSName"),
            SubnetIds=json_data.get("SubnetIds"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            WindowsConfiguration=WindowsConfiguration._deserialize(json_data.get("WindowsConfiguration")),
            FileSystemTypeVersion=json_data.get("FileSystemTypeVersion"),
            OpenZFSConfiguration=OpenZFSConfiguration._deserialize(json_data.get("OpenZFSConfiguration")),
            ResourceARN=json_data.get("ResourceARN"),
            FileSystemType=json_data.get("FileSystemType"),
            Id=json_data.get("Id"),
            LustreMountName=json_data.get("LustreMountName"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsFsxFilesystem = AwsFsxFilesystem


@dataclass
class LustreConfiguration(BaseModel):
    DriveCacheType: Optional[str]
    AutoImportPolicy: Optional[str]
    ImportedFileChunkSize: Optional[int]
    DeploymentType: Optional[str]
    DataCompressionType: Optional[str]
    ImportPath: Optional[str]
    WeeklyMaintenanceStartTime: Optional[str]
    DailyAutomaticBackupStartTime: Optional[str]
    CopyTagsToBackups: Optional[bool]
    ExportPath: Optional[str]
    PerUnitStorageThroughput: Optional[int]
    AutomaticBackupRetentionDays: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_LustreConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LustreConfiguration"]:
        if not json_data:
            return None
        return cls(
            DriveCacheType=json_data.get("DriveCacheType"),
            AutoImportPolicy=json_data.get("AutoImportPolicy"),
            ImportedFileChunkSize=json_data.get("ImportedFileChunkSize"),
            DeploymentType=json_data.get("DeploymentType"),
            DataCompressionType=json_data.get("DataCompressionType"),
            ImportPath=json_data.get("ImportPath"),
            WeeklyMaintenanceStartTime=json_data.get("WeeklyMaintenanceStartTime"),
            DailyAutomaticBackupStartTime=json_data.get("DailyAutomaticBackupStartTime"),
            CopyTagsToBackups=json_data.get("CopyTagsToBackups"),
            ExportPath=json_data.get("ExportPath"),
            PerUnitStorageThroughput=json_data.get("PerUnitStorageThroughput"),
            AutomaticBackupRetentionDays=json_data.get("AutomaticBackupRetentionDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LustreConfiguration = LustreConfiguration


@dataclass
class OntapConfiguration(BaseModel):
    FsxAdminPassword: Optional[str]
    RouteTableIds: Optional[Sequence[str]]
    WeeklyMaintenanceStartTime: Optional[str]
    DiskIopsConfiguration: Optional["_DiskIopsConfiguration"]
    DeploymentType: Optional[str]
    DailyAutomaticBackupStartTime: Optional[str]
    ThroughputCapacity: Optional[int]
    AutomaticBackupRetentionDays: Optional[int]
    EndpointIpAddressRange: Optional[str]
    PreferredSubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OntapConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OntapConfiguration"]:
        if not json_data:
            return None
        return cls(
            FsxAdminPassword=json_data.get("FsxAdminPassword"),
            RouteTableIds=json_data.get("RouteTableIds"),
            WeeklyMaintenanceStartTime=json_data.get("WeeklyMaintenanceStartTime"),
            DiskIopsConfiguration=DiskIopsConfiguration._deserialize(json_data.get("DiskIopsConfiguration")),
            DeploymentType=json_data.get("DeploymentType"),
            DailyAutomaticBackupStartTime=json_data.get("DailyAutomaticBackupStartTime"),
            ThroughputCapacity=json_data.get("ThroughputCapacity"),
            AutomaticBackupRetentionDays=json_data.get("AutomaticBackupRetentionDays"),
            EndpointIpAddressRange=json_data.get("EndpointIpAddressRange"),
            PreferredSubnetId=json_data.get("PreferredSubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OntapConfiguration = OntapConfiguration


@dataclass
class DiskIopsConfiguration(BaseModel):
    Mode: Optional[str]
    Iops: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_DiskIopsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskIopsConfiguration"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
            Iops=json_data.get("Iops"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskIopsConfiguration = DiskIopsConfiguration


@dataclass
class WindowsConfiguration(BaseModel):
    SelfManagedActiveDirectoryConfiguration: Optional["_SelfManagedActiveDirectoryConfiguration"]
    AuditLogConfiguration: Optional["_AuditLogConfiguration"]
    WeeklyMaintenanceStartTime: Optional[str]
    ActiveDirectoryId: Optional[str]
    DeploymentType: Optional[str]
    Aliases: Optional[Sequence[str]]
    ThroughputCapacity: Optional[int]
    CopyTagsToBackups: Optional[bool]
    DailyAutomaticBackupStartTime: Optional[str]
    AutomaticBackupRetentionDays: Optional[int]
    PreferredSubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WindowsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WindowsConfiguration"]:
        if not json_data:
            return None
        return cls(
            SelfManagedActiveDirectoryConfiguration=SelfManagedActiveDirectoryConfiguration._deserialize(json_data.get("SelfManagedActiveDirectoryConfiguration")),
            AuditLogConfiguration=AuditLogConfiguration._deserialize(json_data.get("AuditLogConfiguration")),
            WeeklyMaintenanceStartTime=json_data.get("WeeklyMaintenanceStartTime"),
            ActiveDirectoryId=json_data.get("ActiveDirectoryId"),
            DeploymentType=json_data.get("DeploymentType"),
            Aliases=json_data.get("Aliases"),
            ThroughputCapacity=json_data.get("ThroughputCapacity"),
            CopyTagsToBackups=json_data.get("CopyTagsToBackups"),
            DailyAutomaticBackupStartTime=json_data.get("DailyAutomaticBackupStartTime"),
            AutomaticBackupRetentionDays=json_data.get("AutomaticBackupRetentionDays"),
            PreferredSubnetId=json_data.get("PreferredSubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WindowsConfiguration = WindowsConfiguration


@dataclass
class SelfManagedActiveDirectoryConfiguration(BaseModel):
    FileSystemAdministratorsGroup: Optional[str]
    UserName: Optional[str]
    DomainName: Optional[str]
    OrganizationalUnitDistinguishedName: Optional[str]
    DnsIps: Optional[Sequence[str]]
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SelfManagedActiveDirectoryConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelfManagedActiveDirectoryConfiguration"]:
        if not json_data:
            return None
        return cls(
            FileSystemAdministratorsGroup=json_data.get("FileSystemAdministratorsGroup"),
            UserName=json_data.get("UserName"),
            DomainName=json_data.get("DomainName"),
            OrganizationalUnitDistinguishedName=json_data.get("OrganizationalUnitDistinguishedName"),
            DnsIps=json_data.get("DnsIps"),
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelfManagedActiveDirectoryConfiguration = SelfManagedActiveDirectoryConfiguration


@dataclass
class AuditLogConfiguration(BaseModel):
    FileAccessAuditLogLevel: Optional[str]
    FileShareAccessAuditLogLevel: Optional[str]
    AuditLogDestination: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuditLogConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuditLogConfiguration"]:
        if not json_data:
            return None
        return cls(
            FileAccessAuditLogLevel=json_data.get("FileAccessAuditLogLevel"),
            FileShareAccessAuditLogLevel=json_data.get("FileShareAccessAuditLogLevel"),
            AuditLogDestination=json_data.get("AuditLogDestination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuditLogConfiguration = AuditLogConfiguration


@dataclass
class OpenZFSConfiguration(BaseModel):
    Options: Optional[Sequence[str]]
    WeeklyMaintenanceStartTime: Optional[str]
    DiskIopsConfiguration: Optional["_DiskIopsConfiguration"]
    CopyTagsToVolumes: Optional[bool]
    DeploymentType: Optional[str]
    DailyAutomaticBackupStartTime: Optional[str]
    CopyTagsToBackups: Optional[bool]
    ThroughputCapacity: Optional[int]
    RootVolumeConfiguration: Optional["_RootVolumeConfiguration"]
    AutomaticBackupRetentionDays: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_OpenZFSConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenZFSConfiguration"]:
        if not json_data:
            return None
        return cls(
            Options=json_data.get("Options"),
            WeeklyMaintenanceStartTime=json_data.get("WeeklyMaintenanceStartTime"),
            DiskIopsConfiguration=DiskIopsConfiguration._deserialize(json_data.get("DiskIopsConfiguration")),
            CopyTagsToVolumes=json_data.get("CopyTagsToVolumes"),
            DeploymentType=json_data.get("DeploymentType"),
            DailyAutomaticBackupStartTime=json_data.get("DailyAutomaticBackupStartTime"),
            CopyTagsToBackups=json_data.get("CopyTagsToBackups"),
            ThroughputCapacity=json_data.get("ThroughputCapacity"),
            RootVolumeConfiguration=RootVolumeConfiguration._deserialize(json_data.get("RootVolumeConfiguration")),
            AutomaticBackupRetentionDays=json_data.get("AutomaticBackupRetentionDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenZFSConfiguration = OpenZFSConfiguration


@dataclass
class RootVolumeConfiguration(BaseModel):
    ReadOnly: Optional[bool]
    DataCompressionType: Optional[str]
    NfsExports: Optional[Sequence["_NfsExports"]]
    CopyTagsToSnapshots: Optional[bool]
    RecordSizeKiB: Optional[int]
    UserAndGroupQuotas: Optional[Sequence["_UserAndGroupQuotas"]]

    @classmethod
    def _deserialize(
        cls: Type["_RootVolumeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RootVolumeConfiguration"]:
        if not json_data:
            return None
        return cls(
            ReadOnly=json_data.get("ReadOnly"),
            DataCompressionType=json_data.get("DataCompressionType"),
            NfsExports=deserialize_list(json_data.get("NfsExports"), NfsExports),
            CopyTagsToSnapshots=json_data.get("CopyTagsToSnapshots"),
            RecordSizeKiB=json_data.get("RecordSizeKiB"),
            UserAndGroupQuotas=deserialize_list(json_data.get("UserAndGroupQuotas"), UserAndGroupQuotas),
        )


# work around possible type aliasing issues when variable has same name as a model
_RootVolumeConfiguration = RootVolumeConfiguration


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


