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
    AwsService: Optional[str]
    Locale: Optional[str]
    PublicIpSource: Optional[str]
    Description: Optional[str]
    IpamPoolId: Optional[str]
    IpamArn: Optional[str]
    SourceIpamPoolId: Optional[str]
    IpamScopeArn: Optional[str]
    IpamScopeType: Optional[str]
    AllocationMinNetmaskLength: Optional[int]
    IpamScopeId: Optional[str]
    ProvisionedCidrs: Optional[AbstractSet["_ProvisionedCidr"]]
    AllocationMaxNetmaskLength: Optional[int]
    PoolDepth: Optional[int]
    State: Optional[str]
    AllocationDefaultNetmaskLength: Optional[int]
    AutoImport: Optional[bool]
    AddressFamily: Optional[str]
    Arn: Optional[str]
    StateMessage: Optional[str]
    AllocationResourceTags: Optional[AbstractSet["_Tag"]]
    PubliclyAdvertisable: Optional[bool]
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
            AwsService=json_data.get("AwsService"),
            Locale=json_data.get("Locale"),
            PublicIpSource=json_data.get("PublicIpSource"),
            Description=json_data.get("Description"),
            IpamPoolId=json_data.get("IpamPoolId"),
            IpamArn=json_data.get("IpamArn"),
            SourceIpamPoolId=json_data.get("SourceIpamPoolId"),
            IpamScopeArn=json_data.get("IpamScopeArn"),
            IpamScopeType=json_data.get("IpamScopeType"),
            AllocationMinNetmaskLength=json_data.get("AllocationMinNetmaskLength"),
            IpamScopeId=json_data.get("IpamScopeId"),
            ProvisionedCidrs=set_or_none(json_data.get("ProvisionedCidrs")),
            AllocationMaxNetmaskLength=json_data.get("AllocationMaxNetmaskLength"),
            PoolDepth=json_data.get("PoolDepth"),
            State=json_data.get("State"),
            AllocationDefaultNetmaskLength=json_data.get("AllocationDefaultNetmaskLength"),
            AutoImport=json_data.get("AutoImport"),
            AddressFamily=json_data.get("AddressFamily"),
            Arn=json_data.get("Arn"),
            StateMessage=json_data.get("StateMessage"),
            AllocationResourceTags=set_or_none(json_data.get("AllocationResourceTags")),
            PubliclyAdvertisable=json_data.get("PubliclyAdvertisable"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Ipampool = AwsEc2Ipampool


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


@dataclass
class Tag(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


