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
class AwsCodebuildReportgroup(BaseModel):
    Type: Optional[str]
    ExportConfig: Optional["_ReportExportConfig"]
    Id: Optional[str]
    Arn: Optional[str]
    DeleteReports: Optional[bool]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCodebuildReportgroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCodebuildReportgroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Type=json_data.get("Type"),
            ExportConfig=ReportExportConfig._deserialize(json_data.get("ExportConfig")),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            DeleteReports=json_data.get("DeleteReports"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCodebuildReportgroup = AwsCodebuildReportgroup


@dataclass
class ReportExportConfig(BaseModel):
    S3Destination: Optional["_S3ReportExportConfig"]
    ExportConfigType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReportExportConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReportExportConfig"]:
        if not json_data:
            return None
        return cls(
            S3Destination=S3ReportExportConfig._deserialize(json_data.get("S3Destination")),
            ExportConfigType=json_data.get("ExportConfigType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReportExportConfig = ReportExportConfig


@dataclass
class S3ReportExportConfig(BaseModel):
    Path: Optional[str]
    Bucket: Optional[str]
    Packaging: Optional[str]
    EncryptionKey: Optional[str]
    BucketOwner: Optional[str]
    EncryptionDisabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_S3ReportExportConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3ReportExportConfig"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Bucket=json_data.get("Bucket"),
            Packaging=json_data.get("Packaging"),
            EncryptionKey=json_data.get("EncryptionKey"),
            BucketOwner=json_data.get("BucketOwner"),
            EncryptionDisabled=json_data.get("EncryptionDisabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3ReportExportConfig = S3ReportExportConfig


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


