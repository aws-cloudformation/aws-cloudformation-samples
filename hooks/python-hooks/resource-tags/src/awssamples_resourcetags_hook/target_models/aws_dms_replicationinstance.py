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
class AwsDmsReplicationinstance(BaseModel):
    ReplicationInstanceIdentifier: Optional[str]
    EngineVersion: Optional[str]
    KmsKeyId: Optional[str]
    AvailabilityZone: Optional[str]
    PreferredMaintenanceWindow: Optional[str]
    AutoMinorVersionUpgrade: Optional[bool]
    ReplicationSubnetGroupIdentifier: Optional[str]
    ReplicationInstancePrivateIpAddresses: Optional[str]
    AllocatedStorage: Optional[int]
    ResourceIdentifier: Optional[str]
    VpcSecurityGroupIds: Optional[Sequence[str]]
    AllowMajorVersionUpgrade: Optional[bool]
    ReplicationInstanceClass: Optional[str]
    PubliclyAccessible: Optional[bool]
    Id: Optional[str]
    MultiAZ: Optional[bool]
    ReplicationInstancePublicIpAddresses: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDmsReplicationinstance"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDmsReplicationinstance"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ReplicationInstanceIdentifier=json_data.get("ReplicationInstanceIdentifier"),
            EngineVersion=json_data.get("EngineVersion"),
            KmsKeyId=json_data.get("KmsKeyId"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            PreferredMaintenanceWindow=json_data.get("PreferredMaintenanceWindow"),
            AutoMinorVersionUpgrade=json_data.get("AutoMinorVersionUpgrade"),
            ReplicationSubnetGroupIdentifier=json_data.get("ReplicationSubnetGroupIdentifier"),
            ReplicationInstancePrivateIpAddresses=json_data.get("ReplicationInstancePrivateIpAddresses"),
            AllocatedStorage=json_data.get("AllocatedStorage"),
            ResourceIdentifier=json_data.get("ResourceIdentifier"),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
            AllowMajorVersionUpgrade=json_data.get("AllowMajorVersionUpgrade"),
            ReplicationInstanceClass=json_data.get("ReplicationInstanceClass"),
            PubliclyAccessible=json_data.get("PubliclyAccessible"),
            Id=json_data.get("Id"),
            MultiAZ=json_data.get("MultiAZ"),
            ReplicationInstancePublicIpAddresses=json_data.get("ReplicationInstancePublicIpAddresses"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDmsReplicationinstance = AwsDmsReplicationinstance


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


