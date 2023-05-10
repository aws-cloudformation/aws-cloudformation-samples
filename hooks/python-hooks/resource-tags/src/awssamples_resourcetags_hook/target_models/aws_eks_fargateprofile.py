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
class AwsEksFargateprofile(BaseModel):
    ClusterName: Optional[str]
    FargateProfileName: Optional[str]
    PodExecutionRoleArn: Optional[str]
    Arn: Optional[str]
    Subnets: Optional[Sequence[str]]
    Selectors: Optional[Sequence["_Selector"]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEksFargateprofile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEksFargateprofile"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ClusterName=json_data.get("ClusterName"),
            FargateProfileName=json_data.get("FargateProfileName"),
            PodExecutionRoleArn=json_data.get("PodExecutionRoleArn"),
            Arn=json_data.get("Arn"),
            Subnets=json_data.get("Subnets"),
            Selectors=deserialize_list(json_data.get("Selectors"), Selector),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEksFargateprofile = AwsEksFargateprofile


@dataclass
class Selector(BaseModel):
    Namespace: Optional[str]
    Labels: Optional[Sequence["_Label"]]

    @classmethod
    def _deserialize(
        cls: Type["_Selector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Selector"]:
        if not json_data:
            return None
        return cls(
            Namespace=json_data.get("Namespace"),
            Labels=deserialize_list(json_data.get("Labels"), Label),
        )


# work around possible type aliasing issues when variable has same name as a model
_Selector = Selector


@dataclass
class Label(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Label"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Label"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Label = Label


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


