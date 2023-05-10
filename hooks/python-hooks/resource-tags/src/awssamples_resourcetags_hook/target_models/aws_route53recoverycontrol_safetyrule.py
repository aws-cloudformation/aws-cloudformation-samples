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
class AwsRoute53recoverycontrolSafetyrule(BaseModel):
    AssertionRule: Optional["_AssertionRule"]
    GatingRule: Optional["_GatingRule"]
    Name: Optional[str]
    SafetyRuleArn: Optional[str]
    ControlPanelArn: Optional[str]
    Status: Optional[str]
    RuleConfig: Optional["_RuleConfig"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRoute53recoverycontrolSafetyrule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRoute53recoverycontrolSafetyrule"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AssertionRule=AssertionRule._deserialize(json_data.get("AssertionRule")),
            GatingRule=GatingRule._deserialize(json_data.get("GatingRule")),
            Name=json_data.get("Name"),
            SafetyRuleArn=json_data.get("SafetyRuleArn"),
            ControlPanelArn=json_data.get("ControlPanelArn"),
            Status=json_data.get("Status"),
            RuleConfig=RuleConfig._deserialize(json_data.get("RuleConfig")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRoute53recoverycontrolSafetyrule = AwsRoute53recoverycontrolSafetyrule


@dataclass
class AssertionRule(BaseModel):
    WaitPeriodMs: Optional[int]
    AssertedControls: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AssertionRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssertionRule"]:
        if not json_data:
            return None
        return cls(
            WaitPeriodMs=json_data.get("WaitPeriodMs"),
            AssertedControls=json_data.get("AssertedControls"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssertionRule = AssertionRule


@dataclass
class GatingRule(BaseModel):
    GatingControls: Optional[Sequence[str]]
    TargetControls: Optional[Sequence[str]]
    WaitPeriodMs: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_GatingRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GatingRule"]:
        if not json_data:
            return None
        return cls(
            GatingControls=json_data.get("GatingControls"),
            TargetControls=json_data.get("TargetControls"),
            WaitPeriodMs=json_data.get("WaitPeriodMs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GatingRule = GatingRule


@dataclass
class RuleConfig(BaseModel):
    Type: Optional[str]
    Threshold: Optional[int]
    Inverted: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RuleConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleConfig"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Threshold=json_data.get("Threshold"),
            Inverted=json_data.get("Inverted"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleConfig = RuleConfig


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


