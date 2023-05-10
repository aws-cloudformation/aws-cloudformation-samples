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
class AwsDatasyncLocationhdfs(BaseModel):
    NameNodes: Optional[Sequence["_NameNode"]]
    BlockSize: Optional[int]
    ReplicationFactor: Optional[int]
    KmsKeyProviderUri: Optional[str]
    QopConfiguration: Optional["_QopConfiguration"]
    AuthenticationType: Optional[str]
    SimpleUser: Optional[str]
    KerberosPrincipal: Optional[str]
    KerberosKeytab: Optional[str]
    KerberosKrb5Conf: Optional[str]
    Tags: Optional[Any]
    AgentArns: Optional[Sequence[str]]
    Subdirectory: Optional[str]
    LocationArn: Optional[str]
    LocationUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDatasyncLocationhdfs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDatasyncLocationhdfs"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            NameNodes=deserialize_list(json_data.get("NameNodes"), NameNode),
            BlockSize=json_data.get("BlockSize"),
            ReplicationFactor=json_data.get("ReplicationFactor"),
            KmsKeyProviderUri=json_data.get("KmsKeyProviderUri"),
            QopConfiguration=QopConfiguration._deserialize(json_data.get("QopConfiguration")),
            AuthenticationType=json_data.get("AuthenticationType"),
            SimpleUser=json_data.get("SimpleUser"),
            KerberosPrincipal=json_data.get("KerberosPrincipal"),
            KerberosKeytab=json_data.get("KerberosKeytab"),
            KerberosKrb5Conf=json_data.get("KerberosKrb5Conf"),
            Tags=json_data.get("Tags"),
            AgentArns=json_data.get("AgentArns"),
            Subdirectory=json_data.get("Subdirectory"),
            LocationArn=json_data.get("LocationArn"),
            LocationUri=json_data.get("LocationUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDatasyncLocationhdfs = AwsDatasyncLocationhdfs


@dataclass
class NameNode(BaseModel):
    Hostname: Optional[str]
    Port: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_NameNode"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NameNode"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NameNode = NameNode


@dataclass
class QopConfiguration(BaseModel):
    RpcProtection: Optional[str]
    DataTransferProtection: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QopConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QopConfiguration"]:
        if not json_data:
            return None
        return cls(
            RpcProtection=json_data.get("RpcProtection"),
            DataTransferProtection=json_data.get("DataTransferProtection"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QopConfiguration = QopConfiguration


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


