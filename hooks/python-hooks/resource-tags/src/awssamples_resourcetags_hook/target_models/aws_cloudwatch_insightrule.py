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
class AwsCloudwatchInsightrule(BaseModel):
    RuleState: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]
    RuleBody: Optional[str]
    RuleName: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudwatchInsightrule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudwatchInsightrule"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            RuleState=json_data.get("RuleState"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            RuleBody=json_data.get("RuleBody"),
            RuleName=json_data.get("RuleName"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudwatchInsightrule = AwsCloudwatchInsightrule


