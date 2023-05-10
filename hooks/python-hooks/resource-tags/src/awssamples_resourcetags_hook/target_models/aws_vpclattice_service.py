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
class AwsVpclatticeService(BaseModel):
    Arn: Optional[str]
    AuthType: Optional[str]
    CreatedAt: Optional[str]
    DnsEntry: Optional["_DnsEntry"]
    Id: Optional[str]
    LastUpdatedAt: Optional[str]
    Name: Optional[str]
    Status: Optional[str]
    CertificateArn: Optional[str]
    CustomDomainName: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsVpclatticeService"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsVpclatticeService"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            AuthType=json_data.get("AuthType"),
            CreatedAt=json_data.get("CreatedAt"),
            DnsEntry=DnsEntry._deserialize(json_data.get("DnsEntry")),
            Id=json_data.get("Id"),
            LastUpdatedAt=json_data.get("LastUpdatedAt"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            CertificateArn=json_data.get("CertificateArn"),
            CustomDomainName=json_data.get("CustomDomainName"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsVpclatticeService = AwsVpclatticeService


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


