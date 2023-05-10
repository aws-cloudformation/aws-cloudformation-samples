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
class AwsOrganizationsAccount(BaseModel):
    AccountName: Optional[str]
    Email: Optional[str]
    RoleName: Optional[str]
    ParentIds: Optional[AbstractSet[str]]
    Tags: Optional[Any]
    AccountId: Optional[str]
    Arn: Optional[str]
    JoinedMethod: Optional[str]
    JoinedTimestamp: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsOrganizationsAccount"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsOrganizationsAccount"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AccountName=json_data.get("AccountName"),
            Email=json_data.get("Email"),
            RoleName=json_data.get("RoleName"),
            ParentIds=set_or_none(json_data.get("ParentIds")),
            Tags=json_data.get("Tags"),
            AccountId=json_data.get("AccountId"),
            Arn=json_data.get("Arn"),
            JoinedMethod=json_data.get("JoinedMethod"),
            JoinedTimestamp=json_data.get("JoinedTimestamp"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsOrganizationsAccount = AwsOrganizationsAccount


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


