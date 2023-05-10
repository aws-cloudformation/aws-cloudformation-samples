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
class AwsIotwirelessPartneraccount(BaseModel):
    Sidewalk: Optional["_SidewalkAccountInfo"]
    PartnerAccountId: Optional[str]
    PartnerType: Optional[str]
    SidewalkResponse: Optional["_SidewalkAccountInfoWithFingerprint"]
    AccountLinked: Optional[bool]
    SidewalkUpdate: Optional["_SidewalkUpdateAccount"]
    Fingerprint: Optional[str]
    Arn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotwirelessPartneraccount"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotwirelessPartneraccount"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Sidewalk=SidewalkAccountInfo._deserialize(json_data.get("Sidewalk")),
            PartnerAccountId=json_data.get("PartnerAccountId"),
            PartnerType=json_data.get("PartnerType"),
            SidewalkResponse=SidewalkAccountInfoWithFingerprint._deserialize(json_data.get("SidewalkResponse")),
            AccountLinked=json_data.get("AccountLinked"),
            SidewalkUpdate=SidewalkUpdateAccount._deserialize(json_data.get("SidewalkUpdate")),
            Fingerprint=json_data.get("Fingerprint"),
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotwirelessPartneraccount = AwsIotwirelessPartneraccount


@dataclass
class SidewalkAccountInfo(BaseModel):
    AppServerPrivateKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SidewalkAccountInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SidewalkAccountInfo"]:
        if not json_data:
            return None
        return cls(
            AppServerPrivateKey=json_data.get("AppServerPrivateKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SidewalkAccountInfo = SidewalkAccountInfo


@dataclass
class SidewalkAccountInfoWithFingerprint(BaseModel):
    AmazonId: Optional[str]
    Fingerprint: Optional[str]
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SidewalkAccountInfoWithFingerprint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SidewalkAccountInfoWithFingerprint"]:
        if not json_data:
            return None
        return cls(
            AmazonId=json_data.get("AmazonId"),
            Fingerprint=json_data.get("Fingerprint"),
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SidewalkAccountInfoWithFingerprint = SidewalkAccountInfoWithFingerprint


@dataclass
class SidewalkUpdateAccount(BaseModel):
    AppServerPrivateKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SidewalkUpdateAccount"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SidewalkUpdateAccount"]:
        if not json_data:
            return None
        return cls(
            AppServerPrivateKey=json_data.get("AppServerPrivateKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SidewalkUpdateAccount = SidewalkUpdateAccount


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


