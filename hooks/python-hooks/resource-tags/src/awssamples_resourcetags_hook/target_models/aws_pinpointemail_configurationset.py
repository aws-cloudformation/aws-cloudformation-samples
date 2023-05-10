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
class AwsPinpointemailConfigurationset(BaseModel):
    Id: Optional[str]
    SendingOptions: Optional["_SendingOptions"]
    TrackingOptions: Optional["_TrackingOptions"]
    ReputationOptions: Optional["_ReputationOptions"]
    DeliveryOptions: Optional["_DeliveryOptions"]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsPinpointemailConfigurationset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsPinpointemailConfigurationset"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            SendingOptions=SendingOptions._deserialize(json_data.get("SendingOptions")),
            TrackingOptions=TrackingOptions._deserialize(json_data.get("TrackingOptions")),
            ReputationOptions=ReputationOptions._deserialize(json_data.get("ReputationOptions")),
            DeliveryOptions=DeliveryOptions._deserialize(json_data.get("DeliveryOptions")),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsPinpointemailConfigurationset = AwsPinpointemailConfigurationset


@dataclass
class SendingOptions(BaseModel):
    SendingEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SendingOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SendingOptions"]:
        if not json_data:
            return None
        return cls(
            SendingEnabled=json_data.get("SendingEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SendingOptions = SendingOptions


@dataclass
class TrackingOptions(BaseModel):
    CustomRedirectDomain: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrackingOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrackingOptions"]:
        if not json_data:
            return None
        return cls(
            CustomRedirectDomain=json_data.get("CustomRedirectDomain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrackingOptions = TrackingOptions


@dataclass
class ReputationOptions(BaseModel):
    ReputationMetricsEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ReputationOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReputationOptions"]:
        if not json_data:
            return None
        return cls(
            ReputationMetricsEnabled=json_data.get("ReputationMetricsEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReputationOptions = ReputationOptions


@dataclass
class DeliveryOptions(BaseModel):
    SendingPoolName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeliveryOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeliveryOptions"]:
        if not json_data:
            return None
        return cls(
            SendingPoolName=json_data.get("SendingPoolName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeliveryOptions = DeliveryOptions


@dataclass
class Tags(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


