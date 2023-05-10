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
class AwsDatasyncLocationefs(BaseModel):
    Ec2Config: Optional["_Ec2Config"]
    EfsFilesystemArn: Optional[str]
    AccessPointArn: Optional[str]
    FileSystemAccessRoleArn: Optional[str]
    InTransitEncryption: Optional[str]
    Subdirectory: Optional[str]
    Tags: Optional[Any]
    LocationArn: Optional[str]
    LocationUri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDatasyncLocationefs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDatasyncLocationefs"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Ec2Config=Ec2Config._deserialize(json_data.get("Ec2Config")),
            EfsFilesystemArn=json_data.get("EfsFilesystemArn"),
            AccessPointArn=json_data.get("AccessPointArn"),
            FileSystemAccessRoleArn=json_data.get("FileSystemAccessRoleArn"),
            InTransitEncryption=json_data.get("InTransitEncryption"),
            Subdirectory=json_data.get("Subdirectory"),
            Tags=json_data.get("Tags"),
            LocationArn=json_data.get("LocationArn"),
            LocationUri=json_data.get("LocationUri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDatasyncLocationefs = AwsDatasyncLocationefs


@dataclass
class Ec2Config(BaseModel):
    SecurityGroupArns: Optional[Sequence[str]]
    SubnetArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ec2Config"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ec2Config"]:
        if not json_data:
            return None
        return cls(
            SecurityGroupArns=json_data.get("SecurityGroupArns"),
            SubnetArn=json_data.get("SubnetArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ec2Config = Ec2Config


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


