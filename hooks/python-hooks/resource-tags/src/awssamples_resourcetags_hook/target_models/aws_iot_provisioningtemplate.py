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
class AwsIotProvisioningtemplate(BaseModel):
    TemplateArn: Optional[str]
    TemplateName: Optional[str]
    Description: Optional[str]
    Enabled: Optional[bool]
    ProvisioningRoleArn: Optional[str]
    TemplateBody: Optional[str]
    TemplateType: Optional[str]
    PreProvisioningHook: Optional["_ProvisioningHook"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotProvisioningtemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotProvisioningtemplate"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            TemplateArn=json_data.get("TemplateArn"),
            TemplateName=json_data.get("TemplateName"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            ProvisioningRoleArn=json_data.get("ProvisioningRoleArn"),
            TemplateBody=json_data.get("TemplateBody"),
            TemplateType=json_data.get("TemplateType"),
            PreProvisioningHook=ProvisioningHook._deserialize(json_data.get("PreProvisioningHook")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotProvisioningtemplate = AwsIotProvisioningtemplate


@dataclass
class ProvisioningHook(BaseModel):
    TargetArn: Optional[str]
    PayloadVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProvisioningHook"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProvisioningHook"]:
        if not json_data:
            return None
        return cls(
            TargetArn=json_data.get("TargetArn"),
            PayloadVersion=json_data.get("PayloadVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProvisioningHook = ProvisioningHook


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


