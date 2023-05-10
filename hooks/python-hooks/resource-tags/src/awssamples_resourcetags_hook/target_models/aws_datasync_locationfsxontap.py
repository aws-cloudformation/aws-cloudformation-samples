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
class AwsDatasyncLocationfsxontap(BaseModel):
    StorageVirtualMachineArn: Optional[str]
    FsxFilesystemArn: Optional[str]
    SecurityGroupArns: Optional[Sequence[str]]
    Protocol: Optional["_Protocol"]
    Subdirectory: Optional[str]
    Tags: Optional[Any]
    LocationArn: Optional[str]
    LocationUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDatasyncLocationfsxontap"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDatasyncLocationfsxontap"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            StorageVirtualMachineArn=json_data.get("StorageVirtualMachineArn"),
            FsxFilesystemArn=json_data.get("FsxFilesystemArn"),
            SecurityGroupArns=json_data.get("SecurityGroupArns"),
            Protocol=Protocol._deserialize(json_data.get("Protocol")),
            Subdirectory=json_data.get("Subdirectory"),
            Tags=json_data.get("Tags"),
            LocationArn=json_data.get("LocationArn"),
            LocationUri=json_data.get("LocationUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDatasyncLocationfsxontap = AwsDatasyncLocationfsxontap


@dataclass
class Protocol(BaseModel):
    NFS: Optional["_NFS"]
    SMB: Optional["_SMB"]

    @classmethod
    def _deserialize(
        cls: Type["_Protocol"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Protocol"]:
        if not json_data:
            return None
        return cls(
            NFS=NFS._deserialize(json_data.get("NFS")),
            SMB=SMB._deserialize(json_data.get("SMB")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Protocol = Protocol


@dataclass
class NFS(BaseModel):
    MountOptions: Optional["_NfsMountOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_NFS"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NFS"]:
        if not json_data:
            return None
        return cls(
            MountOptions=NfsMountOptions._deserialize(json_data.get("MountOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NFS = NFS


@dataclass
class NfsMountOptions(BaseModel):
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NfsMountOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NfsMountOptions"]:
        if not json_data:
            return None
        return cls(
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NfsMountOptions = NfsMountOptions


@dataclass
class SMB(BaseModel):
    MountOptions: Optional["_SmbMountOptions"]
    Domain: Optional[str]
    Password: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SMB"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SMB"]:
        if not json_data:
            return None
        return cls(
            MountOptions=SmbMountOptions._deserialize(json_data.get("MountOptions")),
            Domain=json_data.get("Domain"),
            Password=json_data.get("Password"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SMB = SMB


@dataclass
class SmbMountOptions(BaseModel):
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SmbMountOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmbMountOptions"]:
        if not json_data:
            return None
        return cls(
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmbMountOptions = SmbMountOptions


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


