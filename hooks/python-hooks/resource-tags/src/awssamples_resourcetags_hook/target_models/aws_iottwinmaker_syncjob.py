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
class AwsIottwinmakerSyncjob(BaseModel):
    WorkspaceId: Optional[str]
    SyncSource: Optional[str]
    SyncRole: Optional[str]
    CreationDateTime: Optional[str]
    UpdateDateTime: Optional[str]
    Arn: Optional[str]
    State: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIottwinmakerSyncjob"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIottwinmakerSyncjob"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            WorkspaceId=json_data.get("WorkspaceId"),
            SyncSource=json_data.get("SyncSource"),
            SyncRole=json_data.get("SyncRole"),
            CreationDateTime=json_data.get("CreationDateTime"),
            UpdateDateTime=json_data.get("UpdateDateTime"),
            Arn=json_data.get("Arn"),
            State=json_data.get("State"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIottwinmakerSyncjob = AwsIottwinmakerSyncjob


