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
class AwsCustomerprofilesDomain(BaseModel):
    DomainName: Optional[str]
    DeadLetterQueueUrl: Optional[str]
    DefaultEncryptionKey: Optional[str]
    DefaultExpirationDays: Optional[int]
    Matching: Optional["_Matching"]
    RuleBasedMatching: Optional["_RuleBasedMatching"]
    Stats: Optional["_DomainStats"]
    Tags: Optional[Any]
    CreatedAt: Optional[str]
    LastUpdatedAt: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCustomerprofilesDomain"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCustomerprofilesDomain"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DomainName=json_data.get("DomainName"),
            DeadLetterQueueUrl=json_data.get("DeadLetterQueueUrl"),
            DefaultEncryptionKey=json_data.get("DefaultEncryptionKey"),
            DefaultExpirationDays=json_data.get("DefaultExpirationDays"),
            Matching=Matching._deserialize(json_data.get("Matching")),
            RuleBasedMatching=RuleBasedMatching._deserialize(json_data.get("RuleBasedMatching")),
            Stats=DomainStats._deserialize(json_data.get("Stats")),
            Tags=json_data.get("Tags"),
            CreatedAt=json_data.get("CreatedAt"),
            LastUpdatedAt=json_data.get("LastUpdatedAt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCustomerprofilesDomain = AwsCustomerprofilesDomain


@dataclass
class Matching(BaseModel):
    Enabled: Optional[bool]
    AutoMerging: Optional["_AutoMerging"]
    ExportingConfig: Optional["_ExportingConfig"]
    JobSchedule: Optional["_JobSchedule"]

    @classmethod
    def _deserialize(
        cls: Type["_Matching"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Matching"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            AutoMerging=AutoMerging._deserialize(json_data.get("AutoMerging")),
            ExportingConfig=ExportingConfig._deserialize(json_data.get("ExportingConfig")),
            JobSchedule=JobSchedule._deserialize(json_data.get("JobSchedule")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Matching = Matching


@dataclass
class AutoMerging(BaseModel):
    Enabled: Optional[bool]
    ConflictResolution: Optional["_ConflictResolution"]
    Consolidation: Optional["_Consolidation"]
    MinAllowedConfidenceScoreForMerging: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AutoMerging"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoMerging"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            ConflictResolution=ConflictResolution._deserialize(json_data.get("ConflictResolution")),
            Consolidation=Consolidation._deserialize(json_data.get("Consolidation")),
            MinAllowedConfidenceScoreForMerging=json_data.get("MinAllowedConfidenceScoreForMerging"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoMerging = AutoMerging


@dataclass
class ConflictResolution(BaseModel):
    ConflictResolvingModel: Optional[str]
    SourceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConflictResolution"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConflictResolution"]:
        if not json_data:
            return None
        return cls(
            ConflictResolvingModel=json_data.get("ConflictResolvingModel"),
            SourceName=json_data.get("SourceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConflictResolution = ConflictResolution


@dataclass
class Consolidation(BaseModel):
    MatchingAttributesList: Optional[Sequence[Sequence[str]]]

    @classmethod
    def _deserialize(
        cls: Type["_Consolidation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Consolidation"]:
        if not json_data:
            return None
        return cls(
            MatchingAttributesList=json_data.get("MatchingAttributesList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Consolidation = Consolidation


@dataclass
class ExportingConfig(BaseModel):
    S3Exporting: Optional["_S3ExportingConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_ExportingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExportingConfig"]:
        if not json_data:
            return None
        return cls(
            S3Exporting=S3ExportingConfig._deserialize(json_data.get("S3Exporting")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExportingConfig = ExportingConfig


@dataclass
class S3ExportingConfig(BaseModel):
    S3BucketName: Optional[str]
    S3KeyName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3ExportingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3ExportingConfig"]:
        if not json_data:
            return None
        return cls(
            S3BucketName=json_data.get("S3BucketName"),
            S3KeyName=json_data.get("S3KeyName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3ExportingConfig = S3ExportingConfig


@dataclass
class JobSchedule(BaseModel):
    DayOfTheWeek: Optional[str]
    Time: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JobSchedule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JobSchedule"]:
        if not json_data:
            return None
        return cls(
            DayOfTheWeek=json_data.get("DayOfTheWeek"),
            Time=json_data.get("Time"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JobSchedule = JobSchedule


@dataclass
class RuleBasedMatching(BaseModel):
    Enabled: Optional[bool]
    AttributeTypesSelector: Optional["_AttributeTypesSelector"]
    ConflictResolution: Optional["_ConflictResolution"]
    ExportingConfig: Optional["_ExportingConfig"]
    MatchingRules: Optional[Sequence["_MatchingRule"]]
    MaxAllowedRuleLevelForMatching: Optional[int]
    MaxAllowedRuleLevelForMerging: Optional[int]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RuleBasedMatching"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleBasedMatching"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            AttributeTypesSelector=AttributeTypesSelector._deserialize(json_data.get("AttributeTypesSelector")),
            ConflictResolution=ConflictResolution._deserialize(json_data.get("ConflictResolution")),
            ExportingConfig=ExportingConfig._deserialize(json_data.get("ExportingConfig")),
            MatchingRules=deserialize_list(json_data.get("MatchingRules"), MatchingRule),
            MaxAllowedRuleLevelForMatching=json_data.get("MaxAllowedRuleLevelForMatching"),
            MaxAllowedRuleLevelForMerging=json_data.get("MaxAllowedRuleLevelForMerging"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleBasedMatching = RuleBasedMatching


@dataclass
class AttributeTypesSelector(BaseModel):
    AttributeMatchingModel: Optional[str]
    Address: Optional[Sequence[str]]
    EmailAddress: Optional[Sequence[str]]
    PhoneNumber: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AttributeTypesSelector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributeTypesSelector"]:
        if not json_data:
            return None
        return cls(
            AttributeMatchingModel=json_data.get("AttributeMatchingModel"),
            Address=json_data.get("Address"),
            EmailAddress=json_data.get("EmailAddress"),
            PhoneNumber=json_data.get("PhoneNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributeTypesSelector = AttributeTypesSelector


@dataclass
class MatchingRule(BaseModel):
    Rule: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchingRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchingRule"]:
        if not json_data:
            return None
        return cls(
            Rule=json_data.get("Rule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchingRule = MatchingRule


@dataclass
class DomainStats(BaseModel):
    MeteringProfileCount: Optional[float]
    ObjectCount: Optional[float]
    ProfileCount: Optional[float]
    TotalSize: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DomainStats"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainStats"]:
        if not json_data:
            return None
        return cls(
            MeteringProfileCount=json_data.get("MeteringProfileCount"),
            ObjectCount=json_data.get("ObjectCount"),
            ProfileCount=json_data.get("ProfileCount"),
            TotalSize=json_data.get("TotalSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainStats = DomainStats


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


