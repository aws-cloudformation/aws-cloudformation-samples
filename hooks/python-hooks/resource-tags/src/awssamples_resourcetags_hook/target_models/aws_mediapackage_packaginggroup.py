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
class AwsMediapackagePackaginggroup(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]
    DomainName: Optional[str]
    Authorization: Optional["_Authorization"]
    Tags: Optional[Any]
    EgressAccessLogs: Optional["_LogConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMediapackagePackaginggroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMediapackagePackaginggroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            DomainName=json_data.get("DomainName"),
            Authorization=Authorization._deserialize(json_data.get("Authorization")),
            Tags=json_data.get("Tags"),
            EgressAccessLogs=LogConfiguration._deserialize(json_data.get("EgressAccessLogs")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMediapackagePackaginggroup = AwsMediapackagePackaginggroup


@dataclass
class Authorization(BaseModel):
    CdnIdentifierSecret: Optional[str]
    SecretsRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Authorization"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Authorization"]:
        if not json_data:
            return None
        return cls(
            CdnIdentifierSecret=json_data.get("CdnIdentifierSecret"),
            SecretsRoleArn=json_data.get("SecretsRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Authorization = Authorization


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


@dataclass
class LogConfiguration(BaseModel):
    LogGroupName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogConfiguration"]:
        if not json_data:
            return None
        return cls(
            LogGroupName=json_data.get("LogGroupName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogConfiguration = LogConfiguration


