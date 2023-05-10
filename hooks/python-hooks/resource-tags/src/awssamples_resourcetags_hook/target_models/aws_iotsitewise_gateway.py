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
class AwsIotsitewiseGateway(BaseModel):
    GatewayName: Optional[str]
    GatewayPlatform: Optional["_GatewayPlatform"]
    Tags: Optional[Any]
    GatewayId: Optional[str]
    GatewayCapabilitySummaries: Optional[Sequence["_GatewayCapabilitySummary"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotsitewiseGateway"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotsitewiseGateway"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            GatewayName=json_data.get("GatewayName"),
            GatewayPlatform=GatewayPlatform._deserialize(json_data.get("GatewayPlatform")),
            Tags=json_data.get("Tags"),
            GatewayId=json_data.get("GatewayId"),
            GatewayCapabilitySummaries=deserialize_list(json_data.get("GatewayCapabilitySummaries"), GatewayCapabilitySummary),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotsitewiseGateway = AwsIotsitewiseGateway


@dataclass
class GatewayPlatform(BaseModel):
    Greengrass: Optional["_Greengrass"]
    GreengrassV2: Optional["_GreengrassV2"]

    @classmethod
    def _deserialize(
        cls: Type["_GatewayPlatform"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GatewayPlatform"]:
        if not json_data:
            return None
        return cls(
            Greengrass=Greengrass._deserialize(json_data.get("Greengrass")),
            GreengrassV2=GreengrassV2._deserialize(json_data.get("GreengrassV2")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GatewayPlatform = GatewayPlatform


@dataclass
class Greengrass(BaseModel):
    GroupArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Greengrass"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Greengrass"]:
        if not json_data:
            return None
        return cls(
            GroupArn=json_data.get("GroupArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Greengrass = Greengrass


@dataclass
class GreengrassV2(BaseModel):
    CoreDeviceThingName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GreengrassV2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GreengrassV2"]:
        if not json_data:
            return None
        return cls(
            CoreDeviceThingName=json_data.get("CoreDeviceThingName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GreengrassV2 = GreengrassV2


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


@dataclass
class GatewayCapabilitySummary(BaseModel):
    CapabilityNamespace: Optional[str]
    CapabilityConfiguration: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GatewayCapabilitySummary"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GatewayCapabilitySummary"]:
        if not json_data:
            return None
        return cls(
            CapabilityNamespace=json_data.get("CapabilityNamespace"),
            CapabilityConfiguration=json_data.get("CapabilityConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GatewayCapabilitySummary = GatewayCapabilitySummary


