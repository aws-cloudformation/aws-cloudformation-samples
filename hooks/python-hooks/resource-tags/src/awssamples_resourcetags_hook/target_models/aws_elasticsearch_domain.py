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
class AwsElasticsearchDomain(BaseModel):
    ElasticsearchClusterConfig: Optional["_ElasticsearchClusterConfig"]
    DomainName: Optional[str]
    ElasticsearchVersion: Optional[str]
    LogPublishingOptions: Optional[MutableMapping[str, "_LogPublishingOption"]]
    SnapshotOptions: Optional["_SnapshotOptions"]
    VPCOptions: Optional["_VPCOptions"]
    NodeToNodeEncryptionOptions: Optional["_NodeToNodeEncryptionOptions"]
    AccessPolicies: Optional[MutableMapping[str, Any]]
    DomainEndpointOptions: Optional["_DomainEndpointOptions"]
    DomainArn: Optional[str]
    CognitoOptions: Optional["_CognitoOptions"]
    AdvancedOptions: Optional[MutableMapping[str, str]]
    AdvancedSecurityOptions: Optional["_AdvancedSecurityOptionsInput"]
    DomainEndpoint: Optional[str]
    EBSOptions: Optional["_EBSOptions"]
    Id: Optional[str]
    Arn: Optional[str]
    EncryptionAtRestOptions: Optional["_EncryptionAtRestOptions"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsElasticsearchDomain"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsElasticsearchDomain"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ElasticsearchClusterConfig=ElasticsearchClusterConfig._deserialize(json_data.get("ElasticsearchClusterConfig")),
            DomainName=json_data.get("DomainName"),
            ElasticsearchVersion=json_data.get("ElasticsearchVersion"),
            LogPublishingOptions=json_data.get("LogPublishingOptions"),
            SnapshotOptions=SnapshotOptions._deserialize(json_data.get("SnapshotOptions")),
            VPCOptions=VPCOptions._deserialize(json_data.get("VPCOptions")),
            NodeToNodeEncryptionOptions=NodeToNodeEncryptionOptions._deserialize(json_data.get("NodeToNodeEncryptionOptions")),
            AccessPolicies=json_data.get("AccessPolicies"),
            DomainEndpointOptions=DomainEndpointOptions._deserialize(json_data.get("DomainEndpointOptions")),
            DomainArn=json_data.get("DomainArn"),
            CognitoOptions=CognitoOptions._deserialize(json_data.get("CognitoOptions")),
            AdvancedOptions=json_data.get("AdvancedOptions"),
            AdvancedSecurityOptions=AdvancedSecurityOptionsInput._deserialize(json_data.get("AdvancedSecurityOptions")),
            DomainEndpoint=json_data.get("DomainEndpoint"),
            EBSOptions=EBSOptions._deserialize(json_data.get("EBSOptions")),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            EncryptionAtRestOptions=EncryptionAtRestOptions._deserialize(json_data.get("EncryptionAtRestOptions")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsElasticsearchDomain = AwsElasticsearchDomain


@dataclass
class ElasticsearchClusterConfig(BaseModel):
    InstanceCount: Optional[int]
    WarmEnabled: Optional[bool]
    WarmCount: Optional[int]
    DedicatedMasterEnabled: Optional[bool]
    ZoneAwarenessConfig: Optional["_ZoneAwarenessConfig"]
    ColdStorageOptions: Optional["_ColdStorageOptions"]
    DedicatedMasterCount: Optional[int]
    InstanceType: Optional[str]
    WarmType: Optional[str]
    ZoneAwarenessEnabled: Optional[bool]
    DedicatedMasterType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticsearchClusterConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticsearchClusterConfig"]:
        if not json_data:
            return None
        return cls(
            InstanceCount=json_data.get("InstanceCount"),
            WarmEnabled=json_data.get("WarmEnabled"),
            WarmCount=json_data.get("WarmCount"),
            DedicatedMasterEnabled=json_data.get("DedicatedMasterEnabled"),
            ZoneAwarenessConfig=ZoneAwarenessConfig._deserialize(json_data.get("ZoneAwarenessConfig")),
            ColdStorageOptions=ColdStorageOptions._deserialize(json_data.get("ColdStorageOptions")),
            DedicatedMasterCount=json_data.get("DedicatedMasterCount"),
            InstanceType=json_data.get("InstanceType"),
            WarmType=json_data.get("WarmType"),
            ZoneAwarenessEnabled=json_data.get("ZoneAwarenessEnabled"),
            DedicatedMasterType=json_data.get("DedicatedMasterType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticsearchClusterConfig = ElasticsearchClusterConfig


@dataclass
class ZoneAwarenessConfig(BaseModel):
    AvailabilityZoneCount: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ZoneAwarenessConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZoneAwarenessConfig"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZoneCount=json_data.get("AvailabilityZoneCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZoneAwarenessConfig = ZoneAwarenessConfig


@dataclass
class ColdStorageOptions(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ColdStorageOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ColdStorageOptions"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ColdStorageOptions = ColdStorageOptions


@dataclass
class LogPublishingOption(BaseModel):
    CloudWatchLogsLogGroupArn: Optional[str]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_LogPublishingOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogPublishingOption"]:
        if not json_data:
            return None
        return cls(
            CloudWatchLogsLogGroupArn=json_data.get("CloudWatchLogsLogGroupArn"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogPublishingOption = LogPublishingOption


@dataclass
class SnapshotOptions(BaseModel):
    AutomatedSnapshotStartHour: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotOptions"]:
        if not json_data:
            return None
        return cls(
            AutomatedSnapshotStartHour=json_data.get("AutomatedSnapshotStartHour"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotOptions = SnapshotOptions


@dataclass
class VPCOptions(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VPCOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VPCOptions"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VPCOptions = VPCOptions


@dataclass
class NodeToNodeEncryptionOptions(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_NodeToNodeEncryptionOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeToNodeEncryptionOptions"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeToNodeEncryptionOptions = NodeToNodeEncryptionOptions


@dataclass
class DomainEndpointOptions(BaseModel):
    CustomEndpointCertificateArn: Optional[str]
    CustomEndpointEnabled: Optional[bool]
    EnforceHTTPS: Optional[bool]
    CustomEndpoint: Optional[str]
    TLSSecurityPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DomainEndpointOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainEndpointOptions"]:
        if not json_data:
            return None
        return cls(
            CustomEndpointCertificateArn=json_data.get("CustomEndpointCertificateArn"),
            CustomEndpointEnabled=json_data.get("CustomEndpointEnabled"),
            EnforceHTTPS=json_data.get("EnforceHTTPS"),
            CustomEndpoint=json_data.get("CustomEndpoint"),
            TLSSecurityPolicy=json_data.get("TLSSecurityPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainEndpointOptions = DomainEndpointOptions


@dataclass
class CognitoOptions(BaseModel):
    Enabled: Optional[bool]
    IdentityPoolId: Optional[str]
    UserPoolId: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CognitoOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CognitoOptions"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            IdentityPoolId=json_data.get("IdentityPoolId"),
            UserPoolId=json_data.get("UserPoolId"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CognitoOptions = CognitoOptions


@dataclass
class AdvancedSecurityOptionsInput(BaseModel):
    Enabled: Optional[bool]
    MasterUserOptions: Optional["_MasterUserOptions"]
    AnonymousAuthEnabled: Optional[bool]
    InternalUserDatabaseEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedSecurityOptionsInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedSecurityOptionsInput"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            MasterUserOptions=MasterUserOptions._deserialize(json_data.get("MasterUserOptions")),
            AnonymousAuthEnabled=json_data.get("AnonymousAuthEnabled"),
            InternalUserDatabaseEnabled=json_data.get("InternalUserDatabaseEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedSecurityOptionsInput = AdvancedSecurityOptionsInput


@dataclass
class MasterUserOptions(BaseModel):
    MasterUserPassword: Optional[str]
    MasterUserName: Optional[str]
    MasterUserARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MasterUserOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MasterUserOptions"]:
        if not json_data:
            return None
        return cls(
            MasterUserPassword=json_data.get("MasterUserPassword"),
            MasterUserName=json_data.get("MasterUserName"),
            MasterUserARN=json_data.get("MasterUserARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MasterUserOptions = MasterUserOptions


@dataclass
class EBSOptions(BaseModel):
    EBSEnabled: Optional[bool]
    VolumeType: Optional[str]
    Iops: Optional[int]
    VolumeSize: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_EBSOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EBSOptions"]:
        if not json_data:
            return None
        return cls(
            EBSEnabled=json_data.get("EBSEnabled"),
            VolumeType=json_data.get("VolumeType"),
            Iops=json_data.get("Iops"),
            VolumeSize=json_data.get("VolumeSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EBSOptions = EBSOptions


@dataclass
class EncryptionAtRestOptions(BaseModel):
    KmsKeyId: Optional[str]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionAtRestOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionAtRestOptions"]:
        if not json_data:
            return None
        return cls(
            KmsKeyId=json_data.get("KmsKeyId"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionAtRestOptions = EncryptionAtRestOptions


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


