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
class AwsMedialiveInput(BaseModel):
    Type: Optional[str]
    Destinations: Optional[Sequence["_InputDestinationRequest"]]
    Vpc: Optional["_InputVpcRequest"]
    MediaConnectFlows: Optional[Sequence["_MediaConnectFlowRequest"]]
    Id: Optional[str]
    Arn: Optional[str]
    InputSecurityGroups: Optional[Sequence[str]]
    Sources: Optional[Sequence["_InputSourceRequest"]]
    InputDevices: Optional[Sequence["_InputDeviceSettings"]]
    RoleArn: Optional[str]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMedialiveInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMedialiveInput"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Type=json_data.get("Type"),
            Destinations=deserialize_list(json_data.get("Destinations"), InputDestinationRequest),
            Vpc=InputVpcRequest._deserialize(json_data.get("Vpc")),
            MediaConnectFlows=deserialize_list(json_data.get("MediaConnectFlows"), MediaConnectFlowRequest),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            InputSecurityGroups=json_data.get("InputSecurityGroups"),
            Sources=deserialize_list(json_data.get("Sources"), InputSourceRequest),
            InputDevices=deserialize_list(json_data.get("InputDevices"), InputDeviceSettings),
            RoleArn=json_data.get("RoleArn"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMedialiveInput = AwsMedialiveInput


@dataclass
class InputDestinationRequest(BaseModel):
    StreamName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputDestinationRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputDestinationRequest"]:
        if not json_data:
            return None
        return cls(
            StreamName=json_data.get("StreamName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputDestinationRequest = InputDestinationRequest


@dataclass
class InputVpcRequest(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_InputVpcRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputVpcRequest"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputVpcRequest = InputVpcRequest


@dataclass
class MediaConnectFlowRequest(BaseModel):
    FlowArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MediaConnectFlowRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MediaConnectFlowRequest"]:
        if not json_data:
            return None
        return cls(
            FlowArn=json_data.get("FlowArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MediaConnectFlowRequest = MediaConnectFlowRequest


@dataclass
class InputSourceRequest(BaseModel):
    PasswordParam: Optional[str]
    Username: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputSourceRequest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputSourceRequest"]:
        if not json_data:
            return None
        return cls(
            PasswordParam=json_data.get("PasswordParam"),
            Username=json_data.get("Username"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputSourceRequest = InputSourceRequest


@dataclass
class InputDeviceSettings(BaseModel):
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputDeviceSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputDeviceSettings"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputDeviceSettings = InputDeviceSettings


