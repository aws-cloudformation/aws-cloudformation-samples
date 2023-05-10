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
class AwsProtonEnvironmentaccountconnection(BaseModel):
    Arn: Optional[str]
    CodebuildRoleArn: Optional[str]
    ComponentRoleArn: Optional[str]
    EnvironmentAccountId: Optional[str]
    EnvironmentName: Optional[str]
    Id: Optional[str]
    ManagementAccountId: Optional[str]
    RoleArn: Optional[str]
    Status: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsProtonEnvironmentaccountconnection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsProtonEnvironmentaccountconnection"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            CodebuildRoleArn=json_data.get("CodebuildRoleArn"),
            ComponentRoleArn=json_data.get("ComponentRoleArn"),
            EnvironmentAccountId=json_data.get("EnvironmentAccountId"),
            EnvironmentName=json_data.get("EnvironmentName"),
            Id=json_data.get("Id"),
            ManagementAccountId=json_data.get("ManagementAccountId"),
            RoleArn=json_data.get("RoleArn"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsProtonEnvironmentaccountconnection = AwsProtonEnvironmentaccountconnection


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


