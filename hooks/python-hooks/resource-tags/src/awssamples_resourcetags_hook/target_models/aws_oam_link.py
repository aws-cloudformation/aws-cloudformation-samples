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
class AwsOamLink(BaseModel):
    Arn: Optional[str]
    Label: Optional[str]
    LabelTemplate: Optional[str]
    ResourceTypes: Optional[AbstractSet[str]]
    SinkIdentifier: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsOamLink"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsOamLink"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Label=json_data.get("Label"),
            LabelTemplate=json_data.get("LabelTemplate"),
            ResourceTypes=set_or_none(json_data.get("ResourceTypes")),
            SinkIdentifier=json_data.get("SinkIdentifier"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsOamLink = AwsOamLink


