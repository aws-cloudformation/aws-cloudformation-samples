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
class AwsSagemakerProject(BaseModel):
    Tags: Optional[Any]
    ProjectArn: Optional[str]
    ProjectId: Optional[str]
    ProjectName: Optional[str]
    ProjectDescription: Optional[str]
    CreationTime: Optional[str]
    ServiceCatalogProvisioningDetails: Optional["_ServiceCatalogProvisioningDetails"]
    ServiceCatalogProvisionedProductDetails: Optional["_ServiceCatalogProvisionedProductDetails"]
    ProjectStatus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSagemakerProject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSagemakerProject"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Tags=json_data.get("Tags"),
            ProjectArn=json_data.get("ProjectArn"),
            ProjectId=json_data.get("ProjectId"),
            ProjectName=json_data.get("ProjectName"),
            ProjectDescription=json_data.get("ProjectDescription"),
            CreationTime=json_data.get("CreationTime"),
            ServiceCatalogProvisioningDetails=ServiceCatalogProvisioningDetails._deserialize(json_data.get("ServiceCatalogProvisioningDetails")),
            ServiceCatalogProvisionedProductDetails=ServiceCatalogProvisionedProductDetails._deserialize(json_data.get("ServiceCatalogProvisionedProductDetails")),
            ProjectStatus=json_data.get("ProjectStatus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSagemakerProject = AwsSagemakerProject


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
class ServiceCatalogProvisioningDetails(BaseModel):
    ProductId: Optional[str]
    ProvisioningArtifactId: Optional[str]
    PathId: Optional[str]
    ProvisioningParameters: Optional[Sequence["_ProvisioningParameter"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceCatalogProvisioningDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceCatalogProvisioningDetails"]:
        if not json_data:
            return None
        return cls(
            ProductId=json_data.get("ProductId"),
            ProvisioningArtifactId=json_data.get("ProvisioningArtifactId"),
            PathId=json_data.get("PathId"),
            ProvisioningParameters=deserialize_list(json_data.get("ProvisioningParameters"), ProvisioningParameter),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceCatalogProvisioningDetails = ServiceCatalogProvisioningDetails


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
class ServiceCatalogProvisionedProductDetails(BaseModel):
    ProvisionedProductId: Optional[str]
    ProvisionedProductStatusMessage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceCatalogProvisionedProductDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceCatalogProvisionedProductDetails"]:
        if not json_data:
            return None
        return cls(
            ProvisionedProductId=json_data.get("ProvisionedProductId"),
            ProvisionedProductStatusMessage=json_data.get("ProvisionedProductStatusMessage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceCatalogProvisionedProductDetails = ServiceCatalogProvisionedProductDetails


