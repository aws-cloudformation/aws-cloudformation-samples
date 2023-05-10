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
class AwsApplicationinsightsApplication(BaseModel):
    ResourceGroupName: Optional[str]
    ApplicationARN: Optional[str]
    CWEMonitorEnabled: Optional[bool]
    OpsCenterEnabled: Optional[bool]
    OpsItemSNSTopicArn: Optional[str]
    Tags: Optional[Any]
    CustomComponents: Optional[Sequence["_CustomComponent"]]
    LogPatternSets: Optional[Sequence["_LogPatternSet"]]
    AutoConfigurationEnabled: Optional[bool]
    ComponentMonitoringSettings: Optional[Sequence["_ComponentMonitoringSetting"]]
    GroupingType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApplicationinsightsApplication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApplicationinsightsApplication"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ApplicationARN=json_data.get("ApplicationARN"),
            CWEMonitorEnabled=json_data.get("CWEMonitorEnabled"),
            OpsCenterEnabled=json_data.get("OpsCenterEnabled"),
            OpsItemSNSTopicArn=json_data.get("OpsItemSNSTopicArn"),
            Tags=json_data.get("Tags"),
            CustomComponents=deserialize_list(json_data.get("CustomComponents"), CustomComponent),
            LogPatternSets=deserialize_list(json_data.get("LogPatternSets"), LogPatternSet),
            AutoConfigurationEnabled=json_data.get("AutoConfigurationEnabled"),
            ComponentMonitoringSettings=deserialize_list(json_data.get("ComponentMonitoringSettings"), ComponentMonitoringSetting),
            GroupingType=json_data.get("GroupingType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApplicationinsightsApplication = AwsApplicationinsightsApplication


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
class CustomComponent(BaseModel):
    ComponentName: Optional[str]
    ResourceList: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomComponent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomComponent"]:
        if not json_data:
            return None
        return cls(
            ComponentName=json_data.get("ComponentName"),
            ResourceList=json_data.get("ResourceList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomComponent = CustomComponent


@dataclass
class LogPatternSet(BaseModel):
    PatternSetName: Optional[str]
    LogPatterns: Optional[Sequence["_LogPattern"]]

    @classmethod
    def _deserialize(
        cls: Type["_LogPatternSet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogPatternSet"]:
        if not json_data:
            return None
        return cls(
            PatternSetName=json_data.get("PatternSetName"),
            LogPatterns=deserialize_list(json_data.get("LogPatterns"), LogPattern),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogPatternSet = LogPatternSet


@dataclass
class LogPattern(BaseModel):
    PatternName: Optional[str]
    Pattern: Optional[str]
    Rank: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_LogPattern"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogPattern"]:
        if not json_data:
            return None
        return cls(
            PatternName=json_data.get("PatternName"),
            Pattern=json_data.get("Pattern"),
            Rank=json_data.get("Rank"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogPattern = LogPattern


@dataclass
class ComponentMonitoringSetting(BaseModel):
    ComponentName: Optional[str]
    ComponentARN: Optional[str]
    Tier: Optional[str]
    ComponentConfigurationMode: Optional[str]
    DefaultOverwriteComponentConfiguration: Optional["_ComponentConfiguration"]
    CustomComponentConfiguration: Optional["_ComponentConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentMonitoringSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentMonitoringSetting"]:
        if not json_data:
            return None
        return cls(
            ComponentName=json_data.get("ComponentName"),
            ComponentARN=json_data.get("ComponentARN"),
            Tier=json_data.get("Tier"),
            ComponentConfigurationMode=json_data.get("ComponentConfigurationMode"),
            DefaultOverwriteComponentConfiguration=ComponentConfiguration._deserialize(json_data.get("DefaultOverwriteComponentConfiguration")),
            CustomComponentConfiguration=ComponentConfiguration._deserialize(json_data.get("CustomComponentConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentMonitoringSetting = ComponentMonitoringSetting


@dataclass
class ComponentConfiguration(BaseModel):
    ConfigurationDetails: Optional["_ConfigurationDetails"]
    SubComponentTypeConfigurations: Optional[Sequence["_SubComponentTypeConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentConfiguration"]:
        if not json_data:
            return None
        return cls(
            ConfigurationDetails=ConfigurationDetails._deserialize(json_data.get("ConfigurationDetails")),
            SubComponentTypeConfigurations=deserialize_list(json_data.get("SubComponentTypeConfigurations"), SubComponentTypeConfiguration),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentConfiguration = ComponentConfiguration


@dataclass
class ConfigurationDetails(BaseModel):
    AlarmMetrics: Optional[Sequence["_AlarmMetric"]]
    Logs: Optional[Sequence["_Log"]]
    WindowsEvents: Optional[Sequence["_WindowsEvent"]]
    Alarms: Optional[Sequence["_Alarm"]]
    JMXPrometheusExporter: Optional["_JMXPrometheusExporter"]
    HANAPrometheusExporter: Optional["_HANAPrometheusExporter"]
    HAClusterPrometheusExporter: Optional["_HAClusterPrometheusExporter"]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationDetails"]:
        if not json_data:
            return None
        return cls(
            AlarmMetrics=deserialize_list(json_data.get("AlarmMetrics"), AlarmMetric),
            Logs=deserialize_list(json_data.get("Logs"), Log),
            WindowsEvents=deserialize_list(json_data.get("WindowsEvents"), WindowsEvent),
            Alarms=deserialize_list(json_data.get("Alarms"), Alarm),
            JMXPrometheusExporter=JMXPrometheusExporter._deserialize(json_data.get("JMXPrometheusExporter")),
            HANAPrometheusExporter=HANAPrometheusExporter._deserialize(json_data.get("HANAPrometheusExporter")),
            HAClusterPrometheusExporter=HAClusterPrometheusExporter._deserialize(json_data.get("HAClusterPrometheusExporter")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationDetails = ConfigurationDetails


@dataclass
class AlarmMetric(BaseModel):
    AlarmMetricName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AlarmMetric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlarmMetric"]:
        if not json_data:
            return None
        return cls(
            AlarmMetricName=json_data.get("AlarmMetricName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlarmMetric = AlarmMetric


@dataclass
class Log(BaseModel):
    LogGroupName: Optional[str]
    LogPath: Optional[str]
    LogType: Optional[str]
    Encoding: Optional[str]
    PatternSet: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Log"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Log"]:
        if not json_data:
            return None
        return cls(
            LogGroupName=json_data.get("LogGroupName"),
            LogPath=json_data.get("LogPath"),
            LogType=json_data.get("LogType"),
            Encoding=json_data.get("Encoding"),
            PatternSet=json_data.get("PatternSet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Log = Log


@dataclass
class WindowsEvent(BaseModel):
    LogGroupName: Optional[str]
    EventName: Optional[str]
    EventLevels: Optional[Sequence[str]]
    PatternSet: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WindowsEvent"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WindowsEvent"]:
        if not json_data:
            return None
        return cls(
            LogGroupName=json_data.get("LogGroupName"),
            EventName=json_data.get("EventName"),
            EventLevels=json_data.get("EventLevels"),
            PatternSet=json_data.get("PatternSet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WindowsEvent = WindowsEvent


@dataclass
class Alarm(BaseModel):
    AlarmName: Optional[str]
    Severity: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Alarm"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Alarm"]:
        if not json_data:
            return None
        return cls(
            AlarmName=json_data.get("AlarmName"),
            Severity=json_data.get("Severity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Alarm = Alarm


@dataclass
class JMXPrometheusExporter(BaseModel):
    JMXURL: Optional[str]
    HostPort: Optional[str]
    PrometheusPort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JMXPrometheusExporter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JMXPrometheusExporter"]:
        if not json_data:
            return None
        return cls(
            JMXURL=json_data.get("JMXURL"),
            HostPort=json_data.get("HostPort"),
            PrometheusPort=json_data.get("PrometheusPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JMXPrometheusExporter = JMXPrometheusExporter


@dataclass
class HANAPrometheusExporter(BaseModel):
    HANASID: Optional[str]
    HANAPort: Optional[str]
    HANASecretName: Optional[str]
    AgreeToInstallHANADBClient: Optional[bool]
    PrometheusPort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HANAPrometheusExporter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HANAPrometheusExporter"]:
        if not json_data:
            return None
        return cls(
            HANASID=json_data.get("HANASID"),
            HANAPort=json_data.get("HANAPort"),
            HANASecretName=json_data.get("HANASecretName"),
            AgreeToInstallHANADBClient=json_data.get("AgreeToInstallHANADBClient"),
            PrometheusPort=json_data.get("PrometheusPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HANAPrometheusExporter = HANAPrometheusExporter


@dataclass
class HAClusterPrometheusExporter(BaseModel):
    PrometheusPort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HAClusterPrometheusExporter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HAClusterPrometheusExporter"]:
        if not json_data:
            return None
        return cls(
            PrometheusPort=json_data.get("PrometheusPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HAClusterPrometheusExporter = HAClusterPrometheusExporter


@dataclass
class SubComponentTypeConfiguration(BaseModel):
    SubComponentType: Optional[str]
    SubComponentConfigurationDetails: Optional["_SubComponentConfigurationDetails"]

    @classmethod
    def _deserialize(
        cls: Type["_SubComponentTypeConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubComponentTypeConfiguration"]:
        if not json_data:
            return None
        return cls(
            SubComponentType=json_data.get("SubComponentType"),
            SubComponentConfigurationDetails=SubComponentConfigurationDetails._deserialize(json_data.get("SubComponentConfigurationDetails")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubComponentTypeConfiguration = SubComponentTypeConfiguration


@dataclass
class SubComponentConfigurationDetails(BaseModel):
    AlarmMetrics: Optional[Sequence["_AlarmMetric"]]
    Logs: Optional[Sequence["_Log"]]
    WindowsEvents: Optional[Sequence["_WindowsEvent"]]

    @classmethod
    def _deserialize(
        cls: Type["_SubComponentConfigurationDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubComponentConfigurationDetails"]:
        if not json_data:
            return None
        return cls(
            AlarmMetrics=deserialize_list(json_data.get("AlarmMetrics"), AlarmMetric),
            Logs=deserialize_list(json_data.get("Logs"), Log),
            WindowsEvents=deserialize_list(json_data.get("WindowsEvents"), WindowsEvent),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubComponentConfigurationDetails = SubComponentConfigurationDetails


