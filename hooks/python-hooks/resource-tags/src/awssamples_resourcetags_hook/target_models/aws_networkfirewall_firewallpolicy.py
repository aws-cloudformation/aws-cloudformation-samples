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
class AwsNetworkfirewallFirewallpolicy(BaseModel):
    FirewallPolicyName: Optional[str]
    FirewallPolicyArn: Optional[str]
    FirewallPolicy: Optional["_FirewallPolicy"]
    FirewallPolicyId: Optional[str]
    Description: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsNetworkfirewallFirewallpolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsNetworkfirewallFirewallpolicy"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            FirewallPolicyName=json_data.get("FirewallPolicyName"),
            FirewallPolicyArn=json_data.get("FirewallPolicyArn"),
            FirewallPolicy=FirewallPolicy._deserialize(json_data.get("FirewallPolicy")),
            FirewallPolicyId=json_data.get("FirewallPolicyId"),
            Description=json_data.get("Description"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsNetworkfirewallFirewallpolicy = AwsNetworkfirewallFirewallpolicy


@dataclass
class FirewallPolicy(BaseModel):
    StatelessDefaultActions: Optional[Sequence[str]]
    StatelessFragmentDefaultActions: Optional[Sequence[str]]
    StatelessCustomActions: Optional[Sequence["_CustomAction"]]
    StatelessRuleGroupReferences: Optional[Sequence["_StatelessRuleGroupReference"]]
    StatefulRuleGroupReferences: Optional[Sequence["_StatefulRuleGroupReference"]]
    StatefulDefaultActions: Optional[Sequence[str]]
    StatefulEngineOptions: Optional["_StatefulEngineOptions"]
    PolicyVariables: Optional["_PolicyVariables"]

    @classmethod
    def _deserialize(
        cls: Type["_FirewallPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FirewallPolicy"]:
        if not json_data:
            return None
        return cls(
            StatelessDefaultActions=json_data.get("StatelessDefaultActions"),
            StatelessFragmentDefaultActions=json_data.get("StatelessFragmentDefaultActions"),
            StatelessCustomActions=deserialize_list(json_data.get("StatelessCustomActions"), CustomAction),
            StatelessRuleGroupReferences=deserialize_list(json_data.get("StatelessRuleGroupReferences"), StatelessRuleGroupReference),
            StatefulRuleGroupReferences=deserialize_list(json_data.get("StatefulRuleGroupReferences"), StatefulRuleGroupReference),
            StatefulDefaultActions=json_data.get("StatefulDefaultActions"),
            StatefulEngineOptions=StatefulEngineOptions._deserialize(json_data.get("StatefulEngineOptions")),
            PolicyVariables=PolicyVariables._deserialize(json_data.get("PolicyVariables")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FirewallPolicy = FirewallPolicy


@dataclass
class CustomAction(BaseModel):
    ActionName: Optional[str]
    ActionDefinition: Optional["_ActionDefinition"]

    @classmethod
    def _deserialize(
        cls: Type["_CustomAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomAction"]:
        if not json_data:
            return None
        return cls(
            ActionName=json_data.get("ActionName"),
            ActionDefinition=ActionDefinition._deserialize(json_data.get("ActionDefinition")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomAction = CustomAction


@dataclass
class ActionDefinition(BaseModel):
    PublishMetricAction: Optional["_PublishMetricAction"]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            PublishMetricAction=PublishMetricAction._deserialize(json_data.get("PublishMetricAction")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class PublishMetricAction(BaseModel):
    Dimensions: Optional[Sequence["_Dimension"]]

    @classmethod
    def _deserialize(
        cls: Type["_PublishMetricAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublishMetricAction"]:
        if not json_data:
            return None
        return cls(
            Dimensions=deserialize_list(json_data.get("Dimensions"), Dimension),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublishMetricAction = PublishMetricAction


@dataclass
class Dimension(BaseModel):
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dimension"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dimension"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dimension = Dimension


@dataclass
class StatelessRuleGroupReference(BaseModel):
    ResourceArn: Optional[str]
    Priority: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_StatelessRuleGroupReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatelessRuleGroupReference"]:
        if not json_data:
            return None
        return cls(
            ResourceArn=json_data.get("ResourceArn"),
            Priority=json_data.get("Priority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatelessRuleGroupReference = StatelessRuleGroupReference


@dataclass
class StatefulRuleGroupReference(BaseModel):
    ResourceArn: Optional[str]
    Priority: Optional[int]
    Override: Optional["_StatefulRuleGroupOverride"]

    @classmethod
    def _deserialize(
        cls: Type["_StatefulRuleGroupReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatefulRuleGroupReference"]:
        if not json_data:
            return None
        return cls(
            ResourceArn=json_data.get("ResourceArn"),
            Priority=json_data.get("Priority"),
            Override=StatefulRuleGroupOverride._deserialize(json_data.get("Override")),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatefulRuleGroupReference = StatefulRuleGroupReference


@dataclass
class StatefulRuleGroupOverride(BaseModel):
    Action: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatefulRuleGroupOverride"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatefulRuleGroupOverride"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatefulRuleGroupOverride = StatefulRuleGroupOverride


@dataclass
class StatefulEngineOptions(BaseModel):
    RuleOrder: Optional[str]
    StreamExceptionPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatefulEngineOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatefulEngineOptions"]:
        if not json_data:
            return None
        return cls(
            RuleOrder=json_data.get("RuleOrder"),
            StreamExceptionPolicy=json_data.get("StreamExceptionPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatefulEngineOptions = StatefulEngineOptions


@dataclass
class PolicyVariables(BaseModel):
    RuleVariables: Optional[MutableMapping[str, "_IPSet"]]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyVariables"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyVariables"]:
        if not json_data:
            return None
        return cls(
            RuleVariables=json_data.get("RuleVariables"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyVariables = PolicyVariables


@dataclass
class IPSet(BaseModel):
    Definition: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IPSet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IPSet"]:
        if not json_data:
            return None
        return cls(
            Definition=json_data.get("Definition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IPSet = IPSet


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


