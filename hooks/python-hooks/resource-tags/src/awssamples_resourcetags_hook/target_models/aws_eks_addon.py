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
class AwsEksAddon(BaseModel):
    ClusterName: Optional[str]
    AddonName: Optional[str]
    AddonVersion: Optional[str]
    PreserveOnDelete: Optional[bool]
    ResolveConflicts: Optional[str]
    ServiceAccountRoleArn: Optional[str]
    ConfigurationValues: Optional[str]
    Arn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEksAddon"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEksAddon"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ClusterName=json_data.get("ClusterName"),
            AddonName=json_data.get("AddonName"),
            AddonVersion=json_data.get("AddonVersion"),
            PreserveOnDelete=json_data.get("PreserveOnDelete"),
            ResolveConflicts=json_data.get("ResolveConflicts"),
            ServiceAccountRoleArn=json_data.get("ServiceAccountRoleArn"),
            ConfigurationValues=json_data.get("ConfigurationValues"),
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEksAddon = AwsEksAddon


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


