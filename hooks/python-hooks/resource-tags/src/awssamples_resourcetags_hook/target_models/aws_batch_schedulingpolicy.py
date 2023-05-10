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
class AwsBatchSchedulingpolicy(BaseModel):
    Name: Optional[str]
    Arn: Optional[str]
    FairsharePolicy: Optional["_FairsharePolicy"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsBatchSchedulingpolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsBatchSchedulingpolicy"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Arn=json_data.get("Arn"),
            FairsharePolicy=FairsharePolicy._deserialize(json_data.get("FairsharePolicy")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsBatchSchedulingpolicy = AwsBatchSchedulingpolicy


@dataclass
class FairsharePolicy(BaseModel):
    ShareDecaySeconds: Optional[float]
    ComputeReservation: Optional[float]
    ShareDistribution: Optional[Sequence["_ShareAttributes"]]

    @classmethod
    def _deserialize(
        cls: Type["_FairsharePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FairsharePolicy"]:
        if not json_data:
            return None
        return cls(
            ShareDecaySeconds=json_data.get("ShareDecaySeconds"),
            ComputeReservation=json_data.get("ComputeReservation"),
            ShareDistribution=deserialize_list(json_data.get("ShareDistribution"), ShareAttributes),
        )


# work around possible type aliasing issues when variable has same name as a model
_FairsharePolicy = FairsharePolicy


@dataclass
class ShareAttributes(BaseModel):
    ShareIdentifier: Optional[str]
    WeightFactor: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ShareAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShareAttributes"]:
        if not json_data:
            return None
        return cls(
            ShareIdentifier=json_data.get("ShareIdentifier"),
            WeightFactor=json_data.get("WeightFactor"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShareAttributes = ShareAttributes


