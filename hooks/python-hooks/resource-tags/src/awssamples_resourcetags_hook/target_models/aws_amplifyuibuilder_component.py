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
class AwsAmplifyuibuilderComponent(BaseModel):
    AppId: Optional[str]
    BindingProperties: Optional[MutableMapping[str, "_ComponentBindingPropertiesValue"]]
    Children: Optional[Sequence["_ComponentChild"]]
    CollectionProperties: Optional[MutableMapping[str, "_ComponentDataConfiguration"]]
    ComponentType: Optional[str]
    EnvironmentName: Optional[str]
    Events: Optional[MutableMapping[str, "_ComponentEvent"]]
    Id: Optional[str]
    Name: Optional[str]
    Overrides: Optional[MutableMapping[str, MutableMapping[str, str]]]
    Properties: Optional[MutableMapping[str, "_ComponentProperty"]]
    SchemaVersion: Optional[str]
    SourceId: Optional[str]
    Tags: Optional[Any]
    Variants: Optional[Sequence["_ComponentVariant"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAmplifyuibuilderComponent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAmplifyuibuilderComponent"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AppId=json_data.get("AppId"),
            BindingProperties=json_data.get("BindingProperties"),
            Children=deserialize_list(json_data.get("Children"), ComponentChild),
            CollectionProperties=json_data.get("CollectionProperties"),
            ComponentType=json_data.get("ComponentType"),
            EnvironmentName=json_data.get("EnvironmentName"),
            Events=json_data.get("Events"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Overrides=json_data.get("Overrides"),
            Properties=json_data.get("Properties"),
            SchemaVersion=json_data.get("SchemaVersion"),
            SourceId=json_data.get("SourceId"),
            Tags=json_data.get("Tags"),
            Variants=deserialize_list(json_data.get("Variants"), ComponentVariant),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAmplifyuibuilderComponent = AwsAmplifyuibuilderComponent


@dataclass
class ComponentBindingPropertiesValue(BaseModel):
    Type: Optional[str]
    BindingProperties: Optional["_ComponentBindingPropertiesValueProperties"]
    DefaultValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentBindingPropertiesValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentBindingPropertiesValue"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            BindingProperties=ComponentBindingPropertiesValueProperties._deserialize(json_data.get("BindingProperties")),
            DefaultValue=json_data.get("DefaultValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentBindingPropertiesValue = ComponentBindingPropertiesValue


@dataclass
class ComponentBindingPropertiesValueProperties(BaseModel):
    Model: Optional[str]
    Field: Optional[str]
    Predicates: Optional[Sequence["_Predicate"]]
    UserAttribute: Optional[str]
    Bucket: Optional[str]
    Key: Optional[str]
    DefaultValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentBindingPropertiesValueProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentBindingPropertiesValueProperties"]:
        if not json_data:
            return None
        return cls(
            Model=json_data.get("Model"),
            Field=json_data.get("Field"),
            Predicates=deserialize_list(json_data.get("Predicates"), Predicate),
            UserAttribute=json_data.get("UserAttribute"),
            Bucket=json_data.get("Bucket"),
            Key=json_data.get("Key"),
            DefaultValue=json_data.get("DefaultValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentBindingPropertiesValueProperties = ComponentBindingPropertiesValueProperties


@dataclass
class Predicate(BaseModel):
    Or: Optional[Sequence["_Predicate"]]
    And: Optional[Sequence["_Predicate"]]
    Field: Optional[str]
    Operator: Optional[str]
    Operand: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Predicate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Predicate"]:
        if not json_data:
            return None
        return cls(
            Or=deserialize_list(json_data.get("Or"), Predicate),
            And=deserialize_list(json_data.get("And"), Predicate),
            Field=json_data.get("Field"),
            Operator=json_data.get("Operator"),
            Operand=json_data.get("Operand"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Predicate = Predicate


@dataclass
class ComponentChild(BaseModel):
    ComponentType: Optional[str]
    Name: Optional[str]
    Properties: Optional[MutableMapping[str, "_ComponentProperty"]]
    Children: Optional[Sequence["_ComponentChild"]]
    Events: Optional[MutableMapping[str, "_ComponentEvent"]]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentChild"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentChild"]:
        if not json_data:
            return None
        return cls(
            ComponentType=json_data.get("ComponentType"),
            Name=json_data.get("Name"),
            Properties=json_data.get("Properties"),
            Children=deserialize_list(json_data.get("Children"), ComponentChild),
            Events=json_data.get("Events"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentChild = ComponentChild


@dataclass
class ComponentProperty(BaseModel):
    Value: Optional[str]
    BindingProperties: Optional["_ComponentPropertyBindingProperties"]
    CollectionBindingProperties: Optional["_ComponentPropertyBindingProperties"]
    DefaultValue: Optional[str]
    Model: Optional[str]
    Bindings: Optional[MutableMapping[str, "_FormBindingElement"]]
    Event: Optional[str]
    UserAttribute: Optional[str]
    Concat: Optional[Sequence["_ComponentProperty"]]
    Condition: Optional["_ComponentConditionProperty"]
    Configured: Optional[bool]
    Type: Optional[str]
    ImportedValue: Optional[str]
    ComponentName: Optional[str]
    Property: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentProperty"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentProperty"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            BindingProperties=ComponentPropertyBindingProperties._deserialize(json_data.get("BindingProperties")),
            CollectionBindingProperties=ComponentPropertyBindingProperties._deserialize(json_data.get("CollectionBindingProperties")),
            DefaultValue=json_data.get("DefaultValue"),
            Model=json_data.get("Model"),
            Bindings=json_data.get("Bindings"),
            Event=json_data.get("Event"),
            UserAttribute=json_data.get("UserAttribute"),
            Concat=deserialize_list(json_data.get("Concat"), ComponentProperty),
            Condition=ComponentConditionProperty._deserialize(json_data.get("Condition")),
            Configured=json_data.get("Configured"),
            Type=json_data.get("Type"),
            ImportedValue=json_data.get("ImportedValue"),
            ComponentName=json_data.get("ComponentName"),
            Property=json_data.get("Property"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentProperty = ComponentProperty


@dataclass
class ComponentPropertyBindingProperties(BaseModel):
    Property: Optional[str]
    Field: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentPropertyBindingProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentPropertyBindingProperties"]:
        if not json_data:
            return None
        return cls(
            Property=json_data.get("Property"),
            Field=json_data.get("Field"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentPropertyBindingProperties = ComponentPropertyBindingProperties


@dataclass
class FormBindingElement(BaseModel):
    Element: Optional[str]
    Property: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FormBindingElement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FormBindingElement"]:
        if not json_data:
            return None
        return cls(
            Element=json_data.get("Element"),
            Property=json_data.get("Property"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FormBindingElement = FormBindingElement


@dataclass
class ComponentConditionProperty(BaseModel):
    Property: Optional[str]
    Field: Optional[str]
    Operator: Optional[str]
    Operand: Optional[str]
    Then: Optional["_ComponentProperty"]
    Else: Optional["_ComponentProperty"]
    OperandType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentConditionProperty"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentConditionProperty"]:
        if not json_data:
            return None
        return cls(
            Property=json_data.get("Property"),
            Field=json_data.get("Field"),
            Operator=json_data.get("Operator"),
            Operand=json_data.get("Operand"),
            Then=ComponentProperty._deserialize(json_data.get("Then")),
            Else=ComponentProperty._deserialize(json_data.get("Else")),
            OperandType=json_data.get("OperandType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentConditionProperty = ComponentConditionProperty


@dataclass
class ComponentEvent(BaseModel):
    Action: Optional[str]
    Parameters: Optional["_ActionParameters"]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentEvent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentEvent"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Parameters=ActionParameters._deserialize(json_data.get("Parameters")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentEvent = ComponentEvent


@dataclass
class ActionParameters(BaseModel):
    Type: Optional["_ComponentProperty"]
    Url: Optional["_ComponentProperty"]
    Anchor: Optional["_ComponentProperty"]
    Target: Optional["_ComponentProperty"]
    Global: Optional["_ComponentProperty"]
    Model: Optional[str]
    Id: Optional["_ComponentProperty"]
    Fields: Optional[MutableMapping[str, "_ComponentProperty"]]
    State: Optional["_MutationActionSetStateParameter"]

    @classmethod
    def _deserialize(
        cls: Type["_ActionParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionParameters"]:
        if not json_data:
            return None
        return cls(
            Type=ComponentProperty._deserialize(json_data.get("Type")),
            Url=ComponentProperty._deserialize(json_data.get("Url")),
            Anchor=ComponentProperty._deserialize(json_data.get("Anchor")),
            Target=ComponentProperty._deserialize(json_data.get("Target")),
            Global=ComponentProperty._deserialize(json_data.get("Global")),
            Model=json_data.get("Model"),
            Id=ComponentProperty._deserialize(json_data.get("Id")),
            Fields=json_data.get("Fields"),
            State=MutationActionSetStateParameter._deserialize(json_data.get("State")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionParameters = ActionParameters


@dataclass
class MutationActionSetStateParameter(BaseModel):
    ComponentName: Optional[str]
    Property: Optional[str]
    Set: Optional["_ComponentProperty"]

    @classmethod
    def _deserialize(
        cls: Type["_MutationActionSetStateParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MutationActionSetStateParameter"]:
        if not json_data:
            return None
        return cls(
            ComponentName=json_data.get("ComponentName"),
            Property=json_data.get("Property"),
            Set=ComponentProperty._deserialize(json_data.get("Set")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MutationActionSetStateParameter = MutationActionSetStateParameter


@dataclass
class ComponentDataConfiguration(BaseModel):
    Model: Optional[str]
    Sort: Optional[Sequence["_SortProperty"]]
    Predicate: Optional["_Predicate"]
    Identifiers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentDataConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentDataConfiguration"]:
        if not json_data:
            return None
        return cls(
            Model=json_data.get("Model"),
            Sort=deserialize_list(json_data.get("Sort"), SortProperty),
            Predicate=Predicate._deserialize(json_data.get("Predicate")),
            Identifiers=json_data.get("Identifiers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentDataConfiguration = ComponentDataConfiguration


@dataclass
class SortProperty(BaseModel):
    Field: Optional[str]
    Direction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SortProperty"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SortProperty"]:
        if not json_data:
            return None
        return cls(
            Field=json_data.get("Field"),
            Direction=json_data.get("Direction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SortProperty = SortProperty


@dataclass
class ComponentVariant(BaseModel):
    VariantValues: Optional[MutableMapping[str, str]]
    Overrides: Optional[MutableMapping[str, MutableMapping[str, str]]]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentVariant"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentVariant"]:
        if not json_data:
            return None
        return cls(
            VariantValues=json_data.get("VariantValues"),
            Overrides=json_data.get("Overrides"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentVariant = ComponentVariant


