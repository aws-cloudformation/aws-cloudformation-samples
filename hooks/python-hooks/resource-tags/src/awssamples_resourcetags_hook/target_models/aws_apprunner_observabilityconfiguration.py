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
class AwsApprunnerObservabilityconfiguration(BaseModel):
    ObservabilityConfigurationArn: Optional[str]
    ObservabilityConfigurationName: Optional[str]
    ObservabilityConfigurationRevision: Optional[int]
    Latest: Optional[bool]
    TraceConfiguration: Optional["_TraceConfiguration"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApprunnerObservabilityconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApprunnerObservabilityconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ObservabilityConfigurationArn=json_data.get("ObservabilityConfigurationArn"),
            ObservabilityConfigurationName=json_data.get("ObservabilityConfigurationName"),
            ObservabilityConfigurationRevision=json_data.get("ObservabilityConfigurationRevision"),
            Latest=json_data.get("Latest"),
            TraceConfiguration=TraceConfiguration._deserialize(json_data.get("TraceConfiguration")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApprunnerObservabilityconfiguration = AwsApprunnerObservabilityconfiguration


@dataclass
class TraceConfiguration(BaseModel):
    Vendor: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TraceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TraceConfiguration"]:
        if not json_data:
            return None
        return cls(
            Vendor=json_data.get("Vendor"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TraceConfiguration = TraceConfiguration


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


