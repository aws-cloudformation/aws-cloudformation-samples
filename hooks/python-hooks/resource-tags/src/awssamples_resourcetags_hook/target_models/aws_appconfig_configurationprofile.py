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
class AwsAppconfigConfigurationprofile(BaseModel):
    LocationUri: Optional[str]
    Type: Optional[str]
    Description: Optional[str]
    Validators: Optional[Sequence["_Validators"]]
    RetrievalRoleArn: Optional[str]
    Id: Optional[str]
    ApplicationId: Optional[str]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppconfigConfigurationprofile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppconfigConfigurationprofile"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            LocationUri=json_data.get("LocationUri"),
            Type=json_data.get("Type"),
            Description=json_data.get("Description"),
            Validators=deserialize_list(json_data.get("Validators"), Validators),
            RetrievalRoleArn=json_data.get("RetrievalRoleArn"),
            Id=json_data.get("Id"),
            ApplicationId=json_data.get("ApplicationId"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppconfigConfigurationprofile = AwsAppconfigConfigurationprofile


@dataclass
class Validators(BaseModel):
    Type: Optional[str]
    Content: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Validators"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Validators"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Content=json_data.get("Content"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Validators = Validators


@dataclass
class Tags(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


