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
class AwsVpclatticeListener(BaseModel):
    Arn: Optional[str]
    DefaultAction: Optional["_DefaultAction"]
    Id: Optional[str]
    Name: Optional[str]
    Port: Optional[int]
    Protocol: Optional[str]
    ServiceArn: Optional[str]
    ServiceId: Optional[str]
    ServiceIdentifier: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsVpclatticeListener"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsVpclatticeListener"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            DefaultAction=DefaultAction._deserialize(json_data.get("DefaultAction")),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            ServiceArn=json_data.get("ServiceArn"),
            ServiceId=json_data.get("ServiceId"),
            ServiceIdentifier=json_data.get("ServiceIdentifier"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsVpclatticeListener = AwsVpclatticeListener


@dataclass
class DefaultAction(BaseModel):
    Forward: Optional["_Forward"]
    FixedResponse: Optional["_FixedResponse"]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultAction"]:
        if not json_data:
            return None
        return cls(
            Forward=Forward._deserialize(json_data.get("Forward")),
            FixedResponse=FixedResponse._deserialize(json_data.get("FixedResponse")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultAction = DefaultAction


@dataclass
class Forward(BaseModel):
    TargetGroups: Optional[Sequence["_WeightedTargetGroup"]]

    @classmethod
    def _deserialize(
        cls: Type["_Forward"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Forward"]:
        if not json_data:
            return None
        return cls(
            TargetGroups=deserialize_list(json_data.get("TargetGroups"), WeightedTargetGroup),
        )


# work around possible type aliasing issues when variable has same name as a model
_Forward = Forward


@dataclass
class WeightedTargetGroup(BaseModel):
    TargetGroupIdentifier: Optional[str]
    Weight: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_WeightedTargetGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WeightedTargetGroup"]:
        if not json_data:
            return None
        return cls(
            TargetGroupIdentifier=json_data.get("TargetGroupIdentifier"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WeightedTargetGroup = WeightedTargetGroup


@dataclass
class FixedResponse(BaseModel):
    StatusCode: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_FixedResponse"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FixedResponse"]:
        if not json_data:
            return None
        return cls(
            StatusCode=json_data.get("StatusCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FixedResponse = FixedResponse


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


