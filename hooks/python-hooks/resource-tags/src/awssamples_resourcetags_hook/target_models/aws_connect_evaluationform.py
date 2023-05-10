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
class AwsConnectEvaluationform(BaseModel):
    Title: Optional[str]
    Description: Optional[str]
    EvaluationFormArn: Optional[str]
    InstanceArn: Optional[str]
    Items: Optional[Sequence["_EvaluationFormBaseItem"]]
    ScoringStrategy: Optional["_ScoringStrategy"]
    Status: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConnectEvaluationform"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConnectEvaluationform"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Title=json_data.get("Title"),
            Description=json_data.get("Description"),
            EvaluationFormArn=json_data.get("EvaluationFormArn"),
            InstanceArn=json_data.get("InstanceArn"),
            Items=deserialize_list(json_data.get("Items"), EvaluationFormBaseItem),
            ScoringStrategy=ScoringStrategy._deserialize(json_data.get("ScoringStrategy")),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConnectEvaluationform = AwsConnectEvaluationform


@dataclass
class EvaluationFormBaseItem(BaseModel):
    Section: Optional["_EvaluationFormSection"]

    @classmethod
    def _deserialize(
        cls: Type["_EvaluationFormBaseItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EvaluationFormBaseItem"]:
        if not json_data:
            return None
        return cls(
            Section=EvaluationFormSection._deserialize(json_data.get("Section")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EvaluationFormBaseItem = EvaluationFormBaseItem


@dataclass
class EvaluationFormSection(BaseModel):
    Title: Optional[str]
    Instructions: Optional[str]
    RefId: Optional[str]
    Items: Optional[Sequence["_EvaluationFormItem"]]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EvaluationFormSection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EvaluationFormSection"]:
        if not json_data:
            return None
        return cls(
            Title=json_data.get("Title"),
            Instructions=json_data.get("Instructions"),
            RefId=json_data.get("RefId"),
            Items=deserialize_list(json_data.get("Items"), EvaluationFormItem),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EvaluationFormSection = EvaluationFormSection


@dataclass
class EvaluationFormItem(BaseModel):
    Section: Optional["_EvaluationFormSection"]
    Question: Optional["_EvaluationFormQuestion"]

    @classmethod
    def _deserialize(
        cls: Type["_EvaluationFormItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EvaluationFormItem"]:
        if not json_data:
            return None
        return cls(
            Section=EvaluationFormSection._deserialize(json_data.get("Section")),
            Question=EvaluationFormQuestion._deserialize(json_data.get("Question")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EvaluationFormItem = EvaluationFormItem


@dataclass
class EvaluationFormQuestion(BaseModel):
    Title: Optional[str]
    Instructions: Optional[str]
    RefId: Optional[str]
    NotApplicableEnabled: Optional[bool]
    QuestionType: Optional[str]
    QuestionTypeProperties: Optional["_EvaluationFormQuestionTypeProperties"]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_EvaluationFormQuestion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EvaluationFormQuestion"]:
        if not json_data:
            return None
        return cls(
            Title=json_data.get("Title"),
            Instructions=json_data.get("Instructions"),
            RefId=json_data.get("RefId"),
            NotApplicableEnabled=json_data.get("NotApplicableEnabled"),
            QuestionType=json_data.get("QuestionType"),
            QuestionTypeProperties=EvaluationFormQuestionTypeProperties._deserialize(json_data.get("QuestionTypeProperties")),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EvaluationFormQuestion = EvaluationFormQuestion


@dataclass
class EvaluationFormQuestionTypeProperties(BaseModel):
    Numeric: Optional["_EvaluationFormNumericQuestionProperties"]
    SingleSelect: Optional["_EvaluationFormSingleSelectQuestionProperties"]

    @classmethod
    def _deserialize(
        cls: Type["_EvaluationFormQuestionTypeProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EvaluationFormQuestionTypeProperties"]:
        if not json_data:
            return None
        return cls(
            Numeric=EvaluationFormNumericQuestionProperties._deserialize(json_data.get("Numeric")),
            SingleSelect=EvaluationFormSingleSelectQuestionProperties._deserialize(json_data.get("SingleSelect")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EvaluationFormQuestionTypeProperties = EvaluationFormQuestionTypeProperties


@dataclass
class EvaluationFormNumericQuestionProperties(BaseModel):
    MinValue: Optional[int]
    MaxValue: Optional[int]
    Options: Optional[Sequence["_EvaluationFormNumericQuestionOption"]]
    Automation: Optional["_EvaluationFormNumericQuestionAutomation"]

    @classmethod
    def _deserialize(
        cls: Type["_EvaluationFormNumericQuestionProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EvaluationFormNumericQuestionProperties"]:
        if not json_data:
            return None
        return cls(
            MinValue=json_data.get("MinValue"),
            MaxValue=json_data.get("MaxValue"),
            Options=deserialize_list(json_data.get("Options"), EvaluationFormNumericQuestionOption),
            Automation=EvaluationFormNumericQuestionAutomation._deserialize(json_data.get("Automation")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EvaluationFormNumericQuestionProperties = EvaluationFormNumericQuestionProperties


@dataclass
class EvaluationFormNumericQuestionOption(BaseModel):
    MinValue: Optional[int]
    MaxValue: Optional[int]
    Score: Optional[int]
    AutomaticFail: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EvaluationFormNumericQuestionOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EvaluationFormNumericQuestionOption"]:
        if not json_data:
            return None
        return cls(
            MinValue=json_data.get("MinValue"),
            MaxValue=json_data.get("MaxValue"),
            Score=json_data.get("Score"),
            AutomaticFail=json_data.get("AutomaticFail"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EvaluationFormNumericQuestionOption = EvaluationFormNumericQuestionOption


@dataclass
class EvaluationFormNumericQuestionAutomation(BaseModel):
    PropertyValue: Optional["_NumericQuestionPropertyValueAutomation"]

    @classmethod
    def _deserialize(
        cls: Type["_EvaluationFormNumericQuestionAutomation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EvaluationFormNumericQuestionAutomation"]:
        if not json_data:
            return None
        return cls(
            PropertyValue=NumericQuestionPropertyValueAutomation._deserialize(json_data.get("PropertyValue")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EvaluationFormNumericQuestionAutomation = EvaluationFormNumericQuestionAutomation


@dataclass
class NumericQuestionPropertyValueAutomation(BaseModel):
    Label: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NumericQuestionPropertyValueAutomation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumericQuestionPropertyValueAutomation"]:
        if not json_data:
            return None
        return cls(
            Label=json_data.get("Label"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumericQuestionPropertyValueAutomation = NumericQuestionPropertyValueAutomation


@dataclass
class EvaluationFormSingleSelectQuestionProperties(BaseModel):
    Options: Optional[Sequence["_EvaluationFormSingleSelectQuestionOption"]]
    DisplayAs: Optional[str]
    Automation: Optional["_EvaluationFormSingleSelectQuestionAutomation"]

    @classmethod
    def _deserialize(
        cls: Type["_EvaluationFormSingleSelectQuestionProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EvaluationFormSingleSelectQuestionProperties"]:
        if not json_data:
            return None
        return cls(
            Options=deserialize_list(json_data.get("Options"), EvaluationFormSingleSelectQuestionOption),
            DisplayAs=json_data.get("DisplayAs"),
            Automation=EvaluationFormSingleSelectQuestionAutomation._deserialize(json_data.get("Automation")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EvaluationFormSingleSelectQuestionProperties = EvaluationFormSingleSelectQuestionProperties


@dataclass
class EvaluationFormSingleSelectQuestionOption(BaseModel):
    RefId: Optional[str]
    Text: Optional[str]
    Score: Optional[int]
    AutomaticFail: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EvaluationFormSingleSelectQuestionOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EvaluationFormSingleSelectQuestionOption"]:
        if not json_data:
            return None
        return cls(
            RefId=json_data.get("RefId"),
            Text=json_data.get("Text"),
            Score=json_data.get("Score"),
            AutomaticFail=json_data.get("AutomaticFail"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EvaluationFormSingleSelectQuestionOption = EvaluationFormSingleSelectQuestionOption


@dataclass
class EvaluationFormSingleSelectQuestionAutomation(BaseModel):
    Options: Optional[Sequence["_EvaluationFormSingleSelectQuestionAutomationOption"]]
    DefaultOptionRefId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EvaluationFormSingleSelectQuestionAutomation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EvaluationFormSingleSelectQuestionAutomation"]:
        if not json_data:
            return None
        return cls(
            Options=deserialize_list(json_data.get("Options"), EvaluationFormSingleSelectQuestionAutomationOption),
            DefaultOptionRefId=json_data.get("DefaultOptionRefId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EvaluationFormSingleSelectQuestionAutomation = EvaluationFormSingleSelectQuestionAutomation


@dataclass
class EvaluationFormSingleSelectQuestionAutomationOption(BaseModel):
    RuleCategory: Optional["_SingleSelectQuestionRuleCategoryAutomation"]

    @classmethod
    def _deserialize(
        cls: Type["_EvaluationFormSingleSelectQuestionAutomationOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EvaluationFormSingleSelectQuestionAutomationOption"]:
        if not json_data:
            return None
        return cls(
            RuleCategory=SingleSelectQuestionRuleCategoryAutomation._deserialize(json_data.get("RuleCategory")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EvaluationFormSingleSelectQuestionAutomationOption = EvaluationFormSingleSelectQuestionAutomationOption


@dataclass
class SingleSelectQuestionRuleCategoryAutomation(BaseModel):
    Category: Optional[str]
    Condition: Optional[str]
    OptionRefId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SingleSelectQuestionRuleCategoryAutomation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SingleSelectQuestionRuleCategoryAutomation"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            Condition=json_data.get("Condition"),
            OptionRefId=json_data.get("OptionRefId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SingleSelectQuestionRuleCategoryAutomation = SingleSelectQuestionRuleCategoryAutomation


@dataclass
class ScoringStrategy(BaseModel):
    Mode: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScoringStrategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScoringStrategy"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScoringStrategy = ScoringStrategy


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


