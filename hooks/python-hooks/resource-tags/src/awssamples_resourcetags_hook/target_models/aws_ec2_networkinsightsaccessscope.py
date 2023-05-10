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
class AwsEc2Networkinsightsaccessscope(BaseModel):
    NetworkInsightsAccessScopeId: Optional[str]
    NetworkInsightsAccessScopeArn: Optional[str]
    CreatedDate: Optional[str]
    UpdatedDate: Optional[str]
    Tags: Optional[Any]
    MatchPaths: Optional[Sequence["_AccessScopePathRequest"]]
    ExcludePaths: Optional[Sequence["_AccessScopePathRequest"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Networkinsightsaccessscope"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Networkinsightsaccessscope"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            NetworkInsightsAccessScopeId=json_data.get("NetworkInsightsAccessScopeId"),
            NetworkInsightsAccessScopeArn=json_data.get("NetworkInsightsAccessScopeArn"),
            CreatedDate=json_data.get("CreatedDate"),
            UpdatedDate=json_data.get("UpdatedDate"),
            Tags=json_data.get("Tags"),
            MatchPaths=deserialize_list(json_data.get("MatchPaths"), AccessScopePathRequest),
            ExcludePaths=deserialize_list(json_data.get("ExcludePaths"), AccessScopePathRequest),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Networkinsightsaccessscope = AwsEc2Networkinsightsaccessscope


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
class AccessScopePathRequest(BaseModel):
    Source: Optional["_PathStatementRequest"]
    Destination: Optional["_PathStatementRequest"]
    ThroughResources: Optional[Sequence["_ThroughResourcesStatementRequest"]]

    @classmethod
    def _deserialize(
        cls: Type["_AccessScopePathRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessScopePathRequest"]:
        if not json_data:
            return None
        return cls(
            Source=PathStatementRequest._deserialize(json_data.get("Source")),
            Destination=PathStatementRequest._deserialize(json_data.get("Destination")),
            ThroughResources=deserialize_list(json_data.get("ThroughResources"), ThroughResourcesStatementRequest),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessScopePathRequest = AccessScopePathRequest


@dataclass
class PathStatementRequest(BaseModel):
    PacketHeaderStatement: Optional["_PacketHeaderStatementRequest"]
    ResourceStatement: Optional["_ResourceStatementRequest"]

    @classmethod
    def _deserialize(
        cls: Type["_PathStatementRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathStatementRequest"]:
        if not json_data:
            return None
        return cls(
            PacketHeaderStatement=PacketHeaderStatementRequest._deserialize(json_data.get("PacketHeaderStatement")),
            ResourceStatement=ResourceStatementRequest._deserialize(json_data.get("ResourceStatement")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathStatementRequest = PathStatementRequest


@dataclass
class PacketHeaderStatementRequest(BaseModel):
    SourceAddresses: Optional[Sequence[str]]
    DestinationAddresses: Optional[Sequence[str]]
    SourcePorts: Optional[Sequence[str]]
    DestinationPorts: Optional[Sequence[str]]
    SourcePrefixLists: Optional[Sequence[str]]
    DestinationPrefixLists: Optional[Sequence[str]]
    Protocols: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PacketHeaderStatementRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PacketHeaderStatementRequest"]:
        if not json_data:
            return None
        return cls(
            SourceAddresses=json_data.get("SourceAddresses"),
            DestinationAddresses=json_data.get("DestinationAddresses"),
            SourcePorts=json_data.get("SourcePorts"),
            DestinationPorts=json_data.get("DestinationPorts"),
            SourcePrefixLists=json_data.get("SourcePrefixLists"),
            DestinationPrefixLists=json_data.get("DestinationPrefixLists"),
            Protocols=json_data.get("Protocols"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PacketHeaderStatementRequest = PacketHeaderStatementRequest


@dataclass
class ResourceStatementRequest(BaseModel):
    Resources: Optional[Sequence[str]]
    ResourceTypes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceStatementRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceStatementRequest"]:
        if not json_data:
            return None
        return cls(
            Resources=json_data.get("Resources"),
            ResourceTypes=json_data.get("ResourceTypes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceStatementRequest = ResourceStatementRequest


@dataclass
class ThroughResourcesStatementRequest(BaseModel):
    ResourceStatement: Optional["_ResourceStatementRequest"]

    @classmethod
    def _deserialize(
        cls: Type["_ThroughResourcesStatementRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ThroughResourcesStatementRequest"]:
        if not json_data:
            return None
        return cls(
            ResourceStatement=ResourceStatementRequest._deserialize(json_data.get("ResourceStatement")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ThroughResourcesStatementRequest = ThroughResourcesStatementRequest


