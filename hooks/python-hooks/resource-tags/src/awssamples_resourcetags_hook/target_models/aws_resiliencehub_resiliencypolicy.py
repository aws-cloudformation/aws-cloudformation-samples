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
class AwsResiliencehubResiliencypolicy(BaseModel):
    PolicyName: Optional[str]
    PolicyDescription: Optional[str]
    DataLocationConstraint: Optional[str]
    Tier: Optional[str]
    Policy: Optional[MutableMapping[str, "_FailurePolicy"]]
    PolicyArn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsResiliencehubResiliencypolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsResiliencehubResiliencypolicy"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            PolicyName=json_data.get("PolicyName"),
            PolicyDescription=json_data.get("PolicyDescription"),
            DataLocationConstraint=json_data.get("DataLocationConstraint"),
            Tier=json_data.get("Tier"),
            Policy=json_data.get("Policy"),
            PolicyArn=json_data.get("PolicyArn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsResiliencehubResiliencypolicy = AwsResiliencehubResiliencypolicy


@dataclass
class FailurePolicy(BaseModel):
    RtoInSecs: Optional[int]
    RpoInSecs: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_FailurePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FailurePolicy"]:
        if not json_data:
            return None
        return cls(
            RtoInSecs=json_data.get("RtoInSecs"),
            RpoInSecs=json_data.get("RpoInSecs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FailurePolicy = FailurePolicy


