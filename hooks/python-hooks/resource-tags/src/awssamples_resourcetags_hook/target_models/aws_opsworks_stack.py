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
class AwsOpsworksStack(BaseModel):
    Id: Optional[str]
    AgentVersion: Optional[str]
    Attributes: Optional[MutableMapping[str, str]]
    ChefConfiguration: Optional["_ChefConfiguration"]
    CloneAppIds: Optional[Sequence[str]]
    ClonePermissions: Optional[bool]
    ConfigurationManager: Optional["_StackConfigurationManager"]
    CustomCookbooksSource: Optional["_Source"]
    CustomJson: Optional[MutableMapping[str, Any]]
    DefaultAvailabilityZone: Optional[str]
    DefaultInstanceProfileArn: Optional[str]
    DefaultOs: Optional[str]
    DefaultRootDeviceType: Optional[str]
    DefaultSshKeyName: Optional[str]
    DefaultSubnetId: Optional[str]
    EcsClusterArn: Optional[str]
    ElasticIps: Optional[Sequence["_ElasticIp"]]
    HostnameTheme: Optional[str]
    Name: Optional[str]
    RdsDbInstances: Optional[Sequence["_RdsDbInstance"]]
    ServiceRoleArn: Optional[str]
    SourceStackId: Optional[str]
    Tags: Optional[Any]
    UseCustomCookbooks: Optional[bool]
    UseOpsworksSecurityGroups: Optional[bool]
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsOpsworksStack"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsOpsworksStack"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            AgentVersion=json_data.get("AgentVersion"),
            Attributes=json_data.get("Attributes"),
            ChefConfiguration=ChefConfiguration._deserialize(json_data.get("ChefConfiguration")),
            CloneAppIds=json_data.get("CloneAppIds"),
            ClonePermissions=json_data.get("ClonePermissions"),
            ConfigurationManager=StackConfigurationManager._deserialize(json_data.get("ConfigurationManager")),
            CustomCookbooksSource=Source._deserialize(json_data.get("CustomCookbooksSource")),
            CustomJson=json_data.get("CustomJson"),
            DefaultAvailabilityZone=json_data.get("DefaultAvailabilityZone"),
            DefaultInstanceProfileArn=json_data.get("DefaultInstanceProfileArn"),
            DefaultOs=json_data.get("DefaultOs"),
            DefaultRootDeviceType=json_data.get("DefaultRootDeviceType"),
            DefaultSshKeyName=json_data.get("DefaultSshKeyName"),
            DefaultSubnetId=json_data.get("DefaultSubnetId"),
            EcsClusterArn=json_data.get("EcsClusterArn"),
            ElasticIps=deserialize_list(json_data.get("ElasticIps"), ElasticIp),
            HostnameTheme=json_data.get("HostnameTheme"),
            Name=json_data.get("Name"),
            RdsDbInstances=deserialize_list(json_data.get("RdsDbInstances"), RdsDbInstance),
            ServiceRoleArn=json_data.get("ServiceRoleArn"),
            SourceStackId=json_data.get("SourceStackId"),
            Tags=json_data.get("Tags"),
            UseCustomCookbooks=json_data.get("UseCustomCookbooks"),
            UseOpsworksSecurityGroups=json_data.get("UseOpsworksSecurityGroups"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsOpsworksStack = AwsOpsworksStack


@dataclass
class ChefConfiguration(BaseModel):
    BerkshelfVersion: Optional[str]
    ManageBerkshelf: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ChefConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChefConfiguration"]:
        if not json_data:
            return None
        return cls(
            BerkshelfVersion=json_data.get("BerkshelfVersion"),
            ManageBerkshelf=json_data.get("ManageBerkshelf"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChefConfiguration = ChefConfiguration


@dataclass
class StackConfigurationManager(BaseModel):
    Name: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StackConfigurationManager"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StackConfigurationManager"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StackConfigurationManager = StackConfigurationManager


@dataclass
class Source(BaseModel):
    Password: Optional[str]
    Revision: Optional[str]
    SshKey: Optional[str]
    Type: Optional[str]
    Url: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Source"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Source"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Revision=json_data.get("Revision"),
            SshKey=json_data.get("SshKey"),
            Type=json_data.get("Type"),
            Url=json_data.get("Url"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Source = Source


@dataclass
class ElasticIp(BaseModel):
    Ip: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticIp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticIp"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticIp = ElasticIp


@dataclass
class RdsDbInstance(BaseModel):
    DbPassword: Optional[str]
    DbUser: Optional[str]
    RdsDbInstanceArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RdsDbInstance"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RdsDbInstance"]:
        if not json_data:
            return None
        return cls(
            DbPassword=json_data.get("DbPassword"),
            DbUser=json_data.get("DbUser"),
            RdsDbInstanceArn=json_data.get("RdsDbInstanceArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RdsDbInstance = RdsDbInstance


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


