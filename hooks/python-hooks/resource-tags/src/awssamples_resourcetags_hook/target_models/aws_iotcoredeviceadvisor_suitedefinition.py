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
class AwsIotcoredeviceadvisorSuitedefinition(BaseModel):
    SuiteDefinitionConfiguration: Optional["_SuiteDefinitionConfiguration"]
    SuiteDefinitionId: Optional[str]
    SuiteDefinitionArn: Optional[str]
    SuiteDefinitionVersion: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotcoredeviceadvisorSuitedefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotcoredeviceadvisorSuitedefinition"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            SuiteDefinitionConfiguration=SuiteDefinitionConfiguration._deserialize(json_data.get("SuiteDefinitionConfiguration")),
            SuiteDefinitionId=json_data.get("SuiteDefinitionId"),
            SuiteDefinitionArn=json_data.get("SuiteDefinitionArn"),
            SuiteDefinitionVersion=json_data.get("SuiteDefinitionVersion"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotcoredeviceadvisorSuitedefinition = AwsIotcoredeviceadvisorSuitedefinition


@dataclass
class SuiteDefinitionConfiguration(BaseModel):
    DevicePermissionRoleArn: Optional[str]
    Devices: Optional[Sequence["_DeviceUnderTest"]]
    IntendedForQualification: Optional[bool]
    RootGroup: Optional[str]
    SuiteDefinitionName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SuiteDefinitionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SuiteDefinitionConfiguration"]:
        if not json_data:
            return None
        return cls(
            DevicePermissionRoleArn=json_data.get("DevicePermissionRoleArn"),
            Devices=deserialize_list(json_data.get("Devices"), DeviceUnderTest),
            IntendedForQualification=json_data.get("IntendedForQualification"),
            RootGroup=json_data.get("RootGroup"),
            SuiteDefinitionName=json_data.get("SuiteDefinitionName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SuiteDefinitionConfiguration = SuiteDefinitionConfiguration


@dataclass
class DeviceUnderTest(BaseModel):
    CertificateArn: Optional[str]
    ThingArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeviceUnderTest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeviceUnderTest"]:
        if not json_data:
            return None
        return cls(
            CertificateArn=json_data.get("CertificateArn"),
            ThingArn=json_data.get("ThingArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeviceUnderTest = DeviceUnderTest


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


