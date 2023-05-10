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
class AwsSagemakerEndpoint(BaseModel):
    RetainAllVariantProperties: Optional[bool]
    EndpointName: Optional[str]
    ExcludeRetainedVariantProperties: Optional[Sequence["_VariantProperty"]]
    EndpointConfigName: Optional[str]
    Id: Optional[str]
    DeploymentConfig: Optional["_DeploymentConfig"]
    RetainDeploymentConfig: Optional[bool]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSagemakerEndpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSagemakerEndpoint"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            RetainAllVariantProperties=json_data.get("RetainAllVariantProperties"),
            EndpointName=json_data.get("EndpointName"),
            ExcludeRetainedVariantProperties=deserialize_list(json_data.get("ExcludeRetainedVariantProperties"), VariantProperty),
            EndpointConfigName=json_data.get("EndpointConfigName"),
            Id=json_data.get("Id"),
            DeploymentConfig=DeploymentConfig._deserialize(json_data.get("DeploymentConfig")),
            RetainDeploymentConfig=json_data.get("RetainDeploymentConfig"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSagemakerEndpoint = AwsSagemakerEndpoint


@dataclass
class VariantProperty(BaseModel):
    VariantPropertyType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VariantProperty"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VariantProperty"]:
        if not json_data:
            return None
        return cls(
            VariantPropertyType=json_data.get("VariantPropertyType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VariantProperty = VariantProperty


@dataclass
class DeploymentConfig(BaseModel):
    AutoRollbackConfiguration: Optional["_AutoRollbackConfig"]
    BlueGreenUpdatePolicy: Optional["_BlueGreenUpdatePolicy"]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentConfig"]:
        if not json_data:
            return None
        return cls(
            AutoRollbackConfiguration=AutoRollbackConfig._deserialize(json_data.get("AutoRollbackConfiguration")),
            BlueGreenUpdatePolicy=BlueGreenUpdatePolicy._deserialize(json_data.get("BlueGreenUpdatePolicy")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentConfig = DeploymentConfig


@dataclass
class AutoRollbackConfig(BaseModel):
    Alarms: Optional[Sequence["_Alarm"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutoRollbackConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoRollbackConfig"]:
        if not json_data:
            return None
        return cls(
            Alarms=deserialize_list(json_data.get("Alarms"), Alarm),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoRollbackConfig = AutoRollbackConfig


@dataclass
class Alarm(BaseModel):
    AlarmName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Alarm"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Alarm"]:
        if not json_data:
            return None
        return cls(
            AlarmName=json_data.get("AlarmName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Alarm = Alarm


@dataclass
class BlueGreenUpdatePolicy(BaseModel):
    MaximumExecutionTimeoutInSeconds: Optional[int]
    TerminationWaitInSeconds: Optional[int]
    TrafficRoutingConfiguration: Optional["_TrafficRoutingConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_BlueGreenUpdatePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlueGreenUpdatePolicy"]:
        if not json_data:
            return None
        return cls(
            MaximumExecutionTimeoutInSeconds=json_data.get("MaximumExecutionTimeoutInSeconds"),
            TerminationWaitInSeconds=json_data.get("TerminationWaitInSeconds"),
            TrafficRoutingConfiguration=TrafficRoutingConfig._deserialize(json_data.get("TrafficRoutingConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlueGreenUpdatePolicy = BlueGreenUpdatePolicy


@dataclass
class TrafficRoutingConfig(BaseModel):
    Type: Optional[str]
    LinearStepSize: Optional["_CapacitySize"]
    CanarySize: Optional["_CapacitySize"]
    WaitIntervalInSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_TrafficRoutingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrafficRoutingConfig"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            LinearStepSize=CapacitySize._deserialize(json_data.get("LinearStepSize")),
            CanarySize=CapacitySize._deserialize(json_data.get("CanarySize")),
            WaitIntervalInSeconds=json_data.get("WaitIntervalInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrafficRoutingConfig = TrafficRoutingConfig


@dataclass
class CapacitySize(BaseModel):
    Value: Optional[int]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CapacitySize"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacitySize"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacitySize = CapacitySize


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


