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
class AwsImagebuilderInfrastructureconfiguration(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    Description: Optional[str]
    InstanceTypes: Optional[Sequence[str]]
    SecurityGroupIds: Optional[Sequence[str]]
    Logging: Optional["_Logging"]
    SubnetId: Optional[str]
    KeyPair: Optional[str]
    TerminateInstanceOnFailure: Optional[bool]
    InstanceProfileName: Optional[str]
    InstanceMetadataOptions: Optional["_InstanceMetadataOptions"]
    SnsTopicArn: Optional[str]
    ResourceTags: Optional[MutableMapping[str, str]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsImagebuilderInfrastructureconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsImagebuilderInfrastructureconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            InstanceTypes=json_data.get("InstanceTypes"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            Logging=Logging._deserialize(json_data.get("Logging")),
            SubnetId=json_data.get("SubnetId"),
            KeyPair=json_data.get("KeyPair"),
            TerminateInstanceOnFailure=json_data.get("TerminateInstanceOnFailure"),
            InstanceProfileName=json_data.get("InstanceProfileName"),
            InstanceMetadataOptions=InstanceMetadataOptions._deserialize(json_data.get("InstanceMetadataOptions")),
            SnsTopicArn=json_data.get("SnsTopicArn"),
            ResourceTags=json_data.get("ResourceTags"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsImagebuilderInfrastructureconfiguration = AwsImagebuilderInfrastructureconfiguration


@dataclass
class Logging(BaseModel):
    S3Logs: Optional["_S3Logs"]

    @classmethod
    def _deserialize(
        cls: Type["_Logging"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Logging"]:
        if not json_data:
            return None
        return cls(
            S3Logs=S3Logs._deserialize(json_data.get("S3Logs")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Logging = Logging


@dataclass
class S3Logs(BaseModel):
    S3BucketName: Optional[str]
    S3KeyPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Logs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Logs"]:
        if not json_data:
            return None
        return cls(
            S3BucketName=json_data.get("S3BucketName"),
            S3KeyPrefix=json_data.get("S3KeyPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Logs = S3Logs


@dataclass
class InstanceMetadataOptions(BaseModel):
    HttpPutResponseHopLimit: Optional[int]
    HttpTokens: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceMetadataOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceMetadataOptions"]:
        if not json_data:
            return None
        return cls(
            HttpPutResponseHopLimit=json_data.get("HttpPutResponseHopLimit"),
            HttpTokens=json_data.get("HttpTokens"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceMetadataOptions = InstanceMetadataOptions


