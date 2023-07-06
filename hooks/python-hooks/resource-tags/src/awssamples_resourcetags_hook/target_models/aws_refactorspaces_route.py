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
class AwsRefactorspacesRoute(BaseModel):
    PathResourceToId: Optional[str]
    Arn: Optional[str]
    ApplicationIdentifier: Optional[str]
    EnvironmentIdentifier: Optional[str]
    RouteIdentifier: Optional[str]
    RouteType: Optional[str]
    ServiceIdentifier: Optional[str]
    DefaultRoute: Optional["_DefaultRouteInput"]
    UriPathRoute: Optional["_UriPathRouteInput"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRefactorspacesRoute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRefactorspacesRoute"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            PathResourceToId=json_data.get("PathResourceToId"),
            Arn=json_data.get("Arn"),
            ApplicationIdentifier=json_data.get("ApplicationIdentifier"),
            EnvironmentIdentifier=json_data.get("EnvironmentIdentifier"),
            RouteIdentifier=json_data.get("RouteIdentifier"),
            RouteType=json_data.get("RouteType"),
            ServiceIdentifier=json_data.get("ServiceIdentifier"),
            DefaultRoute=DefaultRouteInput._deserialize(json_data.get("DefaultRoute")),
            UriPathRoute=UriPathRouteInput._deserialize(json_data.get("UriPathRoute")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRefactorspacesRoute = AwsRefactorspacesRoute


@dataclass
class DefaultRouteInput(BaseModel):
    ActivationState: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultRouteInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultRouteInput"]:
        if not json_data:
            return None
        return cls(
            ActivationState=json_data.get("ActivationState"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultRouteInput = DefaultRouteInput


@dataclass
class UriPathRouteInput(BaseModel):
    SourcePath: Optional[str]
    ActivationState: Optional[str]
    Methods: Optional[Sequence[str]]
    IncludeChildPaths: Optional[bool]
    AppendSourcePath: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_UriPathRouteInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UriPathRouteInput"]:
        if not json_data:
            return None
        return cls(
            SourcePath=json_data.get("SourcePath"),
            ActivationState=json_data.get("ActivationState"),
            Methods=json_data.get("Methods"),
            IncludeChildPaths=json_data.get("IncludeChildPaths"),
            AppendSourcePath=json_data.get("AppendSourcePath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UriPathRouteInput = UriPathRouteInput


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


