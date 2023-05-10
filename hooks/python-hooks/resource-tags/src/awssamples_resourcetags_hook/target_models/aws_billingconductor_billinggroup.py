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
class AwsBillingconductorBillinggroup(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    Description: Optional[str]
    PrimaryAccountId: Optional[str]
    ComputationPreference: Optional["_ComputationPreference"]
    AccountGrouping: Optional["_AccountGrouping"]
    Size: Optional[int]
    Status: Optional[str]
    StatusReason: Optional[str]
    CreationTime: Optional[int]
    LastModifiedTime: Optional[int]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsBillingconductorBillinggroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsBillingconductorBillinggroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            PrimaryAccountId=json_data.get("PrimaryAccountId"),
            ComputationPreference=ComputationPreference._deserialize(json_data.get("ComputationPreference")),
            AccountGrouping=AccountGrouping._deserialize(json_data.get("AccountGrouping")),
            Size=json_data.get("Size"),
            Status=json_data.get("Status"),
            StatusReason=json_data.get("StatusReason"),
            CreationTime=json_data.get("CreationTime"),
            LastModifiedTime=json_data.get("LastModifiedTime"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsBillingconductorBillinggroup = AwsBillingconductorBillinggroup


@dataclass
class ComputationPreference(BaseModel):
    PricingPlanArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComputationPreference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComputationPreference"]:
        if not json_data:
            return None
        return cls(
            PricingPlanArn=json_data.get("PricingPlanArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComputationPreference = ComputationPreference


@dataclass
class AccountGrouping(BaseModel):
    LinkedAccountIds: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AccountGrouping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccountGrouping"]:
        if not json_data:
            return None
        return cls(
            LinkedAccountIds=set_or_none(json_data.get("LinkedAccountIds")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccountGrouping = AccountGrouping


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


