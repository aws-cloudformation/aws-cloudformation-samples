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
class AwsCloudfrontStreamingdistribution(BaseModel):
    Id: Optional[str]
    DomainName: Optional[str]
    StreamingDistributionConfig: Optional["_StreamingDistributionConfig"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudfrontStreamingdistribution"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudfrontStreamingdistribution"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            DomainName=json_data.get("DomainName"),
            StreamingDistributionConfig=StreamingDistributionConfig._deserialize(json_data.get("StreamingDistributionConfig")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudfrontStreamingdistribution = AwsCloudfrontStreamingdistribution


@dataclass
class StreamingDistributionConfig(BaseModel):
    Logging: Optional["_Logging"]
    Comment: Optional[str]
    PriceClass: Optional[str]
    S3Origin: Optional["_S3Origin"]
    Enabled: Optional[bool]
    Aliases: Optional[Sequence[str]]
    TrustedSigners: Optional["_TrustedSigners"]

    @classmethod
    def _deserialize(
        cls: Type["_StreamingDistributionConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StreamingDistributionConfig"]:
        if not json_data:
            return None
        return cls(
            Logging=Logging._deserialize(json_data.get("Logging")),
            Comment=json_data.get("Comment"),
            PriceClass=json_data.get("PriceClass"),
            S3Origin=S3Origin._deserialize(json_data.get("S3Origin")),
            Enabled=json_data.get("Enabled"),
            Aliases=json_data.get("Aliases"),
            TrustedSigners=TrustedSigners._deserialize(json_data.get("TrustedSigners")),
        )


# work around possible type aliasing issues when variable has same name as a model
_StreamingDistributionConfig = StreamingDistributionConfig


@dataclass
class Logging(BaseModel):
    Bucket: Optional[str]
    Enabled: Optional[bool]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Logging"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Logging"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Enabled=json_data.get("Enabled"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Logging = Logging


@dataclass
class S3Origin(BaseModel):
    DomainName: Optional[str]
    OriginAccessIdentity: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Origin"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Origin"]:
        if not json_data:
            return None
        return cls(
            DomainName=json_data.get("DomainName"),
            OriginAccessIdentity=json_data.get("OriginAccessIdentity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Origin = S3Origin


@dataclass
class TrustedSigners(BaseModel):
    Enabled: Optional[bool]
    AwsAccountNumbers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TrustedSigners"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrustedSigners"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            AwsAccountNumbers=json_data.get("AwsAccountNumbers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrustedSigners = TrustedSigners


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


