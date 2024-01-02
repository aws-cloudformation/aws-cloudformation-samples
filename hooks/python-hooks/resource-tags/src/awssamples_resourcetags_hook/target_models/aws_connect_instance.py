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
class AwsConnectInstance(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]
    IdentityManagementType: Optional[str]
    InstanceAlias: Optional[str]
    CreatedTime: Optional[str]
    ServiceRole: Optional[str]
    InstanceStatus: Optional[str]
    DirectoryId: Optional[str]
    Attributes: Optional["_Attributes"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConnectInstance"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConnectInstance"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            IdentityManagementType=json_data.get("IdentityManagementType"),
            InstanceAlias=json_data.get("InstanceAlias"),
            CreatedTime=json_data.get("CreatedTime"),
            ServiceRole=json_data.get("ServiceRole"),
            InstanceStatus=json_data.get("InstanceStatus"),
            DirectoryId=json_data.get("DirectoryId"),
            Attributes=Attributes._deserialize(json_data.get("Attributes")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConnectInstance = AwsConnectInstance


@dataclass
class Attributes(BaseModel):
    InboundCalls: Optional[bool]
    OutboundCalls: Optional[bool]
    ContactflowLogs: Optional[bool]
    ContactLens: Optional[bool]
    AutoResolveBestVoices: Optional[bool]
    UseCustomTTSVoices: Optional[bool]
    EarlyMedia: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Attributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Attributes"]:
        if not json_data:
            return None
        return cls(
            InboundCalls=json_data.get("InboundCalls"),
            OutboundCalls=json_data.get("OutboundCalls"),
            ContactflowLogs=json_data.get("ContactflowLogs"),
            ContactLens=json_data.get("ContactLens"),
            AutoResolveBestVoices=json_data.get("AutoResolveBestVoices"),
            UseCustomTTSVoices=json_data.get("UseCustomTTSVoices"),
            EarlyMedia=json_data.get("EarlyMedia"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Attributes = Attributes


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


