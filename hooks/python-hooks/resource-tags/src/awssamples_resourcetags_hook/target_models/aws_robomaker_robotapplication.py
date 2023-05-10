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
class AwsRobomakerRobotapplication(BaseModel):
    Name: Optional[str]
    Sources: Optional[Sequence["_SourceConfig"]]
    Environment: Optional[str]
    RobotSoftwareSuite: Optional["_RobotSoftwareSuite"]
    CurrentRevisionId: Optional[str]
    Arn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRobomakerRobotapplication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRobomakerRobotapplication"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Sources=deserialize_list(json_data.get("Sources"), SourceConfig),
            Environment=json_data.get("Environment"),
            RobotSoftwareSuite=RobotSoftwareSuite._deserialize(json_data.get("RobotSoftwareSuite")),
            CurrentRevisionId=json_data.get("CurrentRevisionId"),
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRobomakerRobotapplication = AwsRobomakerRobotapplication


@dataclass
class SourceConfig(BaseModel):
    S3Bucket: Optional[str]
    S3Key: Optional[str]
    Architecture: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceConfig"]:
        if not json_data:
            return None
        return cls(
            S3Bucket=json_data.get("S3Bucket"),
            S3Key=json_data.get("S3Key"),
            Architecture=json_data.get("Architecture"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceConfig = SourceConfig


@dataclass
class RobotSoftwareSuite(BaseModel):
    Name: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RobotSoftwareSuite"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RobotSoftwareSuite"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RobotSoftwareSuite = RobotSoftwareSuite


