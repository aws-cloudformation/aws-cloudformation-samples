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
class AwsNimblestudioStudio(BaseModel):
    AdminRoleArn: Optional[str]
    DisplayName: Optional[str]
    HomeRegion: Optional[str]
    SsoClientId: Optional[str]
    StudioEncryptionConfiguration: Optional["_StudioEncryptionConfiguration"]
    StudioId: Optional[str]
    StudioName: Optional[str]
    StudioUrl: Optional[str]
    Tags: Optional[Any]
    UserRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsNimblestudioStudio"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsNimblestudioStudio"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AdminRoleArn=json_data.get("AdminRoleArn"),
            DisplayName=json_data.get("DisplayName"),
            HomeRegion=json_data.get("HomeRegion"),
            SsoClientId=json_data.get("SsoClientId"),
            StudioEncryptionConfiguration=StudioEncryptionConfiguration._deserialize(json_data.get("StudioEncryptionConfiguration")),
            StudioId=json_data.get("StudioId"),
            StudioName=json_data.get("StudioName"),
            StudioUrl=json_data.get("StudioUrl"),
            Tags=json_data.get("Tags"),
            UserRoleArn=json_data.get("UserRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsNimblestudioStudio = AwsNimblestudioStudio


@dataclass
class StudioEncryptionConfiguration(BaseModel):
    KeyType: Optional[str]
    KeyArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StudioEncryptionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StudioEncryptionConfiguration"]:
        if not json_data:
            return None
        return cls(
            KeyType=json_data.get("KeyType"),
            KeyArn=json_data.get("KeyArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StudioEncryptionConfiguration = StudioEncryptionConfiguration


