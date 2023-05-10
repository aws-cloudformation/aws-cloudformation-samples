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
class AwsAppstreamStack(BaseModel):
    Description: Optional[str]
    StorageConnectors: Optional[Sequence["_StorageConnector"]]
    DeleteStorageConnectors: Optional[bool]
    EmbedHostDomains: Optional[Sequence[str]]
    UserSettings: Optional[Sequence["_UserSetting"]]
    AttributesToDelete: Optional[Sequence[str]]
    RedirectURL: Optional[str]
    StreamingExperienceSettings: Optional["_StreamingExperienceSettings"]
    Name: Optional[str]
    FeedbackURL: Optional[str]
    ApplicationSettings: Optional["_ApplicationSettings"]
    DisplayName: Optional[str]
    Id: Optional[str]
    Tags: Optional[Any]
    AccessEndpoints: Optional[Sequence["_AccessEndpoint"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppstreamStack"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppstreamStack"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            StorageConnectors=deserialize_list(json_data.get("StorageConnectors"), StorageConnector),
            DeleteStorageConnectors=json_data.get("DeleteStorageConnectors"),
            EmbedHostDomains=json_data.get("EmbedHostDomains"),
            UserSettings=deserialize_list(json_data.get("UserSettings"), UserSetting),
            AttributesToDelete=json_data.get("AttributesToDelete"),
            RedirectURL=json_data.get("RedirectURL"),
            StreamingExperienceSettings=StreamingExperienceSettings._deserialize(json_data.get("StreamingExperienceSettings")),
            Name=json_data.get("Name"),
            FeedbackURL=json_data.get("FeedbackURL"),
            ApplicationSettings=ApplicationSettings._deserialize(json_data.get("ApplicationSettings")),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
            AccessEndpoints=deserialize_list(json_data.get("AccessEndpoints"), AccessEndpoint),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppstreamStack = AwsAppstreamStack


@dataclass
class StorageConnector(BaseModel):
    Domains: Optional[Sequence[str]]
    ResourceIdentifier: Optional[str]
    ConnectorType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageConnector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageConnector"]:
        if not json_data:
            return None
        return cls(
            Domains=json_data.get("Domains"),
            ResourceIdentifier=json_data.get("ResourceIdentifier"),
            ConnectorType=json_data.get("ConnectorType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageConnector = StorageConnector


@dataclass
class UserSetting(BaseModel):
    Permission: Optional[str]
    Action: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserSetting"]:
        if not json_data:
            return None
        return cls(
            Permission=json_data.get("Permission"),
            Action=json_data.get("Action"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserSetting = UserSetting


@dataclass
class StreamingExperienceSettings(BaseModel):
    PreferredProtocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StreamingExperienceSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StreamingExperienceSettings"]:
        if not json_data:
            return None
        return cls(
            PreferredProtocol=json_data.get("PreferredProtocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StreamingExperienceSettings = StreamingExperienceSettings


@dataclass
class ApplicationSettings(BaseModel):
    SettingsGroup: Optional[str]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationSettings"]:
        if not json_data:
            return None
        return cls(
            SettingsGroup=json_data.get("SettingsGroup"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationSettings = ApplicationSettings


@dataclass
class Tag(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


@dataclass
class AccessEndpoint(BaseModel):
    EndpointType: Optional[str]
    VpceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessEndpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessEndpoint"]:
        if not json_data:
            return None
        return cls(
            EndpointType=json_data.get("EndpointType"),
            VpceId=json_data.get("VpceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessEndpoint = AccessEndpoint


