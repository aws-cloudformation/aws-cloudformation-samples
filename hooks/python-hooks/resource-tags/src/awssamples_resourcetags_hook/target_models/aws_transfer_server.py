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
class AwsTransferServer(BaseModel):
    LoggingRole: Optional[str]
    Protocols: Optional[Sequence[MutableMapping[str, Any]]]
    IdentityProviderDetails: Optional["_IdentityProviderDetails"]
    EndpointDetails: Optional["_EndpointDetails"]
    PreAuthenticationLoginBanner: Optional[str]
    ServerId: Optional[str]
    PostAuthenticationLoginBanner: Optional[str]
    EndpointType: Optional[str]
    SecurityPolicyName: Optional[str]
    ProtocolDetails: Optional["_ProtocolDetails"]
    WorkflowDetails: Optional["_WorkflowDetails"]
    Arn: Optional[str]
    Domain: Optional[str]
    IdentityProviderType: Optional[str]
    Tags: Optional[Any]
    Certificate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsTransferServer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsTransferServer"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            LoggingRole=json_data.get("LoggingRole"),
            Protocols=json_data.get("Protocols"),
            IdentityProviderDetails=IdentityProviderDetails._deserialize(json_data.get("IdentityProviderDetails")),
            EndpointDetails=EndpointDetails._deserialize(json_data.get("EndpointDetails")),
            PreAuthenticationLoginBanner=json_data.get("PreAuthenticationLoginBanner"),
            ServerId=json_data.get("ServerId"),
            PostAuthenticationLoginBanner=json_data.get("PostAuthenticationLoginBanner"),
            EndpointType=json_data.get("EndpointType"),
            SecurityPolicyName=json_data.get("SecurityPolicyName"),
            ProtocolDetails=ProtocolDetails._deserialize(json_data.get("ProtocolDetails")),
            WorkflowDetails=WorkflowDetails._deserialize(json_data.get("WorkflowDetails")),
            Arn=json_data.get("Arn"),
            Domain=json_data.get("Domain"),
            IdentityProviderType=json_data.get("IdentityProviderType"),
            Tags=json_data.get("Tags"),
            Certificate=json_data.get("Certificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsTransferServer = AwsTransferServer


@dataclass
class IdentityProviderDetails(BaseModel):
    Function: Optional[str]
    DirectoryId: Optional[str]
    Url: Optional[str]
    InvocationRole: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdentityProviderDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentityProviderDetails"]:
        if not json_data:
            return None
        return cls(
            Function=json_data.get("Function"),
            DirectoryId=json_data.get("DirectoryId"),
            Url=json_data.get("Url"),
            InvocationRole=json_data.get("InvocationRole"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdentityProviderDetails = IdentityProviderDetails


@dataclass
class EndpointDetails(BaseModel):
    AddressAllocationIds: Optional[Sequence[str]]
    VpcId: Optional[str]
    VpcEndpointId: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointDetails"]:
        if not json_data:
            return None
        return cls(
            AddressAllocationIds=json_data.get("AddressAllocationIds"),
            VpcId=json_data.get("VpcId"),
            VpcEndpointId=json_data.get("VpcEndpointId"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointDetails = EndpointDetails


@dataclass
class ProtocolDetails(BaseModel):
    As2Transports: Optional[Sequence[MutableMapping[str, Any]]]
    PassiveIp: Optional[str]
    SetStatOption: Optional[str]
    TlsSessionResumptionMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProtocolDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProtocolDetails"]:
        if not json_data:
            return None
        return cls(
            As2Transports=json_data.get("As2Transports"),
            PassiveIp=json_data.get("PassiveIp"),
            SetStatOption=json_data.get("SetStatOption"),
            TlsSessionResumptionMode=json_data.get("TlsSessionResumptionMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProtocolDetails = ProtocolDetails


@dataclass
class WorkflowDetails(BaseModel):
    OnUpload: Optional[Sequence["_WorkflowDetail"]]
    OnPartialUpload: Optional[Sequence["_WorkflowDetail"]]

    @classmethod
    def _deserialize(
        cls: Type["_WorkflowDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkflowDetails"]:
        if not json_data:
            return None
        return cls(
            OnUpload=deserialize_list(json_data.get("OnUpload"), WorkflowDetail),
            OnPartialUpload=deserialize_list(json_data.get("OnPartialUpload"), WorkflowDetail),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkflowDetails = WorkflowDetails


@dataclass
class WorkflowDetail(BaseModel):
    WorkflowId: Optional[str]
    ExecutionRole: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkflowDetail"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkflowDetail"]:
        if not json_data:
            return None
        return cls(
            WorkflowId=json_data.get("WorkflowId"),
            ExecutionRole=json_data.get("ExecutionRole"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkflowDetail = WorkflowDetail


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


