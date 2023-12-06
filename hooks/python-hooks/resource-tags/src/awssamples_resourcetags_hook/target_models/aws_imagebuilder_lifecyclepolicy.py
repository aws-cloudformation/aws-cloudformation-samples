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
class AwsImagebuilderLifecyclepolicy(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    Description: Optional[str]
    Status: Optional[str]
    ExecutionRole: Optional[str]
    ResourceType: Optional[str]
    PolicyDetails: Optional[Sequence["_PolicyDetail"]]
    ResourceSelection: Optional["_ResourceSelection"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsImagebuilderLifecyclepolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsImagebuilderLifecyclepolicy"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            Status=json_data.get("Status"),
            ExecutionRole=json_data.get("ExecutionRole"),
            ResourceType=json_data.get("ResourceType"),
            PolicyDetails=deserialize_list(json_data.get("PolicyDetails"), PolicyDetail),
            ResourceSelection=ResourceSelection._deserialize(json_data.get("ResourceSelection")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsImagebuilderLifecyclepolicy = AwsImagebuilderLifecyclepolicy


@dataclass
class PolicyDetail(BaseModel):
    Action: Optional["_Action"]
    Filter: Optional["_Filter"]
    ExclusionRules: Optional["_ExclusionRules"]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyDetail"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyDetail"]:
        if not json_data:
            return None
        return cls(
            Action=Action._deserialize(json_data.get("Action")),
            Filter=Filter._deserialize(json_data.get("Filter")),
            ExclusionRules=ExclusionRules._deserialize(json_data.get("ExclusionRules")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyDetail = PolicyDetail


@dataclass
class Action(BaseModel):
    Type: Optional[str]
    IncludeResources: Optional["_IncludeResources"]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            IncludeResources=IncludeResources._deserialize(json_data.get("IncludeResources")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class IncludeResources(BaseModel):
    Amis: Optional[bool]
    Containers: Optional[bool]
    Snapshots: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_IncludeResources"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IncludeResources"]:
        if not json_data:
            return None
        return cls(
            Amis=json_data.get("Amis"),
            Containers=json_data.get("Containers"),
            Snapshots=json_data.get("Snapshots"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IncludeResources = IncludeResources


@dataclass
class Filter(BaseModel):
    Type: Optional[str]
    Value: Optional[int]
    Unit: Optional[str]
    RetainAtLeast: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Filter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filter"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
            Unit=json_data.get("Unit"),
            RetainAtLeast=json_data.get("RetainAtLeast"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Filter = Filter


@dataclass
class ExclusionRules(BaseModel):
    TagMap: Optional[MutableMapping[str, str]]
    Amis: Optional["_AmiExclusionRules"]

    @classmethod
    def _deserialize(
        cls: Type["_ExclusionRules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExclusionRules"]:
        if not json_data:
            return None
        return cls(
            TagMap=json_data.get("TagMap"),
            Amis=AmiExclusionRules._deserialize(json_data.get("Amis")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExclusionRules = ExclusionRules


@dataclass
class AmiExclusionRules(BaseModel):
    IsPublic: Optional[bool]
    Regions: Optional[Sequence[str]]
    SharedAccounts: Optional[Sequence[str]]
    LastLaunched: Optional["_LastLaunched"]
    TagMap: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_AmiExclusionRules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AmiExclusionRules"]:
        if not json_data:
            return None
        return cls(
            IsPublic=json_data.get("IsPublic"),
            Regions=json_data.get("Regions"),
            SharedAccounts=json_data.get("SharedAccounts"),
            LastLaunched=LastLaunched._deserialize(json_data.get("LastLaunched")),
            TagMap=json_data.get("TagMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AmiExclusionRules = AmiExclusionRules


@dataclass
class LastLaunched(BaseModel):
    Value: Optional[int]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LastLaunched"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LastLaunched"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LastLaunched = LastLaunched


@dataclass
class ResourceSelection(BaseModel):
    Recipes: Optional[Sequence["_RecipeSelection"]]
    TagMap: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceSelection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceSelection"]:
        if not json_data:
            return None
        return cls(
            Recipes=deserialize_list(json_data.get("Recipes"), RecipeSelection),
            TagMap=json_data.get("TagMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceSelection = ResourceSelection


@dataclass
class RecipeSelection(BaseModel):
    Name: Optional[str]
    SemanticVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecipeSelection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecipeSelection"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            SemanticVersion=json_data.get("SemanticVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecipeSelection = RecipeSelection


