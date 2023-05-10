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
class AwsImagebuilderImagerecipe(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    Description: Optional[str]
    Version: Optional[str]
    Components: Optional[Sequence["_ComponentConfiguration"]]
    BlockDeviceMappings: Optional[Sequence["_InstanceBlockDeviceMapping"]]
    ParentImage: Optional[str]
    WorkingDirectory: Optional[str]
    AdditionalInstanceConfiguration: Optional["_AdditionalInstanceConfiguration"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsImagebuilderImagerecipe"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsImagebuilderImagerecipe"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            Version=json_data.get("Version"),
            Components=deserialize_list(json_data.get("Components"), ComponentConfiguration),
            BlockDeviceMappings=deserialize_list(json_data.get("BlockDeviceMappings"), InstanceBlockDeviceMapping),
            ParentImage=json_data.get("ParentImage"),
            WorkingDirectory=json_data.get("WorkingDirectory"),
            AdditionalInstanceConfiguration=AdditionalInstanceConfiguration._deserialize(json_data.get("AdditionalInstanceConfiguration")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsImagebuilderImagerecipe = AwsImagebuilderImagerecipe


@dataclass
class ComponentConfiguration(BaseModel):
    ComponentArn: Optional[str]
    Parameters: Optional[Sequence["_ComponentParameter"]]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentConfiguration"]:
        if not json_data:
            return None
        return cls(
            ComponentArn=json_data.get("ComponentArn"),
            Parameters=deserialize_list(json_data.get("Parameters"), ComponentParameter),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentConfiguration = ComponentConfiguration


@dataclass
class ComponentParameter(BaseModel):
    Name: Optional[str]
    Value: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentParameter"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentParameter = ComponentParameter


@dataclass
class InstanceBlockDeviceMapping(BaseModel):
    DeviceName: Optional[str]
    VirtualName: Optional[str]
    NoDevice: Optional[str]
    Ebs: Optional["_EbsInstanceBlockDeviceSpecification"]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceBlockDeviceMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceBlockDeviceMapping"]:
        if not json_data:
            return None
        return cls(
            DeviceName=json_data.get("DeviceName"),
            VirtualName=json_data.get("VirtualName"),
            NoDevice=json_data.get("NoDevice"),
            Ebs=EbsInstanceBlockDeviceSpecification._deserialize(json_data.get("Ebs")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceBlockDeviceMapping = InstanceBlockDeviceMapping


@dataclass
class EbsInstanceBlockDeviceSpecification(BaseModel):
    Encrypted: Optional[bool]
    DeleteOnTermination: Optional[bool]
    Iops: Optional[int]
    KmsKeyId: Optional[str]
    SnapshotId: Optional[str]
    Throughput: Optional[int]
    VolumeSize: Optional[int]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EbsInstanceBlockDeviceSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsInstanceBlockDeviceSpecification"]:
        if not json_data:
            return None
        return cls(
            Encrypted=json_data.get("Encrypted"),
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            Iops=json_data.get("Iops"),
            KmsKeyId=json_data.get("KmsKeyId"),
            SnapshotId=json_data.get("SnapshotId"),
            Throughput=json_data.get("Throughput"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsInstanceBlockDeviceSpecification = EbsInstanceBlockDeviceSpecification


@dataclass
class AdditionalInstanceConfiguration(BaseModel):
    SystemsManagerAgent: Optional["_SystemsManagerAgent"]
    UserDataOverride: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalInstanceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalInstanceConfiguration"]:
        if not json_data:
            return None
        return cls(
            SystemsManagerAgent=SystemsManagerAgent._deserialize(json_data.get("SystemsManagerAgent")),
            UserDataOverride=json_data.get("UserDataOverride"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalInstanceConfiguration = AdditionalInstanceConfiguration


@dataclass
class SystemsManagerAgent(BaseModel):
    UninstallAfterBuild: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SystemsManagerAgent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SystemsManagerAgent"]:
        if not json_data:
            return None
        return cls(
            UninstallAfterBuild=json_data.get("UninstallAfterBuild"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SystemsManagerAgent = SystemsManagerAgent


