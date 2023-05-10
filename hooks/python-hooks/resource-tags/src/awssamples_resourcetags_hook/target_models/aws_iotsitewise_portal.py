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
class AwsIotsitewisePortal(BaseModel):
    PortalAuthMode: Optional[str]
    PortalArn: Optional[str]
    PortalClientId: Optional[str]
    PortalContactEmail: Optional[str]
    PortalDescription: Optional[str]
    PortalId: Optional[str]
    PortalName: Optional[str]
    PortalStartUrl: Optional[str]
    RoleArn: Optional[str]
    NotificationSenderEmail: Optional[str]
    Alarms: Optional["_Alarms"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotsitewisePortal"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotsitewisePortal"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            PortalAuthMode=json_data.get("PortalAuthMode"),
            PortalArn=json_data.get("PortalArn"),
            PortalClientId=json_data.get("PortalClientId"),
            PortalContactEmail=json_data.get("PortalContactEmail"),
            PortalDescription=json_data.get("PortalDescription"),
            PortalId=json_data.get("PortalId"),
            PortalName=json_data.get("PortalName"),
            PortalStartUrl=json_data.get("PortalStartUrl"),
            RoleArn=json_data.get("RoleArn"),
            NotificationSenderEmail=json_data.get("NotificationSenderEmail"),
            Alarms=Alarms._deserialize(json_data.get("Alarms")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotsitewisePortal = AwsIotsitewisePortal


@dataclass
class Alarms(BaseModel):
    AlarmRoleArn: Optional[str]
    NotificationLambdaArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Alarms"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Alarms"]:
        if not json_data:
            return None
        return cls(
            AlarmRoleArn=json_data.get("AlarmRoleArn"),
            NotificationLambdaArn=json_data.get("NotificationLambdaArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Alarms = Alarms


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


