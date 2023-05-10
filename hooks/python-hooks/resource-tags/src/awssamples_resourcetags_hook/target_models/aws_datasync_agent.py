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
class AwsDatasyncAgent(BaseModel):
    AgentName: Optional[str]
    ActivationKey: Optional[str]
    SecurityGroupArns: Optional[Sequence[str]]
    SubnetArns: Optional[Sequence[str]]
    VpcEndpointId: Optional[str]
    EndpointType: Optional[str]
    Tags: Optional[Any]
    AgentArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDatasyncAgent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDatasyncAgent"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AgentName=json_data.get("AgentName"),
            ActivationKey=json_data.get("ActivationKey"),
            SecurityGroupArns=json_data.get("SecurityGroupArns"),
            SubnetArns=json_data.get("SubnetArns"),
            VpcEndpointId=json_data.get("VpcEndpointId"),
            EndpointType=json_data.get("EndpointType"),
            Tags=json_data.get("Tags"),
            AgentArn=json_data.get("AgentArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDatasyncAgent = AwsDatasyncAgent


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


