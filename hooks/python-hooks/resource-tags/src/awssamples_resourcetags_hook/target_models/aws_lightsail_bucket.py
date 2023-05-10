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
class AwsLightsailBucket(BaseModel):
    BucketName: Optional[str]
    BundleId: Optional[str]
    BucketArn: Optional[str]
    ObjectVersioning: Optional[bool]
    AccessRules: Optional["_AccessRules"]
    ResourcesReceivingAccess: Optional[AbstractSet[str]]
    ReadOnlyAccessAccounts: Optional[AbstractSet[str]]
    Tags: Optional[Any]
    Url: Optional[str]
    AbleToUpdateBundle: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLightsailBucket"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLightsailBucket"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            BucketName=json_data.get("BucketName"),
            BundleId=json_data.get("BundleId"),
            BucketArn=json_data.get("BucketArn"),
            ObjectVersioning=json_data.get("ObjectVersioning"),
            AccessRules=AccessRules._deserialize(json_data.get("AccessRules")),
            ResourcesReceivingAccess=set_or_none(json_data.get("ResourcesReceivingAccess")),
            ReadOnlyAccessAccounts=set_or_none(json_data.get("ReadOnlyAccessAccounts")),
            Tags=json_data.get("Tags"),
            Url=json_data.get("Url"),
            AbleToUpdateBundle=json_data.get("AbleToUpdateBundle"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLightsailBucket = AwsLightsailBucket


@dataclass
class AccessRules(BaseModel):
    GetObject: Optional[str]
    AllowPublicOverrides: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AccessRules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessRules"]:
        if not json_data:
            return None
        return cls(
            GetObject=json_data.get("GetObject"),
            AllowPublicOverrides=json_data.get("AllowPublicOverrides"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessRules = AccessRules


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


