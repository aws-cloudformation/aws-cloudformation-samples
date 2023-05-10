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
class AwsSagemakerNotebookinstance(BaseModel):
    KmsKeyId: Optional[str]
    VolumeSizeInGB: Optional[int]
    AdditionalCodeRepositories: Optional[Sequence[str]]
    DefaultCodeRepository: Optional[str]
    DirectInternetAccess: Optional[str]
    PlatformIdentifier: Optional[str]
    AcceleratorTypes: Optional[Sequence[str]]
    SubnetId: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    RoleArn: Optional[str]
    InstanceMetadataServiceConfiguration: Optional["_InstanceMetadataServiceConfiguration"]
    RootAccess: Optional[str]
    Id: Optional[str]
    NotebookInstanceName: Optional[str]
    InstanceType: Optional[str]
    LifecycleConfigName: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSagemakerNotebookinstance"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSagemakerNotebookinstance"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            KmsKeyId=json_data.get("KmsKeyId"),
            VolumeSizeInGB=json_data.get("VolumeSizeInGB"),
            AdditionalCodeRepositories=json_data.get("AdditionalCodeRepositories"),
            DefaultCodeRepository=json_data.get("DefaultCodeRepository"),
            DirectInternetAccess=json_data.get("DirectInternetAccess"),
            PlatformIdentifier=json_data.get("PlatformIdentifier"),
            AcceleratorTypes=json_data.get("AcceleratorTypes"),
            SubnetId=json_data.get("SubnetId"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            RoleArn=json_data.get("RoleArn"),
            InstanceMetadataServiceConfiguration=InstanceMetadataServiceConfiguration._deserialize(json_data.get("InstanceMetadataServiceConfiguration")),
            RootAccess=json_data.get("RootAccess"),
            Id=json_data.get("Id"),
            NotebookInstanceName=json_data.get("NotebookInstanceName"),
            InstanceType=json_data.get("InstanceType"),
            LifecycleConfigName=json_data.get("LifecycleConfigName"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSagemakerNotebookinstance = AwsSagemakerNotebookinstance


@dataclass
class InstanceMetadataServiceConfiguration(BaseModel):
    MinimumInstanceMetadataServiceVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceMetadataServiceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceMetadataServiceConfiguration"]:
        if not json_data:
            return None
        return cls(
            MinimumInstanceMetadataServiceVersion=json_data.get("MinimumInstanceMetadataServiceVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceMetadataServiceConfiguration = InstanceMetadataServiceConfiguration


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


