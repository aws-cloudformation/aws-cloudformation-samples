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
class AwsBackupgatewayHypervisor(BaseModel):
    Host: Optional[str]
    HypervisorArn: Optional[str]
    KmsKeyArn: Optional[str]
    LogGroupArn: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Tags: Optional[Any]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsBackupgatewayHypervisor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsBackupgatewayHypervisor"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Host=json_data.get("Host"),
            HypervisorArn=json_data.get("HypervisorArn"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            LogGroupArn=json_data.get("LogGroupArn"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Tags=json_data.get("Tags"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsBackupgatewayHypervisor = AwsBackupgatewayHypervisor


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


