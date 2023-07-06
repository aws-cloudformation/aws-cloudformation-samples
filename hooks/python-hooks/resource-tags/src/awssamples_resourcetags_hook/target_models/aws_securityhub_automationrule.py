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
class AwsSecurityhubAutomationrule(BaseModel):
    RuleArn: Optional[str]
    RuleStatus: Optional[str]
    RuleOrder: Optional[int]
    Description: Optional[str]
    RuleName: Optional[str]
    CreatedAt: Optional[str]
    UpdatedAt: Optional[str]
    CreatedBy: Optional[str]
    IsTerminal: Optional[bool]
    Actions: Optional[Sequence["_AutomationRulesAction"]]
    Criteria: Optional["_AutomationRulesFindingFilters"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSecurityhubAutomationrule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSecurityhubAutomationrule"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            RuleArn=json_data.get("RuleArn"),
            RuleStatus=json_data.get("RuleStatus"),
            RuleOrder=json_data.get("RuleOrder"),
            Description=json_data.get("Description"),
            RuleName=json_data.get("RuleName"),
            CreatedAt=json_data.get("CreatedAt"),
            UpdatedAt=json_data.get("UpdatedAt"),
            CreatedBy=json_data.get("CreatedBy"),
            IsTerminal=json_data.get("IsTerminal"),
            Actions=deserialize_list(json_data.get("Actions"), AutomationRulesAction),
            Criteria=AutomationRulesFindingFilters._deserialize(json_data.get("Criteria")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSecurityhubAutomationrule = AwsSecurityhubAutomationrule


@dataclass
class AutomationRulesAction(BaseModel):
    Type: Optional[str]
    FindingFieldsUpdate: Optional["_AutomationRulesFindingFieldsUpdate"]

    @classmethod
    def _deserialize(
        cls: Type["_AutomationRulesAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutomationRulesAction"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            FindingFieldsUpdate=AutomationRulesFindingFieldsUpdate._deserialize(json_data.get("FindingFieldsUpdate")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutomationRulesAction = AutomationRulesAction


@dataclass
class AutomationRulesFindingFieldsUpdate(BaseModel):
    Types: Optional[Sequence[str]]
    Severity: Optional["_SeverityUpdate"]
    Confidence: Optional[int]
    Criticality: Optional[int]
    UserDefinedFields: Optional[MutableMapping[str, str]]
    VerificationState: Optional[str]
    RelatedFindings: Optional[Sequence["_RelatedFinding"]]
    Note: Optional["_NoteUpdate"]
    Workflow: Optional["_WorkflowUpdate"]

    @classmethod
    def _deserialize(
        cls: Type["_AutomationRulesFindingFieldsUpdate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutomationRulesFindingFieldsUpdate"]:
        if not json_data:
            return None
        return cls(
            Types=json_data.get("Types"),
            Severity=SeverityUpdate._deserialize(json_data.get("Severity")),
            Confidence=json_data.get("Confidence"),
            Criticality=json_data.get("Criticality"),
            UserDefinedFields=json_data.get("UserDefinedFields"),
            VerificationState=json_data.get("VerificationState"),
            RelatedFindings=deserialize_list(json_data.get("RelatedFindings"), RelatedFinding),
            Note=NoteUpdate._deserialize(json_data.get("Note")),
            Workflow=WorkflowUpdate._deserialize(json_data.get("Workflow")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutomationRulesFindingFieldsUpdate = AutomationRulesFindingFieldsUpdate


@dataclass
class SeverityUpdate(BaseModel):
    Product: Optional[float]
    Label: Optional[str]
    Normalized: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_SeverityUpdate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SeverityUpdate"]:
        if not json_data:
            return None
        return cls(
            Product=json_data.get("Product"),
            Label=json_data.get("Label"),
            Normalized=json_data.get("Normalized"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SeverityUpdate = SeverityUpdate


@dataclass
class RelatedFinding(BaseModel):
    ProductArn: Optional[str]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RelatedFinding"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RelatedFinding"]:
        if not json_data:
            return None
        return cls(
            ProductArn=json_data.get("ProductArn"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RelatedFinding = RelatedFinding


@dataclass
class NoteUpdate(BaseModel):
    Text: Optional[str]
    UpdatedBy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NoteUpdate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NoteUpdate"]:
        if not json_data:
            return None
        return cls(
            Text=json_data.get("Text"),
            UpdatedBy=json_data.get("UpdatedBy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NoteUpdate = NoteUpdate


@dataclass
class WorkflowUpdate(BaseModel):
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkflowUpdate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkflowUpdate"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkflowUpdate = WorkflowUpdate


@dataclass
class AutomationRulesFindingFilters(BaseModel):
    ProductArn: Optional[Sequence["_StringFilter"]]
    AwsAccountId: Optional[Sequence["_StringFilter"]]
    Id: Optional[Sequence["_StringFilter"]]
    GeneratorId: Optional[Sequence["_StringFilter"]]
    Type: Optional[Sequence["_StringFilter"]]
    FirstObservedAt: Optional[Sequence["_DateFilter"]]
    LastObservedAt: Optional[Sequence["_DateFilter"]]
    CreatedAt: Optional[Sequence["_DateFilter"]]
    UpdatedAt: Optional[Sequence["_DateFilter"]]
    Confidence: Optional[Sequence["_NumberFilter"]]
    Criticality: Optional[Sequence["_NumberFilter"]]
    Title: Optional[Sequence["_StringFilter"]]
    Description: Optional[Sequence["_StringFilter"]]
    SourceUrl: Optional[Sequence["_StringFilter"]]
    ProductName: Optional[Sequence["_StringFilter"]]
    CompanyName: Optional[Sequence["_StringFilter"]]
    SeverityLabel: Optional[Sequence["_StringFilter"]]
    ResourceType: Optional[Sequence["_StringFilter"]]
    ResourceId: Optional[Sequence["_StringFilter"]]
    ResourcePartition: Optional[Sequence["_StringFilter"]]
    ResourceRegion: Optional[Sequence["_StringFilter"]]
    ResourceTags: Optional[Sequence["_MapFilter"]]
    ResourceDetailsOther: Optional[Sequence["_MapFilter"]]
    ComplianceStatus: Optional[Sequence["_StringFilter"]]
    ComplianceSecurityControlId: Optional[Sequence["_StringFilter"]]
    ComplianceAssociatedStandardsId: Optional[Sequence["_StringFilter"]]
    VerificationState: Optional[Sequence["_StringFilter"]]
    WorkflowStatus: Optional[Sequence["_StringFilter"]]
    RecordState: Optional[Sequence["_StringFilter"]]
    RelatedFindingsProductArn: Optional[Sequence["_StringFilter"]]
    RelatedFindingsId: Optional[Sequence["_StringFilter"]]
    NoteText: Optional[Sequence["_StringFilter"]]
    NoteUpdatedAt: Optional[Sequence["_DateFilter"]]
    NoteUpdatedBy: Optional[Sequence["_StringFilter"]]
    UserDefinedFields: Optional[Sequence["_MapFilter"]]

    @classmethod
    def _deserialize(
        cls: Type["_AutomationRulesFindingFilters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutomationRulesFindingFilters"]:
        if not json_data:
            return None
        return cls(
            ProductArn=deserialize_list(json_data.get("ProductArn"), StringFilter),
            AwsAccountId=deserialize_list(json_data.get("AwsAccountId"), StringFilter),
            Id=deserialize_list(json_data.get("Id"), StringFilter),
            GeneratorId=deserialize_list(json_data.get("GeneratorId"), StringFilter),
            Type=deserialize_list(json_data.get("Type"), StringFilter),
            FirstObservedAt=deserialize_list(json_data.get("FirstObservedAt"), DateFilter),
            LastObservedAt=deserialize_list(json_data.get("LastObservedAt"), DateFilter),
            CreatedAt=deserialize_list(json_data.get("CreatedAt"), DateFilter),
            UpdatedAt=deserialize_list(json_data.get("UpdatedAt"), DateFilter),
            Confidence=deserialize_list(json_data.get("Confidence"), NumberFilter),
            Criticality=deserialize_list(json_data.get("Criticality"), NumberFilter),
            Title=deserialize_list(json_data.get("Title"), StringFilter),
            Description=deserialize_list(json_data.get("Description"), StringFilter),
            SourceUrl=deserialize_list(json_data.get("SourceUrl"), StringFilter),
            ProductName=deserialize_list(json_data.get("ProductName"), StringFilter),
            CompanyName=deserialize_list(json_data.get("CompanyName"), StringFilter),
            SeverityLabel=deserialize_list(json_data.get("SeverityLabel"), StringFilter),
            ResourceType=deserialize_list(json_data.get("ResourceType"), StringFilter),
            ResourceId=deserialize_list(json_data.get("ResourceId"), StringFilter),
            ResourcePartition=deserialize_list(json_data.get("ResourcePartition"), StringFilter),
            ResourceRegion=deserialize_list(json_data.get("ResourceRegion"), StringFilter),
            ResourceTags=deserialize_list(json_data.get("ResourceTags"), MapFilter),
            ResourceDetailsOther=deserialize_list(json_data.get("ResourceDetailsOther"), MapFilter),
            ComplianceStatus=deserialize_list(json_data.get("ComplianceStatus"), StringFilter),
            ComplianceSecurityControlId=deserialize_list(json_data.get("ComplianceSecurityControlId"), StringFilter),
            ComplianceAssociatedStandardsId=deserialize_list(json_data.get("ComplianceAssociatedStandardsId"), StringFilter),
            VerificationState=deserialize_list(json_data.get("VerificationState"), StringFilter),
            WorkflowStatus=deserialize_list(json_data.get("WorkflowStatus"), StringFilter),
            RecordState=deserialize_list(json_data.get("RecordState"), StringFilter),
            RelatedFindingsProductArn=deserialize_list(json_data.get("RelatedFindingsProductArn"), StringFilter),
            RelatedFindingsId=deserialize_list(json_data.get("RelatedFindingsId"), StringFilter),
            NoteText=deserialize_list(json_data.get("NoteText"), StringFilter),
            NoteUpdatedAt=deserialize_list(json_data.get("NoteUpdatedAt"), DateFilter),
            NoteUpdatedBy=deserialize_list(json_data.get("NoteUpdatedBy"), StringFilter),
            UserDefinedFields=deserialize_list(json_data.get("UserDefinedFields"), MapFilter),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutomationRulesFindingFilters = AutomationRulesFindingFilters


@dataclass
class StringFilter(BaseModel):
    Comparison: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StringFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StringFilter"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StringFilter = StringFilter


@dataclass
class DateFilter(BaseModel):
    DateRange: Optional["_DateRange"]
    End: Optional[str]
    Start: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DateFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DateFilter"]:
        if not json_data:
            return None
        return cls(
            DateRange=DateRange._deserialize(json_data.get("DateRange")),
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DateFilter = DateFilter


@dataclass
class DateRange(BaseModel):
    Unit: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DateRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DateRange"]:
        if not json_data:
            return None
        return cls(
            Unit=json_data.get("Unit"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DateRange = DateRange


@dataclass
class NumberFilter(BaseModel):
    Eq: Optional[float]
    Gte: Optional[float]
    Lte: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NumberFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NumberFilter"]:
        if not json_data:
            return None
        return cls(
            Eq=json_data.get("Eq"),
            Gte=json_data.get("Gte"),
            Lte=json_data.get("Lte"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NumberFilter = NumberFilter


@dataclass
class MapFilter(BaseModel):
    Comparison: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MapFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MapFilter"]:
        if not json_data:
            return None
        return cls(
            Comparison=json_data.get("Comparison"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MapFilter = MapFilter


