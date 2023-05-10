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
class AwsCodestarnotificationsNotificationrule(BaseModel):
    EventTypeId: Optional[str]
    CreatedBy: Optional[str]
    TargetAddress: Optional[str]
    EventTypeIds: Optional[Sequence[str]]
    Status: Optional[str]
    DetailType: Optional[str]
    Resource: Optional[str]
    Targets: Optional[Sequence["_Target"]]
    Tags: Optional[Any]
    Name: Optional[str]
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCodestarnotificationsNotificationrule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCodestarnotificationsNotificationrule"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            EventTypeId=json_data.get("EventTypeId"),
            CreatedBy=json_data.get("CreatedBy"),
            TargetAddress=json_data.get("TargetAddress"),
            EventTypeIds=json_data.get("EventTypeIds"),
            Status=json_data.get("Status"),
            DetailType=json_data.get("DetailType"),
            Resource=json_data.get("Resource"),
            Targets=deserialize_list(json_data.get("Targets"), Target),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCodestarnotificationsNotificationrule = AwsCodestarnotificationsNotificationrule


@dataclass
class Target(BaseModel):
    TargetType: Optional[str]
    TargetAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Target"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Target"]:
        if not json_data:
            return None
        return cls(
            TargetType=json_data.get("TargetType"),
            TargetAddress=json_data.get("TargetAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Target = Target


