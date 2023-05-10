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
class AwsServicecatalogCloudformationproduct(BaseModel):
    Owner: Optional[str]
    Description: Optional[str]
    ProductName: Optional[str]
    SupportEmail: Optional[str]
    ProductType: Optional[str]
    ProvisioningArtifactNames: Optional[str]
    Name: Optional[str]
    ReplaceProvisioningArtifacts: Optional[bool]
    SupportDescription: Optional[str]
    Distributor: Optional[str]
    ProvisioningArtifactIds: Optional[str]
    AcceptLanguage: Optional[str]
    SupportUrl: Optional[str]
    Id: Optional[str]
    SourceConnection: Optional["_SourceConnection"]
    Tags: Optional[Any]
    ProvisioningArtifactParameters: Optional[Sequence["_ProvisioningArtifactProperties"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsServicecatalogCloudformationproduct"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsServicecatalogCloudformationproduct"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Owner=json_data.get("Owner"),
            Description=json_data.get("Description"),
            ProductName=json_data.get("ProductName"),
            SupportEmail=json_data.get("SupportEmail"),
            ProductType=json_data.get("ProductType"),
            ProvisioningArtifactNames=json_data.get("ProvisioningArtifactNames"),
            Name=json_data.get("Name"),
            ReplaceProvisioningArtifacts=json_data.get("ReplaceProvisioningArtifacts"),
            SupportDescription=json_data.get("SupportDescription"),
            Distributor=json_data.get("Distributor"),
            ProvisioningArtifactIds=json_data.get("ProvisioningArtifactIds"),
            AcceptLanguage=json_data.get("AcceptLanguage"),
            SupportUrl=json_data.get("SupportUrl"),
            Id=json_data.get("Id"),
            SourceConnection=SourceConnection._deserialize(json_data.get("SourceConnection")),
            Tags=json_data.get("Tags"),
            ProvisioningArtifactParameters=deserialize_list(json_data.get("ProvisioningArtifactParameters"), ProvisioningArtifactProperties),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsServicecatalogCloudformationproduct = AwsServicecatalogCloudformationproduct


@dataclass
class SourceConnection(BaseModel):
    ConnectionParameters: Optional["_ConnectionParameters"]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceConnection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceConnection"]:
        if not json_data:
            return None
        return cls(
            ConnectionParameters=ConnectionParameters._deserialize(json_data.get("ConnectionParameters")),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceConnection = SourceConnection


@dataclass
class ConnectionParameters(BaseModel):
    CodeStar: Optional["_CodeStarParameters"]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionParameters"]:
        if not json_data:
            return None
        return cls(
            CodeStar=CodeStarParameters._deserialize(json_data.get("CodeStar")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionParameters = ConnectionParameters


@dataclass
class CodeStarParameters(BaseModel):
    ArtifactPath: Optional[str]
    ConnectionArn: Optional[str]
    Repository: Optional[str]
    Branch: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CodeStarParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CodeStarParameters"]:
        if not json_data:
            return None
        return cls(
            ArtifactPath=json_data.get("ArtifactPath"),
            ConnectionArn=json_data.get("ConnectionArn"),
            Repository=json_data.get("Repository"),
            Branch=json_data.get("Branch"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CodeStarParameters = CodeStarParameters


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


@dataclass
class ProvisioningArtifactProperties(BaseModel):
    Type: Optional[str]
    Description: Optional[str]
    Info: Optional[MutableMapping[str, Any]]
    DisableTemplateValidation: Optional[bool]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProvisioningArtifactProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProvisioningArtifactProperties"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Description=json_data.get("Description"),
            Info=json_data.get("Info"),
            DisableTemplateValidation=json_data.get("DisableTemplateValidation"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProvisioningArtifactProperties = ProvisioningArtifactProperties


