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
class AwsEc2Ipampool(BaseModel):
    IpamPoolId: Optional[str]
    AddressFamily: Optional[str]
    AllocationMinNetmaskLength: Optional[int]
    AllocationDefaultNetmaskLength: Optional[int]
    AllocationMaxNetmaskLength: Optional[int]
    AllocationResourceTags: Optional[AbstractSet["_Tag"]]
    Arn: Optional[str]
    AutoImport: Optional[bool]
    AwsService: Optional[str]
    Description: Optional[str]
    IpamScopeId: Optional[str]
    IpamScopeArn: Optional[str]
    IpamScopeType: Optional[str]
    IpamArn: Optional[str]
    Locale: Optional[str]
    PoolDepth: Optional[int]
    ProvisionedCidrs: Optional[AbstractSet["_ProvisionedCidr"]]
    PublicIpSource: Optional[str]
    PubliclyAdvertisable: Optional[bool]
    SourceIpamPoolId: Optional[str]
    State: Optional[str]
    StateMessage: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Ipampool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Ipampool"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            IpamPoolId=json_data.get("IpamPoolId"),
            AddressFamily=json_data.get("AddressFamily"),
            AllocationMinNetmaskLength=json_data.get("AllocationMinNetmaskLength"),
            AllocationDefaultNetmaskLength=json_data.get("AllocationDefaultNetmaskLength"),
            AllocationMaxNetmaskLength=json_data.get("AllocationMaxNetmaskLength"),
            AllocationResourceTags=set_or_none(json_data.get("AllocationResourceTags")),
            Arn=json_data.get("Arn"),
            AutoImport=json_data.get("AutoImport"),
            AwsService=json_data.get("AwsService"),
            Description=json_data.get("Description"),
            IpamScopeId=json_data.get("IpamScopeId"),
            IpamScopeArn=json_data.get("IpamScopeArn"),
            IpamScopeType=json_data.get("IpamScopeType"),
            IpamArn=json_data.get("IpamArn"),
            Locale=json_data.get("Locale"),
            PoolDepth=json_data.get("PoolDepth"),
            ProvisionedCidrs=set_or_none(json_data.get("ProvisionedCidrs")),
            PublicIpSource=json_data.get("PublicIpSource"),
            PubliclyAdvertisable=json_data.get("PubliclyAdvertisable"),
            SourceIpamPoolId=json_data.get("SourceIpamPoolId"),
            State=json_data.get("State"),
            StateMessage=json_data.get("StateMessage"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Ipampool = AwsEc2Ipampool


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
class ProvisionedCidr(BaseModel):
    Cidr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProvisionedCidr"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProvisionedCidr"]:
        if not json_data:
            return None
        return cls(
            Cidr=json_data.get("Cidr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProvisionedCidr = ProvisionedCidr


