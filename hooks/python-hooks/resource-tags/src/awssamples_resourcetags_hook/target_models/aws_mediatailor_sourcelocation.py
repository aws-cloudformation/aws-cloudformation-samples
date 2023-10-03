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
class AwsMediatailorSourcelocation(BaseModel):
    AccessConfiguration: Optional["_AccessConfiguration"]
    Arn: Optional[str]
    DefaultSegmentDeliveryConfiguration: Optional["_DefaultSegmentDeliveryConfiguration"]
    HttpConfiguration: Optional["_HttpConfiguration"]
    SegmentDeliveryConfigurations: Optional[Sequence["_SegmentDeliveryConfiguration"]]
    SourceLocationName: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMediatailorSourcelocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMediatailorSourcelocation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AccessConfiguration=AccessConfiguration._deserialize(json_data.get("AccessConfiguration")),
            Arn=json_data.get("Arn"),
            DefaultSegmentDeliveryConfiguration=DefaultSegmentDeliveryConfiguration._deserialize(json_data.get("DefaultSegmentDeliveryConfiguration")),
            HttpConfiguration=HttpConfiguration._deserialize(json_data.get("HttpConfiguration")),
            SegmentDeliveryConfigurations=deserialize_list(json_data.get("SegmentDeliveryConfigurations"), SegmentDeliveryConfiguration),
            SourceLocationName=json_data.get("SourceLocationName"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMediatailorSourcelocation = AwsMediatailorSourcelocation


@dataclass
class AccessConfiguration(BaseModel):
    AccessType: Optional[str]
    SecretsManagerAccessTokenConfiguration: Optional["_SecretsManagerAccessTokenConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AccessConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessConfiguration"]:
        if not json_data:
            return None
        return cls(
            AccessType=json_data.get("AccessType"),
            SecretsManagerAccessTokenConfiguration=SecretsManagerAccessTokenConfiguration._deserialize(json_data.get("SecretsManagerAccessTokenConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessConfiguration = AccessConfiguration


@dataclass
class SecretsManagerAccessTokenConfiguration(BaseModel):
    HeaderName: Optional[str]
    SecretArn: Optional[str]
    SecretStringKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecretsManagerAccessTokenConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecretsManagerAccessTokenConfiguration"]:
        if not json_data:
            return None
        return cls(
            HeaderName=json_data.get("HeaderName"),
            SecretArn=json_data.get("SecretArn"),
            SecretStringKey=json_data.get("SecretStringKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecretsManagerAccessTokenConfiguration = SecretsManagerAccessTokenConfiguration


@dataclass
class DefaultSegmentDeliveryConfiguration(BaseModel):
    BaseUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultSegmentDeliveryConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultSegmentDeliveryConfiguration"]:
        if not json_data:
            return None
        return cls(
            BaseUrl=json_data.get("BaseUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultSegmentDeliveryConfiguration = DefaultSegmentDeliveryConfiguration


@dataclass
class HttpConfiguration(BaseModel):
    BaseUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpConfiguration"]:
        if not json_data:
            return None
        return cls(
            BaseUrl=json_data.get("BaseUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpConfiguration = HttpConfiguration


@dataclass
class SegmentDeliveryConfiguration(BaseModel):
    BaseUrl: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SegmentDeliveryConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SegmentDeliveryConfiguration"]:
        if not json_data:
            return None
        return cls(
            BaseUrl=json_data.get("BaseUrl"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SegmentDeliveryConfiguration = SegmentDeliveryConfiguration


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


