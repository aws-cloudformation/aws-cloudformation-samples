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
class AwsEc2Verifiedaccessendpoint(BaseModel):
    VerifiedAccessEndpointId: Optional[str]
    VerifiedAccessGroupId: Optional[str]
    VerifiedAccessInstanceId: Optional[str]
    Status: Optional[str]
    SecurityGroupIds: Optional[AbstractSet[str]]
    NetworkInterfaceOptions: Optional["_NetworkInterfaceOptions"]
    LoadBalancerOptions: Optional["_LoadBalancerOptions"]
    EndpointType: Optional[str]
    EndpointDomain: Optional[str]
    EndpointDomainPrefix: Optional[str]
    DeviceValidationDomain: Optional[str]
    DomainCertificateArn: Optional[str]
    AttachmentType: Optional[str]
    ApplicationDomain: Optional[str]
    CreationTime: Optional[str]
    LastUpdatedTime: Optional[str]
    Description: Optional[str]
    PolicyDocument: Optional[str]
    PolicyEnabled: Optional[bool]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Verifiedaccessendpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Verifiedaccessendpoint"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            VerifiedAccessEndpointId=json_data.get("VerifiedAccessEndpointId"),
            VerifiedAccessGroupId=json_data.get("VerifiedAccessGroupId"),
            VerifiedAccessInstanceId=json_data.get("VerifiedAccessInstanceId"),
            Status=json_data.get("Status"),
            SecurityGroupIds=set_or_none(json_data.get("SecurityGroupIds")),
            NetworkInterfaceOptions=NetworkInterfaceOptions._deserialize(json_data.get("NetworkInterfaceOptions")),
            LoadBalancerOptions=LoadBalancerOptions._deserialize(json_data.get("LoadBalancerOptions")),
            EndpointType=json_data.get("EndpointType"),
            EndpointDomain=json_data.get("EndpointDomain"),
            EndpointDomainPrefix=json_data.get("EndpointDomainPrefix"),
            DeviceValidationDomain=json_data.get("DeviceValidationDomain"),
            DomainCertificateArn=json_data.get("DomainCertificateArn"),
            AttachmentType=json_data.get("AttachmentType"),
            ApplicationDomain=json_data.get("ApplicationDomain"),
            CreationTime=json_data.get("CreationTime"),
            LastUpdatedTime=json_data.get("LastUpdatedTime"),
            Description=json_data.get("Description"),
            PolicyDocument=json_data.get("PolicyDocument"),
            PolicyEnabled=json_data.get("PolicyEnabled"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Verifiedaccessendpoint = AwsEc2Verifiedaccessendpoint


@dataclass
class NetworkInterfaceOptions(BaseModel):
    NetworkInterfaceId: Optional[str]
    Port: Optional[int]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterfaceOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterfaceOptions"]:
        if not json_data:
            return None
        return cls(
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterfaceOptions = NetworkInterfaceOptions


@dataclass
class LoadBalancerOptions(BaseModel):
    LoadBalancerArn: Optional[str]
    Port: Optional[int]
    Protocol: Optional[str]
    SubnetIds: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancerOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancerOptions"]:
        if not json_data:
            return None
        return cls(
            LoadBalancerArn=json_data.get("LoadBalancerArn"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            SubnetIds=set_or_none(json_data.get("SubnetIds")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancerOptions = LoadBalancerOptions


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


