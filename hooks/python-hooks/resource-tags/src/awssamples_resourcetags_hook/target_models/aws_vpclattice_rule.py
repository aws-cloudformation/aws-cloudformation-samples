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
class AwsVpclatticeRule(BaseModel):
    Action: Optional["_Action"]
    Arn: Optional[str]
    Id: Optional[str]
    ListenerIdentifier: Optional[str]
    Match: Optional["_Match"]
    Name: Optional[str]
    Priority: Optional[int]
    ServiceIdentifier: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsVpclatticeRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsVpclatticeRule"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Action=Action._deserialize(json_data.get("Action")),
            Arn=json_data.get("Arn"),
            Id=json_data.get("Id"),
            ListenerIdentifier=json_data.get("ListenerIdentifier"),
            Match=Match._deserialize(json_data.get("Match")),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            ServiceIdentifier=json_data.get("ServiceIdentifier"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsVpclatticeRule = AwsVpclatticeRule


@dataclass
class Action(BaseModel):
    Forward: Optional["_Forward"]
    FixedResponse: Optional["_FixedResponse"]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            Forward=Forward._deserialize(json_data.get("Forward")),
            FixedResponse=FixedResponse._deserialize(json_data.get("FixedResponse")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class Forward(BaseModel):
    TargetGroups: Optional[Sequence["_WeightedTargetGroup"]]

    @classmethod
    def _deserialize(
        cls: Type["_Forward"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Forward"]:
        if not json_data:
            return None
        return cls(
            TargetGroups=deserialize_list(json_data.get("TargetGroups"), WeightedTargetGroup),
        )


# work around possible type aliasing issues when variable has same name as a model
_Forward = Forward


@dataclass
class WeightedTargetGroup(BaseModel):
    TargetGroupIdentifier: Optional[str]
    Weight: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_WeightedTargetGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WeightedTargetGroup"]:
        if not json_data:
            return None
        return cls(
            TargetGroupIdentifier=json_data.get("TargetGroupIdentifier"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WeightedTargetGroup = WeightedTargetGroup


@dataclass
class FixedResponse(BaseModel):
    StatusCode: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_FixedResponse"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FixedResponse"]:
        if not json_data:
            return None
        return cls(
            StatusCode=json_data.get("StatusCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FixedResponse = FixedResponse


@dataclass
class Match(BaseModel):
    HttpMatch: Optional["_HttpMatch"]

    @classmethod
    def _deserialize(
        cls: Type["_Match"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Match"]:
        if not json_data:
            return None
        return cls(
            HttpMatch=HttpMatch._deserialize(json_data.get("HttpMatch")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Match = Match


@dataclass
class HttpMatch(BaseModel):
    Method: Optional[str]
    PathMatch: Optional["_PathMatch"]
    HeaderMatches: Optional[Sequence["_HeaderMatch"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpMatch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpMatch"]:
        if not json_data:
            return None
        return cls(
            Method=json_data.get("Method"),
            PathMatch=PathMatch._deserialize(json_data.get("PathMatch")),
            HeaderMatches=deserialize_list(json_data.get("HeaderMatches"), HeaderMatch),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpMatch = HttpMatch


@dataclass
class PathMatch(BaseModel):
    Match: Optional["_PathMatchType"]
    CaseSensitive: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PathMatch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathMatch"]:
        if not json_data:
            return None
        return cls(
            Match=PathMatchType._deserialize(json_data.get("Match")),
            CaseSensitive=json_data.get("CaseSensitive"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathMatch = PathMatch


@dataclass
class PathMatchType(BaseModel):
    Exact: Optional[str]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PathMatchType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathMatchType"]:
        if not json_data:
            return None
        return cls(
            Exact=json_data.get("Exact"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathMatchType = PathMatchType


@dataclass
class HeaderMatch(BaseModel):
    Name: Optional[str]
    Match: Optional["_HeaderMatchType"]
    CaseSensitive: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderMatch"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderMatch"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Match=HeaderMatchType._deserialize(json_data.get("Match")),
            CaseSensitive=json_data.get("CaseSensitive"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderMatch = HeaderMatch


@dataclass
class HeaderMatchType(BaseModel):
    Exact: Optional[str]
    Prefix: Optional[str]
    Contains: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeaderMatchType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeaderMatchType"]:
        if not json_data:
            return None
        return cls(
            Exact=json_data.get("Exact"),
            Prefix=json_data.get("Prefix"),
            Contains=json_data.get("Contains"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeaderMatchType = HeaderMatchType


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


