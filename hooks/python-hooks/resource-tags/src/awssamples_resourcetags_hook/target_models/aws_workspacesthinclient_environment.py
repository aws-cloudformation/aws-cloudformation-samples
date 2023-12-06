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
class AwsWorkspacesthinclientEnvironment(BaseModel):
    Id: Optional[str]
    Name: Optional[str]
    DesktopArn: Optional[str]
    DesktopEndpoint: Optional[str]
    DesktopType: Optional[str]
    ActivationCode: Optional[str]
    RegisteredDevicesCount: Optional[int]
    SoftwareSetUpdateSchedule: Optional[str]
    MaintenanceWindow: Optional["_MaintenanceWindow"]
    SoftwareSetUpdateMode: Optional[str]
    DesiredSoftwareSetId: Optional[str]
    PendingSoftwareSetId: Optional[str]
    PendingSoftwareSetVersion: Optional[str]
    SoftwareSetComplianceStatus: Optional[str]
    CreatedAt: Optional[str]
    UpdatedAt: Optional[str]
    Arn: Optional[str]
    KmsKeyArn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsWorkspacesthinclientEnvironment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsWorkspacesthinclientEnvironment"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            DesktopArn=json_data.get("DesktopArn"),
            DesktopEndpoint=json_data.get("DesktopEndpoint"),
            DesktopType=json_data.get("DesktopType"),
            ActivationCode=json_data.get("ActivationCode"),
            RegisteredDevicesCount=json_data.get("RegisteredDevicesCount"),
            SoftwareSetUpdateSchedule=json_data.get("SoftwareSetUpdateSchedule"),
            MaintenanceWindow=MaintenanceWindow._deserialize(json_data.get("MaintenanceWindow")),
            SoftwareSetUpdateMode=json_data.get("SoftwareSetUpdateMode"),
            DesiredSoftwareSetId=json_data.get("DesiredSoftwareSetId"),
            PendingSoftwareSetId=json_data.get("PendingSoftwareSetId"),
            PendingSoftwareSetVersion=json_data.get("PendingSoftwareSetVersion"),
            SoftwareSetComplianceStatus=json_data.get("SoftwareSetComplianceStatus"),
            CreatedAt=json_data.get("CreatedAt"),
            UpdatedAt=json_data.get("UpdatedAt"),
            Arn=json_data.get("Arn"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsWorkspacesthinclientEnvironment = AwsWorkspacesthinclientEnvironment


@dataclass
class MaintenanceWindow(BaseModel):
    Type: Optional[str]
    StartTimeHour: Optional[int]
    StartTimeMinute: Optional[int]
    EndTimeHour: Optional[int]
    EndTimeMinute: Optional[int]
    DaysOfTheWeek: Optional[AbstractSet[str]]
    ApplyTimeOf: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindow"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindow"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            StartTimeHour=json_data.get("StartTimeHour"),
            StartTimeMinute=json_data.get("StartTimeMinute"),
            EndTimeHour=json_data.get("EndTimeHour"),
            EndTimeMinute=json_data.get("EndTimeMinute"),
            DaysOfTheWeek=set_or_none(json_data.get("DaysOfTheWeek")),
            ApplyTimeOf=json_data.get("ApplyTimeOf"),
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


