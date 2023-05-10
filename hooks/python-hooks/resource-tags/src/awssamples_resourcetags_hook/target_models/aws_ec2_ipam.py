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
class AwsEc2Ipam(BaseModel):
    IpamId: Optional[str]
    Arn: Optional[str]
    DefaultResourceDiscoveryId: Optional[str]
    DefaultResourceDiscoveryAssociationId: Optional[str]
    ResourceDiscoveryAssociationCount: Optional[int]
    Description: Optional[str]
    PublicDefaultScopeId: Optional[str]
    PrivateDefaultScopeId: Optional[str]
    ScopeCount: Optional[int]
    OperatingRegions: Optional[AbstractSet["_IpamOperatingRegion"]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Ipam"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Ipam"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            IpamId=json_data.get("IpamId"),
            Arn=json_data.get("Arn"),
            DefaultResourceDiscoveryId=json_data.get("DefaultResourceDiscoveryId"),
            DefaultResourceDiscoveryAssociationId=json_data.get("DefaultResourceDiscoveryAssociationId"),
            ResourceDiscoveryAssociationCount=json_data.get("ResourceDiscoveryAssociationCount"),
            Description=json_data.get("Description"),
            PublicDefaultScopeId=json_data.get("PublicDefaultScopeId"),
            PrivateDefaultScopeId=json_data.get("PrivateDefaultScopeId"),
            ScopeCount=json_data.get("ScopeCount"),
            OperatingRegions=set_or_none(json_data.get("OperatingRegions")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Ipam = AwsEc2Ipam


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


