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
class AwsConfigConfigurationaggregator(BaseModel):
    AccountAggregationSources: Optional[Sequence["_AccountAggregationSource"]]
    ConfigurationAggregatorName: Optional[str]
    ConfigurationAggregatorArn: Optional[str]
    OrganizationAggregationSource: Optional["_OrganizationAggregationSource"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConfigConfigurationaggregator"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConfigConfigurationaggregator"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AccountAggregationSources=deserialize_list(json_data.get("AccountAggregationSources"), AccountAggregationSource),
            ConfigurationAggregatorName=json_data.get("ConfigurationAggregatorName"),
            ConfigurationAggregatorArn=json_data.get("ConfigurationAggregatorArn"),
            OrganizationAggregationSource=OrganizationAggregationSource._deserialize(json_data.get("OrganizationAggregationSource")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConfigConfigurationaggregator = AwsConfigConfigurationaggregator


@dataclass
class AccountAggregationSource(BaseModel):
    AllAwsRegions: Optional[bool]
    AwsRegions: Optional[Sequence[str]]
    AccountIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AccountAggregationSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccountAggregationSource"]:
        if not json_data:
            return None
        return cls(
            AllAwsRegions=json_data.get("AllAwsRegions"),
            AwsRegions=json_data.get("AwsRegions"),
            AccountIds=json_data.get("AccountIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccountAggregationSource = AccountAggregationSource


@dataclass
class OrganizationAggregationSource(BaseModel):
    AllAwsRegions: Optional[bool]
    AwsRegions: Optional[Sequence[str]]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OrganizationAggregationSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrganizationAggregationSource"]:
        if not json_data:
            return None
        return cls(
            AllAwsRegions=json_data.get("AllAwsRegions"),
            AwsRegions=json_data.get("AwsRegions"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrganizationAggregationSource = OrganizationAggregationSource


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


