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
class AwsEc2Networkinsightsaccessscopeanalysis(BaseModel):
    NetworkInsightsAccessScopeAnalysisId: Optional[str]
    NetworkInsightsAccessScopeAnalysisArn: Optional[str]
    NetworkInsightsAccessScopeId: Optional[str]
    Status: Optional[str]
    StatusMessage: Optional[str]
    StartDate: Optional[str]
    EndDate: Optional[str]
    FindingsFound: Optional[str]
    AnalyzedEniCount: Optional[int]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Networkinsightsaccessscopeanalysis"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Networkinsightsaccessscopeanalysis"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            NetworkInsightsAccessScopeAnalysisId=json_data.get("NetworkInsightsAccessScopeAnalysisId"),
            NetworkInsightsAccessScopeAnalysisArn=json_data.get("NetworkInsightsAccessScopeAnalysisArn"),
            NetworkInsightsAccessScopeId=json_data.get("NetworkInsightsAccessScopeId"),
            Status=json_data.get("Status"),
            StatusMessage=json_data.get("StatusMessage"),
            StartDate=json_data.get("StartDate"),
            EndDate=json_data.get("EndDate"),
            FindingsFound=json_data.get("FindingsFound"),
            AnalyzedEniCount=json_data.get("AnalyzedEniCount"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Networkinsightsaccessscopeanalysis = AwsEc2Networkinsightsaccessscopeanalysis


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


