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
class AwsApprunnerAutoscalingconfiguration(BaseModel):
    AutoScalingConfigurationArn: Optional[str]
    AutoScalingConfigurationName: Optional[str]
    AutoScalingConfigurationRevision: Optional[int]
    MaxConcurrency: Optional[int]
    MaxSize: Optional[int]
    MinSize: Optional[int]
    Latest: Optional[bool]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApprunnerAutoscalingconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApprunnerAutoscalingconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AutoScalingConfigurationArn=json_data.get("AutoScalingConfigurationArn"),
            AutoScalingConfigurationName=json_data.get("AutoScalingConfigurationName"),
            AutoScalingConfigurationRevision=json_data.get("AutoScalingConfigurationRevision"),
            MaxConcurrency=json_data.get("MaxConcurrency"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            Latest=json_data.get("Latest"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApprunnerAutoscalingconfiguration = AwsApprunnerAutoscalingconfiguration


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


