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
class AwsConnectSecurityprofile(BaseModel):
    AllowedAccessControlTags: Optional[AbstractSet["_Tag"]]
    Description: Optional[str]
    InstanceArn: Optional[str]
    Permissions: Optional[AbstractSet[str]]
    SecurityProfileArn: Optional[str]
    SecurityProfileName: Optional[str]
    TagRestrictedResources: Optional[AbstractSet[str]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConnectSecurityprofile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConnectSecurityprofile"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AllowedAccessControlTags=set_or_none(json_data.get("AllowedAccessControlTags")),
            Description=json_data.get("Description"),
            InstanceArn=json_data.get("InstanceArn"),
            Permissions=set_or_none(json_data.get("Permissions")),
            SecurityProfileArn=json_data.get("SecurityProfileArn"),
            SecurityProfileName=json_data.get("SecurityProfileName"),
            TagRestrictedResources=set_or_none(json_data.get("TagRestrictedResources")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConnectSecurityprofile = AwsConnectSecurityprofile


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


