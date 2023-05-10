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
class AwsRolesanywhereTrustanchor(BaseModel):
    Enabled: Optional[bool]
    Name: Optional[str]
    Source: Optional["_Source"]
    Tags: Optional[Any]
    TrustAnchorId: Optional[str]
    TrustAnchorArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRolesanywhereTrustanchor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRolesanywhereTrustanchor"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Enabled=json_data.get("Enabled"),
            Name=json_data.get("Name"),
            Source=Source._deserialize(json_data.get("Source")),
            Tags=json_data.get("Tags"),
            TrustAnchorId=json_data.get("TrustAnchorId"),
            TrustAnchorArn=json_data.get("TrustAnchorArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRolesanywhereTrustanchor = AwsRolesanywhereTrustanchor


@dataclass
class Source(BaseModel):
    SourceType: Optional[str]
    SourceData: Optional["_SourceData"]

    @classmethod
    def _deserialize(
        cls: Type["_Source"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Source"]:
        if not json_data:
            return None
        return cls(
            SourceType=json_data.get("SourceType"),
            SourceData=SourceData._deserialize(json_data.get("SourceData")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Source = Source


@dataclass
class SourceData(BaseModel):
    X509CertificateData: Optional[str]
    AcmPcaArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceData"]:
        if not json_data:
            return None
        return cls(
            X509CertificateData=json_data.get("X509CertificateData"),
            AcmPcaArn=json_data.get("AcmPcaArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceData = SourceData


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


