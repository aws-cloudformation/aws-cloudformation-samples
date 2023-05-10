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
class AwsForecastDataset(BaseModel):
    Arn: Optional[str]
    DatasetName: Optional[str]
    DatasetType: Optional[str]
    DataFrequency: Optional[str]
    Domain: Optional[str]
    EncryptionConfig: Optional["_EncryptionConfig"]
    Schema: Optional["_Schema"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsForecastDataset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsForecastDataset"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            DatasetName=json_data.get("DatasetName"),
            DatasetType=json_data.get("DatasetType"),
            DataFrequency=json_data.get("DataFrequency"),
            Domain=json_data.get("Domain"),
            EncryptionConfig=EncryptionConfig._deserialize(json_data.get("EncryptionConfig")),
            Schema=Schema._deserialize(json_data.get("Schema")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsForecastDataset = AwsForecastDataset


@dataclass
class EncryptionConfig(BaseModel):
    KmsKeyArn: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfig"]:
        if not json_data:
            return None
        return cls(
            KmsKeyArn=json_data.get("KmsKeyArn"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfig = EncryptionConfig


@dataclass
class Schema(BaseModel):
    Attributes: Optional[Sequence["_Attributes"]]

    @classmethod
    def _deserialize(
        cls: Type["_Schema"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Schema"]:
        if not json_data:
            return None
        return cls(
            Attributes=deserialize_list(json_data.get("Attributes"), Attributes),
        )


# work around possible type aliasing issues when variable has same name as a model
_Schema = Schema


@dataclass
class Attributes(BaseModel):
    AttributeName: Optional[str]
    AttributeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Attributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Attributes"]:
        if not json_data:
            return None
        return cls(
            AttributeName=json_data.get("AttributeName"),
            AttributeType=json_data.get("AttributeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Attributes = Attributes


@dataclass
class Tags(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


