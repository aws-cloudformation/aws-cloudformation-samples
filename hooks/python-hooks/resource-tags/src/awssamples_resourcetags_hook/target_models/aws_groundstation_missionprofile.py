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
class AwsGroundstationMissionprofile(BaseModel):
    Name: Optional[str]
    ContactPrePassDurationSeconds: Optional[int]
    ContactPostPassDurationSeconds: Optional[int]
    MinimumViableContactDurationSeconds: Optional[int]
    StreamsKmsKey: Optional["_StreamsKmsKey"]
    StreamsKmsRole: Optional[str]
    DataflowEdges: Optional[Sequence["_DataflowEdge"]]
    TrackingConfigArn: Optional[str]
    Tags: Optional[Any]
    Id: Optional[str]
    Arn: Optional[str]
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGroundstationMissionprofile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGroundstationMissionprofile"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            ContactPrePassDurationSeconds=json_data.get("ContactPrePassDurationSeconds"),
            ContactPostPassDurationSeconds=json_data.get("ContactPostPassDurationSeconds"),
            MinimumViableContactDurationSeconds=json_data.get("MinimumViableContactDurationSeconds"),
            StreamsKmsKey=StreamsKmsKey._deserialize(json_data.get("StreamsKmsKey")),
            StreamsKmsRole=json_data.get("StreamsKmsRole"),
            DataflowEdges=deserialize_list(json_data.get("DataflowEdges"), DataflowEdge),
            TrackingConfigArn=json_data.get("TrackingConfigArn"),
            Tags=json_data.get("Tags"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGroundstationMissionprofile = AwsGroundstationMissionprofile


@dataclass
class StreamsKmsKey(BaseModel):
    KmsKeyArn: Optional[str]
    KmsAliasArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StreamsKmsKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StreamsKmsKey"]:
        if not json_data:
            return None
        return cls(
            KmsKeyArn=json_data.get("KmsKeyArn"),
            KmsAliasArn=json_data.get("KmsAliasArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StreamsKmsKey = StreamsKmsKey


@dataclass
class DataflowEdge(BaseModel):
    Source: Optional[str]
    Destination: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataflowEdge"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataflowEdge"]:
        if not json_data:
            return None
        return cls(
            Source=json_data.get("Source"),
            Destination=json_data.get("Destination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataflowEdge = DataflowEdge


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


