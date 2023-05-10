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
class AwsGreengrassv2Deployment(BaseModel):
    TargetArn: Optional[str]
    ParentTargetArn: Optional[str]
    DeploymentId: Optional[str]
    DeploymentName: Optional[str]
    Components: Optional[MutableMapping[str, "_ComponentDeploymentSpecification"]]
    IotJobConfiguration: Optional["_DeploymentIoTJobConfiguration"]
    DeploymentPolicies: Optional["_DeploymentPolicies"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGreengrassv2Deployment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGreengrassv2Deployment"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            TargetArn=json_data.get("TargetArn"),
            ParentTargetArn=json_data.get("ParentTargetArn"),
            DeploymentId=json_data.get("DeploymentId"),
            DeploymentName=json_data.get("DeploymentName"),
            Components=json_data.get("Components"),
            IotJobConfiguration=DeploymentIoTJobConfiguration._deserialize(json_data.get("IotJobConfiguration")),
            DeploymentPolicies=DeploymentPolicies._deserialize(json_data.get("DeploymentPolicies")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGreengrassv2Deployment = AwsGreengrassv2Deployment


@dataclass
class ComponentDeploymentSpecification(BaseModel):
    ComponentVersion: Optional[str]
    ConfigurationUpdate: Optional["_ComponentConfigurationUpdate"]
    RunWith: Optional["_ComponentRunWith"]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentDeploymentSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentDeploymentSpecification"]:
        if not json_data:
            return None
        return cls(
            ComponentVersion=json_data.get("ComponentVersion"),
            ConfigurationUpdate=ComponentConfigurationUpdate._deserialize(json_data.get("ConfigurationUpdate")),
            RunWith=ComponentRunWith._deserialize(json_data.get("RunWith")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentDeploymentSpecification = ComponentDeploymentSpecification


@dataclass
class ComponentConfigurationUpdate(BaseModel):
    Merge: Optional[str]
    Reset: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentConfigurationUpdate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentConfigurationUpdate"]:
        if not json_data:
            return None
        return cls(
            Merge=json_data.get("Merge"),
            Reset=json_data.get("Reset"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentConfigurationUpdate = ComponentConfigurationUpdate


@dataclass
class ComponentRunWith(BaseModel):
    PosixUser: Optional[str]
    SystemResourceLimits: Optional["_SystemResourceLimits"]
    WindowsUser: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentRunWith"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentRunWith"]:
        if not json_data:
            return None
        return cls(
            PosixUser=json_data.get("PosixUser"),
            SystemResourceLimits=SystemResourceLimits._deserialize(json_data.get("SystemResourceLimits")),
            WindowsUser=json_data.get("WindowsUser"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentRunWith = ComponentRunWith


@dataclass
class SystemResourceLimits(BaseModel):
    Memory: Optional[int]
    Cpus: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SystemResourceLimits"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemResourceLimits"]:
        if not json_data:
            return None
        return cls(
            Memory=json_data.get("Memory"),
            Cpus=json_data.get("Cpus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemResourceLimits = SystemResourceLimits


@dataclass
class DeploymentIoTJobConfiguration(BaseModel):
    JobExecutionsRolloutConfig: Optional["_IoTJobExecutionsRolloutConfig"]
    AbortConfig: Optional["_IoTJobAbortConfig"]
    TimeoutConfig: Optional["_IoTJobTimeoutConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentIoTJobConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentIoTJobConfiguration"]:
        if not json_data:
            return None
        return cls(
            JobExecutionsRolloutConfig=IoTJobExecutionsRolloutConfig._deserialize(json_data.get("JobExecutionsRolloutConfig")),
            AbortConfig=IoTJobAbortConfig._deserialize(json_data.get("AbortConfig")),
            TimeoutConfig=IoTJobTimeoutConfig._deserialize(json_data.get("TimeoutConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentIoTJobConfiguration = DeploymentIoTJobConfiguration


@dataclass
class IoTJobExecutionsRolloutConfig(BaseModel):
    ExponentialRate: Optional["_IoTJobExponentialRolloutRate"]
    MaximumPerMinute: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_IoTJobExecutionsRolloutConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IoTJobExecutionsRolloutConfig"]:
        if not json_data:
            return None
        return cls(
            ExponentialRate=IoTJobExponentialRolloutRate._deserialize(json_data.get("ExponentialRate")),
            MaximumPerMinute=json_data.get("MaximumPerMinute"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IoTJobExecutionsRolloutConfig = IoTJobExecutionsRolloutConfig


@dataclass
class IoTJobExponentialRolloutRate(BaseModel):
    BaseRatePerMinute: Optional[int]
    IncrementFactor: Optional[float]
    RateIncreaseCriteria: Optional["_IoTJobRateIncreaseCriteria"]

    @classmethod
    def _deserialize(
        cls: Type["_IoTJobExponentialRolloutRate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IoTJobExponentialRolloutRate"]:
        if not json_data:
            return None
        return cls(
            BaseRatePerMinute=json_data.get("BaseRatePerMinute"),
            IncrementFactor=json_data.get("IncrementFactor"),
            RateIncreaseCriteria=IoTJobRateIncreaseCriteria._deserialize(json_data.get("RateIncreaseCriteria")),
        )


# work around possible type aliasing issues when variable has same name as a model
_IoTJobExponentialRolloutRate = IoTJobExponentialRolloutRate


@dataclass
class IoTJobRateIncreaseCriteria(BaseModel):
    NumberOfNotifiedThings: Optional[int]
    NumberOfSucceededThings: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_IoTJobRateIncreaseCriteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IoTJobRateIncreaseCriteria"]:
        if not json_data:
            return None
        return cls(
            NumberOfNotifiedThings=json_data.get("NumberOfNotifiedThings"),
            NumberOfSucceededThings=json_data.get("NumberOfSucceededThings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IoTJobRateIncreaseCriteria = IoTJobRateIncreaseCriteria


@dataclass
class IoTJobAbortConfig(BaseModel):
    CriteriaList: Optional[Sequence["_IoTJobAbortCriteria"]]

    @classmethod
    def _deserialize(
        cls: Type["_IoTJobAbortConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IoTJobAbortConfig"]:
        if not json_data:
            return None
        return cls(
            CriteriaList=deserialize_list(json_data.get("CriteriaList"), IoTJobAbortCriteria),
        )


# work around possible type aliasing issues when variable has same name as a model
_IoTJobAbortConfig = IoTJobAbortConfig


@dataclass
class IoTJobAbortCriteria(BaseModel):
    FailureType: Optional[str]
    Action: Optional[str]
    ThresholdPercentage: Optional[float]
    MinNumberOfExecutedThings: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_IoTJobAbortCriteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IoTJobAbortCriteria"]:
        if not json_data:
            return None
        return cls(
            FailureType=json_data.get("FailureType"),
            Action=json_data.get("Action"),
            ThresholdPercentage=json_data.get("ThresholdPercentage"),
            MinNumberOfExecutedThings=json_data.get("MinNumberOfExecutedThings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IoTJobAbortCriteria = IoTJobAbortCriteria


@dataclass
class IoTJobTimeoutConfig(BaseModel):
    InProgressTimeoutInMinutes: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_IoTJobTimeoutConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IoTJobTimeoutConfig"]:
        if not json_data:
            return None
        return cls(
            InProgressTimeoutInMinutes=json_data.get("InProgressTimeoutInMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IoTJobTimeoutConfig = IoTJobTimeoutConfig


@dataclass
class DeploymentPolicies(BaseModel):
    FailureHandlingPolicy: Optional[str]
    ComponentUpdatePolicy: Optional["_DeploymentComponentUpdatePolicy"]
    ConfigurationValidationPolicy: Optional["_DeploymentConfigurationValidationPolicy"]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentPolicies"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentPolicies"]:
        if not json_data:
            return None
        return cls(
            FailureHandlingPolicy=json_data.get("FailureHandlingPolicy"),
            ComponentUpdatePolicy=DeploymentComponentUpdatePolicy._deserialize(json_data.get("ComponentUpdatePolicy")),
            ConfigurationValidationPolicy=DeploymentConfigurationValidationPolicy._deserialize(json_data.get("ConfigurationValidationPolicy")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentPolicies = DeploymentPolicies


@dataclass
class DeploymentComponentUpdatePolicy(BaseModel):
    TimeoutInSeconds: Optional[int]
    Action: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentComponentUpdatePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentComponentUpdatePolicy"]:
        if not json_data:
            return None
        return cls(
            TimeoutInSeconds=json_data.get("TimeoutInSeconds"),
            Action=json_data.get("Action"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentComponentUpdatePolicy = DeploymentComponentUpdatePolicy


@dataclass
class DeploymentConfigurationValidationPolicy(BaseModel):
    TimeoutInSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentConfigurationValidationPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentConfigurationValidationPolicy"]:
        if not json_data:
            return None
        return cls(
            TimeoutInSeconds=json_data.get("TimeoutInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentConfigurationValidationPolicy = DeploymentConfigurationValidationPolicy


