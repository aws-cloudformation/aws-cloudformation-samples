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
class AwsOsisPipeline(BaseModel):
    LogPublishingOptions: Optional["_LogPublishingOptions"]
    MaxUnits: Optional[int]
    MinUnits: Optional[int]
    PipelineConfigurationBody: Optional[str]
    PipelineName: Optional[str]
    Tags: Optional[Any]
    VpcOptions: Optional["_VpcOptions"]
    VpcEndpoints: Optional[Sequence["_VpcEndpoint"]]
    PipelineArn: Optional[str]
    IngestEndpointUrls: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsOsisPipeline"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsOsisPipeline"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            LogPublishingOptions=LogPublishingOptions._deserialize(json_data.get("LogPublishingOptions")),
            MaxUnits=json_data.get("MaxUnits"),
            MinUnits=json_data.get("MinUnits"),
            PipelineConfigurationBody=json_data.get("PipelineConfigurationBody"),
            PipelineName=json_data.get("PipelineName"),
            Tags=json_data.get("Tags"),
            VpcOptions=VpcOptions._deserialize(json_data.get("VpcOptions")),
            VpcEndpoints=deserialize_list(json_data.get("VpcEndpoints"), VpcEndpoint),
            PipelineArn=json_data.get("PipelineArn"),
            IngestEndpointUrls=json_data.get("IngestEndpointUrls"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsOsisPipeline = AwsOsisPipeline


@dataclass
class LogPublishingOptions(BaseModel):
    IsLoggingEnabled: Optional[bool]
    CloudWatchLogDestination: Optional["_CloudWatchLogDestination"]

    @classmethod
    def _deserialize(
        cls: Type["_LogPublishingOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogPublishingOptions"]:
        if not json_data:
            return None
        return cls(
            IsLoggingEnabled=json_data.get("IsLoggingEnabled"),
            CloudWatchLogDestination=CloudWatchLogDestination._deserialize(json_data.get("CloudWatchLogDestination")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogPublishingOptions = LogPublishingOptions


@dataclass
class CloudWatchLogDestination(BaseModel):
    LogGroup: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudWatchLogDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudWatchLogDestination"]:
        if not json_data:
            return None
        return cls(
            LogGroup=json_data.get("LogGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudWatchLogDestination = CloudWatchLogDestination


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
class VpcOptions(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcOptions"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcOptions = VpcOptions


@dataclass
class VpcEndpoint(BaseModel):
    VpcEndpointId: Optional[str]
    VpcId: Optional[str]
    VpcOptions: Optional["_VpcOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_VpcEndpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcEndpoint"]:
        if not json_data:
            return None
        return cls(
            VpcEndpointId=json_data.get("VpcEndpointId"),
            VpcId=json_data.get("VpcId"),
            VpcOptions=VpcOptions._deserialize(json_data.get("VpcOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcEndpoint = VpcEndpoint


