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
class AwsIotanalyticsDataset(BaseModel):
    Actions: Optional[Sequence["_Action"]]
    LateDataRules: Optional[Sequence["_LateDataRule"]]
    DatasetName: Optional[str]
    ContentDeliveryRules: Optional[Sequence["_DatasetContentDeliveryRule"]]
    Triggers: Optional[Sequence["_Trigger"]]
    VersioningConfiguration: Optional["_VersioningConfiguration"]
    Id: Optional[str]
    RetentionPeriod: Optional["_RetentionPeriod"]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotanalyticsDataset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotanalyticsDataset"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Actions=deserialize_list(json_data.get("Actions"), Action),
            LateDataRules=deserialize_list(json_data.get("LateDataRules"), LateDataRule),
            DatasetName=json_data.get("DatasetName"),
            ContentDeliveryRules=deserialize_list(json_data.get("ContentDeliveryRules"), DatasetContentDeliveryRule),
            Triggers=deserialize_list(json_data.get("Triggers"), Trigger),
            VersioningConfiguration=VersioningConfiguration._deserialize(json_data.get("VersioningConfiguration")),
            Id=json_data.get("Id"),
            RetentionPeriod=RetentionPeriod._deserialize(json_data.get("RetentionPeriod")),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotanalyticsDataset = AwsIotanalyticsDataset


