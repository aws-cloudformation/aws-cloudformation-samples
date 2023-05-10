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
class AwsConnectRule(BaseModel):
    Name: Optional[str]
    RuleArn: Optional[str]
    InstanceArn: Optional[str]
    TriggerEventSource: Optional["_RuleTriggerEventSource"]
    Function: Optional[str]
    Actions: Optional["_Actions"]
    PublishStatus: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConnectRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConnectRule"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            RuleArn=json_data.get("RuleArn"),
            InstanceArn=json_data.get("InstanceArn"),
            TriggerEventSource=RuleTriggerEventSource._deserialize(json_data.get("TriggerEventSource")),
            Function=json_data.get("Function"),
            Actions=Actions._deserialize(json_data.get("Actions")),
            PublishStatus=json_data.get("PublishStatus"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConnectRule = AwsConnectRule


@dataclass
class RuleTriggerEventSource(BaseModel):
    EventSourceName: Optional[str]
    IntegrationAssociationArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RuleTriggerEventSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleTriggerEventSource"]:
        if not json_data:
            return None
        return cls(
            EventSourceName=json_data.get("EventSourceName"),
            IntegrationAssociationArn=json_data.get("IntegrationAssociationArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleTriggerEventSource = RuleTriggerEventSource


@dataclass
class Actions(BaseModel):
    AssignContactCategoryActions: Optional[AbstractSet[MutableMapping[str, Any]]]
    EventBridgeActions: Optional[AbstractSet["_EventBridgeAction"]]
    TaskActions: Optional[AbstractSet["_TaskAction"]]
    SendNotificationActions: Optional[AbstractSet["_SendNotificationAction"]]

    @classmethod
    def _deserialize(
        cls: Type["_Actions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Actions"]:
        if not json_data:
            return None
        return cls(
            AssignContactCategoryActions=set_or_none(json_data.get("AssignContactCategoryActions")),
            EventBridgeActions=set_or_none(json_data.get("EventBridgeActions")),
            TaskActions=set_or_none(json_data.get("TaskActions")),
            SendNotificationActions=set_or_none(json_data.get("SendNotificationActions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Actions = Actions


@dataclass
class EventBridgeAction(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EventBridgeAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventBridgeAction"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventBridgeAction = EventBridgeAction


@dataclass
class TaskAction(BaseModel):
    Name: Optional[str]
    Description: Optional[str]
    ContactFlowArn: Optional[str]
    References: Optional[MutableMapping[str, "_Reference"]]

    @classmethod
    def _deserialize(
        cls: Type["_TaskAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskAction"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            ContactFlowArn=json_data.get("ContactFlowArn"),
            References=json_data.get("References"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskAction = TaskAction


@dataclass
class Reference(BaseModel):
    Value: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Reference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Reference"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Reference = Reference


@dataclass
class SendNotificationAction(BaseModel):
    DeliveryMethod: Optional[str]
    Subject: Optional[str]
    Content: Optional[str]
    ContentType: Optional[str]
    Recipient: Optional["_NotificationRecipientType"]

    @classmethod
    def _deserialize(
        cls: Type["_SendNotificationAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SendNotificationAction"]:
        if not json_data:
            return None
        return cls(
            DeliveryMethod=json_data.get("DeliveryMethod"),
            Subject=json_data.get("Subject"),
            Content=json_data.get("Content"),
            ContentType=json_data.get("ContentType"),
            Recipient=NotificationRecipientType._deserialize(json_data.get("Recipient")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SendNotificationAction = SendNotificationAction


@dataclass
class NotificationRecipientType(BaseModel):
    UserTags: Optional[MutableMapping[str, str]]
    UserArns: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationRecipientType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationRecipientType"]:
        if not json_data:
            return None
        return cls(
            UserTags=json_data.get("UserTags"),
            UserArns=set_or_none(json_data.get("UserArns")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationRecipientType = NotificationRecipientType


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


