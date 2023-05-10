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
class AwsDlmLifecyclepolicy(BaseModel):
    ExecutionRoleArn: Optional[str]
    Description: Optional[str]
    State: Optional[str]
    PolicyDetails: Optional["_PolicyDetails"]
    Id: Optional[str]
    Arn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDlmLifecyclepolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDlmLifecyclepolicy"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            Description=json_data.get("Description"),
            State=json_data.get("State"),
            PolicyDetails=PolicyDetails._deserialize(json_data.get("PolicyDetails")),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDlmLifecyclepolicy = AwsDlmLifecyclepolicy


@dataclass
class PolicyDetails(BaseModel):
    ResourceTypes: Optional[Sequence[str]]
    Schedules: Optional[Sequence["_Schedule"]]
    PolicyType: Optional[str]
    EventSource: Optional["_EventSource"]
    Parameters: Optional["_Parameters"]
    Actions: Optional[Sequence["_Action"]]
    TargetTags: Optional[Sequence["_Tag"]]
    ResourceLocations: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyDetails"]:
        if not json_data:
            return None
        return cls(
            ResourceTypes=json_data.get("ResourceTypes"),
            Schedules=deserialize_list(json_data.get("Schedules"), Schedule),
            PolicyType=json_data.get("PolicyType"),
            EventSource=EventSource._deserialize(json_data.get("EventSource")),
            Parameters=Parameters._deserialize(json_data.get("Parameters")),
            Actions=deserialize_list(json_data.get("Actions"), Action),
            TargetTags=deserialize_list(json_data.get("TargetTags"), Tag),
            ResourceLocations=json_data.get("ResourceLocations"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyDetails = PolicyDetails


@dataclass
class Schedule(BaseModel):
    ShareRules: Optional[Sequence["_ShareRule"]]
    DeprecateRule: Optional["_DeprecateRule"]
    TagsToAdd: Optional[Sequence["_Tag"]]
    CreateRule: Optional["_CreateRule"]
    VariableTags: Optional[Sequence["_Tag"]]
    FastRestoreRule: Optional["_FastRestoreRule"]
    ArchiveRule: Optional["_ArchiveRule"]
    RetainRule: Optional["_RetainRule"]
    CrossRegionCopyRules: Optional[Sequence["_CrossRegionCopyRule"]]
    Name: Optional[str]
    CopyTags: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Schedule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Schedule"]:
        if not json_data:
            return None
        return cls(
            ShareRules=deserialize_list(json_data.get("ShareRules"), ShareRule),
            DeprecateRule=DeprecateRule._deserialize(json_data.get("DeprecateRule")),
            TagsToAdd=deserialize_list(json_data.get("TagsToAdd"), Tag),
            CreateRule=CreateRule._deserialize(json_data.get("CreateRule")),
            VariableTags=deserialize_list(json_data.get("VariableTags"), Tag),
            FastRestoreRule=FastRestoreRule._deserialize(json_data.get("FastRestoreRule")),
            ArchiveRule=ArchiveRule._deserialize(json_data.get("ArchiveRule")),
            RetainRule=RetainRule._deserialize(json_data.get("RetainRule")),
            CrossRegionCopyRules=deserialize_list(json_data.get("CrossRegionCopyRules"), CrossRegionCopyRule),
            Name=json_data.get("Name"),
            CopyTags=json_data.get("CopyTags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Schedule = Schedule


@dataclass
class ShareRule(BaseModel):
    TargetAccounts: Optional[Sequence[str]]
    UnshareIntervalUnit: Optional[str]
    UnshareInterval: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ShareRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShareRule"]:
        if not json_data:
            return None
        return cls(
            TargetAccounts=json_data.get("TargetAccounts"),
            UnshareIntervalUnit=json_data.get("UnshareIntervalUnit"),
            UnshareInterval=json_data.get("UnshareInterval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShareRule = ShareRule


@dataclass
class DeprecateRule(BaseModel):
    IntervalUnit: Optional[str]
    Count: Optional[int]
    Interval: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_DeprecateRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeprecateRule"]:
        if not json_data:
            return None
        return cls(
            IntervalUnit=json_data.get("IntervalUnit"),
            Count=json_data.get("Count"),
            Interval=json_data.get("Interval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeprecateRule = DeprecateRule


@dataclass
class Tag(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


@dataclass
class CreateRule(BaseModel):
    IntervalUnit: Optional[str]
    CronExpression: Optional[str]
    Times: Optional[Sequence[str]]
    Interval: Optional[int]
    Location: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CreateRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CreateRule"]:
        if not json_data:
            return None
        return cls(
            IntervalUnit=json_data.get("IntervalUnit"),
            CronExpression=json_data.get("CronExpression"),
            Times=json_data.get("Times"),
            Interval=json_data.get("Interval"),
            Location=json_data.get("Location"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CreateRule = CreateRule


@dataclass
class FastRestoreRule(BaseModel):
    IntervalUnit: Optional[str]
    Count: Optional[int]
    AvailabilityZones: Optional[Sequence[str]]
    Interval: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_FastRestoreRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FastRestoreRule"]:
        if not json_data:
            return None
        return cls(
            IntervalUnit=json_data.get("IntervalUnit"),
            Count=json_data.get("Count"),
            AvailabilityZones=json_data.get("AvailabilityZones"),
            Interval=json_data.get("Interval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FastRestoreRule = FastRestoreRule


@dataclass
class ArchiveRule(BaseModel):
    RetainRule: Optional["_ArchiveRetainRule"]

    @classmethod
    def _deserialize(
        cls: Type["_ArchiveRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArchiveRule"]:
        if not json_data:
            return None
        return cls(
            RetainRule=ArchiveRetainRule._deserialize(json_data.get("RetainRule")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArchiveRule = ArchiveRule


@dataclass
class ArchiveRetainRule(BaseModel):
    RetentionArchiveTier: Optional["_RetentionArchiveTier"]

    @classmethod
    def _deserialize(
        cls: Type["_ArchiveRetainRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ArchiveRetainRule"]:
        if not json_data:
            return None
        return cls(
            RetentionArchiveTier=RetentionArchiveTier._deserialize(json_data.get("RetentionArchiveTier")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ArchiveRetainRule = ArchiveRetainRule


@dataclass
class RetentionArchiveTier(BaseModel):
    IntervalUnit: Optional[str]
    Count: Optional[int]
    Interval: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionArchiveTier"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionArchiveTier"]:
        if not json_data:
            return None
        return cls(
            IntervalUnit=json_data.get("IntervalUnit"),
            Count=json_data.get("Count"),
            Interval=json_data.get("Interval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionArchiveTier = RetentionArchiveTier


@dataclass
class RetainRule(BaseModel):
    IntervalUnit: Optional[str]
    Count: Optional[int]
    Interval: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_RetainRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetainRule"]:
        if not json_data:
            return None
        return cls(
            IntervalUnit=json_data.get("IntervalUnit"),
            Count=json_data.get("Count"),
            Interval=json_data.get("Interval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetainRule = RetainRule


@dataclass
class CrossRegionCopyRule(BaseModel):
    TargetRegion: Optional[str]
    Target: Optional[str]
    DeprecateRule: Optional["_CrossRegionCopyDeprecateRule"]
    Encrypted: Optional[bool]
    CmkArn: Optional[str]
    RetainRule: Optional["_CrossRegionCopyRetainRule"]
    CopyTags: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CrossRegionCopyRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CrossRegionCopyRule"]:
        if not json_data:
            return None
        return cls(
            TargetRegion=json_data.get("TargetRegion"),
            Target=json_data.get("Target"),
            DeprecateRule=CrossRegionCopyDeprecateRule._deserialize(json_data.get("DeprecateRule")),
            Encrypted=json_data.get("Encrypted"),
            CmkArn=json_data.get("CmkArn"),
            RetainRule=CrossRegionCopyRetainRule._deserialize(json_data.get("RetainRule")),
            CopyTags=json_data.get("CopyTags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CrossRegionCopyRule = CrossRegionCopyRule


@dataclass
class CrossRegionCopyDeprecateRule(BaseModel):
    IntervalUnit: Optional[str]
    Interval: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_CrossRegionCopyDeprecateRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CrossRegionCopyDeprecateRule"]:
        if not json_data:
            return None
        return cls(
            IntervalUnit=json_data.get("IntervalUnit"),
            Interval=json_data.get("Interval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CrossRegionCopyDeprecateRule = CrossRegionCopyDeprecateRule


@dataclass
class CrossRegionCopyRetainRule(BaseModel):
    IntervalUnit: Optional[str]
    Interval: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_CrossRegionCopyRetainRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CrossRegionCopyRetainRule"]:
        if not json_data:
            return None
        return cls(
            IntervalUnit=json_data.get("IntervalUnit"),
            Interval=json_data.get("Interval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CrossRegionCopyRetainRule = CrossRegionCopyRetainRule


@dataclass
class EventSource(BaseModel):
    Type: Optional[str]
    Parameters: Optional["_EventParameters"]

    @classmethod
    def _deserialize(
        cls: Type["_EventSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventSource"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Parameters=EventParameters._deserialize(json_data.get("Parameters")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventSource = EventSource


@dataclass
class EventParameters(BaseModel):
    DescriptionRegex: Optional[str]
    EventType: Optional[str]
    SnapshotOwner: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_EventParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventParameters"]:
        if not json_data:
            return None
        return cls(
            DescriptionRegex=json_data.get("DescriptionRegex"),
            EventType=json_data.get("EventType"),
            SnapshotOwner=json_data.get("SnapshotOwner"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventParameters = EventParameters


@dataclass
class Parameters(BaseModel):
    ExcludeBootVolume: Optional[bool]
    NoReboot: Optional[bool]
    ExcludeDataVolumeTags: Optional[Sequence["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_Parameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Parameters"]:
        if not json_data:
            return None
        return cls(
            ExcludeBootVolume=json_data.get("ExcludeBootVolume"),
            NoReboot=json_data.get("NoReboot"),
            ExcludeDataVolumeTags=deserialize_list(json_data.get("ExcludeDataVolumeTags"), Tag),
        )


# work around possible type aliasing issues when variable has same name as a model
_Parameters = Parameters


@dataclass
class Action(BaseModel):
    CrossRegionCopy: Optional[Sequence["_CrossRegionCopyAction"]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            CrossRegionCopy=deserialize_list(json_data.get("CrossRegionCopy"), CrossRegionCopyAction),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class CrossRegionCopyAction(BaseModel):
    Target: Optional[str]
    EncryptionConfiguration: Optional["_EncryptionConfiguration"]
    RetainRule: Optional["_CrossRegionCopyRetainRule"]

    @classmethod
    def _deserialize(
        cls: Type["_CrossRegionCopyAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CrossRegionCopyAction"]:
        if not json_data:
            return None
        return cls(
            Target=json_data.get("Target"),
            EncryptionConfiguration=EncryptionConfiguration._deserialize(json_data.get("EncryptionConfiguration")),
            RetainRule=CrossRegionCopyRetainRule._deserialize(json_data.get("RetainRule")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CrossRegionCopyAction = CrossRegionCopyAction


@dataclass
class EncryptionConfiguration(BaseModel):
    Encrypted: Optional[bool]
    CmkArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EncryptionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EncryptionConfiguration"]:
        if not json_data:
            return None
        return cls(
            Encrypted=json_data.get("Encrypted"),
            CmkArn=json_data.get("CmkArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EncryptionConfiguration = EncryptionConfiguration


