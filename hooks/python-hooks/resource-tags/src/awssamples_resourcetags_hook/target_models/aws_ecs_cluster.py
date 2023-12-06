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
class AwsEcsCluster(BaseModel):
    ClusterSettings: Optional[Sequence["_ClusterSettings"]]
    DefaultCapacityProviderStrategy: Optional[Sequence["_CapacityProviderStrategyItem"]]
    Configuration: Optional["_ClusterConfiguration"]
    ServiceConnectDefaults: Optional["_ServiceConnectDefaults"]
    CapacityProviders: Optional[Sequence[str]]
    ClusterName: Optional[str]
    Arn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEcsCluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEcsCluster"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ClusterSettings=deserialize_list(json_data.get("ClusterSettings"), ClusterSettings),
            DefaultCapacityProviderStrategy=deserialize_list(json_data.get("DefaultCapacityProviderStrategy"), CapacityProviderStrategyItem),
            Configuration=ClusterConfiguration._deserialize(json_data.get("Configuration")),
            ServiceConnectDefaults=ServiceConnectDefaults._deserialize(json_data.get("ServiceConnectDefaults")),
            CapacityProviders=json_data.get("CapacityProviders"),
            ClusterName=json_data.get("ClusterName"),
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEcsCluster = AwsEcsCluster


@dataclass
class ClusterSettings(BaseModel):
    Value: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterSettings"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterSettings = ClusterSettings


@dataclass
class CapacityProviderStrategyItem(BaseModel):
    CapacityProvider: Optional[str]
    Weight: Optional[int]
    Base: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityProviderStrategyItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityProviderStrategyItem"]:
        if not json_data:
            return None
        return cls(
            CapacityProvider=json_data.get("CapacityProvider"),
            Weight=json_data.get("Weight"),
            Base=json_data.get("Base"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityProviderStrategyItem = CapacityProviderStrategyItem


@dataclass
class ClusterConfiguration(BaseModel):
    ExecuteCommandConfiguration: Optional["_ExecuteCommandConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ClusterConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClusterConfiguration"]:
        if not json_data:
            return None
        return cls(
            ExecuteCommandConfiguration=ExecuteCommandConfiguration._deserialize(json_data.get("ExecuteCommandConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClusterConfiguration = ClusterConfiguration


@dataclass
class ExecuteCommandConfiguration(BaseModel):
    Logging: Optional[str]
    KmsKeyId: Optional[str]
    LogConfiguration: Optional["_ExecuteCommandLogConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ExecuteCommandConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExecuteCommandConfiguration"]:
        if not json_data:
            return None
        return cls(
            Logging=json_data.get("Logging"),
            KmsKeyId=json_data.get("KmsKeyId"),
            LogConfiguration=ExecuteCommandLogConfiguration._deserialize(json_data.get("LogConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExecuteCommandConfiguration = ExecuteCommandConfiguration


@dataclass
class ExecuteCommandLogConfiguration(BaseModel):
    S3EncryptionEnabled: Optional[bool]
    CloudWatchEncryptionEnabled: Optional[bool]
    CloudWatchLogGroupName: Optional[str]
    S3KeyPrefix: Optional[str]
    S3BucketName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExecuteCommandLogConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExecuteCommandLogConfiguration"]:
        if not json_data:
            return None
        return cls(
            S3EncryptionEnabled=json_data.get("S3EncryptionEnabled"),
            CloudWatchEncryptionEnabled=json_data.get("CloudWatchEncryptionEnabled"),
            CloudWatchLogGroupName=json_data.get("CloudWatchLogGroupName"),
            S3KeyPrefix=json_data.get("S3KeyPrefix"),
            S3BucketName=json_data.get("S3BucketName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExecuteCommandLogConfiguration = ExecuteCommandLogConfiguration


@dataclass
class ServiceConnectDefaults(BaseModel):
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceConnectDefaults"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceConnectDefaults"]:
        if not json_data:
            return None
        return cls(
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceConnectDefaults = ServiceConnectDefaults


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


