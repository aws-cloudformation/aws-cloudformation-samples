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
class AwsHealthimagingDatastore(BaseModel):
    DatastoreArn: Optional[str]
    DatastoreName: Optional[str]
    DatastoreId: Optional[str]
    DatastoreStatus: Optional[str]
    KmsKeyArn: Optional[str]
    CreatedAt: Optional[str]
    UpdatedAt: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsHealthimagingDatastore"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsHealthimagingDatastore"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DatastoreArn=json_data.get("DatastoreArn"),
            DatastoreName=json_data.get("DatastoreName"),
            DatastoreId=json_data.get("DatastoreId"),
            DatastoreStatus=json_data.get("DatastoreStatus"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            CreatedAt=json_data.get("CreatedAt"),
            UpdatedAt=json_data.get("UpdatedAt"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsHealthimagingDatastore = AwsHealthimagingDatastore


