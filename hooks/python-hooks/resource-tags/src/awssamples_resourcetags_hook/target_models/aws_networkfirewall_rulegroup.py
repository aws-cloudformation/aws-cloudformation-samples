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
class AwsNetworkfirewallRulegroup(BaseModel):
    RuleGroupName: Optional[str]
    RuleGroupArn: Optional[str]
    RuleGroupId: Optional[str]
    RuleGroup: Optional["_RuleGroup"]
    Type: Optional[str]
    Capacity: Optional[int]
    Description: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsNetworkfirewallRulegroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsNetworkfirewallRulegroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            RuleGroupName=json_data.get("RuleGroupName"),
            RuleGroupArn=json_data.get("RuleGroupArn"),
            RuleGroupId=json_data.get("RuleGroupId"),
            RuleGroup=RuleGroup._deserialize(json_data.get("RuleGroup")),
            Type=json_data.get("Type"),
            Capacity=json_data.get("Capacity"),
            Description=json_data.get("Description"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsNetworkfirewallRulegroup = AwsNetworkfirewallRulegroup


@dataclass
class RuleGroup(BaseModel):
    RuleVariables: Optional["_RuleVariables"]
    ReferenceSets: Optional["_ReferenceSets"]
    RulesSource: Optional["_RulesSource"]
    StatefulRuleOptions: Optional["_StatefulRuleOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_RuleGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleGroup"]:
        if not json_data:
            return None
        return cls(
            RuleVariables=RuleVariables._deserialize(json_data.get("RuleVariables")),
            ReferenceSets=ReferenceSets._deserialize(json_data.get("ReferenceSets")),
            RulesSource=RulesSource._deserialize(json_data.get("RulesSource")),
            StatefulRuleOptions=StatefulRuleOptions._deserialize(json_data.get("StatefulRuleOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleGroup = RuleGroup


@dataclass
class RuleVariables(BaseModel):
    IPSets: Optional[MutableMapping[str, "_IPSet"]]
    PortSets: Optional[MutableMapping[str, "_PortSet"]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleVariables"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleVariables"]:
        if not json_data:
            return None
        return cls(
            IPSets=json_data.get("IPSets"),
            PortSets=json_data.get("PortSets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleVariables = RuleVariables


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
class PortSet(BaseModel):
    Definition: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PortSet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortSet"]:
        if not json_data:
            return None
        return cls(
            Definition=json_data.get("Definition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortSet = PortSet


@dataclass
class ReferenceSets(BaseModel):
    IPSetReferences: Optional[MutableMapping[str, "_IPSetReference"]]

    @classmethod
    def _deserialize(
        cls: Type["_ReferenceSets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReferenceSets"]:
        if not json_data:
            return None
        return cls(
            IPSetReferences=json_data.get("IPSetReferences"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReferenceSets = ReferenceSets


@dataclass
class IPSetReference(BaseModel):
    ReferenceArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IPSetReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IPSetReference"]:
        if not json_data:
            return None
        return cls(
            ReferenceArn=json_data.get("ReferenceArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IPSetReference = IPSetReference


@dataclass
class RulesSource(BaseModel):
    RulesString: Optional[str]
    RulesSourceList: Optional["_RulesSourceList"]
    StatefulRules: Optional[Sequence["_StatefulRule"]]
    StatelessRulesAndCustomActions: Optional["_StatelessRulesAndCustomActions"]

    @classmethod
    def _deserialize(
        cls: Type["_RulesSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesSource"]:
        if not json_data:
            return None
        return cls(
            RulesString=json_data.get("RulesString"),
            RulesSourceList=RulesSourceList._deserialize(json_data.get("RulesSourceList")),
            StatefulRules=deserialize_list(json_data.get("StatefulRules"), StatefulRule),
            StatelessRulesAndCustomActions=StatelessRulesAndCustomActions._deserialize(json_data.get("StatelessRulesAndCustomActions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesSource = RulesSource


@dataclass
class RulesSourceList(BaseModel):
    Targets: Optional[Sequence[str]]
    TargetTypes: Optional[Sequence[str]]
    GeneratedRulesType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RulesSourceList"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesSourceList"]:
        if not json_data:
            return None
        return cls(
            Targets=json_data.get("Targets"),
            TargetTypes=json_data.get("TargetTypes"),
            GeneratedRulesType=json_data.get("GeneratedRulesType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesSourceList = RulesSourceList


@dataclass
class StatefulRule(BaseModel):
    Action: Optional[str]
    Header: Optional["_Header"]
    RuleOptions: Optional[Sequence["_RuleOption"]]

    @classmethod
    def _deserialize(
        cls: Type["_StatefulRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatefulRule"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Header=Header._deserialize(json_data.get("Header")),
            RuleOptions=deserialize_list(json_data.get("RuleOptions"), RuleOption),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatefulRule = StatefulRule


@dataclass
class Header(BaseModel):
    Protocol: Optional[str]
    Source: Optional[str]
    SourcePort: Optional[str]
    Direction: Optional[str]
    Destination: Optional[str]
    DestinationPort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Header"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Header"]:
        if not json_data:
            return None
        return cls(
            Protocol=json_data.get("Protocol"),
            Source=json_data.get("Source"),
            SourcePort=json_data.get("SourcePort"),
            Direction=json_data.get("Direction"),
            Destination=json_data.get("Destination"),
            DestinationPort=json_data.get("DestinationPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Header = Header


@dataclass
class RuleOption(BaseModel):
    Keyword: Optional[str]
    Settings: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleOption"]:
        if not json_data:
            return None
        return cls(
            Keyword=json_data.get("Keyword"),
            Settings=json_data.get("Settings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleOption = RuleOption


@dataclass
class StatelessRulesAndCustomActions(BaseModel):
    StatelessRules: Optional[Sequence["_StatelessRule"]]
    CustomActions: Optional[Sequence["_CustomAction"]]

    @classmethod
    def _deserialize(
        cls: Type["_StatelessRulesAndCustomActions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatelessRulesAndCustomActions"]:
        if not json_data:
            return None
        return cls(
            StatelessRules=deserialize_list(json_data.get("StatelessRules"), StatelessRule),
            CustomActions=deserialize_list(json_data.get("CustomActions"), CustomAction),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatelessRulesAndCustomActions = StatelessRulesAndCustomActions


@dataclass
class StatelessRule(BaseModel):
    RuleDefinition: Optional["_RuleDefinition"]
    Priority: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_StatelessRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatelessRule"]:
        if not json_data:
            return None
        return cls(
            RuleDefinition=RuleDefinition._deserialize(json_data.get("RuleDefinition")),
            Priority=json_data.get("Priority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatelessRule = StatelessRule


@dataclass
class RuleDefinition(BaseModel):
    MatchAttributes: Optional["_MatchAttributes"]
    Actions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchAttributes=MatchAttributes._deserialize(json_data.get("MatchAttributes")),
            Actions=json_data.get("Actions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


@dataclass
class MatchAttributes(BaseModel):
    Sources: Optional[Sequence["_Address"]]
    Destinations: Optional[Sequence["_Address"]]
    SourcePorts: Optional[Sequence["_PortRange"]]
    DestinationPorts: Optional[Sequence["_PortRange"]]
    Protocols: Optional[Sequence[int]]
    TCPFlags: Optional[Sequence["_TCPFlagField"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchAttributes"]:
        if not json_data:
            return None
        return cls(
            Sources=deserialize_list(json_data.get("Sources"), Address),
            Destinations=deserialize_list(json_data.get("Destinations"), Address),
            SourcePorts=deserialize_list(json_data.get("SourcePorts"), PortRange),
            DestinationPorts=deserialize_list(json_data.get("DestinationPorts"), PortRange),
            Protocols=json_data.get("Protocols"),
            TCPFlags=deserialize_list(json_data.get("TCPFlags"), TCPFlagField),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchAttributes = MatchAttributes


@dataclass
class Address(BaseModel):
    AddressDefinition: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Address"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Address"]:
        if not json_data:
            return None
        return cls(
            AddressDefinition=json_data.get("AddressDefinition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Address = Address


@dataclass
class PortRange(BaseModel):
    FromPort: Optional[int]
    ToPort: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_PortRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortRange"]:
        if not json_data:
            return None
        return cls(
            FromPort=json_data.get("FromPort"),
            ToPort=json_data.get("ToPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortRange = PortRange


@dataclass
class TCPFlagField(BaseModel):
    Flags: Optional[Sequence[str]]
    Masks: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_TCPFlagField"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TCPFlagField"]:
        if not json_data:
            return None
        return cls(
            Flags=json_data.get("Flags"),
            Masks=json_data.get("Masks"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TCPFlagField = TCPFlagField


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
class StatefulRuleOptions(BaseModel):
    RuleOrder: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatefulRuleOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatefulRuleOptions"]:
        if not json_data:
            return None
        return cls(
            RuleOrder=json_data.get("RuleOrder"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatefulRuleOptions = StatefulRuleOptions


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


