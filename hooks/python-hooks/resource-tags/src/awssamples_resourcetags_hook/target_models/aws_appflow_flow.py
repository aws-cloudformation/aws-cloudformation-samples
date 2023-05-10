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
class AwsAppflowFlow(BaseModel):
    FlowArn: Optional[str]
    FlowName: Optional[str]
    Description: Optional[str]
    KMSArn: Optional[str]
    TriggerConfig: Optional["_TriggerConfig"]
    SourceFlowConfig: Optional["_SourceFlowConfig"]
    DestinationFlowConfigList: Optional[Sequence["_DestinationFlowConfig"]]
    Tasks: Optional[Sequence["_Task"]]
    Tags: Optional[Any]
    MetadataCatalogConfig: Optional["_MetadataCatalogConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppflowFlow"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppflowFlow"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            FlowArn=json_data.get("FlowArn"),
            FlowName=json_data.get("FlowName"),
            Description=json_data.get("Description"),
            KMSArn=json_data.get("KMSArn"),
            TriggerConfig=TriggerConfig._deserialize(json_data.get("TriggerConfig")),
            SourceFlowConfig=SourceFlowConfig._deserialize(json_data.get("SourceFlowConfig")),
            DestinationFlowConfigList=deserialize_list(json_data.get("DestinationFlowConfigList"), DestinationFlowConfig),
            Tasks=deserialize_list(json_data.get("Tasks"), Task),
            Tags=json_data.get("Tags"),
            MetadataCatalogConfig=MetadataCatalogConfig._deserialize(json_data.get("MetadataCatalogConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppflowFlow = AwsAppflowFlow


@dataclass
class TriggerConfig(BaseModel):
    TriggerType: Optional[str]
    TriggerProperties: Optional["_ScheduledTriggerProperties"]
    ActivateFlowOnCreate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TriggerConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TriggerConfig"]:
        if not json_data:
            return None
        return cls(
            TriggerType=json_data.get("TriggerType"),
            TriggerProperties=ScheduledTriggerProperties._deserialize(json_data.get("TriggerProperties")),
            ActivateFlowOnCreate=json_data.get("ActivateFlowOnCreate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TriggerConfig = TriggerConfig


@dataclass
class ScheduledTriggerProperties(BaseModel):
    ScheduleExpression: Optional[str]
    DataPullMode: Optional[str]
    ScheduleStartTime: Optional[float]
    ScheduleEndTime: Optional[float]
    FirstExecutionFrom: Optional[float]
    TimeZone: Optional[str]
    ScheduleOffset: Optional[float]
    FlowErrorDeactivationThreshold: Optional[int]

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
            FirstExecutionFrom=json_data.get("FirstExecutionFrom"),
            TimeZone=json_data.get("TimeZone"),
            ScheduleOffset=json_data.get("ScheduleOffset"),
            FlowErrorDeactivationThreshold=json_data.get("FlowErrorDeactivationThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduledTriggerProperties = ScheduledTriggerProperties


@dataclass
class SourceFlowConfig(BaseModel):
    ConnectorType: Optional[str]
    ApiVersion: Optional[str]
    ConnectorProfileName: Optional[str]
    SourceConnectorProperties: Optional["_SourceConnectorProperties"]
    IncrementalPullConfig: Optional["_IncrementalPullConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_SourceFlowConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceFlowConfig"]:
        if not json_data:
            return None
        return cls(
            ConnectorType=json_data.get("ConnectorType"),
            ApiVersion=json_data.get("ApiVersion"),
            ConnectorProfileName=json_data.get("ConnectorProfileName"),
            SourceConnectorProperties=SourceConnectorProperties._deserialize(json_data.get("SourceConnectorProperties")),
            IncrementalPullConfig=IncrementalPullConfig._deserialize(json_data.get("IncrementalPullConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceFlowConfig = SourceFlowConfig


@dataclass
class SourceConnectorProperties(BaseModel):
    Amplitude: Optional["_AmplitudeSourceProperties"]
    Datadog: Optional["_DatadogSourceProperties"]
    Dynatrace: Optional["_DynatraceSourceProperties"]
    GoogleAnalytics: Optional["_GoogleAnalyticsSourceProperties"]
    InforNexus: Optional["_InforNexusSourceProperties"]
    Marketo: Optional["_MarketoSourceProperties"]
    S3: Optional["_S3SourceProperties"]
    SAPOData: Optional["_SAPODataSourceProperties"]
    Salesforce: Optional["_SalesforceSourceProperties"]
    Pardot: Optional["_PardotSourceProperties"]
    ServiceNow: Optional["_ServiceNowSourceProperties"]
    Singular: Optional["_SingularSourceProperties"]
    Slack: Optional["_SlackSourceProperties"]
    Trendmicro: Optional["_TrendmicroSourceProperties"]
    Veeva: Optional["_VeevaSourceProperties"]
    Zendesk: Optional["_ZendeskSourceProperties"]
    CustomConnector: Optional["_CustomConnectorSourceProperties"]

    @classmethod
    def _deserialize(
        cls: Type["_SourceConnectorProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceConnectorProperties"]:
        if not json_data:
            return None
        return cls(
            Amplitude=AmplitudeSourceProperties._deserialize(json_data.get("Amplitude")),
            Datadog=DatadogSourceProperties._deserialize(json_data.get("Datadog")),
            Dynatrace=DynatraceSourceProperties._deserialize(json_data.get("Dynatrace")),
            GoogleAnalytics=GoogleAnalyticsSourceProperties._deserialize(json_data.get("GoogleAnalytics")),
            InforNexus=InforNexusSourceProperties._deserialize(json_data.get("InforNexus")),
            Marketo=MarketoSourceProperties._deserialize(json_data.get("Marketo")),
            S3=S3SourceProperties._deserialize(json_data.get("S3")),
            SAPOData=SAPODataSourceProperties._deserialize(json_data.get("SAPOData")),
            Salesforce=SalesforceSourceProperties._deserialize(json_data.get("Salesforce")),
            Pardot=PardotSourceProperties._deserialize(json_data.get("Pardot")),
            ServiceNow=ServiceNowSourceProperties._deserialize(json_data.get("ServiceNow")),
            Singular=SingularSourceProperties._deserialize(json_data.get("Singular")),
            Slack=SlackSourceProperties._deserialize(json_data.get("Slack")),
            Trendmicro=TrendmicroSourceProperties._deserialize(json_data.get("Trendmicro")),
            Veeva=VeevaSourceProperties._deserialize(json_data.get("Veeva")),
            Zendesk=ZendeskSourceProperties._deserialize(json_data.get("Zendesk")),
            CustomConnector=CustomConnectorSourceProperties._deserialize(json_data.get("CustomConnector")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceConnectorProperties = SourceConnectorProperties


@dataclass
class AmplitudeSourceProperties(BaseModel):
    Object: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AmplitudeSourceProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AmplitudeSourceProperties"]:
        if not json_data:
            return None
        return cls(
            Object=json_data.get("Object"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AmplitudeSourceProperties = AmplitudeSourceProperties


@dataclass
class DatadogSourceProperties(BaseModel):
    Object: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatadogSourceProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatadogSourceProperties"]:
        if not json_data:
            return None
        return cls(
            Object=json_data.get("Object"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatadogSourceProperties = DatadogSourceProperties


@dataclass
class DynatraceSourceProperties(BaseModel):
    Object: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DynatraceSourceProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynatraceSourceProperties"]:
        if not json_data:
            return None
        return cls(
            Object=json_data.get("Object"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynatraceSourceProperties = DynatraceSourceProperties


@dataclass
class GoogleAnalyticsSourceProperties(BaseModel):
    Object: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GoogleAnalyticsSourceProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GoogleAnalyticsSourceProperties"]:
        if not json_data:
            return None
        return cls(
            Object=json_data.get("Object"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GoogleAnalyticsSourceProperties = GoogleAnalyticsSourceProperties


@dataclass
class InforNexusSourceProperties(BaseModel):
    Object: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InforNexusSourceProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InforNexusSourceProperties"]:
        if not json_data:
            return None
        return cls(
            Object=json_data.get("Object"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InforNexusSourceProperties = InforNexusSourceProperties


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
    S3InputFormatConfig: Optional["_S3InputFormatConfig"]

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
            S3InputFormatConfig=S3InputFormatConfig._deserialize(json_data.get("S3InputFormatConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3SourceProperties = S3SourceProperties


@dataclass
class S3InputFormatConfig(BaseModel):
    S3InputFileType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3InputFormatConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3InputFormatConfig"]:
        if not json_data:
            return None
        return cls(
            S3InputFileType=json_data.get("S3InputFileType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3InputFormatConfig = S3InputFormatConfig


@dataclass
class SAPODataSourceProperties(BaseModel):
    ObjectPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SAPODataSourceProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SAPODataSourceProperties"]:
        if not json_data:
            return None
        return cls(
            ObjectPath=json_data.get("ObjectPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SAPODataSourceProperties = SAPODataSourceProperties


@dataclass
class SalesforceSourceProperties(BaseModel):
    Object: Optional[str]
    EnableDynamicFieldUpdate: Optional[bool]
    IncludeDeletedRecords: Optional[bool]
    DataTransferApi: Optional[str]

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
            DataTransferApi=json_data.get("DataTransferApi"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SalesforceSourceProperties = SalesforceSourceProperties


@dataclass
class PardotSourceProperties(BaseModel):
    Object: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PardotSourceProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PardotSourceProperties"]:
        if not json_data:
            return None
        return cls(
            Object=json_data.get("Object"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PardotSourceProperties = PardotSourceProperties


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
class SingularSourceProperties(BaseModel):
    Object: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SingularSourceProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SingularSourceProperties"]:
        if not json_data:
            return None
        return cls(
            Object=json_data.get("Object"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SingularSourceProperties = SingularSourceProperties


@dataclass
class SlackSourceProperties(BaseModel):
    Object: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SlackSourceProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlackSourceProperties"]:
        if not json_data:
            return None
        return cls(
            Object=json_data.get("Object"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlackSourceProperties = SlackSourceProperties


@dataclass
class TrendmicroSourceProperties(BaseModel):
    Object: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrendmicroSourceProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrendmicroSourceProperties"]:
        if not json_data:
            return None
        return cls(
            Object=json_data.get("Object"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrendmicroSourceProperties = TrendmicroSourceProperties


@dataclass
class VeevaSourceProperties(BaseModel):
    Object: Optional[str]
    DocumentType: Optional[str]
    IncludeSourceFiles: Optional[bool]
    IncludeRenditions: Optional[bool]
    IncludeAllVersions: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_VeevaSourceProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VeevaSourceProperties"]:
        if not json_data:
            return None
        return cls(
            Object=json_data.get("Object"),
            DocumentType=json_data.get("DocumentType"),
            IncludeSourceFiles=json_data.get("IncludeSourceFiles"),
            IncludeRenditions=json_data.get("IncludeRenditions"),
            IncludeAllVersions=json_data.get("IncludeAllVersions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VeevaSourceProperties = VeevaSourceProperties


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
class CustomConnectorSourceProperties(BaseModel):
    EntityName: Optional[str]
    CustomProperties: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomConnectorSourceProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomConnectorSourceProperties"]:
        if not json_data:
            return None
        return cls(
            EntityName=json_data.get("EntityName"),
            CustomProperties=json_data.get("CustomProperties"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomConnectorSourceProperties = CustomConnectorSourceProperties


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
class DestinationFlowConfig(BaseModel):
    ConnectorType: Optional[str]
    ApiVersion: Optional[str]
    ConnectorProfileName: Optional[str]
    DestinationConnectorProperties: Optional["_DestinationConnectorProperties"]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationFlowConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationFlowConfig"]:
        if not json_data:
            return None
        return cls(
            ConnectorType=json_data.get("ConnectorType"),
            ApiVersion=json_data.get("ApiVersion"),
            ConnectorProfileName=json_data.get("ConnectorProfileName"),
            DestinationConnectorProperties=DestinationConnectorProperties._deserialize(json_data.get("DestinationConnectorProperties")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationFlowConfig = DestinationFlowConfig


@dataclass
class DestinationConnectorProperties(BaseModel):
    Redshift: Optional["_RedshiftDestinationProperties"]
    S3: Optional["_S3DestinationProperties"]
    Salesforce: Optional["_SalesforceDestinationProperties"]
    Snowflake: Optional["_SnowflakeDestinationProperties"]
    EventBridge: Optional["_EventBridgeDestinationProperties"]
    Upsolver: Optional["_UpsolverDestinationProperties"]
    LookoutMetrics: Optional["_LookoutMetricsDestinationProperties"]
    Marketo: Optional["_MarketoDestinationProperties"]
    Zendesk: Optional["_ZendeskDestinationProperties"]
    CustomConnector: Optional["_CustomConnectorDestinationProperties"]
    SAPOData: Optional["_SAPODataDestinationProperties"]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationConnectorProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationConnectorProperties"]:
        if not json_data:
            return None
        return cls(
            Redshift=RedshiftDestinationProperties._deserialize(json_data.get("Redshift")),
            S3=S3DestinationProperties._deserialize(json_data.get("S3")),
            Salesforce=SalesforceDestinationProperties._deserialize(json_data.get("Salesforce")),
            Snowflake=SnowflakeDestinationProperties._deserialize(json_data.get("Snowflake")),
            EventBridge=EventBridgeDestinationProperties._deserialize(json_data.get("EventBridge")),
            Upsolver=UpsolverDestinationProperties._deserialize(json_data.get("Upsolver")),
            LookoutMetrics=LookoutMetricsDestinationProperties._deserialize(json_data.get("LookoutMetrics")),
            Marketo=MarketoDestinationProperties._deserialize(json_data.get("Marketo")),
            Zendesk=ZendeskDestinationProperties._deserialize(json_data.get("Zendesk")),
            CustomConnector=CustomConnectorDestinationProperties._deserialize(json_data.get("CustomConnector")),
            SAPOData=SAPODataDestinationProperties._deserialize(json_data.get("SAPOData")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationConnectorProperties = DestinationConnectorProperties


@dataclass
class RedshiftDestinationProperties(BaseModel):
    Object: Optional[str]
    IntermediateBucketName: Optional[str]
    BucketPrefix: Optional[str]
    ErrorHandlingConfig: Optional["_ErrorHandlingConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_RedshiftDestinationProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedshiftDestinationProperties"]:
        if not json_data:
            return None
        return cls(
            Object=json_data.get("Object"),
            IntermediateBucketName=json_data.get("IntermediateBucketName"),
            BucketPrefix=json_data.get("BucketPrefix"),
            ErrorHandlingConfig=ErrorHandlingConfig._deserialize(json_data.get("ErrorHandlingConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedshiftDestinationProperties = RedshiftDestinationProperties


@dataclass
class ErrorHandlingConfig(BaseModel):
    FailOnFirstError: Optional[bool]
    BucketPrefix: Optional[str]
    BucketName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ErrorHandlingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ErrorHandlingConfig"]:
        if not json_data:
            return None
        return cls(
            FailOnFirstError=json_data.get("FailOnFirstError"),
            BucketPrefix=json_data.get("BucketPrefix"),
            BucketName=json_data.get("BucketName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ErrorHandlingConfig = ErrorHandlingConfig


@dataclass
class S3DestinationProperties(BaseModel):
    BucketName: Optional[str]
    BucketPrefix: Optional[str]
    S3OutputFormatConfig: Optional["_S3OutputFormatConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_S3DestinationProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3DestinationProperties"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            BucketPrefix=json_data.get("BucketPrefix"),
            S3OutputFormatConfig=S3OutputFormatConfig._deserialize(json_data.get("S3OutputFormatConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3DestinationProperties = S3DestinationProperties


@dataclass
class S3OutputFormatConfig(BaseModel):
    FileType: Optional[str]
    PrefixConfig: Optional["_PrefixConfig"]
    AggregationConfig: Optional["_AggregationConfig"]
    PreserveSourceDataTyping: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_S3OutputFormatConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3OutputFormatConfig"]:
        if not json_data:
            return None
        return cls(
            FileType=json_data.get("FileType"),
            PrefixConfig=PrefixConfig._deserialize(json_data.get("PrefixConfig")),
            AggregationConfig=AggregationConfig._deserialize(json_data.get("AggregationConfig")),
            PreserveSourceDataTyping=json_data.get("PreserveSourceDataTyping"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3OutputFormatConfig = S3OutputFormatConfig


@dataclass
class PrefixConfig(BaseModel):
    PrefixType: Optional[str]
    PrefixFormat: Optional[str]
    PathPrefixHierarchy: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PrefixConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrefixConfig"]:
        if not json_data:
            return None
        return cls(
            PrefixType=json_data.get("PrefixType"),
            PrefixFormat=json_data.get("PrefixFormat"),
            PathPrefixHierarchy=json_data.get("PathPrefixHierarchy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrefixConfig = PrefixConfig


@dataclass
class AggregationConfig(BaseModel):
    AggregationType: Optional[str]
    TargetFileSize: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AggregationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AggregationConfig"]:
        if not json_data:
            return None
        return cls(
            AggregationType=json_data.get("AggregationType"),
            TargetFileSize=json_data.get("TargetFileSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AggregationConfig = AggregationConfig


@dataclass
class SalesforceDestinationProperties(BaseModel):
    Object: Optional[str]
    ErrorHandlingConfig: Optional["_ErrorHandlingConfig"]
    IdFieldNames: Optional[Sequence[str]]
    WriteOperationType: Optional[str]
    DataTransferApi: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SalesforceDestinationProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SalesforceDestinationProperties"]:
        if not json_data:
            return None
        return cls(
            Object=json_data.get("Object"),
            ErrorHandlingConfig=ErrorHandlingConfig._deserialize(json_data.get("ErrorHandlingConfig")),
            IdFieldNames=json_data.get("IdFieldNames"),
            WriteOperationType=json_data.get("WriteOperationType"),
            DataTransferApi=json_data.get("DataTransferApi"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SalesforceDestinationProperties = SalesforceDestinationProperties


@dataclass
class SnowflakeDestinationProperties(BaseModel):
    Object: Optional[str]
    IntermediateBucketName: Optional[str]
    BucketPrefix: Optional[str]
    ErrorHandlingConfig: Optional["_ErrorHandlingConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_SnowflakeDestinationProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnowflakeDestinationProperties"]:
        if not json_data:
            return None
        return cls(
            Object=json_data.get("Object"),
            IntermediateBucketName=json_data.get("IntermediateBucketName"),
            BucketPrefix=json_data.get("BucketPrefix"),
            ErrorHandlingConfig=ErrorHandlingConfig._deserialize(json_data.get("ErrorHandlingConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnowflakeDestinationProperties = SnowflakeDestinationProperties


@dataclass
class EventBridgeDestinationProperties(BaseModel):
    Object: Optional[str]
    ErrorHandlingConfig: Optional["_ErrorHandlingConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_EventBridgeDestinationProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventBridgeDestinationProperties"]:
        if not json_data:
            return None
        return cls(
            Object=json_data.get("Object"),
            ErrorHandlingConfig=ErrorHandlingConfig._deserialize(json_data.get("ErrorHandlingConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventBridgeDestinationProperties = EventBridgeDestinationProperties


@dataclass
class UpsolverDestinationProperties(BaseModel):
    BucketName: Optional[str]
    BucketPrefix: Optional[str]
    S3OutputFormatConfig: Optional["_UpsolverS3OutputFormatConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_UpsolverDestinationProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpsolverDestinationProperties"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            BucketPrefix=json_data.get("BucketPrefix"),
            S3OutputFormatConfig=UpsolverS3OutputFormatConfig._deserialize(json_data.get("S3OutputFormatConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpsolverDestinationProperties = UpsolverDestinationProperties


@dataclass
class UpsolverS3OutputFormatConfig(BaseModel):
    FileType: Optional[str]
    PrefixConfig: Optional["_PrefixConfig"]
    AggregationConfig: Optional["_AggregationConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_UpsolverS3OutputFormatConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpsolverS3OutputFormatConfig"]:
        if not json_data:
            return None
        return cls(
            FileType=json_data.get("FileType"),
            PrefixConfig=PrefixConfig._deserialize(json_data.get("PrefixConfig")),
            AggregationConfig=AggregationConfig._deserialize(json_data.get("AggregationConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpsolverS3OutputFormatConfig = UpsolverS3OutputFormatConfig


@dataclass
class LookoutMetricsDestinationProperties(BaseModel):
    Object: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LookoutMetricsDestinationProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LookoutMetricsDestinationProperties"]:
        if not json_data:
            return None
        return cls(
            Object=json_data.get("Object"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LookoutMetricsDestinationProperties = LookoutMetricsDestinationProperties


@dataclass
class MarketoDestinationProperties(BaseModel):
    Object: Optional[str]
    ErrorHandlingConfig: Optional["_ErrorHandlingConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_MarketoDestinationProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarketoDestinationProperties"]:
        if not json_data:
            return None
        return cls(
            Object=json_data.get("Object"),
            ErrorHandlingConfig=ErrorHandlingConfig._deserialize(json_data.get("ErrorHandlingConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarketoDestinationProperties = MarketoDestinationProperties


@dataclass
class ZendeskDestinationProperties(BaseModel):
    Object: Optional[str]
    ErrorHandlingConfig: Optional["_ErrorHandlingConfig"]
    IdFieldNames: Optional[Sequence[str]]
    WriteOperationType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ZendeskDestinationProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZendeskDestinationProperties"]:
        if not json_data:
            return None
        return cls(
            Object=json_data.get("Object"),
            ErrorHandlingConfig=ErrorHandlingConfig._deserialize(json_data.get("ErrorHandlingConfig")),
            IdFieldNames=json_data.get("IdFieldNames"),
            WriteOperationType=json_data.get("WriteOperationType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZendeskDestinationProperties = ZendeskDestinationProperties


@dataclass
class CustomConnectorDestinationProperties(BaseModel):
    EntityName: Optional[str]
    ErrorHandlingConfig: Optional["_ErrorHandlingConfig"]
    WriteOperationType: Optional[str]
    IdFieldNames: Optional[Sequence[str]]
    CustomProperties: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomConnectorDestinationProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomConnectorDestinationProperties"]:
        if not json_data:
            return None
        return cls(
            EntityName=json_data.get("EntityName"),
            ErrorHandlingConfig=ErrorHandlingConfig._deserialize(json_data.get("ErrorHandlingConfig")),
            WriteOperationType=json_data.get("WriteOperationType"),
            IdFieldNames=json_data.get("IdFieldNames"),
            CustomProperties=json_data.get("CustomProperties"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomConnectorDestinationProperties = CustomConnectorDestinationProperties


@dataclass
class SAPODataDestinationProperties(BaseModel):
    ObjectPath: Optional[str]
    ErrorHandlingConfig: Optional["_ErrorHandlingConfig"]
    SuccessResponseHandlingConfig: Optional["_SuccessResponseHandlingConfig"]
    IdFieldNames: Optional[Sequence[str]]
    WriteOperationType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SAPODataDestinationProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SAPODataDestinationProperties"]:
        if not json_data:
            return None
        return cls(
            ObjectPath=json_data.get("ObjectPath"),
            ErrorHandlingConfig=ErrorHandlingConfig._deserialize(json_data.get("ErrorHandlingConfig")),
            SuccessResponseHandlingConfig=SuccessResponseHandlingConfig._deserialize(json_data.get("SuccessResponseHandlingConfig")),
            IdFieldNames=json_data.get("IdFieldNames"),
            WriteOperationType=json_data.get("WriteOperationType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SAPODataDestinationProperties = SAPODataDestinationProperties


@dataclass
class SuccessResponseHandlingConfig(BaseModel):
    BucketPrefix: Optional[str]
    BucketName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SuccessResponseHandlingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SuccessResponseHandlingConfig"]:
        if not json_data:
            return None
        return cls(
            BucketPrefix=json_data.get("BucketPrefix"),
            BucketName=json_data.get("BucketName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SuccessResponseHandlingConfig = SuccessResponseHandlingConfig


@dataclass
class Task(BaseModel):
    SourceFields: Optional[Sequence[str]]
    ConnectorOperator: Optional["_ConnectorOperator"]
    DestinationField: Optional[str]
    TaskType: Optional[str]
    TaskProperties: Optional[Sequence["_TaskPropertiesObject"]]

    @classmethod
    def _deserialize(
        cls: Type["_Task"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Task"]:
        if not json_data:
            return None
        return cls(
            SourceFields=json_data.get("SourceFields"),
            ConnectorOperator=ConnectorOperator._deserialize(json_data.get("ConnectorOperator")),
            DestinationField=json_data.get("DestinationField"),
            TaskType=json_data.get("TaskType"),
            TaskProperties=deserialize_list(json_data.get("TaskProperties"), TaskPropertiesObject),
        )


# work around possible type aliasing issues when variable has same name as a model
_Task = Task


@dataclass
class ConnectorOperator(BaseModel):
    Amplitude: Optional[str]
    Datadog: Optional[str]
    Dynatrace: Optional[str]
    GoogleAnalytics: Optional[str]
    InforNexus: Optional[str]
    Marketo: Optional[str]
    S3: Optional[str]
    SAPOData: Optional[str]
    Salesforce: Optional[str]
    Pardot: Optional[str]
    ServiceNow: Optional[str]
    Singular: Optional[str]
    Slack: Optional[str]
    Trendmicro: Optional[str]
    Veeva: Optional[str]
    Zendesk: Optional[str]
    CustomConnector: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectorOperator"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectorOperator"]:
        if not json_data:
            return None
        return cls(
            Amplitude=json_data.get("Amplitude"),
            Datadog=json_data.get("Datadog"),
            Dynatrace=json_data.get("Dynatrace"),
            GoogleAnalytics=json_data.get("GoogleAnalytics"),
            InforNexus=json_data.get("InforNexus"),
            Marketo=json_data.get("Marketo"),
            S3=json_data.get("S3"),
            SAPOData=json_data.get("SAPOData"),
            Salesforce=json_data.get("Salesforce"),
            Pardot=json_data.get("Pardot"),
            ServiceNow=json_data.get("ServiceNow"),
            Singular=json_data.get("Singular"),
            Slack=json_data.get("Slack"),
            Trendmicro=json_data.get("Trendmicro"),
            Veeva=json_data.get("Veeva"),
            Zendesk=json_data.get("Zendesk"),
            CustomConnector=json_data.get("CustomConnector"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectorOperator = ConnectorOperator


@dataclass
class TaskPropertiesObject(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaskPropertiesObject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskPropertiesObject"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskPropertiesObject = TaskPropertiesObject


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
class MetadataCatalogConfig(BaseModel):
    GlueDataCatalog: Optional["_GlueDataCatalog"]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataCatalogConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataCatalogConfig"]:
        if not json_data:
            return None
        return cls(
            GlueDataCatalog=GlueDataCatalog._deserialize(json_data.get("GlueDataCatalog")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataCatalogConfig = MetadataCatalogConfig


@dataclass
class GlueDataCatalog(BaseModel):
    RoleArn: Optional[str]
    DatabaseName: Optional[str]
    TablePrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GlueDataCatalog"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlueDataCatalog"]:
        if not json_data:
            return None
        return cls(
            RoleArn=json_data.get("RoleArn"),
            DatabaseName=json_data.get("DatabaseName"),
            TablePrefix=json_data.get("TablePrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlueDataCatalog = GlueDataCatalog


