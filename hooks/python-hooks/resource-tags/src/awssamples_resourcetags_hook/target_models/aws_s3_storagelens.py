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
class AwsS3Storagelens(BaseModel):
    StorageLensConfiguration: Optional["_StorageLensConfiguration"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsS3Storagelens"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsS3Storagelens"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            StorageLensConfiguration=StorageLensConfiguration._deserialize(json_data.get("StorageLensConfiguration")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsS3Storagelens = AwsS3Storagelens


@dataclass
class StorageLensConfiguration(BaseModel):
    Id: Optional[str]
    Include: Optional["_BucketsAndRegions"]
    Exclude: Optional["_BucketsAndRegions"]
    AwsOrg: Optional["_AwsOrg"]
    AccountLevel: Optional["_AccountLevel"]
    DataExport: Optional["_DataExport"]
    IsEnabled: Optional[bool]
    StorageLensArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageLensConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageLensConfiguration"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Include=BucketsAndRegions._deserialize(json_data.get("Include")),
            Exclude=BucketsAndRegions._deserialize(json_data.get("Exclude")),
            AwsOrg=AwsOrg._deserialize(json_data.get("AwsOrg")),
            AccountLevel=AccountLevel._deserialize(json_data.get("AccountLevel")),
            DataExport=DataExport._deserialize(json_data.get("DataExport")),
            IsEnabled=json_data.get("IsEnabled"),
            StorageLensArn=json_data.get("StorageLensArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageLensConfiguration = StorageLensConfiguration


@dataclass
class BucketsAndRegions(BaseModel):
    Buckets: Optional[AbstractSet[str]]
    Regions: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_BucketsAndRegions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BucketsAndRegions"]:
        if not json_data:
            return None
        return cls(
            Buckets=set_or_none(json_data.get("Buckets")),
            Regions=set_or_none(json_data.get("Regions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BucketsAndRegions = BucketsAndRegions


@dataclass
class AwsOrg(BaseModel):
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsOrg"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsOrg"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsOrg = AwsOrg


@dataclass
class AccountLevel(BaseModel):
    ActivityMetrics: Optional["_ActivityMetrics"]
    AdvancedCostOptimizationMetrics: Optional["_AdvancedCostOptimizationMetrics"]
    AdvancedDataProtectionMetrics: Optional["_AdvancedDataProtectionMetrics"]
    DetailedStatusCodesMetrics: Optional["_DetailedStatusCodesMetrics"]
    BucketLevel: Optional["_BucketLevel"]

    @classmethod
    def _deserialize(
        cls: Type["_AccountLevel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccountLevel"]:
        if not json_data:
            return None
        return cls(
            ActivityMetrics=ActivityMetrics._deserialize(json_data.get("ActivityMetrics")),
            AdvancedCostOptimizationMetrics=AdvancedCostOptimizationMetrics._deserialize(json_data.get("AdvancedCostOptimizationMetrics")),
            AdvancedDataProtectionMetrics=AdvancedDataProtectionMetrics._deserialize(json_data.get("AdvancedDataProtectionMetrics")),
            DetailedStatusCodesMetrics=DetailedStatusCodesMetrics._deserialize(json_data.get("DetailedStatusCodesMetrics")),
            BucketLevel=BucketLevel._deserialize(json_data.get("BucketLevel")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccountLevel = AccountLevel


@dataclass
class ActivityMetrics(BaseModel):
    IsEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ActivityMetrics"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActivityMetrics"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActivityMetrics = ActivityMetrics


@dataclass
class AdvancedCostOptimizationMetrics(BaseModel):
    IsEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedCostOptimizationMetrics"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedCostOptimizationMetrics"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedCostOptimizationMetrics = AdvancedCostOptimizationMetrics


@dataclass
class AdvancedDataProtectionMetrics(BaseModel):
    IsEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedDataProtectionMetrics"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedDataProtectionMetrics"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedDataProtectionMetrics = AdvancedDataProtectionMetrics


@dataclass
class DetailedStatusCodesMetrics(BaseModel):
    IsEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DetailedStatusCodesMetrics"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DetailedStatusCodesMetrics"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DetailedStatusCodesMetrics = DetailedStatusCodesMetrics


@dataclass
class BucketLevel(BaseModel):
    ActivityMetrics: Optional["_ActivityMetrics"]
    AdvancedCostOptimizationMetrics: Optional["_AdvancedCostOptimizationMetrics"]
    AdvancedDataProtectionMetrics: Optional["_AdvancedDataProtectionMetrics"]
    DetailedStatusCodesMetrics: Optional["_DetailedStatusCodesMetrics"]
    PrefixLevel: Optional["_PrefixLevel"]

    @classmethod
    def _deserialize(
        cls: Type["_BucketLevel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BucketLevel"]:
        if not json_data:
            return None
        return cls(
            ActivityMetrics=ActivityMetrics._deserialize(json_data.get("ActivityMetrics")),
            AdvancedCostOptimizationMetrics=AdvancedCostOptimizationMetrics._deserialize(json_data.get("AdvancedCostOptimizationMetrics")),
            AdvancedDataProtectionMetrics=AdvancedDataProtectionMetrics._deserialize(json_data.get("AdvancedDataProtectionMetrics")),
            DetailedStatusCodesMetrics=DetailedStatusCodesMetrics._deserialize(json_data.get("DetailedStatusCodesMetrics")),
            PrefixLevel=PrefixLevel._deserialize(json_data.get("PrefixLevel")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BucketLevel = BucketLevel


@dataclass
class PrefixLevel(BaseModel):
    StorageMetrics: Optional["_PrefixLevelStorageMetrics"]

    @classmethod
    def _deserialize(
        cls: Type["_PrefixLevel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrefixLevel"]:
        if not json_data:
            return None
        return cls(
            StorageMetrics=PrefixLevelStorageMetrics._deserialize(json_data.get("StorageMetrics")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrefixLevel = PrefixLevel


@dataclass
class PrefixLevelStorageMetrics(BaseModel):
    IsEnabled: Optional[bool]
    SelectionCriteria: Optional["_SelectionCriteria"]

    @classmethod
    def _deserialize(
        cls: Type["_PrefixLevelStorageMetrics"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrefixLevelStorageMetrics"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            SelectionCriteria=SelectionCriteria._deserialize(json_data.get("SelectionCriteria")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrefixLevelStorageMetrics = PrefixLevelStorageMetrics


@dataclass
class SelectionCriteria(BaseModel):
    MaxDepth: Optional[int]
    Delimiter: Optional[str]
    MinStorageBytesPercentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SelectionCriteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelectionCriteria"]:
        if not json_data:
            return None
        return cls(
            MaxDepth=json_data.get("MaxDepth"),
            Delimiter=json_data.get("Delimiter"),
            MinStorageBytesPercentage=json_data.get("MinStorageBytesPercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelectionCriteria = SelectionCriteria


@dataclass
class DataExport(BaseModel):
    S3BucketDestination: Optional["_S3BucketDestination"]
    CloudWatchMetrics: Optional["_CloudWatchMetrics"]

    @classmethod
    def _deserialize(
        cls: Type["_DataExport"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataExport"]:
        if not json_data:
            return None
        return cls(
            S3BucketDestination=S3BucketDestination._deserialize(json_data.get("S3BucketDestination")),
            CloudWatchMetrics=CloudWatchMetrics._deserialize(json_data.get("CloudWatchMetrics")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataExport = DataExport


@dataclass
class S3BucketDestination(BaseModel):
    OutputSchemaVersion: Optional[str]
    Format: Optional[str]
    AccountId: Optional[str]
    Arn: Optional[str]
    Prefix: Optional[str]
    Encryption: Optional["_Encryption"]

    @classmethod
    def _deserialize(
        cls: Type["_S3BucketDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3BucketDestination"]:
        if not json_data:
            return None
        return cls(
            OutputSchemaVersion=json_data.get("OutputSchemaVersion"),
            Format=json_data.get("Format"),
            AccountId=json_data.get("AccountId"),
            Arn=json_data.get("Arn"),
            Prefix=json_data.get("Prefix"),
            Encryption=Encryption._deserialize(json_data.get("Encryption")),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3BucketDestination = S3BucketDestination


@dataclass
class Encryption(BaseModel):
    SSES3: Optional[MutableMapping[str, Any]]
    SSEKMS: Optional["_SSEKMS"]

    @classmethod
    def _deserialize(
        cls: Type["_Encryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Encryption"]:
        if not json_data:
            return None
        return cls(
            SSES3=json_data.get("SSES3"),
            SSEKMS=SSEKMS._deserialize(json_data.get("SSEKMS")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Encryption = Encryption


@dataclass
class SSEKMS(BaseModel):
    KeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SSEKMS"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SSEKMS"]:
        if not json_data:
            return None
        return cls(
            KeyId=json_data.get("KeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SSEKMS = SSEKMS


@dataclass
class CloudWatchMetrics(BaseModel):
    IsEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CloudWatchMetrics"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudWatchMetrics"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudWatchMetrics = CloudWatchMetrics


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


