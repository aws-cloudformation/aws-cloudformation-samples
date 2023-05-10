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
class AwsLambdaFunction(BaseModel):
    Description: Optional[str]
    TracingConfig: Optional["_TracingConfig"]
    VpcConfig: Optional["_VpcConfig"]
    RuntimeManagementConfig: Optional["_RuntimeManagementConfig"]
    ReservedConcurrentExecutions: Optional[int]
    SnapStart: Optional["_SnapStart"]
    FileSystemConfigs: Optional[Sequence["_FileSystemConfig"]]
    FunctionName: Optional[str]
    Runtime: Optional[str]
    KmsKeyArn: Optional[str]
    PackageType: Optional[str]
    CodeSigningConfigArn: Optional[str]
    Layers: Optional[Sequence[str]]
    Tags: Optional[Any]
    ImageConfig: Optional["_ImageConfig"]
    MemorySize: Optional[int]
    DeadLetterConfig: Optional["_DeadLetterConfig"]
    Timeout: Optional[int]
    Handler: Optional[str]
    SnapStartResponse: Optional["_SnapStartResponse"]
    Code: Optional["_Code"]
    Role: Optional[str]
    Environment: Optional["_Environment"]
    Arn: Optional[str]
    EphemeralStorage: Optional["_EphemeralStorage"]
    Architectures: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLambdaFunction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLambdaFunction"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            TracingConfig=TracingConfig._deserialize(json_data.get("TracingConfig")),
            VpcConfig=VpcConfig._deserialize(json_data.get("VpcConfig")),
            RuntimeManagementConfig=RuntimeManagementConfig._deserialize(json_data.get("RuntimeManagementConfig")),
            ReservedConcurrentExecutions=json_data.get("ReservedConcurrentExecutions"),
            SnapStart=SnapStart._deserialize(json_data.get("SnapStart")),
            FileSystemConfigs=deserialize_list(json_data.get("FileSystemConfigs"), FileSystemConfig),
            FunctionName=json_data.get("FunctionName"),
            Runtime=json_data.get("Runtime"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            PackageType=json_data.get("PackageType"),
            CodeSigningConfigArn=json_data.get("CodeSigningConfigArn"),
            Layers=json_data.get("Layers"),
            Tags=json_data.get("Tags"),
            ImageConfig=ImageConfig._deserialize(json_data.get("ImageConfig")),
            MemorySize=json_data.get("MemorySize"),
            DeadLetterConfig=DeadLetterConfig._deserialize(json_data.get("DeadLetterConfig")),
            Timeout=json_data.get("Timeout"),
            Handler=json_data.get("Handler"),
            SnapStartResponse=SnapStartResponse._deserialize(json_data.get("SnapStartResponse")),
            Code=Code._deserialize(json_data.get("Code")),
            Role=json_data.get("Role"),
            Environment=Environment._deserialize(json_data.get("Environment")),
            Arn=json_data.get("Arn"),
            EphemeralStorage=EphemeralStorage._deserialize(json_data.get("EphemeralStorage")),
            Architectures=json_data.get("Architectures"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLambdaFunction = AwsLambdaFunction


@dataclass
class TracingConfig(BaseModel):
    Mode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TracingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TracingConfig"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TracingConfig = TracingConfig


@dataclass
class VpcConfig(BaseModel):
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfig"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetIds=json_data.get("SubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfig = VpcConfig


@dataclass
class RuntimeManagementConfig(BaseModel):
    UpdateRuntimeOn: Optional[str]
    RuntimeVersionArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RuntimeManagementConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuntimeManagementConfig"]:
        if not json_data:
            return None
        return cls(
            UpdateRuntimeOn=json_data.get("UpdateRuntimeOn"),
            RuntimeVersionArn=json_data.get("RuntimeVersionArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuntimeManagementConfig = RuntimeManagementConfig


@dataclass
class SnapStart(BaseModel):
    ApplyOn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnapStart"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapStart"]:
        if not json_data:
            return None
        return cls(
            ApplyOn=json_data.get("ApplyOn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapStart = SnapStart


@dataclass
class FileSystemConfig(BaseModel):
    Arn: Optional[str]
    LocalMountPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FileSystemConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileSystemConfig"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            LocalMountPath=json_data.get("LocalMountPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileSystemConfig = FileSystemConfig


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


@dataclass
class ImageConfig(BaseModel):
    WorkingDirectory: Optional[str]
    Command: Optional[Sequence[str]]
    EntryPoint: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ImageConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImageConfig"]:
        if not json_data:
            return None
        return cls(
            WorkingDirectory=json_data.get("WorkingDirectory"),
            Command=json_data.get("Command"),
            EntryPoint=json_data.get("EntryPoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImageConfig = ImageConfig


@dataclass
class DeadLetterConfig(BaseModel):
    TargetArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeadLetterConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeadLetterConfig"]:
        if not json_data:
            return None
        return cls(
            TargetArn=json_data.get("TargetArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeadLetterConfig = DeadLetterConfig


@dataclass
class SnapStartResponse(BaseModel):
    OptimizationStatus: Optional[str]
    ApplyOn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnapStartResponse"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapStartResponse"]:
        if not json_data:
            return None
        return cls(
            OptimizationStatus=json_data.get("OptimizationStatus"),
            ApplyOn=json_data.get("ApplyOn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapStartResponse = SnapStartResponse


@dataclass
class Code(BaseModel):
    S3ObjectVersion: Optional[str]
    S3Bucket: Optional[str]
    ZipFile: Optional[str]
    S3Key: Optional[str]
    ImageUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Code"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Code"]:
        if not json_data:
            return None
        return cls(
            S3ObjectVersion=json_data.get("S3ObjectVersion"),
            S3Bucket=json_data.get("S3Bucket"),
            ZipFile=json_data.get("ZipFile"),
            S3Key=json_data.get("S3Key"),
            ImageUri=json_data.get("ImageUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Code = Code


@dataclass
class Environment(BaseModel):
    Variables: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_Environment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Environment"]:
        if not json_data:
            return None
        return cls(
            Variables=json_data.get("Variables"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Environment = Environment


@dataclass
class EphemeralStorage(BaseModel):
    Size: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_EphemeralStorage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EphemeralStorage"]:
        if not json_data:
            return None
        return cls(
            Size=json_data.get("Size"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EphemeralStorage = EphemeralStorage


