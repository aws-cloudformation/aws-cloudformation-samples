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
class AwsSystemsmanagersapApplication(BaseModel):
    ApplicationId: Optional[str]
    ApplicationType: Optional[str]
    Arn: Optional[str]
    Credentials: Optional[Sequence["_Credential"]]
    Instances: Optional[Sequence[str]]
    SapInstanceNumber: Optional[str]
    Sid: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSystemsmanagersapApplication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSystemsmanagersapApplication"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ApplicationId=json_data.get("ApplicationId"),
            ApplicationType=json_data.get("ApplicationType"),
            Arn=json_data.get("Arn"),
            Credentials=deserialize_list(json_data.get("Credentials"), Credential),
            Instances=json_data.get("Instances"),
            SapInstanceNumber=json_data.get("SapInstanceNumber"),
            Sid=json_data.get("Sid"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSystemsmanagersapApplication = AwsSystemsmanagersapApplication


@dataclass
class Credential(BaseModel):
    DatabaseName: Optional[str]
    CredentialType: Optional[str]
    SecretId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Credential"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Credential"]:
        if not json_data:
            return None
        return cls(
            DatabaseName=json_data.get("DatabaseName"),
            CredentialType=json_data.get("CredentialType"),
            SecretId=json_data.get("SecretId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Credential = Credential


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


