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
class AwsGroundstationDataflowendpointgroup(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]
    EndpointDetails: Optional[Sequence["_EndpointDetails"]]
    ContactPrePassDurationSeconds: Optional[int]
    ContactPostPassDurationSeconds: Optional[int]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGroundstationDataflowendpointgroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGroundstationDataflowendpointgroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            EndpointDetails=deserialize_list(json_data.get("EndpointDetails"), EndpointDetails),
            ContactPrePassDurationSeconds=json_data.get("ContactPrePassDurationSeconds"),
            ContactPostPassDurationSeconds=json_data.get("ContactPostPassDurationSeconds"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGroundstationDataflowendpointgroup = AwsGroundstationDataflowendpointgroup


@dataclass
class EndpointDetails(BaseModel):
    SecurityDetails: Optional["_SecurityDetails"]
    Endpoint: Optional["_DataflowEndpoint"]
    AwsGroundStationAgentEndpoint: Optional["_AwsGroundStationAgentEndpoint"]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointDetails"]:
        if not json_data:
            return None
        return cls(
            SecurityDetails=SecurityDetails._deserialize(json_data.get("SecurityDetails")),
            Endpoint=DataflowEndpoint._deserialize(json_data.get("Endpoint")),
            AwsGroundStationAgentEndpoint=AwsGroundStationAgentEndpoint._deserialize(json_data.get("AwsGroundStationAgentEndpoint")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointDetails = EndpointDetails


@dataclass
class SecurityDetails(BaseModel):
    SubnetIds: Optional[Sequence[str]]
    SecurityGroupIds: Optional[Sequence[str]]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityDetails"]:
        if not json_data:
            return None
        return cls(
            SubnetIds=json_data.get("SubnetIds"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecurityDetails = SecurityDetails


@dataclass
class DataflowEndpoint(BaseModel):
    Name: Optional[str]
    Address: Optional["_SocketAddress"]
    Mtu: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_DataflowEndpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataflowEndpoint"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Address=SocketAddress._deserialize(json_data.get("Address")),
            Mtu=json_data.get("Mtu"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataflowEndpoint = DataflowEndpoint


@dataclass
class SocketAddress(BaseModel):
    Name: Optional[str]
    Port: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_SocketAddress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SocketAddress"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SocketAddress = SocketAddress


@dataclass
class AwsGroundStationAgentEndpoint(BaseModel):
    Name: Optional[str]
    EgressAddress: Optional["_ConnectionDetails"]
    IngressAddress: Optional["_RangedConnectionDetails"]
    AgentStatus: Optional[str]
    AuditResults: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGroundStationAgentEndpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGroundStationAgentEndpoint"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            EgressAddress=ConnectionDetails._deserialize(json_data.get("EgressAddress")),
            IngressAddress=RangedConnectionDetails._deserialize(json_data.get("IngressAddress")),
            AgentStatus=json_data.get("AgentStatus"),
            AuditResults=json_data.get("AuditResults"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGroundStationAgentEndpoint = AwsGroundStationAgentEndpoint


@dataclass
class ConnectionDetails(BaseModel):
    SocketAddress: Optional["_SocketAddress"]
    Mtu: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionDetails"]:
        if not json_data:
            return None
        return cls(
            SocketAddress=SocketAddress._deserialize(json_data.get("SocketAddress")),
            Mtu=json_data.get("Mtu"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionDetails = ConnectionDetails


@dataclass
class RangedConnectionDetails(BaseModel):
    SocketAddress: Optional["_RangedSocketAddress"]
    Mtu: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_RangedConnectionDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangedConnectionDetails"]:
        if not json_data:
            return None
        return cls(
            SocketAddress=RangedSocketAddress._deserialize(json_data.get("SocketAddress")),
            Mtu=json_data.get("Mtu"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangedConnectionDetails = RangedConnectionDetails


@dataclass
class RangedSocketAddress(BaseModel):
    Name: Optional[str]
    PortRange: Optional["_IntegerRange"]

    @classmethod
    def _deserialize(
        cls: Type["_RangedSocketAddress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangedSocketAddress"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PortRange=IntegerRange._deserialize(json_data.get("PortRange")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangedSocketAddress = RangedSocketAddress


@dataclass
class IntegerRange(BaseModel):
    Minimum: Optional[int]
    Maximum: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_IntegerRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegerRange"]:
        if not json_data:
            return None
        return cls(
            Minimum=json_data.get("Minimum"),
            Maximum=json_data.get("Maximum"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegerRange = IntegerRange


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


