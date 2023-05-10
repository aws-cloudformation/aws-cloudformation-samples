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
class AwsIotanalyticsChannel(BaseModel):
    ChannelStorage: Optional["_ChannelStorage"]
    ChannelName: Optional[str]
    Id: Optional[str]
    RetentionPeriod: Optional["_RetentionPeriod"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotanalyticsChannel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotanalyticsChannel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ChannelStorage=ChannelStorage._deserialize(json_data.get("ChannelStorage")),
            ChannelName=json_data.get("ChannelName"),
            Id=json_data.get("Id"),
            RetentionPeriod=RetentionPeriod._deserialize(json_data.get("RetentionPeriod")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotanalyticsChannel = AwsIotanalyticsChannel


@dataclass
class ChannelStorage(BaseModel):
    ServiceManagedS3: Optional[MutableMapping[str, Any]]
    CustomerManagedS3: Optional["_CustomerManagedS3"]

    @classmethod
    def _deserialize(
        cls: Type["_ChannelStorage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChannelStorage"]:
        if not json_data:
            return None
        return cls(
            ServiceManagedS3=json_data.get("ServiceManagedS3"),
            CustomerManagedS3=CustomerManagedS3._deserialize(json_data.get("CustomerManagedS3")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChannelStorage = ChannelStorage


@dataclass
class CustomerManagedS3(BaseModel):
    Bucket: Optional[str]
    RoleArn: Optional[str]
    KeyPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomerManagedS3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomerManagedS3"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            RoleArn=json_data.get("RoleArn"),
            KeyPrefix=json_data.get("KeyPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomerManagedS3 = CustomerManagedS3


@dataclass
class RetentionPeriod(BaseModel):
    NumberOfDays: Optional[int]
    Unlimited: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionPeriod"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionPeriod"]:
        if not json_data:
            return None
        return cls(
            NumberOfDays=json_data.get("NumberOfDays"),
            Unlimited=json_data.get("Unlimited"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionPeriod = RetentionPeriod


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


