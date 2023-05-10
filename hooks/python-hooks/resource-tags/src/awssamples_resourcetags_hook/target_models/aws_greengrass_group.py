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
class AwsGreengrassGroup(BaseModel):
    RoleAttachedAt: Optional[str]
    LatestVersionArn: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    RoleArn: Optional[str]
    Name: Optional[str]
    InitialVersion: Optional["_GroupVersion"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGreengrassGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGreengrassGroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            RoleAttachedAt=json_data.get("RoleAttachedAt"),
            LatestVersionArn=json_data.get("LatestVersionArn"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            RoleArn=json_data.get("RoleArn"),
            Name=json_data.get("Name"),
            InitialVersion=GroupVersion._deserialize(json_data.get("InitialVersion")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGreengrassGroup = AwsGreengrassGroup


@dataclass
class GroupVersion(BaseModel):
    LoggerDefinitionVersionArn: Optional[str]
    DeviceDefinitionVersionArn: Optional[str]
    FunctionDefinitionVersionArn: Optional[str]
    CoreDefinitionVersionArn: Optional[str]
    ResourceDefinitionVersionArn: Optional[str]
    ConnectorDefinitionVersionArn: Optional[str]
    SubscriptionDefinitionVersionArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GroupVersion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupVersion"]:
        if not json_data:
            return None
        return cls(
            LoggerDefinitionVersionArn=json_data.get("LoggerDefinitionVersionArn"),
            DeviceDefinitionVersionArn=json_data.get("DeviceDefinitionVersionArn"),
            FunctionDefinitionVersionArn=json_data.get("FunctionDefinitionVersionArn"),
            CoreDefinitionVersionArn=json_data.get("CoreDefinitionVersionArn"),
            ResourceDefinitionVersionArn=json_data.get("ResourceDefinitionVersionArn"),
            ConnectorDefinitionVersionArn=json_data.get("ConnectorDefinitionVersionArn"),
            SubscriptionDefinitionVersionArn=json_data.get("SubscriptionDefinitionVersionArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupVersion = GroupVersion


