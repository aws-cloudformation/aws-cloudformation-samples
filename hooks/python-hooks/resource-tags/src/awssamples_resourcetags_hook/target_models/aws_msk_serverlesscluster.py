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
class AwsMskServerlesscluster(BaseModel):
    Arn: Optional[str]
    ClusterName: Optional[str]
    VpcConfigs: Optional[AbstractSet["_VpcConfig"]]
    ClientAuthentication: Optional["_ClientAuthentication"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMskServerlesscluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMskServerlesscluster"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            ClusterName=json_data.get("ClusterName"),
            VpcConfigs=set_or_none(json_data.get("VpcConfigs")),
            ClientAuthentication=ClientAuthentication._deserialize(json_data.get("ClientAuthentication")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMskServerlesscluster = AwsMskServerlesscluster


@dataclass
class VpcConfig(BaseModel):
    SecurityGroups: Optional[AbstractSet[str]]
    SubnetIds: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfig"]:
        if not json_data:
            return None
        return cls(
            SecurityGroups=set_or_none(json_data.get("SecurityGroups")),
            SubnetIds=set_or_none(json_data.get("SubnetIds")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfig = VpcConfig


@dataclass
class ClientAuthentication(BaseModel):
    Sasl: Optional["_Sasl"]

    @classmethod
    def _deserialize(
        cls: Type["_ClientAuthentication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientAuthentication"]:
        if not json_data:
            return None
        return cls(
            Sasl=Sasl._deserialize(json_data.get("Sasl")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientAuthentication = ClientAuthentication


@dataclass
class Sasl(BaseModel):
    Iam: Optional["_Iam"]

    @classmethod
    def _deserialize(
        cls: Type["_Sasl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sasl"]:
        if not json_data:
            return None
        return cls(
            Iam=Iam._deserialize(json_data.get("Iam")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sasl = Sasl


@dataclass
class Iam(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Iam"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Iam"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Iam = Iam


