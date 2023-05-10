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
class AwsConnectTasktemplate(BaseModel):
    Arn: Optional[str]
    InstanceArn: Optional[str]
    Name: Optional[str]
    Description: Optional[str]
    ContactFlowArn: Optional[str]
    Constraints: Optional["_Constraints"]
    Defaults: Optional[Sequence["_DefaultFieldValue"]]
    Fields: Optional[Sequence["_Field"]]
    Status: Optional[str]
    ClientToken: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConnectTasktemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConnectTasktemplate"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            InstanceArn=json_data.get("InstanceArn"),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            ContactFlowArn=json_data.get("ContactFlowArn"),
            Constraints=Constraints._deserialize(json_data.get("Constraints")),
            Defaults=deserialize_list(json_data.get("Defaults"), DefaultFieldValue),
            Fields=deserialize_list(json_data.get("Fields"), Field),
            Status=json_data.get("Status"),
            ClientToken=json_data.get("ClientToken"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConnectTasktemplate = AwsConnectTasktemplate


@dataclass
class Constraints(BaseModel):
    InvisibleFields: Optional[Sequence["_InvisibleFieldInfo"]]
    RequiredFields: Optional[Sequence["_RequiredFieldInfo"]]
    ReadOnlyFields: Optional[Sequence["_ReadOnlyFieldInfo"]]

    @classmethod
    def _deserialize(
        cls: Type["_Constraints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Constraints"]:
        if not json_data:
            return None
        return cls(
            InvisibleFields=deserialize_list(json_data.get("InvisibleFields"), InvisibleFieldInfo),
            RequiredFields=deserialize_list(json_data.get("RequiredFields"), RequiredFieldInfo),
            ReadOnlyFields=deserialize_list(json_data.get("ReadOnlyFields"), ReadOnlyFieldInfo),
        )


# work around possible type aliasing issues when variable has same name as a model
_Constraints = Constraints


@dataclass
class InvisibleFieldInfo(BaseModel):
    Id: Optional["_FieldIdentifier"]

    @classmethod
    def _deserialize(
        cls: Type["_InvisibleFieldInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InvisibleFieldInfo"]:
        if not json_data:
            return None
        return cls(
            Id=FieldIdentifier._deserialize(json_data.get("Id")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InvisibleFieldInfo = InvisibleFieldInfo


@dataclass
class FieldIdentifier(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FieldIdentifier"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FieldIdentifier"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FieldIdentifier = FieldIdentifier


@dataclass
class RequiredFieldInfo(BaseModel):
    Id: Optional["_FieldIdentifier"]

    @classmethod
    def _deserialize(
        cls: Type["_RequiredFieldInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequiredFieldInfo"]:
        if not json_data:
            return None
        return cls(
            Id=FieldIdentifier._deserialize(json_data.get("Id")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequiredFieldInfo = RequiredFieldInfo


@dataclass
class ReadOnlyFieldInfo(BaseModel):
    Id: Optional["_FieldIdentifier"]

    @classmethod
    def _deserialize(
        cls: Type["_ReadOnlyFieldInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReadOnlyFieldInfo"]:
        if not json_data:
            return None
        return cls(
            Id=FieldIdentifier._deserialize(json_data.get("Id")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReadOnlyFieldInfo = ReadOnlyFieldInfo


@dataclass
class DefaultFieldValue(BaseModel):
    Id: Optional["_FieldIdentifier"]
    DefaultValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultFieldValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultFieldValue"]:
        if not json_data:
            return None
        return cls(
            Id=FieldIdentifier._deserialize(json_data.get("Id")),
            DefaultValue=json_data.get("DefaultValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultFieldValue = DefaultFieldValue


@dataclass
class Field(BaseModel):
    Id: Optional["_FieldIdentifier"]
    Description: Optional[str]
    Type: Optional[str]
    SingleSelectOptions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Field"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Field"]:
        if not json_data:
            return None
        return cls(
            Id=FieldIdentifier._deserialize(json_data.get("Id")),
            Description=json_data.get("Description"),
            Type=json_data.get("Type"),
            SingleSelectOptions=json_data.get("SingleSelectOptions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Field = Field


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


