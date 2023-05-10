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
class AwsEc2Verifiedaccessinstance(BaseModel):
    VerifiedAccessInstanceId: Optional[str]
    VerifiedAccessTrustProviders: Optional[AbstractSet["_VerifiedAccessTrustProvider"]]
    VerifiedAccessTrustProviderIds: Optional[AbstractSet[str]]
    CreationTime: Optional[str]
    LastUpdatedTime: Optional[str]
    Description: Optional[str]
    LoggingConfigurations: Optional["_VerifiedAccessLogs"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Verifiedaccessinstance"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Verifiedaccessinstance"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            VerifiedAccessInstanceId=json_data.get("VerifiedAccessInstanceId"),
            VerifiedAccessTrustProviders=set_or_none(json_data.get("VerifiedAccessTrustProviders")),
            VerifiedAccessTrustProviderIds=set_or_none(json_data.get("VerifiedAccessTrustProviderIds")),
            CreationTime=json_data.get("CreationTime"),
            LastUpdatedTime=json_data.get("LastUpdatedTime"),
            Description=json_data.get("Description"),
            LoggingConfigurations=VerifiedAccessLogs._deserialize(json_data.get("LoggingConfigurations")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Verifiedaccessinstance = AwsEc2Verifiedaccessinstance


@dataclass
class VerifiedAccessTrustProvider(BaseModel):
    VerifiedAccessTrustProviderId: Optional[str]
    Description: Optional[str]
    TrustProviderType: Optional[str]
    UserTrustProviderType: Optional[str]
    DeviceTrustProviderType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VerifiedAccessTrustProvider"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VerifiedAccessTrustProvider"]:
        if not json_data:
            return None
        return cls(
            VerifiedAccessTrustProviderId=json_data.get("VerifiedAccessTrustProviderId"),
            Description=json_data.get("Description"),
            TrustProviderType=json_data.get("TrustProviderType"),
            UserTrustProviderType=json_data.get("UserTrustProviderType"),
            DeviceTrustProviderType=json_data.get("DeviceTrustProviderType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VerifiedAccessTrustProvider = VerifiedAccessTrustProvider


@dataclass
class VerifiedAccessLogs(BaseModel):
    CloudWatchLogs: Optional["_CloudWatchLogs"]
    KinesisDataFirehose: Optional["_KinesisDataFirehose"]
    S3: Optional["_S3"]

    @classmethod
    def _deserialize(
        cls: Type["_VerifiedAccessLogs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VerifiedAccessLogs"]:
        if not json_data:
            return None
        return cls(
            CloudWatchLogs=CloudWatchLogs._deserialize(json_data.get("CloudWatchLogs")),
            KinesisDataFirehose=KinesisDataFirehose._deserialize(json_data.get("KinesisDataFirehose")),
            S3=S3._deserialize(json_data.get("S3")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VerifiedAccessLogs = VerifiedAccessLogs


@dataclass
class CloudWatchLogs(BaseModel):
    Enabled: Optional[bool]
    LogGroup: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudWatchLogs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudWatchLogs"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            LogGroup=json_data.get("LogGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudWatchLogs = CloudWatchLogs


@dataclass
class KinesisDataFirehose(BaseModel):
    Enabled: Optional[bool]
    DeliveryStream: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisDataFirehose"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisDataFirehose"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            DeliveryStream=json_data.get("DeliveryStream"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisDataFirehose = KinesisDataFirehose


@dataclass
class S3(BaseModel):
    Enabled: Optional[bool]
    BucketName: Optional[str]
    BucketOwner: Optional[str]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            BucketName=json_data.get("BucketName"),
            BucketOwner=json_data.get("BucketOwner"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3 = S3


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


