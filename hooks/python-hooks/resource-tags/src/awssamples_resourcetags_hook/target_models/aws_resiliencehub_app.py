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
class AwsResiliencehubApp(BaseModel):
    Name: Optional[str]
    Description: Optional[str]
    AppArn: Optional[str]
    ResiliencyPolicyArn: Optional[str]
    Tags: Optional[Any]
    AppTemplateBody: Optional[str]
    ResourceMappings: Optional[Sequence["_ResourceMapping"]]
    AppAssessmentSchedule: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsResiliencehubApp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsResiliencehubApp"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            AppArn=json_data.get("AppArn"),
            ResiliencyPolicyArn=json_data.get("ResiliencyPolicyArn"),
            Tags=json_data.get("Tags"),
            AppTemplateBody=json_data.get("AppTemplateBody"),
            ResourceMappings=deserialize_list(json_data.get("ResourceMappings"), ResourceMapping),
            AppAssessmentSchedule=json_data.get("AppAssessmentSchedule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsResiliencehubApp = AwsResiliencehubApp


@dataclass
class ResourceMapping(BaseModel):
    LogicalStackName: Optional[str]
    MappingType: Optional[str]
    ResourceName: Optional[str]
    TerraformSourceName: Optional[str]
    EksSourceName: Optional[str]
    PhysicalResourceId: Optional["_PhysicalResourceId"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceMapping"]:
        if not json_data:
            return None
        return cls(
            LogicalStackName=json_data.get("LogicalStackName"),
            MappingType=json_data.get("MappingType"),
            ResourceName=json_data.get("ResourceName"),
            TerraformSourceName=json_data.get("TerraformSourceName"),
            EksSourceName=json_data.get("EksSourceName"),
            PhysicalResourceId=PhysicalResourceId._deserialize(json_data.get("PhysicalResourceId")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceMapping = ResourceMapping


@dataclass
class PhysicalResourceId(BaseModel):
    AwsAccountId: Optional[str]
    AwsRegion: Optional[str]
    Identifier: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PhysicalResourceId"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PhysicalResourceId"]:
        if not json_data:
            return None
        return cls(
            AwsAccountId=json_data.get("AwsAccountId"),
            AwsRegion=json_data.get("AwsRegion"),
            Identifier=json_data.get("Identifier"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PhysicalResourceId = PhysicalResourceId


