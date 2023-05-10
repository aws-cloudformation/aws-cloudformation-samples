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
class AwsSsmDocument(BaseModel):
    Content: Optional[Any]
    Attachments: Optional[Sequence["_AttachmentsSource"]]
    Name: Optional[str]
    VersionName: Optional[str]
    DocumentType: Optional[str]
    DocumentFormat: Optional[str]
    TargetType: Optional[str]
    Tags: Optional[Any]
    Requires: Optional[Sequence["_DocumentRequires"]]
    UpdateMethod: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSsmDocument"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSsmDocument"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Content=json_data.get("Content"),
            Attachments=deserialize_list(json_data.get("Attachments"), AttachmentsSource),
            Name=json_data.get("Name"),
            VersionName=json_data.get("VersionName"),
            DocumentType=json_data.get("DocumentType"),
            DocumentFormat=json_data.get("DocumentFormat"),
            TargetType=json_data.get("TargetType"),
            Tags=json_data.get("Tags"),
            Requires=deserialize_list(json_data.get("Requires"), DocumentRequires),
            UpdateMethod=json_data.get("UpdateMethod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSsmDocument = AwsSsmDocument


@dataclass
class AttachmentsSource(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttachmentsSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttachmentsSource"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttachmentsSource = AttachmentsSource


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
class DocumentRequires(BaseModel):
    Name: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DocumentRequires"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DocumentRequires"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DocumentRequires = DocumentRequires


