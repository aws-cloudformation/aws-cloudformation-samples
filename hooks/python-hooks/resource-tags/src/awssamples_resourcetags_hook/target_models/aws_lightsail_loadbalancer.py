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
class AwsLightsailLoadbalancer(BaseModel):
    LoadBalancerName: Optional[str]
    LoadBalancerArn: Optional[str]
    InstancePort: Optional[int]
    IpAddressType: Optional[str]
    AttachedInstances: Optional[AbstractSet[str]]
    HealthCheckPath: Optional[str]
    SessionStickinessEnabled: Optional[bool]
    SessionStickinessLBCookieDurationSeconds: Optional[str]
    TlsPolicyName: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLightsailLoadbalancer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLightsailLoadbalancer"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            LoadBalancerName=json_data.get("LoadBalancerName"),
            LoadBalancerArn=json_data.get("LoadBalancerArn"),
            InstancePort=json_data.get("InstancePort"),
            IpAddressType=json_data.get("IpAddressType"),
            AttachedInstances=set_or_none(json_data.get("AttachedInstances")),
            HealthCheckPath=json_data.get("HealthCheckPath"),
            SessionStickinessEnabled=json_data.get("SessionStickinessEnabled"),
            SessionStickinessLBCookieDurationSeconds=json_data.get("SessionStickinessLBCookieDurationSeconds"),
            TlsPolicyName=json_data.get("TlsPolicyName"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLightsailLoadbalancer = AwsLightsailLoadbalancer


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


