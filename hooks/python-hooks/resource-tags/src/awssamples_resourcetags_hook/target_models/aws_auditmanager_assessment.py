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
class AwsAuditmanagerAssessment(BaseModel):
    FrameworkId: Optional[str]
    AssessmentId: Optional[str]
    AwsAccount: Optional["_AWSAccount"]
    Arn: Optional[str]
    Tags: Optional[Any]
    Delegations: Optional[Sequence["_Delegation"]]
    Roles: Optional[Sequence["_Role"]]
    Scope: Optional["_Scope"]
    AssessmentReportsDestination: Optional["_AssessmentReportsDestination"]
    Status: Optional[str]
    CreationTime: Optional[float]
    Name: Optional[str]
    Description: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAuditmanagerAssessment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAuditmanagerAssessment"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            FrameworkId=json_data.get("FrameworkId"),
            AssessmentId=json_data.get("AssessmentId"),
            AwsAccount=AWSAccount._deserialize(json_data.get("AwsAccount")),
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
            Delegations=deserialize_list(json_data.get("Delegations"), Delegation),
            Roles=deserialize_list(json_data.get("Roles"), Role),
            Scope=Scope._deserialize(json_data.get("Scope")),
            AssessmentReportsDestination=AssessmentReportsDestination._deserialize(json_data.get("AssessmentReportsDestination")),
            Status=json_data.get("Status"),
            CreationTime=json_data.get("CreationTime"),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAuditmanagerAssessment = AwsAuditmanagerAssessment


@dataclass
class AWSAccount(BaseModel):
    Id: Optional[str]
    EmailAddress: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AWSAccount"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AWSAccount"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            EmailAddress=json_data.get("EmailAddress"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AWSAccount = AWSAccount


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
class Delegation(BaseModel):
    LastUpdated: Optional[float]
    ControlSetId: Optional[str]
    CreationTime: Optional[float]
    CreatedBy: Optional[str]
    RoleArn: Optional[str]
    AssessmentName: Optional[str]
    Comment: Optional[str]
    Id: Optional[str]
    RoleType: Optional[str]
    AssessmentId: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Delegation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Delegation"]:
        if not json_data:
            return None
        return cls(
            LastUpdated=json_data.get("LastUpdated"),
            ControlSetId=json_data.get("ControlSetId"),
            CreationTime=json_data.get("CreationTime"),
            CreatedBy=json_data.get("CreatedBy"),
            RoleArn=json_data.get("RoleArn"),
            AssessmentName=json_data.get("AssessmentName"),
            Comment=json_data.get("Comment"),
            Id=json_data.get("Id"),
            RoleType=json_data.get("RoleType"),
            AssessmentId=json_data.get("AssessmentId"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Delegation = Delegation


@dataclass
class Role(BaseModel):
    RoleArn: Optional[str]
    RoleType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Role"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Role"]:
        if not json_data:
            return None
        return cls(
            RoleArn=json_data.get("RoleArn"),
            RoleType=json_data.get("RoleType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Role = Role


@dataclass
class Scope(BaseModel):
    AwsAccounts: Optional[Sequence["_AWSAccount"]]
    AwsServices: Optional[Sequence["_AWSService"]]

    @classmethod
    def _deserialize(
        cls: Type["_Scope"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Scope"]:
        if not json_data:
            return None
        return cls(
            AwsAccounts=deserialize_list(json_data.get("AwsAccounts"), AWSAccount),
            AwsServices=deserialize_list(json_data.get("AwsServices"), AWSService),
        )


# work around possible type aliasing issues when variable has same name as a model
_Scope = Scope


@dataclass
class AWSService(BaseModel):
    ServiceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AWSService"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AWSService"]:
        if not json_data:
            return None
        return cls(
            ServiceName=json_data.get("ServiceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AWSService = AWSService


@dataclass
class AssessmentReportsDestination(BaseModel):
    Destination: Optional[str]
    DestinationType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssessmentReportsDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssessmentReportsDestination"]:
        if not json_data:
            return None
        return cls(
            Destination=json_data.get("Destination"),
            DestinationType=json_data.get("DestinationType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssessmentReportsDestination = AssessmentReportsDestination


