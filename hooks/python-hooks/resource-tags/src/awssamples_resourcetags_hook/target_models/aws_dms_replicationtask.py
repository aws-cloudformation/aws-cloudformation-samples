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
class AwsDmsReplicationtask(BaseModel):
    ReplicationTaskSettings: Optional[str]
    CdcStartPosition: Optional[str]
    CdcStopPosition: Optional[str]
    MigrationType: Optional[str]
    TargetEndpointArn: Optional[str]
    ReplicationInstanceArn: Optional[str]
    TaskData: Optional[str]
    CdcStartTime: Optional[float]
    ResourceIdentifier: Optional[str]
    TableMappings: Optional[str]
    ReplicationTaskIdentifier: Optional[str]
    SourceEndpointArn: Optional[str]
    Id: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDmsReplicationtask"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDmsReplicationtask"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ReplicationTaskSettings=json_data.get("ReplicationTaskSettings"),
            CdcStartPosition=json_data.get("CdcStartPosition"),
            CdcStopPosition=json_data.get("CdcStopPosition"),
            MigrationType=json_data.get("MigrationType"),
            TargetEndpointArn=json_data.get("TargetEndpointArn"),
            ReplicationInstanceArn=json_data.get("ReplicationInstanceArn"),
            TaskData=json_data.get("TaskData"),
            CdcStartTime=json_data.get("CdcStartTime"),
            ResourceIdentifier=json_data.get("ResourceIdentifier"),
            TableMappings=json_data.get("TableMappings"),
            ReplicationTaskIdentifier=json_data.get("ReplicationTaskIdentifier"),
            SourceEndpointArn=json_data.get("SourceEndpointArn"),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDmsReplicationtask = AwsDmsReplicationtask


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


