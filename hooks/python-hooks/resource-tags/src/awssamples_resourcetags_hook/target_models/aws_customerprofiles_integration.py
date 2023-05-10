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
class AwsCustomerprofilesIntegration(BaseModel):
    DomainName: Optional[str]
    Uri: Optional[str]
    FlowDefinition: Optional["_FlowDefinition"]
    ObjectTypeName: Optional[str]
    CreatedAt: Optional[str]
    LastUpdatedAt: Optional[str]
    Tags: Optional[Any]
    ObjectTypeNames: Optional[Sequence["_ObjectTypeMapping"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCustomerprofilesIntegration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCustomerprofilesIntegration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DomainName=json_data.get("DomainName"),
            Uri=json_data.get("Uri"),
            FlowDefinition=FlowDefinition._deserialize(json_data.get("FlowDefinition")),
            ObjectTypeName=json_data.get("ObjectTypeName"),
            CreatedAt=json_data.get("CreatedAt"),
            LastUpdatedAt=json_data.get("LastUpdatedAt"),
            Tags=json_data.get("Tags"),
            ObjectTypeNames=deserialize_list(json_data.get("ObjectTypeNames"), ObjectTypeMapping),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCustomerprofilesIntegration = AwsCustomerprofilesIntegration


@dataclass
class FlowDefinition(BaseModel):
    FlowName: Optional[str]
    Description: Optional[str]
    KmsArn: Optional[str]
    Tasks: Optional[Sequence["_Task"]]
    TriggerConfig: Optional["_TriggerConfig"]
    SourceFlowConfig: Optional["_SourceFlowConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_FlowDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FlowDefinition"]:
        if not json_data:
            return None
        return cls(
            FlowName=json_data.get("FlowName"),
            Description=json_data.get("Description"),
            KmsArn=json_data.get("KmsArn"),
            Tasks=deserialize_list(json_data.get("Tasks"), Task),
            TriggerConfig=TriggerConfig._deserialize(json_data.get("TriggerConfig")),
            SourceFlowConfig=SourceFlowConfig._deserialize(json_data.get("SourceFlowConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FlowDefinition = FlowDefinition


@dataclass
class Task(BaseModel):
    ConnectorOperator: Optional["_ConnectorOperator"]
    SourceFields: Optional[Sequence[str]]
    DestinationField: Optional[str]
    TaskType: Optional[str]
    TaskProperties: Optional[Sequence["_TaskPropertiesMap"]]

    @classmethod
    def _deserialize(
        cls: Type["_Task"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Task"]:
        if not json_data:
            return None
        return cls(
            ConnectorOperator=ConnectorOperator._deserialize(json_data.get("ConnectorOperator")),
            SourceFields=json_data.get("SourceFields"),
            DestinationField=json_data.get("DestinationField"),
            TaskType=json_data.get("TaskType"),
            TaskProperties=deserialize_list(json_data.get("TaskProperties"), TaskPropertiesMap),
        )


# work around possible type aliasing issues when variable has same name as a model
_Task = Task


@dataclass
class ConnectorOperator(BaseModel):
    Marketo: Optional[str]
    S3: Optional[str]
    Salesforce: Optional[str]
    ServiceNow: Optional[str]
    Zendesk: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectorOperator"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectorOperator"]:
        if not json_data:
            return None
        return cls(
            Marketo=json_data.get("Marketo"),
            S3=json_data.get("S3"),
            Salesforce=json_data.get("Salesforce"),
            ServiceNow=json_data.get("ServiceNow"),
            Zendesk=json_data.get("Zendesk"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectorOperator = ConnectorOperator


@dataclass
class TaskPropertiesMap(BaseModel):
    OperatorPropertyKey: Optional[str]
    Property: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaskPropertiesMap"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskPropertiesMap"]:
        if not json_data:
            return None
        return cls(
            OperatorPropertyKey=json_data.get("OperatorPropertyKey"),
            Property=json_data.get("Property"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskPropertiesMap = TaskPropertiesMap


@dataclass
class TriggerConfig(BaseModel):
    TriggerType: Optional[str]
    TriggerProperties: Optional["_TriggerProperties"]

    @classmethod
    def _deserialize(
        cls: Type["_TriggerConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TriggerConfig"]:
        if not json_data:
            return None
        return cls(
            TriggerType=json_data.get("TriggerType"),
            TriggerProperties=TriggerProperties._deserialize(json_data.get("TriggerProperties")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TriggerConfig = TriggerConfig


@dataclass
class TriggerProperties(BaseModel):
    Scheduled: Optional["_ScheduledTriggerProperties"]

    @classmethod
    def _deserialize(
        cls: Type["_TriggerProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TriggerProperties"]:
        if not json_data:
            return None
        return cls(
            Scheduled=ScheduledTriggerProperties._deserialize(json_data.get("Scheduled")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TriggerProperties = TriggerProperties


@dataclass
class ScheduledTriggerProperties(BaseModel):
    ScheduleExpression: Optional[str]
    DataPullMode: Optional[str]
    ScheduleStartTime: Optional[float]
    ScheduleEndTime: Optional[float]
    Timezone: Optional[str]
    ScheduleOffset: Optional[int]
    FirstExecutionFrom: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduledTriggerProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduledTriggerProperties"]:
        if not json_data:
            return None
        return cls(
            ScheduleExpression=json_data.get("ScheduleExpression"),
            DataPullMode=json_data.get("DataPullMode"),
            ScheduleStartTime=json_data.get("ScheduleStartTime"),
            ScheduleEndTime=json_data.get("ScheduleEndTime"),
            Timezone=json_data.get("Timezone"),
            ScheduleOffset=json_data.get("ScheduleOffset"),
            FirstExecutionFrom=json_data.get("FirstExecutionFrom"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduledTriggerProperties = ScheduledTriggerProperties


@dataclass
class SourceFlowConfig(BaseModel):
    ConnectorType: Optional[str]
    ConnectorProfileName: Optional[str]
    IncrementalPullConfig: Optional["_IncrementalPullConfig"]
    SourceConnectorProperties: Optional["_SourceConnectorProperties"]

    @classmethod
    def _deserialize(
        cls: Type["_SourceFlowConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceFlowConfig"]:
        if not json_data:
            return None
        return cls(
            ConnectorType=json_data.get("ConnectorType"),
            ConnectorProfileName=json_data.get("ConnectorProfileName"),
            IncrementalPullConfig=IncrementalPullConfig._deserialize(json_data.get("IncrementalPullConfig")),
            SourceConnectorProperties=SourceConnectorProperties._deserialize(json_data.get("SourceConnectorProperties")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceFlowConfig = SourceFlowConfig


@dataclass
class IncrementalPullConfig(BaseModel):
    DatetimeTypeFieldName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IncrementalPullConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IncrementalPullConfig"]:
        if not json_data:
            return None
        return cls(
            DatetimeTypeFieldName=json_data.get("DatetimeTypeFieldName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IncrementalPullConfig = IncrementalPullConfig


@dataclass
class SourceConnectorProperties(BaseModel):
    Marketo: Optional["_MarketoSourceProperties"]
    S3: Optional["_S3SourceProperties"]
    Salesforce: Optional["_SalesforceSourceProperties"]
    ServiceNow: Optional["_ServiceNowSourceProperties"]
    Zendesk: Optional["_ZendeskSourceProperties"]

    @classmethod
    def _deserialize(
        cls: Type["_SourceConnectorProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceConnectorProperties"]:
        if not json_data:
            return None
        return cls(
            Marketo=MarketoSourceProperties._deserialize(json_data.get("Marketo")),
            S3=S3SourceProperties._deserialize(json_data.get("S3")),
            Salesforce=SalesforceSourceProperties._deserialize(json_data.get("Salesforce")),
            ServiceNow=ServiceNowSourceProperties._deserialize(json_data.get("ServiceNow")),
            Zendesk=ZendeskSourceProperties._deserialize(json_data.get("Zendesk")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceConnectorProperties = SourceConnectorProperties


@dataclass
class MarketoSourceProperties(BaseModel):
    Object: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MarketoSourceProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarketoSourceProperties"]:
        if not json_data:
            return None
        return cls(
            Object=json_data.get("Object"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarketoSourceProperties = MarketoSourceProperties


@dataclass
class S3SourceProperties(BaseModel):
    BucketName: Optional[str]
    BucketPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3SourceProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3SourceProperties"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            BucketPrefix=json_data.get("BucketPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3SourceProperties = S3SourceProperties


@dataclass
class SalesforceSourceProperties(BaseModel):
    Object: Optional[str]
    EnableDynamicFieldUpdate: Optional[bool]
    IncludeDeletedRecords: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SalesforceSourceProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SalesforceSourceProperties"]:
        if not json_data:
            return None
        return cls(
            Object=json_data.get("Object"),
            EnableDynamicFieldUpdate=json_data.get("EnableDynamicFieldUpdate"),
            IncludeDeletedRecords=json_data.get("IncludeDeletedRecords"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SalesforceSourceProperties = SalesforceSourceProperties


@dataclass
class ServiceNowSourceProperties(BaseModel):
    Object: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceNowSourceProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceNowSourceProperties"]:
        if not json_data:
            return None
        return cls(
            Object=json_data.get("Object"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceNowSourceProperties = ServiceNowSourceProperties


@dataclass
class ZendeskSourceProperties(BaseModel):
    Object: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ZendeskSourceProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZendeskSourceProperties"]:
        if not json_data:
            return None
        return cls(
            Object=json_data.get("Object"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZendeskSourceProperties = ZendeskSourceProperties


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
class ObjectTypeMapping(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ObjectTypeMapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObjectTypeMapping"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObjectTypeMapping = ObjectTypeMapping


