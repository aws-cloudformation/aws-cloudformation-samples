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
class AwsWorkspaceswebIpaccesssettings(BaseModel):
    AdditionalEncryptionContext: Optional[MutableMapping[str, str]]
    AssociatedPortalArns: Optional[Sequence[str]]
    CreationDate: Optional[str]
    CustomerManagedKey: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    IpAccessSettingsArn: Optional[str]
    IpRules: Optional[Sequence["_IpRule"]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsWorkspaceswebIpaccesssettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsWorkspaceswebIpaccesssettings"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AdditionalEncryptionContext=json_data.get("AdditionalEncryptionContext"),
            AssociatedPortalArns=json_data.get("AssociatedPortalArns"),
            CreationDate=json_data.get("CreationDate"),
            CustomerManagedKey=json_data.get("CustomerManagedKey"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            IpAccessSettingsArn=json_data.get("IpAccessSettingsArn"),
            IpRules=deserialize_list(json_data.get("IpRules"), IpRule),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsWorkspaceswebIpaccesssettings = AwsWorkspaceswebIpaccesssettings


@dataclass
class IpRule(BaseModel):
    IpRange: Optional[str]
    Description: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpRule"]:
        if not json_data:
            return None
        return cls(
            IpRange=json_data.get("IpRange"),
            Description=json_data.get("Description"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpRule = IpRule


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


