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
class AwsSignerSigningprofile(BaseModel):
    ProfileName: Optional[str]
    ProfileVersion: Optional[str]
    Arn: Optional[str]
    ProfileVersionArn: Optional[str]
    SignatureValidityPeriod: Optional["_SignatureValidityPeriod"]
    PlatformId: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSignerSigningprofile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSignerSigningprofile"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ProfileName=json_data.get("ProfileName"),
            ProfileVersion=json_data.get("ProfileVersion"),
            Arn=json_data.get("Arn"),
            ProfileVersionArn=json_data.get("ProfileVersionArn"),
            SignatureValidityPeriod=SignatureValidityPeriod._deserialize(json_data.get("SignatureValidityPeriod")),
            PlatformId=json_data.get("PlatformId"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSignerSigningprofile = AwsSignerSigningprofile


@dataclass
class SignatureValidityPeriod(BaseModel):
    Value: Optional[int]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SignatureValidityPeriod"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SignatureValidityPeriod"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SignatureValidityPeriod = SignatureValidityPeriod


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


