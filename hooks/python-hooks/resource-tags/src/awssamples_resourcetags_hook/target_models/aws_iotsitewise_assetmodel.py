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
class AwsIotsitewiseAssetmodel(BaseModel):
    AssetModelId: Optional[str]
    AssetModelArn: Optional[str]
    AssetModelName: Optional[str]
    AssetModelDescription: Optional[str]
    AssetModelProperties: Optional[Sequence["_AssetModelProperty"]]
    AssetModelCompositeModels: Optional[Sequence["_AssetModelCompositeModel"]]
    AssetModelHierarchies: Optional[Sequence["_AssetModelHierarchy"]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotsitewiseAssetmodel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotsitewiseAssetmodel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AssetModelId=json_data.get("AssetModelId"),
            AssetModelArn=json_data.get("AssetModelArn"),
            AssetModelName=json_data.get("AssetModelName"),
            AssetModelDescription=json_data.get("AssetModelDescription"),
            AssetModelProperties=deserialize_list(json_data.get("AssetModelProperties"), AssetModelProperty),
            AssetModelCompositeModels=deserialize_list(json_data.get("AssetModelCompositeModels"), AssetModelCompositeModel),
            AssetModelHierarchies=deserialize_list(json_data.get("AssetModelHierarchies"), AssetModelHierarchy),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotsitewiseAssetmodel = AwsIotsitewiseAssetmodel


@dataclass
class AssetModelProperty(BaseModel):
    LogicalId: Optional[str]
    Name: Optional[str]
    DataType: Optional[str]
    DataTypeSpec: Optional[str]
    Unit: Optional[str]
    Type: Optional["_PropertyType"]

    @classmethod
    def _deserialize(
        cls: Type["_AssetModelProperty"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssetModelProperty"]:
        if not json_data:
            return None
        return cls(
            LogicalId=json_data.get("LogicalId"),
            Name=json_data.get("Name"),
            DataType=json_data.get("DataType"),
            DataTypeSpec=json_data.get("DataTypeSpec"),
            Unit=json_data.get("Unit"),
            Type=PropertyType._deserialize(json_data.get("Type")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssetModelProperty = AssetModelProperty


@dataclass
class PropertyType(BaseModel):
    TypeName: Optional[str]
    Attribute: Optional["_Attribute"]
    Transform: Optional["_Transform"]
    Metric: Optional["_Metric"]

    @classmethod
    def _deserialize(
        cls: Type["_PropertyType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertyType"]:
        if not json_data:
            return None
        return cls(
            TypeName=json_data.get("TypeName"),
            Attribute=Attribute._deserialize(json_data.get("Attribute")),
            Transform=Transform._deserialize(json_data.get("Transform")),
            Metric=Metric._deserialize(json_data.get("Metric")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertyType = PropertyType


@dataclass
class Attribute(BaseModel):
    DefaultValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Attribute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Attribute"]:
        if not json_data:
            return None
        return cls(
            DefaultValue=json_data.get("DefaultValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Attribute = Attribute


@dataclass
class Transform(BaseModel):
    Expression: Optional[str]
    Variables: Optional[Sequence["_ExpressionVariable"]]

    @classmethod
    def _deserialize(
        cls: Type["_Transform"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Transform"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            Variables=deserialize_list(json_data.get("Variables"), ExpressionVariable),
        )


# work around possible type aliasing issues when variable has same name as a model
_Transform = Transform


@dataclass
class ExpressionVariable(BaseModel):
    Name: Optional[str]
    Value: Optional["_VariableValue"]

    @classmethod
    def _deserialize(
        cls: Type["_ExpressionVariable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExpressionVariable"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=VariableValue._deserialize(json_data.get("Value")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExpressionVariable = ExpressionVariable


@dataclass
class VariableValue(BaseModel):
    PropertyLogicalId: Optional[str]
    HierarchyLogicalId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VariableValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VariableValue"]:
        if not json_data:
            return None
        return cls(
            PropertyLogicalId=json_data.get("PropertyLogicalId"),
            HierarchyLogicalId=json_data.get("HierarchyLogicalId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VariableValue = VariableValue


@dataclass
class Metric(BaseModel):
    Expression: Optional[str]
    Variables: Optional[Sequence["_ExpressionVariable"]]
    Window: Optional["_MetricWindow"]

    @classmethod
    def _deserialize(
        cls: Type["_Metric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metric"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            Variables=deserialize_list(json_data.get("Variables"), ExpressionVariable),
            Window=MetricWindow._deserialize(json_data.get("Window")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metric = Metric


@dataclass
class MetricWindow(BaseModel):
    Tumbling: Optional["_TumblingWindow"]

    @classmethod
    def _deserialize(
        cls: Type["_MetricWindow"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricWindow"]:
        if not json_data:
            return None
        return cls(
            Tumbling=TumblingWindow._deserialize(json_data.get("Tumbling")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricWindow = MetricWindow


@dataclass
class TumblingWindow(BaseModel):
    Interval: Optional[str]
    Offset: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TumblingWindow"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TumblingWindow"]:
        if not json_data:
            return None
        return cls(
            Interval=json_data.get("Interval"),
            Offset=json_data.get("Offset"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TumblingWindow = TumblingWindow


@dataclass
class AssetModelCompositeModel(BaseModel):
    Description: Optional[str]
    Name: Optional[str]
    Type: Optional[str]
    CompositeModelProperties: Optional[Sequence["_AssetModelProperty"]]

    @classmethod
    def _deserialize(
        cls: Type["_AssetModelCompositeModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssetModelCompositeModel"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            CompositeModelProperties=deserialize_list(json_data.get("CompositeModelProperties"), AssetModelProperty),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssetModelCompositeModel = AssetModelCompositeModel


@dataclass
class AssetModelHierarchy(BaseModel):
    LogicalId: Optional[str]
    Name: Optional[str]
    ChildAssetModelId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssetModelHierarchy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssetModelHierarchy"]:
        if not json_data:
            return None
        return cls(
            LogicalId=json_data.get("LogicalId"),
            Name=json_data.get("Name"),
            ChildAssetModelId=json_data.get("ChildAssetModelId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssetModelHierarchy = AssetModelHierarchy


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


