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
class AwsKendraIndex(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]
    Description: Optional[str]
    ServerSideEncryptionConfiguration: Optional["_ServerSideEncryptionConfiguration"]
    Tags: Optional[Any]
    Name: Optional[str]
    RoleArn: Optional[str]
    Edition: Optional[str]
    DocumentMetadataConfigurations: Optional[Sequence["_DocumentMetadataConfiguration"]]
    CapacityUnits: Optional["_CapacityUnitsConfiguration"]
    UserContextPolicy: Optional[str]
    UserTokenConfigurations: Optional[Sequence["_UserTokenConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsKendraIndex"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsKendraIndex"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            ServerSideEncryptionConfiguration=ServerSideEncryptionConfiguration._deserialize(json_data.get("ServerSideEncryptionConfiguration")),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
            RoleArn=json_data.get("RoleArn"),
            Edition=json_data.get("Edition"),
            DocumentMetadataConfigurations=deserialize_list(json_data.get("DocumentMetadataConfigurations"), DocumentMetadataConfiguration),
            CapacityUnits=CapacityUnitsConfiguration._deserialize(json_data.get("CapacityUnits")),
            UserContextPolicy=json_data.get("UserContextPolicy"),
            UserTokenConfigurations=deserialize_list(json_data.get("UserTokenConfigurations"), UserTokenConfiguration),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsKendraIndex = AwsKendraIndex


@dataclass
class ServerSideEncryptionConfiguration(BaseModel):
    KmsKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerSideEncryptionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerSideEncryptionConfiguration"]:
        if not json_data:
            return None
        return cls(
            KmsKeyId=json_data.get("KmsKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerSideEncryptionConfiguration = ServerSideEncryptionConfiguration


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
class DocumentMetadataConfiguration(BaseModel):
    Name: Optional[str]
    Type: Optional[str]
    Relevance: Optional["_Relevance"]
    Search: Optional["_Search"]

    @classmethod
    def _deserialize(
        cls: Type["_DocumentMetadataConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DocumentMetadataConfiguration"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Relevance=Relevance._deserialize(json_data.get("Relevance")),
            Search=Search._deserialize(json_data.get("Search")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DocumentMetadataConfiguration = DocumentMetadataConfiguration


@dataclass
class Relevance(BaseModel):
    Freshness: Optional[bool]
    Importance: Optional[int]
    Duration: Optional[str]
    RankOrder: Optional[str]
    ValueImportanceItems: Optional[Sequence["_ValueImportanceItem"]]

    @classmethod
    def _deserialize(
        cls: Type["_Relevance"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Relevance"]:
        if not json_data:
            return None
        return cls(
            Freshness=json_data.get("Freshness"),
            Importance=json_data.get("Importance"),
            Duration=json_data.get("Duration"),
            RankOrder=json_data.get("RankOrder"),
            ValueImportanceItems=deserialize_list(json_data.get("ValueImportanceItems"), ValueImportanceItem),
        )


# work around possible type aliasing issues when variable has same name as a model
_Relevance = Relevance


@dataclass
class ValueImportanceItem(BaseModel):
    Key: Optional[str]
    Value: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ValueImportanceItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValueImportanceItem"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValueImportanceItem = ValueImportanceItem


@dataclass
class Search(BaseModel):
    Facetable: Optional[bool]
    Searchable: Optional[bool]
    Displayable: Optional[bool]
    Sortable: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Search"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Search"]:
        if not json_data:
            return None
        return cls(
            Facetable=json_data.get("Facetable"),
            Searchable=json_data.get("Searchable"),
            Displayable=json_data.get("Displayable"),
            Sortable=json_data.get("Sortable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Search = Search


@dataclass
class CapacityUnitsConfiguration(BaseModel):
    StorageCapacityUnits: Optional[int]
    QueryCapacityUnits: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityUnitsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityUnitsConfiguration"]:
        if not json_data:
            return None
        return cls(
            StorageCapacityUnits=json_data.get("StorageCapacityUnits"),
            QueryCapacityUnits=json_data.get("QueryCapacityUnits"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityUnitsConfiguration = CapacityUnitsConfiguration


@dataclass
class UserTokenConfiguration(BaseModel):
    JwtTokenTypeConfiguration: Optional["_JwtTokenTypeConfiguration"]
    JsonTokenTypeConfiguration: Optional["_JsonTokenTypeConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_UserTokenConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserTokenConfiguration"]:
        if not json_data:
            return None
        return cls(
            JwtTokenTypeConfiguration=JwtTokenTypeConfiguration._deserialize(json_data.get("JwtTokenTypeConfiguration")),
            JsonTokenTypeConfiguration=JsonTokenTypeConfiguration._deserialize(json_data.get("JsonTokenTypeConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserTokenConfiguration = UserTokenConfiguration


@dataclass
class JwtTokenTypeConfiguration(BaseModel):
    KeyLocation: Optional[str]
    URL: Optional[str]
    SecretManagerArn: Optional[str]
    UserNameAttributeField: Optional[str]
    GroupAttributeField: Optional[str]
    Issuer: Optional[str]
    ClaimRegex: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JwtTokenTypeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JwtTokenTypeConfiguration"]:
        if not json_data:
            return None
        return cls(
            KeyLocation=json_data.get("KeyLocation"),
            URL=json_data.get("URL"),
            SecretManagerArn=json_data.get("SecretManagerArn"),
            UserNameAttributeField=json_data.get("UserNameAttributeField"),
            GroupAttributeField=json_data.get("GroupAttributeField"),
            Issuer=json_data.get("Issuer"),
            ClaimRegex=json_data.get("ClaimRegex"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JwtTokenTypeConfiguration = JwtTokenTypeConfiguration


@dataclass
class JsonTokenTypeConfiguration(BaseModel):
    UserNameAttributeField: Optional[str]
    GroupAttributeField: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JsonTokenTypeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JsonTokenTypeConfiguration"]:
        if not json_data:
            return None
        return cls(
            UserNameAttributeField=json_data.get("UserNameAttributeField"),
            GroupAttributeField=json_data.get("GroupAttributeField"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JsonTokenTypeConfiguration = JsonTokenTypeConfiguration


