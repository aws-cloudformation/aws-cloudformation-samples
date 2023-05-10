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
class AwsRedshiftserverlessNamespace(BaseModel):
    AdminUserPassword: Optional[str]
    AdminUsername: Optional[str]
    DbName: Optional[str]
    DefaultIamRoleArn: Optional[str]
    IamRoles: Optional[Sequence[str]]
    KmsKeyId: Optional[str]
    LogExports: Optional[Sequence[str]]
    Namespace: Optional["_Namespace"]
    NamespaceName: Optional[str]
    Tags: Optional[Any]
    FinalSnapshotName: Optional[str]
    FinalSnapshotRetentionPeriod: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRedshiftserverlessNamespace"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRedshiftserverlessNamespace"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AdminUserPassword=json_data.get("AdminUserPassword"),
            AdminUsername=json_data.get("AdminUsername"),
            DbName=json_data.get("DbName"),
            DefaultIamRoleArn=json_data.get("DefaultIamRoleArn"),
            IamRoles=json_data.get("IamRoles"),
            KmsKeyId=json_data.get("KmsKeyId"),
            LogExports=json_data.get("LogExports"),
            Namespace=Namespace._deserialize(json_data.get("Namespace")),
            NamespaceName=json_data.get("NamespaceName"),
            Tags=json_data.get("Tags"),
            FinalSnapshotName=json_data.get("FinalSnapshotName"),
            FinalSnapshotRetentionPeriod=json_data.get("FinalSnapshotRetentionPeriod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRedshiftserverlessNamespace = AwsRedshiftserverlessNamespace


@dataclass
class Namespace(BaseModel):
    NamespaceArn: Optional[str]
    NamespaceId: Optional[str]
    NamespaceName: Optional[str]
    AdminUsername: Optional[str]
    DbName: Optional[str]
    KmsKeyId: Optional[str]
    DefaultIamRoleArn: Optional[str]
    IamRoles: Optional[Sequence[str]]
    LogExports: Optional[Sequence[str]]
    Status: Optional[str]
    CreationDate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Namespace"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Namespace"]:
        if not json_data:
            return None
        return cls(
            NamespaceArn=json_data.get("NamespaceArn"),
            NamespaceId=json_data.get("NamespaceId"),
            NamespaceName=json_data.get("NamespaceName"),
            AdminUsername=json_data.get("AdminUsername"),
            DbName=json_data.get("DbName"),
            KmsKeyId=json_data.get("KmsKeyId"),
            DefaultIamRoleArn=json_data.get("DefaultIamRoleArn"),
            IamRoles=json_data.get("IamRoles"),
            LogExports=json_data.get("LogExports"),
            Status=json_data.get("Status"),
            CreationDate=json_data.get("CreationDate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Namespace = Namespace


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


