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
class AwsCloudtrailEventdatastore(BaseModel):
    AdvancedEventSelectors: Optional[AbstractSet["_AdvancedEventSelector"]]
    CreatedTimestamp: Optional[str]
    EventDataStoreArn: Optional[str]
    MultiRegionEnabled: Optional[bool]
    Name: Optional[str]
    OrganizationEnabled: Optional[bool]
    RetentionPeriod: Optional[int]
    Status: Optional[str]
    TerminationProtectionEnabled: Optional[bool]
    UpdatedTimestamp: Optional[str]
    KmsKeyId: Optional[str]
    Tags: Optional[Any]
    IngestionEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudtrailEventdatastore"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudtrailEventdatastore"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AdvancedEventSelectors=set_or_none(json_data.get("AdvancedEventSelectors")),
            CreatedTimestamp=json_data.get("CreatedTimestamp"),
            EventDataStoreArn=json_data.get("EventDataStoreArn"),
            MultiRegionEnabled=json_data.get("MultiRegionEnabled"),
            Name=json_data.get("Name"),
            OrganizationEnabled=json_data.get("OrganizationEnabled"),
            RetentionPeriod=json_data.get("RetentionPeriod"),
            Status=json_data.get("Status"),
            TerminationProtectionEnabled=json_data.get("TerminationProtectionEnabled"),
            UpdatedTimestamp=json_data.get("UpdatedTimestamp"),
            KmsKeyId=json_data.get("KmsKeyId"),
            Tags=json_data.get("Tags"),
            IngestionEnabled=json_data.get("IngestionEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudtrailEventdatastore = AwsCloudtrailEventdatastore


@dataclass
class AdvancedEventSelector(BaseModel):
    Name: Optional[str]
    FieldSelectors: Optional[AbstractSet["_AdvancedFieldSelector"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedEventSelector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedEventSelector"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            FieldSelectors=set_or_none(json_data.get("FieldSelectors")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedEventSelector = AdvancedEventSelector


@dataclass
class AdvancedFieldSelector(BaseModel):
    Field: Optional[str]
    Equals: Optional[AbstractSet[str]]
    StartsWith: Optional[AbstractSet[str]]
    EndsWith: Optional[AbstractSet[str]]
    NotEquals: Optional[AbstractSet[str]]
    NotStartsWith: Optional[AbstractSet[str]]
    NotEndsWith: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AdvancedFieldSelector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdvancedFieldSelector"]:
        if not json_data:
            return None
        return cls(
            Field=json_data.get("Field"),
            Equals=set_or_none(json_data.get("Equals")),
            StartsWith=set_or_none(json_data.get("StartsWith")),
            EndsWith=set_or_none(json_data.get("EndsWith")),
            NotEquals=set_or_none(json_data.get("NotEquals")),
            NotStartsWith=set_or_none(json_data.get("NotStartsWith")),
            NotEndsWith=set_or_none(json_data.get("NotEndsWith")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdvancedFieldSelector = AdvancedFieldSelector


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


