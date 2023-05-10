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
class AwsIottwinmakerScene(BaseModel):
    SceneId: Optional[str]
    Arn: Optional[str]
    Description: Optional[str]
    ContentLocation: Optional[str]
    CreationDateTime: Optional[str]
    UpdateDateTime: Optional[str]
    Tags: Optional[Any]
    WorkspaceId: Optional[str]
    Capabilities: Optional[AbstractSet[str]]
    SceneMetadata: Optional[MutableMapping[str, str]]
    GeneratedSceneMetadata: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIottwinmakerScene"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIottwinmakerScene"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            SceneId=json_data.get("SceneId"),
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            ContentLocation=json_data.get("ContentLocation"),
            CreationDateTime=json_data.get("CreationDateTime"),
            UpdateDateTime=json_data.get("UpdateDateTime"),
            Tags=json_data.get("Tags"),
            WorkspaceId=json_data.get("WorkspaceId"),
            Capabilities=set_or_none(json_data.get("Capabilities")),
            SceneMetadata=json_data.get("SceneMetadata"),
            GeneratedSceneMetadata=json_data.get("GeneratedSceneMetadata"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIottwinmakerScene = AwsIottwinmakerScene


