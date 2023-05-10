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
class AwsRumAppmonitor(BaseModel):
    Id: Optional[str]
    Name: Optional[str]
    Domain: Optional[str]
    CwLogEnabled: Optional[bool]
    Tags: Optional[Any]
    AppMonitorConfiguration: Optional["_AppMonitorConfiguration"]
    CustomEvents: Optional["_CustomEvents"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRumAppmonitor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRumAppmonitor"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Domain=json_data.get("Domain"),
            CwLogEnabled=json_data.get("CwLogEnabled"),
            Tags=json_data.get("Tags"),
            AppMonitorConfiguration=AppMonitorConfiguration._deserialize(json_data.get("AppMonitorConfiguration")),
            CustomEvents=CustomEvents._deserialize(json_data.get("CustomEvents")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRumAppmonitor = AwsRumAppmonitor


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
class AppMonitorConfiguration(BaseModel):
    IdentityPoolId: Optional[str]
    ExcludedPages: Optional[Sequence[str]]
    IncludedPages: Optional[Sequence[str]]
    FavoritePages: Optional[Sequence[str]]
    SessionSampleRate: Optional[float]
    GuestRoleArn: Optional[str]
    AllowCookies: Optional[bool]
    Telemetries: Optional[Sequence[str]]
    EnableXRay: Optional[bool]
    MetricDestinations: Optional[AbstractSet["_MetricDestination"]]

    @classmethod
    def _deserialize(
        cls: Type["_AppMonitorConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppMonitorConfiguration"]:
        if not json_data:
            return None
        return cls(
            IdentityPoolId=json_data.get("IdentityPoolId"),
            ExcludedPages=json_data.get("ExcludedPages"),
            IncludedPages=json_data.get("IncludedPages"),
            FavoritePages=json_data.get("FavoritePages"),
            SessionSampleRate=json_data.get("SessionSampleRate"),
            GuestRoleArn=json_data.get("GuestRoleArn"),
            AllowCookies=json_data.get("AllowCookies"),
            Telemetries=json_data.get("Telemetries"),
            EnableXRay=json_data.get("EnableXRay"),
            MetricDestinations=set_or_none(json_data.get("MetricDestinations")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppMonitorConfiguration = AppMonitorConfiguration


@dataclass
class MetricDestination(BaseModel):
    Destination: Optional[str]
    DestinationArn: Optional[str]
    IamRoleArn: Optional[str]
    MetricDefinitions: Optional[AbstractSet["_MetricDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDestination"]:
        if not json_data:
            return None
        return cls(
            Destination=json_data.get("Destination"),
            DestinationArn=json_data.get("DestinationArn"),
            IamRoleArn=json_data.get("IamRoleArn"),
            MetricDefinitions=set_or_none(json_data.get("MetricDefinitions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDestination = MetricDestination


@dataclass
class MetricDefinition(BaseModel):
    Name: Optional[str]
    Namespace: Optional[str]
    ValueKey: Optional[str]
    UnitLabel: Optional[str]
    DimensionKeys: Optional[MutableMapping[str, str]]
    EventPattern: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Namespace=json_data.get("Namespace"),
            ValueKey=json_data.get("ValueKey"),
            UnitLabel=json_data.get("UnitLabel"),
            DimensionKeys=json_data.get("DimensionKeys"),
            EventPattern=json_data.get("EventPattern"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricDefinition = MetricDefinition


@dataclass
class CustomEvents(BaseModel):
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomEvents"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomEvents"]:
        if not json_data:
            return None
        return cls(
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomEvents = CustomEvents


