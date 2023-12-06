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
class AwsBackupRestoretestingplan(BaseModel):
    RecoveryPointSelection: Optional["_RestoreTestingRecoveryPointSelection"]
    RestoreTestingPlanArn: Optional[str]
    RestoreTestingPlanName: Optional[str]
    ScheduleExpression: Optional[str]
    ScheduleExpressionTimezone: Optional[str]
    StartWindowHours: Optional[int]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsBackupRestoretestingplan"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsBackupRestoretestingplan"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            RecoveryPointSelection=RestoreTestingRecoveryPointSelection._deserialize(json_data.get("RecoveryPointSelection")),
            RestoreTestingPlanArn=json_data.get("RestoreTestingPlanArn"),
            RestoreTestingPlanName=json_data.get("RestoreTestingPlanName"),
            ScheduleExpression=json_data.get("ScheduleExpression"),
            ScheduleExpressionTimezone=json_data.get("ScheduleExpressionTimezone"),
            StartWindowHours=json_data.get("StartWindowHours"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsBackupRestoretestingplan = AwsBackupRestoretestingplan


@dataclass
class RestoreTestingRecoveryPointSelection(BaseModel):
    Algorithm: Optional[str]
    SelectionWindowDays: Optional[int]
    RecoveryPointTypes: Optional[Sequence[str]]
    IncludeVaults: Optional[Sequence[str]]
    ExcludeVaults: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RestoreTestingRecoveryPointSelection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RestoreTestingRecoveryPointSelection"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            SelectionWindowDays=json_data.get("SelectionWindowDays"),
            RecoveryPointTypes=json_data.get("RecoveryPointTypes"),
            IncludeVaults=json_data.get("IncludeVaults"),
            ExcludeVaults=json_data.get("ExcludeVaults"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RestoreTestingRecoveryPointSelection = RestoreTestingRecoveryPointSelection


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


