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
class AwsAthenaWorkgroup(BaseModel):
    Name: Optional[str]
    Description: Optional[str]
    Tags: Optional[Any]
    WorkGroupConfiguration: Optional["_WorkGroupConfiguration"]
    WorkGroupConfigurationUpdates: Optional["_WorkGroupConfigurationUpdates"]
    CreationTime: Optional[str]
    State: Optional[str]
    RecursiveDeleteOption: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAthenaWorkgroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAthenaWorkgroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            Tags=json_data.get("Tags"),
            WorkGroupConfiguration=WorkGroupConfiguration._deserialize(json_data.get("WorkGroupConfiguration")),
            WorkGroupConfigurationUpdates=WorkGroupConfigurationUpdates._deserialize(json_data.get("WorkGroupConfigurationUpdates")),
            CreationTime=json_data.get("CreationTime"),
            State=json_data.get("State"),
            RecursiveDeleteOption=json_data.get("RecursiveDeleteOption"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAthenaWorkgroup = AwsAthenaWorkgroup


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
class WorkGroupConfiguration(BaseModel):
    BytesScannedCutoffPerQuery: Optional[int]
    EnforceWorkGroupConfiguration: Optional[bool]
    PublishCloudWatchMetricsEnabled: Optional[bool]
    RequesterPaysEnabled: Optional[bool]
    ResultConfiguration: Optional["_ResultConfiguration"]
    EngineVersion: Optional["_EngineVersion"]
    AdditionalConfiguration: Optional[str]
    ExecutionRole: Optional[str]
    CustomerContentEncryptionConfiguration: Optional["_CustomerContentEncryptionConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_WorkGroupConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkGroupConfiguration"]:
        if not json_data:
            return None
        return cls(
            BytesScannedCutoffPerQuery=json_data.get("BytesScannedCutoffPerQuery"),
            EnforceWorkGroupConfiguration=json_data.get("EnforceWorkGroupConfiguration"),
            PublishCloudWatchMetricsEnabled=json_data.get("PublishCloudWatchMetricsEnabled"),
            RequesterPaysEnabled=json_data.get("RequesterPaysEnabled"),
            ResultConfiguration=ResultConfiguration._deserialize(json_data.get("ResultConfiguration")),
            EngineVersion=EngineVersion._deserialize(json_data.get("EngineVersion")),
            AdditionalConfiguration=json_data.get("AdditionalConfiguration"),
            ExecutionRole=json_data.get("ExecutionRole"),
            CustomerContentEncryptionConfiguration=CustomerContentEncryptionConfiguration._deserialize(json_data.get("CustomerContentEncryptionConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkGroupConfiguration = WorkGroupConfiguration


@dataclass
class ResultConfiguration(BaseModel):
    EncryptionConfiguration: Optional["_EncryptionConfiguration"]
    OutputLocation: Optional[str]
    ExpectedBucketOwner: Optional[str]
    AclConfiguration: Optional["_AclConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ResultConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResultConfiguration"]:
        if not json_data:
            return None
        return cls(
            EncryptionConfiguration=EncryptionConfiguration._deserialize(json_data.get("EncryptionConfiguration")),
            OutputLocation=json_data.get("OutputLocation"),
            ExpectedBucketOwner=json_data.get("ExpectedBucketOwner"),
            AclConfiguration=AclConfiguration._deserialize(json_data.get("AclConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResultConfiguration = ResultConfiguration


@dataclass
class EncryptionConfiguration(BaseModel):
    EncryptionOption: Optional[str]
    KmsKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfiguration"]:
        if not json_data:
            return None
        return cls(
            EncryptionOption=json_data.get("EncryptionOption"),
            KmsKey=json_data.get("KmsKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfiguration = EncryptionConfiguration


@dataclass
class AclConfiguration(BaseModel):
    S3AclOption: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AclConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AclConfiguration"]:
        if not json_data:
            return None
        return cls(
            S3AclOption=json_data.get("S3AclOption"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AclConfiguration = AclConfiguration


@dataclass
class EngineVersion(BaseModel):
    SelectedEngineVersion: Optional[str]
    EffectiveEngineVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EngineVersion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EngineVersion"]:
        if not json_data:
            return None
        return cls(
            SelectedEngineVersion=json_data.get("SelectedEngineVersion"),
            EffectiveEngineVersion=json_data.get("EffectiveEngineVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EngineVersion = EngineVersion


@dataclass
class CustomerContentEncryptionConfiguration(BaseModel):
    KmsKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomerContentEncryptionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomerContentEncryptionConfiguration"]:
        if not json_data:
            return None
        return cls(
            KmsKey=json_data.get("KmsKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomerContentEncryptionConfiguration = CustomerContentEncryptionConfiguration


@dataclass
class WorkGroupConfigurationUpdates(BaseModel):
    BytesScannedCutoffPerQuery: Optional[int]
    EnforceWorkGroupConfiguration: Optional[bool]
    PublishCloudWatchMetricsEnabled: Optional[bool]
    RequesterPaysEnabled: Optional[bool]
    ResultConfigurationUpdates: Optional["_ResultConfigurationUpdates"]
    RemoveBytesScannedCutoffPerQuery: Optional[bool]
    EngineVersion: Optional["_EngineVersion"]
    AdditionalConfiguration: Optional[str]
    ExecutionRole: Optional[str]
    CustomerContentEncryptionConfiguration: Optional["_CustomerContentEncryptionConfiguration"]
    RemoveCustomerContentEncryptionConfiguration: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_WorkGroupConfigurationUpdates"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkGroupConfigurationUpdates"]:
        if not json_data:
            return None
        return cls(
            BytesScannedCutoffPerQuery=json_data.get("BytesScannedCutoffPerQuery"),
            EnforceWorkGroupConfiguration=json_data.get("EnforceWorkGroupConfiguration"),
            PublishCloudWatchMetricsEnabled=json_data.get("PublishCloudWatchMetricsEnabled"),
            RequesterPaysEnabled=json_data.get("RequesterPaysEnabled"),
            ResultConfigurationUpdates=ResultConfigurationUpdates._deserialize(json_data.get("ResultConfigurationUpdates")),
            RemoveBytesScannedCutoffPerQuery=json_data.get("RemoveBytesScannedCutoffPerQuery"),
            EngineVersion=EngineVersion._deserialize(json_data.get("EngineVersion")),
            AdditionalConfiguration=json_data.get("AdditionalConfiguration"),
            ExecutionRole=json_data.get("ExecutionRole"),
            CustomerContentEncryptionConfiguration=CustomerContentEncryptionConfiguration._deserialize(json_data.get("CustomerContentEncryptionConfiguration")),
            RemoveCustomerContentEncryptionConfiguration=json_data.get("RemoveCustomerContentEncryptionConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkGroupConfigurationUpdates = WorkGroupConfigurationUpdates


@dataclass
class ResultConfigurationUpdates(BaseModel):
    EncryptionConfiguration: Optional["_EncryptionConfiguration"]
    OutputLocation: Optional[str]
    ExpectedBucketOwner: Optional[str]
    AclConfiguration: Optional["_AclConfiguration"]
    RemoveEncryptionConfiguration: Optional[bool]
    RemoveOutputLocation: Optional[bool]
    RemoveExpectedBucketOwner: Optional[bool]
    RemoveAclConfiguration: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResultConfigurationUpdates"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResultConfigurationUpdates"]:
        if not json_data:
            return None
        return cls(
            EncryptionConfiguration=EncryptionConfiguration._deserialize(json_data.get("EncryptionConfiguration")),
            OutputLocation=json_data.get("OutputLocation"),
            ExpectedBucketOwner=json_data.get("ExpectedBucketOwner"),
            AclConfiguration=AclConfiguration._deserialize(json_data.get("AclConfiguration")),
            RemoveEncryptionConfiguration=json_data.get("RemoveEncryptionConfiguration"),
            RemoveOutputLocation=json_data.get("RemoveOutputLocation"),
            RemoveExpectedBucketOwner=json_data.get("RemoveExpectedBucketOwner"),
            RemoveAclConfiguration=json_data.get("RemoveAclConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResultConfigurationUpdates = ResultConfigurationUpdates


