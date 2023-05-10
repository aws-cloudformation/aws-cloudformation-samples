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
class AwsGlueTrigger(BaseModel):
    Type: Optional[str]
    StartOnCreation: Optional[bool]
    Description: Optional[str]
    Actions: Optional[Sequence["_Action"]]
    EventBatchingCondition: Optional["_EventBatchingCondition"]
    WorkflowName: Optional[str]
    Schedule: Optional[str]
    Id: Optional[str]
    Tags: Optional[Any]
    Name: Optional[str]
    Predicate: Optional["_Predicate"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGlueTrigger"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGlueTrigger"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Type=json_data.get("Type"),
            StartOnCreation=json_data.get("StartOnCreation"),
            Description=json_data.get("Description"),
            Actions=deserialize_list(json_data.get("Actions"), Action),
            EventBatchingCondition=EventBatchingCondition._deserialize(json_data.get("EventBatchingCondition")),
            WorkflowName=json_data.get("WorkflowName"),
            Schedule=json_data.get("Schedule"),
            Id=json_data.get("Id"),
            Tags=json_data.get("Tags"),
            Name=json_data.get("Name"),
            Predicate=Predicate._deserialize(json_data.get("Predicate")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGlueTrigger = AwsGlueTrigger


@dataclass
class Action(BaseModel):
    NotificationProperty: Optional["_NotificationProperty"]
    CrawlerName: Optional[str]
    Timeout: Optional[int]
    JobName: Optional[str]
    Arguments: Optional[MutableMapping[str, Any]]
    SecurityConfiguration: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            NotificationProperty=NotificationProperty._deserialize(json_data.get("NotificationProperty")),
            CrawlerName=json_data.get("CrawlerName"),
            Timeout=json_data.get("Timeout"),
            JobName=json_data.get("JobName"),
            Arguments=json_data.get("Arguments"),
            SecurityConfiguration=json_data.get("SecurityConfiguration"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class NotificationProperty(BaseModel):
    NotifyDelayAfter: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationProperty"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationProperty"]:
        if not json_data:
            return None
        return cls(
            NotifyDelayAfter=json_data.get("NotifyDelayAfter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationProperty = NotificationProperty


@dataclass
class EventBatchingCondition(BaseModel):
    BatchSize: Optional[int]
    BatchWindow: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_EventBatchingCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventBatchingCondition"]:
        if not json_data:
            return None
        return cls(
            BatchSize=json_data.get("BatchSize"),
            BatchWindow=json_data.get("BatchWindow"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventBatchingCondition = EventBatchingCondition


@dataclass
class Predicate(BaseModel):
    Logical: Optional[str]
    Conditions: Optional[Sequence["_Condition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Predicate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Predicate"]:
        if not json_data:
            return None
        return cls(
            Logical=json_data.get("Logical"),
            Conditions=deserialize_list(json_data.get("Conditions"), Condition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Predicate = Predicate


@dataclass
class Condition(BaseModel):
    JobName: Optional[str]
    CrawlerName: Optional[str]
    State: Optional[str]
    CrawlState: Optional[str]
    LogicalOperator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Condition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Condition"]:
        if not json_data:
            return None
        return cls(
            JobName=json_data.get("JobName"),
            CrawlerName=json_data.get("CrawlerName"),
            State=json_data.get("State"),
            CrawlState=json_data.get("CrawlState"),
            LogicalOperator=json_data.get("LogicalOperator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Condition = Condition


