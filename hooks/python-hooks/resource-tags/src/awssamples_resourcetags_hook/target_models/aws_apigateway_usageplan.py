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
class AwsApigatewayUsageplan(BaseModel):
    Id: Optional[str]
    ApiStages: Optional[Sequence["_ApiStage"]]
    Description: Optional[str]
    Quota: Optional["_QuotaSettings"]
    Tags: Optional[Any]
    Throttle: Optional["_ThrottleSettings"]
    UsagePlanName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayUsageplan"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayUsageplan"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            ApiStages=deserialize_list(json_data.get("ApiStages"), ApiStage),
            Description=json_data.get("Description"),
            Quota=QuotaSettings._deserialize(json_data.get("Quota")),
            Tags=json_data.get("Tags"),
            Throttle=ThrottleSettings._deserialize(json_data.get("Throttle")),
            UsagePlanName=json_data.get("UsagePlanName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayUsageplan = AwsApigatewayUsageplan


@dataclass
class ApiStage(BaseModel):
    ApiId: Optional[str]
    Stage: Optional[str]
    Throttle: Optional[MutableMapping[str, "_ThrottleSettings"]]

    @classmethod
    def _deserialize(
        cls: Type["_ApiStage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApiStage"]:
        if not json_data:
            return None
        return cls(
            ApiId=json_data.get("ApiId"),
            Stage=json_data.get("Stage"),
            Throttle=json_data.get("Throttle"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApiStage = ApiStage


@dataclass
class ThrottleSettings(BaseModel):
    BurstLimit: Optional[int]
    RateLimit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ThrottleSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThrottleSettings"]:
        if not json_data:
            return None
        return cls(
            BurstLimit=json_data.get("BurstLimit"),
            RateLimit=json_data.get("RateLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThrottleSettings = ThrottleSettings


@dataclass
class QuotaSettings(BaseModel):
    Limit: Optional[int]
    Offset: Optional[int]
    Period: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QuotaSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QuotaSettings"]:
        if not json_data:
            return None
        return cls(
            Limit=json_data.get("Limit"),
            Offset=json_data.get("Offset"),
            Period=json_data.get("Period"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QuotaSettings = QuotaSettings


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


