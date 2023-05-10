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
class AwsSsmPatchbaseline(BaseModel):
    OperatingSystem: Optional[str]
    Description: Optional[str]
    ApprovalRules: Optional["_RuleGroup"]
    Sources: Optional[Sequence["_PatchSource"]]
    Name: Optional[str]
    RejectedPatches: Optional[Sequence[str]]
    ApprovedPatches: Optional[Sequence[str]]
    RejectedPatchesAction: Optional[str]
    PatchGroups: Optional[Sequence[str]]
    ApprovedPatchesComplianceLevel: Optional[str]
    ApprovedPatchesEnableNonSecurity: Optional[bool]
    Id: Optional[str]
    GlobalFilters: Optional["_PatchFilterGroup"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSsmPatchbaseline"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSsmPatchbaseline"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            OperatingSystem=json_data.get("OperatingSystem"),
            Description=json_data.get("Description"),
            ApprovalRules=RuleGroup._deserialize(json_data.get("ApprovalRules")),
            Sources=deserialize_list(json_data.get("Sources"), PatchSource),
            Name=json_data.get("Name"),
            RejectedPatches=json_data.get("RejectedPatches"),
            ApprovedPatches=json_data.get("ApprovedPatches"),
            RejectedPatchesAction=json_data.get("RejectedPatchesAction"),
            PatchGroups=json_data.get("PatchGroups"),
            ApprovedPatchesComplianceLevel=json_data.get("ApprovedPatchesComplianceLevel"),
            ApprovedPatchesEnableNonSecurity=json_data.get("ApprovedPatchesEnableNonSecurity"),
            Id=json_data.get("Id"),
            GlobalFilters=PatchFilterGroup._deserialize(json_data.get("GlobalFilters")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSsmPatchbaseline = AwsSsmPatchbaseline


@dataclass
class RuleGroup(BaseModel):
    PatchRules: Optional[Sequence["_Rule"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleGroup"]:
        if not json_data:
            return None
        return cls(
            PatchRules=deserialize_list(json_data.get("PatchRules"), Rule),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleGroup = RuleGroup


@dataclass
class Rule(BaseModel):
    ApproveUntilDate: Optional[MutableMapping[str, Any]]
    ApproveAfterDays: Optional[int]
    EnableNonSecurity: Optional[bool]
    ComplianceLevel: Optional[str]
    PatchFilterGroup: Optional["_PatchFilterGroup"]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            ApproveUntilDate=json_data.get("ApproveUntilDate"),
            ApproveAfterDays=json_data.get("ApproveAfterDays"),
            EnableNonSecurity=json_data.get("EnableNonSecurity"),
            ComplianceLevel=json_data.get("ComplianceLevel"),
            PatchFilterGroup=PatchFilterGroup._deserialize(json_data.get("PatchFilterGroup")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class PatchFilterGroup(BaseModel):
    PatchFilters: Optional[Sequence["_PatchFilter"]]

    @classmethod
    def _deserialize(
        cls: Type["_PatchFilterGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PatchFilterGroup"]:
        if not json_data:
            return None
        return cls(
            PatchFilters=deserialize_list(json_data.get("PatchFilters"), PatchFilter),
        )


# work around possible type aliasing issues when variable has same name as a model
_PatchFilterGroup = PatchFilterGroup


@dataclass
class PatchFilter(BaseModel):
    Values: Optional[Sequence[str]]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PatchFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PatchFilter"]:
        if not json_data:
            return None
        return cls(
            Values=json_data.get("Values"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PatchFilter = PatchFilter


@dataclass
class PatchSource(BaseModel):
    Products: Optional[Sequence[str]]
    Configuration: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PatchSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PatchSource"]:
        if not json_data:
            return None
        return cls(
            Products=json_data.get("Products"),
            Configuration=json_data.get("Configuration"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PatchSource = PatchSource


@dataclass
class Tag(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


