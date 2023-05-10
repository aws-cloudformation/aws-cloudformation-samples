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
class AwsIottwinmakerComponenttype(BaseModel):
    WorkspaceId: Optional[str]
    ComponentTypeId: Optional[str]
    Description: Optional[str]
    ExtendsFrom: Optional[AbstractSet[str]]
    Functions: Optional[MutableMapping[str, "_Function"]]
    IsSingleton: Optional[bool]
    PropertyDefinitions: Optional[MutableMapping[str, "_PropertyDefinition"]]
    PropertyGroups: Optional[MutableMapping[str, "_PropertyGroup"]]
    Arn: Optional[str]
    CreationDateTime: Optional[str]
    UpdateDateTime: Optional[str]
    Status: Optional["_Status"]
    IsAbstract: Optional[bool]
    IsSchemaInitialized: Optional[bool]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIottwinmakerComponenttype"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIottwinmakerComponenttype"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            WorkspaceId=json_data.get("WorkspaceId"),
            ComponentTypeId=json_data.get("ComponentTypeId"),
            Description=json_data.get("Description"),
            ExtendsFrom=set_or_none(json_data.get("ExtendsFrom")),
            Functions=json_data.get("Functions"),
            IsSingleton=json_data.get("IsSingleton"),
            PropertyDefinitions=json_data.get("PropertyDefinitions"),
            PropertyGroups=json_data.get("PropertyGroups"),
            Arn=json_data.get("Arn"),
            CreationDateTime=json_data.get("CreationDateTime"),
            UpdateDateTime=json_data.get("UpdateDateTime"),
            Status=Status._deserialize(json_data.get("Status")),
            IsAbstract=json_data.get("IsAbstract"),
            IsSchemaInitialized=json_data.get("IsSchemaInitialized"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIottwinmakerComponenttype = AwsIottwinmakerComponenttype


@dataclass
class Function(BaseModel):
    ImplementedBy: Optional["_DataConnector"]
    RequiredProperties: Optional[AbstractSet[str]]
    Scope: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Function"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Function"]:
        if not json_data:
            return None
        return cls(
            ImplementedBy=DataConnector._deserialize(json_data.get("ImplementedBy")),
            RequiredProperties=set_or_none(json_data.get("RequiredProperties")),
            Scope=json_data.get("Scope"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Function = Function


@dataclass
class DataConnector(BaseModel):
    IsNative: Optional[bool]
    Lambda: Optional["_LambdaFunction"]

    @classmethod
    def _deserialize(
        cls: Type["_DataConnector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataConnector"]:
        if not json_data:
            return None
        return cls(
            IsNative=json_data.get("IsNative"),
            Lambda=LambdaFunction._deserialize(json_data.get("Lambda")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataConnector = DataConnector


@dataclass
class LambdaFunction(BaseModel):
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaFunction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaFunction"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaFunction = LambdaFunction


@dataclass
class PropertyDefinition(BaseModel):
    Configurations: Optional[MutableMapping[str, str]]
    DataType: Optional["_DataType"]
    DefaultValue: Optional["_DataValue"]
    IsExternalId: Optional[bool]
    IsRequiredInEntity: Optional[bool]
    IsStoredExternally: Optional[bool]
    IsTimeSeries: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PropertyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertyDefinition"]:
        if not json_data:
            return None
        return cls(
            Configurations=json_data.get("Configurations"),
            DataType=DataType._deserialize(json_data.get("DataType")),
            DefaultValue=DataValue._deserialize(json_data.get("DefaultValue")),
            IsExternalId=json_data.get("IsExternalId"),
            IsRequiredInEntity=json_data.get("IsRequiredInEntity"),
            IsStoredExternally=json_data.get("IsStoredExternally"),
            IsTimeSeries=json_data.get("IsTimeSeries"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertyDefinition = PropertyDefinition


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


