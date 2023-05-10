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
class AwsRedshiftserverlessWorkgroup(BaseModel):
    WorkgroupName: Optional[str]
    NamespaceName: Optional[str]
    BaseCapacity: Optional[int]
    EnhancedVpcRouting: Optional[bool]
    ConfigParameters: Optional[AbstractSet["_ConfigParameter"]]
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]
    PubliclyAccessible: Optional[bool]
    Port: Optional[int]
    Tags: Optional[Any]
    Workgroup: Optional["_Workgroup"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRedshiftserverlessWorkgroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRedshiftserverlessWorkgroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            WorkgroupName=json_data.get("WorkgroupName"),
            NamespaceName=json_data.get("NamespaceName"),
            BaseCapacity=json_data.get("BaseCapacity"),
            EnhancedVpcRouting=json_data.get("EnhancedVpcRouting"),
            ConfigParameters=set_or_none(json_data.get("ConfigParameters")),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
            PubliclyAccessible=json_data.get("PubliclyAccessible"),
            Port=json_data.get("Port"),
            Tags=json_data.get("Tags"),
            Workgroup=Workgroup._deserialize(json_data.get("Workgroup")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRedshiftserverlessWorkgroup = AwsRedshiftserverlessWorkgroup


@dataclass
class ConfigParameter(BaseModel):
    ParameterKey: Optional[str]
    ParameterValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigParameter"]:
        if not json_data:
            return None
        return cls(
            ParameterKey=json_data.get("ParameterKey"),
            ParameterValue=json_data.get("ParameterValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigParameter = ConfigParameter


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
class Workgroup(BaseModel):
    WorkgroupId: Optional[str]
    WorkgroupArn: Optional[str]
    WorkgroupName: Optional[str]
    NamespaceName: Optional[str]
    BaseCapacity: Optional[int]
    EnhancedVpcRouting: Optional[bool]
    ConfigParameters: Optional[AbstractSet["_ConfigParameter"]]
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]
    Status: Optional[str]
    Endpoint: Optional["_Endpoint"]
    PubliclyAccessible: Optional[bool]
    CreationDate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Workgroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Workgroup"]:
        if not json_data:
            return None
        return cls(
            WorkgroupId=json_data.get("WorkgroupId"),
            WorkgroupArn=json_data.get("WorkgroupArn"),
            WorkgroupName=json_data.get("WorkgroupName"),
            NamespaceName=json_data.get("NamespaceName"),
            BaseCapacity=json_data.get("BaseCapacity"),
            EnhancedVpcRouting=json_data.get("EnhancedVpcRouting"),
            ConfigParameters=set_or_none(json_data.get("ConfigParameters")),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
            Status=json_data.get("Status"),
            Endpoint=Endpoint._deserialize(json_data.get("Endpoint")),
            PubliclyAccessible=json_data.get("PubliclyAccessible"),
            CreationDate=json_data.get("CreationDate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Workgroup = Workgroup


@dataclass
class Endpoint(BaseModel):
    Address: Optional[str]
    Port: Optional[int]
    VpcEndpoints: Optional[Sequence["_VpcEndpoint"]]

    @classmethod
    def _deserialize(
        cls: Type["_Endpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Endpoint"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            Port=json_data.get("Port"),
            VpcEndpoints=deserialize_list(json_data.get("VpcEndpoints"), VpcEndpoint),
        )


# work around possible type aliasing issues when variable has same name as a model
_Endpoint = Endpoint


@dataclass
class VpcEndpoint(BaseModel):
    VpcEndpointId: Optional[str]
    VpcId: Optional[str]
    NetworkInterfaces: Optional[Sequence["_NetworkInterface"]]

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
            NetworkInterfaces=deserialize_list(json_data.get("NetworkInterfaces"), NetworkInterface),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcEndpoint = VpcEndpoint


@dataclass
class NetworkInterface(BaseModel):
    NetworkInterfaceId: Optional[str]
    SubnetId: Optional[str]
    PrivateIpAddress: Optional[str]
    AvailabilityZone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterface"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterface"]:
        if not json_data:
            return None
        return cls(
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            SubnetId=json_data.get("SubnetId"),
            PrivateIpAddress=json_data.get("PrivateIpAddress"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterface = NetworkInterface


