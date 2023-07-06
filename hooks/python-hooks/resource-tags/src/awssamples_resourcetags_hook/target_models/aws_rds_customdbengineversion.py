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
class AwsRdsCustomdbengineversion(BaseModel):
    DatabaseInstallationFilesS3BucketName: Optional[str]
    DatabaseInstallationFilesS3Prefix: Optional[str]
    Description: Optional[str]
    Engine: Optional[str]
    EngineVersion: Optional[str]
    KMSKeyId: Optional[str]
    Manifest: Optional[str]
    DBEngineVersionArn: Optional[str]
    Status: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRdsCustomdbengineversion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRdsCustomdbengineversion"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DatabaseInstallationFilesS3BucketName=json_data.get("DatabaseInstallationFilesS3BucketName"),
            DatabaseInstallationFilesS3Prefix=json_data.get("DatabaseInstallationFilesS3Prefix"),
            Description=json_data.get("Description"),
            Engine=json_data.get("Engine"),
            EngineVersion=json_data.get("EngineVersion"),
            KMSKeyId=json_data.get("KMSKeyId"),
            Manifest=json_data.get("Manifest"),
            DBEngineVersionArn=json_data.get("DBEngineVersionArn"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRdsCustomdbengineversion = AwsRdsCustomdbengineversion


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


