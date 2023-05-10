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
class AwsAppstreamFleet(BaseModel):
    Description: Optional[str]
    ComputeCapacity: Optional["_ComputeCapacity"]
    Platform: Optional[str]
    VpcConfig: Optional["_VpcConfig"]
    FleetType: Optional[str]
    EnableDefaultInternetAccess: Optional[bool]
    DomainJoinInfo: Optional["_DomainJoinInfo"]
    SessionScriptS3Location: Optional["_S3Location"]
    Name: Optional[str]
    ImageName: Optional[str]
    MaxUserDurationInSeconds: Optional[int]
    IdleDisconnectTimeoutInSeconds: Optional[int]
    UsbDeviceFilterStrings: Optional[Sequence[str]]
    DisconnectTimeoutInSeconds: Optional[int]
    DisplayName: Optional[str]
    StreamView: Optional[str]
    IamRoleArn: Optional[str]
    Id: Optional[str]
    InstanceType: Optional[str]
    MaxConcurrentSessions: Optional[int]
    Tags: Optional[Any]
    ImageArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppstreamFleet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppstreamFleet"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            ComputeCapacity=ComputeCapacity._deserialize(json_data.get("ComputeCapacity")),
            Platform=json_data.get("Platform"),
            VpcConfig=VpcConfig._deserialize(json_data.get("VpcConfig")),
            FleetType=json_data.get("FleetType"),
            EnableDefaultInternetAccess=json_data.get("EnableDefaultInternetAccess"),
            DomainJoinInfo=DomainJoinInfo._deserialize(json_data.get("DomainJoinInfo")),
            SessionScriptS3Location=S3Location._deserialize(json_data.get("SessionScriptS3Location")),
            Name=json_data.get("Name"),
            ImageName=json_data.get("ImageName"),
            MaxUserDurationInSeconds=json_data.get("MaxUserDurationInSeconds"),
            IdleDisconnectTimeoutInSeconds=json_data.get("IdleDisconnectTimeoutInSeconds"),
            UsbDeviceFilterStrings=json_data.get("UsbDeviceFilterStrings"),
            DisconnectTimeoutInSeconds=json_data.get("DisconnectTimeoutInSeconds"),
            DisplayName=json_data.get("DisplayName"),
            StreamView=json_data.get("StreamView"),
            IamRoleArn=json_data.get("IamRoleArn"),
            Id=json_data.get("Id"),
            InstanceType=json_data.get("InstanceType"),
            MaxConcurrentSessions=json_data.get("MaxConcurrentSessions"),
            Tags=json_data.get("Tags"),
            ImageArn=json_data.get("ImageArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppstreamFleet = AwsAppstreamFleet


@dataclass
class ComputeCapacity(BaseModel):
    DesiredInstances: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ComputeCapacity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComputeCapacity"]:
        if not json_data:
            return None
        return cls(
            DesiredInstances=json_data.get("DesiredInstances"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComputeCapacity = ComputeCapacity


@dataclass
class VpcConfig(BaseModel):
    SubnetIds: Optional[Sequence[str]]
    SecurityGroupIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfig"]:
        if not json_data:
            return None
        return cls(
            SubnetIds=json_data.get("SubnetIds"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfig = VpcConfig


@dataclass
class DomainJoinInfo(BaseModel):
    OrganizationalUnitDistinguishedName: Optional[str]
    DirectoryName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DomainJoinInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainJoinInfo"]:
        if not json_data:
            return None
        return cls(
            OrganizationalUnitDistinguishedName=json_data.get("OrganizationalUnitDistinguishedName"),
            DirectoryName=json_data.get("DirectoryName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainJoinInfo = DomainJoinInfo


@dataclass
class S3Location(BaseModel):
    S3Bucket: Optional[str]
    S3Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Location"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Location"]:
        if not json_data:
            return None
        return cls(
            S3Bucket=json_data.get("S3Bucket"),
            S3Key=json_data.get("S3Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Location = S3Location


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


