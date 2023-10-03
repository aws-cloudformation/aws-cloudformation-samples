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
class AwsWorkspaceswebUsersettings(BaseModel):
    AdditionalEncryptionContext: Optional[MutableMapping[str, str]]
    AssociatedPortalArns: Optional[Sequence[str]]
    CookieSynchronizationConfiguration: Optional["_CookieSynchronizationConfiguration"]
    CopyAllowed: Optional[str]
    CustomerManagedKey: Optional[str]
    DisconnectTimeoutInMinutes: Optional[float]
    DownloadAllowed: Optional[str]
    IdleDisconnectTimeoutInMinutes: Optional[float]
    PasteAllowed: Optional[str]
    PrintAllowed: Optional[str]
    Tags: Optional[Any]
    UploadAllowed: Optional[str]
    UserSettingsArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsWorkspaceswebUsersettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsWorkspaceswebUsersettings"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AdditionalEncryptionContext=json_data.get("AdditionalEncryptionContext"),
            AssociatedPortalArns=json_data.get("AssociatedPortalArns"),
            CookieSynchronizationConfiguration=CookieSynchronizationConfiguration._deserialize(json_data.get("CookieSynchronizationConfiguration")),
            CopyAllowed=json_data.get("CopyAllowed"),
            CustomerManagedKey=json_data.get("CustomerManagedKey"),
            DisconnectTimeoutInMinutes=json_data.get("DisconnectTimeoutInMinutes"),
            DownloadAllowed=json_data.get("DownloadAllowed"),
            IdleDisconnectTimeoutInMinutes=json_data.get("IdleDisconnectTimeoutInMinutes"),
            PasteAllowed=json_data.get("PasteAllowed"),
            PrintAllowed=json_data.get("PrintAllowed"),
            Tags=json_data.get("Tags"),
            UploadAllowed=json_data.get("UploadAllowed"),
            UserSettingsArn=json_data.get("UserSettingsArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsWorkspaceswebUsersettings = AwsWorkspaceswebUsersettings


@dataclass
class CookieSynchronizationConfiguration(BaseModel):
    Allowlist: Optional[Sequence["_CookieSpecification"]]
    Blocklist: Optional[Sequence["_CookieSpecification"]]

    @classmethod
    def _deserialize(
        cls: Type["_CookieSynchronizationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CookieSynchronizationConfiguration"]:
        if not json_data:
            return None
        return cls(
            Allowlist=deserialize_list(json_data.get("Allowlist"), CookieSpecification),
            Blocklist=deserialize_list(json_data.get("Blocklist"), CookieSpecification),
        )


# work around possible type aliasing issues when variable has same name as a model
_CookieSynchronizationConfiguration = CookieSynchronizationConfiguration


@dataclass
class CookieSpecification(BaseModel):
    Domain: Optional[str]
    Name: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CookieSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CookieSpecification"]:
        if not json_data:
            return None
        return cls(
            Domain=json_data.get("Domain"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CookieSpecification = CookieSpecification


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


