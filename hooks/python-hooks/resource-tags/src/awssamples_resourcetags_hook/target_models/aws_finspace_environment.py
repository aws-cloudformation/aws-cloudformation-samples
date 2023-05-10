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
class AwsFinspaceEnvironment(BaseModel):
    EnvironmentId: Optional[str]
    Name: Optional[str]
    AwsAccountId: Optional[str]
    Description: Optional[str]
    Status: Optional[str]
    EnvironmentUrl: Optional[str]
    EnvironmentArn: Optional[str]
    SageMakerStudioDomainUrl: Optional[str]
    KmsKeyId: Optional[str]
    DedicatedServiceAccountId: Optional[str]
    FederationMode: Optional[str]
    FederationParameters: Optional["_FederationParameters"]
    SuperuserParameters: Optional["_SuperuserParameters"]
    DataBundles: Optional[Sequence[str]]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsFinspaceEnvironment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsFinspaceEnvironment"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            EnvironmentId=json_data.get("EnvironmentId"),
            Name=json_data.get("Name"),
            AwsAccountId=json_data.get("AwsAccountId"),
            Description=json_data.get("Description"),
            Status=json_data.get("Status"),
            EnvironmentUrl=json_data.get("EnvironmentUrl"),
            EnvironmentArn=json_data.get("EnvironmentArn"),
            SageMakerStudioDomainUrl=json_data.get("SageMakerStudioDomainUrl"),
            KmsKeyId=json_data.get("KmsKeyId"),
            DedicatedServiceAccountId=json_data.get("DedicatedServiceAccountId"),
            FederationMode=json_data.get("FederationMode"),
            FederationParameters=FederationParameters._deserialize(json_data.get("FederationParameters")),
            SuperuserParameters=SuperuserParameters._deserialize(json_data.get("SuperuserParameters")),
            DataBundles=json_data.get("DataBundles"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsFinspaceEnvironment = AwsFinspaceEnvironment


@dataclass
class FederationParameters(BaseModel):
    SamlMetadataURL: Optional[str]
    FederationProviderName: Optional[str]
    SamlMetadataDocument: Optional[str]
    ApplicationCallBackURL: Optional[str]
    FederationURN: Optional[str]
    AttributeMap: Optional[Sequence["_AttributeMap"]]

    @classmethod
    def _deserialize(
        cls: Type["_FederationParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FederationParameters"]:
        if not json_data:
            return None
        return cls(
            SamlMetadataURL=json_data.get("SamlMetadataURL"),
            FederationProviderName=json_data.get("FederationProviderName"),
            SamlMetadataDocument=json_data.get("SamlMetadataDocument"),
            ApplicationCallBackURL=json_data.get("ApplicationCallBackURL"),
            FederationURN=json_data.get("FederationURN"),
            AttributeMap=deserialize_list(json_data.get("AttributeMap"), AttributeMap),
        )


# work around possible type aliasing issues when variable has same name as a model
_FederationParameters = FederationParameters


@dataclass
class AttributeMap(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttributeMap"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributeMap"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributeMap = AttributeMap


@dataclass
class SuperuserParameters(BaseModel):
    FirstName: Optional[str]
    LastName: Optional[str]
    EmailAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SuperuserParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SuperuserParameters"]:
        if not json_data:
            return None
        return cls(
            FirstName=json_data.get("FirstName"),
            LastName=json_data.get("LastName"),
            EmailAddress=json_data.get("EmailAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SuperuserParameters = SuperuserParameters


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


