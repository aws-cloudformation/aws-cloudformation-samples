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
class AwsTransferProfile(BaseModel):
    As2Id: Optional[str]
    ProfileType: Optional[str]
    Tags: Optional[Any]
    CertificateIds: Optional[Sequence[str]]
    Arn: Optional[str]
    ProfileId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsTransferProfile"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsTransferProfile"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            As2Id=json_data.get("As2Id"),
            ProfileType=json_data.get("ProfileType"),
            Tags=json_data.get("Tags"),
            CertificateIds=json_data.get("CertificateIds"),
            Arn=json_data.get("Arn"),
            ProfileId=json_data.get("ProfileId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsTransferProfile = AwsTransferProfile


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


