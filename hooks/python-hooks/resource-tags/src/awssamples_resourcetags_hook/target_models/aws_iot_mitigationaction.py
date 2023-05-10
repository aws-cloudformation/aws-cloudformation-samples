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
class AwsIotMitigationaction(BaseModel):
    ActionName: Optional[str]
    RoleArn: Optional[str]
    Tags: Optional[Any]
    ActionParams: Optional["_ActionParams"]
    MitigationActionArn: Optional[str]
    MitigationActionId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotMitigationaction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotMitigationaction"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ActionName=json_data.get("ActionName"),
            RoleArn=json_data.get("RoleArn"),
            Tags=json_data.get("Tags"),
            ActionParams=ActionParams._deserialize(json_data.get("ActionParams")),
            MitigationActionArn=json_data.get("MitigationActionArn"),
            MitigationActionId=json_data.get("MitigationActionId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotMitigationaction = AwsIotMitigationaction


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
class ActionParams(BaseModel):
    AddThingsToThingGroupParams: Optional["_AddThingsToThingGroupParams"]
    EnableIoTLoggingParams: Optional["_EnableIoTLoggingParams"]
    PublishFindingToSnsParams: Optional["_PublishFindingToSnsParams"]
    ReplaceDefaultPolicyVersionParams: Optional["_ReplaceDefaultPolicyVersionParams"]
    UpdateCACertificateParams: Optional["_UpdateCACertificateParams"]
    UpdateDeviceCertificateParams: Optional["_UpdateDeviceCertificateParams"]

    @classmethod
    def _deserialize(
        cls: Type["_ActionParams"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionParams"]:
        if not json_data:
            return None
        return cls(
            AddThingsToThingGroupParams=AddThingsToThingGroupParams._deserialize(json_data.get("AddThingsToThingGroupParams")),
            EnableIoTLoggingParams=EnableIoTLoggingParams._deserialize(json_data.get("EnableIoTLoggingParams")),
            PublishFindingToSnsParams=PublishFindingToSnsParams._deserialize(json_data.get("PublishFindingToSnsParams")),
            ReplaceDefaultPolicyVersionParams=ReplaceDefaultPolicyVersionParams._deserialize(json_data.get("ReplaceDefaultPolicyVersionParams")),
            UpdateCACertificateParams=UpdateCACertificateParams._deserialize(json_data.get("UpdateCACertificateParams")),
            UpdateDeviceCertificateParams=UpdateDeviceCertificateParams._deserialize(json_data.get("UpdateDeviceCertificateParams")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionParams = ActionParams


@dataclass
class AddThingsToThingGroupParams(BaseModel):
    OverrideDynamicGroups: Optional[bool]
    ThingGroupNames: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AddThingsToThingGroupParams"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddThingsToThingGroupParams"]:
        if not json_data:
            return None
        return cls(
            OverrideDynamicGroups=json_data.get("OverrideDynamicGroups"),
            ThingGroupNames=set_or_none(json_data.get("ThingGroupNames")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddThingsToThingGroupParams = AddThingsToThingGroupParams


@dataclass
class EnableIoTLoggingParams(BaseModel):
    LogLevel: Optional[str]
    RoleArnForLogging: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnableIoTLoggingParams"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnableIoTLoggingParams"]:
        if not json_data:
            return None
        return cls(
            LogLevel=json_data.get("LogLevel"),
            RoleArnForLogging=json_data.get("RoleArnForLogging"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnableIoTLoggingParams = EnableIoTLoggingParams


@dataclass
class PublishFindingToSnsParams(BaseModel):
    TopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublishFindingToSnsParams"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublishFindingToSnsParams"]:
        if not json_data:
            return None
        return cls(
            TopicArn=json_data.get("TopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublishFindingToSnsParams = PublishFindingToSnsParams


@dataclass
class ReplaceDefaultPolicyVersionParams(BaseModel):
    TemplateName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReplaceDefaultPolicyVersionParams"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplaceDefaultPolicyVersionParams"]:
        if not json_data:
            return None
        return cls(
            TemplateName=json_data.get("TemplateName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplaceDefaultPolicyVersionParams = ReplaceDefaultPolicyVersionParams


@dataclass
class UpdateCACertificateParams(BaseModel):
    Action: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UpdateCACertificateParams"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpdateCACertificateParams"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpdateCACertificateParams = UpdateCACertificateParams


@dataclass
class UpdateDeviceCertificateParams(BaseModel):
    Action: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UpdateDeviceCertificateParams"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpdateDeviceCertificateParams"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpdateDeviceCertificateParams = UpdateDeviceCertificateParams


