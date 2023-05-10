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
class AwsGreengrassCoredefinition(BaseModel):
    LatestVersionArn: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    Name: Optional[str]
    InitialVersion: Optional["_CoreDefinitionVersion"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGreengrassCoredefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGreengrassCoredefinition"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            LatestVersionArn=json_data.get("LatestVersionArn"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            InitialVersion=CoreDefinitionVersion._deserialize(json_data.get("InitialVersion")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGreengrassCoredefinition = AwsGreengrassCoredefinition


@dataclass
class CoreDefinitionVersion(BaseModel):
    Cores: Optional[Sequence["_Core"]]

    @classmethod
    def _deserialize(
        cls: Type["_CoreDefinitionVersion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CoreDefinitionVersion"]:
        if not json_data:
            return None
        return cls(
            Cores=deserialize_list(json_data.get("Cores"), Core),
        )


# work around possible type aliasing issues when variable has same name as a model
_CoreDefinitionVersion = CoreDefinitionVersion


@dataclass
class Core(BaseModel):
    SyncShadow: Optional[bool]
    ThingArn: Optional[str]
    Id: Optional[str]
    CertificateArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Core"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Core"]:
        if not json_data:
            return None
        return cls(
            SyncShadow=json_data.get("SyncShadow"),
            ThingArn=json_data.get("ThingArn"),
            Id=json_data.get("Id"),
            CertificateArn=json_data.get("CertificateArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Core = Core