@dataclass
class Action(BaseModel):
    ActionName: Optional[str]
    ContainerAction: Optional["_ContainerAction"]
    QueryAction: Optional["_QueryAction"]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            ActionName=json_data.get("ActionName"),
            ContainerAction=ContainerAction._deserialize(json_data.get("ContainerAction")),
            QueryAction=QueryAction._deserialize(json_data.get("QueryAction")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class ContainerAction(BaseModel):
    Variables: Optional[Sequence["_Variable"]]
    ExecutionRoleArn: Optional[str]
    Image: Optional[str]
    ResourceConfiguration: Optional["_ResourceConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerAction"]:
        if not json_data:
            return None
        return cls(
            Variables=deserialize_list(json_data.get("Variables"), Variable),
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            Image=json_data.get("Image"),
            ResourceConfiguration=ResourceConfiguration._deserialize(json_data.get("ResourceConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerAction = ContainerAction


@dataclass
class Variable(BaseModel):
    VariableName: Optional[str]
    DatasetContentVersionValue: Optional["_DatasetContentVersionValue"]
    StringValue: Optional[str]
    DoubleValue: Optional[float]
    OutputFileUriValue: Optional["_OutputFileUriValue"]

    @classmethod
    def _deserialize(
        cls: Type["_Variable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Variable"]:
        if not json_data:
            return None
        return cls(
            VariableName=json_data.get("VariableName"),
            DatasetContentVersionValue=DatasetContentVersionValue._deserialize(json_data.get("DatasetContentVersionValue")),
            StringValue=json_data.get("StringValue"),
            DoubleValue=json_data.get("DoubleValue"),
            OutputFileUriValue=OutputFileUriValue._deserialize(json_data.get("OutputFileUriValue")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Variable = Variable


@dataclass
class DatasetContentVersionValue(BaseModel):
    DatasetName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatasetContentVersionValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatasetContentVersionValue"]:
        if not json_data:
            return None
        return cls(
            DatasetName=json_data.get("DatasetName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatasetContentVersionValue = DatasetContentVersionValue


@dataclass
class OutputFileUriValue(BaseModel):
    FileName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OutputFileUriValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OutputFileUriValue"]:
        if not json_data:
            return None
        return cls(
            FileName=json_data.get("FileName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OutputFileUriValue = OutputFileUriValue


@dataclass
class ResourceConfiguration(BaseModel):
    VolumeSizeInGB: Optional[int]
    ComputeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceConfiguration"]:
        if not json_data:
            return None
        return cls(
            VolumeSizeInGB=json_data.get("VolumeSizeInGB"),
            ComputeType=json_data.get("ComputeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceConfiguration = ResourceConfiguration


@dataclass
class QueryAction(BaseModel):
    Filters: Optional[Sequence["_Filter"]]
    SqlQuery: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QueryAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryAction"]:
        if not json_data:
            return None
        return cls(
            Filters=deserialize_list(json_data.get("Filters"), Filter),
            SqlQuery=json_data.get("SqlQuery"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryAction = QueryAction


@dataclass
class Filter(BaseModel):
    DeltaTime: Optional["_DeltaTime"]

    @classmethod
    def _deserialize(
        cls: Type["_Filter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filter"]:
        if not json_data:
            return None
        return cls(
            DeltaTime=DeltaTime._deserialize(json_data.get("DeltaTime")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Filter = Filter


@dataclass
class DeltaTime(BaseModel):
    OffsetSeconds: Optional[int]
    TimeExpression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeltaTime"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeltaTime"]:
        if not json_data:
            return None
        return cls(
            OffsetSeconds=json_data.get("OffsetSeconds"),
            TimeExpression=json_data.get("TimeExpression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeltaTime = DeltaTime


@dataclass
class LateDataRule(BaseModel):
    RuleConfiguration: Optional["_LateDataRuleConfiguration"]
    RuleName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LateDataRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LateDataRule"]:
        if not json_data:
            return None
        return cls(
            RuleConfiguration=LateDataRuleConfiguration._deserialize(json_data.get("RuleConfiguration")),
            RuleName=json_data.get("RuleName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LateDataRule = LateDataRule


@dataclass
class LateDataRuleConfiguration(BaseModel):
    DeltaTimeSessionWindowConfiguration: Optional["_DeltaTimeSessionWindowConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_LateDataRuleConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LateDataRuleConfiguration"]:
        if not json_data:
            return None
        return cls(
            DeltaTimeSessionWindowConfiguration=DeltaTimeSessionWindowConfiguration._deserialize(json_data.get("DeltaTimeSessionWindowConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LateDataRuleConfiguration = LateDataRuleConfiguration


@dataclass
class DeltaTimeSessionWindowConfiguration(BaseModel):
    TimeoutInMinutes: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_DeltaTimeSessionWindowConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeltaTimeSessionWindowConfiguration"]:
        if not json_data:
            return None
        return cls(
            TimeoutInMinutes=json_data.get("TimeoutInMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeltaTimeSessionWindowConfiguration = DeltaTimeSessionWindowConfiguration


@dataclass
class DatasetContentDeliveryRule(BaseModel):
    Destination: Optional["_DatasetContentDeliveryRuleDestination"]
    EntryName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DatasetContentDeliveryRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatasetContentDeliveryRule"]:
        if not json_data:
            return None
        return cls(
            Destination=DatasetContentDeliveryRuleDestination._deserialize(json_data.get("Destination")),
            EntryName=json_data.get("EntryName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatasetContentDeliveryRule = DatasetContentDeliveryRule


@dataclass
class DatasetContentDeliveryRuleDestination(BaseModel):
    IotEventsDestinationConfiguration: Optional["_IotEventsDestinationConfiguration"]
    S3DestinationConfiguration: Optional["_S3DestinationConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_DatasetContentDeliveryRuleDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DatasetContentDeliveryRuleDestination"]:
        if not json_data:
            return None
        return cls(
            IotEventsDestinationConfiguration=IotEventsDestinationConfiguration._deserialize(json_data.get("IotEventsDestinationConfiguration")),
            S3DestinationConfiguration=S3DestinationConfiguration._deserialize(json_data.get("S3DestinationConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DatasetContentDeliveryRuleDestination = DatasetContentDeliveryRuleDestination


@dataclass
class IotEventsDestinationConfiguration(BaseModel):
    InputName: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IotEventsDestinationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IotEventsDestinationConfiguration"]:
        if not json_data:
            return None
        return cls(
            InputName=json_data.get("InputName"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IotEventsDestinationConfiguration = IotEventsDestinationConfiguration


@dataclass
class S3DestinationConfiguration(BaseModel):
    GlueConfiguration: Optional["_GlueConfiguration"]
    Bucket: Optional[str]
    Key: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3DestinationConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3DestinationConfiguration"]:
        if not json_data:
            return None
        return cls(
            GlueConfiguration=GlueConfiguration._deserialize(json_data.get("GlueConfiguration")),
            Bucket=json_data.get("Bucket"),
            Key=json_data.get("Key"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3DestinationConfiguration = S3DestinationConfiguration


@dataclass
class GlueConfiguration(BaseModel):
    DatabaseName: Optional[str]
    TableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GlueConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlueConfiguration"]:
        if not json_data:
            return None
        return cls(
            DatabaseName=json_data.get("DatabaseName"),
            TableName=json_data.get("TableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlueConfiguration = GlueConfiguration


@dataclass
class Trigger(BaseModel):
    TriggeringDataset: Optional["_TriggeringDataset"]
    Schedule: Optional["_Schedule"]

    @classmethod
    def _deserialize(
        cls: Type["_Trigger"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Trigger"]:
        if not json_data:
            return None
        return cls(
            TriggeringDataset=TriggeringDataset._deserialize(json_data.get("TriggeringDataset")),
            Schedule=Schedule._deserialize(json_data.get("Schedule")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Trigger = Trigger


@dataclass
class TriggeringDataset(BaseModel):
    DatasetName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TriggeringDataset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TriggeringDataset"]:
        if not json_data:
            return None
        return cls(
            DatasetName=json_data.get("DatasetName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TriggeringDataset = TriggeringDataset


@dataclass
class Schedule(BaseModel):
    ScheduleExpression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Schedule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Schedule"]:
        if not json_data:
            return None
        return cls(
            ScheduleExpression=json_data.get("ScheduleExpression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Schedule = Schedule


@dataclass
class VersioningConfiguration(BaseModel):
    Unlimited: Optional[bool]
    MaxVersions: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_VersioningConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersioningConfiguration"]:
        if not json_data:
            return None
        return cls(
            Unlimited=json_data.get("Unlimited"),
            MaxVersions=json_data.get("MaxVersions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersioningConfiguration = VersioningConfiguration


@dataclass
class RetentionPeriod(BaseModel):
    NumberOfDays: Optional[int]
    Unlimited: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionPeriod"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionPeriod"]:
        if not json_data:
            return None
        return cls(
            NumberOfDays=json_data.get("NumberOfDays"),
            Unlimited=json_data.get("Unlimited"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionPeriod = RetentionPeriod


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


