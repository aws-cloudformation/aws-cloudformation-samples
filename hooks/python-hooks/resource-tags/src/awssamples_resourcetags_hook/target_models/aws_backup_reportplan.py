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
class AwsBackupReportplan(BaseModel):
    ReportPlanName: Optional[str]
    ReportPlanArn: Optional[str]
    ReportPlanDescription: Optional[str]
    ReportPlanTags: Optional[Sequence["_Tag"]]
    ReportDeliveryChannel: Optional["_ReportDeliveryChannel"]
    ReportSetting: Optional["_ReportSetting"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsBackupReportplan"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsBackupReportplan"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ReportPlanName=json_data.get("ReportPlanName"),
            ReportPlanArn=json_data.get("ReportPlanArn"),
            ReportPlanDescription=json_data.get("ReportPlanDescription"),
            ReportPlanTags=deserialize_list(json_data.get("ReportPlanTags"), Tag),
            ReportDeliveryChannel=ReportDeliveryChannel._deserialize(json_data.get("ReportDeliveryChannel")),
            ReportSetting=ReportSetting._deserialize(json_data.get("ReportSetting")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsBackupReportplan = AwsBackupReportplan


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
class ReportDeliveryChannel(BaseModel):
    Formats: Optional[AbstractSet[str]]
    S3BucketName: Optional[str]
    S3KeyPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReportDeliveryChannel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReportDeliveryChannel"]:
        if not json_data:
            return None
        return cls(
            Formats=set_or_none(json_data.get("Formats")),
            S3BucketName=json_data.get("S3BucketName"),
            S3KeyPrefix=json_data.get("S3KeyPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReportDeliveryChannel = ReportDeliveryChannel


@dataclass
class ReportSetting(BaseModel):
    ReportTemplate: Optional[str]
    FrameworkArns: Optional[AbstractSet[str]]
    Accounts: Optional[AbstractSet[str]]
    OrganizationUnits: Optional[AbstractSet[str]]
    Regions: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ReportSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReportSetting"]:
        if not json_data:
            return None
        return cls(
            ReportTemplate=json_data.get("ReportTemplate"),
            FrameworkArns=set_or_none(json_data.get("FrameworkArns")),
            Accounts=set_or_none(json_data.get("Accounts")),
            OrganizationUnits=set_or_none(json_data.get("OrganizationUnits")),
            Regions=set_or_none(json_data.get("Regions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReportSetting = ReportSetting


