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
class AwsSsmincidentsResponseplan(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    DisplayName: Optional[str]
    ChatChannel: Optional["_ChatChannel"]
    Engagements: Optional[AbstractSet[str]]
    Actions: Optional[Sequence["_Action"]]
    Integrations: Optional[Sequence["_Integration"]]
    Tags: Optional[Any]
    IncidentTemplate: Optional["_IncidentTemplate"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSsmincidentsResponseplan"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSsmincidentsResponseplan"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            DisplayName=json_data.get("DisplayName"),
            ChatChannel=ChatChannel._deserialize(json_data.get("ChatChannel")),
            Engagements=set_or_none(json_data.get("Engagements")),
            Actions=deserialize_list(json_data.get("Actions"), Action),
            Integrations=deserialize_list(json_data.get("Integrations"), Integration),
            Tags=json_data.get("Tags"),
            IncidentTemplate=IncidentTemplate._deserialize(json_data.get("IncidentTemplate")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSsmincidentsResponseplan = AwsSsmincidentsResponseplan


@dataclass
class ChatChannel(BaseModel):
    ChatbotSns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ChatChannel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChatChannel"]:
        if not json_data:
            return None
        return cls(
            ChatbotSns=json_data.get("ChatbotSns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChatChannel = ChatChannel


@dataclass
class Action(BaseModel):
    SsmAutomation: Optional["_SsmAutomation"]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            SsmAutomation=SsmAutomation._deserialize(json_data.get("SsmAutomation")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class SsmAutomation(BaseModel):
    RoleArn: Optional[str]
    DocumentName: Optional[str]
    DocumentVersion: Optional[str]
    TargetAccount: Optional[str]
    Parameters: Optional[AbstractSet["_SsmParameter"]]
    DynamicParameters: Optional[AbstractSet["_DynamicSsmParameter"]]

    @classmethod
    def _deserialize(
        cls: Type["_SsmAutomation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SsmAutomation"]:
        if not json_data:
            return None
        return cls(
            RoleArn=json_data.get("RoleArn"),
            DocumentName=json_data.get("DocumentName"),
            DocumentVersion=json_data.get("DocumentVersion"),
            TargetAccount=json_data.get("TargetAccount"),
            Parameters=set_or_none(json_data.get("Parameters")),
            DynamicParameters=set_or_none(json_data.get("DynamicParameters")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SsmAutomation = SsmAutomation


@dataclass
class SsmParameter(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SsmParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SsmParameter"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SsmParameter = SsmParameter


@dataclass
class DynamicSsmParameter(BaseModel):
    Key: Optional[str]
    Value: Optional["_DynamicSsmParameterValue"]

    @classmethod
    def _deserialize(
        cls: Type["_DynamicSsmParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamicSsmParameter"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=DynamicSsmParameterValue._deserialize(json_data.get("Value")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamicSsmParameter = DynamicSsmParameter


@dataclass
class DynamicSsmParameterValue(BaseModel):
    Variable: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DynamicSsmParameterValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamicSsmParameterValue"]:
        if not json_data:
            return None
        return cls(
            Variable=json_data.get("Variable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamicSsmParameterValue = DynamicSsmParameterValue


@dataclass
class Integration(BaseModel):
    PagerDutyConfiguration: Optional["_PagerDutyConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_Integration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Integration"]:
        if not json_data:
            return None
        return cls(
            PagerDutyConfiguration=PagerDutyConfiguration._deserialize(json_data.get("PagerDutyConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Integration = Integration


@dataclass
class PagerDutyConfiguration(BaseModel):
    Name: Optional[str]
    SecretId: Optional[str]
    PagerDutyIncidentConfiguration: Optional["_PagerDutyIncidentConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_PagerDutyConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PagerDutyConfiguration"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            SecretId=json_data.get("SecretId"),
            PagerDutyIncidentConfiguration=PagerDutyIncidentConfiguration._deserialize(json_data.get("PagerDutyIncidentConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_PagerDutyConfiguration = PagerDutyConfiguration


@dataclass
class PagerDutyIncidentConfiguration(BaseModel):
    ServiceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PagerDutyIncidentConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PagerDutyIncidentConfiguration"]:
        if not json_data:
            return None
        return cls(
            ServiceId=json_data.get("ServiceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PagerDutyIncidentConfiguration = PagerDutyIncidentConfiguration


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
class IncidentTemplate(BaseModel):
    DedupeString: Optional[str]
    Impact: Optional[int]
    NotificationTargets: Optional[Sequence["_NotificationTargetItem"]]
    Summary: Optional[str]
    Title: Optional[str]
    IncidentTags: Optional[AbstractSet["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_IncidentTemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IncidentTemplate"]:
        if not json_data:
            return None
        return cls(
            DedupeString=json_data.get("DedupeString"),
            Impact=json_data.get("Impact"),
            NotificationTargets=deserialize_list(json_data.get("NotificationTargets"), NotificationTargetItem),
            Summary=json_data.get("Summary"),
            Title=json_data.get("Title"),
            IncidentTags=set_or_none(json_data.get("IncidentTags")),
        )


# work around possible type aliasing issues when variable has same name as a model
_IncidentTemplate = IncidentTemplate


@dataclass
class NotificationTargetItem(BaseModel):
    SnsTopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationTargetItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationTargetItem"]:
        if not json_data:
            return None
        return cls(
            SnsTopicArn=json_data.get("SnsTopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationTargetItem = NotificationTargetItem


