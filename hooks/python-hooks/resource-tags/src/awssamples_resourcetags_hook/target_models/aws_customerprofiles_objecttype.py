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
class AwsCustomerprofilesObjecttype(BaseModel):
    DomainName: Optional[str]
    ObjectTypeName: Optional[str]
    AllowProfileCreation: Optional[bool]
    Description: Optional[str]
    EncryptionKey: Optional[str]
    ExpirationDays: Optional[int]
    Fields: Optional[Sequence["_FieldMap"]]
    Keys: Optional[Sequence["_KeyMap"]]
    CreatedAt: Optional[str]
    LastUpdatedAt: Optional[str]
    Tags: Optional[Any]
    TemplateId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCustomerprofilesObjecttype"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCustomerprofilesObjecttype"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DomainName=json_data.get("DomainName"),
            ObjectTypeName=json_data.get("ObjectTypeName"),
            AllowProfileCreation=json_data.get("AllowProfileCreation"),
            Description=json_data.get("Description"),
            EncryptionKey=json_data.get("EncryptionKey"),
            ExpirationDays=json_data.get("ExpirationDays"),
            Fields=deserialize_list(json_data.get("Fields"), FieldMap),
            Keys=deserialize_list(json_data.get("Keys"), KeyMap),
            CreatedAt=json_data.get("CreatedAt"),
            LastUpdatedAt=json_data.get("LastUpdatedAt"),
            Tags=json_data.get("Tags"),
            TemplateId=json_data.get("TemplateId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCustomerprofilesObjecttype = AwsCustomerprofilesObjecttype


@dataclass
class FieldMap(BaseModel):
    Name: Optional[str]
    ObjectTypeField: Optional["_ObjectTypeField"]

    @classmethod
    def _deserialize(
        cls: Type["_FieldMap"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldMap"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            ObjectTypeField=ObjectTypeField._deserialize(json_data.get("ObjectTypeField")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldMap = FieldMap


@dataclass
class ObjectTypeField(BaseModel):
    Source: Optional[str]
    Target: Optional[str]
    ContentType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ObjectTypeField"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObjectTypeField"]:
        if not json_data:
            return None
        return cls(
            Source=json_data.get("Source"),
            Target=json_data.get("Target"),
            ContentType=json_data.get("ContentType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObjectTypeField = ObjectTypeField


@dataclass
class KeyMap(BaseModel):
    Name: Optional[str]
    ObjectTypeKeyList: Optional[Sequence["_ObjectTypeKey"]]

    @classmethod
    def _deserialize(
        cls: Type["_KeyMap"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyMap"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            ObjectTypeKeyList=deserialize_list(json_data.get("ObjectTypeKeyList"), ObjectTypeKey),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyMap = KeyMap


@dataclass
class ObjectTypeKey(BaseModel):
    FieldNames: Optional[Sequence[str]]
    StandardIdentifiers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ObjectTypeKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObjectTypeKey"]:
        if not json_data:
            return None
        return cls(
            FieldNames=json_data.get("FieldNames"),
            StandardIdentifiers=json_data.get("StandardIdentifiers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObjectTypeKey = ObjectTypeKey


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


