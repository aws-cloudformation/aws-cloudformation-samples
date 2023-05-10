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
class AwsNeptuneDbinstance(BaseModel):
    Id: Optional[str]
    Endpoint: Optional[str]
    Port: Optional[str]
    DBParameterGroupName: Optional[str]
    DBInstanceClass: Optional[str]
    AllowMajorVersionUpgrade: Optional[bool]
    DBClusterIdentifier: Optional[str]
    AvailabilityZone: Optional[str]
    PreferredMaintenanceWindow: Optional[str]
    AutoMinorVersionUpgrade: Optional[bool]
    DBSubnetGroupName: Optional[str]
    DBInstanceIdentifier: Optional[str]
    DBSnapshotIdentifier: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsNeptuneDbinstance"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsNeptuneDbinstance"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Endpoint=json_data.get("Endpoint"),
            Port=json_data.get("Port"),
            DBParameterGroupName=json_data.get("DBParameterGroupName"),
            DBInstanceClass=json_data.get("DBInstanceClass"),
            AllowMajorVersionUpgrade=json_data.get("AllowMajorVersionUpgrade"),
            DBClusterIdentifier=json_data.get("DBClusterIdentifier"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            PreferredMaintenanceWindow=json_data.get("PreferredMaintenanceWindow"),
            AutoMinorVersionUpgrade=json_data.get("AutoMinorVersionUpgrade"),
            DBSubnetGroupName=json_data.get("DBSubnetGroupName"),
            DBInstanceIdentifier=json_data.get("DBInstanceIdentifier"),
            DBSnapshotIdentifier=json_data.get("DBSnapshotIdentifier"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsNeptuneDbinstance = AwsNeptuneDbinstance


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


