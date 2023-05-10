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
class AwsApprunnerVpcingressconnection(BaseModel):
    VpcIngressConnectionArn: Optional[str]
    VpcIngressConnectionName: Optional[str]
    ServiceArn: Optional[str]
    Status: Optional[str]
    DomainName: Optional[str]
    IngressVpcConfiguration: Optional["_IngressVpcConfiguration"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApprunnerVpcingressconnection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApprunnerVpcingressconnection"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            VpcIngressConnectionArn=json_data.get("VpcIngressConnectionArn"),
            VpcIngressConnectionName=json_data.get("VpcIngressConnectionName"),
            ServiceArn=json_data.get("ServiceArn"),
            Status=json_data.get("Status"),
            DomainName=json_data.get("DomainName"),
            IngressVpcConfiguration=IngressVpcConfiguration._deserialize(json_data.get("IngressVpcConfiguration")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApprunnerVpcingressconnection = AwsApprunnerVpcingressconnection


@dataclass
class IngressVpcConfiguration(BaseModel):
    VpcId: Optional[str]
    VpcEndpointId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IngressVpcConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressVpcConfiguration"]:
        if not json_data:
            return None
        return cls(
            VpcId=json_data.get("VpcId"),
            VpcEndpointId=json_data.get("VpcEndpointId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngressVpcConfiguration = IngressVpcConfiguration


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


