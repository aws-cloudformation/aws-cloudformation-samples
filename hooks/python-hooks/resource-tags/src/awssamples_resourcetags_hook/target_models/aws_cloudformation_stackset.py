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
class AwsCloudformationStackset(BaseModel):
    StackSetName: Optional[str]
    StackSetId: Optional[str]
    AdministrationRoleARN: Optional[str]
    AutoDeployment: Optional["_AutoDeployment"]
    Capabilities: Optional[AbstractSet[str]]
    Description: Optional[str]
    ExecutionRoleName: Optional[str]
    OperationPreferences: Optional["_OperationPreferences"]
    StackInstancesGroup: Optional[AbstractSet["_StackInstances"]]
    Parameters: Optional[AbstractSet["_Parameter"]]
    PermissionModel: Optional[str]
    Tags: Optional[Any]
    TemplateBody: Optional[str]
    TemplateURL: Optional[str]
    CallAs: Optional[str]
    ManagedExecution: Optional["_ManagedExecution"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudformationStackset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudformationStackset"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            StackSetName=json_data.get("StackSetName"),
            StackSetId=json_data.get("StackSetId"),
            AdministrationRoleARN=json_data.get("AdministrationRoleARN"),
            AutoDeployment=AutoDeployment._deserialize(json_data.get("AutoDeployment")),
            Capabilities=set_or_none(json_data.get("Capabilities")),
            Description=json_data.get("Description"),
            ExecutionRoleName=json_data.get("ExecutionRoleName"),
            OperationPreferences=OperationPreferences._deserialize(json_data.get("OperationPreferences")),
            StackInstancesGroup=set_or_none(json_data.get("StackInstancesGroup")),
            Parameters=set_or_none(json_data.get("Parameters")),
            PermissionModel=json_data.get("PermissionModel"),
            Tags=json_data.get("Tags"),
            TemplateBody=json_data.get("TemplateBody"),
            TemplateURL=json_data.get("TemplateURL"),
            CallAs=json_data.get("CallAs"),
            ManagedExecution=ManagedExecution._deserialize(json_data.get("ManagedExecution")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudformationStackset = AwsCloudformationStackset


@dataclass
class AutoDeployment(BaseModel):
    Enabled: Optional[bool]
    RetainStacksOnAccountRemoval: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AutoDeployment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoDeployment"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            RetainStacksOnAccountRemoval=json_data.get("RetainStacksOnAccountRemoval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoDeployment = AutoDeployment


@dataclass
class OperationPreferences(BaseModel):
    FailureToleranceCount: Optional[int]
    FailureTolerancePercentage: Optional[int]
    MaxConcurrentCount: Optional[int]
    MaxConcurrentPercentage: Optional[int]
    RegionOrder: Optional[Sequence[str]]
    RegionConcurrencyType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OperationPreferences"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OperationPreferences"]:
        if not json_data:
            return None
        return cls(
            FailureToleranceCount=json_data.get("FailureToleranceCount"),
            FailureTolerancePercentage=json_data.get("FailureTolerancePercentage"),
            MaxConcurrentCount=json_data.get("MaxConcurrentCount"),
            MaxConcurrentPercentage=json_data.get("MaxConcurrentPercentage"),
            RegionOrder=json_data.get("RegionOrder"),
            RegionConcurrencyType=json_data.get("RegionConcurrencyType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OperationPreferences = OperationPreferences


@dataclass
class StackInstances(BaseModel):
    DeploymentTargets: Optional["_DeploymentTargets"]
    Regions: Optional[AbstractSet[str]]
    ParameterOverrides: Optional[AbstractSet["_Parameter"]]

    @classmethod
    def _deserialize(
        cls: Type["_StackInstances"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StackInstances"]:
        if not json_data:
            return None
        return cls(
            DeploymentTargets=DeploymentTargets._deserialize(json_data.get("DeploymentTargets")),
            Regions=set_or_none(json_data.get("Regions")),
            ParameterOverrides=set_or_none(json_data.get("ParameterOverrides")),
        )


# work around possible type aliasing issues when variable has same name as a model
_StackInstances = StackInstances


@dataclass
class DeploymentTargets(BaseModel):
    Accounts: Optional[AbstractSet[str]]
    OrganizationalUnitIds: Optional[AbstractSet[str]]
    AccountFilterType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentTargets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentTargets"]:
        if not json_data:
            return None
        return cls(
            Accounts=set_or_none(json_data.get("Accounts")),
            OrganizationalUnitIds=set_or_none(json_data.get("OrganizationalUnitIds")),
            AccountFilterType=json_data.get("AccountFilterType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentTargets = DeploymentTargets


@dataclass
class Parameter(BaseModel):
    ParameterKey: Optional[str]
    ParameterValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Parameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Parameter"]:
        if not json_data:
            return None
        return cls(
            ParameterKey=json_data.get("ParameterKey"),
            ParameterValue=json_data.get("ParameterValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Parameter = Parameter


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
class ManagedExecution(BaseModel):
    Active: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedExecution"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedExecution"]:
        if not json_data:
            return None
        return cls(
            Active=json_data.get("Active"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagedExecution = ManagedExecution


