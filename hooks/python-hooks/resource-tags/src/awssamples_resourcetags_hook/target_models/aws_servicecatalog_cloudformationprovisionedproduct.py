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
class AwsServicecatalogCloudformationprovisionedproduct(BaseModel):
    AcceptLanguage: Optional[str]
    NotificationArns: Optional[Sequence[str]]
    PathId: Optional[str]
    PathName: Optional[str]
    ProductId: Optional[str]
    ProductName: Optional[str]
    ProvisionedProductName: Optional[str]
    ProvisioningArtifactId: Optional[str]
    ProvisioningArtifactName: Optional[str]
    ProvisioningParameters: Optional[Sequence["_ProvisioningParameter"]]
    ProvisioningPreferences: Optional["_ProvisioningPreferences"]
    Tags: Optional[Any]
    ProvisionedProductId: Optional[str]
    RecordId: Optional[str]
    CloudformationStackArn: Optional[str]
    Outputs: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsServicecatalogCloudformationprovisionedproduct"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsServicecatalogCloudformationprovisionedproduct"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AcceptLanguage=json_data.get("AcceptLanguage"),
            NotificationArns=json_data.get("NotificationArns"),
            PathId=json_data.get("PathId"),
            PathName=json_data.get("PathName"),
            ProductId=json_data.get("ProductId"),
            ProductName=json_data.get("ProductName"),
            ProvisionedProductName=json_data.get("ProvisionedProductName"),
            ProvisioningArtifactId=json_data.get("ProvisioningArtifactId"),
            ProvisioningArtifactName=json_data.get("ProvisioningArtifactName"),
            ProvisioningParameters=deserialize_list(json_data.get("ProvisioningParameters"), ProvisioningParameter),
            ProvisioningPreferences=ProvisioningPreferences._deserialize(json_data.get("ProvisioningPreferences")),
            Tags=json_data.get("Tags"),
            ProvisionedProductId=json_data.get("ProvisionedProductId"),
            RecordId=json_data.get("RecordId"),
            CloudformationStackArn=json_data.get("CloudformationStackArn"),
            Outputs=json_data.get("Outputs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsServicecatalogCloudformationprovisionedproduct = AwsServicecatalogCloudformationprovisionedproduct


@dataclass
class ProvisioningParameter(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProvisioningParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProvisioningParameter"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProvisioningParameter = ProvisioningParameter


@dataclass
class ProvisioningPreferences(BaseModel):
    StackSetAccounts: Optional[Sequence[str]]
    StackSetFailureToleranceCount: Optional[int]
    StackSetFailureTolerancePercentage: Optional[int]
    StackSetMaxConcurrencyCount: Optional[int]
    StackSetMaxConcurrencyPercentage: Optional[int]
    StackSetOperationType: Optional[str]
    StackSetRegions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ProvisioningPreferences"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProvisioningPreferences"]:
        if not json_data:
            return None
        return cls(
            StackSetAccounts=json_data.get("StackSetAccounts"),
            StackSetFailureToleranceCount=json_data.get("StackSetFailureToleranceCount"),
            StackSetFailureTolerancePercentage=json_data.get("StackSetFailureTolerancePercentage"),
            StackSetMaxConcurrencyCount=json_data.get("StackSetMaxConcurrencyCount"),
            StackSetMaxConcurrencyPercentage=json_data.get("StackSetMaxConcurrencyPercentage"),
            StackSetOperationType=json_data.get("StackSetOperationType"),
            StackSetRegions=json_data.get("StackSetRegions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProvisioningPreferences = ProvisioningPreferences


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


