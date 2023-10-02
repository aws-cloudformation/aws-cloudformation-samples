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
class AwsDmsReplicationconfig(BaseModel):
    ReplicationConfigIdentifier: Optional[str]
    ReplicationConfigArn: Optional[str]
    SourceEndpointArn: Optional[str]
    TargetEndpointArn: Optional[str]
    ReplicationType: Optional[str]
    ComputeConfig: Optional["_ComputeConfig"]
    ReplicationSettings: Optional[MutableMapping[str, Any]]
    SupplementalSettings: Optional[MutableMapping[str, Any]]
    ResourceIdentifier: Optional[str]
    TableMappings: Optional[MutableMapping[str, Any]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDmsReplicationconfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDmsReplicationconfig"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ReplicationConfigIdentifier=json_data.get("ReplicationConfigIdentifier"),
            ReplicationConfigArn=json_data.get("ReplicationConfigArn"),
            SourceEndpointArn=json_data.get("SourceEndpointArn"),
            TargetEndpointArn=json_data.get("TargetEndpointArn"),
            ReplicationType=json_data.get("ReplicationType"),
            ComputeConfig=ComputeConfig._deserialize(json_data.get("ComputeConfig")),
            ReplicationSettings=json_data.get("ReplicationSettings"),
            SupplementalSettings=json_data.get("SupplementalSettings"),
            ResourceIdentifier=json_data.get("ResourceIdentifier"),
            TableMappings=json_data.get("TableMappings"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDmsReplicationconfig = AwsDmsReplicationconfig


@dataclass
class ComputeConfig(BaseModel):
    AvailabilityZone: Optional[str]
    DnsNameServers: Optional[str]
    KmsKeyId: Optional[str]
    MaxCapacityUnits: Optional[int]
    MinCapacityUnits: Optional[int]
    MultiAZ: Optional[bool]
    PreferredMaintenanceWindow: Optional[str]
    ReplicationSubnetGroupId: Optional[str]
    VpcSecurityGroupIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ComputeConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComputeConfig"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZone=json_data.get("AvailabilityZone"),
            DnsNameServers=json_data.get("DnsNameServers"),
            KmsKeyId=json_data.get("KmsKeyId"),
            MaxCapacityUnits=json_data.get("MaxCapacityUnits"),
            MinCapacityUnits=json_data.get("MinCapacityUnits"),
            MultiAZ=json_data.get("MultiAZ"),
            PreferredMaintenanceWindow=json_data.get("PreferredMaintenanceWindow"),
            ReplicationSubnetGroupId=json_data.get("ReplicationSubnetGroupId"),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComputeConfig = ComputeConfig


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


