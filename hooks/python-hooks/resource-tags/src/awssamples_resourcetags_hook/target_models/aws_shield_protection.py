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
class AwsShieldProtection(BaseModel):
    ProtectionId: Optional[str]
    ProtectionArn: Optional[str]
    Name: Optional[str]
    ResourceArn: Optional[str]
    HealthCheckArns: Optional[Sequence[str]]
    ApplicationLayerAutomaticResponseConfiguration: Optional["_ApplicationLayerAutomaticResponseConfiguration"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsShieldProtection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsShieldProtection"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ProtectionId=json_data.get("ProtectionId"),
            ProtectionArn=json_data.get("ProtectionArn"),
            Name=json_data.get("Name"),
            ResourceArn=json_data.get("ResourceArn"),
            HealthCheckArns=json_data.get("HealthCheckArns"),
            ApplicationLayerAutomaticResponseConfiguration=ApplicationLayerAutomaticResponseConfiguration._deserialize(json_data.get("ApplicationLayerAutomaticResponseConfiguration")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsShieldProtection = AwsShieldProtection


@dataclass
class ApplicationLayerAutomaticResponseConfiguration(BaseModel):
    Action: Optional["_Action"]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationLayerAutomaticResponseConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationLayerAutomaticResponseConfiguration"]:
        if not json_data:
            return None
        return cls(
            Action=Action._deserialize(json_data.get("Action")),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationLayerAutomaticResponseConfiguration = ApplicationLayerAutomaticResponseConfiguration


@dataclass
class Action(BaseModel):
    Count: Optional[MutableMapping[str, Any]]
    Block: Optional[MutableMapping[str, Any]]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
            Block=json_data.get("Block"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


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


