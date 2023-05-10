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
class AwsEc2Ipamresourcediscovery(BaseModel):
    IpamResourceDiscoveryId: Optional[str]
    OwnerId: Optional[str]
    OperatingRegions: Optional[AbstractSet["_IpamOperatingRegion"]]
    IpamResourceDiscoveryRegion: Optional[str]
    Description: Optional[str]
    IsDefault: Optional[bool]
    IpamResourceDiscoveryArn: Optional[str]
    State: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Ipamresourcediscovery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Ipamresourcediscovery"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            IpamResourceDiscoveryId=json_data.get("IpamResourceDiscoveryId"),
            OwnerId=json_data.get("OwnerId"),
            OperatingRegions=set_or_none(json_data.get("OperatingRegions")),
            IpamResourceDiscoveryRegion=json_data.get("IpamResourceDiscoveryRegion"),
            Description=json_data.get("Description"),
            IsDefault=json_data.get("IsDefault"),
            IpamResourceDiscoveryArn=json_data.get("IpamResourceDiscoveryArn"),
            State=json_data.get("State"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Ipamresourcediscovery = AwsEc2Ipamresourcediscovery


@dataclass
class IpamOperatingRegion(BaseModel):
    RegionName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpamOperatingRegion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpamOperatingRegion"]:
        if not json_data:
            return None
        return cls(
            RegionName=json_data.get("RegionName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpamOperatingRegion = IpamOperatingRegion


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


