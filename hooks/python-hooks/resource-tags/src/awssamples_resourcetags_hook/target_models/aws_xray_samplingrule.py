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
class AwsXraySamplingrule(BaseModel):
    SamplingRule: Optional["_SamplingRule"]
    SamplingRuleRecord: Optional["_SamplingRuleRecord"]
    SamplingRuleUpdate: Optional["_SamplingRuleUpdate"]
    RuleARN: Optional[str]
    RuleName: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsXraySamplingrule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsXraySamplingrule"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            SamplingRule=SamplingRule._deserialize(json_data.get("SamplingRule")),
            SamplingRuleRecord=SamplingRuleRecord._deserialize(json_data.get("SamplingRuleRecord")),
            SamplingRuleUpdate=SamplingRuleUpdate._deserialize(json_data.get("SamplingRuleUpdate")),
            RuleARN=json_data.get("RuleARN"),
            RuleName=json_data.get("RuleName"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsXraySamplingrule = AwsXraySamplingrule


@dataclass
class SamplingRule(BaseModel):
    Attributes: Optional[MutableMapping[str, str]]
    FixedRate: Optional[float]
    Host: Optional[str]
    HTTPMethod: Optional[str]
    Priority: Optional[int]
    ReservoirSize: Optional[int]
    ResourceARN: Optional[str]
    RuleARN: Optional[str]
    RuleName: Optional[str]
    ServiceName: Optional[str]
    ServiceType: Optional[str]
    URLPath: Optional[str]
    Version: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_SamplingRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SamplingRule"]:
        if not json_data:
            return None
        return cls(
            Attributes=json_data.get("Attributes"),
            FixedRate=json_data.get("FixedRate"),
            Host=json_data.get("Host"),
            HTTPMethod=json_data.get("HTTPMethod"),
            Priority=json_data.get("Priority"),
            ReservoirSize=json_data.get("ReservoirSize"),
            ResourceARN=json_data.get("ResourceARN"),
            RuleARN=json_data.get("RuleARN"),
            RuleName=json_data.get("RuleName"),
            ServiceName=json_data.get("ServiceName"),
            ServiceType=json_data.get("ServiceType"),
            URLPath=json_data.get("URLPath"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SamplingRule = SamplingRule


@dataclass
class SamplingRuleRecord(BaseModel):
    CreatedAt: Optional[str]
    ModifiedAt: Optional[str]
    SamplingRule: Optional["_SamplingRule"]

    @classmethod
    def _deserialize(
        cls: Type["_SamplingRuleRecord"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SamplingRuleRecord"]:
        if not json_data:
            return None
        return cls(
            CreatedAt=json_data.get("CreatedAt"),
            ModifiedAt=json_data.get("ModifiedAt"),
            SamplingRule=SamplingRule._deserialize(json_data.get("SamplingRule")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SamplingRuleRecord = SamplingRuleRecord


@dataclass
class SamplingRuleUpdate(BaseModel):
    Attributes: Optional[MutableMapping[str, str]]
    FixedRate: Optional[float]
    Host: Optional[str]
    HTTPMethod: Optional[str]
    Priority: Optional[int]
    ReservoirSize: Optional[int]
    ResourceARN: Optional[str]
    RuleARN: Optional[str]
    RuleName: Optional[str]
    ServiceName: Optional[str]
    ServiceType: Optional[str]
    URLPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SamplingRuleUpdate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SamplingRuleUpdate"]:
        if not json_data:
            return None
        return cls(
            Attributes=json_data.get("Attributes"),
            FixedRate=json_data.get("FixedRate"),
            Host=json_data.get("Host"),
            HTTPMethod=json_data.get("HTTPMethod"),
            Priority=json_data.get("Priority"),
            ReservoirSize=json_data.get("ReservoirSize"),
            ResourceARN=json_data.get("ResourceARN"),
            RuleARN=json_data.get("RuleARN"),
            RuleName=json_data.get("RuleName"),
            ServiceName=json_data.get("ServiceName"),
            ServiceType=json_data.get("ServiceType"),
            URLPath=json_data.get("URLPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SamplingRuleUpdate = SamplingRuleUpdate


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


