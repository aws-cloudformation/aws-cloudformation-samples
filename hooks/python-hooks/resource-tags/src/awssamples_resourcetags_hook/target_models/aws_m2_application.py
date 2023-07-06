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
class AwsM2Application(BaseModel):
    ApplicationArn: Optional[str]
    ApplicationId: Optional[str]
    Definition: Optional["_Definition"]
    Description: Optional[str]
    EngineType: Optional[str]
    KmsKeyId: Optional[str]
    Name: Optional[str]
    RoleArn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsM2Application"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsM2Application"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ApplicationArn=json_data.get("ApplicationArn"),
            ApplicationId=json_data.get("ApplicationId"),
            Definition=Definition._deserialize(json_data.get("Definition")),
            Description=json_data.get("Description"),
            EngineType=json_data.get("EngineType"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Name=json_data.get("Name"),
            RoleArn=json_data.get("RoleArn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsM2Application = AwsM2Application


@dataclass
class Definition(BaseModel):
    S3Location: Optional[str]
    Content: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Definition"]:
        if not json_data:
            return None
        return cls(
            S3Location=json_data.get("S3Location"),
            Content=json_data.get("Content"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Definition = Definition


