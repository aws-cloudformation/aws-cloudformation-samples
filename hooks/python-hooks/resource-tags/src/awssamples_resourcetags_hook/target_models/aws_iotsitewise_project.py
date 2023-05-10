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
class AwsIotsitewiseProject(BaseModel):
    PortalId: Optional[str]
    ProjectId: Optional[str]
    ProjectName: Optional[str]
    ProjectDescription: Optional[str]
    ProjectArn: Optional[str]
    AssetIds: Optional[Sequence[str]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotsitewiseProject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotsitewiseProject"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            PortalId=json_data.get("PortalId"),
            ProjectId=json_data.get("ProjectId"),
            ProjectName=json_data.get("ProjectName"),
            ProjectDescription=json_data.get("ProjectDescription"),
            ProjectArn=json_data.get("ProjectArn"),
            AssetIds=json_data.get("AssetIds"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotsitewiseProject = AwsIotsitewiseProject


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


