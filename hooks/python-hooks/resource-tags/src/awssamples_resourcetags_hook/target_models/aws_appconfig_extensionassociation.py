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
class AwsAppconfigExtensionassociation(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]
    ExtensionArn: Optional[str]
    ResourceArn: Optional[str]
    ExtensionIdentifier: Optional[str]
    ResourceIdentifier: Optional[str]
    ExtensionVersionNumber: Optional[int]
    Parameters: Optional[MutableMapping[str, str]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppconfigExtensionassociation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppconfigExtensionassociation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            ExtensionArn=json_data.get("ExtensionArn"),
            ResourceArn=json_data.get("ResourceArn"),
            ExtensionIdentifier=json_data.get("ExtensionIdentifier"),
            ResourceIdentifier=json_data.get("ResourceIdentifier"),
            ExtensionVersionNumber=json_data.get("ExtensionVersionNumber"),
            Parameters=json_data.get("Parameters"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppconfigExtensionassociation = AwsAppconfigExtensionassociation


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


