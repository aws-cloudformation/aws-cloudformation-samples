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
class AwsEc2Networkinsightspath(BaseModel):
    NetworkInsightsPathId: Optional[str]
    NetworkInsightsPathArn: Optional[str]
    CreatedDate: Optional[str]
    SourceIp: Optional[str]
    FilterAtSource: Optional["_PathFilter"]
    FilterAtDestination: Optional["_PathFilter"]
    DestinationIp: Optional[str]
    Source: Optional[str]
    Destination: Optional[str]
    SourceArn: Optional[str]
    DestinationArn: Optional[str]
    Protocol: Optional[str]
    DestinationPort: Optional[int]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Networkinsightspath"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Networkinsightspath"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            NetworkInsightsPathId=json_data.get("NetworkInsightsPathId"),
            NetworkInsightsPathArn=json_data.get("NetworkInsightsPathArn"),
            CreatedDate=json_data.get("CreatedDate"),
            SourceIp=json_data.get("SourceIp"),
            FilterAtSource=PathFilter._deserialize(json_data.get("FilterAtSource")),
            FilterAtDestination=PathFilter._deserialize(json_data.get("FilterAtDestination")),
            DestinationIp=json_data.get("DestinationIp"),
            Source=json_data.get("Source"),
            Destination=json_data.get("Destination"),
            SourceArn=json_data.get("SourceArn"),
            DestinationArn=json_data.get("DestinationArn"),
            Protocol=json_data.get("Protocol"),
            DestinationPort=json_data.get("DestinationPort"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Networkinsightspath = AwsEc2Networkinsightspath


@dataclass
class PathFilter(BaseModel):
    SourceAddress: Optional[str]
    SourcePortRange: Optional["_FilterPortRange"]
    DestinationAddress: Optional[str]
    DestinationPortRange: Optional["_FilterPortRange"]

    @classmethod
    def _deserialize(
        cls: Type["_PathFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathFilter"]:
        if not json_data:
            return None
        return cls(
            SourceAddress=json_data.get("SourceAddress"),
            SourcePortRange=FilterPortRange._deserialize(json_data.get("SourcePortRange")),
            DestinationAddress=json_data.get("DestinationAddress"),
            DestinationPortRange=FilterPortRange._deserialize(json_data.get("DestinationPortRange")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathFilter = PathFilter


@dataclass
class FilterPortRange(BaseModel):
    FromPort: Optional[int]
    ToPort: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_FilterPortRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterPortRange"]:
        if not json_data:
            return None
        return cls(
            FromPort=json_data.get("FromPort"),
            ToPort=json_data.get("ToPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterPortRange = FilterPortRange


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


