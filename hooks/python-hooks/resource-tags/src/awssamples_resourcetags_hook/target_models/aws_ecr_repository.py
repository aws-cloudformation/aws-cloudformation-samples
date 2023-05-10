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
class AwsEcrRepository(BaseModel):
    LifecyclePolicy: Optional["_LifecyclePolicy"]
    RepositoryName: Optional[str]
    RepositoryPolicyText: Optional[Any]
    Tags: Optional[Any]
    Arn: Optional[str]
    RepositoryUri: Optional[str]
    ImageTagMutability: Optional[str]
    ImageScanningConfiguration: Optional["_ImageScanningConfiguration"]
    EncryptionConfiguration: Optional["_EncryptionConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEcrRepository"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEcrRepository"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            LifecyclePolicy=LifecyclePolicy._deserialize(json_data.get("LifecyclePolicy")),
            RepositoryName=json_data.get("RepositoryName"),
            RepositoryPolicyText=json_data.get("RepositoryPolicyText"),
            Tags=json_data.get("Tags"),
            Arn=json_data.get("Arn"),
            RepositoryUri=json_data.get("RepositoryUri"),
            ImageTagMutability=json_data.get("ImageTagMutability"),
            ImageScanningConfiguration=ImageScanningConfiguration._deserialize(json_data.get("ImageScanningConfiguration")),
            EncryptionConfiguration=EncryptionConfiguration._deserialize(json_data.get("EncryptionConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEcrRepository = AwsEcrRepository


@dataclass
class LifecyclePolicy(BaseModel):
    LifecyclePolicyText: Optional[str]
    RegistryId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LifecyclePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifecyclePolicy"]:
        if not json_data:
            return None
        return cls(
            LifecyclePolicyText=json_data.get("LifecyclePolicyText"),
            RegistryId=json_data.get("RegistryId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifecyclePolicy = LifecyclePolicy


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
class ImageScanningConfiguration(BaseModel):
    ScanOnPush: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ImageScanningConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageScanningConfiguration"]:
        if not json_data:
            return None
        return cls(
            ScanOnPush=json_data.get("ScanOnPush"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageScanningConfiguration = ImageScanningConfiguration


@dataclass
class EncryptionConfiguration(BaseModel):
    EncryptionType: Optional[str]
    KmsKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfiguration"]:
        if not json_data:
            return None
        return cls(
            EncryptionType=json_data.get("EncryptionType"),
            KmsKey=json_data.get("KmsKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfiguration = EncryptionConfiguration


