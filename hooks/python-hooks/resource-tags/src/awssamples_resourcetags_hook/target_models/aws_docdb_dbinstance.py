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
class AwsDocdbDbinstance(BaseModel):
    Endpoint: Optional[str]
    DBInstanceClass: Optional[str]
    Port: Optional[str]
    DBClusterIdentifier: Optional[str]
    AvailabilityZone: Optional[str]
    PreferredMaintenanceWindow: Optional[str]
    EnablePerformanceInsights: Optional[bool]
    AutoMinorVersionUpgrade: Optional[bool]
    Id: Optional[str]
    DBInstanceIdentifier: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDocdbDbinstance"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDocdbDbinstance"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Endpoint=json_data.get("Endpoint"),
            DBInstanceClass=json_data.get("DBInstanceClass"),
            Port=json_data.get("Port"),
            DBClusterIdentifier=json_data.get("DBClusterIdentifier"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            PreferredMaintenanceWindow=json_data.get("PreferredMaintenanceWindow"),
            EnablePerformanceInsights=json_data.get("EnablePerformanceInsights"),
            AutoMinorVersionUpgrade=json_data.get("AutoMinorVersionUpgrade"),
            Id=json_data.get("Id"),
            DBInstanceIdentifier=json_data.get("DBInstanceIdentifier"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDocdbDbinstance = AwsDocdbDbinstance


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


