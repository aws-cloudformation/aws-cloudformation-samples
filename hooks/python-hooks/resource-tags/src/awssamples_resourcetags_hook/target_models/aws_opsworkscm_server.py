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
class AwsOpsworkscmServer(BaseModel):
    KeyPair: Optional[str]
    EngineVersion: Optional[str]
    ServiceRoleArn: Optional[str]
    DisableAutomatedBackup: Optional[bool]
    BackupId: Optional[str]
    EngineModel: Optional[str]
    PreferredMaintenanceWindow: Optional[str]
    AssociatePublicIpAddress: Optional[bool]
    InstanceProfileArn: Optional[str]
    CustomCertificate: Optional[str]
    PreferredBackupWindow: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]
    CustomDomain: Optional[str]
    Endpoint: Optional[str]
    CustomPrivateKey: Optional[str]
    ServerName: Optional[str]
    EngineAttributes: Optional[Sequence["_EngineAttribute"]]
    BackupRetentionCount: Optional[int]
    Arn: Optional[str]
    InstanceType: Optional[str]
    Tags: Optional[Any]
    Engine: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsOpsworkscmServer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsOpsworkscmServer"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            KeyPair=json_data.get("KeyPair"),
            EngineVersion=json_data.get("EngineVersion"),
            ServiceRoleArn=json_data.get("ServiceRoleArn"),
            DisableAutomatedBackup=json_data.get("DisableAutomatedBackup"),
            BackupId=json_data.get("BackupId"),
            EngineModel=json_data.get("EngineModel"),
            PreferredMaintenanceWindow=json_data.get("PreferredMaintenanceWindow"),
            AssociatePublicIpAddress=json_data.get("AssociatePublicIpAddress"),
            InstanceProfileArn=json_data.get("InstanceProfileArn"),
            CustomCertificate=json_data.get("CustomCertificate"),
            PreferredBackupWindow=json_data.get("PreferredBackupWindow"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
            CustomDomain=json_data.get("CustomDomain"),
            Endpoint=json_data.get("Endpoint"),
            CustomPrivateKey=json_data.get("CustomPrivateKey"),
            ServerName=json_data.get("ServerName"),
            EngineAttributes=deserialize_list(json_data.get("EngineAttributes"), EngineAttribute),
            BackupRetentionCount=json_data.get("BackupRetentionCount"),
            Arn=json_data.get("Arn"),
            InstanceType=json_data.get("InstanceType"),
            Tags=json_data.get("Tags"),
            Engine=json_data.get("Engine"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsOpsworkscmServer = AwsOpsworkscmServer


@dataclass
class EngineAttribute(BaseModel):
    Value: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EngineAttribute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EngineAttribute"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EngineAttribute = EngineAttribute


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


