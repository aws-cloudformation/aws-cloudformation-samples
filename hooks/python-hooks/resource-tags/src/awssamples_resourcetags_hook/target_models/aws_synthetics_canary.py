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
class AwsSyntheticsCanary(BaseModel):
    Name: Optional[str]
    Id: Optional[str]
    State: Optional[str]
    Code: Optional["_Code"]
    ArtifactS3Location: Optional[str]
    ArtifactConfig: Optional["_ArtifactConfig"]
    Schedule: Optional["_Schedule"]
    ExecutionRoleArn: Optional[str]
    RuntimeVersion: Optional[str]
    SuccessRetentionPeriod: Optional[int]
    FailureRetentionPeriod: Optional[int]
    Tags: Optional[Any]
    VPCConfig: Optional["_VPCConfig"]
    RunConfig: Optional["_RunConfig"]
    StartCanaryAfterCreation: Optional[bool]
    VisualReference: Optional["_VisualReference"]
    DeleteLambdaResourcesOnCanaryDeletion: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSyntheticsCanary"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSyntheticsCanary"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Id=json_data.get("Id"),
            State=json_data.get("State"),
            Code=Code._deserialize(json_data.get("Code")),
            ArtifactS3Location=json_data.get("ArtifactS3Location"),
            ArtifactConfig=ArtifactConfig._deserialize(json_data.get("ArtifactConfig")),
            Schedule=Schedule._deserialize(json_data.get("Schedule")),
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            RuntimeVersion=json_data.get("RuntimeVersion"),
            SuccessRetentionPeriod=json_data.get("SuccessRetentionPeriod"),
            FailureRetentionPeriod=json_data.get("FailureRetentionPeriod"),
            Tags=json_data.get("Tags"),
            VPCConfig=VPCConfig._deserialize(json_data.get("VPCConfig")),
            RunConfig=RunConfig._deserialize(json_data.get("RunConfig")),
            StartCanaryAfterCreation=json_data.get("StartCanaryAfterCreation"),
            VisualReference=VisualReference._deserialize(json_data.get("VisualReference")),
            DeleteLambdaResourcesOnCanaryDeletion=json_data.get("DeleteLambdaResourcesOnCanaryDeletion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSyntheticsCanary = AwsSyntheticsCanary


@dataclass
class Code(BaseModel):
    S3Bucket: Optional[str]
    S3Key: Optional[str]
    S3ObjectVersion: Optional[str]
    Script: Optional[str]
    Handler: Optional[str]
    SourceLocationArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Code"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Code"]:
        if not json_data:
            return None
        return cls(
            S3Bucket=json_data.get("S3Bucket"),
            S3Key=json_data.get("S3Key"),
            S3ObjectVersion=json_data.get("S3ObjectVersion"),
            Script=json_data.get("Script"),
            Handler=json_data.get("Handler"),
            SourceLocationArn=json_data.get("SourceLocationArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Code = Code


@dataclass
class ArtifactConfig(BaseModel):
    S3Encryption: Optional["_S3Encryption"]

    @classmethod
    def _deserialize(
        cls: Type["_ArtifactConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArtifactConfig"]:
        if not json_data:
            return None
        return cls(
            S3Encryption=S3Encryption._deserialize(json_data.get("S3Encryption")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArtifactConfig = ArtifactConfig


@dataclass
class S3Encryption(BaseModel):
    EncryptionMode: Optional[str]
    KmsKeyArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Encryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Encryption"]:
        if not json_data:
            return None
        return cls(
            EncryptionMode=json_data.get("EncryptionMode"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Encryption = S3Encryption


@dataclass
class Schedule(BaseModel):
    Expression: Optional[str]
    DurationInSeconds: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Schedule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Schedule"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            DurationInSeconds=json_data.get("DurationInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Schedule = Schedule


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
class VPCConfig(BaseModel):
    VpcId: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    SecurityGroupIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VPCConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VPCConfig"]:
        if not json_data:
            return None
        return cls(
            VpcId=json_data.get("VpcId"),
            SubnetIds=json_data.get("SubnetIds"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VPCConfig = VPCConfig


@dataclass
class RunConfig(BaseModel):
    TimeoutInSeconds: Optional[int]
    MemoryInMB: Optional[int]
    ActiveTracing: Optional[bool]
    EnvironmentVariables: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_RunConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RunConfig"]:
        if not json_data:
            return None
        return cls(
            TimeoutInSeconds=json_data.get("TimeoutInSeconds"),
            MemoryInMB=json_data.get("MemoryInMB"),
            ActiveTracing=json_data.get("ActiveTracing"),
            EnvironmentVariables=json_data.get("EnvironmentVariables"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RunConfig = RunConfig


@dataclass
class VisualReference(BaseModel):
    BaseCanaryRunId: Optional[str]
    BaseScreenshots: Optional[Sequence["_BaseScreenshot"]]

    @classmethod
    def _deserialize(
        cls: Type["_VisualReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VisualReference"]:
        if not json_data:
            return None
        return cls(
            BaseCanaryRunId=json_data.get("BaseCanaryRunId"),
            BaseScreenshots=deserialize_list(json_data.get("BaseScreenshots"), BaseScreenshot),
        )


# work around possible type aliasing issues when variable has same name as a model
_VisualReference = VisualReference


@dataclass
class BaseScreenshot(BaseModel):
    ScreenshotName: Optional[str]
    IgnoreCoordinates: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_BaseScreenshot"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BaseScreenshot"]:
        if not json_data:
            return None
        return cls(
            ScreenshotName=json_data.get("ScreenshotName"),
            IgnoreCoordinates=json_data.get("IgnoreCoordinates"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BaseScreenshot = BaseScreenshot


