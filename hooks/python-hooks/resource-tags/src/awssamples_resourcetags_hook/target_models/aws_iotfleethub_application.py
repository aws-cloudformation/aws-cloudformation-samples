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
class AwsIotfleethubApplication(BaseModel):
    ApplicationId: Optional[str]
    ApplicationArn: Optional[str]
    ApplicationName: Optional[str]
    ApplicationDescription: Optional[str]
    ApplicationUrl: Optional[str]
    ApplicationState: Optional[str]
    ApplicationCreationDate: Optional[int]
    ApplicationLastUpdateDate: Optional[int]
    RoleArn: Optional[str]
    SsoClientId: Optional[str]
    ErrorMessage: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotfleethubApplication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotfleethubApplication"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ApplicationId=json_data.get("ApplicationId"),
            ApplicationArn=json_data.get("ApplicationArn"),
            ApplicationName=json_data.get("ApplicationName"),
            ApplicationDescription=json_data.get("ApplicationDescription"),
            ApplicationUrl=json_data.get("ApplicationUrl"),
            ApplicationState=json_data.get("ApplicationState"),
            ApplicationCreationDate=json_data.get("ApplicationCreationDate"),
            ApplicationLastUpdateDate=json_data.get("ApplicationLastUpdateDate"),
            RoleArn=json_data.get("RoleArn"),
            SsoClientId=json_data.get("SsoClientId"),
            ErrorMessage=json_data.get("ErrorMessage"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotfleethubApplication = AwsIotfleethubApplication


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


