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
class AwsCeAnomalymonitor(BaseModel):
    MonitorArn: Optional[str]
    MonitorType: Optional[str]
    MonitorName: Optional[str]
    CreationDate: Optional[str]
    LastEvaluatedDate: Optional[str]
    LastUpdatedDate: Optional[str]
    MonitorDimension: Optional[str]
    MonitorSpecification: Optional[str]
    DimensionalValueCount: Optional[int]
    ResourceTags: Optional[Sequence["_ResourceTag"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCeAnomalymonitor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCeAnomalymonitor"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            MonitorArn=json_data.get("MonitorArn"),
            MonitorType=json_data.get("MonitorType"),
            MonitorName=json_data.get("MonitorName"),
            CreationDate=json_data.get("CreationDate"),
            LastEvaluatedDate=json_data.get("LastEvaluatedDate"),
            LastUpdatedDate=json_data.get("LastUpdatedDate"),
            MonitorDimension=json_data.get("MonitorDimension"),
            MonitorSpecification=json_data.get("MonitorSpecification"),
            DimensionalValueCount=json_data.get("DimensionalValueCount"),
            ResourceTags=deserialize_list(json_data.get("ResourceTags"), ResourceTag),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCeAnomalymonitor = AwsCeAnomalymonitor


@dataclass
class ResourceTag(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceTag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceTag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceTag = ResourceTag


