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
class AwsCleanroomsCollaboration(BaseModel):
    Arn: Optional[str]
    Tags: Optional[Any]
    CollaborationIdentifier: Optional[str]
    CreatorDisplayName: Optional[str]
    CreatorMemberAbilities: Optional[AbstractSet[str]]
    DataEncryptionMetadata: Optional["_DataEncryptionMetadata"]
    Description: Optional[str]
    Members: Optional[Sequence["_MemberSpecification"]]
    Name: Optional[str]
    QueryLogStatus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCleanroomsCollaboration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCleanroomsCollaboration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
            CollaborationIdentifier=json_data.get("CollaborationIdentifier"),
            CreatorDisplayName=json_data.get("CreatorDisplayName"),
            CreatorMemberAbilities=set_or_none(json_data.get("CreatorMemberAbilities")),
            DataEncryptionMetadata=DataEncryptionMetadata._deserialize(json_data.get("DataEncryptionMetadata")),
            Description=json_data.get("Description"),
            Members=deserialize_list(json_data.get("Members"), MemberSpecification),
            Name=json_data.get("Name"),
            QueryLogStatus=json_data.get("QueryLogStatus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCleanroomsCollaboration = AwsCleanroomsCollaboration


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
class DataEncryptionMetadata(BaseModel):
    AllowCleartext: Optional[bool]
    AllowDuplicates: Optional[bool]
    AllowJoinsOnColumnsWithDifferentNames: Optional[bool]
    PreserveNulls: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DataEncryptionMetadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataEncryptionMetadata"]:
        if not json_data:
            return None
        return cls(
            AllowCleartext=json_data.get("AllowCleartext"),
            AllowDuplicates=json_data.get("AllowDuplicates"),
            AllowJoinsOnColumnsWithDifferentNames=json_data.get("AllowJoinsOnColumnsWithDifferentNames"),
            PreserveNulls=json_data.get("PreserveNulls"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataEncryptionMetadata = DataEncryptionMetadata


@dataclass
class MemberSpecification(BaseModel):
    AccountId: Optional[str]
    MemberAbilities: Optional[AbstractSet[str]]
    DisplayName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MemberSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemberSpecification"]:
        if not json_data:
            return None
        return cls(
            AccountId=json_data.get("AccountId"),
            MemberAbilities=set_or_none(json_data.get("MemberAbilities")),
            DisplayName=json_data.get("DisplayName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemberSpecification = MemberSpecification


