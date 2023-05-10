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
class AwsEc2Ipamresourcediscoveryassociation(BaseModel):
    IpamArn: Optional[str]
    IpamRegion: Optional[str]
    IpamResourceDiscoveryAssociationId: Optional[str]
    IpamResourceDiscoveryId: Optional[str]
    IpamId: Optional[str]
    IpamResourceDiscoveryAssociationArn: Optional[str]
    IsDefault: Optional[bool]
    OwnerId: Optional[str]
    State: Optional[str]
    ResourceDiscoveryStatus: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Ipamresourcediscoveryassociation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Ipamresourcediscoveryassociation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            IpamArn=json_data.get("IpamArn"),
            IpamRegion=json_data.get("IpamRegion"),
            IpamResourceDiscoveryAssociationId=json_data.get("IpamResourceDiscoveryAssociationId"),
            IpamResourceDiscoveryId=json_data.get("IpamResourceDiscoveryId"),
            IpamId=json_data.get("IpamId"),
            IpamResourceDiscoveryAssociationArn=json_data.get("IpamResourceDiscoveryAssociationArn"),
            IsDefault=json_data.get("IsDefault"),
            OwnerId=json_data.get("OwnerId"),
            State=json_data.get("State"),
            ResourceDiscoveryStatus=json_data.get("ResourceDiscoveryStatus"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Ipamresourcediscoveryassociation = AwsEc2Ipamresourcediscoveryassociation


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


