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
class AwsRoute53recoverycontrolControlpanel(BaseModel):
    ClusterArn: Optional[str]
    ControlPanelArn: Optional[str]
    Name: Optional[str]
    Status: Optional[str]
    DefaultControlPanel: Optional[bool]
    RoutingControlCount: Optional[int]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRoute53recoverycontrolControlpanel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRoute53recoverycontrolControlpanel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ClusterArn=json_data.get("ClusterArn"),
            ControlPanelArn=json_data.get("ControlPanelArn"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            DefaultControlPanel=json_data.get("DefaultControlPanel"),
            RoutingControlCount=json_data.get("RoutingControlCount"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRoute53recoverycontrolControlpanel = AwsRoute53recoverycontrolControlpanel


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


