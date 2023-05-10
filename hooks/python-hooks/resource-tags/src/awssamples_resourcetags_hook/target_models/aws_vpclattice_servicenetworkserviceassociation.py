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
class AwsVpclatticeServicenetworkserviceassociation(BaseModel):
    Arn: Optional[str]
    CreatedAt: Optional[str]
    DnsEntry: Optional["_DnsEntry"]
    Id: Optional[str]
    ServiceNetworkArn: Optional[str]
    ServiceNetworkId: Optional[str]
    ServiceNetworkIdentifier: Optional[str]
    ServiceNetworkName: Optional[str]
    ServiceArn: Optional[str]
    ServiceId: Optional[str]
    ServiceIdentifier: Optional[str]
    ServiceName: Optional[str]
    Status: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsVpclatticeServicenetworkserviceassociation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsVpclatticeServicenetworkserviceassociation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            CreatedAt=json_data.get("CreatedAt"),
            DnsEntry=DnsEntry._deserialize(json_data.get("DnsEntry")),
            Id=json_data.get("Id"),
            ServiceNetworkArn=json_data.get("ServiceNetworkArn"),
            ServiceNetworkId=json_data.get("ServiceNetworkId"),
            ServiceNetworkIdentifier=json_data.get("ServiceNetworkIdentifier"),
            ServiceNetworkName=json_data.get("ServiceNetworkName"),
            ServiceArn=json_data.get("ServiceArn"),
            ServiceId=json_data.get("ServiceId"),
            ServiceIdentifier=json_data.get("ServiceIdentifier"),
            ServiceName=json_data.get("ServiceName"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsVpclatticeServicenetworkserviceassociation = AwsVpclatticeServicenetworkserviceassociation


@dataclass
class DnsEntry(BaseModel):
    DomainName: Optional[str]
    HostedZoneId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnsEntry"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsEntry"]:
        if not json_data:
            return None
        return cls(
            DomainName=json_data.get("DomainName"),
            HostedZoneId=json_data.get("HostedZoneId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsEntry = DnsEntry


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


