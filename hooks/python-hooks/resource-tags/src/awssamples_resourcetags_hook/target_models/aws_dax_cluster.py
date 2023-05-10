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
class AwsDaxCluster(BaseModel):
    SSESpecification: Optional["_SSESpecification"]
    ClusterDiscoveryEndpointURL: Optional[str]
    Description: Optional[str]
    ReplicationFactor: Optional[int]
    ParameterGroupName: Optional[str]
    AvailabilityZones: Optional[Sequence[str]]
    IAMRoleARN: Optional[str]
    SubnetGroupName: Optional[str]
    PreferredMaintenanceWindow: Optional[str]
    ClusterEndpointEncryptionType: Optional[str]
    NotificationTopicARN: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    NodeType: Optional[str]
    ClusterName: Optional[str]
    ClusterDiscoveryEndpoint: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDaxCluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDaxCluster"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            SSESpecification=SSESpecification._deserialize(json_data.get("SSESpecification")),
            ClusterDiscoveryEndpointURL=json_data.get("ClusterDiscoveryEndpointURL"),
            Description=json_data.get("Description"),
            ReplicationFactor=json_data.get("ReplicationFactor"),
            ParameterGroupName=json_data.get("ParameterGroupName"),
            AvailabilityZones=json_data.get("AvailabilityZones"),
            IAMRoleARN=json_data.get("IAMRoleARN"),
            SubnetGroupName=json_data.get("SubnetGroupName"),
            PreferredMaintenanceWindow=json_data.get("PreferredMaintenanceWindow"),
            ClusterEndpointEncryptionType=json_data.get("ClusterEndpointEncryptionType"),
            NotificationTopicARN=json_data.get("NotificationTopicARN"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            NodeType=json_data.get("NodeType"),
            ClusterName=json_data.get("ClusterName"),
            ClusterDiscoveryEndpoint=json_data.get("ClusterDiscoveryEndpoint"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDaxCluster = AwsDaxCluster


@dataclass
class SSESpecification(BaseModel):
    SSEEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SSESpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SSESpecification"]:
        if not json_data:
            return None
        return cls(
            SSEEnabled=json_data.get("SSEEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SSESpecification = SSESpecification


