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
class AwsAmazonmqBroker(BaseModel):
    SecurityGroups: Optional[Sequence[str]]
    Configuration: Optional["_ConfigurationId"]
    AuthenticationStrategy: Optional[str]
    Users: Optional[Sequence["_User"]]
    SubnetIds: Optional[Sequence[str]]
    StompEndpoints: Optional[Sequence[str]]
    MqttEndpoints: Optional[Sequence[str]]
    AmqpEndpoints: Optional[Sequence[str]]
    DeploymentMode: Optional[str]
    EngineType: Optional[str]
    EncryptionOptions: Optional["_EncryptionOptions"]
    Tags: Optional[Any]
    ConfigurationRevision: Optional[int]
    StorageType: Optional[str]
    EngineVersion: Optional[str]
    MaintenanceWindowStartTime: Optional["_MaintenanceWindow"]
    HostInstanceType: Optional[str]
    AutoMinorVersionUpgrade: Optional[bool]
    Logs: Optional["_LogList"]
    ConfigurationId: Optional[str]
    BrokerName: Optional[str]
    WssEndpoints: Optional[Sequence[str]]
    IpAddresses: Optional[Sequence[str]]
    OpenWireEndpoints: Optional[Sequence[str]]
    LdapServerMetadata: Optional["_LdapServerMetadata"]
    PubliclyAccessible: Optional[bool]
    Id: Optional[str]
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAmazonmqBroker"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAmazonmqBroker"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            SecurityGroups=json_data.get("SecurityGroups"),
            Configuration=ConfigurationId._deserialize(json_data.get("Configuration")),
            AuthenticationStrategy=json_data.get("AuthenticationStrategy"),
            Users=deserialize_list(json_data.get("Users"), User),
            SubnetIds=json_data.get("SubnetIds"),
            StompEndpoints=json_data.get("StompEndpoints"),
            MqttEndpoints=json_data.get("MqttEndpoints"),
            AmqpEndpoints=json_data.get("AmqpEndpoints"),
            DeploymentMode=json_data.get("DeploymentMode"),
            EngineType=json_data.get("EngineType"),
            EncryptionOptions=EncryptionOptions._deserialize(json_data.get("EncryptionOptions")),
            Tags=json_data.get("Tags"),
            ConfigurationRevision=json_data.get("ConfigurationRevision"),
            StorageType=json_data.get("StorageType"),
            EngineVersion=json_data.get("EngineVersion"),
            MaintenanceWindowStartTime=MaintenanceWindow._deserialize(json_data.get("MaintenanceWindowStartTime")),
            HostInstanceType=json_data.get("HostInstanceType"),
            AutoMinorVersionUpgrade=json_data.get("AutoMinorVersionUpgrade"),
            Logs=LogList._deserialize(json_data.get("Logs")),
            ConfigurationId=json_data.get("ConfigurationId"),
            BrokerName=json_data.get("BrokerName"),
            WssEndpoints=json_data.get("WssEndpoints"),
            IpAddresses=json_data.get("IpAddresses"),
            OpenWireEndpoints=json_data.get("OpenWireEndpoints"),
            LdapServerMetadata=LdapServerMetadata._deserialize(json_data.get("LdapServerMetadata")),
            PubliclyAccessible=json_data.get("PubliclyAccessible"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAmazonmqBroker = AwsAmazonmqBroker


@dataclass
class ConfigurationId(BaseModel):
    Revision: Optional[int]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationId"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationId"]:
        if not json_data:
            return None
        return cls(
            Revision=json_data.get("Revision"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationId = ConfigurationId


@dataclass
class User(BaseModel):
    ConsoleAccess: Optional[bool]
    Username: Optional[str]
    Groups: Optional[Sequence[str]]
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_User"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_User"]:
        if not json_data:
            return None
        return cls(
            ConsoleAccess=json_data.get("ConsoleAccess"),
            Username=json_data.get("Username"),
            Groups=json_data.get("Groups"),
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_User = User


@dataclass
class EncryptionOptions(BaseModel):
    KmsKeyId: Optional[str]
    UseAwsOwnedKey: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionOptions"]:
        if not json_data:
            return None
        return cls(
            KmsKeyId=json_data.get("KmsKeyId"),
            UseAwsOwnedKey=json_data.get("UseAwsOwnedKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionOptions = EncryptionOptions


@dataclass
class TagsEntry(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsEntry"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsEntry"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsEntry = TagsEntry


@dataclass
class MaintenanceWindow(BaseModel):
    DayOfWeek: Optional[str]
    TimeOfDay: Optional[str]
    TimeZone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindow"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindow"]:
        if not json_data:
            return None
        return cls(
            DayOfWeek=json_data.get("DayOfWeek"),
            TimeOfDay=json_data.get("TimeOfDay"),
            TimeZone=json_data.get("TimeZone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceWindow = MaintenanceWindow


@dataclass
class LogList(BaseModel):
    Audit: Optional[bool]
    General: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_LogList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogList"]:
        if not json_data:
            return None
        return cls(
            Audit=json_data.get("Audit"),
            General=json_data.get("General"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogList = LogList


@dataclass
class LdapServerMetadata(BaseModel):
    Hosts: Optional[Sequence[str]]
    UserRoleName: Optional[str]
    UserSearchMatching: Optional[str]
    RoleName: Optional[str]
    UserBase: Optional[str]
    UserSearchSubtree: Optional[bool]
    RoleSearchMatching: Optional[str]
    ServiceAccountUsername: Optional[str]
    RoleBase: Optional[str]
    ServiceAccountPassword: Optional[str]
    RoleSearchSubtree: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_LdapServerMetadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LdapServerMetadata"]:
        if not json_data:
            return None
        return cls(
            Hosts=json_data.get("Hosts"),
            UserRoleName=json_data.get("UserRoleName"),
            UserSearchMatching=json_data.get("UserSearchMatching"),
            RoleName=json_data.get("RoleName"),
            UserBase=json_data.get("UserBase"),
            UserSearchSubtree=json_data.get("UserSearchSubtree"),
            RoleSearchMatching=json_data.get("RoleSearchMatching"),
            ServiceAccountUsername=json_data.get("ServiceAccountUsername"),
            RoleBase=json_data.get("RoleBase"),
            ServiceAccountPassword=json_data.get("ServiceAccountPassword"),
            RoleSearchSubtree=json_data.get("RoleSearchSubtree"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LdapServerMetadata = LdapServerMetadata


