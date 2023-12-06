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
class AwsS3Accessgrant(BaseModel):
    AccessGrantId: Optional[str]
    AccessGrantsLocationId: Optional[str]
    Tags: Optional[Any]
    Permission: Optional[str]
    ApplicationArn: Optional[str]
    S3PrefixType: Optional[str]
    GrantScope: Optional[str]
    AccessGrantArn: Optional[str]
    Grantee: Optional["_Grantee"]
    AccessGrantsLocationConfiguration: Optional["_AccessGrantsLocationConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsS3Accessgrant"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsS3Accessgrant"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AccessGrantId=json_data.get("AccessGrantId"),
            AccessGrantsLocationId=json_data.get("AccessGrantsLocationId"),
            Tags=json_data.get("Tags"),
            Permission=json_data.get("Permission"),
            ApplicationArn=json_data.get("ApplicationArn"),
            S3PrefixType=json_data.get("S3PrefixType"),
            GrantScope=json_data.get("GrantScope"),
            AccessGrantArn=json_data.get("AccessGrantArn"),
            Grantee=Grantee._deserialize(json_data.get("Grantee")),
            AccessGrantsLocationConfiguration=AccessGrantsLocationConfiguration._deserialize(json_data.get("AccessGrantsLocationConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsS3Accessgrant = AwsS3Accessgrant


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
class Grantee(BaseModel):
    GranteeType: Optional[str]
    GranteeIdentifier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Grantee"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Grantee"]:
        if not json_data:
            return None
        return cls(
            GranteeType=json_data.get("GranteeType"),
            GranteeIdentifier=json_data.get("GranteeIdentifier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Grantee = Grantee


@dataclass
class AccessGrantsLocationConfiguration(BaseModel):
    S3SubPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessGrantsLocationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessGrantsLocationConfiguration"]:
        if not json_data:
            return None
        return cls(
            S3SubPrefix=json_data.get("S3SubPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessGrantsLocationConfiguration = AccessGrantsLocationConfiguration


