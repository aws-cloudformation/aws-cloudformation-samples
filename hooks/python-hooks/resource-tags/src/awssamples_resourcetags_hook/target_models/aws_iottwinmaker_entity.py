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
class AwsIottwinmakerEntity(BaseModel):
    EntityId: Optional[str]
    EntityName: Optional[str]
    Status: Optional["_Status"]
    HasChildEntities: Optional[bool]
    ParentEntityId: Optional[str]
    Arn: Optional[str]
    Description: Optional[str]
    CreationDateTime: Optional[str]
    UpdateDateTime: Optional[str]
    Tags: Optional[Any]
    WorkspaceId: Optional[str]
    Components: Optional[MutableMapping[str, "_Component"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIottwinmakerEntity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIottwinmakerEntity"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            EntityId=json_data.get("EntityId"),
            EntityName=json_data.get("EntityName"),
            Status=Status._deserialize(json_data.get("Status")),
            HasChildEntities=json_data.get("HasChildEntities"),
            ParentEntityId=json_data.get("ParentEntityId"),
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            CreationDateTime=json_data.get("CreationDateTime"),
            UpdateDateTime=json_data.get("UpdateDateTime"),
            Tags=json_data.get("Tags"),
            WorkspaceId=json_data.get("WorkspaceId"),
            Components=json_data.get("Components"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIottwinmakerEntity = AwsIottwinmakerEntity


@dataclass
class Status(BaseModel):
    State: Optional[str]
    Error: Optional["_Error"]

    @classmethod
    def _deserialize(
        cls: Type["_Status"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Status"]:
        if not json_data:
            return None
        return cls(
            State=json_data.get("State"),
            Error=Error._deserialize(json_data.get("Error")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Status = Status


@dataclass
class Error(BaseModel):
    Message: Optional[str]
    Code: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Error"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Error"]:
        if not json_data:
            return None
        return cls(
            Message=json_data.get("Message"),
            Code=json_data.get("Code"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Error = Error


@dataclass
class Component(BaseModel):
    ComponentName: Optional[str]
    ComponentTypeId: Optional[str]
    Description: Optional[str]
    DefinedIn: Optional[str]
    Properties: Optional[MutableMapping[str, "_Property"]]
    PropertyGroups: Optional[MutableMapping[str, "_PropertyGroup"]]
    Status: Optional["_Status"]

    @classmethod
    def _deserialize(
        cls: Type["_Component"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Component"]:
        if not json_data:
            return None
        return cls(
            ComponentName=json_data.get("ComponentName"),
            ComponentTypeId=json_data.get("ComponentTypeId"),
            Description=json_data.get("Description"),
            DefinedIn=json_data.get("DefinedIn"),
            Properties=json_data.get("Properties"),
            PropertyGroups=json_data.get("PropertyGroups"),
            Status=Status._deserialize(json_data.get("Status")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Component = Component


@dataclass
class Property(BaseModel):
    Definition: Optional["_Definition"]
    Value: Optional["_DataValue"]

    @classmethod
    def _deserialize(
        cls: Type["_Property"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Property"]:
        if not json_data:
            return None
        return cls(
            Definition=Definition._deserialize(json_data.get("Definition")),
            Value=DataValue._deserialize(json_data.get("Value")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Property = Property


@dataclass
class Definition(BaseModel):
    Configuration: Optional[MutableMapping[str, str]]
    DataType: Optional["_DataType"]
    DefaultValue: Optional["_DataValue"]
    IsExternalId: Optional[bool]
    IsFinal: Optional[bool]
    IsImported: Optional[bool]
    IsInherited: Optional[bool]
    IsRequiredInEntity: Optional[bool]
    IsStoredExternally: Optional[bool]
    IsTimeSeries: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Definition"]:
        if not json_data:
            return None
        return cls(
            Configuration=json_data.get("Configuration"),
            DataType=DataType._deserialize(json_data.get("DataType")),
            DefaultValue=DataValue._deserialize(json_data.get("DefaultValue")),
            IsExternalId=json_data.get("IsExternalId"),
            IsFinal=json_data.get("IsFinal"),
            IsImported=json_data.get("IsImported"),
            IsInherited=json_data.get("IsInherited"),
            IsRequiredInEntity=json_data.get("IsRequiredInEntity"),
            IsStoredExternally=json_data.get("IsStoredExternally"),
            IsTimeSeries=json_data.get("IsTimeSeries"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Definition = Definition


@dataclass
class DataType(BaseModel):
    AllowedValues: Optional[Sequence["_DataValue"]]
    NestedType: Optional["_DataType"]
    Relationship: Optional["_Relationship"]
    Type: Optional[str]
    UnitOfMeasure: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataType"]:
        if not json_data:
            return None
        return cls(
            AllowedValues=deserialize_list(json_data.get("AllowedValues"), DataValue),
            NestedType=DataType._deserialize(json_data.get("NestedType")),
            Relationship=Relationship._deserialize(json_data.get("Relationship")),
            Type=json_data.get("Type"),
            UnitOfMeasure=json_data.get("UnitOfMeasure"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataType = DataType


@dataclass
class DataValue(BaseModel):
    BooleanValue: Optional[bool]
    DoubleValue: Optional[float]
    Expression: Optional[str]
    IntegerValue: Optional[int]
    ListValue: Optional[Sequence["_DataValue"]]
    LongValue: Optional[float]
    StringValue: Optional[str]
    MapValue: Optional[MutableMapping[str, "_DataValue"]]
    RelationshipValue: Optional["_RelationshipValue"]

    @classmethod
    def _deserialize(
        cls: Type["_DataValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataValue"]:
        if not json_data:
            return None
        return cls(
            BooleanValue=json_data.get("BooleanValue"),
            DoubleValue=json_data.get("DoubleValue"),
            Expression=json_data.get("Expression"),
            IntegerValue=json_data.get("IntegerValue"),
            ListValue=deserialize_list(json_data.get("ListValue"), DataValue),
            LongValue=json_data.get("LongValue"),
            StringValue=json_data.get("StringValue"),
            MapValue=json_data.get("MapValue"),
            RelationshipValue=RelationshipValue._deserialize(json_data.get("RelationshipValue")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataValue = DataValue


@dataclass
class RelationshipValue(BaseModel):
    TargetComponentName: Optional[str]
    TargetEntityId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelationshipValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelationshipValue"]:
        if not json_data:
            return None
        return cls(
            TargetComponentName=json_data.get("TargetComponentName"),
            TargetEntityId=json_data.get("TargetEntityId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelationshipValue = RelationshipValue


@dataclass
class Relationship(BaseModel):
    RelationshipType: Optional[str]
    TargetComponentTypeId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Relationship"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Relationship"]:
        if not json_data:
            return None
        return cls(
            RelationshipType=json_data.get("RelationshipType"),
            TargetComponentTypeId=json_data.get("TargetComponentTypeId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Relationship = Relationship


@dataclass
class PropertyGroup(BaseModel):
    GroupType: Optional[str]
    PropertyNames: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PropertyGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertyGroup"]:
        if not json_data:
            return None
        return cls(
            GroupType=json_data.get("GroupType"),
            PropertyNames=set_or_none(json_data.get("PropertyNames")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertyGroup = PropertyGroup


