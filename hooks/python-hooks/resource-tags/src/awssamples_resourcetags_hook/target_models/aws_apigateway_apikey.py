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
class AwsApigatewayApikey(BaseModel):
    APIKeyId: Optional[str]
    CustomerId: Optional[str]
    Description: Optional[str]
    Enabled: Optional[bool]
    GenerateDistinctId: Optional[bool]
    Name: Optional[str]
    StageKeys: Optional[Sequence["_StageKey"]]
    Tags: Optional[Any]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayApikey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayApikey"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            APIKeyId=json_data.get("APIKeyId"),
            CustomerId=json_data.get("CustomerId"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            GenerateDistinctId=json_data.get("GenerateDistinctId"),
            Name=json_data.get("Name"),
            StageKeys=deserialize_list(json_data.get("StageKeys"), StageKey),
            Tags=json_data.get("Tags"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayApikey = AwsApigatewayApikey


@dataclass
class StageKey(BaseModel):
    RestApiId: Optional[str]
    StageName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StageKey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StageKey"]:
        if not json_data:
            return None
        return cls(
            RestApiId=json_data.get("RestApiId"),
            StageName=json_data.get("StageName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StageKey = StageKey


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


