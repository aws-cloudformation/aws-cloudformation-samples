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
class AwsImagebuilderComponent(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    Version: Optional[str]
    Description: Optional[str]
    ChangeDescription: Optional[str]
    Type: Optional[str]
    Platform: Optional[str]
    Data: Optional[str]
    KmsKeyId: Optional[str]
    Encrypted: Optional[bool]
    Tags: Optional[Any]
    Uri: Optional[str]
    SupportedOsVersions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsImagebuilderComponent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsImagebuilderComponent"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            Version=json_data.get("Version"),
            Description=json_data.get("Description"),
            ChangeDescription=json_data.get("ChangeDescription"),
            Type=json_data.get("Type"),
            Platform=json_data.get("Platform"),
            Data=json_data.get("Data"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Encrypted=json_data.get("Encrypted"),
            Tags=json_data.get("Tags"),
            Uri=json_data.get("Uri"),
            SupportedOsVersions=json_data.get("SupportedOsVersions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsImagebuilderComponent = AwsImagebuilderComponent


