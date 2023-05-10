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
class AwsIotJobtemplate(BaseModel):
    Arn: Optional[str]
    JobArn: Optional[str]
    JobTemplateId: Optional[str]
    Description: Optional[str]
    Document: Optional[str]
    DocumentSource: Optional[str]
    TimeoutConfig: Optional["_TimeoutConfig"]
    JobExecutionsRolloutConfig: Optional["_JobExecutionsRolloutConfig"]
    AbortConfig: Optional["_AbortConfig"]
    PresignedUrlConfig: Optional["_PresignedUrlConfig"]
    JobExecutionsRetryConfig: Optional["_JobExecutionsRetryConfig"]
    MaintenanceWindows: Optional[Sequence["_MaintenanceWindow"]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotJobtemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotJobtemplate"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            JobArn=json_data.get("JobArn"),
            JobTemplateId=json_data.get("JobTemplateId"),
            Description=json_data.get("Description"),
            Document=json_data.get("Document"),
            DocumentSource=json_data.get("DocumentSource"),
            TimeoutConfig=TimeoutConfig._deserialize(json_data.get("TimeoutConfig")),
            JobExecutionsRolloutConfig=JobExecutionsRolloutConfig._deserialize(json_data.get("JobExecutionsRolloutConfig")),
            AbortConfig=AbortConfig._deserialize(json_data.get("AbortConfig")),
            PresignedUrlConfig=PresignedUrlConfig._deserialize(json_data.get("PresignedUrlConfig")),
            JobExecutionsRetryConfig=JobExecutionsRetryConfig._deserialize(json_data.get("JobExecutionsRetryConfig")),
            MaintenanceWindows=deserialize_list(json_data.get("MaintenanceWindows"), MaintenanceWindow),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotJobtemplate = AwsIotJobtemplate


@dataclass
class TimeoutConfig(BaseModel):
    InProgressTimeoutInMinutes: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutConfig"]:
        if not json_data:
            return None
        return cls(
            InProgressTimeoutInMinutes=json_data.get("InProgressTimeoutInMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutConfig = TimeoutConfig


@dataclass
class JobExecutionsRolloutConfig(BaseModel):
    ExponentialRolloutRate: Optional["_ExponentialRolloutRate"]
    MaximumPerMinute: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_JobExecutionsRolloutConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JobExecutionsRolloutConfig"]:
        if not json_data:
            return None
        return cls(
            ExponentialRolloutRate=ExponentialRolloutRate._deserialize(json_data.get("ExponentialRolloutRate")),
            MaximumPerMinute=json_data.get("MaximumPerMinute"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JobExecutionsRolloutConfig = JobExecutionsRolloutConfig


@dataclass
class ExponentialRolloutRate(BaseModel):
    BaseRatePerMinute: Optional[int]
    IncrementFactor: Optional[float]
    RateIncreaseCriteria: Optional["_RateIncreaseCriteria"]

    @classmethod
    def _deserialize(
        cls: Type["_ExponentialRolloutRate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExponentialRolloutRate"]:
        if not json_data:
            return None
        return cls(
            BaseRatePerMinute=json_data.get("BaseRatePerMinute"),
            IncrementFactor=json_data.get("IncrementFactor"),
            RateIncreaseCriteria=RateIncreaseCriteria._deserialize(json_data.get("RateIncreaseCriteria")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExponentialRolloutRate = ExponentialRolloutRate


@dataclass
class RateIncreaseCriteria(BaseModel):
    NumberOfNotifiedThings: Optional[int]
    NumberOfSucceededThings: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_RateIncreaseCriteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateIncreaseCriteria"]:
        if not json_data:
            return None
        return cls(
            NumberOfNotifiedThings=json_data.get("NumberOfNotifiedThings"),
            NumberOfSucceededThings=json_data.get("NumberOfSucceededThings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RateIncreaseCriteria = RateIncreaseCriteria


@dataclass
class AbortConfig(BaseModel):
    CriteriaList: Optional[Sequence["_AbortCriteria"]]

    @classmethod
    def _deserialize(
        cls: Type["_AbortConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AbortConfig"]:
        if not json_data:
            return None
        return cls(
            CriteriaList=deserialize_list(json_data.get("CriteriaList"), AbortCriteria),
        )


# work around possible type aliasing issues when variable has same name as a model
_AbortConfig = AbortConfig


@dataclass
class AbortCriteria(BaseModel):
    Action: Optional[str]
    FailureType: Optional[str]
    MinNumberOfExecutedThings: Optional[int]
    ThresholdPercentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AbortCriteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AbortCriteria"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            FailureType=json_data.get("FailureType"),
            MinNumberOfExecutedThings=json_data.get("MinNumberOfExecutedThings"),
            ThresholdPercentage=json_data.get("ThresholdPercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AbortCriteria = AbortCriteria


@dataclass
class PresignedUrlConfig(BaseModel):
    RoleArn: Optional[str]
    ExpiresInSec: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_PresignedUrlConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PresignedUrlConfig"]:
        if not json_data:
            return None
        return cls(
            RoleArn=json_data.get("RoleArn"),
            ExpiresInSec=json_data.get("ExpiresInSec"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PresignedUrlConfig = PresignedUrlConfig


@dataclass
class JobExecutionsRetryConfig(BaseModel):
    RetryCriteriaList: Optional[Sequence["_RetryCriteria"]]

    @classmethod
    def _deserialize(
        cls: Type["_JobExecutionsRetryConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JobExecutionsRetryConfig"]:
        if not json_data:
            return None
        return cls(
            RetryCriteriaList=deserialize_list(json_data.get("RetryCriteriaList"), RetryCriteria),
        )


# work around possible type aliasing issues when variable has same name as a model
_JobExecutionsRetryConfig = JobExecutionsRetryConfig


@dataclass
class RetryCriteria(BaseModel):
    NumberOfRetries: Optional[int]
    FailureType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RetryCriteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetryCriteria"]:
        if not json_data:
            return None
        return cls(
            NumberOfRetries=json_data.get("NumberOfRetries"),
            FailureType=json_data.get("FailureType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetryCriteria = RetryCriteria


@dataclass
class MaintenanceWindow(BaseModel):
    StartTime: Optional[str]
    DurationInMinutes: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindow"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindow"]:
        if not json_data:
            return None
        return cls(
            StartTime=json_data.get("StartTime"),
            DurationInMinutes=json_data.get("DurationInMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceWindow = MaintenanceWindow


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


