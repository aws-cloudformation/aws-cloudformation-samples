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
class AwsSecretsmanagerSecret(BaseModel):
    Description: Optional[str]
    KmsKeyId: Optional[str]
    SecretString: Optional[str]
    GenerateSecretString: Optional["_GenerateSecretString"]
    ReplicaRegions: Optional[Sequence["_ReplicaRegion"]]
    Id: Optional[str]
    Tags: Optional[Any]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSecretsmanagerSecret"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSecretsmanagerSecret"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            KmsKeyId=json_data.get("KmsKeyId"),
            SecretString=json_data.get("SecretString"),
            GenerateSecretString=GenerateSecretString._deserialize(json_data.get("GenerateSecretString")),
            ReplicaRegions=deserialize_list(json_data.get("ReplicaRegions"), ReplicaRegion),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSecretsmanagerSecret = AwsSecretsmanagerSecret


@dataclass
class GenerateSecretString(BaseModel):
    ExcludeUppercase: Optional[bool]
    RequireEachIncludedType: Optional[bool]
    IncludeSpace: Optional[bool]
    ExcludeCharacters: Optional[str]
    GenerateStringKey: Optional[str]
    PasswordLength: Optional[int]
    ExcludePunctuation: Optional[bool]
    ExcludeLowercase: Optional[bool]
    SecretStringTemplate: Optional[str]
    ExcludeNumbers: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GenerateSecretString"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GenerateSecretString"]:
        if not json_data:
            return None
        return cls(
            ExcludeUppercase=json_data.get("ExcludeUppercase"),
            RequireEachIncludedType=json_data.get("RequireEachIncludedType"),
            IncludeSpace=json_data.get("IncludeSpace"),
            ExcludeCharacters=json_data.get("ExcludeCharacters"),
            GenerateStringKey=json_data.get("GenerateStringKey"),
            PasswordLength=json_data.get("PasswordLength"),
            ExcludePunctuation=json_data.get("ExcludePunctuation"),
            ExcludeLowercase=json_data.get("ExcludeLowercase"),
            SecretStringTemplate=json_data.get("SecretStringTemplate"),
            ExcludeNumbers=json_data.get("ExcludeNumbers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GenerateSecretString = GenerateSecretString


@dataclass
class ReplicaRegion(BaseModel):
    KmsKeyId: Optional[str]
    Region: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicaRegion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicaRegion"]:
        if not json_data:
            return None
        return cls(
            KmsKeyId=json_data.get("KmsKeyId"),
            Region=json_data.get("Region"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicaRegion = ReplicaRegion


@dataclass
class Tag(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


