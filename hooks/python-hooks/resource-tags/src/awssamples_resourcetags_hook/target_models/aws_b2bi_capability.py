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
class AwsB2biCapability(BaseModel):
    CapabilityArn: Optional[str]
    CapabilityId: Optional[str]
    Configuration: Optional["_CapabilityConfiguration"]
    CreatedAt: Optional[str]
    InstructionsDocuments: Optional[Sequence["_S3Location"]]
    ModifiedAt: Optional[str]
    Name: Optional[str]
    Tags: Optional[Any]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsB2biCapability"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsB2biCapability"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CapabilityArn=json_data.get("CapabilityArn"),
            CapabilityId=json_data.get("CapabilityId"),
            Configuration=CapabilityConfiguration._deserialize(json_data.get("Configuration")),
            CreatedAt=json_data.get("CreatedAt"),
            InstructionsDocuments=deserialize_list(json_data.get("InstructionsDocuments"), S3Location),
            ModifiedAt=json_data.get("ModifiedAt"),
            Name=json_data.get("Name"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsB2biCapability = AwsB2biCapability


@dataclass
class CapabilityConfiguration(BaseModel):
    Edi: Optional["_EdiConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_CapabilityConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapabilityConfiguration"]:
        if not json_data:
            return None
        return cls(
            Edi=EdiConfiguration._deserialize(json_data.get("Edi")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapabilityConfiguration = CapabilityConfiguration


@dataclass
class EdiConfiguration(BaseModel):
    Type: Optional["_EdiType"]
    InputLocation: Optional["_S3Location"]
    OutputLocation: Optional["_S3Location"]
    TransformerId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EdiConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EdiConfiguration"]:
        if not json_data:
            return None
        return cls(
            Type=EdiType._deserialize(json_data.get("Type")),
            InputLocation=S3Location._deserialize(json_data.get("InputLocation")),
            OutputLocation=S3Location._deserialize(json_data.get("OutputLocation")),
            TransformerId=json_data.get("TransformerId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EdiConfiguration = EdiConfiguration


@dataclass
class EdiType(BaseModel):
    X12Details: Optional["_X12Details"]

    @classmethod
    def _deserialize(
        cls: Type["_EdiType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EdiType"]:
        if not json_data:
            return None
        return cls(
            X12Details=X12Details._deserialize(json_data.get("X12Details")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EdiType = EdiType


@dataclass
class X12Details(BaseModel):
    TransactionSet: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_X12Details"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_X12Details"]:
        if not json_data:
            return None
        return cls(
            TransactionSet=json_data.get("TransactionSet"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_X12Details = X12Details


@dataclass
class S3Location(BaseModel):
    BucketName: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Location"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Location"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Location = S3Location


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


