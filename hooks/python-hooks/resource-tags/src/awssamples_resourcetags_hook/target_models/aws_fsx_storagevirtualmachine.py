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
class AwsFsxStoragevirtualmachine(BaseModel):
    ResourceARN: Optional[str]
    SvmAdminPassword: Optional[str]
    StorageVirtualMachineId: Optional[str]
    ActiveDirectoryConfiguration: Optional["_ActiveDirectoryConfiguration"]
    RootVolumeSecurityStyle: Optional[str]
    FileSystemId: Optional[str]
    UUID: Optional[str]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsFsxStoragevirtualmachine"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsFsxStoragevirtualmachine"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ResourceARN=json_data.get("ResourceARN"),
            SvmAdminPassword=json_data.get("SvmAdminPassword"),
            StorageVirtualMachineId=json_data.get("StorageVirtualMachineId"),
            ActiveDirectoryConfiguration=ActiveDirectoryConfiguration._deserialize(json_data.get("ActiveDirectoryConfiguration")),
            RootVolumeSecurityStyle=json_data.get("RootVolumeSecurityStyle"),
            FileSystemId=json_data.get("FileSystemId"),
            UUID=json_data.get("UUID"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsFsxStoragevirtualmachine = AwsFsxStoragevirtualmachine


@dataclass
class ActiveDirectoryConfiguration(BaseModel):
    SelfManagedActiveDirectoryConfiguration: Optional["_SelfManagedActiveDirectoryConfiguration"]
    NetBiosName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActiveDirectoryConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActiveDirectoryConfiguration"]:
        if not json_data:
            return None
        return cls(
            SelfManagedActiveDirectoryConfiguration=SelfManagedActiveDirectoryConfiguration._deserialize(json_data.get("SelfManagedActiveDirectoryConfiguration")),
            NetBiosName=json_data.get("NetBiosName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActiveDirectoryConfiguration = ActiveDirectoryConfiguration


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


