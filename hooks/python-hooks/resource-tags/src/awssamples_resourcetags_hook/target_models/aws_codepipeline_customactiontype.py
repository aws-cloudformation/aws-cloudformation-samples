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
class AwsCodepipelineCustomactiontype(BaseModel):
    Category: Optional[str]
    ConfigurationProperties: Optional[AbstractSet["_ConfigurationProperties"]]
    InputArtifactDetails: Optional["_ArtifactDetails"]
    OutputArtifactDetails: Optional["_ArtifactDetails"]
    Provider: Optional[str]
    Settings: Optional["_Settings"]
    Tags: Optional[Any]
    Version: Optional[str]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCodepipelineCustomactiontype"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCodepipelineCustomactiontype"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Category=json_data.get("Category"),
            ConfigurationProperties=set_or_none(json_data.get("ConfigurationProperties")),
            InputArtifactDetails=ArtifactDetails._deserialize(json_data.get("InputArtifactDetails")),
            OutputArtifactDetails=ArtifactDetails._deserialize(json_data.get("OutputArtifactDetails")),
            Provider=json_data.get("Provider"),
            Settings=Settings._deserialize(json_data.get("Settings")),
            Tags=json_data.get("Tags"),
            Version=json_data.get("Version"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCodepipelineCustomactiontype = AwsCodepipelineCustomactiontype


@dataclass
class ConfigurationProperties(BaseModel):
    Description: Optional[str]
    Key: Optional[bool]
    Name: Optional[str]
    Queryable: Optional[bool]
    Required: Optional[bool]
    Secret: Optional[bool]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationProperties"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
            Queryable=json_data.get("Queryable"),
            Required=json_data.get("Required"),
            Secret=json_data.get("Secret"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationProperties = ConfigurationProperties


@dataclass
class ArtifactDetails(BaseModel):
    MaximumCount: Optional[int]
    MinimumCount: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ArtifactDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArtifactDetails"]:
        if not json_data:
            return None
        return cls(
            MaximumCount=json_data.get("MaximumCount"),
            MinimumCount=json_data.get("MinimumCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArtifactDetails = ArtifactDetails


@dataclass
class Settings(BaseModel):
    EntityUrlTemplate: Optional[str]
    ExecutionUrlTemplate: Optional[str]
    RevisionUrlTemplate: Optional[str]
    ThirdPartyConfigurationUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Settings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Settings"]:
        if not json_data:
            return None
        return cls(
            EntityUrlTemplate=json_data.get("EntityUrlTemplate"),
            ExecutionUrlTemplate=json_data.get("ExecutionUrlTemplate"),
            RevisionUrlTemplate=json_data.get("RevisionUrlTemplate"),
            ThirdPartyConfigurationUrl=json_data.get("ThirdPartyConfigurationUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Settings = Settings


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


